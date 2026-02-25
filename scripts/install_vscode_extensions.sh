#!/usr/bin/env bash
set -euo pipefail

CODE_BIN="${CODE_BIN:-code}"
CODEX_VSCODE_EXTENSION_ID="${CODEX_VSCODE_EXTENSION_ID:-openai.chatgpt}"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# shellcheck source=../conf.d/vscode/env.sh
source "$REPO_ROOT/conf.d/vscode/env.sh"

if ! command -v "$CODE_BIN" >/dev/null 2>&1; then
  echo "vscode cli not found: $CODE_BIN" >&2
  exit 1
fi

mkdir -p "$ORACLE_VSCODE_USER_DATA_DIR" "$ORACLE_VSCODE_EXTENSIONS_DIR"

install_required() {
  local ext="$1"
  timeout 60s "$CODE_BIN" \
    --user-data-dir "$ORACLE_VSCODE_USER_DATA_DIR" \
    --extensions-dir "$ORACLE_VSCODE_EXTENSIONS_DIR" \
    --profile "$ORACLE_VSCODE_PROFILE" \
    --install-extension "$ext"
}

install_optional() {
  local ext="$1"
  if timeout 45s "$CODE_BIN" \
    --user-data-dir "$ORACLE_VSCODE_USER_DATA_DIR" \
    --extensions-dir "$ORACLE_VSCODE_EXTENSIONS_DIR" \
    --profile "$ORACLE_VSCODE_PROFILE" \
    --install-extension "$ext"; then
    return 0
  fi
  echo "optional extension unavailable: $ext"
  return 0
}

install_required ms-python.python
# Pylance is unavailable in some OpenVSX-backed distributions.
install_optional ms-python.vscode-pylance
install_optional ms-python.vscode-python-envs
install_optional "$CODEX_VSCODE_EXTENSION_ID"

echo "installed extension set via $CODE_BIN"
echo "codex extension id used: $CODEX_VSCODE_EXTENSION_ID"
echo "profile: $ORACLE_VSCODE_PROFILE"
echo "user-data-dir: $ORACLE_VSCODE_USER_DATA_DIR"
echo "extensions-dir: $ORACLE_VSCODE_EXTENSIONS_DIR"
