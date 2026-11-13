# SDLC Process

Twelve cards are within the fourteen-card cap: seven Addy skills, three Superpowers additions, plus Spec Kit tasks/converge and Superpowers verification. Other targets remain skipped in `progress.md`; this is a capped, evidence-bounded synthesis.

## RANKED CANDIDATES
1. [Spec Kit tasks and converge](../skills/github__spec-kit/spec-kit-tasks-converge.md) — story-grouped phased tasks, source refs, append-only reconciliation.
2. [Addy planning and task breakdown](../skills/addyosmani__agent-skills/planning-and-task-breakdown.md) — dependency-aware tasks with interfaces, tests and review focus.
3. [Addy incremental implementation](../skills/addyosmani__agent-skills/incremental-implementation.md) — thin vertical slices verified and committed individually.
4. [Addy code review and quality](../skills/addyosmani__agent-skills/code-review-and-quality.md) — five-axis review, caller/test filtering and structural remedies.
5. [Superpowers verification](../skills/obra__superpowers/verification-before-completion.md) — requires fresh command output before a completion claim.
6. [Addy Git workflow](../skills/addyosmani__agent-skills/git-workflow-and-versioning.md) and [Superpowers branch finishing](../skills/obra__superpowers/finishing-a-development-branch.md) — atomic history and user-controlled integration.
7. [Addy shipping](../skills/addyosmani__agent-skills/shipping-and-launch.md) and [CI/CD](../skills/addyosmani__agent-skills/ci-cd-and-automation.md) — measurable rollout, monitoring and rollback gates.
8. [Addy documentation/ADRs](../skills/addyosmani__agent-skills/documentation-and-adrs.md) — decision context and fact-preserving docs.
9. [Superpowers writing plans](../skills/obra__superpowers/writing-plans.md) and [requesting review](../skills/obra__superpowers/requesting-code-review.md) — exact plan interfaces and bounded fresh review.

## COMPARISON MATRIX
| Source | Stages / gates | State / resume | Review / approval | Fit |
|---|---|---|---|---|
| Spec Kit tasks/converge | Setup, Foundational, user stories, Polish; converge after implement | `tasks.md`, stable IDs; append-only | CRITICAL/HIGH/MEDIUM/LOW; no reviewer model | Single-agent possible; hooks may run commands |
| Addy plan/increment | Plan → slices → test/build → commit | `tasks/plan.md`, task list, git | Plan approval; scope discipline | Simple; repo-native commands |
| Addy review / Superpowers review | Five-axis review; fresh reviewer gets exact range/context | Review output, no shared ledger | Addy severity labels; Superpowers subagent | Parallel review costs extra context |
| Addy CI / ship | Quality gates → staging → canary → rollout/rollback | YAML, flags, dashboards, runbooks | Required reviews/checks; human ship approval | GitHub Actions/provider examples |
| Addy docs / ADR | Proposed → accepted → superseded/deprecated | ADR, README, changelog | Project convention first | Portable formats, project-specific templates |
| Superpowers finish | Verify → detect workspace → choose merge/PR/keep | Git history and worktree | Explicit user choice; destructive discard confirmation | Requires a user at integration |

## CONFLICTS
- Spec Kit `converge` is not a git diff/branch comparison and may invoke configured hooks; test tasks are optional by default.
- Addy CI says “no gate can be skipped” but labels E2E optional. Make required gates explicit for each project.
- Addy review severity (`Critical`, required/no-prefix, `Nit`, `Optional`, `FYI`) differs from Spec Kit's four-level scale and Superpowers' Critical/Important/Minor.
- Addy incremental implementation says commit each slice; preserve repository and user approval policy for commits.
- Superpowers writing-plans references `references/definition-of-done.md`, but that path is absent in the clone. The card records the broken dependency.
- Superpowers plans recommend execution subskills; executing-plans was read but not carded because its scripts and linked execution/review protocols were not fully reviewed.

