# arch-requirements.md (block 3)

## Architectural reasoning

Requirements is the first consumer of the kernel. It defines `R-`, `US-`, `AC-` and `FLOW-`, and every later block cites them. Three constraints shape it:

1. **It sits between three neighbours with overlapping claims.** Intent hands it a confirmed statement. Stack & Constraints owns the numbers. Experience Design and Backend consume its IDs. Most of the design below draws those ownership lines so each fact has one home (D3).
2. **It must work standalone.** It has to audit a PRD or recover a spec from code with no `.wings/` present. The mechanical checks therefore need to travel with the skill.
3. **Its biggest failure mode is the agent weakening the spec to match the code.** That drives the change-mode design.

Dependency order for the sections: boundaries → artifacts and shapes → trace graph → modes → gate → skill layout → QA.

## 1. Boundaries (D3 resolutions)

| Fact | Home | Requirements' role |
|---|---|---|
| Who, why, stakes level, size class | Intent (`.wings/intent.md`) | Read it. Never re-ask who or why. |
| Stack, versions, NFR target values (LCP, budgets, availability) | Stack & Constraints (`manifest.md`) | An `R-` of category NFR cites the constraint by reference and never copies the number. |
| Six-area spec (commands, structure, code style, boundaries) | Stack record, project rules, kernel K7 | Not owned. The spec is stack-inclusive by reference. |
| `FLOW-` definition (need-level journey: named protagonist, goal, climax beat) | Requirements | Experience elaborates it into EXPERIENCE.md Key Flows and cites the `FLOW-` ID. |
| `PG-` | Experience | Requirements only checks that Must stories reach a flow. |
| `ADR-` format and index | Requirements | Stack and Architecture author entries. `AD-` stays with Architecture. |
| Success criteria wording | Requirements | User-observable and technology-agnostic. This reconciles spec-kit's rule with the stack-inclusive spec: stack decisions live in the stack record, outcomes stay technology-neutral. |

## 2. Artifacts and layout

```
.wings/spec/spec.md        living spec (split to spec/<area>.md past ~40 R-: wings judgment)
.wings/spec/glossary.md    canonical terms + Avoid: synonyms
.wings/spec/adr/ADR-0001-<slug>.md
.wings/log.md              kernel K10; assumption, gap, approval, waiver entries
```

**Spec section order.** Scope (from intent) → Glossary link → Actors → Stories → Requirements → Acceptance → Flows → Out of scope → Assumptions → Traceability.

Traceability is script-generated and comes last, which follows the define-before-trace rule.

**Shapes** (labeled lines, so the linter reads fields, not substrings):

- **`## US-3 <title>`**
  - Fields: Actor; Want; So-that; Scope: Must / Should / Could / Won't (MoSCoW lives here only); Flow: `FLOW-n` or `n/a (reason)`.
- **`## R-12 <title>`**
  - Fields: Statement; Source; Area; Status.
  - The Statement uses MUST / SHOULD / MAY, and each requirement has one verifiable claim.
  - Source is `US-n`, `intent`, or `inferred` / `confirmed` (recover mode).
  - Area is a slug from the spec's own area list. This adds no new ID prefix.
  - Status is `active`, `withdrawn`, or `superseded by R-n` (the target must exist).
  - NFR variant: Constraint ref + Measure method.
- **`## AC-20 <title>`**
  - Fields: Cites `R-12`; Given / When / Then (observable outcome only); Verify-by: `test` / `script` / `manual (reason)`.
  - AC does not name the required check. Plan & Build binds that in the ticket, and Testing puts the AC ID in the test name.

MoSCoW on `US-` and MUST/SHOULD/MAY on `R-` do not duplicate each other. One is release scope, the other is obligation strength. The lint flags an active Must story whose R- uses only MAY.

## 3. Typed trace graph (edges Requirements owns)

| Edge | Rule | Violation |
|---|---|---|
| `R-` → source | Source present and resolves | P1 |
| `R-` → `AC-` | Every active R- has at least one AC; NFR ACs carry a measure | P1 |
| `AC-` → `R-` | Cites an active R- | P1 |
| `US-` Must → `FLOW-` | Flow or reasoned `n/a` | P2 |
| Withdrawn or superseded target | No active item cites a withdrawn ID; superseded target exists | P1 |
| Glossary `Avoid:` terms | Not used in the spec | P3 |
| Downstream edges | Declared by the owning blocks (FN→R, PG→FLOW, AC→test) | n/a |

All edge rules live in the single lint. `--prefixes` limits a run to the prefixes a skill owns.

## 4. Modes (one skill, depth in `references/`)

| Mode | Input | Flow | Output |
|---|---|---|---|
| **Greenfield** | intent.md, stack record | Capability areas → clarify rounds → draft → quality checklist → lint → sign-off | spec, glossary, ADRs |
| **Audit** (standalone-capable) | Any spec, PRD or ticket text | Pass 1 scripted (ID integrity, AC shape, placeholders, weak-word scan, unmeasured NFRs). Pass 2 lenses (testability, altitude/bloat, contradiction, completeness). | K5-shape findings with local `F-` IDs. Never edits the document. |
| **Recover** (brownfield) | Code | Recon surface inventory → candidate R- / AC- each cited `file:line` → user confirms | Spec with every item `inferred` until the user confirms. Nothing invented. |
| **Change** | Edit request | Impact walk over the trace graph → edit in place → supersede or withdraw → `ACCEPTANCE_EDITED` check → approval | Updated spec, log entries |

