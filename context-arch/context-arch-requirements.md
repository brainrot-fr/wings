# context-requirements-arch.md: Requirements block (3), first pass, master chat handoff

Architectural reasoning: Requirements is the first block that consumes the kernel (K3 IDs, K4 vocabularies, K6 gates, K10 log), and every later block cites its IDs (`R-`, `US-`, `AC-`, `FLOW-`). The design therefore went in this order: ownership boundaries, then artifact shapes, then the typed trace graph, then modes, then the gate, then skill layout and QA. Boundaries came first because Requirements sits between three blocks with overlapping claims (Intent, Stack & Constraints, Experience Design), and an unclear boundary would break D3 (one home per fact) before any shape was written.

Memory: nothing is saved, per the standing instruction. No memory tools were used.

## A. Status

| Item | State |
|---|---|
| Wings architecture (D1-D12) and kernel (K1-K12) | Accepted earlier. This session builds on them without re-litigating. |
| Requirements design (`arch-requirements.md`) | **Proposed, not accepted.** Three decisions are pending (section D). |
| Written reference files, scripts, `SKILL.md` | None drafted. This is contract-level design only. |

## B. How I approached it (thinking mode)

1. **Hold decisions, fill gaps.** You said earlier you would give decisions only after the context was complete. I treated the kernel and wings arch as fixed inputs and designed Requirements as a consumer of them. Where the design exposed a kernel gap, I flagged it and did not silently amend the kernel.
2. **One home per fact (D3) as the primary filter.** Every overlap with a neighbour got a table row naming the owner. The non-obvious calls were `FLOW-` (defined in Requirements, elaborated in Experience) and NFR values (owned by Stack, only referenced from `R-`).
3. **Mechanical before judgment.** Every check that can be a script is one (checks 1-6 of the gate). Lenses are reserved for testability, altitude, contradiction and completeness, which need judgment.
4. **Threat model: the agent weakens the spec to match the code.** This was the failure mode I weighted most. It drove the `ACCEPTANCE_EDITED` class, the human `approval` bound to the diff hash, and the rule that recover and change modes cannot close with `inferred` items or an unapproved edit.
5. **Reconcile contradictions between sources instead of picking a winner.** The main one: spec-kit wants technology-agnostic success criteria, while you want a stack-inclusive spec. My resolution is that stack decisions live in the stack record and success criteria stay outcome-level.
6. **Standalone constraint as a test of every design choice.** I asked of each check whether it works with no `.wings/`. That is how the lint-inlining gap in section C surfaced.
7. **Honesty about evidence.** I labeled what was carried from earlier reads, what was my own judgment, and what was never read (section E).

## C. Decisions proposed

**Boundaries**

| Fact | Home |
|---|---|
| Who, why, stakes, size class | Intent (`.wings/intent.md`). Requirements never re-asks. |
| Stack, versions, NFR target values | Stack & Constraints. An NFR `R-` cites the constraint and never copies the number. |
| `FLOW-` (need-level journey: named protagonist, goal, climax beat) | Requirements. Experience elaborates it in EXPERIENCE.md. |
| `PG-` | Experience. Requirements only checks that Must stories reach a flow. |
| `ADR-` format and index | Requirements. `AD-` stays with Architecture. |
| Success-criteria wording | Requirements: user-observable and technology-agnostic. |

**Layout**

```
.wings/spec/spec.md          living spec (split to spec/<area>.md past ~40 R-)
.wings/spec/glossary.md      canonical terms + Avoid: synonyms
.wings/spec/adr/ADR-0001-<slug>.md
.wings/log.md                kernel K10
```

Spec section order: Scope, Glossary link, Actors, Stories, Requirements, Acceptance, Flows, Out of scope, Assumptions, Traceability. Traceability is script-generated and last (define before trace).

**Shapes** (labeled lines, so the linter reads fields):
- `US-n`: Actor, Want, So-that, Scope (MoSCoW lives only here), Flow.
- `R-n`: Statement (MUST/SHOULD/MAY, one verifiable claim), Source (`US-n` / `intent` / `inferred` / `confirmed`), Area (slug, no new prefix), Status (`active` / `withdrawn` / `superseded by R-n`). The NFR variant adds Constraint ref and Measure method.
- `AC-n`: Cites `R-n`, Given/When/Then (observable outcome only), Verify-by (`test` / `script` / `manual (reason)`). The AC does not name the check. Plan & Build binds that in the ticket, and Testing puts the AC ID in the test name.

MoSCoW (release scope) and MUST/SHOULD/MAY (obligation strength) are separate axes. The lint flags an active Must story whose `R-` uses only MAY.

**Trace graph edges owned here**

| Edge | Violation severity |
|---|---|
| `R-` source present and resolves | P1 |
| Every active `R-` has at least one `AC-` (NFR ACs carry a measure) | P1 |
| `AC-` cites an active `R-` | P1 |
| Must `US-` has a `FLOW-` or a reasoned `n/a` | P2 |
| No active item cites a withdrawn ID; superseded target exists | P1 |
| Glossary `Avoid:` terms unused in the spec | P3 |

Downstream edges (FN to R, PG to FLOW, AC to test) are declared by the owning blocks.

**Modes** (one skill, depth in `references/modes/`)

