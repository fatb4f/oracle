# Changelog

## [25b647a] - 2026-02-12
### Added
- Created `packages/oracle_api` with stable API primitives (`contracts`, `control`, `trace`, `seeded`).
- Created `packages/oracle_tools` with tooling helpers (budget + mermaid renderers).
- Added integration smoke test: `tests/integration/test_imports.py`.

### Changed
- Split `experiment.py` into `oracle_tools/budget.py` and `oracle_api/seeded.py`.
- Migrated variable content into `courses/inf2220/content/**`.
- Added `courses/inf1250/` placeholder.
- Moved documentation to top-level `docs/`.

### Removed
- Removed deprecated `.codex/` directory entirely.

### Verified
- Tests: 13 passed with `PYTHONPATH` pointing at both package `src/` dirs.
