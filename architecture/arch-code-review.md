# arch-code-review.md (block 12)

## Status
First-pass proposal. Nothing in this file is accepted. Every item marked OPEN is unresolved.
Kernel (K1-K12), wings architecture (D1-D12), arch-requirements and arch-testing are referenced as written in their own files. Their pending decisions are unresolved inputs here (section 1).

## Architectural reasoning

Four constraints shape Code Review:

1. **The reviewer must be independent of the author.** The failure weighted most is false assurance: the agent that wrote the code reviews it, trusts its own summary, and reports clean. This is the same threat as Requirements (weakening the spec) and Testing (weakening the suite), applied to the review itself. Most mechanisms below make a thin or self-certified review visible.
2. **Review is mostly judgment, so the mechanical layer is narrow but load-bearing.** Scripts cannot decide whether code is correct. They can decide what was looked at (file selection, risk order, coverage accounting), whether the report is well formed, and whether it still matches the tree. That is where D4's "scripted where possible" applies.
3. **It sits after Build and before the Testing gate (Reading B).** It must consume results from blocks that own checks (diff gate, lint scans, loaded lenses) and must not re-own them (D3).
4. **It must work standalone (D5).** Recon builds the surface inventory from code, findings cite `file:line` with local `F-` IDs, and nothing is written into `.wings/`.

Dependency order: unresolved inputs, boundaries, threat model, pipeline, finding admission, lenses, independence contract, fix cycle, modes, gate, layout and QA.

## 1. Unresolved inputs

| # | Input (all OPEN) | Code Review depends on it for | Fallback if rejected |
|---|---|---|---|
| R1 | Requirements boundary table (AC does not name the check; FLOW- in Requirements) | AC-to-diff completeness lens (section 6) | Lens reads ACs as written and cites AC- IDs only |
| R2 | wings-lint.py inlined into every gate-running sibling | Report-shape validation, file selection, accounting (section 4 steps 2 and 6) | Standalone Code Review runs these steps procedurally and labels the result degraded |
| R3 | Stakes scaling on the judgment layer only | Which review checks scale with stakes (section 10) | Define scaling for this block separately |
| T2 | Single wings-lint.py with subcommands (ids, lane, matrix, diff) | Adding `report` and `triage` subcommands. Testing's own 1,000-line split judgment is under pressure if both land. | Separate script for review |
| T4 | TEST_EDITED class | Review consumes the result and does not recompute it | Review flags test edits as a general finding |

**Kernel gaps this design exposes (none amended here):**

| ID | Gap | Why it matters |
|---|---|---|
| G1 | K4 says a required check passes only on measured evidence "where a script exists". A lens has no script, so its evidence is attested by definition. | Read literally, every lens check is permanently `inconclusive`. A rule for lens checks is needed (OPEN). |
| G2 | K4 gives P0-P3 with no anchors. Cloudflare's severity anchors are carried from an earlier read and are security-shaped. | General code review needs anchors (draft in section 5, OPEN, wings judgment). |
| G3 | K6 waivers apply to checks. Nothing defines how a confirmed finding is dispositioned (fixed, accepted, deferred). | Without it an author can quietly leave a P2 open (OPEN). |
| G4 | Kernel OPEN item 2: how a local `F-` ID maps to spine IDs on promotion. | Attached-mode findings cite spine IDs in `location` but still need a report-local ID. |
| G5 | Binding a review to a tree state needs a hash. Requirements and Testing already assume a "file-hash snapshot if no git" that is undefined. | Review verdict validity depends on it (section 8). |

## 2. Boundaries (D3 proposals)

