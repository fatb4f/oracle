#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

# shellcheck source=../conf.d/marimo/env.sh
source "$REPO_ROOT/conf.d/marimo/env.sh"

mkdir -p "$ORACLE_MARIMO_CONFIG_DIR" "$ORACLE_MARIMO_STATE_DIR" "$ORACLE_MARIMO_CACHE_DIR"

# Best-effort XDG isolation for deterministic local state.
export XDG_CONFIG_HOME="$(cd "$ORACLE_MARIMO_CONFIG_DIR" && pwd)"
export XDG_STATE_HOME="$(cd "$ORACLE_MARIMO_STATE_DIR" && pwd)"
export XDG_CACHE_HOME="$(cd "$ORACLE_MARIMO_CACHE_DIR" && pwd)"

exec uv run marimo edit "$@"
