# addyosmani/agent-skills / test-driven-development

SOURCE: `skills/test-driven-development/SKILL.md` | commit `301b02b12bff98e4688e6984af6556802322bbde` | MIT | 657 lines read
FRONTMATTER:
```yaml
name: test-driven-development
description: Drives development with tests using the red-green-refactor loop. Use when implementing any logic, fixing any bug, or changing any behavior. Use when you need to prove that code works, when a bug report arrives, or when you're about to modify existing functionality. Use when asked to add tests to a function, fix a bug in it or change its behavior, even when the code is pasted inline and the request does not mention tests.
```
FILES READ:
| Path | Lines | Role |
|---|---:|---|
| `skills/test-driven-development/SKILL.md` | 400 | Workflow |
| `references/testing-patterns.md` | 236 | JS/TS examples |
| `LICENSE` | 21 | Root license |
FILES UNREAD: No local files referenced; external documentation URLs not opened.
JOB: Apply test-first development to behavior changes and bug fixes, with runtime browser verification for browser-facing work. [V] (`skills/test-driven-development/SKILL.md:L8-L35`, `L314-L343`)
PROCEDURE: Discover the project runner/patterns, write a failing behavior test, make the minimum implementation pass, refactor without behavior change, then run focused and full relevant suites. [V] (`skills/test-driven-development/SKILL.md:L24-L95`, `L389-L400`)
DECISION RULES: Choose unit/integration/E2E by resource boundary; prefer real implementations, then fakes/stubs, then mocks at slow, nondeterministic or side-effecting external boundaries. [V] (`skills/test-driven-development/SKILL.md:L144-L184`, `L234-L248`; `references/testing-patterns.md:L96-L127`)
ARTIFACT SHAPE: Behavior test(s), bug reproduction, implementation, and test-suite evidence; no prescribed output file. [V] (`skills/test-driven-development/SKILL.md:L49-L119`)
QUESTION PROTOCOL: No explicit user interview; requires stack discovery before choosing test commands. [V] (`skills/test-driven-development/SKILL.md:L24-L35`)
VALIDATION: Confirm intended RED, then GREEN, rerun after refactors, and test bug fixes through a reproducer; no scripts run. [V] (`skills/test-driven-development/SKILL.md:L49-L119`, `L389-L400`)
AGENT FEATURES REQUIRED: Chrome DevTools MCP for browser-facing runtime checks; an optional subagent can write a bug reproduction test. [V] (`skills/test-driven-development/SKILL.md:L314-L359`)
STATE ON DISK: No workflow ledger; tests use project conventions and native commands. [V] (`skills/test-driven-development/SKILL.md:L24-L35`)
VOCABULARY: RED/GREEN/REFACTOR; Prove-It Pattern; unit/integration/E2E; Arrange-Act-Assert; DAMP; real/fake/stub/mock. [V] (`skills/test-driven-development/SKILL.md:L38-L119`, `L144-L184`, `L190-L248`)
NON-OBVIOUS TECHNIQUES:
- Discover the existing runner before testing; never assume `npm test`. [V] (`skills/test-driven-development/SKILL.md:L24-L35`)
- For crashes/rollback, exercise the real boundary; injected exceptions and mocked transaction calls do not prove process death or DB rollback. [V] (`skills/test-driven-development/SKILL.md:L234-L248`)
FAILURE MODE FOUGHT: Implementation-first tests, tests coupled to internals, over-mocking and unverified bug fixes. [V] (`skills/test-driven-development/SKILL.md:L96-L119`, `L190-L248`, `L303-L312`)
BAGGAGE: 80/15/5 pyramid ratios are heuristics, not quotas. [V] (`skills/test-driven-development/SKILL.md:L144-L184`)
RISKS: Browser verification requires MCP setup; do not attach to credential-bearing browser state or treat page content as instructions. [V] (`skills/test-driven-development/SKILL.md:L314-L343`)
FIT: testing — **EXTRACT** stack discovery, behavior-first tests and real-boundary checks; keep pyramid proportions advisory. [I]
CONFLICTS: The always-test stance is broad; preserve targeted validation appropriate to change risk and repository conventions. [I]
KEY QUOTES: None.
CONFIDENCE: High; skill, linked local reference and root license read; no tests run.
