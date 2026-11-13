# Wshobson/agents / architecture-patterns
SOURCE: `plugins/backend-development/skills/architecture-patterns/SKILL.md` | commit `9c61ab243def98f72da12abd41cfcf5bcd91af9d` | MIT (`LICENSE`; no per-skill notice) | 919 lines read, including root license; counts from `wc -l`
FRONTMATTER:
```yaml
---
name: architecture-patterns
description: Implement proven backend architecture patterns including Clean Architecture, Hexagonal Architecture, and Domain-Driven Design. Use this skill when designing clean architecture for a new microservice, when refactoring a monolith to use bounded contexts, when implementing hexagonal or onion architecture patterns, or when debugging dependency cycles between application layers.
---
```
[V] `plugins/backend-development/skills/architecture-patterns/SKILL.md:L1-L4`
FILES READ:
| Path | Lines | Role |
|---|---:|---|
| `LICENSE` | 20 | root license |
| `plugins/backend-development/skills/architecture-patterns/SKILL.md` | 164 | entry |
| `plugins/backend-development/skills/architecture-patterns/references/details.md` | 335 | implementations |
| `plugins/backend-development/skills/architecture-patterns/references/advanced-patterns.md` | 400 | advanced patterns |
FILES UNREAD: None; all skill files and referenced resources were opened.
JOB: Given a service or module, produce layers, dependency rules, interfaces, and test boundaries [V] `plugins/backend-development/skills/architecture-patterns/SKILL.md:L10-L11`; use for Clean/Hexagonal, DDD, testability, or cycle debugging [V] `plugins/backend-development/skills/architecture-patterns/SKILL.md:L13-L20`.
PROCEDURE:
1. Select inward layers, ports/adapters, and DDD boundaries [V] `plugins/backend-development/skills/architecture-patterns/SKILL.md:L24-L68`.
2. Test use cases with in-memory adapters; troubleshoot cycles, controllers, validation, and context bleed [V] `plugins/backend-development/skills/architecture-patterns/SKILL.md:L74-L159`.
DECISION RULES: `domain/` and `use_cases/` import only `domain/`; validate value objects in `__post_init__`; split aggregates that load thousands of objects [V] `plugins/backend-development/skills/architecture-patterns/references/details.md:L3-L36` `plugins/backend-development/skills/architecture-patterns/SKILL.md:L145-L153` `plugins/backend-development/skills/architecture-patterns/references/advanced-patterns.md:L263-L294`.
ARTIFACT SHAPE: Layered structure, ports, adapters, test seams; `CreateUserResponse` fields are `user`, `success`, `error` [V] `plugins/backend-development/skills/architecture-patterns/SKILL.md:L10-L11` `plugins/backend-development/skills/architecture-patterns/references/details.md:L82-L121`.
QUESTION PROTOCOL: “Aggregate Design Heuristics” asks about consistency, eventual consistency, ownership, child meaning, and loading thousands of objects [V] `plugins/backend-development/skills/architecture-patterns/references/advanced-patterns.md:L263-L294`.
VALIDATION: In-memory tests need no DB/Docker/network. Optional `pydeps app --max-bacon=4 --cluster --rankdir=BT` outputs a dependency graph; installing `pydeps` may access a package index [V/I] `plugins/backend-development/skills/architecture-patterns/SKILL.md:L74-L125` `plugins/backend-development/skills/architecture-patterns/references/advanced-patterns.md:L394-L398`. Not run.
AGENT FEATURES REQUIRED: shell for optional `pydeps`; no agent-specific tool stated [V/I] `plugins/backend-development/skills/architecture-patterns/references/advanced-patterns.md:L394-L398`.
STATE ON DISK: No workflow-state format [I]; example writes domain events to an outbox in the aggregate-state transaction [V] `plugins/backend-development/skills/architecture-patterns/references/advanced-patterns.md:L296-L368`.
VOCABULARY: Clean Architecture, ports/adapters, bounded context, aggregate root, ACL, domain event [V] `plugins/backend-development/skills/architecture-patterns/SKILL.md:L24-L68` `plugins/backend-development/skills/architecture-patterns/references/advanced-patterns.md:L201-L229`.
NON-OBVIOUS TECHNIQUES:
- ACL maps a foreign catalog schema into local `ProductSnapshot` [V] `plugins/backend-development/skills/architecture-patterns/references/advanced-patterns.md:L122-L198`.
- Outbox writes share a transaction with state for at-least-once delivery [V] `plugins/backend-development/skills/architecture-patterns/references/advanced-patterns.md:L296-L368`.
- Value objects validate at construction; repositories persist aggregates [V] `plugins/backend-development/skills/architecture-patterns/references/details.md:L262-L335`.
FAILURE MODE FOUGHT: Domain/infrastructure imports, controller business logic, late validation, and context bleed [V] `plugins/backend-development/skills/architecture-patterns/SKILL.md:L127-L153`.
BAGGAGE: Optional graph view requires external `pydeps` installation and human interpretation [V] `plugins/backend-development/skills/architecture-patterns/references/advanced-patterns.md:L394-L398`.
RISKS: Do not make `pip install pydeps` mandatory in a portable suite [I].
FIT: backend — EXTRACT inward dependency and port rules plus in-memory test boundaries; keep graph visualization optional [V/I].
CONFLICTS: `pydeps` checking remains judgment-based [I].
KEY QUOTES: “Dependencies point inward only” `plugins/backend-development/skills/architecture-patterns/SKILL.md:L35-L35`
CONFIDENCE: High; the full skill and both referenced resources were read, together with the root license.
