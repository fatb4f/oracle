#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

INTEGRATION_TEST_DIR="tests/integration"

echo "[tests] integration gate suite"
uv run pytest -q "$INTEGRATION_TEST_DIR"
