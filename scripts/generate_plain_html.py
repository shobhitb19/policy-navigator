#!/usr/bin/env python3
"""Generate the bare, no-JS /plain/ HTML layer that llms.txt links to.

Run from the repo root after populating _wiki/ (see CLAUDE.md), before
`mkdocs gh-deploy`. Writes into _wiki/plain/.
"""
import pathlib
import re

import markdown

PLAIN_DIRS = ["claims", "synthesis", "levers", "places", "concepts", "evidence", "ontology", "sources"]

# Relative links between source .md files (e.g. href="claim-0162.md" or
# href="../sources/source-0028.md#anchor") must point at the sibling .html
# file in the mirrored /plain/ tree, not the nonexistent .md path.
RELATIVE_MD_LINK = re.compile(r'href="((?!https?://)[^"]+?)\.md(#[^"]*)?"')


def wrap(title, body):
    return (
        f'<!DOCTYPE html><html lang="en"><head>'
        f'<meta charset="utf-8"><title>{title}</title>'
        f'</head><body>\n{body}\n</body></html>'
    )


def rewrite_md_links(html):
    return RELATIVE_MD_LINK.sub(lambda m: f'href="{m.group(1)}.html{m.group(2) or ""}"', html)


def main():
    md = markdown.Markdown(extensions=["tables", "fenced_code", "toc", "attr_list"])

    for d in PLAIN_DIRS:
        for f in sorted(pathlib.Path(d).glob("*.md")):
            md.reset()
            body = rewrite_md_links(md.convert(f.read_text(encoding="utf-8")))
            out = pathlib.Path(f"_wiki/plain/{d}/{f.stem}.html")
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(wrap(f.stem, body), encoding="utf-8")

    lines = [
        '<!DOCTYPE html><html><head><meta charset="utf-8">'
        "<title>Plain HTML index</title></head><body>",
        "<h1>Plain HTML files for LLM retrieval</h1>",
        "<p>All files below are plain HTML with no JavaScript.</p>",
    ]
    for d in PLAIN_DIRS:
        lines.append(f"<h2>{d}</h2><ul>")
        for f in sorted(pathlib.Path(d).glob("*.md")):
            lines.append(f'<li><a href="{d}/{f.stem}.html">{f.stem}</a></li>')
        lines.append("</ul>")
    lines.append("</body></html>")
    pathlib.Path("_wiki/plain/index.html").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
