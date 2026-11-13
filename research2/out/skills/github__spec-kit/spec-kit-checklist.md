# github/spec-kit / checklist
SOURCE: commit `2ee2b1e8005905db05f5717300a469b3068b908f` | MIT, root `LICENSE` | 1,167 lines across command, template and platform helpers
FRONTMATTER: Command metadata describes checking whether requirements are complete and testable.
FILES READ:
| Path | Lines | Role |
|---|---:|---|
| `templates/commands/checklist.md`; `templates/checklist-template.md` | 379; 45 | Command and output structure |
| `scripts/bash/check-prerequisites.sh`; `scripts/powershell/check-prerequisites.ps1`; `scripts/python/check_prerequisites.py` | 249; 194; 300 | Resolve feature context and prerequisites |
FILES UNREAD: `scripts/{bash/common.sh,powershell/common.ps1,python/common.py}` (942/813/721 lines; only partial portions opened; shared path/template helpers).
JOB: Generate domain-specific checklists that test requirements quality, not implementation behavior. [V] (`templates/commands/checklist.md:L9-L28`, `L139-L165`)
PROCEDURE:
1. Resolve feature docs and template through the platform prerequisite helper. [V] (`templates/commands/checklist.md:L82-L95`)
2. Ask bounded clarifying questions; draft checklist items against coverage, completeness, clarity, consistency and measurable acceptance criteria. [V] (`templates/commands/checklist.md:L109-L165`)
3. Keep items about requirements, label them by requirement references, then run post-execution checks and configured hooks. [V] (`templates/commands/checklist.md:L215-L255`, `L348-L379`)
DECISION RULES: Up to five questions; ask at most two follow-ups when two or more scenario classes remain unclear. Checklist must not contain implementation test cases or QA procedures. [V] (`templates/commands/checklist.md:L120-L120`, `L242-L255`)
ARTIFACT SHAPE: Checklist questions grouped by requirement quality, scenario coverage, traceability, and domain; examples include UX, API, performance and security. [V] (`templates/checklist-template.md:L1-L45`, `templates/commands/checklist.md:L274-L316`)
QUESTION PROTOCOL: User input plus Q1–Q5 clarification flow. [V] (`templates/commands/checklist.md:L39-L45`, `L109-L120`)
VALIDATION: Helpers emit feature paths, available documents and template content; platform variants use shell/PowerShell/Python. Not executed; network use not indicated in opened helper files.
AGENT FEATURES REQUIRED: Shell or platform runtime; ask-user capability; extension hooks may be mandatory.
STATE ON DISK: Feature checklist under `.specify` feature docs; no resumable execution state specified.
VOCABULARY: Questions can cite `FR-###` or acceptance criteria; checklist tests requirement quality, not code. [V] (`templates/commands/checklist.md:L215-L228`, `L242-L255`)
NON-OBVIOUS TECHNIQUES:
- Explicitly prohibit implementation-level test cases. [V] (`templates/commands/checklist.md:L242-L255`)
- Classify primary, alternate, exception/error, recovery and non-functional scenarios. [V] (`templates/commands/checklist.md:L218-L224`)
- Require measurable criteria rather than subjective success language. [V] (`templates/commands/checklist.md:L156-L165`)
FAILURE MODE FOUGHT: Ambiguous, incomplete or untraceable requirements. [I]
BAGGAGE: Product-specific command schema and mandatory extension-hook semantics.
RISKS: Hook instructions may invoke configured commands. [V] (`templates/commands/checklist.md:L352-L379`)
FIT: testing — **REFERENCE** as a requirements-quality checklist, not as an acceptance-criterion-to-test checker. [I]
CONFLICTS: It explicitly excludes implementation tests, so it cannot close test traceability by itself. [V] (`templates/commands/checklist.md:L242-L255`)
KEY QUOTES: None.
CONFIDENCE: Medium; command/template and platform entry scripts were opened, but shared helpers were only partly read and nothing was run.
