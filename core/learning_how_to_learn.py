"""Learning How to Learn: lessons capture + spaced repetition.

Daily-loop responsibilities:
  - On task complete: capture a Lesson, schedule its first review.
  - Throughout the day: surface 1-2 due Lessons.
"""
from __future__ import annotations

import sqlite3
from datetime import datetime

from core.module import MMModule


class LearningHowToLearn(MMModule):
    name = "learning_how_to_learn"
    description = "Lessons capture + spaced repetition"

    SPACING_DAYS = [1, 3, 7, 21, 60]  # the review ladder

    def __init__(self, db: sqlite3.Connection):
        self.db = db

    def capture_lesson(self, task_id: str, text: str) -> str:
        """Record a Lesson and schedule its first review. Returns lesson id."""
        raise NotImplementedError  # cognitive-core slice

    def due_lessons(self, now: datetime | None = None) -> list:
        """Lessons whose review is due."""
        raise NotImplementedError  # cognitive-core slice
