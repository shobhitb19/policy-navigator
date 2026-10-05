# Contributing

## Before you start

- Read [`HOW_IT_WORKS.md`](HOW_IT_WORKS.md) to understand the knowledge model.
- Read [`/ingestion/INGESTION_RULES.md`](../ingestion/INGESTION_RULES.md) for the step-by-step ingestion workflow.
- Check `/ontology/` for allowed tags before writing new claims.

## Adding a new source

1. Create `/sources/source-####.md` using the template in `HOW_IT_WORKS.md`.
2. Assign the next available sequential ID.
3. Define section anchors for all chapters or sections you will cite.

## Adding claims

1. Create `/claims/claim-####.md` using the claim card template.
2. Every claim must have `claim_text`, `claim_type`, `scope`, at least one tag per tag group, and at least one `sources` anchor.
3. All tags must come from the relevant ontology file.
4. Capture qualifiers and caveats — do not upgrade hedged findings to facts.

## Updating existing claims

- Add the new source to the claim's `sources` list and update `supporting_excerpt`.
- If the new source contradicts the claim, add it to `relationships.contradicts` and note the contradiction in `qualifiers`.
- Update `last_reviewed`.

## Adding concepts

- One concept per file in `/concepts/`.
- Link related claims using `linked_claims`.

## Updating synthesis pages

- Add new claim IDs to the relevant synthesis hub's key claim index.
- Do not add new factual assertions to synthesis pages — link to a claim instead.

## Commit messages

Use the format: `ingest: [source title or short description]`

For updates: `update: [claim ID or concept] — [reason]`
