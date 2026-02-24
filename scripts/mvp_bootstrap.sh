#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

echo "[mvp] syncing uv env (dev group)"
uv sync --dev

echo "[mvp] validating core integration gates"
uv run pytest -q \
  integration/tests/test_deprecation_enforcement.py \
  integration/tests/test_imports.py \
  integration/tests/test_otel_schema_contract.py \
  integration/tests/test_oracle_otel_runtime.py \
  integration/tests/test_oracle_otel_adapters.py \
  integration/tests/test_otel_workflow_compat.py

echo "[mvp] done"
echo "[mvp] launch marimo: uv run marimo edit"
