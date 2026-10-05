# Validation Rules

## Claim card requirements

A claim card is valid only if:

1. `claim_text` is present and is a single sentence.
2. `claim_type` is present and its value appears in `ontology/claim_types.md`.
3. `scope.spatial` is present.
4. At least one tag is present in each of: `context_tags`, `mechanism_tags`, `outcome_tags`, `policy_lever_tags`.
5. `sources` contains at least one entry in the format `source-####` or `source-#####anchor-id`.
6. All tags in each tag field appear in the corresponding ontology file.
7. `claim_id` is unique across all files in `/claims/`.
8. `created` and `last_reviewed` are present in `YYYY-MM-DD` format.

## Source page requirements

A source page is valid only if:

1. `source_id` is unique across all files in `/sources/`.
2. `title`, `authors`, `year`, and `document_type` are present.
3. `anchors` contains at least one entry with `id` and `label`.

## Tag conformance

- `claim_type` → `ontology/claim_types.md`
- `mechanism_tags` → `ontology/mechanism_tags.md`
- `policy_lever_tags` → `ontology/policy_lever_tags.md`
- `context_tags` → `ontology/context_tags.md`
- `outcome_tags` → `ontology/outcome_tags.md`
- Relationship types → `ontology/relationship_types.md`

## ID format

- Claims: `claim-NNNN` (four-digit zero-padded integer)
- Sources: `source-NNNN` (four-digit zero-padded integer)
- Evidence: `evidence-NNNN` (four-digit zero-padded integer)
- Concepts: slug matching the filename (e.g., `agglomeration_economies` for `agglomeration-economies.md`)

## Retired content

Do not delete retired claims or sources. Set `status: retired` in frontmatter and add a `retirement_reason` field.
