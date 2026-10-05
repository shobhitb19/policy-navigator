#!/usr/bin/env python3
"""
Build plain HTML files for LLM retrieval.
Output goes to ./plain/ — no scripts, no styles, pure content.
"""
import markdown
import pathlib

DIRS = ['claims', 'synthesis', 'levers', 'places', 'concepts', 'ontology', 'sources']

EXTENSIONS = ['tables', 'fenced_code', 'toc', 'attr_list']

def plain_html(title, body):
    return (
        '<!DOCTYPE html>\n'
        '<html lang="en">\n'
        '<head><meta charset="utf-8">'
        f'<title>{title}</title>'
        '</head>\n'
        f'<body>\n{body}\n</body>\n</html>\n'
    )

def build():
    md = markdown.Markdown(extensions=EXTENSIONS)
    out_root = pathlib.Path('plain')

    for d in DIRS:
        src = pathlib.Path(d)
        if not src.exists():
            continue
        for f in sorted(src.glob('*.md')):
            md.reset()
            body = md.convert(f.read_text(encoding='utf-8'))
            out = out_root / d / (f.stem + '.html')
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(plain_html(f.stem, body), encoding='utf-8')
            print(f'  {out}')

    # Index page listing everything
    lines = [
        '<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">',
        '<title>Place-Based Policy Wiki — LLM Index</title></head><body>',
        '<h1>Place-Based Policy Wiki — LLM retrieval index</h1>',
        '<p>All pages below are plain HTML. No JavaScript required.</p>',
        '<p>Start with a synthesis hub, then follow claim links. '
        'Each claim page has a YAML block with relationship links to related claims.</p>',
    ]
    for d in DIRS:
        src = pathlib.Path(d)
        if not src.exists():
            continue
        files = sorted(src.glob('*.md'))
        if not files:
            continue
        lines.append(f'<h2>{d}</h2><ul>')
        for f in files:
            lines.append(f'<li><a href="{d}/{f.stem}.html">{f.stem}</a></li>')
        lines.append('</ul>')
    lines.append('</body></html>')

    idx = out_root / 'index.html'
    idx.parent.mkdir(parents=True, exist_ok=True)
    idx.write_text('\n'.join(lines), encoding='utf-8')
    print(f'  {idx}')

if __name__ == '__main__':
    build()
    print('Done.')