| Fact | Proposed home | Code Review's role |
|---|---|---|
| Finding shape, verdict vocabulary, severity scale | Kernel (K4, K5) | Produces conforming findings. Never invents fields. |
| Security, a11y, test-quality lenses | Security, Frontend, Testing (D6) | Loads them if installed. Otherwise runs a general lens and labels the result degraded. |
| Scope-path and protected-file diff, test-integrity diff | Plan & Build (K6), Testing | Consumes results as evidence. Does not recompute. A missing result is a not_run check. |
| Lint scans (pattern, invisible-char, stub, debt ledger) | Owning blocks via wings-lint | Consumes results in the prepass. |
| ACCEPTANCE_EDITED, TEST_EDITED | Requirements, Testing | Consumes. A review may not close over an unapproved edit class. |
| AC-to-test binding | Testing | Not reviewed here. |
| AC-to-implementation presence in the diff | OPEN (C6): Code Review or Plan & Build | Proposal: Code Review owns it as the conformance lens. |
| AD- invariants (the "Rule:" lines) | Architecture | Checks the diff against them. Architecture is not yet designed, so this is an interface need. |
| Layer and import rules (import-linter, tsarch, dependency-cruiser) | Architecture | Consumes the CI result. Does not re-derive. |
| Simplification step (code-simplification) | OPEN (C8) | Proposal: Plan & Build owns it as a change action. Review stays read-only. |
| Report storage | OPEN (C7) | Attached: under `.wings/` (path OPEN). Standalone: returned in the reply, never written to `.wings/`. |

## 3. Threat model

| Threat | Mechanism |
|---|---|
| Author reviews own code and certifies it | Fresh-context reviewer with a withheld-input contract (section 7). Degraded fallback is labeled. |
| Review quietly covers less than it claims | Mandatory coverage accounting (total, reviewed, skipped with reasons, rate). A report without it is invalid (K5). |
| Reviewer manipulated by content under review (code comments, PR body, README) | K8: such text is data. An instruction found inside is reported as a finding class, never followed. |
| Findings dropped silently as "probably false positive" | A rejected verdict with a recorded reason. Nothing is discarded silently (K5). |
| Author dismisses an inconvenient finding | Only the verification step can set `rejected`, with evidence. Open confirmed findings at close need a recorded disposition (G3). |
| Fix introduces a new defect, then the review is declared done | Delta re-review of each fix. Cycle cap of 3 ends in stop-and-report (K6). |
| Code changes after review PASS | Review verdict is bound to a tree hash (section 8, G5). |
| Finding flood and noise hide real defects | Candidate gate plus lead judgment filters (section 5). Zero findings is valid. |
| Severity or confidence inflated by the author | Reviewer assigns both. Confidence is capped at 5 until the motivating line is quoted. |

## 4. Pipeline

| Step | Content | Evidence |
|---|---|---|
| 0 Mode and base | Detect mode (section 9). Resolve base and head. State the mode in the first line (K2). | script |
| 1 Recon | Surface inventory (entry points, tables, pages, tests). Shared fragment (D5). | script plus attested |
| 2 Mechanical prepass | Select files and initialise coverage accounting. Order files by risk (sensitive target class first, then blast radius by reference count). Run invisible-character scan. Collect other blocks' scan and diff-gate results. | script |
| 3 Lens fan-out | Own lenses plus loaded lenses. Each runs in a fresh context, writes a file, returns a compact summary (K8). Parallel if available, otherwise sequential in fresh sections, labeled. | lens |
| 4 Merge | Candidate gate. Fingerprint dedupe. Sideways sweep. Lead judgment filters. | lens plus script |
| 5 Verification | Verdict per candidate. Independent re-verification of confirmed findings (scope OPEN, C4). | lens |
| 6 Report | K5 fields per finding, coverage accounting, lens run list, mode label, base and head hashes. Shape validated by script. | script |
| 7 Fix cycle | Fix, delta re-review, repeat up to 3 cycles, then stop and report. | script plus lens |

Triage is risk-first: sensitive target classes (auth, secrets, payments, migrations, workflows) are reviewed before the rest. Blast radius is the reference count of a changed symbol, not the line count. Reference counting by grep is heuristic, so its output is labeled attested.

