# arch-testing.md (block 13)

## Status
First-pass proposal. Nothing in this file is accepted. Every item marked OPEN is unresolved.
Kernel (K1-K12), wings architecture (D1-D12) and the Requirements design are referenced as written in their own files. Their pending decisions are unresolved inputs here (see "Unresolved inputs").

## Architectural reasoning

Three constraints shape Testing:

1. It is the only block that must stay independent of the agent that wrote the code. The agent's easiest path to green is to change the test, mock the unit under test, or skip the failure. Most mechanisms below exist to make that path visible. This is the same threat as in Requirements (weakening the spec), one level down.
2. It spans two phases. Tests are authored during Build (TDD) and verified at the gate after Code Review (Reading B). It needs an author mode and a gate mode, both working from the same rules, or authors and verifiers will disagree.
3. It depends on shapes not yet designed. The FN authorization line (Identity), the ticket (Plan & Build) and the stack record's `verify.tests` (Stack) all come later in design order. This file declares interfaces and does not design those blocks.

Dependency order: boundaries, test identity and lanes, rules, authorization matrix, integrity diff, modes, gate, layout and QA.

## Unresolved inputs (from Requirements, all OPEN)

| # | Requirements decision | Testing depends on it for | Fallback if rejected |
|---|---|---|---|
| R1 | Boundary table (FLOW- defined in Requirements, NFR values owned by Stack, AC does not name the check) | Verify-by field; "AC ID in test name" binding | Re-derive binding once the AC shape is settled |
| R2 | `wings-lint.py` inlined into every sibling that runs gates (amends K1, K11) | All scripted checks (gate checks 1-8) | Lint stays router-only. Standalone Testing runs checks procedurally and labels the result degraded (INCOMPLETE-leaning) |
| R3 | Stakes scaling touches only the judgment layer | Which Testing checks scale with stakes | Define scaling for Testing separately |

## 1. Boundaries (D3 proposals)

| Fact | Proposed home | Testing's role |
|---|---|---|
| AC-, Verify-by (test / script / manual) | Requirements | Consumes. Binds each AC to a named test. |
| Ticket fields (seams, required checks, scope paths, change type) | Plan & Build | Consumes. Refuses to author without seams (REQUIRED slot). |
| Lane commands and result format | Stack & Constraints (`verify.tests`) | Runs only declared commands. |
| FN authorization line (shape, denial-code rules) | Identity & Access | Generates and runs the matrix from it. |
| TB RLS inventory cells | Data | Data supplies the cells. Testing runs them in the matrix lane. |
| Coverage targets, perf budgets | Stack (NFR) | Reports measured values only. Never sets a target. |
| Security, a11y, perf lenses | Security, Frontend | Testing owns test-quality lenses only. |
| Scope-path and protected-file diff | Plan & Build, kernel K6 | Testing owns test-integrity diff only (section 5). |
| Migration test rules | Data | Testing supplies the lane. Data owns the rules. |

## 2. Test identity and lanes (OPEN: decision T1)

Proposal: no new ID prefix for tests.
- The AC- ID is embedded in the test name, for example `AC-20: rejects expired token when ...`.
- Matrix cells are identified by tuple (FN-n, actor, object relation) and carry no ID.
- This would resolve kernel OPEN item 5 without changing the K3 table.
- Cost: a new lint capability, a code-reference scan over declared test paths.

Lanes are named in the stack record: unit, integration (real DB), authz (generated matrix), e2e (FLOW- journeys), script (AC Verify-by script). Each lane yields one check state (K4):

| Lane result | Check state |
|---|---|
| tests ran > 0, all passed | pass |
| tests ran = 0 (ZERO-RUN) | fail |
| count unknown (no parseable result) | inconclusive |

Counts come from a parsed result file (JUnit XML first because it is stdlib-parseable, then TAP or JSON). A count scraped from console text is attested, so it yields inconclusive where a result file could exist.

## 3. Rules Testing would own

