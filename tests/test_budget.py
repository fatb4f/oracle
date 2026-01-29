import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from ctrlr import Budget, budget


def test_budget_construction_defaults() -> None:
    b = Budget(limit=10)
    assert b.used == 0
    assert b.remaining == 10
    assert b.label is None


def test_budget_construction_invariants() -> None:
    with pytest.raises(ValueError):
        Budget(limit=-1)
    with pytest.raises(ValueError):
        Budget(limit=1, used=-1)
    with pytest.raises(ValueError):
        Budget(limit=1, used=2)


def test_budget_consume_monotonic() -> None:
    b = Budget(limit=5, used=1)
    ok = b.consume(2)
    assert ok is True
    assert b.used == 3
    assert b.remaining == 2


def test_budget_consume_overflow() -> None:
    b = Budget(limit=3, used=2)
    ok = b.consume(2)
    assert ok is False
    assert b.used == 2


def test_budget_consume_negative_amount() -> None:
    b = Budget(limit=3)
    with pytest.raises(ValueError):
        b.consume(-1)


def test_budget_repr_and_eq() -> None:
    b1 = Budget(limit=3, used=1, label="x")
    b2 = Budget(limit=3, used=1, label="x")
    assert b1 == b2
    assert "Budget" in repr(b1)


def test_budget_helper() -> None:
    b = budget(4, used=1, label="unit")
    assert isinstance(b, Budget)
    assert b.limit == 4
    assert b.used == 1
    assert b.label == "unit"
