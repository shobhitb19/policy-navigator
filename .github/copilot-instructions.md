# Copilot Instructions — Place-Based Policy Wiki

This repository is a RAG-first knowledge base on urban economics and place-based policy, structured for both human browsing and LLM retrieval. The primary content lives in the `main` branch as plain Markdown files — not in the GitHub Wiki tab and not only on the deployed GitHub Pages site.

## Repository layout

| Path | Content |
|---|---|
| `claims/claim-NNNN.md` | Atomic, citable claim cards (112 files, primary retrieval targets) |
| `synthesis/NN-title.md` | Thematic hub pages that curate claim links — good entry points |
| `levers/lever-name.md` | Policy mechanism pages (housing reform, zoning, transport, etc.) |
| `places/place-name.md` | Place-specific views (currently Auckland) |
| `sources/source-NNNN.md` | Bibliographic source pages with section anchors |
| `concepts/concept-name.md` | Glossary/concept cards for recurring terms |
| `ontology/*.md` | Controlled vocabulary for tags and relationship types |
| `evidence/` | Supporting evidence files |
| `ingestion/` | Workflow rules for adding new content |
| `docs/` | Meta-documentation (contributing, style guide) |

## How to retrieve

1. **Start with synthesis hubs** for broad topic orientation — each hub contains a key claim index with direct links to claim files.
2. **Read claim cards directly** (`claims/claim-NNNN.md`) for the primary evidence. Each claim is self-contained.
3. **Filter by YAML tags** in claim card frontmatter — use `mechanism_tags`, `outcome_tags`, `context_tags`, or `policy_lever_tags` to narrow scope.
4. **Follow relationship links** in the `relationships` block of a claim's YAML — `supports`, `qualifies`, `contradicts`, and `depends_on` point to related claim IDs.
5. **Ground in sources** — the `sources` field points to `sources/source-NNNN.md#section-anchor` for full bibliographic detail.

## Synthesis hub index

| File | Topic |
|---|---|
| `synthesis/01-urbanisation-and-spatial-systems.md` | Urbanisation patterns, spatial structure, primacy |
| `synthesis/02-agglomeration-and-productivity.md` | Agglomeration economies, density, wages |
| `synthesis/03-governance-and-institutions.md` | Metropolitan governance, coordination, fragmentation |
| `synthesis/04-land-markets-zoning-urban-form.md` | Zoning, land supply, housing affordability |
| `synthesis/05-transport-and-accessibility.md` | Transport investment, accessibility, labour markets |
| `synthesis/06-inclusion-and-division.md` | Inequality, informal settlements, targeted programs |
| `synthesis/07-resilience-environment-sustainability.md` | Climate, emissions, urban resilience |
| `synthesis/08-methods-and-tools.md` | Measurement, modelling, data sources |
| `synthesis/09-demographics-and-population-strategy.md` | Demographics, migration, population policy |

## Claim card structure

Each claim file contains:
- **Body**: A single-sentence claim, source citation, key quotation, and list of qualifiers.
- **YAML block** (fenced with ` ```yaml ` at the bottom): Structured metadata for filtering and graph traversal.

Key YAML fields:

```yaml
claim_id: claim-NNNN
claim_type: causal_association | descriptive | normative | methodological
scope:
  spatial: metropolitan | national | subnational | cross-country
  sectoral: economy-wide | housing | transport | ...
context_tags: [OECD, developing, advanced_urbanisation, ...]
mechanism_tags: [agglomeration, land_market_failure, coordination_failure, ...]
outcome_tags: [productivity, wages, housing_affordability, emissions, ...]
policy_lever_tags: [housing_supply_reform, transport_investment, ...]
evidence_strength: meta_analysis | rct | quasi_experimental | observational | expert_review
sources: [source-NNNN#section-anchor, ...]
relationships:
  supports: [claim-NNNN, ...]
  qualifies: [claim-NNNN, ...]
  contradicts: [claim-NNNN, ...]
  depends_on: [claim-NNNN, ...]
```

## Controlled vocabulary (key tags)

**mechanism_tags**: `agglomeration`, `learning_spillovers`, `matching`, `sharing`, `congestion`, `coordination_failure`, `path_dependence`, `land_market_failure`, `network_effects`, `fiscal_incentive`

**outcome_tags**: `productivity`, `wages`, `employment`, `housing_affordability`, `accessibility`, `emissions`, `resilience`, `trust`, `livability`, `inequality`, `urban_form`, `fiscal_sustainability`

**policy_lever_tags**: `housing_supply_reform`, `transport_investment`, `metropolitan_governance`, `land_use_planning`, `zoning_and_far`, `infrastructure_provision`, `investment_and_fdi`, `innovation_and_diffusion`, `integrated_spatial_planning`

**context_tags**: `OECD`, `developing`, `advanced_urbanisation`, `New_Zealand`, `Auckland`

**evidence_strength** (strongest to weakest): `meta_analysis` > `rct` > `quasi_experimental` > `observational` > `expert_review`

## Policy lever pages

`levers/housing-supply-reform.md`, `levers/transport-investment.md`, `levers/metropolitan-governance.md`, `levers/land-use-planning.md`, `levers/zoning-and-far.md`, `levers/infrastructure-provision.md`, `levers/investment-and-fdi.md`, `levers/innovation-and-diffusion.md`, `levers/integrated-spatial-planning.md`

## Do not

- Do not treat synthesis pages as primary evidence — they curate claims but introduce no new facts.
- Do not cite a claim without checking its `evidence_strength` and `qualifiers`.
- Do not invent claim IDs — always look up the actual file.
- Do not use the `gh-pages` branch — all source content is on `main`.
