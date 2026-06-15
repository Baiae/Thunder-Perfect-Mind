# SARA — Session Handoff

**Date:** 2026-06-15
**Session scope:** Architecture v2.0 + full operator/loader/runner build
**Repo state:** `main` at `f58a667` — v0.1 complete

---

## What was built this session

### ARCHITECTURE.md v2.0
Replaced the v1.x implementation doc. Key changes captured:
- Project rename SARA (outer) / TARA (inner cognitive layer)
- OCI substrate downgraded: 3 OCPUs/18 GB → 2 OCPUs/12 GB
- Model locked: Gemma 3 4B primary, 12B optional
- Memory: SQLite only, external adapters stubbed (Supabase paused)
- Telegram cancelled; interface TBD
- Dreaming subsystem: designed, compatible, deferred
- All four open decisions from v1.x resolved or explicitly deferred

### Operator layer (`sara/operators/`, 13 files)
```
01-task-router.yaml           YAML router: domain → operator file paths
02-postures.md                6 postures (P-01–06): identity layer, always in system prompt
03-foundational-mental-models.md  12 mental models (MM-01–12): Tara's cognitive faculties
04-foundational-decision-protocol.md  5 operators (DP-01–05): decision audit, provenance, dead-ends
05-foundational-ice-scoring.md    4 operators (ICE-01–04): ICE scoring method
06-situational-morning.md     4 operators: morning briefing (top 3 tasks + due lesson)
07-situational-lesson.md      4 operators: lesson capture + first review scheduling
08-situational-review.md      3 operators: spaced repetition surfacing
09-situational-weekly.md      4 operators: goal alignment audit + track record review
10-situational-indranet.md    4 operators: IndraNet project context + naming guardrails
11-situational-goals.md       4 operators: goal hierarchy, BHAG, quarterly falsifiability
12-situational-general.md     3 operators: default domain, register-matching, refer-back rule
13-situational-code.md        4 operators: architectural decision logging, OCI constraints
```

### `loader.py`
CWD-independent context assembly. Derives `base_dir` from `__file__`. Reads YAML router, concatenates postures + foundational + situational\[domain\]. Falls back to `general` for unknown domains. Only non-stdlib dependency: PyYAML.

### `runner.py`
CLI entry point. `python3 runner.py <domain> "<query>"`. Single POST to `http://localhost:11434/api/chat`, model `gemma3:4b`, no streaming, 120s timeout. Prints response, exits.

### `requirements.txt`
`PyYAML>=6.0` — only non-stdlib dependency.

---

## Current repo layout

```
thunder-perfect-mind/
├── ARCHITECTURE.md              v2.0 — canonical spec
├── HANDOFF.md                   this file
├── TARA_PERSONA.md              starter persona (source for 02-postures.md)
├── README.md                    (not updated this session)
├── requirements.txt             PyYAML>=6.0
├── loader.py                    operator context loader
├── runner.py                    CLI → Ollama
├── db.py                        SQLite connect + init_db
├── schema.sql                   four-table schema
├── sara/
│   ├── __init__.py
│   └── operators/               13 files — see above
├── memory/
│   ├── reader.py                MemoryReader interface + Memory dataclass
│   ├── claude_mem_adapter.py    stub (NotImplementedError)
│   └── obsidian_adapter.py      stub (NotImplementedError)
└── core/
    ├── module.py                MMModule base class
    ├── goal_prioritization.py   skeleton (top_tasks, weekly_review → NotImplementedError)
    └── learning_how_to_learn.py skeleton (capture_lesson, due_lessons → NotImplementedError)
```

---

## What is NOT done (v0.1 gaps)

These are out of scope per ARCHITECTURE.md. Listed here to prevent re-derivation.

| Gap | Status | Notes |
|-----|--------|-------|
| Cognitive core logic | Not started | `top_tasks`, `capture_lesson`, `due_lessons`, `weekly_review` all raise `NotImplementedError` |
| `sara.db` wiring to runner | Not started | runner.py sends query to Ollama but does not read/write the DB |
| Interface layer | TBD | Telegram cancelled; iPad dashboard desired but undesigned |
| External memory adapters | Stubbed | claude-mem, Obsidian — both raise `NotImplementedError` |
| Dreaming subsystem | Designed, not integrated | `SARA_DREAMING_PROTOCOL v1.1` adds 9 tables, compatible with schema, deferred |
| Other 10 mental models | Stubbed | MM-01–12 exist as operator content; only `goal_prioritization` and `learning_how_to_learn` have MMModule subclasses |

---

## Decisions made this session

**D-01 · Operator file count**
Settled at 13 files (1 router + 12 content). Alternatives: fewer larger files (rejected — harder to route), more granular files (rejected — unnecessary). 47 total operators: 6 postures + 41 operational.

**D-02 · Fallback domain**
Unknown domains fall back to `general` silently. Alternative: raise an error (rejected — degrades gracefully on OCI where a typo shouldn't kill a session).

**D-03 · YAML parser**
Used PyYAML rather than stdlib-only parsing. The router file is small and stable but YAML is cleaner than rolling a parser. Alternative: `.toml` with `tomllib` (stdlib in 3.11+, but OCI Python version unknown — deferred).

**D-04 · No `sara.db` path in runner**
`runner.py` does not instantiate `db.py` or the cognitive modules. The MVP is: Ollama gets the operator context, returns a response. DB integration is the next slice.

---

## Next slice (suggested)

Wire the cognitive core to `runner.py`:

1. `runner.py` takes optional `--db` arg (default `~/sara/sara.db`)
2. `init_db(db_path)` on startup (idempotent)
3. For domain `morning`: call `GoalPrioritization.top_tasks()` and inject results into the query
4. For domain `lesson`: after Ollama response, call `LearningHowToLearn.capture_lesson()`
5. For domain `review`: call `LearningHowToLearn.due_lessons()` and inject into query

Implement `top_tasks` and `due_lessons` first — they're read-only and can be smoke-tested without touching Ollama.

---

## Dev environment note

The local clone lives at a path with a straight apostrophe:
```
~/Documents/Documents - Phaedra's MacBook Pro/GitHub/Thunder-Perfect-Mind/
```
An iCloud-synced directory with a curly apostrophe (`'`, U+2019) exists at the same apparent path. They are different inodes. Git operations require:
```bash
GITDIR=$(find ~/Documents -maxdepth 5 -path "*/Thunder-Perfect-Mind/.git" -type d | head -1)
REPO="${GITDIR%/.git}"
git --git-dir="$GITDIR" --work-tree="$REPO" <command>
```
Or clone fresh on OCI where this is not an issue.

---

*Handoff generated 2026-06-15. Per decision protocol DP-02: captures what was done, options considered, and reason — not a rationalization written after the fact.*
