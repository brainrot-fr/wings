# context-arch-code-review.md: Code Review block (12), first pass, master chat handoff

Architectural reasoning: Code Review is the third block where "the agent certifies its own work" becomes the central threat. It is mostly judgment, so I designed it as a narrow mechanical layer (what was looked at, in what order, whether the report is well formed and still matches the tree) around an independent lens layer. It consumes the kernel (K4, K5, K6, K7, K8), Requirements (ACCEPTANCE_EDITED) and Testing (integrity diff, test-quality lens). It exposes five kernel gaps and several interface needs on blocks not yet designed. Dependency order: unresolved inputs, boundaries, threat model, pipeline, finding admission, lenses, independence contract, fix cycle, modes, gate, layout and QA.

Memory: nothing is saved, per the standing instruction. No memory tools were used.

## A. Status

| Item | State |
|---|---|
| Wings architecture D1-D12, kernel K1-K12 | Referenced as written in their own files |
| Requirements and Testing designs | You said earlier sections are set. I was not told which of R1-R3 and T1-T4 were accepted, so they are carried as OPEN inputs with fallbacks. |
| Code Review design (arch-code-review.md) | Proposed. Twelve decisions (C1-C12) OPEN. |
| Reference files, scripts, SKILL.md | Not drafted |

Nothing in this session is accepted.

## B. What I took into consideration and thinking mode

1. **Same threat, third level.** Requirements guards the spec, Testing guards the suite, Code Review guards the review. The failure weighted most was false assurance: self-review, a thin review reported as complete, or findings quietly dropped. That produced the withheld-input contract, mandatory coverage accounting and the rejected-with-reason rule.
2. **Honest mechanical/judgment split.** D4 says "scripted where possible", but a review cannot be mostly scripts. I limited scripts to selection, risk order, accounting, report shape, hash binding and consuming other blocks' results. Everything about correctness stays a lens and is labeled so.
3. **One home per fact (D3).** Every overlap got a proposed owner before any rule was written: lenses stay with Security, Frontend and Testing, the diff gate and integrity diff stay with Plan & Build and Testing, and AD- rules stay with Architecture. Code Review consumes their results and does not recompute them.
4. **Source conflicts resolved by consequence, not by picking a winner.**
   - BMAD's minimum of 10 adversarial findings conflicts with Cloudflare's candidate gate, ponytail's "no concrete case, no finding" and the zero-findings rule. I did not adopt the minimum.
   - open-code-review's silent false-positive discard conflicts with K5. It becomes a `rejected` verdict with a reason.
   - Addy's "reviewer never receives the claim" conflicts with the reviewer needing the spec. I split the claim from the ACs and left the line OPEN.
   - gstack's fix-first conflicts with a read-only gate. I made read-only the default and left fix-first as an alternative.
5. **Kernel tension surfaced, not patched.** K4 requires measured evidence "where a script exists", which makes every lens check inconclusive by definition (G1). I flagged it and did not amend K4.
6. **Standalone as a test of every choice.** The conformance lens fails it, so it becomes `n/a (no spec)` with a reason. Diff mode without git fails it, so it falls back to Baseline, labeled.
7. **Hash binding.** Review validity bound to a tree hash mirrors K7's approval-bound-to-exact-action. It depends on the undefined no-git snapshot (G5), so it stays open.
8. **Labeled judgment.** The severity anchors, the ownership of AC-to-implementation, the 3-lens count and the "read-only by default" stance are my choices, with no source stating them.
9. **Hold decisions open.** Where a choice depended on an unresolved Requirements or Testing decision, I wrote the dependency and a fallback.

## C. Decisions proposed (all OPEN)