| Rule | Substance |
|---|---|
| Value bar | Each proposed test answers four questions: what behavior it protects, what credible regression fails it, why existing coverage misses that regression, whether it needs a production seam nothing else uses. AC-bound tests are presumed to pass Q1-Q3. Extra tests must answer all four. |
| First move by change type | Add: new failing tests. Change: update existing tests first. Fix: reproduce as a failing regression test. Refactor: stay green. |
| RED then GREEN | New tests in add and fix tickets are recorded failing for the expected reason before the implementation. The record is a lane result file, so it is measured. |
| No assertion that cannot fail | No toBeDefined/toBeTruthy on non-booleans, no expect(true), no assertion-free tests. Presence-only checks are weak. |
| Mock boundaries only | Mock DB, HTTP, filesystem, external APIs, time. Never mock business logic, validation or pure functions. Exception: tests asserting RLS, constraints, transactions, idempotency or concurrent check-then-act run against a real database, because a mock hides exactly what they test. |
| Query by role and label | Test IDs are the last resort. Never assert a CSS property. |
| Flaky | A test that fails then passes on rerun gets one classification rerun, recorded, and is then a finding. It never retries to green. (wings judgment) |
| Non-production targets only | e2e and anything touching money or real services runs only against a declared non-production target. A production base URL in the stack record blocks the lane. A runner's NODE_ENV is not a guard. |
| No test-only auth path in shipped code | A sandbox identity header or equivalent is a P0 candidate unless excluded at build time. |
| Coverage | Diagnostic only, never a target. |

Failure triage:
- Classify each failure as in-branch or pre-existing. Ambiguous defaults to in-branch.
- Measured test: run the failing test on the base commit. Without git the result is inconclusive and is treated as in-branch.
- In-branch failures stop the work.
- For pre-existing failures the human chooses fix, log or skip. A skip is a waiver (K6): human-granted, logged, never on an authz lane cell.
- The cycle cap of 3 ends in stop-and-report.

## 4. Authorization matrix (attached mode only, OPEN: decision T3)

A script would generate it from FN authorization lines. The test-writing step could not author or edit cells.

