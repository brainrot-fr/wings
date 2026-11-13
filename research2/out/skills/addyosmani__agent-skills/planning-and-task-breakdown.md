# addyosmani/agent-skills / planning-and-task-breakdown

SOURCE: `skills/planning-and-task-breakdown/SKILL.md` | commit `301b02b12bff98e4688e6984af6556802322bbde` | MIT | 345 lines read
FRONTMATTER: `name: planning-and-task-breakdown`; `description: Breaks work into ordered tasks. Use when you have a spec or clear requirements and need to break them into implementable tasks. Use when a task feels too large to start, when you need to estimate scope, or when parallel work is possible.`
FILES READ:
| Path | Lines |
|---|---:|
| `skills/planning-and-task-breakdown/SKILL.md` | 257 |
| `references/definition-of-done.md` | 67 |
| `LICENSE` | 21 |
FILES UNREAD: Other skills named as optional depth; not local linked files.
JOB: Turn requirements into ordered, independently verifiable implementation tasks with acceptance criteria, dependencies and checkpoints. [V] (`skills/planning-and-task-breakdown/SKILL.md:L1-L80`)
PROCEDURE: Read code/context; build dependency graph; slice vertically; specify files, interfaces, tests and expected output; self-review before handoff. [V] (`skills/planning-and-task-breakdown/SKILL.md:L19-L80`, `L118-L176`)
DECISION RULES: XS–L task sizing; split XL; preserve unfinished plans; stop for conflicting plans in another task list. [V] (`skills/planning-and-task-breakdown/SKILL.md:L82-L115`)
ARTIFACT SHAPE: Plan header, global constraints, review focus, task cards and staged checkpoints; `docs/decisions` conventions handled by referenced docs. [V] (`skills/planning-and-task-breakdown/SKILL.md:L118-L219`)
QUESTION PROTOCOL: If another unfinished plan conflicts with new work, stop and ask before overwriting or moving it. [V] (`skills/planning-and-task-breakdown/SKILL.md:L142-L166`)
VALIDATION: Self-review spec coverage, step granularity, type consistency, review focus and proportionality; Definition of Done adds correctness/quality/integration/ship gates. [V] (`skills/planning-and-task-breakdown/SKILL.md:L177-L219`; `references/definition-of-done.md:L1-L67`)
AGENT FEATURES REQUIRED: Parallelize independent slices only after shared contracts are defined. [V] (`skills/planning-and-task-breakdown/SKILL.md:L221-L235`)
STATE ON DISK: `tasks/plan.md` and `tasks/todo.md` by default, or an external tracker with an ordered ID index; never overwrite another incomplete plan. [V] (`skills/planning-and-task-breakdown/SKILL.md:L118-L166`)
VOCABULARY: Vertical slice, dependency graph, acceptance criteria, task list target, checkpoint, review focus. [V] (`skills/planning-and-task-breakdown/SKILL.md:L30-L115`)
NON-OBVIOUS TECHNIQUES: Use exact interfaces and tests so each task is independently executable; map the five highest-risk uncovered inputs to tests. [V] (`skills/planning-and-task-breakdown/SKILL.md:L118-L176`)
FAILURE MODE FOUGHT: Oversized vague tasks, hidden dependencies, overwritten plans and plans with no verifiable output. [V] (`skills/planning-and-task-breakdown/SKILL.md:L82-L115`, `L177-L219`)
BAGGAGE: Prescribes a detailed plan header and approval handoff; adapt to existing project task conventions.
RISKS: Writing plans can overwrite in-progress state; the source explicitly requires checking before changing it. [V] (`skills/planning-and-task-breakdown/SKILL.md:L142-L166`)
FIT: SDLC — **EXTRACT** task shape, dependency checks and checkpoints; use a structured ledger for resumability. [I]
CONFLICTS: Default filenames are not universal; external tracker/project conventions take precedence. [V] (`skills/planning-and-task-breakdown/SKILL.md:L118-L166`)
KEY QUOTES: None.
CONFIDENCE: High; complete skill, linked DoD and root license read.