| ID | Proposal | Alternative |
|---|---|---|
| C1 | Diff per slice plus Baseline before ship; PR as a variant | Single mode; PR as a full mode |
| C2 | Reviewer receives diff, ticket scope and ACs, recon, other blocks' measured results, applicable AD- rules. Withheld: author's summary, "tests pass" claims, commit rationale, prior reviewer conclusions. | Withhold less or more |
| C3 | Three own lenses (correctness and paths, conformance, maintainability) plus loaded lenses | Four lenses |
| C4 | Re-verification scope: all confirmed, P0-P1 only, or stakes-scaled | Cloudflare's rule is every confirmed finding |
| C5 | No minimum findings; zero valid with accounting | BMAD's adversarial minimum |
| C6 | Code Review owns AC-to-implementation presence (conformance lens) | Plan & Build |
| C7 | Labeled-line Markdown report (matches Requirements); location OPEN | JSON |
| C8 | Read-only review; Build applies fixes; simplify step lives in Plan & Build | gstack fix-first; simplify inside Review |
| C9 | Fingerprint independent of line numbers; composition and computing party OPEN | Script-computed from a normalized tuple |
| C10 | Code Review asks only whether a changed behavior has a check; Testing owns test quality | Single owner |
| C11 | "Respond" mode vs rules section undecided | Separate block |
| C12 | Whether a degraded fallback can PASS or only INCOMPLETE; kernel rule for lens checks | Kernel amendment |

The gate proposal has 10 checks (arch-code-review.md section 10). Checks 1-8 and 10 are scripts or consumed results, and check 9 is a lens. The coverage threshold for skipped files is OPEN and no number is proposed.

## D. Kernel gaps exposed (none amended)

| ID | Gap |
|---|---|
| G1 | K4's "measured where a script exists" makes lens checks permanently inconclusive. A rule for lens checks is needed. |
| G2 | P0-P3 has no anchors. A draft is given in the design, marked wings judgment. |
| G3 | Findings have no disposition model. K6 waivers apply to checks only. |
| G4 | `F-` promotion to spine IDs (kernel OPEN item 2) still unresolved |
| G5 | No-git file-hash snapshot is assumed by three blocks and defined by none |

## E. Evidence tiers

| Tier | Content |
|---|---|
| Read directly in earlier chats | Cloudflare candidate gate and verdict model (carried as read); K4, K5, K6, K8; Addy skill-lint and agents.md |
| Carried, not re-checked | gstack review and plan-completion; BMAD reviewer gate and lenses; ponytail; mattpocock code-review; Addy doubt-driven and code-review-and-quality; open-code-review delegate; OWASP Secure_Code_Review; ECC click-path-audit |
| My judgment | Section B item 8 |
| Never read | BMAD bmad-code-review render; open-code-review preview and rule docs; Trail of Bits spec-to-code-compliance; superpowers receiving-code-review (not in context) |

## F. Cross-block consequences

- **Plan & Build:** must carry scope paths, seams, change type and AC IDs, define slice boundaries and the diff base, and own the fix-cycle driver and the simplify slot.
- **Architecture:** must expose AD- "Rule" lines in a checkable form and the CI layer-check result.
- **Stack & Constraints:** the git or snapshot requirement for Diff mode belongs in the stack record.
- **Ship & Operate:** needs a Baseline report whose hashes match the release tree.
- **Security, Frontend, Testing:** lens interfaces. Each lens must return K5-shaped findings with a compact summary.
- **wings-lint:** `report` and `triage` subcommands depend on R2 and T2. Together with Testing's subcommands, the 1,000-line split judgment is under pressure.

## G. Unverified, do not carry forward

- Every gstack, BMAD, mattpocock, ponytail, Addy and OWASP detail above (carried, not re-checked in this pass).
- The draft severity anchors, the 3-lens count and the reference-count blast-radius heuristic (wings judgment).
- That grep-based caller counting is accurate across stacks.
- Cloudflare's severity anchors (never seen in this pass).

## H. Files that would improve this block

1. BMAD `bmad-code-review` stub render (the real reviewer gate).
2. gstack review, review-army and plan-completion text again, if the master will quote them.
3. open-code-review `preview` and `rule` docs, for the deterministic file-selection step.
4. Trail of Bits differential-review, fp-check and spec-to-code-compliance (separate credited files if used).
5. superpowers receiving-code-review, for the respond rules.

## I. Next step

Resolve C1-C12, R1-R3, T1-T4 and the kernel gaps, or tell me which to design around as open. In dependency terms, Plan & Build and Stack & Constraints are the next candidates: Requirements, Testing and Code Review all declare interface needs on them (ticket fields, `verify.tests`, diff base, fix-cycle driver). Which block comes next is your call.