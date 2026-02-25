# Documentation

This directory is consolidated into a small set of canonical guides.

## Core docs

- `docs/overview.md`: project purpose, OTEL evidence model, canonical package,
  and package status.
- `docs/setup_and_workflow.md`: environment setup, worktrees, VS Code + Marimo
  flow, and the canonical Evidence-First DSA workflow.

## OTEL migration

- `docs/otel_migration/README.md`: migration plan, compatibility contract,
  adapter/materializer expectations, milestone tracker, and replacement mapping.
- `spec/schema_contract.json`: machine-readable schema contract.

## Rule of use

For all new setup, imports, runtime instrumentation, adapters, and
materializers, use `oracle` as the canonical package.

`oracle_api` and `oracle_tools` are deprecated and retained only for migration
compatibility.
