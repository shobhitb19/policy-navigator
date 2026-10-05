# City Policy LLM Wiki — RAG‑First Knowledge Base (Repo Spec)

**Goal:** This document is a *single, self‑contained* specification you can hand to another LLM to create a Git repository implementing a RAG‑first, human‑browsable city policy wiki.

- Primary retrieval unit: **Claim Cards** (atomic, citable).
- Human browsing: **Synthesis / Lever / Concept** pages that *only* curate and explain claim cards.
- Traceability: **Source** pages that preserve bibliographic metadata and section anchors.

---

## 0) Hard requirements

1. **RAG‑first**: Retrieval must target Claim Cards, not long document chunks.
2. **Human‑browsable**: Humans can navigate by topic hubs → synthesis → claims.
3. **Traceable**: Every claim cites at least one source anchor.
4. **Controlled vocabulary**: Claim types, tags, and relationships come from repo ontology files.
5. **Git‑friendly**: Everything is plain text (`.md`, `.yml`, `.json`) with stable IDs.

---

## 1) Repository layout (create exactly)

Create a new git repository with the following structure:

```text
city-llm-wiki/
├── README.md
├── LICENSE
├── .gitignore
├── docs/
│   ├── HOW_IT_WORKS.md
│   ├── CONTRIBUTING.md
│   └── STYLE_GUIDE.md
│
├── ontology/
│   ├── claim_types.md
│   ├── mechanism_tags.md
│   ├── policy_lever_tags.md
│   ├── context_tags.md
│   ├── outcome_tags.md
│   ├── relationship_types.md
│   └── validation_rules.md
│
├── claims/
│   ├── claim-0001.md
│   ├── claim-0002.md
│   └── ...
│
├── evidence/
│   ├── evidence-0001.md
│   └── ...
│
├── concepts/
│   ├── agglomeration-economies.md
│   ├── livable-density.md
│   └── ...
│
├── synthesis/
│   ├── 01-urbanisation-and-spatial-systems.md
│   ├── 02-agglomeration-and-productivity.md
│   ├── 03-governance-and-institutions.md
│   ├── 04-land-markets-zoning-urban-form.md
│   ├── 05-transport-and-accessibility.md
│   ├── 06-inclusion-and-division.md
│   ├── 07-resilience-environment-sustainability.md
│   └── 08-methods-and-tools.md
│
├── levers/
│   ├── zoning-and-far.md
│   ├── land-use-planning.md
│   ├── transport-investment.md
│   ├── metropolitan-governance.md
│   └── ...
│
├── places/
│   ├── auckland.md
│   └── ...
│
├── sources/
│   ├── source-0001.md
│   ├── source-0002.md
│   └── ...
│
└── ingestion/
    ├── INGESTION_RULES.md
    ├── CHUNKING_GUIDELINES.md
    ├── CLAIM_EXTRACTION_GUIDELINES.md
    └── QA_CHECKLIST.md
```

**Notes**
- All objects are **one file per object** for easy git diffs.
- IDs are stable and used for linking: `claim-####`, `source-####`, etc.

---

## 2) Knowledge model (three layers)

### 2.1 Retrieval layer (canonical)

- **Claim Cards**: the primary retrieval unit.
- **Evidence Cards**: reusable evidence descriptors (meta‑analysis, dataset, model).
- **Concept Cards**: definitions and boundary conditions.

### 2.2 Human layer

- **Synthesis pages**: curated claim sets + narrative.
- **Policy lever pages**: how a lever works, prerequisites, risks, linked claims.
- **Place pages**: place‑specific view, curated claims.

### 2.3 Traceability layer

- **Source pages**: bibliographic metadata + section anchors.
- (Optional) you may store PDFs elsewhere, but the repo should not depend on binaries.

---

## 3) Canonical object: Claim Card (`/claims/claim-####.md`)

Each claim card is a Markdown file with a YAML frontmatter block and an optional short body.

### 3.1 Claim Card template