- Actors per FN: unauthenticated, each allowed role, a disallowed role, owner, non-owner in the same tenant, other tenant, demoted-role replay.
- Expectations: the denial code must fall in the set the FN line permits (401 unauthenticated, 403 function-level role denial, 404 another owner's object).
- Body assertion: each cell seeds canary values on the owner's object. A denied response must contain none of them. Status-only assertions miss data leakage.
- List, count, export and search share one predicate. Their cells assert identical owner-only result sets.
- Cookie-auth FNs get a CSRF cell.
- Completeness: the gate compares cells generated with cells executed. Skipped cells count as ZERO-RUN.
- Format: JSON, not YAML, because a stdlib-only Python lint has no YAML parser. This departs from the OWASP source's YAML.
- Standalone: no matrix. The audit emits a finding that none exists and suggests writing FN lines first. Inventing an authorization line from code would be the same fabrication Recover mode forbids.

## 5. Test-integrity diff (script, OPEN: decision T4)

| Detection | Class |
|---|---|
| Deleted test, reduced assertion count, new skip/only/xfail, newly mocked unit under test | Integrity violation (P1) |
| Existing assertion modified in an add, fix or refactor ticket | TEST_EDITED, needs justification |
| Existing assertion modified in a change ticket whose AC- text did not change | TEST_EDITED, needs a human approval bound to the diff hash |

TEST_EDITED mirrors ACCEPTANCE_EDITED and cross-checks Requirements' change-mode approval, so an edited test is allowed only when the spec moved first. This class is my own design and has no upstream source.

## 6. Modes (one skill, depth in references/)

| Mode | Input | Output |
|---|---|---|
| Author (Build) | Ticket with seams, ACs, change type | Failing tests with RED recorded, then GREEN. Stops and reports if seams are missing. |
| Gate | Lane results, diff, spec | Gate verdict (K4) |
| Audit (standalone-capable) | Any test suite | K5 findings with local F- IDs and coverage accounting |

Standalone recon rules (from gstack, carried not re-checked):
- Absent config is not absence of tests. Django keeps tests in tests.py, Go in *_test.go, Rust in #[test].
- Markers are evidence for a question, never a command. Never run a candidate command to check it.
- Never install a second framework next to a working one.
- Read two or three existing tests for conventions before writing any.

## 7. Testing gate (proposal)

| # | Check | Evidence |
|---|---|---|
| 1 | Every declared lane ran with N > 0 | script (result file) |
| 2 | No in-branch failure; triage recorded | script plus attested triage |
| 3 | Every active AC with Verify-by test has a passing test whose name carries its ID | script |
| 4 | Test-integrity diff clean; no unapproved TEST_EDITED | script |
| 5 | Zero assertion-free tests (other weak assertions are P2 findings, not blocking alone) | script |
| 6 | Authz matrix generated = executed = passed, when the ticket touches an FN | script |
| 7 | RED evidence exists for new tests in add and fix tickets | script (lane result files) |
| 8 | Manual ACs have a human approval bound to the build hash | attested by human |
| 9 | Test-quality lenses (value bar, mocking, level fit) | lens, fresh-context reviewer if available, else labeled sequential fallback |

An unrun check yields INCOMPLETE (K4). Whether checks 1-8 scale with stakes depends on unresolved input R3. The proposal is that only check 9 and e2e breadth scale.

## 8. Layout, rationalizations, QA

```
testing/
  SKILL.md                       mode router + anatomy
  scripts/wings-lint.py          build-inlined; subcommands ids | lane | matrix | diff (depends on R2 and T2)
  references/modes/{author,gate,audit}.md
  references/{value-bar,levels,assertions,mocking,lanes,triage,authz-matrix,flakiness,ui-e2e}.md
  references/stacks/{js-ts,python}.md   each rule carries applies_to, status, verified_at, source
```

| Rationalization | Rebuttal |
|---|---|
| "Exit code 0, so tests pass" | Zero tests also exits 0. The lane counts tests. |
| "I'll add tests after" | Test-first is the default. Opting out is a logged decision. |
| "Mock it, it's faster" | Mocking the unit under test proves nothing. The integrity diff flags it. |
| "The test was wrong, so I fixed it" | TEST_EDITED needs a spec change or a human approval. |
| "That failure was already there" | Ambiguous defaults to in-branch. Prove it on the base commit. |
| "Coverage is 90%" | Coverage is a diagnostic and never evidence a regression is caught. |
| "Rerun, it's flaky" | One classification rerun, then it is a finding. |
| "Authz is covered by a manual check" | The matrix is generated. Manual checks are attested. |

QA (with and without the skill):
1. Author: a ticket with no seams. Expect a stop.
2. Gate: a suite that runs zero tests with exit 0. Expect FAIL.
3. Audit: a seeded suite (toBeDefined, a mocked unit under test, a deleted test, a CSS-property assertion). Expect all found, none invented.
4. Matrix: an FN missing its ownership predicate. Expect the cross-user cell to fail on its body assertion.
5. Change: weaken one assertion. Expect TEST_EDITED and a blocked close.

## 9. Decisions (all OPEN)

| ID | Decision | Alternatives | Amends |
|---|---|---|---|
| T1 | No test IDs. AC- ID goes in the test name, lint gets a code-reference scan over declared test paths. | Add a test ID prefix such as TST-n (fits the pattern, adds an ID to maintain) | K3 (unchanged under proposal), K12 lint scope |
| T2 | One wings-lint.py gains subcommands lane, matrix, diff. Lane results land in .wings/evidence/. Split only past about 1,000 lines (wings judgment). | Separate scripts per concern | K10, K12 |
| T3 | Matrix is JSON and attached-only. The test-writing step writes the harness but cannot edit cells. Executed-versus-generated is counted. | YAML per OWASP; allow standalone inference | none |
| T4 | TEST_EDITED class (section 5) | Fold into the generic integrity violation | none |

## 10. Cross-block interfaces (needs, not designs)

- Identity & Access would supply, as labeled lines on each FN: allowed roles, ownership predicate and owner field, tenant scope, allowed denial codes, auth recency, cookie-auth flag.
- Stack & Constraints would supply `verify.tests` per lane: cmd, result-file path, result format, non-production target. The oma-mobile stack.schema.json fields (detect, syntax, tests, pass_signal) are a seed.
- Plan & Build would carry seams, change type and AC IDs in the ticket. Binding required checks stays there.
- Code Review loads Testing's test-quality lens when installed, otherwise a labeled general lens.
- Data owns migration-test rules and supplies RLS-inventory cells.

## 11. Thin or unread

- Performance and load testing: no source. Only a hook exists (NFR AC- with Verify-by script). No authoring guidance in v1.
- Mutation and property-based testing: Trail of Bits files were never sent. v1 would reserve an optional enhancer lane and design nothing.
- Fixtures and determinism: the flakiness rule is my judgment. No source covers it.
- Level-selection matrix: exact wording comes from gstack at write time.