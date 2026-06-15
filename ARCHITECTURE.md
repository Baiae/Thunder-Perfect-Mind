# SARA — Architecture (v2.0)

> Supersedes TARA_ARCHITECTURE.md v1.x. Project renamed SARA to avoid collision
> with `agents/tara/monitor_loop.py` inside IndraNet. The inner cognitive/persona
> layer retains the TARA name internally.

---

## Vision

SARA is Phaedra's persistent digital twin — a reflective AI whose primary mission
in v0.1 is to serve as the canonical memory and cognitive audit trail for building
IndraNet. She solves IndraNet's documented failure mode: decisions not persisted to
a canonical source get re-derived as conflicting answers across new AI sessions.

She is a decision-rehearsal tool, not a task executor. Her self-building in v0.1
means accumulated memory (logged decisions with provenance, preserved dead-ends,
spaced lesson review) — weight-level retraining is explicitly off the critical path.

The 12 mental models (Michael Simmons' framework) are her cognitive faculties.
v0.1 implements two; the rest plug in over time behind a shared interface.

---

## Substrate

|                    |                                                          |
|--------------------|----------------------------------------------------------|
|**Runtime**         |OCI A1.Flex (Ubuntu 22.04, 2 OCPUs, 12 GB RAM)            |
|**Primary model**   |Gemma 3 4B via Ollama (stable within RAM budget)          |
|**Heavy-lift model**|Gemma 3 12B via Ollama (optional, invoked deliberately)   |
|**Future**          |TBD — substrate migration is mechanical, not architectural|

All heavy work runs on OCI. Development happens on iPad Pro (Working Copy) and
MacBook Pro M1 Max. Neither is part of SARA's runtime.

---

## Three Components

### 1. Memory (SQLite only, v0.1)

v0.1 uses a single local SQLite file (`sara.db`). External memory adapters
(claude-mem, Obsidian, Supabase pgvector) are stubbed behind the `MemoryReader`
interface but not wired. No external reads or writes in v0.1.

**Interface (implemented, adapters stubbed):**

```
search(query) -> list[Memory]
recent(n, since) -> list[Memory]
get(id) -> Memory
```

**Why deferred:** Supabase Open Brain (project `llxehkakxxrkqhtuxyuc`) is currently
paused. The Sovereign Brain ICM pipeline that would feed it is an IndraNet backlog
item, not a SARA v0.1 concern. Memory substrate is re-evaluated when both are stable.

### 2. Cognitive Core

12 mental models scaffolded behind an `MMModule` interface. v0.1 implements:

- `goal_prioritization` — ICE-ranked task surfacing aligned to active goals
- `learning_how_to_learn` — Lesson capture + spaced repetition

**Operator layer (implemented):**
41 operators + 6 postures across three runtime tiers, built into 13 files:

- Postures — always in system prompt (identity layer)
- Foundational operators — always loaded (~2.5k tokens)
- Situational operators — task-routed by domain via YAML router

**Context pipeline (implemented):**

- `loader.py` — derives `base_dir` from router file location (CWD-independent),
  returns concatenated operator content
- `runner.py` — accepts domain + query, sends single non-streaming request to
  local Ollama, prints response, exits. No loop, history, streaming, or retry.

**Daily loop:**

|When          |What                                          |
|--------------|----------------------------------------------|
|Morning       |Top 3 ICE-ranked tasks aligned to active goals|
|Task complete |Capture Lesson, schedule for spaced repetition|
|Throughout day|Surface 1–2 due Lessons                       |
|Weekly        |Goal-alignment review + track record review   |

**Dreaming subsystem (designed, not yet integrated):**
`SARA_DREAMING_PROTOCOL v1.1` — async self-reflection pipeline. Generates
artifacts (proposals for memory/skill/behavior changes), never approves them
autonomously. Requires human review at every gate. Adds 9 orthogonal tables to
`sara.db`. Compatible with existing schema. Integration deferred pending stable
dev environment.

### 3. Interface Layer

**v0.1:** TBD. Telegram bot cancelled. iPad dashboard desired but undesigned.
No interface blocking the cognitive core build — CLI via `runner.py` is sufficient
for initial smoke tests.

**Later:** iPad-native dashboard, voice, MCP integration. All interface options
talk to the same SARA service. One mind, many windows.

---

## Data Model

SQLite at `~/sara/sara.db` on OCI:

```
goals     (id, parent_id, level, text, status, created_at)
            level ∈ {bhag, annual, quarterly, weekly, today}

tasks     (id, goal_id, text, ice_score, status, created_at, completed_at)
            ice_score = impact * confidence * ease

lessons   (id, task_id, text, captured_at)

reviews   (id, lesson_id, due_at, last_seen_at, ease)
            spaced repetition: 1d, 3d, 7d, 21d, 60d
```

Four tables. Dreaming subsystem adds 9 more when integrated (same db, Option A).

---

## What v0.1 Does NOT Do

Deliberately out of scope:

- External memory reads (claude-mem, Obsidian, Supabase) — adapters stubbed only
- The other 10 mental models
- Dreaming subsystem integration
- Interface layer beyond CLI
- Voice / vision
- Web research loop
- Email / calendar / social ingestion
- Multi-user

All plug in later without re-architecture.

---

## File Layout (actual, in repo)

```
thunder-perfect-mind/
├── ARCHITECTURE.md              # this file
├── sara/
│   └── operators/               # 13 operator files
│       └── 01-task-router.yaml  # domain → operator path mapping
├── memory/
│   ├── __init__.py
│   ├── reader.py                # MemoryReader interface + Memory dataclass
│   ├── claude_mem_adapter.py    # stub
│   └── obsidian_adapter.py      # stub
├── core/
│   ├── __init__.py
│   ├── module.py                # MMModule base class
│   ├── goal_prioritization.py
│   └── learning_how_to_learn.py
├── loader.py                    # operator context loader
├── runner.py                    # CLI entry point → Ollama
└── sara.db                      # SQLite (created on first run)
```

---

## Repo

`https://github.com/Baiae/Thunder-Perfect-Mind`

---

## What Changed from v1.x and Why

|Area              |v1.x (original)                       |v2.0 (current)                                                         |
|------------------|--------------------------------------|-----------------------------------------------------------------------|
|**Name**          |TARA                                  |SARA (collision with IndraNet monitor-loop agent)                      |
|**Compute**       |OCI 3 OCPUs / 18 GB                   |OCI 2 OCPUs / 12 GB (downgraded)                                       |
|**Model**         |Not specified                         |Gemma 3 4B primary, 12B optional                                       |
|**Memory**        |claude-mem + Obsidian adapters (wired)|SQLite only; adapters stubbed (Supabase paused, ICM pipeline not built)|
|**Interface**     |Telegram bot (Life Engine extension)  |TBD; Telegram cancelled                                                |
|**Hosting**       |OCI → Hostinger future                |OCI only (Hostinger dropped, income constraint)                        |
|**Operator layer**|Not in original spec                  |41 operators + 6 postures, YAML router, loader.py, runner.py           |
|**Dreaming**      |Not in original spec                  |Designed (v1.1), compatible, integration deferred                      |
|**Mac Mini**      |Excluded from runtime                 |Destroyed; MacBook Pro M1 Max is dev machine                           |
|**Open decisions**|4 listed                              |All resolved or explicitly deferred                                    |

---

*v2.0 — updated to reflect actual build state. Per CLAUDE.MD rule #5.*