```yaml
---
claim_id: claim-0001
claim_text: >
  One atomic, testable statement written as a single sentence.

claim_type: causal_association   # must be in ontology/claim_types.md

scope:
  spatial: metropolitan          # e.g., neighbourhood|city|metropolitan|region|national|global
  sectoral: economy-wide         # optional: economy-wide|manufacturing|services|housing|transport|etc

context_tags:                   # must be in ontology/context_tags.md
  - OECD
  - advanced_urbanisation

mechanism_tags:                 # must be in ontology/mechanism_tags.md
  - coordination_failure

outcome_tags:                   # must be in ontology/outcome_tags.md
  - productivity

policy_lever_tags:              # must be in ontology/policy_lever_tags.md
  - metropolitan_governance
  - integrated_planning

evidence_strength: meta_analysis  # free text but recommended set in ontology/validation_rules.md

sources:
  - source-0003#chapter-2#section-2-3  # anchors defined inside the source page

supporting_excerpt: >
  Short quote or paraphrase of the key supporting passage (keep brief).

qualifiers:
  - Boundary condition or caveat (required if source states it).

relationships:
  supports: []
  qualifies: []
  contradicts: []
  depends_on: []

created: 2026-06-03
last_reviewed: 2026-06-03
---
```

### 3.2 Claim writing rules

- **Atomic**: exactly one idea per claim.
- **Citable**: must have ≥1 `sources` anchor.
- **Scoped**: fill `scope` and `context_tags`.
- **Qualified**: capture caveats in `qualifiers`.
- **No normative language**: claims describe evidence, mechanisms, or observed relationships.

---

## 4) Evidence Card (`/evidence/evidence-####.md`)

Evidence cards describe reusable evidence bases (e.g., a meta‑analysis).

### 4.1 Evidence template

```yaml
---
evidence_id: evidence-0001
evidence_type: meta_analysis   # meta_analysis|cross_country|case_study|structural_model|scenario

describes: >
  What the evidence base is about.

summary: >
  2–4 sentences.

key_results:
  - One bullet per result (no new claims; link to claim IDs if needed).

limitations:
  - One bullet per limitation.

applies_to_context_tags:
  - OECD
  - developing

sources:
  - source-0007

created: 2026-06-03
last_reviewed: 2026-06-03
---
```

---

## 5) Concept Card (`/concepts/*.md`)

Concept cards define terms used across claims.

### 5.1 Concept template

```yaml
---
concept_id: livable_density
name: Livable density

definition: >
  Short, stable definition.

non_examples:
  - Example of what this concept is not.

related_concepts:
  - agglomeration_economies
  - crowding

linked_claims:
  - claim-0123

sources:
  - source-0011#overview

created: 2026-06-03
last_reviewed: 2026-06-03
---
```

---

## 6) Human pages

### 6.1 Synthesis hub pages (`/synthesis/0X-*.md`)

Each hub page provides:
- a short overview
- a table of contents to subpages (optional)
- curated lists of the most important claims by theme

**Rule:** Synthesis pages may explain and connect claims, but **must not introduce new factual assertions** without linking to claim IDs.

#### Synthesis page template

```markdown
# Hub Title

## Summary
2–6 sentences summarising the hub.

## Key claim index
- [[claim-0001]] Short label
- [[claim-0023]] Short label

## Subtopics
- Link to related lever pages
- Link to concept pages

## Open questions
Bullets.
```

### 6.2 Policy lever pages (`/levers/*.md`)

**Rule:** lever pages describe how levers work, prerequisites, and risks, and link to claims.

#### Lever page template

```markdown
# Lever: Zoning and FAR

## What this is
Definition.

## What problem it addresses
Bullets.

## How it works (mechanisms)
- Mechanism → link to concept/claim

## Preconditions
- Enforcement capacity
- Data / governance prerequisites

## Risks and trade-offs
- Link to tradeoff claims

## Key claims
- [[claim-0112]]
- [[claim-0134]]
```

### 6.3 Place pages (`/places/*.md`)

Place pages provide place context and curated claims.

#### Place page template

```markdown
# Place: Auckland

## Context
Short description.

## Key constraints
Bullets.

## Key claims relevant to this place
- [[claim-0201]]

## Priority levers
- Link to lever pages
```

---

## 7) Sources (`/sources/source-####.md`)

Source pages provide bibliographic metadata and **section anchors** used by claims.

### 7.1 Source template

```yaml
---
source_id: source-0001
title: "Document title"
authors:
  - "Author 1"
  - "Author 2"
year: 2022
publisher: "Organisation"
document_type: report  # report|working_paper|meta_analysis|book|chapter
geographic_scope: "e.g., OECD, Auckland, global"

# section anchors used in claims
anchors:
  - id: overview
    label: Overview
  - id: chapter-2
    label: Chapter 2: The secrets of successful cities
  - id: chapter-2#section-2-3
    label: Governance structures and productivity

notes: >
  Optional.

ingestion_status: not_started  # not_started|chunked|claims_extracted|reviewed

created: 2026-06-03
last_reviewed: 2026-06-03
---
```

