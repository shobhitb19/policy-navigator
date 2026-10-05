#!/usr/bin/env bash
# Build and deploy the wiki to gh-pages.
#
# IMPORTANT: source documents (PDF/PPTX/etc.) are NOT published to the site. Most are
# third-party copyright material we have no right to rehost, and two are in-confidence:
# the Treasury Auckland Story (IN-CONFIDENCE draft) and the Kānoa population presentation
# (internal). The source *cards* (source-XXXX.md) carry the citation and quoted extracts,
# which is all the wiki needs; the documents stay in the repo working tree only.
#
# Note: the MartinJenkins Tāmaki Makaurau report was publicly released and is no longer
# restricted (see sources/source-0046.md), but is still not rehosted here — link to the
# publisher's copy instead.
#
# Usage: scripts/deploy_wiki.sh
set -euo pipefail

cd "$(dirname "$0")/.."

rm -rf _wiki _site
mkdir -p _wiki
cp README.md llms.txt _wiki/
cp -r claims sources synthesis levers places concepts evidence docs ontology ingestion _wiki/

# Strip source documents (PDF/PPTX/XLSX/DOCX) from the copied tree. llms.txt and
# any other web assets are kept.
find _wiki -type f \( -iname '*.pdf' -o -iname '*.pptx' -o -iname '*.ppt' \
  -o -iname '*.xlsx' -o -iname '*.xls' -o -iname '*.docx' -o -iname '*.doc' \) \
  -print -delete | sed 's/^/  excluded: /'

python3 scripts/generate_plain_html.py
mkdocs gh-deploy --force

rm -rf _wiki _site

echo
echo "Deployed. Verifying no binaries reached gh-pages…"
git fetch origin gh-pages --quiet
LEAKED=$(git ls-tree -r origin/gh-pages --name-only \
  | grep -iE '\.(pdf|pptx?|xlsx?|docx?)$' || true)
if [ -n "$LEAKED" ]; then
  echo "WARNING — non-web files found on gh-pages:"
  echo "$LEAKED"
  exit 1
fi
echo "OK: no source documents on the deployed site."
git log origin/gh-pages -1 --format="gh-pages: %H %ad %s" --date=iso