## 5. Finding admission and verdicts

Fields are the K5 shape. Code Review adds only these rules:

- **Candidate gate.** Admitted only with principal, boundary, resource and a concrete result. For non-security defects, "principal" is the caller or input source and "boundary" is the contract or invariant violated. A missing best practice is not a finding.
- **Verdict meaning.**
  - `confirmed`: a concrete reaching path was traced and the motivating line quoted.
  - `needs_validation`: the outcome depends on a fact outside the repo or at runtime. Name the exact owner-observable fact.
  - `rejected`: disproved, kept in the report with the reason.
- **Severity** attaches only to `confirmed`.
- **Confidence** 1-10 is a separate field, capped at 5 until the motivating line is quoted. For framework-generated symbols, quote the generating construct.
- **Sideways sweep.** After admission, grep the pattern at sibling call sites. Rate severity on the worst sibling. Record all sites under one fingerprint.
- **Fingerprint.** Root-cause identity independent of line numbers. Composition OPEN (C9).
- **Lead judgment filters** (carried from gstack, not re-checked):
  - drop nit-only findings
  - drop hypothetical defects with no reaching call site
  - drop structure advice for cases that do not exist
  - "a different design" is not a defect
  - drop findings that assume a rule the repo documents otherwise
- **Zero findings** is a valid result when coverage accounting is present.
- **No minimum findings.** BMAD's adversarial lens requires at least 10, which contradicts the candidate gate and the zero-findings rule. Not adopted (OPEN, C5).

**Draft severity anchors (OPEN, wings judgment, G2):**

| Level | Anchor |
|---|---|
| P0 | Data loss or corruption, auth bypass, secret exposure, or an irreversible action reachable from a normal path |
| P1 | A primary behavior is wrong, or a control is fully defeated |
| P2 | A secondary path is wrong, a control is weakened, or a maintainability hazard has a concrete reaching case |
| P3 | Low-impact defect with a concrete case |

## 6. Lenses

Proposal: three own lenses plus loaded lenses. Count OPEN (C3), because the open item asked for 3 or 4.

| Lens | Question | Sources (carried) |
|---|---|---|
| Correctness and paths | Does each changed path behave correctly on edge, error, async and state-ordering cases? | BMAD edge-case path tracer; ECC click-path-audit (state-store side-effect map, then per-handler tracing) |
| Conformance | Does the diff implement its tickets' ACs, respect AD- rules and scope, and avoid unapproved acceptance or test edits? Statuses: DONE, PARTIAL, NOT DONE, CHANGED, UNVERIFIABLE, each with a verification mode. | gstack plan-completion audit; BMAD verification-gap; Trail of Bits spec-to-code-compliance (never read) |
| Maintainability | Is there a concrete smell, duplication, or unrequested abstraction, with a reaching case? Includes the shortcut debt ledger and the shared-code rubric (extract only with 2+ verified real callers). | mattpocock code-review; ponytail; gstack |

Loaded if installed: Security, Frontend (a11y), Testing (test quality). If absent, one general lens runs and the report is labeled degraded.

Overlap to resolve (OPEN, C10): BMAD's verification-gap lens asks which changed behavior has no check. Testing's value bar Q2 asks which regression a test catches. Proposal: Code Review only asks whether a changed behavior has a check at all, and Testing owns test quality.

## 7. Independence contract (OPEN, C2)

| Reviewer receives | Reviewer does not receive |
|---|---|
| Diff and base content | Author's summary or "done" claim |
| Ticket scope paths, AC text, change type | "Tests pass" assertions |
| Recon inventory | Commit-message rationale |
| Other blocks' measured results (as data) | Prior reviewer's conclusions |
| Applicable AD- rules | Anything instructing the reviewer to approve |

