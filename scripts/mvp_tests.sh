#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

echo "[tests] core integration gate suite"
uv run pytest -q \
  integration/tests/test_deprecation_enforcement.py \
  integration/tests/test_imports.py \
  integration/tests/test_otel_schema_contract.py \
  integration/tests/test_oracle_otel_runtime.py \
  integration/tests/test_oracle_otel_adapters.py \
  integration/tests/test_otel_workflow_compat.py

echo "[tests] extra migration compatibility suite"
PYTHONPATH="packages/oracle_api/src:packages/oracle_tools/src" \
  uv run pytest -q \
  packages/oracle_api/tests \
  packages/oracle_tools/tests