| Mode | Core rule |
|---|---|
| Greenfield | Capability areas, clarify, draft, checklist, lint, sign-off |
| Audit (standalone-capable) | Pass 1 scripted, pass 2 lenses. Emits K5 findings with local `F-` IDs and never edits the document. |
| Recover (brownfield) | Every item `inferred` with a `file:line` cite until the user confirms. Nothing invented. |
| Change | Impact walk over the trace graph, edit in place, supersede or withdraw, `ACCEPTANCE_EDITED` check, human approval |

Clarify protocol: one question at a time, a recommended answer attached, answers written into the spec immediately, at most 5 questions per round, at most 3 open `[NEEDS CLARIFICATION]` markers. After 3 rounds it stops and reports (K6) and does not proceed on guesses. Defaults taken are logged as `assumption` entries.

Change-mode guard: the baseline is the commit in the last `approval` entry (a file-hash snapshot if there is no git). An AC whose text changed or was withdrawn while its `R-` is unchanged is tagged `ACCEPTANCE_EDITED`, which needs a human `approval` bound to the exact diff hash. Silence is never approval.

**Requirements gate** (8 checks):
1. ID lint clean (owned prefixes).
2. Every active `R-` has an AC and the AC shape is valid.
3. NFR has constraint ref, number, unit and method.
4. No open `[NEEDS CLARIFICATION]`; assumptions logged.
5. No unapproved `ACCEPTANCE_EDITED`; no `inferred` items.
6. Weak-word and placeholder scan (P3, never blocks alone).
7. Testability, altitude, contradiction and completeness lenses (fresh-context reviewer, else labeled sequential fallback).
8. Human sign-off bound to the spec hash.

Checks 1-6 are scripts. Check 7 is a lens. Check 8 is attested by the human. An unrun check yields INCOMPLETE (K4).

**Stakes scaling:** the stakes level scales only the judgment layer (question volume, lens count, whether a fresh-context reviewer is mandatory). Checks 1-5 never scale down. I recommend stating this once in kernel-lite, which would close kernel OPEN item 3.

**Skill layout:** `requirements/SKILL.md` (mode router plus anatomy), `scripts/wings-lint.py` (build-inlined copy), `references/modes/{greenfield,audit,recover,change}.md`, and `references/{shapes,clarify,quality-checklist,lenses,glossary-and-adr}.md`. Six Common Rationalizations are closed with rebuttals (obvious so skip the AC, NFRs later, user said fast, code does X so X is intended, adjust the AC to the code, too small for a spec).

**QA (with and without the skill):** greenfield from a vague 2-line intent; audit on a seeded bad spec (expect all planted defects found, none invented); recover on a small real repo (AcadFlow is the candidate fixture); change by weakening one AC (expect `ACCEPTANCE_EDITED` and a blocked close).

**Kernel gap exposed (needs your call):** D1 says any sibling works standalone, but K1 keeps the lint only in `wings`, so a standalone Requirements, Testing or Code Review could not run its scripted checks. Proposed fix: `wings-lint.py` is a single-file build-inlined script copied into each sibling that runs gates, with the K11 hash-drift check. This amends K1 and K11.

## D. Decisions pending

1. Accept the boundary table (the two non-obvious calls: `FLOW-` here, NFR values in Stack).
2. Accept lint-as-inlined-script, or keep it router-only and accept that standalone siblings run those checks procedurally, labeled degraded.
3. Accept stakes scaling on the judgment layer only, and add one line to kernel-lite.

## E. Evidence tiers and unverified items

| Tier | Content |
|---|---|
| Carried from earlier chats, not re-checked | spec-kit rules (3 markers, 5 questions, one at a time, checklist as unit tests for English); Addy interview-me and spec areas; BMAD llm-reader calibration; gstack `ACCEPTANCE_EDITED`; mattpocock ADR and glossary formats |
| My own judgment, labeled as such | ~40 `R-` split threshold; 3-round clarify cap; the P1/P2/P3 assignments for trace violations; area slug instead of a new prefix; the weak-word scan existing at all |
| Never read | OpenSpec. The Given/When/Then and change-handling claims rest on spec-kit and Addy, so OpenSpec is secondhand. |

Not yet defined in this pass:
- the weak-word list;
- the exact lint output schema for Requirements findings;
- how the file-hash snapshot works without git;
- the stack-record fields the NFR constraint ref points to.

Exact wording for ADR conditions, glossary format and clarify's ambiguity categories gets taken from the source files at write time, not from memory.

## F. Cross-block consequences

- **Testing** consumes `AC-` IDs and the Verify-by field. It is the next block in design order.
- **Plan & Build** binds required checks and seams to ACs in the ticket. Requirements deliberately does not.
- **Experience Design** cites `FLOW-` IDs and owns surface closure from `PG-` back to them.
- **Stack & Constraints** must expose NFR constraints as referenceable entries, which constrains its stack-record design.
- **Intent** must emit `.wings/intent.md` with stakes level and size class. This block depends on that file's shape.

## G. Files that would improve this block

1. OpenSpec (spec format, change and delta handling, validate and archive docs), which sharpens change mode most.
2. BMAD `bmad-code-review` and `bmad-build` stub renders, for the review-gate comparison.
3. Trail of Bits `spec-to-code-compliance` (BY-SA, separate files if used), the closest source to the AC-to-check lint.

## H. Next step

Settle the three pending decisions, then design **Testing**, which consumes `AC-` and Verify-by. Draft the Requirements reference files alongside it, since Testing is the first downstream consumer of the shapes defined here.