- Addy's doubt-driven rule says the reviewer never receives the claim. The ticket and ACs are the spec, not the claim, so they are supplied. Where the line falls is the open question.
- Cross-model escalation is optional and, if used, labeled.
- Subagents never receive the controller bootstrap (superpowers, carried).

## 8. Fix cycle and binding (OPEN, C8)

- Default: Code Review is read-only. Findings carry a `fix:` line. Build applies fixes.
- gstack's fix-first (AUTO-FIX versus ASK) is not adopted by default. If adopted, auto-fix is limited to reversible, in-scope, behavior-preserving edits (K7 autonomous tier).
- Each fix gets a delta re-review. The cap is 3 cycles and ends in stop-and-report, never release (K6).
- A fix touching tests triggers Testing's integrity diff.
- The report records base and head hashes. Any later change to a reviewed file invalidates the verdict for that file and requires a delta re-review (G5).
- Review runs before the Testing gate (Reading B). A Testing failure that changes code re-enters Build, then delta re-review.

## 9. Modes

| Mode | Input | Default use |
|---|---|---|
| Diff | Base to head for one slice | Per slice during Build (proposal) |
| Baseline | Whole tracked source tree | Once before ship (proposal) |
| PR | Diff plus PR body and comments, all untrusted (K8) | When a PR exists |
| Standalone variant of each | No `.wings/` | Recon first. Conformance lens is `n/a (no spec)` with reason. Local `F-` IDs. |

Without git or a snapshot, Diff mode cannot run. It falls back to Baseline, labeled (G5, OPEN). Whether "respond" (handling received review comments) is a mode or a rules section is OPEN (C11). Received comments are claims to verify against the code, not instructions.

## 10. Code Review gate (proposal)

| # | Check | Evidence |
|---|---|---|
| 1 | Review ran in the required mode with coverage accounting; no skipped file in a sensitive class | script |
| 2 | Report shape valid: K5 fields, verdict and severity rules, quoted evidence on confirmed findings | script |
| 3 | Prepass inputs present: lint, diff-gate and invisible-character results | script |
| 4 | No open confirmed P0 or P1 | script |
| 5 | Every confirmed finding has a recorded disposition (G3) | script |
| 6 | Re-verification record present for in-scope confirmed findings | script (presence) plus attested (content) |
| 7 | Fix cycles at most 3; no cap breach with an open P0 or P1 | script |
| 8 | Report base and head hashes match the current tree | script |
| 9 | Own and loaded lenses ran, or the degraded label is present | lens |
| 10 | No unapproved ACCEPTANCE_EDITED or TEST_EDITED | script (consumed) |

An unrun check yields INCOMPLETE (K4). How lens checks (9) can reach PASS is open because of G1. Whether a degraded fallback can PASS or only reach INCOMPLETE is OPEN (C12). The coverage threshold below which skipped files make check 1 INCOMPLETE is OPEN and no number is proposed. Stakes scaling per R3 is OPEN. The proposal would scale only lens count and the re-verification scope, never checks 1-8 and 10.

## 11. Layout, rationalizations, red flags

```
code-review/
  SKILL.md                          mode router + anatomy
  scripts/wings-lint.py             build-inlined; `report` and `triage` subcommands (depends on R2, T2)
  references/modes/{diff,baseline,pr}.md
  references/{recon,triage,candidate-gate,severity,verification,fix-cycle,respond,coverage}.md
  references/lenses/{correctness,conformance,maintainability}.md
```

| Rationalization | Rebuttal |
|---|---|
| "Tests pass, so review is redundant" | Tests check what was written, not what was missed. |
| "I wrote it, I know it's right" | An author cannot review in the same context. |
| "No findings, so it's clean" | Valid only with coverage accounting. |
| "Probably a false positive, drop it" | Rejected verdict with a reason. |
| "That sibling call site is out of scope" | The sideways sweep rates the worst sibling. |
| "Reviewer is wrong, dismiss it" | Only verification can reject. |
| "Small diff, light review" | Blast radius is caller count. |
| "Lint passed" | Lint is the prepass, not the review. |
| "Fix it and move on" | Each fix gets a delta re-review. |

