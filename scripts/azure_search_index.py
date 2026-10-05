#!/usr/bin/env python3
"""Index policy-navigator claim cards into Azure AI Search.

Parses every ``claims/claim-####.md`` file (one Markdown body + a trailing fenced ```yaml```
block), resolves its cited sources against ``sources/source-####.md`` frontmatter, generates an
embedding per claim via an Azure OpenAI embedding deployment, and upserts the result into the
Azure AI Search index defined in ``infra/search-index-schema.json``.

Claims whose only resolved source(s) are the two permanently-restricted documents
(source-0024 — Kanoa population-shifts deck, source-0045 — Treasury "Auckland Story") are still
indexed (so retrieval doesn't silently drop evidence) but flagged with ``is_restricted_source``.
Any downstream grounding configuration (Phase 2 Copilot Studio agent) must honour that flag.

Auth is via ``DefaultAzureCredential`` throughout: works with ``az login`` locally and with the
GitHub Actions OIDC federated identity in CI (see .github/workflows/index-claims.yml). No API
keys are read, stored, or required.

Usage:
    python scripts/azure_search_index.py --full
    python scripts/azure_search_index.py --since <git-ref>
    python scripts/azure_search_index.py --full --dry-run

Required environment variables (see docs/AZURE_RAG_SETUP.md):
    SEARCH_ENDPOINT                    e.g. https://policynav-search.search.windows.net
    AZURE_OPENAI_ENDPOINT              e.g. https://policynav-openai.openai.azure.com
    AZURE_OPENAI_EMBEDDING_DEPLOYMENT  defaults to "text-embedding-3-large"
    SEARCH_INDEX_NAME                  defaults to "policynav-claims-index"
"""
from __future__ import annotations

import argparse
import datetime
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

import requests
import yaml
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from azure.search.documents import SearchClient

REPO_ROOT = Path(__file__).resolve().parent.parent
CLAIMS_DIR = REPO_ROOT / "claims"
SOURCES_DIR = REPO_ROOT / "sources"
SCHEMA_PATH = REPO_ROOT / "infra" / "search-index-schema.json"

SEARCH_API_VERSION = "2024-07-01"
OPENAI_API_VERSION = "2024-06-01"
GITHUB_BLOB_BASE = "https://github.com/shobhitb19/policy-navigator/blob/main"

RESTRICTED_SOURCE_IDS = {"source-0024", "source-0045"}

YAML_BLOCK_RE = re.compile(r"```yaml\n(.*?)```", re.DOTALL)
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL | re.MULTILINE)
HEADING_RE = re.compile(r"^#\s+claim-\d+\s*$", re.MULTILINE)
QUALIFIERS_HEADER_RE = re.compile(r"\*\*Qualifiers:\*\*\s*\n((?:-.*\n?)+)")


@dataclass
class ParsedClaim:
    claim_id: str
    claim_text: str
    qualifiers: list[str]
    supporting_excerpt: str
    yaml_data: dict
    source_refs: list[str] = field(default_factory=list)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_claim_file(path: Path) -> ParsedClaim:
    content = read_text(path)
    claim_id = path.stem

    yaml_match = YAML_BLOCK_RE.search(content)
    if not yaml_match:
        raise ValueError(f"{path}: no trailing ```yaml block found")
    yaml_data = yaml.safe_load(yaml_match.group(1)) or {}
    body = content[: yaml_match.start()]

    heading_match = HEADING_RE.search(body)
    after_heading = body[heading_match.end():] if heading_match else body

    # claim_text: first non-empty paragraph after the H1 heading.
    paragraph_lines: list[str] = []
    for line in after_heading.strip("\n").splitlines():
        if line.strip() == "" and paragraph_lines:
            break
        if line.strip() == "":
            continue
        paragraph_lines.append(line.strip())
    claim_text = " ".join(paragraph_lines).strip()

    # supporting_excerpt: concatenated blockquote lines ("> ...").
    quote_lines = [
        line.strip()[2:].strip() if line.strip().startswith("> ") else line.strip()[1:].strip()
        for line in body.splitlines()
        if line.strip().startswith(">")
    ]
    supporting_excerpt = " ".join(quote_lines).strip()

    # qualifiers: bullet list under "**Qualifiers:**".
    qualifiers: list[str] = []
    q_match = QUALIFIERS_HEADER_RE.search(body)
    if q_match:
        for line in q_match.group(1).splitlines():
            line = line.strip()
            if line.startswith("- "):
                qualifiers.append(line[2:].strip())

    sources_raw = yaml_data.get("sources") or []
    return ParsedClaim(
        claim_id=claim_id,
        claim_text=claim_text,
        qualifiers=qualifiers,
        supporting_excerpt=supporting_excerpt,
        yaml_data=yaml_data,
        source_refs=list(sources_raw),
    )


