#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

# shellcheck source=../conf.d/vscode/env.sh
source "$REPO_ROOT/conf.d/vscode/env.sh"

if ! command -v "$CODE_BIN" >/dev/null 2>&1; then
  echo "vscode cli not found: $CODE_BIN" >&2
  exit 1
fi

mkdir -p "$ORACLE_VSCODE_USER_DATA_DIR" "$ORACLE_VSCODE_EXTENSIONS_DIR"

exec "$CODE_BIN" \
  --profile "$ORACLE_VSCODE_PROFILE" \
  --user-data-dir "$ORACLE_VSCODE_USER_DATA_DIR" \
  --extensions-dir "$ORACLE_VSCODE_EXTENSIONS_DIR" \
  "$@"
