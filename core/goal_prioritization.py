"""Goal Setting + 80/20 Prioritization.

Daily-loop responsibilities:
  - Morning: surface the top ICE-ranked tasks aligned to active goals.
  - Weekly: goal-alignment review.
"""
from __future__ import annotations

import sqlite3

from core.module import MMModule


class GoalPrioritization(MMModule):
    name = "goal_prioritization"
    description = "Goal Setting + 80/20 Prioritization"

    def __init__(self, db: sqlite3.Connection):
        self.db = db

    def top_tasks(self, limit: int = 3) -> list:
        """Top ICE-ranked tasks aligned to active goals."""
        raise NotImplementedError  # cognitive-core slice

    def weekly_review(self) -> None:
        """Goal-alignment review."""
        raise NotImplementedError  # cognitive-core slice
