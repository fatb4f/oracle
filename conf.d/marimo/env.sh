# shellcheck shell=bash

# Best-effort deterministic Marimo state directories.
# Marimo may still use additional platform defaults depending on version.
: "${ORACLE_MARIMO_CONFIG_DIR:=.state/marimo/config}"
: "${ORACLE_MARIMO_STATE_DIR:=.state/marimo/state}"
: "${ORACLE_MARIMO_CACHE_DIR:=.state/marimo/cache}"
