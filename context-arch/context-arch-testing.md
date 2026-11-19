# context-arch-testing.md: Testing block (13), first pass, master chat handoff

Architectural reasoning: Testing is where the "agent weakens the check to pass" threat becomes mostly mechanical. I designed it as scripts that make weakening visible (lane counts, integrity diff, immutable generated cells) plus a thin lens layer for judgment. It consumes Requirements (AC-, Verify-by) and the kernel (K4 vocabularies, K6 gates, K7 approvals), and it exposes interface needs on three blocks not yet designed. Dependency order: boundaries, test identity and lanes, rules, matrix, integrity diff, modes, gate, layout and QA.

Memory: nothing is saved, per the standing instruction. No memory tools were used.

## A. Status

| Item | State |
|---|---|
| Wings architecture D1-D12, kernel K1-K12 | Referenced as written in their own files. No new rulings made here. |
| Requirements design | Referenced as written. Its three pending decisions (R1-R3) are OPEN and are inputs here. |
| Testing design (arch-testing.md) | Proposed. Four decisions (T1-T4) OPEN. |
| Reference files, scripts, SKILL.md | Not drafted |

Nothing in this session is accepted. Where Testing depends on an unresolved decision, the dependency and a fallback are stated.

## B. Thinking mode

1. Same threat model as Requirements, one level down. The failure weighted most was the agent turning the suite green by editing, mocking or skipping. That produced the lane-count rule, the integrity diff and TEST_EDITED.
2. Mechanical before judgment. Gate checks 1-8 are scripts or human approvals. Only check 9 is a lens.
3. Declare interfaces, do not design neighbours. Identity, Stack and Plan & Build come later in design order. I wrote what Testing needs from each and left their shapes alone.
4. One home per fact. Each overlap (coverage, scope diff, RLS cells, migration tests) got a proposed owner before any rule was written.
5. Resolve source conflicts by consequence. "Mock the DB" (Addy) conflicts with "assert request role is not BYPASSRLS" (OWASP Multi_Tenant). I resolved it by what the test must observe, which produced the real-DB exception.
6. Standalone as a test of every choice. The matrix failed it, so it became attached-only. Honest degradation beats invented authorization lines.
7. Labeled judgment. TEST_EDITED, the 1,000-line split, the classification-rerun rule and the JSON matrix format are my choices. No source states them.
8. Hold decisions open. Earlier in the session I wrote as if Requirements' pending decisions were accepted. That was wrong. They are now listed as unresolved inputs with fallbacks.

## C. Unresolved inputs from Requirements (all OPEN)

| # | Decision | Effect on Testing if rejected |
|---|---|---|
| R1 | Boundary table (FLOW- here, NFR values in Stack, AC does not name the check) | Verify-by field and AC-ID-in-test-name binding are re-derived |
| R2 | wings-lint.py inlined into every gate-running sibling | Standalone Testing runs checks procedurally, labeled degraded |
| R3 | Stakes scaling on the judgment layer only | Testing defines its own scaling |

## D. Decisions proposed (all OPEN)

| ID | Proposal | Alternative |
|---|---|---|
| T1 | No test ID prefix. AC- ID goes in the test name. Lint gains a code-reference scan over declared test paths. Matrix cells identified by tuple, no ID. Would resolve kernel OPEN item 5. | A TST-n prefix |
| T2 | wings-lint.py gains subcommands ids, lane, matrix, diff. Lane results go to .wings/evidence/. Split only past about 1,000 lines (wings judgment). | Separate scripts per concern |
| T3 | Authorization matrix is JSON, attached-only, generated from FN lines. The test-writing step writes the harness but cannot edit cells. Executed-versus-generated is counted. | YAML per OWASP; standalone inference |
| T4 | TEST_EDITED class: an existing assertion modified in a change ticket whose AC- text did not change needs a human approval bound to the diff hash. | Fold into the generic integrity violation |

Proposed rules and the 9-check gate are in arch-testing.md sections 3, 5 and 7.

## E. Kernel and Requirements amendments the proposals would imply (not made)

- K10 would gain .wings/evidence/.
- K12 lint would gain subcommands ids | lane | matrix | diff and a code-reference scan.
- Kernel OPEN item 5 (test and cell ID shape) would be resolved by T1.
- Stakes scaling (R3) would apply to check 9 and e2e breadth only.

## F. Evidence tiers

| Tier | Content |
|---|---|
| Read directly in earlier chats, carried | Addy testing-patterns (JS-only, weak assertions listed as normal, CSS-property Playwright example); ECC test and QA skills and defects (data-testid, NODE_ENV guard, sandbox-header bypass); Requirements ACCEPTANCE_EDITED |
| Carried, not re-checked | gstack tests, failure triage and value bar; mattpocock tdd and seams; OWASP authorization regression and automation sheets (CC BY-SA, so adapt only in my own words or separate credited files); oma TDD evidence |
| My judgment | See section B item 7 |
| Never read | Trail of Bits mutation-testing, property-based-testing, spec-to-code-compliance; OpenSpec |

## G. Cross-block interface needs

- Identity & Access: labeled lines on each FN for allowed roles, ownership predicate and owner field, tenant scope, allowed denial codes, auth recency, cookie-auth flag.
- Stack & Constraints: verify.tests per lane with cmd, result-file path, result format, non-production target. Seed: oma-mobile stack.schema.json.
- Plan & Build: seams, change type and AC IDs carried in the ticket. Binding required checks stays there.
- Code Review: loads Testing's test-quality lens if installed, else a labeled general lens.
- Data: owns migration-test rules, supplies RLS-inventory cells.

## H. Thin or unread

- Performance and load testing: no source. Only a hook exists. No authoring guidance in v1.
- Mutation and property-based testing: files never sent. v1 would reserve an optional enhancer lane only.
- Fixtures and determinism: flakiness rule is my judgment.
- Level-selection matrix: wording taken from gstack at write time, not from memory.

## I. Unverified, do not carry forward

- Every gstack, mattpocock, OWASP and ECC detail above (carried, not re-checked in this pass).
- The claim that JUnit XML is the most reliably parseable result format across stacks (judgment).
- The 1,000-line split threshold and the one-classification-rerun rule (wings judgment).

## J. Files that would improve this block

1. Trail of Bits mutation-testing, property-based-testing, spec-to-code-compliance (separate credited files if used).
2. The gstack test-level decision matrix text, for levels.md.
3. OWASP Authorization_Regression_Testing and Authorization_Testing_Automation, if verbatim adaptation is wanted.

## K. Next step

Resolve R1-R3 and T1-T4, or tell me which to design around as open. Then Code Review (block 12), which consumes this block's integrity diff and test-quality lens, the kernel's K5 finding shape and the coverage-accounting rule.