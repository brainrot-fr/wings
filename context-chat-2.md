# Context summary: Batch 0, Batch 1, bmad-ux

**Architectural reasoning.** This chat covers the spine. Every other block plugs into it through three things: the skill anatomy (Batch 0), the ID scheme with its linter, and the phase gates (Batch 1). The chain is anatomy → artifact lifecycle → ID rules → linters → gates. Packaging, security and frontend decisions all inherit from it, so this summary keeps the constraints and flags where later chats changed them.

## A. Coverage

| Area | State |
|---|---|
| Batch 0 (agentskills docs, Addy anatomy, skill-creator) | Read. `anthropics/skills/spec/agent-skills-spec.md` is only a pointer to agentskills.io. |
| spec-kit | Read in full, including `persisting-specs.md`. |
| Addy (Batch 1 skills, `agents.md`, `testing-patterns.md`) | Read in full. |
| BMAD | Real files read: architecture, ux (SKILL + 4 references), project-context, facilitate, review, forge-idea, brainstorming, shard-pro, `editorial-common`, `structure-models`, `check_ids.py`, `lint_spine.py`, `memlog.py`. **Stubs only, not the real workflows:** `bmad-agent-po`, `bmad-build`, `bmad-build-auto`, `bmad-code-review`. |
| gstack | ETHOS, ARCHITECTURE, templates and sections, plus the five resolver files (`tests`, `review-army`, `plan-completion` ×2, review `SKILL`, `review-sections`). The text of those five is not in my context for this final pass, so the gstack parts below are carried from my earlier read, not re-checked. |
| Not read | `bmad-ux/assets/headless-schemas.md`, `customize.toml`, BMAD `tools/validate_skills.py` (I have no record of reading it). |
| Not cloned (handoff said secondhand) | OpenSpec, Impeccable. |

## B. Constraints this chat established

