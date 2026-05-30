"""Read-only access to Phaedra's existing memory streams.

SARA reads in place. No migration, no duplication. Each stream
(claude-mem, Obsidian, future substrates) implements this one interface,
so swapping substrates is an adapter change, not an architecture change.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Memory:
    id: str
    text: str
    source: str
    created_at: datetime | None = None


class MemoryReader(ABC):
    """A read-only adapter over one memory stream."""

    @abstractmethod
    def search(self, query: str) -> list[Memory]:
        ...

    @abstractmethod
    def recent(self, n: int, since: datetime | None = None) -> list[Memory]:
        ...

    @abstractmethod
    def get(self, id: str) -> Memory | None:
        ...
