from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Budget:
    limit: int | float
    used: int | float = 0
    label: str | None = None

    def __post_init__(self) -> None:
        if self.limit < 0:
            raise ValueError("limit must be >= 0")
        if self.used < 0:
            raise ValueError("used must be >= 0")
        if self.used > self.limit:
            raise ValueError("used must be <= limit")

    @property
    def remaining(self) -> int | float:
        return self.limit - self.used

    def consume(self, amount: int | float) -> bool:
        if amount < 0:
            raise ValueError("amount must be >= 0")
        if self.used + amount > self.limit:
            return False
        self.used += amount
        return True


def budget(limit: int | float, used: int | float = 0, label: str | None = None) -> Budget:
    return Budget(limit=limit, used=used, label=label)
