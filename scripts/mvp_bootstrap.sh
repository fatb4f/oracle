#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

echo "[mvp] syncing uv env (dev group)"
uv sync --dev

echo "[mvp] validating integration gates"
"$REPO_ROOT/scripts/mvp_tests.sh"

echo "[mvp] done"
echo "[mvp] launch marimo: uv run marimo edit"
