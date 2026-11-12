#!/usr/bin/env bash
# Rebuilds the two distributable files from the cv-match-coach/ folder:
#   cv-match-coach.zip               – upload as a ChatGPT skill
#   cv-match-coach-all-in-one.md     – one text file: attach, link, or upload to a Project
# Run from the repo root after every change to the skill:  ./build.sh
set -euo pipefail
cd "$(dirname "$0")"

SKILL=cv-match-coach
OUT=cv-match-coach-all-in-one.md
VERSION=$(date +%Y-%m-%d)

rm -f "$SKILL.zip"
zip -rq "$SKILL.zip" "$SKILL" -x "*.DS_Store"

{
  echo "# CV Match Coach – all-in-one (version $VERSION)"
  echo
  echo "This single file contains the complete CV Match Coach skill. Each part starts with a line '=== FILE: <path> ==='."
  echo "Treat the part 'SKILL.md' as your instructions for this whole chat. When SKILL.md refers to a file such as"
  echo "'references/workflow.md', use the part with that path below. Read the whole file before starting."
  echo "The file ends with the line 'END-OF-CV-MATCH-COACH $VERSION'."
  echo
  for f in "$SKILL/SKILL.md" "$SKILL"/references/*.md "$SKILL"/examples/example-*.md "$SKILL"/scripts/*.py; do
    echo "=== FILE: ${f#"$SKILL"/} ==="
    echo
    case "$f" in *.py) echo '```python'; cat "$f"; echo '```' ;; *) cat "$f" ;; esac
    echo
  done
  echo "END-OF-CV-MATCH-COACH $VERSION"
} > "$OUT"

echo "Built $SKILL.zip and $OUT ($(wc -c < "$OUT") bytes)"

# Public-repo guard: warn if the zip contains anything other than the skill's markdown files
EXTRA=$(unzip -Z1 "$SKILL.zip" | grep -v -E '/$|\.md$|^cv-match-coach/scripts/[a-z_]+\.py$' || true)
if [ -n "$EXTRA" ]; then
  echo
  echo "WARNING: $SKILL.zip contains files other than the skill's markdown and scripts:"
  echo "$EXTRA" | sed 's/^/  /'
  echo "Upload this zip to ChatGPT, but do NOT commit it to the public repo (git checkout -- $SKILL.zip)."
fi
