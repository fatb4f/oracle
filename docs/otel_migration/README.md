# OTEL Migration Guide

This guide consolidates migration planning for deprecating `oracle_api` and
`oracle_tools` in favor of OTEL-native `oracle`.

## Scope and replacement mapping

- `oracle`: active and canonical
- `oracle_api`: deprecated, migration-only
- `oracle_tools`: deprecated, migration-only

Legacy to replacement mapping:

- `oracle_tools` -> `oracle` (OTEL-native adapters/materializers/helpers)
- `oracle_api` -> `oracle` (OTEL schema and runtime instrumentation surfaces)

Cutover rule:

- Docs, examples, and setup guides present `oracle` as the primary path.
- Legacy packages are referenced only in explicit deprecation notes.

## Evidence-first tool targets

- `pytest`, `hypothesis`
- `snoop`, `birdseye`
- `hunter`, `viztracer`
- `coverage`, `pytest-cov`

## OTEL compatibility contract

Required evidence metadata for all workflows:

- `oracle.evidence.schema_version`
- `oracle.run_id`
- deterministic step ordering key: `oracle.seq`
- one of `oracle.variant_id` or `oracle.run_label`
- guard and invariant outcome fields

The normative contract is:

- `spec/schema_contract.json`

The human-readable schema companion is:

- `spec/schema.md`

### VS Code compatibility

Compatibility is satisfied when:

1. VS Code runs emit OTEL traces for operations, guards, invariants, and
   transitions.
2. Tool outputs correlate to trace/run identifiers.
3. Editor provenance is present (`code.filepath`, `code.lineno` at minimum).
4. Export works for local (`console`/`file`) and OTLP endpoints via env vars.

### Marimo compatibility

Compatibility is satisfied when:

1. Cell execution emits OTEL traces/events with notebook provenance.
2. Notebook evidence views resolve trace/run identifiers.
3. Provenance keys are present (`oracle.notebook_id`, `oracle.cell_id`).
4. Deterministic rerun comparison metadata remains stable.

## Runtime configuration

`oracle` reads OTEL-style environment variables:

- `OTEL_TRACES_EXPORTER`: `none`, `console`, or `otlp`
- `OTEL_SERVICE_NAME`
- `OTEL_EXPORTER_OTLP_ENDPOINT`
- `OTEL_RESOURCE_ATTRIBUTES` (comma-separated `key=value`)

The runtime emits schema-aligned keys for Evidence-First DSA spans/events,
including required correlation and provenance attributes.

## Adapter and materializer contract (M3)

Each adapter path must emit one `oracle.step` span with required schema keys:

- `oracle.evidence.schema_version`
- `oracle.run_id`
- `oracle.seq`
- one of `oracle.variant_id` or `oracle.run_label`

Target behavior by tool family:

- `pytest`/`hypothesis`: map test examples to OTEL spans and assertion outcomes
- `snoop`/`birdseye`: adapt runtime introspection to OTEL events/linked records
- `hunter`/`viztracer`: map call and line traces to OTEL-linked structures
- `coverage`/`pytest-cov`: emit run-level coverage summaries as OTEL-linked
  evidence metadata

Materializer requirement:

- `oracle.materializers.dsa.materialize_dsa_steps` reconstructs ordered steps by
  `oracle.seq`, guard/invariant outcomes, and workflow provenance.

## Validation suites (M4)

Compatibility checks are defined in:

- `tests/integration/test_otel_workflow_compat.py::test_vscode_compat_suite`
- `tests/integration/test_otel_workflow_compat.py::test_marimo_compat_suite`
- `tests/integration/test_otel_workflow_compat.py::test_deterministic_rerun_metadata_is_stable`
- `tests/integration/test_otel_workflow_compat.py::test_shared_env_config_model_supports_local_and_otlp`

These checks verify schema keys, provenance, correlation, and rerun stability.

## Milestones and exit criteria

### M1: schema contract locked

- Schema documented and versioned.
- Required keys fixed.
- Validation fixture exists for one expected trace payload.

### M2: OTEL core runtime in `oracle`

- OTEL-native helpers for run/span/step/event emission are implemented.
- Runtime is independent of deprecated packages.
- Export configuration is env-var driven and documented.

### M3: adapter/materializer coverage

- Adapters/materializers implemented for all tool families.
- Adapter outputs preserve run/trace correlation.
- Non-native outputs are mapped or linked to OTEL evidence.

### M4: workflow compatibility validated

- VS Code compatibility milestones satisfied.
- Marimo compatibility milestones satisfied.
- Deterministic rerun metadata stable.

### M5: deprecation cutover complete

- Legacy imports removed from active paths.
- Docs and scripts use `oracle` as canonical target.
- Migration notes retained only as compatibility references.

## Tracker template

Use this tracker section for current status:

- M1: [ ]
- M2: [ ]
- M3: [ ]
- M4: [ ]
- M5: [ ]
