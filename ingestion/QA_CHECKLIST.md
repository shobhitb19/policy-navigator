# QA Checklist

Run this checklist before committing a batch of new or updated claims.

## Per claim card

- [ ] `claim_id` is unique — no other file in `/claims/` uses this ID.
- [ ] `claim_text` is a single sentence.
- [ ] `claim_type` appears in `ontology/claim_types.md`.
- [ ] `scope.spatial` is present.
- [ ] At least one tag in `context_tags`, and all tags appear in `ontology/context_tags.md`.
- [ ] At least one tag in `mechanism_tags`, and all tags appear in `ontology/mechanism_tags.md`.
- [ ] At least one tag in `outcome_tags`, and all tags appear in `ontology/outcome_tags.md`.
- [ ] At least one tag in `policy_lever_tags`, and all tags appear in `ontology/policy_lever_tags.md`.
- [ ] `sources` contains at least one entry.
- [ ] Source anchor IDs match entries in the relevant source page's `anchors` list.
- [ ] `qualifiers` present if the source states any boundary conditions or caveats.
- [ ] `created` and `last_reviewed` are in `YYYY-MM-DD` format.
- [ ] No normative language in `claim_text` (unless `claim_type` is `design_principle` or `governance_requirement`).
- [ ] No invented numbers — all quantitative values traceable to source.

## Per source page

- [ ] `source_id` is unique.
- [ ] `title`, `authors`, `year`, `document_type` are present.
- [ ] At least one `anchors` entry with `id` and `label`.
- [ ] All anchor IDs used by claims in this ingestion batch are defined here.

## Cross-cutting

- [ ] No duplicate claims — existing claim corpus checked for overlapping ideas.
- [ ] Relationships (`supports`, `qualifies`, `contradicts`, `depends_on`) are populated where relevant.
- [ ] Synthesis hub pages updated with new claim IDs.
- [ ] New concepts added to `/concepts/` if recurring terms were introduced.
- [ ] `README.md` does not need updating (it links to synthesis hubs, not individual claims).

## Commit message

- [ ] Message follows format: `ingest: [source title]` or `update: [claim/concept] — [reason]`
