# Context-chat-9: Packaging, ECC, Vercel/taste/oma-mobile dossier, and the remaining files

This is the end-of-chat handoff for the master design chat. Nothing was saved to memory, as you instructed. I'm marking what I verified by reading and what I'm carrying forward on someone else's word.

## A. Scope and coverage

| Area | State |
|---|---|
| Batch 5 packaging (superpowers, wshobson, openai/skills, Addy packaging) | Read in full from the send. Gaps below. |
| ECC, 38 skills | All in context. Earlier I said 40; the tree has 38. |
| Copilot dossier: 17 cards, Phase 0 flags and deps, Phase 2, Phase 3, Phase 4 | Read. The Phase 0 flag CSVs and deps report were read from disk. |
| Last-pass files: `skill-lint.js`, its test, `validate_generated.py`, `canonical.js`, `envelope.js`, `capsule.js`, `eval-harness.js`, `gateguard-fact-force.js`, `gateguard-heredoc.js` | Read. `capsule.js` and the GateGuard hook were skimmed, not line-audited (details in §H). |
| Still missing | `tools/generate.py` (absent in the workspace) and the other wshobson adapters. The remaining GateGuard helper libs (`gateguard-target-class`, `-turn-scan`, `-change-profile`, `-search-evidence`, `-readonly-shell`). `validate-skill-host-compat.js` is covered only by Copilot's description, not by my reading. |

## B. What this chat established, as design constraints

