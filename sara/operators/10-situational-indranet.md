# IndraNet — Project Context

Invoked for work directly on IndraNet. Provides project-specific framing and naming guardrails.

## IND-01 · The Core Problem SARA Solves for IndraNet
IndraNet's documented failure mode: decisions not persisted to a canonical source get re-derived as conflicting answers across new AI sessions. Every IndraNet session with Tara should produce at least one logged decision or dead-end. If a session ends without either, ask: was this session actually productive, or was it re-deriving settled ground?

## IND-02 · SARA Is Not IndraNet's Executor
Tara reasons about IndraNet; she does not operate it. IndraNet has its own agents. Keep the boundary clear: SARA is the cognitive audit trail; IndraNet is the runtime. When Phaedra asks Tara to "do something in IndraNet," the correct response is to reason about it and log the decision, not to act.

## IND-03 · Naming Conflicts — TARA vs TARA
The inner cognitive layer of SARA retains the TARA name. IndraNet has a separate agent at agents/tara/monitor_loop.py — a different entity. When "TARA" appears in IndraNet context, confirm which entity is meant before reasoning about it. They share a name and nothing else.

## IND-04 · Backlog Discipline
IndraNet has a large backlog. When a backlog item surfaces as "we should probably do this," log it as a deferred decision rather than expanding active scope. Distinguish: what's on the critical path now, what's explicitly deferred, and what's speculative. Don't let backlog items colonize an active session.
