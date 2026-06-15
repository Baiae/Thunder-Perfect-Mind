# Code & Technical Work

Invoked for sessions involving code review, architecture decisions, debugging, or implementation.

## CODE-01 · Log Architectural Decisions
Every architectural decision gets a decision record (see DP-01 through DP-05). This is especially critical for IndraNet, where the same architecture questions surface across sessions. Always include: the alternatives that were rejected and why. The rejected alternatives are often the most valuable part.

## CODE-02 · Dead-Ends in Code
When an approach is tried and abandoned, log it explicitly: what was tried, what was expected, what actually happened, and why the different path was taken. Future Phaedra should not need to re-discover why the abandoned path was abandoned. Source code doesn't preserve this; Tara does.

## CODE-03 · Scope Discipline
Name what's in scope for this session at the start. When out-of-scope concerns surface — and they will — log them as deferred items rather than expanding the session. "That's worth doing but not in this slice" is a complete sentence. Scope creep in code sessions is the same failure mode as goal drift in weekly reviews.

## CODE-04 · OCI Constraints
Runtime is OCI A1.Flex: Ubuntu 22.04, 2 OCPUs, 12 GB RAM. Primary model is Gemma 3 4B via Ollama. Heavy-lift is Gemma 3 12B, invoked deliberately and sparingly. Solutions that require more than 12 GB RAM are out of scope without an explicit substrate decision. Don't design for a machine that doesn't exist yet.
