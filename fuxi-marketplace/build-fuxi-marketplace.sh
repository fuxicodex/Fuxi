#!/usr/bin/env bash
# build-fuxi-marketplace.sh — package the FuXi official marketplace (fuxi-plugins)
# into the layout the FUXI download server serves and official_marketplace_gcs.go
# consumes.
#
# Contract (matches internal/services/plugins/official_marketplace_gcs.go):
#   - the FUXI consumer GETs:
#       <base>/plugins/fuxi-plugins/latest            → 40-char SHA
#       <base>/plugins/fuxi-plugins/{sha}.zip         → the marketplace zip
#     where <base> = $FUXI_DOWNLOAD_BASE_URL or https://downloads.fuxicode.com
#   - the zip arc root is "plugins/fuxi-plugins/" (gcsArcPrefix) so the extractor
#     strips it and the materialized dir lands at
#     marketplaces/fuxi-plugins/ holding .claude-plugin/marketplace.json.
#
# So this script produces dist/PLUGINS/fuxi-plugins/{latest,<sha>.zip} — the exact
# path tree to upload to the server (upload dist/plugins / as /plugins /).
#
# Usage:
#   ./build-fuxi-marketplace.sh          # builds into ./dist (server path tree)
#   OUTPUT_DIR=/path ./build-fuxi-marketplace.sh
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC_DIR="$SCRIPT_DIR/plugins/fuxi-plugins"            # the rebranded marketplace content
OUT_DIR="${OUTPUT_DIR:-$SCRIPT_DIR/dist}"
MKT_DIR="$OUT_DIR/plugins/fuxi-plugins"               # server path tree root (the <base>/plugins/fuxi-plugins/ subtree)
ARC_PREFIX="plugins/fuxi-plugins"                     # gcsArcPrefix (zip arc root)

if [ ! -f "$SRC_DIR/.claude-plugin/marketplace.json" ]; then
  echo "ERROR: $SRC_DIR/.claude-plugin/marketplace.json not found" >&2
  exit 1
fi

mkdir -p "$MKT_DIR"
STAGE="$(mktemp -d)"
trap 'rm -rf "$STAGE"' EXIT

# 1. Compute a deterministic CONTENT SHA of the marketplace tree (content-addressed,
#    like the archive's git-SHA key). A plain `git -C` HEAD would walk UP to an
#    enclosing unrelated repo (this directory is NOT its own checkout), producing a
#    SHA that never changes when the marketplace content changes — the `latest`
#    pointer would then stay stale and FUXI's sentinel would no-op forever. So hash
#    every file's content (sorted for determinism), excluding .git.
#    A rebrand/edit therefore changes the SHA, the new zip is named by it, and the
#    consumer's .gcs-sha sentinel correctly re-downloads.
SHA="$(
  cd "$SRC_DIR" && find . -type f -not -path './.git/*' -not -name '.DS_Store' \
    -print0 | sort -z | xargs -0 shasum 2>/dev/null \
    | shasum | awk '{print $1}'
)"
echo "marketplace content SHA: $SHA"

# 2. Build the zip with the ARC prefix. The zip root must be
#    plugins/fuxi-plugins/<content> so gcsArcPrefix strip yields the content root.
( cd "$SCRIPT_DIR" && zip -qr "$STAGE/$SHA.zip" "$ARC_PREFIX" )
echo "packed: $STAGE/$SHA.zip ($(du -h "$STAGE/$SHA.zip" | cut -f1))"

# 3. Write the `latest` pointer (the exact string the extractor reads).
printf '%s' "$SHA" > "$STAGE/latest"

# 4. Verify zip entries carry the arc prefix. Capture output FIRST (a `grep -q`
#    under set -o pipefail closes the pipe early and SIGPIPEs unzip, flipping the
#    `!` into a false failure — the same trap the release scripts warn about).
list_out="$(unzip -l "$STAGE/$SHA.zip")"
if ! printf '%s\n' "$list_out" | grep -q "$ARC_PREFIX/.claude-plugin/marketplace.json"; then
  echo "ERROR: zip is missing the arc-prefixed marketplace manifest" >&2
  exit 1
fi

# 5. Place into the server path tree (<base>/plugins/fuxi-plugins/…).
mv "$STAGE/$SHA.zip" "$MKT_DIR/$SHA.zip"
mv "$STAGE/latest" "$MKT_DIR/latest"

echo ""
echo "server-path tree ready (upload this as /plugins/fuxi-plugins/ on your server):"
ls -la "$MKT_DIR"