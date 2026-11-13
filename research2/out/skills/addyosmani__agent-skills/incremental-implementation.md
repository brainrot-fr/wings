# addyosmani/agent-skills / incremental-implementation

SOURCE: `skills/incremental-implementation/SKILL.md` | commit `301b02b12bff98e4688e6984af6556802322bbde` | MIT | 337 lines read
FRONTMATTER: `name: incremental-implementation`; `description: Delivers changes incrementally in thin, verifiable slices. Use when implementing any feature or change that touches more than one file, or when picking up the next task from a plan. Use when rolling a change out behind a feature flag, when you're about to write a large amount of code at once, or when a task feels too big to land in one step.`
FILES READ:
| Path | Lines |
|---|---:|
| `skills/incremental-implementation/SKILL.md` | 249 |
| `references/definition-of-done.md` | 67 |
| `LICENSE` | 21 |
FILES UNREAD: Other skills named as optional depth; not local linked files.
JOB: Deliver multi-file work in thin vertical slices, each tested, verified and independently reviewable. [V] (`skills/incremental-implementation/SKILL.md:L1-L50`)
PROCEDURE: Implement one slice, test, verify, commit, then continue; prefer vertical, contract-first or risk-first slicing. [V] (`skills/incremental-implementation/SKILL.md:L24-L96`)
DECISION RULES: Keep scope narrow and compilable; feature-flag incomplete work; prefer simple code and reversible changes. [V] (`skills/incremental-implementation/SKILL.md:L98-L190`)
ARTIFACT SHAPE: Sequence of independently testable commits, verified against the Definition of Done. [V] (`skills/incremental-implementation/SKILL.md:L24-L96`; `references/definition-of-done.md:L20-L67`)
QUESTION PROTOCOL: Surface out-of-scope issues separately instead of fixing them; ask before adding follow-up tasks. [V] (`skills/incremental-implementation/SKILL.md:L106-L130`)
VALIDATION: Use repository-native test/build/typecheck/lint per increment; do not rerun unchanged commands. [V] (`skills/incremental-implementation/SKILL.md:L190-L249`)
AGENT FEATURES REQUIRED: Optional agent instructions specify exact in/out-of-scope slice boundaries. [V] (`skills/incremental-implementation/SKILL.md:L168-L190`)
STATE ON DISK: Git commits retain slice state; plan/task list is the external work queue. [V] (`skills/incremental-implementation/SKILL.md:L24-L50`)
VOCABULARY: Vertical slice; contract-first; risk-first; feature flag; rollback-friendly; Definition of Done. [V] (`skills/incremental-implementation/SKILL.md:L24-L190`)
NON-OBVIOUS TECHNIQUES: Prove the riskiest dependency first; when parallelizing, define the shared API contract before independent work. [V] (`skills/incremental-implementation/SKILL.md:L74-L96`)
FAILURE MODE FOUGHT: Large unverified batches, scope creep, broken intermediate states and unreviewable commits. [V] (`skills/incremental-implementation/SKILL.md:L98-L249`)
BAGGAGE: The ~100-line implementation threshold is advisory; use the repo’s own command set.
RISKS: Encourages commits after each slice; do not commit or publish without authorization. [V] (`skills/incremental-implementation/SKILL.md:L24-L50`)
FIT: SDLC — **EXTRACT** slice/check/commit loop and risk-first sequencing; align commit policy to user/project rules. [I]
CONFLICTS: “Commit every slice” is stronger than some repositories’ contribution workflows; treat as configurable policy. [I]
KEY QUOTES: None.
CONFIDENCE: High; read the full skill and linked DoD, and verified the root license.