_source_title_cache: dict[str, str] = {}


def resolve_source_title(source_id: str) -> str:
    if source_id in _source_title_cache:
        return _source_title_cache[source_id]
    path = SOURCES_DIR / f"{source_id}.md"
    title = source_id
    if path.exists():
        content = read_text(path)
        fm_match = FRONTMATTER_RE.search(content)
        if fm_match:
            try:
                fm = yaml.safe_load(fm_match.group(1)) or {}
                title = fm.get("title") or fm.get("short_ref") or source_id
            except yaml.YAMLError:
                pass
    _source_title_cache[source_id] = title
    return title


def to_datetimeoffset(value) -> str | None:
    if value is None:
        return None
    if isinstance(value, (datetime.date, datetime.datetime)):
        return f"{value.isoformat()}T00:00:00Z" if isinstance(value, datetime.date) and not isinstance(value, datetime.datetime) else value.isoformat()
    return None


def build_document(parsed: ParsedClaim) -> dict:
    y = parsed.yaml_data
    scope = y.get("scope") or {}
    relationships = y.get("relationships") or {}

    source_ids = sorted({ref.split("#", 1)[0] for ref in parsed.source_refs if ref})
    source_titles = sorted({resolve_source_title(sid) for sid in source_ids})
    is_restricted = bool(source_ids) and set(source_ids).issubset(RESTRICTED_SOURCE_IDS)

    doc = {
        "id": parsed.claim_id,
        "claim_id": parsed.claim_id,
        "claim_text": parsed.claim_text,
        "claim_type": y.get("claim_type") or "",
        "scope_spatial": scope.get("spatial") or y.get("geographic_scope") or "",
        "scope_sectoral": scope.get("sectoral") or "",
        "evidence_strength": y.get("evidence_strength") or "",
        "context_tags": y.get("context_tags") or [],
        "mechanism_tags": y.get("mechanism_tags") or [],
        "outcome_tags": y.get("outcome_tags") or [],
        "policy_lever_tags": y.get("policy_lever_tags") or [],
        "qualifiers": parsed.qualifiers,
        "supporting_excerpt": parsed.supporting_excerpt,
        "sources": parsed.source_refs,
        "source_titles": source_titles,
        "relationships_supports": relationships.get("supports") or [],
        "relationships_qualifies": relationships.get("qualifies") or [],
        "relationships_contradicts": relationships.get("contradicts") or [],
        "relationships_depends_on": relationships.get("depends_on") or [],
        "is_restricted_source": is_restricted,
        "created": to_datetimeoffset(y.get("created")),
        "last_reviewed": to_datetimeoffset(y.get("last_reviewed")),
        "claim_url": f"{GITHUB_BLOB_BASE}/claims/{parsed.claim_id}.md",
    }
    return {k: v for k, v in doc.items() if v is not None}


def embedding_input_text(doc: dict) -> str:
    parts = [doc.get("claim_text", ""), " ".join(doc.get("qualifiers", [])), doc.get("supporting_excerpt", "")]
    return " ".join(p for p in parts if p).strip()


def chunked(items: list, size: int) -> Iterable[list]:
    for i in range(0, len(items), size):
        yield items[i : i + size]


