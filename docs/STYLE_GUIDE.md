# Style Guide

## Claim text

- One sentence. One idea.
- Use present tense for structural relationships ("Doubling city size is associated with…").
- Use past tense only when the finding is specific to a historical period ("Between 1990 and 2015, cities in X experienced…").
- Avoid normative language. Claims describe evidence, not recommendations.
- If the source hedges ("suggests", "is consistent with", "may reflect"), preserve that hedge in the claim text.
- Include quantitative estimates when the source provides them ("…by approximately 2–5%").

## Qualifiers

- Required whenever the source states a boundary condition, sample restriction, or caveat.
- Write as plain bullets, not full sentences.
- Examples: "Estimated for OECD cities; may not generalise to developing contexts." / "Effect size varies by city size."

## Tags

- Use only tags listed in the relevant ontology file.
- Prefer more specific tags over broader ones when both apply.
- `context_tags` describe where the evidence was gathered, not where the claim might apply.

## Source anchors

- Anchor IDs must match exactly what is defined in the source page's `anchors` list.
- Format: `source-#####anchor-id`

## Prose in synthesis and lever pages

- Short paragraphs. No filler.
- Every factual assertion must link to a claim ID.
- Use standard markdown links for claim references: `[claim-0001](../claims/claim-0001.md)`
- From `synthesis/`, `places/`, and `levers/`, the relative path to claims is `../claims/claim-XXXX.md`

## Claim card bodies

Each claim card has a YAML frontmatter block followed by a markdown body. The body must include:

- `## Source` — markdown links to the source file(s), e.g. `[Donovan et al. (2021)](../sources/source-0004.md) — [section 4.1](../sources/source-0004.md#section-4-1)`
- `## Related claims` — markdown links for any non-empty relationship fields (supports, qualifies, contradicts, depends_on)

## Source file bodies

Source files must include `<a id="...">` anchor tags before each section heading, matching the `id` values declared in the YAML `anchors` or `sections` list. This enables claim cards to link directly to specific sections.

## Frontmatter dates

- Format: `YYYY-MM-DD`
- `created`: date the file was first written.
- `last_reviewed`: date the file was last checked for accuracy.
