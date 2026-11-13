# github/spec-kit / tasks and converge
SOURCE: commit `2ee2b1e8005905db05f5717300a469b3068b908f` | MIT, root `LICENSE` | 1,857 lines across commands, template and platform helpers
FRONTMATTER: `tasks` generates a story-organized implementation plan; `converge` appends remaining work after implementation.
FILES READ:
| Path | Lines | Role |
|---|---:|---|
| `templates/commands/tasks.md`; `templates/commands/converge.md`; `templates/tasks-template.md` | 220; 279; 252 | Generation, reconciliation and task format |
| `scripts/bash/setup-tasks.sh`; `scripts/powershell/setup-tasks.ps1`; `scripts/python/setup_tasks.py` | 94; 93; 176 | Resolve task template and feature artifacts |
| `scripts/bash/check-prerequisites.sh`; `scripts/powershell/check-prerequisites.ps1`; `scripts/python/check_prerequisites.py` | 249; 194; 300 | Resolve and validate feature context |
FILES UNREAD: `scripts/{bash/common.sh,powershell/common.ps1,python/common.py}` (942/813/721 lines; only partial portions opened; shared path/template helpers).
JOB: Generate tasks grouped by user story, then compare implemented code against spec/plan/tasks and append only unmet work. [V] (`templates/commands/tasks.md:L63-L95`, `templates/commands/converge.md:L57-L79`)
PROCEDURE:
1. Build Setup, Foundational, story and Polish phases with file-specific tasks and independent-test notes. [V] (`templates/commands/tasks.md:L80-L95`, `templates/tasks-template.md:L16-L22`, `L48-L77`)
2. Tests are task items only when requested; an included test must precede implementation in its story phase. [V] (`templates/commands/tasks.md:L145-L194`, `templates/tasks-template.md:L97-L115`)
3. `converge` inventories intent, classifies gaps, assigns severity, reports findings, then appends a numbered Convergence phase or leaves tasks byte-identical. [V] (`templates/commands/converge.md:L133-L228`)
DECISION RULES: Convergence gaps are `missing|partial|contradicts|unrequested`; severity is CRITICAL/HIGH/MEDIUM/LOW; each new task traces to a source requirement. Existing tasks are never rewritten. [V] (`templates/commands/converge.md:L145-L182`, `L202-L228`)
ARTIFACT SHAPE: `[ID] [P?] [Story] Description`; phases and checkboxes, file paths, goals and independent-test criteria. Convergence uses `F#`, source refs, and `T###` tasks. [V] (`templates/tasks-template.md:L16-L20`, `templates/commands/converge.md:L165-L218`)
QUESTION PROTOCOL: User input is considered; no fixed question sequence.
VALIDATION: Setup helpers return JSON paths/template/docs; Bash uses `eval` on quoted assignments, PowerShell uses objects and Python emits JSON. They inspect local files; none was run and no network path was identified.
AGENT FEATURES REQUIRED: Shell/platform runtime; configured extension hooks may be mandatory.
STATE ON DISK: `tasks.md` is the plan and resumable task list; no separate run-state file.
VOCABULARY: `P1–P3`, `US#`, `[P]`, `T###`, `F#`, `FR-###`, `SC-###`; tests optional by default. [V] (`templates/tasks-template.md:L16-L20`, `templates/commands/tasks.md:L145-L166`, `templates/commands/converge.md:L165-L218`)
NON-OBVIOUS TECHNIQUES:
- Tasks are independently testable per story, with explicit phase dependencies. [V] (`templates/tasks-template.md:L163-L211`)
- Convergence is append-only and leaves an already-converged file byte-for-byte unchanged. [V] (`templates/commands/converge.md:L71-L86`, `L228-L232`)
- Completion checkboxes are not evidence; convergence inspects current code. [V] (`templates/commands/converge.md:L145-L172`)
FAILURE MODE FOUGHT: Missing implementation work and tasks detached from user-story intent. [I]
BAGGAGE: Command ecosystem and `optional tests` default can omit test work.
RISKS: Bash `eval` consumes helper-generated assignments; configured hooks explicitly require invocation. [V] (`scripts/bash/setup-tasks.sh:L27-L27`, `templates/commands/tasks.md:L100-L116`, `templates/commands/converge.md:L246-L279`)
FIT: sdlc-process — **EXTRACT** phased tasks, source refs, append-only reconciliation; testing — **ADAPT** test ordering but make test traceability explicit.
CONFLICTS: Test tasks are optional and there is no acceptance-criterion-to-test checker. [V] (`templates/commands/tasks.md:L145-L148`)
KEY QUOTES: None.
CONFIDENCE: Medium; shared helpers only partially read; nothing was run.
