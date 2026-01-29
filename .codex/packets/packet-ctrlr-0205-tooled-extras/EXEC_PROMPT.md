# Packet 0205 — Tooling extras

## Intent
Add pyproject extras for tooling used in coursework.

## Deliverables
- `pyproject.toml` extras groups
- Tests for import guards (minimal install import + helpful errors)

## Constraints
- Base install must import `ctrlr` without extras.
- Optional features should raise helpful errors naming the extra.

## Suggested extras
- `test = ["pytest", "hypothesis"]`
- `surfacing = ["marimo"]`
- `inspect = ["snoop", "birdseye"]`
- `otel = ["opentelemetry-api"]` (only what is used)
- `dev = ["ctrlr[test,surfacing,inspect,otel]"]`

## Evidence
- Pytest log
- Diffstat
