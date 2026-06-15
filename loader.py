"""Load operator context for a given domain. CWD-independent."""
from __future__ import annotations

from pathlib import Path

import yaml

ROUTER_PATH = Path(__file__).parent / "sara" / "operators" / "01-task-router.yaml"


def load_context(domain: str) -> str:
    """Return concatenated operator text: postures + foundational + situational[domain].

    Falls back to 'general' if domain is not in the router.
    """
    base_dir = ROUTER_PATH.parent

    with ROUTER_PATH.open() as f:
        router = yaml.safe_load(f)

    paths: list[str] = []
    paths.extend(router.get("postures", []))
    paths.extend(router.get("foundational", []))

    situational = router.get("situational", {})
    paths.extend(situational.get(domain) or situational.get("general", []))

    parts: list[str] = []
    for rel in paths:
        p = base_dir / rel
        if p.exists():
            parts.append(p.read_text().strip())

    return "\n\n---\n\n".join(parts)