---

## 8) Ontology (controlled vocabulary)

Populate each file in `/ontology/` with the following lists (bullet lists are fine).

### 8.1 `ontology/claim_types.md`
- `causal_association`
- `mechanism`
- `tradeoff`
- `sequencing_rule`
- `design_principle`
- `governance_requirement`
- `definition`
- `model_insight`
- `scenario`

### 8.2 `ontology/mechanism_tags.md`
- `agglomeration`
- `learning_spillovers`
- `matching`
- `sharing`
- `congestion`
- `coordination_failure`
- `path_dependence`
- `land_market_failure`

### 8.3 `ontology/policy_lever_tags.md`
- `integrated_planning`
- `metropolitan_governance`
- `land_use_planning`
- `zoning`
- `transport_investment`
- `citizen_engagement`
- `targeted_inclusion_programs`

### 8.4 `ontology/context_tags.md`
- `OECD`
- `developing`
- `low_income`
- `lower_middle_income`
- `upper_middle_income`
- `high_income`
- `incipient_urbanisation`
- `intermediate_urbanisation`
- `advanced_urbanisation`

### 8.5 `ontology/outcome_tags.md`
- `productivity`
- `wages`
- `employment`
- `housing_affordability`
- `accessibility`
- `emissions`
- `resilience`
- `trust`
- `livability`

### 8.6 `ontology/relationship_types.md`
- `supports`
- `qualifies`
- `contradicts`
- `depends_on`

### 8.7 `ontology/validation_rules.md` (minimum)
Include rules:
- Claim cards must include: `claim_text`, `claim_type`, `scope`, ≥1 tag in each tag group, ≥1 `sources` anchor.
- `claim_type` must be in `claim_types.md`.
- Tags must come from their ontology lists.
- IDs must be unique.

---

## 9) Ingestion instructions (write these files under `/ingestion/`)

### 9.1 `INGESTION_RULES.md`
Include these steps:
1. Register each new paper as a **source** (`/sources/source-####.md`).
2. Define section anchors (ToC headings, chapter IDs).
3. Read each section and extract **atomic claims** into `/claims/`.
4. Each claim must cite at least one source anchor.
5. Add qualifiers and context tags.
6. Link related claims using relationships.
7. Create or update concept cards when a term recurs.
8. Create/update synthesis pages by curating claim links.

### 9.2 `CHUNKING_GUIDELINES.md`
Even though RAG retrieves claims, chunking helps extraction. Add guidance:
- Chunk by heading + 1–3 paragraphs (semantic units).
- Prefer boxes/figures as separate chunks.
- Record page/section references in source anchors.

### 9.3 `CLAIM_EXTRACTION_GUIDELINES.md`
Include rules:
- One sentence; one idea.
- Capture causal direction if stated; otherwise use neutral association.
- Capture boundary conditions and “only if / varies by” language.
- Never invent numbers; if a source gives numbers, put them in claim_text precisely.
- Avoid policy prescriptions unless explicitly stated; otherwise store as design principles or tradeoffs.

### 9.4 `QA_CHECKLIST.md`
- Every claim has a source anchor.
- Every claim has qualifiers if needed.
- No claim duplicates.
- Tags conform to ontology.
- Synthesis pages contain links, not new facts.

---

## 10) README.md content (create this)

README must include:
- What this repo is for (RAG‑first city policy wiki)
- How to browse (start in `/synthesis/`)
- How LLM retrieval should work (retrieve claim cards first; expand with linked claims)
- How to contribute (add sources → claims → synthesis)

---

## 11) Starter content (create minimal examples)

Create:
- 8 synthesis hub files with headings and placeholder claim lists.
- At least 3 lever pages.
- At least 3 concept pages.
- At least 3 source pages.
- At least 10 claim cards using the template (content can be placeholders).

**All placeholders must still validate structurally** (IDs, tags, anchors).

---

## 12) Output expectation

The other LLM should:
1. Create the repo with the file structure.
2. Populate all ontology files.
3. Add templates and minimal starter content.
4. Ensure internal links use IDs (e.g., `[[claim-0001]]`).
5. Commit everything as an initial commit.
