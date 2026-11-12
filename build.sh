#!/usr/bin/env bash
# Rebuilds cv-match-coach.zip, cv-match-coach-all-in-one.md, CHECKSUMS.txt and the
# README checksum block. Deterministic: same skill files -> identical output and checksum.
# Run from anywhere:  ./build.sh        (or: python3 tools/build.py [--check])
set -euo pipefail
exec python3 "$(dirname "$0")/tools/build.py" "$@"
