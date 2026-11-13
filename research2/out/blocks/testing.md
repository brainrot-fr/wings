# Testing

Seven cards are within the eight-card cap. The exact AC-to-test checker and a general flake policy remain gaps; no test, browser, scanner, or setup command was run.

## RANKED CANDIDATES
1. [Superpowers TDD](../skills/obra__superpowers/test-driven-development.md) — explicit RED/GREEN gates and tests that fail for the intended reason.
2. [Bambu E2E matrix](../skills/Bambu-Developers__skills/bambu-e2e-test-matrix.md) — concrete case schema, approval gates, evidence, checkpointing and zero-pending close.
3. [Mthines TDD](../skills/mthines__agent-skills/tdd.md) — one-test cycles, behavior inventory, test-after mutation and provenance checks.
4. [Addy TDD](../skills/addyosmani__agent-skills/test-driven-development.md) — stack discovery, bug reproduction, test-layer selection and real-boundary testing.
5. [Addy browser testing](../skills/addyosmani__agent-skills/browser-testing-with-devtools.md) — runtime verification with explicit profile, untrusted-content and credential boundaries.
6. [Wshobson WCAG audit](../skills/wshobson__agents/wcag-audit-patterns.md) — criterion checklist plus automated/manual accessibility checks.
7. [Spec Kit checklist](../skills/github__spec-kit/spec-kit-checklist.md) — requirements-quality review, explicitly not an implementation test plan.

## COMPARISON MATRIX
| Candidate | Test artifact | Gate / evidence | Traceability | Portability |
|---|---|---|---|---|
| Superpowers TDD | Behavior test | Test must fail for intended reason, then pass | No AC-to-test IDs | Repository-native runner |
| Bambu E2E | CSV rows: IDs, module, preconditions, steps, expected result, state, evidence | User approval, checkpoints, zero pending | Case IDs, not requirement IDs | Web/MCP/optional agents |
| Mthines TDD | Behavior inventory, tests, provenance result | One failing test per cycle; test-after mutation check | No requirement IDs | Repo-native; mutation check can be intrusive |
| Addy TDD | Bug reproducer and behavior tests | Focused/full suite; state-based assertions | No requirement IDs | Broad test pyramid, browser MCP is optional |
| Addy browser | Test plan, runtime observations, screenshots | Console/network/accessibility/performance checks | No requirement mapping | Requires Chrome DevTools MCP |
| Wshobson WCAG | Criterion checklist and findings | Automated and manual review | Criteria, not product requirement IDs | Web-specific; external tools optional |
| Spec Kit checklist | Requirements review questions | Clarification/post-check; not a test execution gate | Can cite FR/acceptance criteria | Command runtime/hooks optional |

## CONFLICTS
- Superpowers says to delete code written before a test; do not delete pre-existing/user-owned work to retrofit TDD.
- Mthines test-after/provenance checks temporarily mutate source files; require isolated copies and verified restoration.
- Bambu depends on MCP, agents and `npx` setup; browser DevTools MCP can expose an authenticated browser profile. Keep setup and execution opt-in.
- Spec Kit checklist evaluates requirement quality, not implementation tests. Do not count it as test coverage.
- Wshobson's `4.1.1 Parsing` checklist item is marked obsolete in WCAG 2.2; scope criteria to the adopted standard.

