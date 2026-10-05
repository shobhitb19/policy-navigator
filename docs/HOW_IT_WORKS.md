# How It Works

## Knowledge model

The wiki has three layers:

### Retrieval layer (primary)

- **Claim Cards** (`/claims/`): the atomic unit. One sentence, one idea, one or more source anchors. These are what an LLM retrieves.
- **Evidence Cards** (`/evidence/`): describe reusable evidence bases (meta-analyses, datasets, structural models). Multiple claims may cite the same evidence card.
- **Concept Cards** (`/concepts/`): define terms used across claims with stable IDs.

### Human browsing layer

- **Synthesis hubs** (`/synthesis/`): curated thematic overviews linking to claim IDs. No new unsourced facts.
- **Policy lever pages** (`/levers/`): how a lever works, prerequisites, risks, and linked claims.
- **Place pages** (`/places/`): place-specific context and curated claims.

### Traceability layer

- **Source pages** (`/sources/`): full bibliographic metadata and section anchors. Claims link to specific anchors within a source.

## Linking model

- **Claim → Source**: each claim's markdown body has a `## Source` section with markdown links to the source file and specific section anchor, e.g. `[Donovan et al. (2021)](../sources/source-0004.md#section-4-1)`. Section anchors are created with `<a id="...">` tags in the source file body.
- **Claim → Claim**: the YAML `relationships` fields (`supports`, `qualifies`, `contradicts`, `depends_on`) record formal relationships. The `## Related claims` body section renders these as clickable links.
- **Synthesis / lever / place → Claim**: use standard markdown links, e.g. `[claim-0001](../claims/claim-0001.md)`. Do not use `[[claim-0001]]` (wiki-link syntax does not render on GitHub).
- **Source → Claim**: source file bodies list all claims extracted from that source with markdown links.

## Controlled vocabulary

All tags must come from the ontology files in `/ontology/`. This ensures retrieval filters work consistently across the entire claim corpus.

## ID stability

IDs are assigned sequentially and never reused. If a claim is retired, it is marked `status: retired` in frontmatter — the file is kept.
