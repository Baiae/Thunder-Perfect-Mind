# SARA — Architecture (implementation doc)

SARA (the digital twin formerly called **TARA** in the design docs) is
Phaedra's persistent twin: she reads existing memory streams, reasons through
12 universal mental models, and grows alongside Phaedra over decades.

This file tracks **what is actually in the repo**. The fuller vision lives in
the design doc (`TARA_ARCHITECTURE.md`). When code and design disagree, this
file describes reality.

## Scope decision (v0.1)

Three visions exist across the docs and they conflict:

1. **Standalone v0.1 twin** (design doc) — self-contained: memory reader +
   2 mental models + Telegram + 4-table SQLite.
2. **Governance layer** (Mental Model Compliance Matrix) — a cognition spine.
3. **Subordinate to IndraNet** (God-Mode Handoff) — SARA as a cognition layer
   under IndraNet, *not* a standalone orchestrator.

**We are building #1 first.** #2 and #3 are deferred, not discarded — they plug
in later through the `MMModule` and `MemoryReader` interfaces without a rewrite.
The standalone-vs-IndraNet tension is a known, consciously deferred decision.

## Components

1. **Memory Reader** (read-only) — adapters over Phaedra's existing streams
   (claude-mem, Obsidian), all behind one `MemoryReader` interface. Reads in
   place; no migration.
2. **Cognitive Core** — the 12 mental models behind an `MMModule` interface.
   v0.1 implements `goal_prioritization` and `learning_how_to_learn`.
3. **Interface Layer** — Telegram bot (not in this slice).

## Data model (`schema.sql`)

Four tables, nothing more:

- `goals` (id, parent_id, level, text, status, created_at) — level ∈
  {bhag, annual, quarterly, weekly, today}
- `tasks` (id, goal_id, text, ice_score, status, created_at, completed_at) —
  ice_score = impact × confidence × ease
- `lessons` (id, task_id, text, captured_at)
- `reviews` (id, lesson_id, due_at, last_seen_at, ease) — spaced-repetition
  ladder: 1, 3, 7, 21, 60 days

## File layout



Thunder-Perfect-Mind/
├── db.py
├── schema.sql
├── memory/
│   ├── init.py
│   ├── reader.py
│   ├── claude_mem_adapter.py
│   └── obsidian_adapter.py
├── core/
│   ├── init.py
│   ├── module.py
│   ├── goal_prioritization.py
│   └── learning_how_to_learn.py
├── SARA_PERSONA.md
└── ARCHITECTURE.md


## Build status

| Piece | Status |
|---|---|
| SQLite schema + init | **built** |
| `MemoryReader` interface + `Memory` | **built** |
| claude-mem / Obsidian adapters | stubbed |
| `MMModule` interface | **built** |
| 2 mental-model modules | skeletons |
| Cognitive-core logic | not started |
| Telegram interface | not started |
| LLM wiring + persona injection | not started |

## Open decisions

1. **Persona name.** Persona prose still says "Tara, the bodhisattva."
   Does "Sara" keep / drop / reinterpret that framing? Phaedra's call.
2. **LLM routing.** Honor the IndraNet `llm_router` rule or waive for
   standalone v0.1? Decide when first model call is wired.
3. **Runtime.** Hostinger (planned). OCI partially provisioned, not active.