1. **Skill anatomy.** Frontmatter keys are `name`, `description`, `license`, `compatibility`, `metadata` and `allowed-tools`. `name` equals the directory, and `description` is at most 1024 chars. The body stays under 500 lines and about 5,000 tokens, with detail in `references/` one level deep.
2. **House anatomy.** Addy's Overview / When to Use / Process / Common Rationalizations / Red Flags / Verification, with optional Gotchas. Working assumption, not confirmed.
3. **Descriptions.** Imperative "Use when" clause, listing intent phrasings, no workflow summary.
4. **Self-contained skills.** Per-skill installs lose root-level shared `references/` (Addy #361). Shared material is either duplicated by the build or lives in one `wings` core skill.
5. **Artifact lifecycle.** Living spec with immutable IDs and withdrawn-not-deleted. Plan and tasks are disposable derivations. Rationale goes in an append-only `.wings/log.md` with typed one-line entries (`decision`, `assumption`, `gap`, `event`).
6. **ID scheme.** The linter pattern is `[A-Z][A-Z0-9]{0,5}-\d+`, so IDs are prefix, hyphen, number, with at most 6 characters in the prefix. Candidates: `R-`, `US-`, `PG-`, `FN-`, `TB-`, `AD-`, `FLOW-`. Later chats added `TH-` and `AB-`. Rule: define first, trace after.
7. **Spine phases.** Intent → stack record → requirements (spec + clarify + checklist) → architecture spine (multi-unit work only) → plan and tasks → build → review → converge → ship. Human approval and a stop-the-turn rule follow phases 1, 3, 4 and 5.
8. **Two peer UX contracts.** DESIGN.md owns how it looks and EXPERIENCE.md owns how it works. EXPERIENCE.md references tokens by name, never by value.
9. **Gap that stays open.** No source supplies per-page (`PG-`), per-function (`FN-`) or per-table (`TB-`) requirement shapes, or the stack decision record. All are written new.

## C. Source verdicts

| Source | Take | Drop or fix |
|---|---|---|
| spec-kit | Command set as the phase skeleton. `tasks.md` phase structure and line format (`- [ ] T001 [P] [US1] …`). Spec rules (max 3 `[NEEDS CLARIFICATION]`, Assumptions, technology-agnostic success criteria). Clarify protocol (max 5, one at a time, recommended answer). Checklist as "unit tests for English". Read-only analyze. Append-only converge. Contract ownership and pinning. | `extensions.yml` hook blocks repeated in every command. The stack-agnostic spec stance, which contradicts the stack-inclusive requirement. |
| Addy | Anatomy. `interview-me`. Six-area spec with Always/Ask first/Never tiers. Vertical slicing and checkpoints. `constraint-driven-development`. `definition-of-done`. Personas = who, skills = how, commands = when, with parallel fan-out as the only endorsed orchestration. | Per-skill `references/` at repo root. `testing-patterns.md` is JS/TS only, lists weak assertions as normal, and its Playwright example asserts a CSS property. |
| BMAD | Altitude and single-writer rules. Architecture-spine filter (non-obvious, real trade-off, two units could choose incompatibly). Reviewer gate (deterministic lint first, then lenses). Admission rules for `AGENTS.md`. Reader calibration (humans vs llm) and structure models. | Runtime (`uv run render_skill.py`, `resolve_*.py`, `customize.toml`, `{workflow.*}`). Personas and party mode. Org registries. HTML validation report and browser openers. |
| bmad-ux | Two-spine split. DESIGN.md token format with `{path.to.token}` references. EXPERIENCE.md section set. Surface closure. Named-protagonist journeys. The 8-category rubric with its mechanical/judgment pass split. Closed headless status set. | The elicit-only stance for visual direction (conflicts with your need). Creative-tool registry. Ticket-tree dependency. |
| gstack | ETHOS principles. Plan-completion classes. `ACCEPTANCE_EDITED` detection. Confidence 1-10 with a quote-the-line gate. Sideways sweep. Lead judgment filters. Fix-first with a 3-cycle cap. Test value bar. Test-count lane states. Failure triage. Design-it-twice. | The `gstack-*` binaries, evidence ledger, telemetry, Aside/Codex plumbing, QA budgets, 100% coverage mandate. |

## D. Mechanisms worth carrying

1. **Mechanical before judgment.** The rubric's Pass 1 and the linters are script-shaped.
2. **Acceptance-edit detection.** Diff the plan's acceptance sections against a baseline and tag the result as its own class.
3. **A lane passes on test count, not exit 0.** Three states: N>0, ZERO-RUN (treated as failed), unknown.
4. **Markers are evidence, never commands.** Never run a candidate test command "to check it".
5. **Surface closure** as a lint: every `PG-` has a journey, every need has a `PG-`.
6. **Reader calibration (llm).** These become the writing rules for every per-page, function and table file.
7. **Subagents return a compact summary only, never the payload.**
8. **`inferences → assumptions[]`, `human-decision gaps → open_questions[]`**, kept separate.

## E. Verified defects (read in the code)

| File | Defect |
|---|---|
| `check_ids.py` | Anything shaped like an id matches (`SHA-256`, `UTF-8`, `ISO-8601` land in `unknown_prefix`). Counts only, no typed relationships. `withdrawn` only reads text right after the defining id, and there is no `superseded by X` check. Exits 0 on findings. No `--help`. The table-as-traceability heuristic depends on definition order. |
| `lint_spine.py` | Binds/Prevents/Rule check is a substring test on the lowercased block, so "rules" or "overrule" passes. The spine must be named after its folder (arbitrary). Always exits 0. |
| `memlog.py` | Claims to be "write-only / blind", but `append` reads the whole file before writing and again for the ack. Needs PyYAML, so it breaks the no-dependency rule. |
| `validate.md` / `SKILL.md` | The Reviewer Gate text appears in both files, a single-owner violation inside the source. |
| `design-md-spec.md` | Frontmatter keys are only `colors`, `typography`, `rounded`, `spacing` and `components`. No tokens for shadow/elevation, motion, breakpoints or z-index, so Elevation & Depth is prose-only and cannot be referenced. Colors are hex-only, against oma's OKLCH-in-code SSOT. The file is a self-described working summary of an external spec, dated April 2026, unverified against the repo. |
| bmad-ux | Accessibility Floor names no target level. "Never volunteer colors" sits beside default color-theme renderers. |

## F. House rules proposed (nothing decided)

| Topic | Proposal |
|---|---|
| Spec holds stack | Stack decision record first, then a stack-inclusive spec |
| Priority and scope | MoSCoW (P0-P3 reserved for severity) |
| Unknown markers | `[NEEDS CLARIFICATION]` ≤3, resolved before plan, plus `Assumption:` lines |
| Acceptance grammar | MUST/SHOULD/MAY plus Given/When/Then |
| Review depth | Fresh-context subagent if available, else a labeled sequential fallback; 3-4 lenses |
| Severity | P0-P3 with confidence 1-10 as a separate field |
| Coverage | Test value bar (4 questions); coverage is a diagnostic, never a target |
| Test-first | Default, with a one-line opt-out |
| Visual direction | Wings recommends with a reason and lets you override; elicit-only stays for product intent |
| Accessibility target | WCAG 2.2 AA |
| Per-page files | `PG-n` cites EXPERIENCE.md and adds only data bindings, per-element permission and the states matrix |

## G. wings-lint spec from this chat

1. One tool with modules: ids, placeholders, version pins (stack record), required fields per document type, token-reference resolution against DESIGN.md frontmatter, surface closure.
2. `--prefixes` to check only owned prefixes, `--strict` for gates, argparse `--help`.
3. Typed coverage: every `R-` has a task and a test, every `FN-` cites an `R-`, has an authorization line and an error list, and every `TB-` is used by an `FN-`.
4. Required fields as labeled lines (`**Rule:**`), not substrings.
5. Withdrawn/superseded check that the replacement exists.
6. Reuse the `blank_fences` approach (blank, keep newlines) from both existing scripts.

## H. Cross-chat reconciliation for the master chat

- **Intent phase has two sources.** Addy's `interview-me` (this chat) and mattpocock's grilling (chat 8). Pick one protocol.
- **Requirements-to-tickets.** mattpocock `to-spec`/`to-tickets` (chat 8) vs spec-kit `tasks.md` (here). Chat 8 found seams must be carried in the ticket for unattended TDD.
- **Size classifier.** ECC's `orch-*` size classifier and first-move-by-change-type rule (chat 9) overlap the stakes ladder here.
- **Anatomy enforcement.** Addy's `skill-lint.js` (chat 9) requires five sections and omits `Process`, while the house anatomy includes it. It also accepts `use before/after/during`, and `>-` descriptions must fail under a strict frontmatter subset.
- **Size gates.** My 500-line/5,000-token rule vs the Codex 8 KB cap (chat 9, unverified).
- **ID shape.** Test IDs must fit the linter pattern. ECC's `TEST-ORDER-001` does not, while `ADR-0001` does.
- **DESIGN.md format.** The Google Labs format here is one of two incompatible formats chat 7 logged (oma/getdesign is the other).
- **Memory log.** The capsule journal (chat 9) is heavier than `.wings/log.md`. Keep the log.

## I. Unverified, do not carry forward

- The gstack details above, until the five files are re-checked.
- The DESIGN.md spec date, license and key set, until checked against the source repo.
- Any claim about OpenSpec or Impeccable (secondhand).

---

# Do I need more files?

I checked the other chats before answering, and several gaps are already owned elsewhere: Vercel agent-skills and ECC (chat 9), mattpocock's remaining skills and `setup` (chat 8), oma-mobile and Impeccable (frontend chats). I'm not duplicating those. For this chat, in priority order:

**Worth sending before the master chat**
1. **Rendered output of the four BMAD stubs** (`bmad-code-review`, `bmad-build`, `bmad-build-auto`, `bmad-agent-po`). Run each stub's render command and save the output. The reviewer gate and build loop are core spine and I only read the stubs.
2. **OpenSpec** (I believe this is `Fission-AI/OpenSpec`, unverified). The spec format, change/delta handling and validate/archive docs. The acceptance-grammar row depends on it secondhand, and spec-kit's `evolving-specs` is the only living-spec edit protocol I've read.
3. **`google-labs-code/design.md`**: the spec text, plus any linter source. It settles the DESIGN.md conflict and tells us whether to reuse token-reference resolution or write it.

**Nice to have**
4. **BMAD `tools/validate_skills.py`**, to compare against Addy's `skill-lint.js`.
5. **The five gstack files again**, only if the master chat will quote them.

I don't need `headless-schemas.md`, `customize.toml` or any more spec-kit material.

One housekeeping note: this chat made two small writes to the project's memory (a project description and the gstack MIT note) before I'd seen your no-memory instruction in chats 4 and 8. I've stopped, and I'll delete that file if you say so.