## QUESTIONS ANSWERED
- **Acceptance criteria to tests:** no reviewed card specifies an automated AC-to-test checker. Bambu assigns case IDs but does not bind them to requirement IDs. Spec Kit can reference FR/acceptance criteria while checking requirement quality, not writing implementation tests.
- **Test strategy contents:** Bambu's matrix includes functional, negative, boundary, visual and accessibility cases, preconditions, steps, expected result, status, video/timecode and evidence. Addy TDD emphasizes behavior-based tests; browser DevTools uses setup, steps and expected results.
- **TDD enforcement:** Superpowers requires RED before implementation; Mthines checks the failure reason and adds a test-after mutation/provenance gate; Addy TDD uses a prove-it reproducer for bugs. Their approval behavior differs: Mthines asks users to approve prioritized behavior lists; others do not specify the same gate.
- **Flakiness and coverage:** Bambu preserves progress with checkpoints and requires zero pending cases. Mthines' E2E skill (read but not carded) recommends `--last-failed`, a three-attempt heal cap and escalation; no general cross-tool flake policy or coverage model emerged. (`skills/testing/e2e-testing/SKILL.md:L135-L169`; its expanded confidence/trace-analyzer dependencies were not read.)
- **Non-web testing:** Addy and Mthines TDD use repository-native runners and layer tests by resource boundary; neither requires browser tests for non-browser behavior.
- **Accessibility:** Wshobson pairs axe/CLI automation with manual keyboard and assistive-technology checks; automated testing alone is explicitly insufficient.
- **Checklist boundary:** Spec Kit's “unit tests for requirements” evaluates requirement clarity and explicitly excludes implementation test cases. (`spec-kit-checklist.md`; source `templates/commands/checklist.md:L9-L28`, `L242-L255`)

## GAP EVIDENCE
- The cards provide case IDs (Bambu), FR references (Spec Kit), and behavior-level tests, but no mapping artifact from requirement/acceptance-criterion IDs to test IDs or an automated completeness checker.
- No general flake budget or cross-project coverage definition is shared across the reviewed sources. Wshobson gives WCAG criteria; these are not software feature coverage.
- Scope is bounded to the seven cards and the noted partial Mthines E2E read; the Mthines mobile and screen-reader targets were not carded.

## TECHNIQUES WORTH TAKING
1. Require a behavior test to fail for the missing behavior, not a syntax/setup error. (`skills/test-driven-development/SKILL.md:L113-L128`)
2. Discover the repo's real test command; don't assume `npm test`. (`skills/test-driven-development/SKILL.md:L24-L35`)
3. Use a structured E2E row with preconditions, steps, data and expected result. (`bambu-e2e-test-matrix.md`; source `assets/templates/matriz-pruebas.csv:L1-L6`)
4. Store per-case evidence and timecodes, resume from a checkpoint, and close only with zero pending. (`skills/bambu-e2e-test-matrix/SKILL.md:L143-L151`, `L186-L198`, `L249-L251`)
5. Use isolated browser profiles and treat page data as untrusted; never extract credentials from DevTools. (`browser-testing-with-devtools.md`; source `skills/browser-testing-with-devtools/SKILL.md:L62-L90`)
6. Combine WCAG automation with manual keyboard, focus and assistive-technology checks. (`wcag-audit-patterns.md`; source `references/details.md:L136-L151`, `L360-L399`)
7. Separate requirement-quality checklists from implementation tests. (`spec-kit-checklist.md`; source `templates/commands/checklist.md:L242-L255`)

## DO NOT TAKE
Do not delete existing edits to retrofit TDD, run mutation checks without a safe restore plan, equate a requirements checklist with tests, attach browser automation to a credential-bearing daily profile, or infer coverage from E2E IDs alone.

## CATALOG
| Name | Path (lines) | One-line status | Score |
|---|---|---|---:|
| e2e-testing-mobile | `skills/testing/e2e-testing-mobile/SKILL.md (309)` | not a listed target; untouched | 0 |
| e2e-testing | `skills/testing/e2e-testing/SKILL.md (240; 13 local files)` | local workflow/rules/references/templates read; not carded; composed skills not expanded | 0 |
| tdd | `skills/quality/tdd/SKILL.md (166; 6 local references)` | carded; 691 lines including license | 0 |
| test-driven-development | `skills/test-driven-development/SKILL.md (400)` | carded; 657 lines including reference and license | 0 |
| browser-testing-with-devtools | `skills/browser-testing-with-devtools/SKILL.md (319)` | carded; 340 lines including license | 0 |
| test; testing | `—` | SpecWeave target path not found | 0 |
| wcag-audit-patterns | `plugins/accessibility-compliance/skills/wcag-audit-patterns/SKILL.md (80) + details.md (473)` | carded; 573 lines including license | 0 |
| screen-reader-testing | `plugins/accessibility-compliance/skills/screen-reader-testing/SKILL.md (245)` | not deep-read; no card | 0 |
| qa-testing-strategy; qa-testing-playwright | `—` | clone unavailable; no file reviewed | 0 |