def get_changed_claim_ids(since_ref: str) -> set[str] | None:
    try:
        out = subprocess.run(
            ["git", "diff", "--name-only", since_ref, "HEAD", "--", "claims", "sources"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout
    except subprocess.CalledProcessError as exc:
        print(f"warning: git diff against {since_ref} failed ({exc}); falling back to full reindex", file=sys.stderr)
        return None

    changed_files = [line.strip() for line in out.splitlines() if line.strip()]
    if not changed_files:
        return set()

    claim_ids: set[str] = set()
    source_touched = False
    for f in changed_files:
        if f.startswith("claims/") and f.endswith(".md"):
            stem = Path(f).stem
            if stem != "index":
                claim_ids.add(stem)
        elif f.startswith("sources/") and f.endswith(".md"):
            source_touched = True

    if source_touched:
        # A source card changed — citations/titles for any claim referencing it may have
        # changed, and we don't track a reverse index, so fall back to a full reindex.
        return None
    return claim_ids


def load_index_schema() -> dict:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    # Strip documentation-only keys that aren't part of the Azure AI Search REST index schema.
    return {k: v for k, v in schema.items() if not k.startswith("$") and k not in ("embedding_model", "restricted_sources")}


def ensure_index(search_endpoint: str, index_name: str, credential, dry_run: bool) -> None:
    schema = load_index_schema()
    schema["name"] = index_name
    if dry_run:
        print(f"[dry-run] would create/update index '{index_name}' with {len(schema['fields'])} fields")
        return
    token = credential.get_token("https://search.azure.com/.default").token
    url = f"{search_endpoint}/indexes/{index_name}?api-version={SEARCH_API_VERSION}"
    resp = requests.put(
        url,
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        data=json.dumps(schema),
        timeout=60,
    )
    if not resp.ok:
        raise RuntimeError(f"Failed to create/update index: {resp.status_code} {resp.text}")
    print(f"Index '{index_name}' created/updated ({resp.status_code}).")


def generate_embeddings(openai_endpoint: str, deployment: str, credential, texts: list[str]) -> list[list[float]]:
    from openai import AzureOpenAI

    token_provider = get_bearer_token_provider(credential, "https://cognitiveservices.azure.com/.default")
    client = AzureOpenAI(
        azure_endpoint=openai_endpoint,
        azure_ad_token_provider=token_provider,
        api_version=OPENAI_API_VERSION,
    )
    vectors: list[list[float]] = []
    for batch in chunked(texts, 16):
        resp = client.embeddings.create(input=batch, model=deployment)
        vectors.extend([item.embedding for item in resp.data])
    return vectors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--full", action="store_true", help="Reindex every claim.")
    group.add_argument("--since", metavar="GIT_REF", help="Only reindex claims changed since this git ref.")
    parser.add_argument("--dry-run", action="store_true", help="Parse and embed but do not write to Azure AI Search.")
    parser.add_argument("--index-name", default=os.environ.get("SEARCH_INDEX_NAME", "policynav-claims-index"))
    args = parser.parse_args()

    search_endpoint = os.environ.get("SEARCH_ENDPOINT")
    openai_endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT")
    embedding_deployment = os.environ.get("AZURE_OPENAI_EMBEDDING_DEPLOYMENT", "text-embedding-3-large")

    if not args.dry_run and not search_endpoint:
        print("error: SEARCH_ENDPOINT environment variable is required (unless --dry-run)", file=sys.stderr)
        return 1
    if not args.dry_run and not openai_endpoint:
        print("error: AZURE_OPENAI_ENDPOINT environment variable is required (unless --dry-run)", file=sys.stderr)
        return 1

    claim_ids_filter: set[str] | None = None
    if args.since:
        claim_ids_filter = get_changed_claim_ids(args.since)
        if claim_ids_filter is None:
            print(f"Falling back to full reindex (source change or diff failure against {args.since}).")
        elif not claim_ids_filter:
            print(f"No claim changes found since {args.since}; nothing to index.")
            return 0
        else:
            print(f"Incremental reindex: {len(claim_ids_filter)} changed claim(s) since {args.since}.")

    claim_paths = sorted(p for p in CLAIMS_DIR.glob("claim-*.md"))
    if claim_ids_filter is not None:
        claim_paths = [p for p in claim_paths if p.stem in claim_ids_filter]

    if not claim_paths:
        print("No claims to index.")
        return 0

    print(f"Parsing {len(claim_paths)} claim file(s)...")
    documents = []
    restricted_count = 0
    for path in claim_paths:
        parsed = parse_claim_file(path)
        doc = build_document(parsed)
        if doc["is_restricted_source"]:
            restricted_count += 1
        documents.append(doc)

    print(f"Parsed {len(documents)} claim(s); {restricted_count} flagged is_restricted_source=true.")

    credential = DefaultAzureCredential()

    ensure_index(search_endpoint, args.index_name, credential, args.dry_run)

    print("Generating embeddings...")
    texts = [embedding_input_text(d) for d in documents]
    if args.dry_run:
        print(f"[dry-run] would generate {len(texts)} embedding(s) via deployment '{embedding_deployment}'")
        for d in documents:
            d["content_vector"] = []
    else:
        vectors = generate_embeddings(openai_endpoint, embedding_deployment, credential, texts)
        for d, v in zip(documents, vectors):
            d["content_vector"] = v

    if args.dry_run:
        print(f"[dry-run] would upsert {len(documents)} document(s) into index '{args.index_name}'")
        return 0

    search_client = SearchClient(
        endpoint=search_endpoint,
        index_name=args.index_name,
        credential=credential,
    )
    for batch in chunked(documents, 100):
        result = search_client.merge_or_upload_documents(documents=batch)
        failed = [r for r in result if not r.succeeded]
        if failed:
            print(f"error: {len(failed)} document(s) failed to upsert in a batch of {len(batch)}", file=sys.stderr)
            for r in failed[:5]:
                print(f"  {r.key}: {r.error_message}", file=sys.stderr)
            return 1
    print(f"Upserted {len(documents)} document(s) into index '{args.index_name}'.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
