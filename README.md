# City Policy LLM Wiki

A RAG-first, human-browsable knowledge base for city policy research.

## What this repo is for

This wiki stores atomic, citable claims about urban economics, governance, land use, transport, and city policy. It is designed so that both humans and LLMs can find, navigate, and reason from evidence efficiently.

Every factual assertion lives in a **Claim Card** — a single-sentence, YAML-structured file with source anchors, tags, and relationships. Human-readable synthesis and lever pages curate those claims but never introduce unsourced facts.

## How to browse

Start in [`/synthesis/`](synthesis/) for thematic overviews:

| Hub | Topic |
|---|---|
| [01 Urbanisation and Spatial Systems](synthesis/01-urbanisation-and-spatial-systems.md) | Urbanisation patterns, spatial structure, primacy |
| [02 Agglomeration and Productivity](synthesis/02-agglomeration-and-productivity.md) | Agglomeration economies, density, wages |
| [03 Governance and Institutions](synthesis/03-governance-and-institutions.md) | Metropolitan governance, coordination, fragmentation |
| [04 Land Markets, Zoning, Urban Form](synthesis/04-land-markets-zoning-urban-form.md) | Zoning, land supply, housing affordability |
| [05 Transport and Accessibility](synthesis/05-transport-and-accessibility.md) | Transport investment, accessibility, labour markets |
| [06 Inclusion and Division](synthesis/06-inclusion-and-division.md) | Inequality, informal settlements, targeted programs |
| [07 Resilience, Environment, Sustainability](synthesis/07-resilience-environment-sustainability.md) | Climate, emissions, urban resilience |
| [08 Methods and Tools](synthesis/08-methods-and-tools.md) | Measurement, modelling, data sources |
| [09 Demographics and Population Strategy](synthesis/09-demographics-and-population-strategy.md) | Demographics, migration, population policy |

From any synthesis page, follow claim links into [`/claims/`](claims/) for the primary evidence.

Policy mechanism pages are in [`/levers/`](levers/). Place-specific views are in [`/places/`](places/).

## How LLM retrieval should work

1. **Retrieve claim cards first.** Embed and index `/claims/*.md`. Each claim is a self-contained retrieval unit.
2. **Expand via relationships.** Follow `supports`, `qualifies`, `contradicts`, and `depends_on` links to related claims.
3. **Ground in sources.** Each claim's `sources` field points to a source anchor in `/sources/`. Fetch those for full bibliographic context.
4. **Use ontology files for filtering.** Retrieve only claims matching a `mechanism_tag`, `outcome_tag`, or `context_tag` to narrow scope.
5. Synthesis and lever pages are useful for orienting a query but should not be the primary retrieval target.

## How to contribute

1. Register the paper as a source page in `/sources/source-####.md`.
2. Define section anchors in the source frontmatter.
3. Extract atomic claims into `/claims/claim-####.md`.
4. Tag each claim using the controlled vocabulary in `/ontology/`.
5. Update or create concept cards in `/concepts/` for recurring terms.
6. Add claim links to the relevant synthesis hub.
7. See [`/ingestion/INGESTION_RULES.md`](ingestion/INGESTION_RULES.md) for the full workflow.
