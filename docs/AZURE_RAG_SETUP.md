# Azure AI Search RAG layer — setup & operations (Phase 1)

This document describes the Phase 1 build-out: an Azure AI Search hybrid (vector + semantic +
keyword) index over this repo's claim cards, with embeddings from a dedicated Azure OpenAI
resource. It is the retrieval layer that a future Phase 2 Copilot Studio agent will ground on.
It does **not** change the authoring model — `claims/`, `sources/`, `synthesis/`, `levers/`,
`places/`, `concepts/`, and `ontology/` remain plain Markdown+YAML in this git repo as the single
source of truth. Azure AI Search is a derived, rebuildable index, not a second copy of record.

## What was created

All resources were deployed via Bicep (`/infra`) into subscription
`fb1c7a78-ca15-45f7-b6b3-83039a763edd` (tenant `28f9b0a6-2573-4a5b-98a7-ab7e3b968f3a`), region
`australiaeast`, resource group **`rg-policy-navigator`**:

| Resource | Name | Tier | Notes |
|---|---|---|---|
| Azure AI Search | `policynav-search` | **Basic** | Semantic ranker: **standard**. ~$75/mo. See [Cost rationale](#cost-rationale). |
| Azure OpenAI | `policynav-openai` | S0 (pay-as-you-go) | Dedicated account, not shared with other projects. |
| Embedding deployment | `text-embedding-3-large` | Standard, 30K TPM capacity | 3072-dim vectors. Confirmed available in `australiaeast` by successful deployment. |
| Search index | `policynav-claims-index` | — | One document per claim card. Schema: `infra/search-index-schema.json`. |

Endpoints:
- Search: `https://policynav-search.search.windows.net`
- OpenAI: `https://policynav-openai.openai.azure.com/`

Both resources have **system-assigned managed identities** and AAD auth enabled
(`aadAuthFailureMode: http401WithBearerChallenge` on Search; `disableLocalAuth: false` on OpenAI
so API keys still work as a fallback, but nothing in this repo's tooling uses them). No API keys
are stored anywhere in the repo, CI, or scripts — everything authenticates via
`DefaultAzureCredential`.

### Cost rationale

- **Search: Basic, not Standard S1.** Basic (~$75/mo) supports the semantic ranker and one
  replica/partition, which comfortably covers this repo's current scale (253 claims, a few MB of
  text). Standard S1 (~$250/mo) adds more storage/throughput headroom this project doesn't need
  yet. Move to Standard S1 if/when replica count, storage (2GB Basic limit), or query throughput
  become binding constraints — there's no re-indexing cost to that move, only a tier change.
- **Semantic ranker: standard, not free.** The free semantic tier caps query volume too low for
  a Teams-bot-backed agent used by multiple analysts; standard removes that cap. It's billed
  per-query, not a flat monthly fee, so cost scales with actual usage.
- **OpenAI: dedicated S0 account, not a shared Foundry project.** The subscription already had
  other AI Foundry/OpenAI resources (e.g. `foundryiqdemo-shresource`), but the user chose a new
  dedicated resource for this project to keep quota, cost attribution, and RBAC scoped
  cleanly to policy-navigator.
- **Embedding model: `text-embedding-3-large`** (3072 dimensions) over `-small` or `ada-002` —
  this corpus is small (253 claims now, likely low hundreds to low thousands long-term), so the
  per-embedding cost difference is negligible, and retrieval quality matters more given the
  RAG answers will ground policy analysis.

## Index schema

`infra/search-index-schema.json` is the **committed source of truth** for the index definition
— not just described in prose. `scripts/azure_search_index.py` loads this file directly and
`PUT`s it (minus two documentation-only keys, `embedding_model` and `restricted_sources`, which
aren't valid Search REST properties) to create/update the index, so the schema can never drift
from what's actually deployed.

Key points:
- **One document per claim card** (`claims/claim-####.md`).
- Every ontology tag group (`context_tags`, `mechanism_tags`, `outcome_tags`,
  `policy_lever_tags`) is `filterable` + `facetable` + `searchable`, so a Copilot Studio agent
  (or any client) can both free-text search and facet/filter by tag.
- `scope_spatial`, `scope_sectoral`, `evidence_strength`, `claim_type` are filterable/facetable
  scalars.
- `relationships_supports` / `_qualifies` / `_contradicts` / `_depends_on` are filterable string
  collections of claim IDs, so an agent can expand from a retrieved claim to related claims
  (mirrors `LLM_Compilation_Instructions.md`'s relationship-link rules) with a second lookup by
  `claim_id`.
- `content_vector` is a 3072-dim HNSW vector field (cosine), populated from the embedding of
  `claim_text + qualifiers + supporting_excerpt`.
- A `policynav-semantic-config` semantic configuration is defined so hybrid queries can use
  `queryType=semantic` for L2 re-ranking on top of vector + keyword results.
- **`is_restricted_source`** (boolean, filterable/facetable): `true` only when *every* source a
  claim cites resolves to one of the two permanently-restricted documents (`source-0024` —
  Kānoa population-shifts deck; `source-0045` — Treasury "Auckland Story", both per `CLAUDE.md`).
  Claims are still indexed (so retrieval doesn't silently lose evidence) but **any Phase 2
  grounding configuration must treat `is_restricted_source=true` claims with extra care** —
  e.g. exclude them from the agent's default search scope, or require an explicit
  acknowledgement/audience check before surfacing them. This is a decision Phase 2 needs from
  the user (see [What Phase 2 needs](#what-phase-2-copilot-studio-agent-needs-from-you)).

## Running the indexer locally

```bash
pip install -r scripts/requirements.txt
az login   # or any DefaultAzureCredential-compatible login

export SEARCH_ENDPOINT="https://policynav-search.search.windows.net"
export AZURE_OPENAI_ENDPOINT="https://policynav-openai.openai.azure.com"
export AZURE_OPENAI_EMBEDDING_DEPLOYMENT="text-embedding-3-large"   # default, can omit

# Full reindex (all claims):
python scripts/azure_search_index.py --full

# Incremental (only claims changed since a git ref):
python scripts/azure_search_index.py --since origin/main~1

# Dry run (parse + embed stats only, no writes to Azure):
python scripts/azure_search_index.py --full --dry-run
```

You need these two **data-plane** RBAC roles (control-plane Contributor/Owner is *not*
sufficient — Search and Cognitive Services data operations are gated separately):
- **Search Index Data Contributor** + **Search Service Contributor** on `policynav-search`
- **Cognitive Services OpenAI User** on `policynav-openai`

```bash
# Example — replace <principal-id> with your user/service-principal object ID
az role assignment create --assignee-object-id <principal-id> --assignee-principal-type User \
  --role "8ebe5a00-799e-43f5-93ac-243d3dce84a7" \
  --scope "/subscriptions/fb1c7a78-ca15-45f7-b6b3-83039a763edd/resourceGroups/rg-policy-navigator/providers/Microsoft.Search/searchServices/policynav-search"
az role assignment create --assignee-object-id <principal-id> --assignee-principal-type User \
  --role "7ca78c08-252a-4471-8644-bb5ff32d4ba0" \
  --scope "/subscriptions/fb1c7a78-ca15-45f7-b6b3-83039a763edd/resourceGroups/rg-policy-navigator/providers/Microsoft.Search/searchServices/policynav-search"
az role assignment create --assignee-object-id <principal-id> --assignee-principal-type User \
  --role "5e0bd9bd-7b93-4f28-af87-19fc36ad61bd" \
  --scope "/subscriptions/fb1c7a78-ca15-45f7-b6b3-83039a763edd/resourceGroups/rg-policy-navigator/providers/Microsoft.CognitiveServices/accounts/policynav-openai"
```

### Script behaviour notes

- Claim card YAML is **not perfectly uniform** across all 253 files — older/core claims use the
  full ontology schema (`scope.spatial`/`scope.sectoral`, `mechanism_tags`, `policy_lever_tags`,
  `relationships`), while some newer demographic claims use a reduced schema (top-level
  `geographic_scope`, no mechanism/lever tags, no relationships block). The parser falls back
  defensively field-by-field so both schemas index cleanly; missing tag groups just become empty
  lists, never a hard failure.
- Source titles are resolved by reading the YAML frontmatter block from the matching
  `sources/source-####.md` card (the block can appear after an H1 heading, not necessarily as the
  literal first line — the parser searches for it rather than assuming position 0).
- `--since <ref>` diffs `claims/` and `sources/` between `<ref>` and `HEAD`. If *any* source card
  changed, the script falls back to a full reindex (source changes can affect resolved titles for
  any claim citing that source, and there's no reverse index to target just the affected claims
  cheaply). If the diff itself fails (e.g. an invalid/unreachable ref, or the very first push to a
  new branch), it also falls back to a full reindex rather than silently indexing nothing.

## GitHub Actions workflow

`.github/workflows/index-claims.yml` runs on every push to `main` that touches `claims/**`,
`sources/**`, the index schema, or the script itself, plus a manual `workflow_dispatch` (with a
`full_reindex` checkbox for a full rebuild). It authenticates to Azure via **OIDC federated
credentials** — no client secrets or API keys are stored in GitHub.

### One-time manual setup required (cannot be done from this session)

These steps need an Entra ID admin and are not scriptable from the tools available to this
session — the user (or an Entra admin) needs to run them once:

1. **Create an Entra ID app registration** (becomes the workflow's identity):
   ```bash
   az ad app create --display-name "policy-navigator-gh-actions-indexer"
   # note the appId (client ID) and the app's objectId from the output
   az ad sp create --id <appId>   # creates the matching service principal
   ```

2. **Add a federated credential** scoped to this repo's `main` branch (replace `<appId>` and
   `<app-object-id>` — the federated-credential subcommand needs the app's **object ID**, not the
   appId):
   ```bash
   az ad app federated-credential create --id <app-object-id> --parameters '{
     "name": "policy-navigator-main-branch",
     "issuer": "https://token.actions.githubusercontent.com",
     "subject": "repo:shobhitb19/policy-navigator:ref:refs/heads/main",
     "audiences": ["api://AzureADTokenExchange"]
   }'
   ```
   Add a second federated credential with
   `"subject": "repo:shobhitb19/policy-navigator:environment:azure-search-rag"` if you also want
   manual `workflow_dispatch` runs gated through a GitHub Environment (recommended — see step 4).

3. **Grant the service principal the same three data-plane roles** the local run needs (reuse
   the `az role assignment create` commands above, substituting the service principal's object
   ID — or re-run the Bicep deployment with `indexerPrincipalId` set to that object ID, which
   wires these same role assignments as conditional resources in `infra/modules/search.bicep` /
   `infra/modules/openai.bicep`):
   ```bash
   az deployment sub create --location australiaeast --template-file infra/main.bicep \
     --parameters infra/main.parameters.json indexerPrincipalId=<service-principal-object-id>
   ```

4. **Create a GitHub Environment named `azure-search-rag`** (Settings → Environments) and add:
   - Repository/Environment **variables** (not secrets — these are non-sensitive endpoints):
     `SEARCH_ENDPOINT`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_EMBEDDING_DEPLOYMENT`,
     `SEARCH_INDEX_NAME`.
   - Repository or Environment **secrets**: `AZURE_CLIENT_ID` (the app registration's appId),
     `AZURE_TENANT_ID` (`28f9b0a6-2573-4a5b-98a7-ab7e3b968f3a`), `AZURE_SUBSCRIPTION_ID`
     (`fb1c7a78-ca15-45f7-b6b3-83039a763edd`). These identify the workload identity for OIDC
     token exchange — not secrets in the "long-lived credential" sense, but GitHub's
     `azure/login@v2` action expects them in that slot.

Until this one-time setup is done, the workflow will fail at the `azure/login@v2` step with an
OIDC trust error — that's expected and not a bug in the workflow itself.

## Validation performed

The full indexer was run against the live resources (`--full`): 253 claim files parsed, 7
correctly flagged `is_restricted_source=true` (all cite only `source-0024` or `source-0045`),
index created, embeddings generated, and all 253 documents upserted successfully.

Five hybrid (vector + semantic + keyword) queries were then run directly against the index to
confirm retrieval quality and filtering, e.g.:

- *"What does the evidence say about housing supply and affordability?"* filtered to
  `policy_lever_tags` containing `housing_supply_reform` → correctly returned claim-0261,
  claim-0075, claim-0191 with semantic reranker scores >2.5, each with correct ontology tags and
  resolved source titles.
- *"What claims are based on the Kānoa population presentation?"* filtered to
  `is_restricted_source eq true` → correctly returned only claim-0113/0114/0117 (all citing
  `source-0024`), confirming the restricted-source flag is queryable and no restricted claim
  leaks into unfiltered results by surprise (it's opt-in visible, not hidden, which is a Phase 2
  grounding-policy decision — see below).
- *"agglomeration economies and wages"* filtered to `evidence_strength eq 'meta_analysis'` →
  correctly returned only meta-analysis-sourced claims (claim-0014, claim-0001), confirming
  evidence-strength faceting.

This confirms hybrid retrieval, semantic ranking, tag/evidence-strength filtering, and
restricted-source flagging all work end-to-end.

## Re-running after content changes

Any push to `main` touching `claims/**` or `sources/**` automatically triggers an incremental
reindex via the GitHub Action (once the one-time OIDC setup above is complete). No manual step is
needed in the common case. Use `workflow_dispatch` with `full_reindex: true` to force a full
rebuild (e.g. after an index schema change).

## What Phase 2 (Copilot Studio agent) needs from you

Before Phase 2 work starts, the following decisions/inputs are needed:

1. **Restricted-source visibility policy**: should the Copilot Studio agent's default grounding
   search *exclude* `is_restricted_source=true` claims entirely, or *include* them but require the
   agent to prefix its answer with an IN-CONFIDENCE/internal-use warning? This directly affects
   how the agent's knowledge source / search parameters are configured.
2. **Microsoft 365 / Copilot Studio environment target**: which Power Platform environment
   (dev/test/prod) and Teams tenant the agent should be published into, and who should be
   listed as co-owners/makers.
3. **Confirmation that the Copilot Studio "Azure AI Search" generative-answers / knowledge-source
   connector will be configured with this index** (`policynav-claims-index` on
   `policynav-search`) — it needs read access, so a decision on whether Copilot Studio
   authenticates via API key (simpler to wire up in Studio's UI) or managed identity/AAD
   (consistent with the no-API-key posture of this phase, but requires more manual Studio
   configuration).
4. **Citation/answer format requirements**: confirm the agent should answer with claim ID
   citations, plain-English meaning, mechanism, and evidence strength, and should expand via
   `relationships_*` fields — as specified in `LLM_Compilation_Instructions.md` — so the Phase 2
   prompt/topic design can be scoped precisely.
5. **Any additional Teams audience/access restrictions** (e.g. should the agent be restricted to
   specific Teams groups/security groups covering only MBIE/Treasury/Auckland Council analysts,
   rather than the whole tenant)?
