"""Adapter over the claude-mem SQLite store (~/Desktop/shAIte/claude-mem/).

Stub: structure only. Wiring the real claude-mem schema is a later slice.
"""
from __future__ import annotations

from datetime import datetime

from memory.reader import Memory, MemoryReader


class ClaudeMemReader(MemoryReader):
    SOURCE = "claude-mem"

    def __init__(self, db_path: str):
        self.db_path = db_path

    def search(self, query: str) -> list[Memory]:
        raise NotImplementedError("claude-mem schema not wired yet")

    def recent(self, n: int, since: datetime | None = None) -> list[Memory]:
        raise NotImplementedError("claude-mem schema not wired yet")

    def get(self, id: str) -> Memory | None:
        raise NotImplementedError("claude-mem schema not wired yet")