**Clarify protocol** (spec-kit + Addy): one question at a time, recommended answer attached, answers written into the spec immediately, 5 questions max per round, and no more than 3 `[NEEDS CLARIFICATION]` markers open at once. The cycle cap is 3 rounds. After that it stops and reports (K6), and does not proceed on guesses. Defaults taken are logged as `assumption` entries.

**Change-mode guard.** The baseline is the commit recorded in the last `approval` entry (a file hash snapshot if there is no git).

- The script diffs AC blocks against it. Any AC whose text changed, or that was withdrawn, while its R- is unchanged is tagged `ACCEPTANCE_EDITED`.
- That class is never folded into ordinary changes. It needs a human `approval` entry bound to the exact diff hash (K7). Silence or timeout is not approval.
- Recover and change modes cannot close with an unapproved `ACCEPTANCE_EDITED` or any `inferred` item.

## 5. Requirements gate

| # | Check | Evidence |
|---|---|---|
| 1 | ID lint clean (owned prefixes) | script |
| 2 | Every active R- has an AC; AC shape valid | script |
| 3 | NFR has constraint ref, number and unit, and method | script |
| 4 | No open `[NEEDS CLARIFICATION]`; assumptions logged | script |
| 5 | No unapproved `ACCEPTANCE_EDITED`; no `inferred` items | script |
| 6 | Weak-word and placeholder scan | script (P3, never blocks alone) |
| 7 | Testability, altitude, contradiction, completeness lenses | lens, fresh-context reviewer if available, else labeled sequential fallback |
| 8 | Human sign-off entry bound to the spec hash | attested by human |

Checklist items are "unit tests for English" (spec-kit), and the generator never ticks its own boxes. An unrun check yields INCOMPLETE (K4).

**Stakes scaling.** The stakes level from Intent scales only the judgment layer: question volume, lens count, and whether a fresh-context reviewer is mandatory. Checks 1–5 never scale down. This answers kernel OPEN item 3 for this block, and I recommend stating it once in kernel-lite (one line).

## 6. Skill layout and anatomy

```
requirements/
  SKILL.md                   mode router + anatomy sections
  scripts/wings-lint.py      build-inlined copy, hash-drift checked
  references/modes/{greenfield,audit,recover,change}.md
  references/{shapes,clarify,quality-checklist,lenses,glossary-and-adr}.md
```

**Common Rationalizations** the skill must close:

| Rationalization | Rebuttal |
|---|---|
| "It's obvious, skip the AC" | An R- without an AC is untestable, so the gate fails. |
| "NFRs later" | An NFR without a number cannot pass. |
| "User said fast, that's enough" | Weak-word scan plus a required measure. |
| "Code does X, so X is intended" | `inferred` until the user confirms. |
| "Adjust the AC to match the code" | `ACCEPTANCE_EDITED` needs human approval. |
| "Too small for a spec" | The stakes ladder shrinks the spec, not the gate. |

**Writing rules** for all artifacts come from BMAD's llm-reader calibration: define before use, consistent terms, no hedging, tables over prose, no unclear antecedents, cite standards instead of re-teaching them.

## 7. QA (eval, with and without the skill)

1. **Greenfield:** vague two-line intent. Expect at most 5 questions per round, each with a recommended answer, and a spec where every R- has an AC.
2. **Audit:** seeded bad spec (planted defects: "fast", a missing AC, a contradiction, a duplicate ID). Expect all planted defects found and zero invented.
3. **Recover:** a small real repo (AcadFlow is the candidate fixture). Expect every item `inferred` with `file:line`, and no behavior without a code cite.
4. **Change:** weaken one AC. Expect `ACCEPTANCE_EDITED` and a blocked close.

## 8. Cross-block consequence for the kernel

**Gap exposed:** D1 says any sibling works standalone, but K1 keeps the lint only in `wings`. A standalone Requirements, Testing or Code Review could not run its scripted checks. Proposed fix: `wings-lint.py` is a single-file build-inlined script, copied into each sibling that runs gates, with the same hash-drift check as kernel-lite (K11). Siblings with no gates do not carry it.

## 9. Decisions needed

1. Accept the boundary table in §1. The two non-obvious calls: `FLOW-` is defined here, and NFR values stay in Stack.
2. Accept the lint-as-inlined-script fix in §8, or tell me to keep it router-only and accept that standalone siblings run those checks procedurally and labeled degraded.
3. Accept the stakes-scaling rule in §5 (judgment layer only, never the mechanical checks).

## Not carried, or still thin

- **OpenSpec** was never read. The Given/When/Then and change-handling claims rest on spec-kit and Addy, and OpenSpec is secondhand. Sending it would sharpen change mode most.
- **ADR conditions and glossary format** are carried from my read of mattpocock's `domain-modeling` (not re-checked). I take the exact wording from the files when I write the references, not from memory.
- **Spec-kit's ambiguity categories** are likewise taken from `clarify.md` at write time.

Next block in design order is **Testing**, which consumes `AC-` IDs and the Verify-by field defined here.