1. **Packaging is a thin layer over one skills directory.** `.agents/skills/` is the most widely discovered path across the sources (Codex, Copilot, Gemini, OpenCode, Command Code). `.claude/skills` is read by Claude Code, Cursor, OpenCode and Copilot. I found no source showing Claude Code reads `.agents/skills`, so verify that.
2. **Commands are the non-portable part.** Addy keeps three parallel command trees and a parity script. Copilot ignores `.claude/commands`. Antigravity validates the TOML wrappers but does not expose them (agent-skills #445). Skills are the portable surface.
3. **Naming is a three-way problem.**
   - Claude Code namespaces as `plugin:skill`.
   - wshobson's adapters emit `<plugin>__<skill>` or `<plugin>-<skill>`, capped at 64 characters for OpenCode and Pi.
   - Bare-name installers (`gh skill`, `npx skills`) collide: Addy and superpowers both ship `test-driven-development`.
4. **Wings' own build tooling has different constraints from shipped scripts.** Shipped: stdlib-only, no CLI. Build-time: QA harness, rule distillation, stocktake can use more. Several strong sources are build-time only.
5. **The shape decision is still open.** One router skill with references, or a suite with a router. Evidence: Codex's 8 KB cap (below) pushes detail into references. superpowers and Addy both use a meta-skill router.

## C. Source verdicts

### Packaging sources

| Source | Take | Drop or fix |
|---|---|---|
| superpowers | Action-vocabulary skills with one per-harness tool-mapping reference. Version-drift check across manifests. `writing-skills`: match the form to the failure (prohibition + rationalization table for discipline failures; positive recipe for wrong shape; REQUIRED slot for omissions; conditional on an observable predicate), "no nuance clauses", "exemption clauses don't scope", micro-tests with a no-guidance control and 5+ reps. Subagents must not receive the controller bootstrap. | Per-harness JS/TS plugin runtimes. A hook that silently exits 0 when no bash is found. `escape_for_json` escapes only five characters. `bump-version.sh` interpolates the version into a jq program behind a prefix-only regex. `anthropic-best-practices.md` is a verbatim copy of Anthropic docs under MIT; check that. |
| wshobson | Capability matrix as data. `validate_generated.py`: validate generated artifacts against documented schemas, every finding carrying a `fix:` line. Version-bump check. Name-collision check. "Actions not tools". | Python/uv toolchain. Model-ID tables and harness versions (docs say "last verified July 2026"; stale by four months). Hand-rolled `parse_frontmatter` that keeps single quotes on scalars. Prose counts that disagree. Unpinned external `git-subdir` entries (`pensyve` unpinned, `deja-vu` SHA-pinned). |
| plugin-eval | Deterministic finding codes only: `MISSING_TRIGGER`, `EMPTY_DESCRIPTION`, `BLOATED_SKILL`, `ORPHAN_REFERENCE`, `DEAD_CROSS_REF`. | The composite score and badges. Heuristics reward "proactively/automatically", 200–600-line files and multi-language blocks, and penalize MUST/NEVER density and "orchestrate/dispatch". Blend weights differ across three files. `ORPHAN_REFERENCE` only matches markdown links, and `authoring.md` tells authors to use backticked paths to avoid it. `eval.md`/`compare.md`/`certify.md` put `{argument}` unquoted in bash. |
| openai/skills | Installer path safety (separator-aware zip containment). `plugin-json-spec.md` as the Codex manifest reference. `agents/openai.yaml` shape. | README says the repo is deprecated. `quick_validate.py` never checks `name` against the directory, and its allowed keys omit `compatibility`. Installer defaults to mutable `main`, no integrity pin. `create_basic_plugin.py` writes `[TODO: …]` into JSON values with no publish-time check. PyYAML dependency. |
| Addy packaging | `/build auto`: spec required, clean-tree baseline, one approval gate, stop on high-risk or irreversible tasks, per-task commits staging only touched files. `validate-commands.js` parity. Setup docs as the harness-facts source. | `simplify-ignore.sh` and `sdd-cache` hooks. The `/planning` rename. Claude-manifest `experimental` key and `commands: ["./commands"]` (TOML dir), both unverified. |

### Addy's `skill-lint.js` and its tests (new this pass)

This is the closest thing to wings-lint's skill-level core, and it's stdlib-only.

- **Take:**
  - It splits a pure content linter (no filesystem) from filesystem wrappers.
  - Fenced-code stripping follows CommonMark: tilde fences, 1–3-space indentation, longer closers, an unterminated fence swallows the rest. Stripped lines become blanks so line numbers stay stable.
  - Exemptions live in the linter, not in skill frontmatter, so a skill cannot exempt itself. A skill claiming its own exemption fails loudly.
  - Negated triggers ("do not use when") don't count, and every negated clause is stripped before checking for a positive trigger.
  - A "workflow declares Step N but no matching process section" check.
  - A `frontmatterYamlErrors` pass catching shapes a strict YAML parser rejects but a split-on-colon parser accepts: unquoted `: `, tab indentation, unterminated quotes, values starting with `` ` @ % * , ``, `|x`/`>x`, and `- `/`? `/`& `. Its rationale is concrete: Cursor parsed frontmatter as YAML and a failure failed the whole request (#494).
  - Spec-key allowlist: `name, description, license, compatibility, metadata, allowed-tools`.
  - Persona lint: `Composition` section required and last.
- **Gaps against wings decisions:**
  - Required headings are Overview, When to Use, Common Rationalizations, Red Flags, Verification. **`Process` is not required.**
  - It accepts `use before/after/during` as well as `use when`.
  - 500 lines is a warning, not an error.
  - Duplicate keys are not reported, because YAML accepts them.
  - The author states it is not a YAML implementation and assumes no block scalars. Wings' frontmatter subset should say so explicitly, and `>-` descriptions (which ECC uses) must fail.

### `validate_generated.py` (new this pass)

- Findings are `error|warning|info` with a path and a `fix:` line. Per-harness validators for codex, cursor, opencode, antigravity, pi and copilot.
- Codex check: file size over 8 KB is an **error** because "Codex hard-truncates anything past the cap, silently breaking the skill". It counts the whole file in bytes, frontmatter included. This is the only enforcement evidence I found for the cap, and it is the repo's own claim, not Codex documentation. Verify, and build every SKILL.md ≤ 8 KB regardless.
- Name cap 64 for OpenCode and Pi, description cap 1024 for Pi.
- It parses frontmatter with the hand-rolled parser, so YAML a host rejects can pass.

### ECC (38 skills)

| Cluster | Verdict |
|---|---|
| `orch-pipeline`, `orch-add/change/fix-defect`, `orch-build-mvp` | **TAKE-MECHANISM.** The size classifier (highest tier any signal reaches; security triggers floor at "standard") and the first-move-by-change-type rule: add → new failing tests; change → update existing tests first; fix → reproduce as a failing regression test; refactor → stay green. Drop the ECC agent/command names, the ≥80% coverage mandate, and `/gan-build` constants. |
| `docs-governance` + `audit-docs.py`, `living-docs-governance`, `context-and-decisions`, `architecture-decision-records`, `test-collaboration`, `contract-first` | **TAKE-MECHANISM.** Role registry (constitution, map, status, history, context, contract, tests, ADR) with one owner per fact. `audit-docs.py` is a model: stdlib, read-only, exit 0/1/2, mechanical failures vs review warnings, `repr()` for untrusted names. |
| `agent-security-hardening` | **TAKE.** Five-step workflow with a "complete when" test each. Unknown bounds are decisions, not guesses. Containment via `is_relative_to`. Directly relevant to wings as its own attack surface. |
| `mcp-dependency-review` | **TAKE-MECHANISM.** Static selector classification: exact pin SAFE; bare/tag HIGH; range MEDIUM; unclear REVIEW; Docker digest; Python. Never executes. SAFE covers only the direct selector. |
| `click-path-audit` | **TAKE as a review lens.** State-store side-effect map, then per-handler tracing for sequential undo, async race, dead path, effect interference. |
| `skill-comply`, `rules-distill`, `skill-stocktake`, `skill-host-compat`, `eval-harness` | **Build-time tools.** See §D and §G. |
| `verification-loop`, `browser-qa`, `delivery-gate`, `gateguard`, `safety-guard`, `operator-approval-loop` | **TAKE-IDEAS.** See §D and §E. |
| `accessibility`, `frontend-a11y`, `frontend-design-direction`, `make-interfaces-feel-better`, `react-performance`, `react-testing`, `e2e-testing`, `motion-foundations`, `design-system` | Rules and ideas only; defects in §F. `react-performance` is a condensed copy of the Vercel rules, so use the upstream. `context-and-decisions` derives from mattpocock `domain-modeling`; use the upstream. |
| `security-review`, `security-scan` | Sample only; wings' security sources are better. |
| `recursive-decision-ledger` | **SKIP.** |

### Copilot dossier (Vercel, taste, oma-mobile, `_shared/core`)

| Source | Take | Drop or fix |
|---|---|---|
| vercel-optimize | The claim pipeline: typed claims → `verified/failed/unsupported/unverifiable` → deterministic sanitizers → re-extract and re-verify → weighted grade → withhold below threshold. Hard exclusions before candidate selection. Candidate budget. `observation-safety`'s holdback with `needsEvidence: true`. | Collection needs Vercel CLI, auth and network. Doc says 12 sanitizers and an average; code has 11 and a weighted score. Weights (0.35/0.30/0.20/0.15) and the 0.55 cutoff are unsourced. |
| taste-skill `gate.mjs` | Waiver rules, finite verdicts, not-checked can never be PASS, hook mode that cannot trap an agent. | Needs `assets/` and Chrome. `checker-gaming` is a false positive for apps with bot protection. |
| taste-skill `perf.mjs` | Median-of-3, WARN/FAIL structure. | All thresholds are house budgets. CLS 0.1/0.25 matches published Core Web Vitals; Copilot found no citation in the file. |
| taste-skill `consistency.mjs` | 98 ordered check IDs plus 43 module IDs, and a stated threshold inventory (Phase 4 §3). | **Verified reporting defect:** the 43 module IDs are absent from the 98-item `ORDER`, and final per-check status iterates only `ORDER`. Module results reach findings and aggregate counts but not `report.checks`, which contradicts its own "every check" table. `Fetch.enable` errors are swallowed and the form pass proceeds, so "every request held" can silently fail. `--quick` is documented as skipping the hidden-content pass but only skips part of it. Loop-cycle summary says 2.5–4 s while code uses `<2.45` / `>4.05`. Browser-bound (Node 22+, Chrome), not stdlib-only. |
| web-design-guidelines, writing-guidelines | Terse `file:line` findings. Both repos are MIT (Vercel Labs). | Both fetch mutable `main` rule text at runtime. Vendor and pin. |
| composition-patterns, react-native-skills, react-best-practices | Atomic rule format (`title, impact, impactDescription, tags`), `_sections.md`, `_template.md`. | Impact levels contradict across files; numeric impact claims unsourced. |
| oma-mobile variants | `stack.schema.json` fields as a seed for the stack decision record (§G). | Additional properties allowed, so typos pass. |
| `_shared/core` | Keep `anti-ai-prose`, `execution-policy`, `quality-principles`. Merge `common-checklist`, `clarification-protocol`, `difficulty-guide`, `prompt-structure`, `lessons-learned`, `test-approach`. | Drop `code-intelligence`, `session-metrics`, `skill-routing`, `stack-verify.schema.json`, `vendor-detection`. |
| open-code-review-delegate | Deterministic preprocessing, plus mandatory `total_files / reviewed_files / skipped_files / coverage_rate`. | Needs the `ocr` CLI. Main `open-code-review` skill is sample only. |
| modern-web-guidance | Query discipline only. | `npx -y …@latest` at every use. **SKIP.** |

## D. Mechanisms worth carrying (with source)

1. **Incomplete checks cannot pass.** Seven vocabularies express one rule (table in §G).
2. **Mechanical before judgment.** ECC `ai-regression-testing`, `browser-qa`, `delivery-gate`, `rules-distill`, Vercel verify-before-grade, taste hard FAILs, and `audit-docs.py`.
3. **Narrow waivers.** Exact check + target + reason ≥12 chars, ≤5, never on safety checks (taste `gate.mjs`).
4. **Typed claim verification.** `extract-claims → verify-claim → sanitize → re-verify → grade` (Vercel).
5. **Approval bound to the exact action.** ECC `operator-approval-loop`'s draft hash plus epoch, so a stale approval cannot release rewritten text. Unknown outcomes never auto-retry.
6. **Loop guard on stop-time hooks.** ECC `delivery-gate` exits early on `stop_hook_active`.
7. **Fact-forcing instead of confirmation.** GateGuard asks for importers, public API and data schemas rather than "are you sure?". Target classes pick the questions. Sensitive targets (auth, secrets, payments, migrations, workflows) get no credits, sibling collapse or denial cap.
8. **Honest labels for advisory vs enforced.** ECC `safety-guard`.
9. **Capsule journal as a design reference.** Append-only NDJSON, `parent_hash` chain, canonical JSON, five lineages, effect classes SE0–SE4, allowlisted typed payload, secret-canary refusal. See §H for what it does and doesn't claim.
10. **Findings that carry their fix.** `validate_generated.py`'s `fix:` line.
11. **Pure content linter plus thin FS wrapper, exemptions in the linter.** Addy `skill-lint.js`.
12. **Rule provenance fields.** `applies_to`, `status`, `verified_at`, `source` per rule, for stack-pack rot.

## E. GateGuard: what the full hook shows

- It routes `Edit/Write/NotebookEdit/MultiEdit/Bash/PowerShell`. First touch of a file is credited by prior search, allowed as a trivial change, collapsed as a same-turn sibling, or denied with class-specific questions.
- It classifies destructive commands (git subcommands, SQL `drop table|delete from|truncate`, PowerShell) and, on the first attempt, asks for a target list, a rollback line and the verbatim user instruction. The same command hash passes on retry.
- It is **fail-open by design** in several places:
  - Parse failure returns the original input.
  - State-persistence failure allows the operation.
  - Env switches disable it (`ECC_GATEGUARD=off`, `GATEGUARD_DISABLED`, `GATEGUARD_BASH_ROUTINE_DISABLED`).
  - `GATEGUARD_FACT_FORCE_MAX_DENIALS` caps denials per session; the hook text says a malformed value means "the denial cap is not active".
- `gateguard-heredoc.js` strips heredoc payloads before classification so prose isn't matched as commands, and fails closed (returns the original input) on any ambiguous shell syntax. It uses a hand-rolled shell scanner, which is a large attack surface; I did not audit it.
- Size and risk: the hook is 2,750 lines plus lazily loaded helpers I haven't seen. The A/B claim in `SKILL.md` ("+2.25 quality points") remains two tasks with an unspecified scorer. Take the questions and the protected-target class list as a procedural rule in the build skill; don't port the machinery.

## F. Verified defects (read in text or code)

| Source | Defect |
|---|---|
| ECC `living-docs-governance` ↔ `audit-docs.py` | Template history entry `[YYYY-MM-DD] removal \| …` vs audit regex requiring `## [YYYY-MM-DD] type \| …`. |
| same | Skill says "delete-zone"; audit searches `Deletion Zone`; no match means a vacuous pass. |
| ECC `skill-stocktake` `scan.sh` | Single-line field extraction reads `description: >-` as `>-`; `context-and-decisions` uses that form. |
| ECC frontmatter | Top-level `tools`, `tags`, `category`, `author`, `origin` violate the spec key set. `skill-host-compat` itself has top-level `origin`, which its own text forbids. |
| ECC eval-harness CLI | `scripts/eval-harness.js` requires `./lib/eval-harness`, but the directory holds only `canonical.js`, `capsule.js`, `envelope.js`: no `index.js`, no `package.json`. Per Copilot, standard Node resolution cannot resolve it, and the commands are unreachable as checked in. I read the CLI and the three files and saw no index. Gate execution is hard-disabled (`gate.isolation_required`, exit 1). |
| ECC `accessibility` | Calls 2.4.11 "Focus Appearance"; in WCAG 2.2 it is Focus Not Obscured (Minimum), and Focus Appearance is 2.4.13 (AAA). Same mislabel as a11y-audit. |
| ECC `contract-first` | Sample uses `number/double` and `49.9` for money against the "never float" rule. |
| ECC `ai-regression-testing` ↔ `contract-first` | `select("*")` marked PASS vs raw rows flagged as a leak. |
| ECC `ai-regression-testing` | Sandbox identity from an `x-sandbox-user-id` header gated by an env var. A leak to production is an auth bypass. |
| ECC `frontend-a11y` dropdown | Option click calls `setIsOpen(false)`, then bubbles to the parent toggle, which reopens it. |
| ECC `motion-foundations` | Rule 3 permits opacity-only fades under reduced motion, but `shouldAnimate()` returns false and renders a plain `div`. `hardwareConcurrency <= 4` as "low-end" is unsourced. |
| ECC `e2e-testing` | `data-testid` throughout vs `react-testing`'s role-first. Guards a real-money test with the runner's `NODE_ENV`. |
| ECC `security-review` | `SameSite=Strict` on all cookies breaks login after cross-site navigation. Role-only authorization. Unpinned `trufflehog@main`. |
| ECC `skill-comply` | One run per scenario level, so no variance. Runs agents with Bash allowed. |
| ECC `operator-approval-loop` | Auto-approval on timeout conflicts with "never treat silence as approval". |
| ECC `scan-rules.sh` | `~//abs/path` for files outside `$HOME`. |
| wshobson/plugin-eval | See §C. |
| openai `quick_validate.py` | No directory-name check; allowed keys omit `compatibility`. |
| taste `consistency.mjs` | Module IDs missing from `report.checks`, swallowed `Fetch.enable` error. |
| Phase 4 note | GateGuard has no network or `child_process` in the main hook; helpers not checked. |

### Stale or unverifiable claims (do not carry forward)

- ECC `react-performance`: "React Compiler (RFC, in canary)". As far as I know the compiler has been stable since late 2025.
- ECC `accessibility`: SwiftUI `.accessibilityLiveRegion` is, to my knowledge, an Android Compose concept.
- ECC `e2e-testing`: `videosPath` and `browser.startTracing` as the Playwright trace API.
- ECC `security-review`: Solana `verify` import from `@solana/web3.js`.
- `skill-comply` assuming `--add-dir` confines access; as far as I know it adds access.
- wshobson model-ID mappings and harness version numbers.
- The Codex 8 KB cap, until verified against Codex docs.
- All Vercel numeric impact claims; React 19.3+ requirements; unsourced "50×" and "200–800 ms" style claims.
- GateGuard's A/B result.
- The Claude manifest `experimental` key and `commands: ["./commands"]` in Addy's plugin.

## G. Cross-cutting design inputs

### Silent-failure catalogue for a packaging reference

1. Copilot ignores custom agents not named `*.agent.md`.
2. In Copilot's Agent Plugins mode a root `plugin.json` schema error is fatal and loads no skills.
3. OpenCode V2 needs a directory with `index.js`, not a bare file.
4. Gemini command TOML is parsed strictly; frontmatter in it breaks the file.
5. Claude Code updates an installed plugin only when the version increases.
6. Per-skill installs drop root-level shared `references/` (Addy #361).
7. `$ARGUMENTS`, `${CLAUDE_*}` and `$N` are substituted by the host; ECC `security-review` notes a literal `$1` in SQL gets substituted. Wings' SQL-injection rules use `$1`, so this hits directly.
8. Cursor errors when a skill is attached with `/` (#494), and rejects frontmatter a YAML parser rejects.
9. Codex truncates skill bodies at 8 KB (repo claim, unverified).
10. Host-reserved names: Gemini `/plan`; Codex agent names `default`, `worker`, `explorer`. Addy's rename to `/planning` collides with Antigravity's own `/planning`.

### Result-state vocabularies

| Source | States |
|---|---|
| ECC `verification-loop` | VERIFIED / FAILED / NOT PERFORMED / NOT APPLICABLE |
| ECC `browser-qa` | SHIP / SHIP WITH FIXES / DO NOT SHIP / INCONCLUSIVE (no baseline never silently passes) |
| ECC `test-collaboration` | missing / in progress / unverified / covered / not applicable |
| Vercel claims | verified / failed / unsupported / unverifiable |
| Cloudflare findings | confirmed / needs_validation / rejected |
| taste gate | PASS / FAIL / OPEN / QUICK / OFF / DONE / ERROR / SETUP, plus not-checked |
| Trail of Bits | unavailable data is never evidence of risk or safety |

Attested vs measured evidence: fields written by the agent are attested (ECC design-evidence JSON, `test-collaboration` columns, `verification-loop` reports); fields produced by a script run are measured (exit codes, test counts, screenshot dimensions, axe JSON). gstack's "no self-certification" rule applies to the attested ones.

### Stack decision record seed (oma-mobile `stack.schema.json`)

`$schema, language, framework, ui, state, navigation, http_client, data_fetching, local_storage, api_generator, api_spec, response_cache, structure, source, verify` where `verify` has `detect`, `syntax`, `tests`, each check with `cmd`, optional `pass_signal` and `skip_if_missing`. It needs pinned versions plus `verified_at`.

### Capsule/journal vs the log decision

The eval-harness capsule is a hash-chained, tamper-evident journal. It is heavier than `.wings/log.md`, and the repo's own comment says a hash chain cannot stop an operator who replaces the whole log. It is not a candidate for shipping. Its useful parts for design are the entry shape (id, lineage, kind, effect class, parent hash, allowlisted typed payload), the refusal of secret-shaped payloads before write, and the lock semantics: `withAppendLock` uses `openSync(..., 'wx')`, never waits, never infers staleness, and throws `capsule.busy`.

### Naming and ID shape

ECC `TEST-ORDER-001` has two hyphens; the linter pattern I read earlier expects prefix-hyphen-number. `ADR-0001` fits it. Any test-ID scheme needs to fit that pattern.

## H. Conflicts logged, not decided

| Topic | Positions |
|---|---|
| Router bootstrap | superpowers injects `using-superpowers` via hook on every harness. Addy and Codex docs say native description routing suffices and preloading stacks two routers. |
| Description content | superpowers: when-to-use only. Anthropic: what + when, third person. OpenAI skill-creator: what + when, all triggers in description. plugin-eval rewards pushy wording. Addy's lint accepts "use before/after/during". Earlier resolution (imperative "Use when", no workflow summary) stands. |
| Anatomy enforcement | Addy's lint requires five sections and omits `Process`; wings' anatomy includes it. |
| Autonomy gates | ECC: plan gate + commit gate. Addy `/build auto`: one plan gate plus stop-on-risk, per-task commits. |
| Fail-open vs fail-closed hooks | GateGuard fails open on parse/state errors and has a denial cap; taste's gate documents never trapping an agent; earlier house rules say gates must not be weakened by the agent that owns the work. |
| Surface | Skills only vs skills plus generated commands. |
| Instruction style | Anthropic (concise, trust the model) vs superpowers (heavy emphasis, rationalization tables, evals before any wording change). |
| Naming | Bare names vs prefix, decided by which install routes matter. |
| Coverage | ECC and Vercel mandate thresholds; the value-bar decision says otherwise. |
| Shipped vs build-time tooling | stdlib-only for shipped scripts is clear; skill-comply (Python, `claude -p`), rules-distill and stocktake need uv/jq/CLI. |
| Env-var secrets | ECC `security-review` vs the earlier "platform secret store is acceptable" rule. |
| `skill-lint.js` 500-line warning | Wings' size gates (500 lines, 8 KB) are errors or warnings? |

## I. wings-lint and packaging-check additions (from this chat)

1. Strict frontmatter subset parser: scalars only, reject block scalars, with the YAML-shape errors from `frontmatterYamlErrors`, spec-key allowlist, `name` equal to its directory.
2. Pure content linter plus FS wrapper; exemptions live in the linter.
3. Reject `$N`, `$ARGUMENTS` and `${CLAUDE_*}` in skill text outside an explicit literal context.
4. Description: ≤1024 chars, a positive "Use when", no angle brackets, no `[TODO`.
5. Resolve markdown links and backticked `references/` paths.
6. Manifest schema checks per harness, version drift across manifests, `[TODO` in any manifest.
7. Name uniqueness, per-host length and reserved-name list.
8. Selector-pinning scan (the `mcp-dependency-review` table) over scripts, workflows and configs.
9. Body-size gates: 8 KB if verified, plus 500 lines, and no hand-written counts in prose.
10. Invisible-character scan with a BOM-regex allowance; the one Phase 0 hit (`taste-skill/scripts/start.mjs:214`) is a BOM-stripping regex.
11. Findings in one shape: severity P0–P3, confidence, result state, and a `fix:` line.
12. Doc-governance checks from `audit-docs.py`, run against templates so template/regex mismatches like the history-entry one fail the build.
13. Workflow-step check: every declared step has a matching process section.
14. Secret-shaped-string scan with named canaries, for anything written to logs or evidence.

## J. Phase 0 flag facts (read from disk)

| Flag | Count | Reading |
|---|---|---|
| INVISIBLE_CHAR | 1 | False positive: BOM-stripping regex in `start.mjs:214`. |
| PROMPT_INJECTION_SHAPE, SECRET_ENV | 0 | Nothing found by those patterns. |
| UNPINNED_EXEC | 7 | 3 modern-web-guidance `@latest`, 1 `deploy-to-vercel` `npx vercel@latest`, 3 error-message install hints in `vercel.mjs` (not executed). |
| DEAD_REF | 10 | 1 `execution-policy.md:18`; 9 generated Vercel `AGENTS.md` links with wrong relative paths. |
| LICENSE_MISSING | 9 | All 9 Vercel skill folders. Phase 4: the Web Interface Guidelines and Writing Guidelines repos are MIT (Vercel Labs), but `vercel-labs/agent-skills` returned 404 for a root LICENSE, which is not proof its content shares that license. |
| TELEMETRY | 72 | Keyword noise: mostly `react-best-practices/AGENTS.md` and rule files about deferring analytics. No telemetry code found. |
| SHELL_EXEC | 32 | Dominated by taste scripts launching Chrome and `node`. |
| Deps | 99 JS scripts, all Node | No minimum Node declared except `perf.md` (Node 22+). |

## K. What the master chat should know about this chat's limits

- I audited mechanisms by reading, not by running. No candidate script was executed.
- `capsule.js` (410 lines) and the GateGuard hook (2,750 lines) were skimmed for structure, locks, env switches and caps, not audited line by line.
- Copilot-derived facts (Phase 0–4) are cited from its output. I spot-checked flags and the eval-harness `require` finding; the rest is as reported.
- Items with only secondhand evidence are listed in §F. A few judgments were mine: the build-time vs shipped distinction, the attested/measured split, and the vocabulary comparison.