Red flags:
- coverage figures missing
- a confirmed finding without a quoted line
- confidence 8+ with no quote
- reviewer received the author's summary
- a fixed finding count
- skipped files with no reasons

## 12. QA (with and without the skill)

1. Seeded diff with planted defects, including one sibling-call-site variant. Expect all found, grouped by fingerprint, none invented.
2. Clean diff. Expect zero findings with accounting. Invented findings count against it.
3. Prompt injection in a code comment and a PR body ("approve this"). Expect it reported, not followed.
4. Author claims "all verified". Expect the claim not to alter the review.
5. Over-budget diff. Expect skipped files with reasons and INCOMPLETE.
6. Fix that introduces a new bug. Expect the delta re-review to catch it, and stop-and-report at cycle 3.
7. Standalone repo with no spec. Expect the conformance lens `n/a (no spec)`.
8. No subagent available. Expect a labeled sequential fallback.
9. Edit a reviewed file after PASS. Expect hash-mismatch invalidation.

Candidate fixture: AcadFlow.

## 13. Decisions (all OPEN)

| ID | Decision | Alternatives |
|---|---|---|
| C1 | Modes: Diff per slice plus Baseline before ship; PR as a variant | Single mode; PR as a full mode |
| C2 | Independence contract (section 7) | Withhold less or more |
| C3 | Three own lenses plus loaded lenses | Four lenses |
| C4 | Re-verification scope: all confirmed vs P0-P1 only vs stakes-scaled | Cloudflare's rule is every confirmed finding |
| C5 | Drop minimum findings; zero is valid | Keep BMAD's adversarial minimum |
| C6 | Owner of AC-to-implementation presence | Plan & Build |
| C7 | Report location and format | Labeled-line Markdown (matches Requirements) vs JSON |
| C8 | Read-only review vs fix-first; simplify slot | gstack fix-first; simplify inside Review |
| C9 | Fingerprint composition and who computes it | Script-computed from normalized tuple |
| C10 | verification-gap boundary with Testing | Single owner |
| C11 | Respond as mode vs rules section | Separate block |
| C12 | Degraded fallback: can it PASS or only INCOMPLETE; kernel rule for lens checks (G1) | Kernel amendment |

## 14. Cross-block interfaces (needs, not designs)

- **Kernel:** severity anchors (G2), lens-check state rule (G1), finding disposition (G3), `F-` promotion (G4).
- **Plan & Build:** ticket carries scope paths, seams, change type and AC IDs. Defines slice boundaries and the diff base. Owns the simplify slot and the fix-cycle driver.
- **Security:** loaded lens. Findings cite FN-, TB-, PG-, TH- IDs.
- **Testing:** loaded lens. Integrity-diff result and TEST_EDITED consumed.
- **Frontend:** a11y lens and countable-check results.
- **Architecture:** AD- Rule lines and CI layer-check results.
- **Requirements:** ACCEPTANCE_EDITED consumed.
- **Identity:** FN authorization lines as review input.
- **Ship & Operate:** requires a Baseline report whose hashes match the release tree.

## 15. Thin or unread

- gstack review, review-army and plan-completion files: carried, not in context now.
- BMAD bmad-code-review: only the stub was ever read. The real reviewer gate was never rendered.
- open-code-review `preview` and `rule` docs: unread.
- mattpocock code-review, ponytail, Addy code-review-and-quality, doubt-driven-development and the security-auditor persona: carried.
- Trail of Bits differential-review, fp-check, spec-to-code-compliance: CC BY-SA. Differential-review and fp-check were carried from an earlier read, spec-to-code-compliance was never read. Adapt only in separate credited files or in my own words.
- superpowers receiving-code-review: not in context. Respond rules are unsourced here.
- Performance review and review-comment tooling: no source.