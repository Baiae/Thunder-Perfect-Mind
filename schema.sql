-- SARA v0.1 data model. Four tables, per ARCHITECTURE.md. Nothing more.

CREATE TABLE IF NOT EXISTS goals (
    id          TEXT PRIMARY KEY,
    parent_id   TEXT REFERENCES goals(id),
    level       TEXT NOT NULL CHECK (level IN ('bhag','annual','quarterly','weekly','today')),
    text        TEXT NOT NULL,
    status      TEXT NOT NULL DEFAULT 'active',
    created_at  TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS tasks (
    id            TEXT PRIMARY KEY,
    goal_id       TEXT REFERENCES goals(id),
    text          TEXT NOT NULL,
    ice_score     REAL,                       -- impact * confidence * ease
    status        TEXT NOT NULL DEFAULT 'open',
    created_at    TEXT NOT NULL DEFAULT (datetime('now')),
    completed_at  TEXT
);

CREATE TABLE IF NOT EXISTS lessons (
    id           TEXT PRIMARY KEY,
    task_id      TEXT REFERENCES tasks(id),
    text         TEXT NOT NULL,
    captured_at  TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS reviews (
    id            TEXT PRIMARY KEY,
    lesson_id     TEXT NOT NULL REFERENCES lessons(id),
    due_at        TEXT NOT NULL,
    last_seen_at  TEXT,
    ease          REAL                        -- spaced-repetition ladder: 1,3,7,21,60 days
);
