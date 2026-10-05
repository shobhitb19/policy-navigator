# Ingestion Rules

Follow these steps when adding a new source document to the wiki.

## Step 1: Register the source

1. Create `/sources/source-####.md` using the source template (see `docs/HOW_IT_WORKS.md`).
2. Assign the next available sequential ID.
3. Set `ingestion_status: not_started`.

## Step 2: Define section anchors

4. Read the document's table of contents or chapter structure.
5. Add an anchor entry for each chapter, section, or named figure you plan to cite.
6. Anchor IDs must be stable — use slugified headings (e.g., `chapter-2#section-2-1`).

## Step 3: Extract claims

7. Read each section and identify atomic, citable claims.
8. For each claim, create `/claims/claim-####.md`.
9. Each claim must:
   - Cite at least one source anchor.
   - Have a valid `claim_type` from the ontology.
   - Have at least one tag in each tag group.
   - Have `qualifiers` if the source states any boundary conditions or caveats.

## Step 4: Link relationships

10. After extracting all claims from the document, review relationships between them.
11. Add `supports`, `qualifies`, `contradicts`, and `depends_on` links where appropriate.
12. Also check existing claims — does the new source confirm, contradict, or update any?

## Step 5: Create or update concept cards

13. If a term is used repeatedly across claims, check `/concepts/` for an existing card.
14. If none exists, create `/concepts/[term-slug].md`.
15. Add `linked_claims` references in the concept card.

## Step 6: Update synthesis pages

16. Add new claim IDs to the relevant synthesis hub's key claim index.
17. Do not add new factual assertions directly to synthesis pages.

## Step 7: Update ingestion status

18. Set `ingestion_status: claims_extracted` in the source page when done.

## Step 8: Commit

19. Commit with message: `ingest: [source title]`
