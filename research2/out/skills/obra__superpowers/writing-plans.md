# obra/superpowers / writing-plans

SOURCE: `skills/writing-plans/SKILL.md` | commit `22f0b463e7a5e579904dd6211a520321035526f7` | MIT | 225 lines read
FRONTMATTER: `name: writing-plans`; `description: Use when you have a spec or requirements for a multi-step task, before touching code`
FILES READ:
| Path | Lines |
|---|---:|
| `skills/writing-plans/SKILL.md` | 204 |
| `LICENSE` | 21 |
FILES UNREAD: `references/definition-of-done.md` is directly referenced but absent from this clone; other named subskills are out-of-scope dependencies.
JOB: Create exact, bite-sized implementation plans for engineers unfamiliar with the codebase. [V] (`skills/writing-plans/SKILL.md:L1-L35`)
PROCEDURE: Map files/interfaces, break into independently tested tasks, include a global header/constraints/review focus, then self-review coverage and proportion. [V] (`skills/writing-plans/SKILL.md:L20-L170`)
DECISION RULES: Preserve existing incomplete plans; stop for a different-work conflict. Steps should specify one action and checkable result. [V] (`skills/writing-plans/SKILL.md:L52-L117`, `L172-L204`)
ARTIFACT SHAPE: `docs/superpowers/plans/YYYY-MM-DD-<feature>.md` by default, with Goal, Architecture, Tech Stack, Spec, Global Constraints, Review Focus and task steps. [V] (`skills/writing-plans/SKILL.md:L12-L20`, `L40-L117`)
QUESTION PROTOCOL: Ask the user when a conflicting unfinished plan exists or at execution-method handoff; user location preference overrides default. [V] (`skills/writing-plans/SKILL.md:L12-L20`, `L132-L166`, `L190-L204`)
VALIDATION: Self-review requirement coverage, task-step precision, type consistency, Review Focus and plan/spec proportion. [V] (`skills/writing-plans/SKILL.md:L172-L204`)
AGENT FEATURES REQUIRED: Recommends subagent-driven or inline execution subskills; plan does not require either while authoring. [V] (`skills/writing-plans/SKILL.md:L40-L48`, `L59-L60`, `L190-L204`)
STATE ON DISK: Plan and task list; external tracker is allowed with an ordered ID index. [V] (`skills/writing-plans/SKILL.md:L118-L166`)
VOCABULARY: Interfaces, Global Constraints, Review Focus, task list target, checkpoint, dependency graph. [V] (`skills/writing-plans/SKILL.md:L40-L117`)
NON-OBVIOUS TECHNIQUES: Write the five highest-risk uncovered input classes once, then add a test for each to its owning task. [V] (`skills/writing-plans/SKILL.md:L40-L51`, `L172-L188`)
FAILURE MODE FOUGHT: Vague tasks, unexecutable steps, mismatched interfaces and overwritten plan state. [V] (`skills/writing-plans/SKILL.md:L52-L117`, `L172-L188`)
BAGGAGE: Strict header and review focus can be heavy for small plans; defaults yield to project/user conventions.
RISKS: The missing DoD reference makes the handoff dependency incomplete; preserve user-owned open tasks. [V] (`skills/writing-plans/SKILL.md:L132-L166`, `L190-L204`)
FIT: SDLC — **ADAPT** exact task interfaces, tests and review focus; make handoff gates explicit. [I]
CONFLICTS: The skill's execution-method handoff can require confirmation; not a blocker for read-only planning. [V] (`skills/writing-plans/SKILL.md:L190-L204`)
KEY QUOTES: None.
CONFIDENCE: High; complete plan skill and root license read; referenced DoD path absent.
