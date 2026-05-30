"""Base for SARA's cognitive faculties: the 12 universal mental models.

v0.1 implements two. The rest plug in over time as MMModule subclasses.

Kept deliberately thin. A shared daily-loop protocol (e.g. a common
`run` hook) will be extracted once there are more than two modules to
generalise from -- designing it now would be guessing.
"""
from __future__ import annotations

from abc import ABC


class MMModule(ABC):
    name: str = ""
    description: str = ""

    def __repr__(self) -> str:
        return f"<MMModule {self.name!r}>"
