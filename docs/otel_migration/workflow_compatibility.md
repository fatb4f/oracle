# Workflow Compatibility Verification (M4)

This report defines the executable compatibility checks for VS Code-like and
Marimo-like workflows.

## Test suites

- `integration/tests/test_otel_workflow_compat.py::test_vscode_compat_suite`
  - validates `code.filepath` + `code.lineno`
  - validates schema-required span/event keys
  - validates correlation through `oracle.run_id` and `oracle.step_id`
- `integration/tests/test_otel_workflow_compat.py::test_marimo_compat_suite`
  - validates `oracle.notebook_id` + `oracle.cell_id`
  - validates schema-required span/event keys
  - validates correlation through `oracle.run_id` and `oracle.step_id`
- `integration/tests/test_otel_workflow_compat.py::test_deterministic_rerun_metadata_is_stable`
  - validates stable `oracle.variant_id`/`oracle.run_label`
  - validates stable step ordering (`oracle.seq`)
  - validates comparable guard/invariant outcomes across reruns
- `integration/tests/test_otel_workflow_compat.py::test_shared_env_config_model_supports_local_and_otlp`
  - validates one env-config model for local (`console`) and OTLP exporters

## Correlation contract

Both workflows must preserve:

- `oracle.run_id` on step span and adapter events
- `oracle.step_id` for event-to-step linkage
- `oracle.seq` (step ordering key)

## Provenance contract

- VS Code/editor runs: `code.filepath`, `code.lineno`
- Marimo runs: `oracle.notebook_id`, `oracle.cell_id`

## Materializer contract

`oracle.materializers.dsa.materialize_dsa_steps` must reconstruct:

- ordered steps by `oracle.seq`
- guard and invariant outcomes
- provenance keys for both workflows
