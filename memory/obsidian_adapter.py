"""Adapter over the Obsidian vault (markdown at the iCloud path, CCP ladder).

Stub: structure only. Parsing the vault is a later slice.
"""
from __future__ import annotations

from datetime import datetime

from memory.reader import Memory, MemoryReader


class ObsidianReader(MemoryReader):
    SOURCE = "obsidian"

    def __init__(self, vault_path: str):
        self.vault_path = vault_path

    def search(self, query: str) -> list[Memory]:
        raise NotImplementedError("vault parsing not wired yet")

    def recent(self, n: int, since: datetime | None = None) -> list[Memory]:
        raise NotImplementedError("vault parsing not wired yet")

    def get(self, id: str) -> Memory | None:
        raise NotImplementedError("vault parsing not wired yet")