## QUESTIONS ANSWERED
- **Stages, gates and DoD:** Spec Kit sequences Setup → Foundational → user stories → Polish, then classifies gaps and appends traceable tasks. Addy plans and slices work; every increment gets test/build checks. Addy's standing DoD includes runtime proof, tests, lint, integration, docs, security, observability, rollback and human review. CI blocks merge on configured gates. Shipping adds staging, canary, metric thresholds and rollback. Superpowers verification requires fresh output before claiming completion. (`spec-kit-tasks-converge.md`; `planning-and-task-breakdown.md`; `incremental-implementation.md`; `references/definition-of-done.md:L1-L67`; `verification-before-completion.md:L22-L48`)
- **Review loops and isolation:** Addy reviews correctness/readability/architecture/security/performance, reviews tests first, filters findings against callers and tests, then verifies evidence. Superpowers requesting-review sends a fresh reviewer a precise read-only range and requires strengths, findings, recommendations and verdict. Git worktrees isolate parallel streams; merge/PR/keep is an explicit user choice. [Code review source](../skills/addyosmani__agent-skills/code-review-and-quality.md); [review request](../skills/obra__superpowers/requesting-code-review.md); [Git workflow](../skills/addyosmani__agent-skills/git-workflow-and-versioning.md).
- **Severity and convergence:** Severity is inconsistent across the carded sources; normalize it in a house schema. Spec Kit's converge classifies gaps and appends only traceable remaining tasks, but does not compare branches. No shared cross-tool convergence contract appears.
- **Branch/PR and releases:** Addy recommends short-lived branches, atomic commits, protected main, required reviews/checks, SemVer tags and impact-oriented changelogs. Superpowers verifies tests, then offers merge, PR or keep; it forbids unapproved discard/force cleanup. (`git-workflow-and-versioning.md`; `finishing-a-development-branch.md`)
- **Decision records and retros:** Addy specifies ADR lifecycle and changelog conventions. No carded source defines a retrospective/learning-capture process.
- **Plan/task formats and resumability:** Addy defines plan header, global constraints, review focus, task interfaces, acceptance criteria, verification commands and dependencies; Spec Kit stores task state in `tasks.md`; Superpowers writing-plans names a dated plan and task list. Git history preserves increment state. The missing DoD link and uncarded execution protocols weaken end-to-end resume evidence.
- **Parallel agents and single-agent behavior:** Addy permits independent vertical slices after shared contracts are defined and recommends worktrees. Superpowers review requests use a separate agent; Spec Kit is single-agent-capable, but hooks may be mandatory. No carded source offers one portable coordination/state model spanning agent and no-agent environments.
- **Shipping/CI:** Addy uses baseline-relative thresholds and feature flags, requires rollback readiness, separates CI from production secrets and recommends small deploy batches. Thresholds are illustrative, not universal policy. No pipeline/deployment command was run.

## GAP EVIDENCE
- Branch/PR, retrospective, decision-record, resume and checkpoint search across the original Spec Kit task/converge and verification sources returned mostly story checkpoints and generic PR/verification references; `converge.md:L69` explicitly rejects branch comparison.
- The new cards add ADR conventions and Git/PR flow, but still provide no retrospective/learning protocol or common severity mapping.
- Scope is the twelve carded sources. The remaining SDLC candidates are recorded as skipped; no claim is made about them.

## TECHNIQUES WORTH TAKING
1. Put shared blockers before user-story implementation; include independent tests and concrete paths. (`templates/tasks-template.md:L48-L115`)
2. Keep convergence append-only; treat checked boxes as claims requiring evidence. (`templates/commands/converge.md:L71-L86`, `L145-L172`)
3. Make task interfaces, expected verification output and highest-risk uncovered inputs explicit. (`planning-and-task-breakdown.md`; `writing-plans.md`)
4. Verify each increment before committing; keep rollback and flag ownership explicit. (`incremental-implementation.md`; `shipping-and-launch.md`)
5. Require a fresh, read-only review range and evidence-calibrated severity. (`requesting-code-review.md`; `code-review-and-quality.md`)
6. Keep ADRs, changelogs and prose edits factual; do not erase decision history. (`documentation-and-adrs.md`)
7. Require fresh test output before completion and preserve user control over integration. (`verification-before-completion.md`; `finishing-a-development-branch.md`)

## DO NOT TAKE
Do not treat unchecked tasks as complete, run configured hooks without review, overwrite unfinished plans, apply universal rollout thresholds, or merge/delete/push without authorization. Do not equate convergence with branch comparison or infer retrospectives from ADRs.

## CATALOG
| Carded target | Status |
|---|---|
| GitHub Spec Kit tasks/converge | Carded |
| Superpowers verification-before-completion | Carded |
| Addy: planning/task breakdown; Git workflow; shipping; CI/CD; code review; documentation/ADRs; incremental implementation | Seven cards; direct linked references read |
| Superpowers: writing-plans; finishing-a-development-branch; requesting-code-review | Three cards; writing-plans DoD link absent |
| Superpowers executing-plans | Read 323-line skill; scripts and dependencies not expanded; not carded |
| Superpowers systematic-debugging | Skipped |
| Other targets (EveryInc, gstack, BMAD, harness, Sentry, SpecWeave, Borkweb, claude-loom) | Skipped or lineage-only as recorded in `progress.md` |
