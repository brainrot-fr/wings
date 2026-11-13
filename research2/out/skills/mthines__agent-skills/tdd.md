# mthines/agent-skills / tdd

SOURCE: `skills/quality/tdd/SKILL.md` | commit `e58875ab27e584112304aba3c542b46a661062a7` | MIT | 691 lines read
FRONTMATTER:
```yaml
name: tdd
description: Enforces strict RED-GREEN-REFACTOR test-driven development — one failing test at a time, minimal code to pass, then refactor against an inline quality checklist and a test-provenance check (`provenance` runs it alone). Triggers on "tdd", "write tests", "test driven", "red green refactor", "/tdd".
```
FILES READ:
| Path | Lines |
|---|---:|
| `skills/quality/tdd/SKILL.md` | 166 |
| `skills/quality/tdd/rules/test-after.md` | 78 |
| `skills/quality/tdd/rules/red.md` | 90 |
| `skills/quality/tdd/rules/green.md` | 89 |
| `skills/quality/tdd/rules/refactor.md` | 149 |
| `skills/quality/tdd/rules/test-provenance.md` | 69 |
| `skills/quality/tdd/lens.md` | 29 |
| `LICENSE` | 21 |
FILES UNREAD: None within the target and its local references.
JOB: Run strict RED-GREEN-REFACTOR cycles; `/tdd after` covers existing code, and `provenance` checks changed tests. [V] (`skills/quality/tdd/SKILL.md:L36-L44`, `L72-L95`)
PROCEDURE: Discover the runner; rank behaviors; get approval; write one failing test; implement minimally; run focused/full suites; refactor one named move at a time. [V] (`skills/quality/tdd/SKILL.md:L47-L95`)
DECISION RULES: Test public behavior, one behavior per test; prefer real implementations, then fakes/stubs, mocking external boundaries only. [V] (`skills/quality/tdd/SKILL.md:L118-L151`)
ARTIFACT SHAPE: Behavior list, tests, RED/GREEN/REFACTOR report, provenance result. [V] (`skills/quality/tdd/SKILL.md:L60-L71`; `skills/quality/tdd/rules/test-provenance.md:L69`)
QUESTION PROTOCOL: Ask for behavior, framework or critical-path ranking when missing/unclear; seek approval before the cycle. [V] (`skills/quality/tdd/SKILL.md:L36-L68`)
VALIDATION: RED must fail for the intended reason; run full relevant suites; provenance statically checks imports and can mutate production code. [V] (`skills/quality/tdd/rules/red.md:L35-L69`; `skills/quality/tdd/rules/test-provenance.md:L12-L55`)
AGENT FEATURES REQUIRED: PR reviewer may auto-load the test lens; no agent integration required. [V] (`skills/quality/tdd/SKILL.md:L34-L34`; `skills/quality/tdd/lens.md:L8-L20`)
STATE ON DISK: No workflow ledger; tests follow repo conventions and changed files use a base ref. [V] (`skills/quality/tdd/SKILL.md:L47-L57`; `skills/quality/tdd/rules/test-provenance.md:L12-L14`)
VOCABULARY: RED/GREEN/REFACTOR; test-after; provenance; by-construction; behavior inventory. [V] (`skills/quality/tdd/SKILL.md:L72-L95`; `skills/quality/tdd/rules/test-provenance.md:L10-L17`)
NON-OBVIOUS TECHNIQUES:
- Test-after mutates the implementation; passing after mutation means the test proves nothing. [V] (`skills/quality/tdd/rules/test-after.md:L33-L48`)
- Provenance stubs production code, runs one test file and requires state restoration even after a crash. [V] (`skills/quality/tdd/rules/test-provenance.md:L20-L55`)
- Refactor one named move at a time and rerun tests. [V] (`skills/quality/tdd/rules/refactor.md:L43-L70`)
FAILURE MODE FOUGHT: Implementation-first tests, by-construction tests, wrong-reason RED failures, unverified refactors. [V] (`skills/quality/tdd/rules/red.md:L35-L60`; `skills/quality/tdd/rules/test-provenance.md:L10-L18`)
BAGGAGE: Strict cadence adds test runs and approval checkpoints; thresholds are heuristics.
RISKS: Mutation temporarily changes production files; isolate and verify restoration. [V] (`skills/quality/tdd/rules/test-provenance.md:L20-L55`)
FIT: testing — **ADAPT** behavior inventory and test-first gate; require a safe mutation sandbox or approval. [I]
CONFLICTS: Test-after's temporary mutation needs a source-preservation gate. [V] (`skills/quality/tdd/rules/test-after.md:L33-L48`; `skills/quality/tdd/rules/test-provenance.md:L20-L55`)
KEY QUOTES: None.
CONFIDENCE: High; complete target, six local references and root license read; no tests/scripts run.
