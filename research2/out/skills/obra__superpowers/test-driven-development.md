# obra/superpowers / test-driven-development
SOURCE: commit `22f0b463e7a5e579904dd6211a520321035526f7` | MIT, root `LICENSE` | 528 lines
FRONTMATTER: `name: test-driven-development`; `description: Use when implementing any feature or bugfix, before writing implementation code`
FILES READ:
| Path | Lines | Role |
|---|---:|---|
| `skills/test-driven-development/SKILL.md` | 330 | Workflow |
| `skills/test-driven-development/writing-good-tests.md` | 198 | Test quality |
FILES UNREAD: None referenced.
JOB: Test-first implementation for features, fixes, refactors and behavior changes; exceptions require partner approval. [V] (`skills/test-driven-development/SKILL.md:L16-L29`)
PROCEDURE:
1. `RED` / `Verify RED`: write a real-behavior test and confirm expected failure. [V] (`skills/test-driven-development/SKILL.md:L71-L128`)
2. `GREEN` / `Verify GREEN`: minimal implementation, then focused and full-suite tests. [V] (`skills/test-driven-development/SKILL.md:L130-L193`)
3. `REFACTOR` while green; repeat. Use linked test-quality rules. [V] (`skills/test-driven-development/SKILL.md:L195-L220`)
DECISION RULES: No production code before a failing test; reject wrong-reason failures and full-suite regressions. [V] (`skills/test-driven-development/SKILL.md:L31-L45`, `L113-L128`, `L168-L193`)
ARTIFACT SHAPE: Behavior tests, implementation, verification checklist; no acceptance-criteria mapping. [V] (`skills/test-driven-development/SKILL.md:L293-L306`)
QUESTION PROTOCOL: Ask partner for exceptions or when test design stalls. [V] (`skills/test-driven-development/SKILL.md:L22-L27`, `L308-L315`)
VALIDATION: Human runs repository-native tests; examples include `npm test`, `pytest`, `cargo test`. No validator script. [V] (`skills/test-driven-development/SKILL.md:L113-L124`, `L168-L193`)
AGENT FEATURES REQUIRED: Shell/test runner; no agents or hooks.
STATE ON DISK: Tests and implementation only; no resume state.
VOCABULARY: `RED`, `GREEN`, `REFACTOR`; no severity or requirement-linked test IDs. [V] (`skills/test-driven-development/SKILL.md:L47-L68`)
NON-OBVIOUS TECHNIQUES:
- Require failure from the missing behavior, not a typo. [V] (`skills/test-driven-development/SKILL.md:L113-L128`)
- Derive expectations independently of production helpers. [V] (`skills/test-driven-development/writing-good-tests.md:L11-L48`)
- Mock slow/external effects, not the component under test. [V] (`skills/test-driven-development/writing-good-tests.md:L65-L115`)
FAILURE MODE FOUGHT: Tautological tests and mock-only assertions. [I] (`skills/test-driven-development/writing-good-tests.md:L11-L48`, `L65-L115`)
BAGGAGE: Requires the whole project test suite for each change. [V] (`skills/test-driven-development/SKILL.md:L185-L193`)
RISKS: “Write code before the test? Delete it” risks erasing existing user work. [V] (`skills/test-driven-development/SKILL.md:L35-L45`)
FIT: testing — **ADAPT** red/green gates and real-behavior test rules; reject delete-first and unconditional suite mandates. No acceptance trace checker. [V] (`skills/test-driven-development/SKILL.md:L31-L45`, `L113-L193`, `L293-L306`)
CONFLICTS: Delete-first conflicts with surgical edits; unrelated suite failures have no scoped fallback. [V] (`skills/test-driven-development/SKILL.md:L35-L45`, `L185-L193`)
KEY QUOTES:
- “If you didn't watch the test fail, you don't know if it tests the right thing.” — `skills/test-driven-development/SKILL.md:L10-L12`
CONFIDENCE: High.
