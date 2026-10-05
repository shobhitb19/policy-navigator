# Chunking Guidelines

These guidelines support claim extraction by creating a consistent mapping between document structure and source anchors.

## Chunk boundaries

- Chunk at the heading level: each `##` or `###` heading starts a new chunk.
- A chunk typically covers one heading plus 1–3 paragraphs of body text.
- Do not split a logical argument across chunks if it spans only a short section.

## Figures and boxes

- Treat each figure, table, or box as its own chunk.
- Record the figure title and page number in the source anchor.
- Do not fabricate data values from chart images. Record direction, ranking, and order of magnitude only.

## Page and section references

- Record the page number or slide number in the anchor ID where possible.
- For reports: `chapter-N#section-N-M` is the preferred anchor format.
- For slide decks: `slide-N` is the preferred anchor format.
- For web pages: use the heading slug as the anchor ID.

## Chunk size

- Aim for chunks of 200–600 words.
- Very long sections should be split at sub-heading boundaries even if the sub-heading is minor.
- Very short sections (a single paragraph or a definition) can be included within the parent heading's chunk.

## Recording chunks

- You do not need to store chunk text in the repo.
- The source anchor in a claim card (`source-0001#chapter-2#section-2-1`) serves as the pointer.
- If you are building a vector index, embed each chunk tagged with its source anchor ID so retrieved chunks can be traced back to specific claims.
