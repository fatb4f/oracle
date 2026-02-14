from __future__ import annotations

import json
import random
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ORACLE_SRC = ROOT / "packages" / "oracle" / "src"
SCHEMA_CONTRACT_PATH = ROOT / "docs" / "otel_migration" / "schema_contract.json"
if str(ORACLE_SRC) not in sys.path:
    sys.path.insert(0, str(ORACLE_SRC))

from oracle import OTelRuntime, load_otel_config, materialize_dsa_steps
from oracle.adapters import emit_pytest_hypothesis_case, emit_snoop_trace


def _load_schema_contract() -> dict:
    return json.loads(SCHEMA_CONTRACT_PATH.read_text(encoding="utf-8"))


def _assert_span_contract(contract: dict, attrs: dict) -> None:
    for key in contract["span"]["required_attributes"]:
        assert key in attrs, f"missing span key {key}"
    for one_of in contract["span"]["required_one_of"]:
        assert any(key in attrs for key in one_of), f"missing one_of keys: {one_of}"


def _assert_event_contract(contract: dict, events: dict[str, dict]) -> None:
    for event_name in ("oracle.guard", "oracle.invariant", "oracle.explanation"):
        attrs = events[event_name]
        event_contract = contract["events"][event_name]
        for key in event_contract["required_attributes"]:
            assert key in attrs, f"missing event key {key} for {event_name}"
        for enum_key, allowed_values in event_contract["enums"].items():
            assert attrs[enum_key] in allowed_values


def _get_event_attrs(span, event_name: str) -> dict:
    for event in span.events:
        if event.name == event_name:
            return event.attributes
    raise AssertionError(f"missing event {event_name}")


def test_vscode_compat_suite() -> None:
    contract = _load_schema_contract()
    rt = OTelRuntime.from_env({"OTEL_TRACES_EXPORTER": "none"})
    rt.set_provenance_file("integration/tests/test_otel_workflow_compat.py", 60)

    step = emit_pytest_hypothesis_case(
        rt,
        run_id="run-vscode-001",
        seq=1,
        nodeid="tests/test_algo.py::test_dijkstra",
        outcome="pass",
        hypothesis_example={"start": "A", "end": "D"},
        run_label="vscode-baseline",
    )

    _assert_span_contract(contract, step.attributes)
    assert step.attributes["code.filepath"] == "integration/tests/test_otel_workflow_compat.py"
    assert step.attributes["code.lineno"] == 60

    case_event = _get_event_attrs(step, "oracle.pytest.case")
    assert case_event["oracle.run_id"] == "run-vscode-001"
    assert case_event["oracle.step_id"] == "pytest:tests/test_algo.py::test_dijkstra"
    assert case_event["oracle.pytest.outcome"] == "pass"
    _assert_event_contract(contract, {event.name: event.attributes for event in step.events})

    materialized = materialize_dsa_steps(rt.spans)
    assert materialized["steps"][0]["run_id"] == "run-vscode-001"
    assert materialized["steps"][0]["seq"] == 1
    assert materialized["steps"][0]["guards"][0]["status"] == "pass"


def test_marimo_compat_suite() -> None:
    contract = _load_schema_contract()
    rt = OTelRuntime.from_env({"OTEL_TRACES_EXPORTER": "none"})
    rt.set_provenance_cell("nb-compat-01", "cell-003")

    step = emit_snoop_trace(
        rt,
        run_id="run-marimo-001",
        seq=2,
        records=[
            {"seq": 1, "message": "dist[A]=0", "filepath": "graph.py", "lineno": 12},
            {"seq": 2, "message": "visit(B)", "filepath": "graph.py", "lineno": 14},
        ],
        run_label="marimo-baseline",
    )

    _assert_span_contract(contract, step.attributes)
    assert step.attributes["oracle.notebook_id"] == "nb-compat-01"
    assert step.attributes["oracle.cell_id"] == "cell-003"

    snoop_event = _get_event_attrs(step, "oracle.snoop.event")
    assert snoop_event["oracle.run_id"] == "run-marimo-001"
    assert snoop_event["oracle.step_id"] == "snoop.trace"
    _assert_event_contract(contract, {event.name: event.attributes for event in step.events})

    materialized = materialize_dsa_steps(rt.spans)
    assert materialized["steps"][0]["run_id"] == "run-marimo-001"
    assert materialized["steps"][0]["provenance"]["oracle.notebook_id"] == "nb-compat-01"
    assert materialized["steps"][0]["invariants"][0]["status"] == "pass"


def _deterministic_signature(seed: int) -> dict[str, object]:
    generator = random.Random(seed)
    run_id = f"run-seeded-{seed}"
    variant_id = f"variant-seed-{seed}"
    run_label = "deterministic-seeded"
    outcome = "pass" if generator.randint(0, 1) == 0 else "fail"

    rt = OTelRuntime.from_env({"OTEL_TRACES_EXPORTER": "none"})
    emit_pytest_hypothesis_case(
        rt,
        run_id=run_id,
        seq=1,
        nodeid="tests/test_algo.py::test_seeded",
        outcome=outcome,
        hypothesis_example={"seed": seed},
        variant_id=variant_id,
        run_label=run_label,
    )

    materialized = materialize_dsa_steps(rt.spans)
    step = materialized["steps"][0]
    return {
        "variant_id": step.get("variant_id"),
        "run_label": step.get("run_label"),
        "seq": step["seq"],
        "guard_statuses": [guard["status"] for guard in step["guards"]],
        "invariant_statuses": [inv["status"] for inv in step["invariants"]],
    }


def test_deterministic_rerun_metadata_is_stable() -> None:
    first = _deterministic_signature(seed=17)
    second = _deterministic_signature(seed=17)
    assert first == second
    assert first["seq"] == 1
    assert first["variant_id"] == "variant-seed-17"
    assert first["run_label"] == "deterministic-seeded"


def test_shared_env_config_model_supports_local_and_otlp() -> None:
    shared = {
        "OTEL_SERVICE_NAME": "oracle-m4",
        "OTEL_RESOURCE_ATTRIBUTES": "deployment.environment=ci,service.namespace=oracle",
    }

    local_cfg = load_otel_config({**shared, "OTEL_TRACES_EXPORTER": "console"})
    otlp_cfg = load_otel_config(
        {
            **shared,
            "OTEL_TRACES_EXPORTER": "otlp",
            "OTEL_EXPORTER_OTLP_ENDPOINT": "http://localhost:4318",
        }
    )

    assert local_cfg.service_name == otlp_cfg.service_name == "oracle-m4"
    assert local_cfg.resource_attributes["deployment.environment"] == "ci"
    assert otlp_cfg.resource_attributes["service.namespace"] == "oracle"
    assert local_cfg.traces_exporter == "console"
    assert otlp_cfg.traces_exporter == "otlp"
    assert otlp_cfg.otlp_endpoint == "http://localhost:4318"
