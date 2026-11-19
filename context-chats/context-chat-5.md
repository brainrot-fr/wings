# Context summary: Batch 2 (database, backend), Batch 3 (security), and the tree cleanup

**Architectural reasoning.** This chat sits under the `FN-` and `TB-` shapes and gives the security block its two modes. Backend and database sources define what a function or table must state. Security splits into build-time controls attached to those IDs and a review-time hunt with an evidence standard. The dependency order is: spine IDs and linter (chat 2), then FN/TB shapes and the authorization line (this chat, chats 3 and 4), then build-time security rules (chat 5), then the review lens and verdict model (this chat), then stack packs (chat 6). Review findings must cite `FN-`/`TB-`/`PG-` IDs, not only file paths, or the spine loses traceability. This was my first pass, and chats 3 to 6 later settled or revised several items. §F marks which ones.

## A. Coverage

| Item | State |
|---|---|
| Batch 2 contents (Addy observability, api-and-interface, deprecation; alirezarezvani; knowledge-work-plugins; ccheney; oma `.agents`; 2 Supabase rules) | Read in turn 1. **The files are not in my context now, so every verdict below is carried, not re-checked.** |
| Batch 3 contents (Addy security, Cloudflare, Semgrep, Trail of Bits) | Same. |
| Cleanup trees (turns 2 and 3) | Trees only. I checked them against my cleanup list and the cuts landed: `migration-architect`, Cloudflare `MEMORY-SAFETY-AND-BINARY.md`, Supabase plumbing, 45 Trail of Bits plugins, and the `.claude-plugin`, `evals`, `tests` and `hooks` folders. |
| Trail of Bits `reference-only/` (entry-point-analyzer, mutation-testing, property-based-testing, spec-to-code-compliance) | **Tree only. Contents never arrived in this chat, so unread.** |
| Not present | alirezarezvani `scripts/` (only `CONTENTS.txt`), the Supabase `advanced-*`/`data-*`/`monitor-*` rule contents, `insecure-defaults` SKILL.md (the final tree confirms no `skills/` folder exists). |
| Residue in the cleaned tree | Collapsed `workflows/` folders remain in 3 Trail of Bits plugins (contents unknown). Each ToB skill ships `assets/trail-of-bits-mark.svg`, a brand mark that should not ship in wings. `agents/openai.yaml` files are a free sample of the Codex shape for Batch 5. |

## B. Constraints this chat established (proposals, not decisions)

1. **Security has two modes.** Build-time rules attach to FN and TB. Review mode is a lens pass over those same IDs, using Cloudflare's verdict model.
2. **Verdicts gate severity.** `confirmed` / `needs_validation` / `rejected`, and only `confirmed` gets a severity. A control outside the repo is never assumed present or absent. It becomes `needs_validation` with the exact owner-observable fact.
3. **Candidate gate.** A finding names the lower-trust principal, the crossed boundary, the affected resource and a concrete result. A missing best practice is not a finding.
4. **FN and TB have no upstream shape.** They are written new. FN cites an `R-`, has an authorization line and an error list. TB has a per-role access matrix, plus RLS or an equivalent when clients reach the database.
5. **Executable acceptance contract (oma).** Each task has acceptance criteria with IDs, plus `required_checks` (argv + cwd) that cover every criterion.
6. **Policy in the application, integrity in the database.** Business policy, workflow and external effects stay in app code. Constraints, RLS, atomic updates and audit live in the database.
7. **Fail closed on signing, session and encryption secrets.** A third-party key may use a labeled simulated mode, never silently in production.
8. **Stack packs are optional.** Postgres-Drizzle and Supabase are conditional references, not core.
9. **Full audit mode is optional.** Wings audits its own output, which is not hostile target code. Chat 6 added that upstream text is itself untrusted.

## C. Source verdicts

| Source | Take | Drop or fix |
|---|---|---|
| oma (first-fluke) | `acceptance_criteria` + `required_checks`. `TDD_EVIDENCE` (RED then GREEN, recorded). Per-task scope prefixes. Anti-patterns §5. `migration-playbook` (expand-contract, lock timeouts, batched backfill). `query-tuning`. `execution-policy`. | ISO 21500/31000/38500/42001/27001 wrappers (the files call them optional ceremony). Serena guard, vendor dispatch, `oma stats` machinery. Needs the `oma` CLI and `.agents/` runtime, so ideas only. |
| Addy observability, api-and-interface, deprecation | On-call questions first, RED/USE, cardinality rule, symptom-based alerts, runbooks. Idempotency: key from intent, atomic claim via unique constraint, payload hash, deliberate in-flight duplicate response, timeout means unknown, retention from the longest retry chain. Contract-first, validate at boundaries, Hyrum's law, expand/contract. | None significant. Highest quality in the batch. |
| ccheney `postgres-drizzle` | Version-aware (Drizzle 0.x vs 1.0), verified caveats. | Stack pack only. |
| ccheney `clean-ddd-hexagonal` | SKILL trigger logic, outbox, idempotent consumer. | Long generic DDD references. |
| Supabase | Best RLS and view checklist. Atomic rule format. | Supabase-conditional. Chat 4 found numeric impact claims, a pooled-connection leak and other defects in the rule files. |
| alirezarezvani | `code-to-prd` page shape, `spec-driven-workflow`, stop-and-ask categories. | See §E. |
| knowledge-work-plugins | ADR template, postmortem, rollback triggers. | Shallow templates. |
| Cloudflare security-audit | Verdicts, candidate gate, source-visibility rule, severity anchors, high/medium discriminator (does it fully defeat a control or only weaken it), root-cause fingerprint, independent re-verification by a fresh context (labeled degraded fallback). The 9 attack-class files become review lenses. | OS sandbox, descriptor promotion, scratch trees, Node validators, JSON-Schema interpreter, percent-encoded coverage IDs, budgets, run profiles. The two `.cjs` files stay as read-only reference. |
| Addy security-and-hardening | STRIDE per trust boundary, Always/Ask/Never tiers, hardening patterns, destructive-path rule (allowlisted root, minimum depth, ownership evidence). | The npm install-script version matrix, a dated snapshot. |
| Semgrep | Rule-file format (title, impact, impactDescription, tags, incorrect/correct). `llm-security`'s "What are you building?" priority table. | Most rule content is already in the model, so add only gotchas. Semgrep stays an optional enhancer with a fallback. Cloudflare's AI-AND-LLM is deeper, so use it as the base. |
| Trail of Bits (7 plugins) | `insecure-defaults` (fail-open vs fail-secure, tested by whether the app runs with the default). `sharp-edges` (config cliffs; 0, empty or negative values with undefined meaning). `fp-check` (standard vs deep split, rationalizations to reject). `differential-review` (risk-first triage, blast radius by caller count). `supply-chain-risk-auditor` ("unavailable data is never evidence of risk or safety"). `variant-analysis`. | CC BY-SA 4.0, so adapted text goes in separate credited files (see §H). `audit-context-building` I did not analyze in depth. |

## D. Mechanisms worth carrying

1. Findings are admitted by a candidate gate, then verdict-labeled, and severity attaches only after confirmation.
2. Fresh-context re-verification of every confirmed finding, with a labeled degraded fallback.
3. Coverage ledger: surface × boundary × attack class, the same shape as BMAD's surface closure.
4. Stable root-cause fingerprint across states, so one bug does not become three findings.
5. Source-visibility rule. Absence of repo evidence for an external control is `needs_validation`, never a pass.
6. Fail-open scan: a literal default feeding a secret name.
7. oma's AC-to-check binding. Every AC has a check, and the AC ID appears in a test name.
8. Idempotency recipe (Addy), ready to merge with chat 5's Business_Logic invariants.

## E. Defects found (all from my turn-1 read, not re-checkable now)

| Source | Defect |
|---|---|
| alirezarezvani `senior-backend/forcing_questions.md` | Citations that look fabricated ("The SLO Handbook (2019)", "Reinertsen Principle Q5", "Aaron Patterson + Rails security advisories"). I did not verify them against any source. Keep the questions and drop the citations. |
| `senior-backend` composition map | Points at skills absent from the clone. |
| `database-designer` | "Most selective column first" contradicts oma's equality-then-range. Chat 4 found wshobson agrees with oma. |
| `backend_security_practices.md` | SSRF hostname-regex blocklist is bypassable (decimal and IPv6 forms, DNS rebinding). `resolved.startsWith(baseDir)` accepts sibling prefixes like `/base-evil`. |
| `database-schema-designer` | Seed script syntax error. Polymorphic attachment table (oma-db flags it). Mutable audit table. |
| `migration-architect` | About 80 KB of non-runnable pseudo-code, including an import I believe does not exist (`sklearn.isolation`). Removed from the tree. |
| alirezarezvani, various | Invented thresholds, such as ambiguity scoring in percent. |
| oma `backend.md` rule 11 | Fallback when the API key is absent. This conflicts with Trail of Bits' fail-open rule. |

## F. House rules proposed (nothing decided)

| Topic | Proposal | Status after later chats |
|---|---|---|
| PK type | UUIDv7 on PG18+, else identity bigint | **Superseded by chat 4.** Default is `bigint generated always as identity`, UUIDv7 only for exposed or distributed IDs. |
| Password hashing | Argon2id default, bcrypt legacy | Argon2id default stands (chat 5). The parameters are OWASP's, secondhand to me. |
| Error envelope | Addy's `{error:{code,message,details}}` + `requestId`, no timestamp | Refined in chat 5 to RFC 9457 problem+json. See §H. |
| Validation status | 400 malformed, 422 failed validation | Unchallenged. |
| Pagination | Cursor/keyset default, offset only for small bounded lists, one envelope | Unchallenged. |
| Soft delete | Only where retention or restore is stated, with a partial index | Unchallenged. |
| Money | Never float. NUMERIC or integer minor units | Supported by chat 9 (ECC `contract-first` used float). |
| Layering | Layered default, DDD only on trigger | Unchallenged. ponytail's "never add layers" (chat 8) conflicts. |
| JWT/session | Stack record chooses, access ≤15 min, revocation story | **The 15-minute figure is my own unsourced number.** Chat 5 also says first-party web uses sessions, with JWT for service tokens and OIDC. |
| Secret fallback | Never for signing, session or encryption secrets | Consistent with chat 5's fail-open pattern scan. |
| Severity | P0-P3, confidence as a separate field | Unchallenged. Chat 5 maps CRITICAL to P0-P1. |
| Coverage | Value bar, not a mandate | Already decided. |

## G. wings-lint additions from this chat

1. FN cites at least one `R-`, has an authorization line and an error list. TB has a per-role access matrix, and RLS or equivalent.
2. AC to check: every AC has a `required_check`, and the AC ID appears in a test name.
3. Fail-open default scan: `getenv("X", "literal")` feeding a secret name.
4. Findings validate against the verdict contract, carry FN/TB/PG IDs, and never carry a severity unless `confirmed`.
5. Task-scope check from oma's per-task prefixes (shared with chat 4's scope gate).

## H. Cross-chat reconciliation for the master chat

- **Result-state vocabulary.** Cloudflare (`confirmed/needs_validation/rejected`) is one of seven vocabularies chat 9 lists, alongside Vercel's claim states, taste's gate verdicts and ECC's states. The master picks one. Chat 9's rule that unavailable or incomplete data can never pass is the same as the source-visibility rule here.
- **Review depth.** Cloudflare's fresh-context re-verification, Addy's doubt-driven development, BMAD's reviewer gate and chat 4's test-independence rule all describe one mechanism. Keep one, with a labeled sequential fallback.
- **Acceptance binding.** oma's `required_checks`, spec-kit's tasks, mattpocock's seams in the ticket (chat 8), ECC `test-collaboration` (chat 9) and chat 4's generated authz matrix all bind a requirement to a check. One ticket shape should carry all of it.
- **Scope and protected targets.** oma's scope prefixes, chat 4's scope gate and GateGuard's protected-target classes (chat 9) overlap. Take one list of protected paths.
- **Fail-open.** The secret-fallback rule here is about application defaults. GateGuard's fail-open hook behavior (chat 9) is a different failure, and the master should not conflate the two. Both conflict with "no gate weakened by the agent that owns the work".
- **Rule atom.** The Semgrep/Supabase/Vercel format (title, impact, tags, incorrect/correct) needs the `applies_to`, `status`, `verified_at` and `source` fields from chats 7 and 9. Qualitative impact tiers replace unsourced numbers, because Supabase's `_contributing.md` mandates numbers.
- **Idempotency.** Addy's recipe merges with chat 5's Business_Logic section. Addy's is the stronger of the two.
- **Error envelope.** Chat 5 serializes it as RFC 9457. The 9457 `instance` member is path-like, so decide whether "no path" still holds.
- **Optional enhancer pattern.** `semgrep --config p/security-audit` pulls rules from the network, the same class of problem as `npx @latest` in chat 8. Pin it or vendor it. Semgrep's `sql-injection` rule uses `$1`, which chat 9 found hosts substitute in skill text, so the packaging lint's literal-context exemption covers it.
- **License.** Chat 8's ruling means Trail of Bits and OWASP (both CC BY-SA 4.0) can be adapted if the text stays in separate credited files with a change notice. I only treated Trail of Bits as idea-only in this chat. The ToB brand SVG should not ship either way.
- **Lint runtime.** Cloudflare's validators and Addy's `skill-lint.js` are Node. `check_ids.py` and `lint_spine.py` are Python. The shipped stdlib-only rule needs a decision on one language for wings-lint.
- **Size gates.** Cloudflare's SKILL and its 9 attack-class files are long. I do not know their sizes, but they will probably need splitting to fit the 500-line and 8 KB gates chat 9 raised.

## I. Unverified, do not carry forward

- Every Batch 2 and Batch 3 defect above, since I cannot re-check the files.
- The "fabricated citations" claim, which is my suspicion and not a verified finding.
- The ≤15-minute access-token figure and any numeric threshold I cited from alirezarezvani.
- The Addy npm version matrix (11.18/12.0.1), which I called dated without checking current npm.
- Semgrep rule-text licensing. You ruled everything is MIT/Apache, but Semgrep can ship rule content under a separate rules license, and I never saw the file.
- All Trail of Bits `reference-only` content, which is unread.

## J. Open decisions carried (not asked of you)

Security block shape (build-time rules plus review lens pass, no sandbox or Node machinery). The conflict table above, minus the rows later chats superseded. Stack packs (chat 6 proposed Next.js, Supabase/BaaS, Postgres-Drizzle, GitHub Actions, Docker).

---

# Do I need more files?

I checked chats 2 to 9 first. Most of what I asked for earlier in this chat has since been supplied or taken over, so I'm withdrawing it.

**Withdrawn (already sent or owned elsewhere):**
- Supabase `security-*`, `schema-*`, `_sections` and `_template` contents, plus wshobson ×4 and Addy `code-simplification` (sent and analyzed in chat 4).
- LICENSE files. Your ruling covers them, and the one I'd still glance at is Semgrep's.
- `insecure-defaults/SKILL.md`. The final tree shows no `skills/` folder, so the plugin is built from `commands/audit.md` and `references/*.md`.
- OWASP Tiers 1 to 5, NIST 63B-4 and 63C-4 (chats 5 and 6). Primary-source docs (Postgres, RFC 9457/9106) were raised in chat 3, and I can fetch them if you allow it.

**Worth sending for this chat, in priority order:**
1. **Trail of Bits `reference-only/spec-to-code-compliance`**: `SKILL.md`, `resources/DIVERGENCE_RUBRIC.md`, `ANALYSIS_FORMAT.md` and `WORKED_EXAMPLE.md`. It is the closest source to wings-lint's AC-to-check lint and to the `ACCEPTANCE_EDITED` idea from chat 2, and I have only seen its tree.
2. **`reference-only/mutation-testing` and `property-based-testing`**: both `SKILL.md` files, mutation-testing's `equivalent-mutants.md`, `severity-classification.md` and `workflows/analyzing-results.md`, and property-based-testing's `references/generating.md` and `reviewing.md`. They feed the test value bar and the weak-assertion rule, which chat 2 flagged and chat 4's test-independence gate depends on.
3. **OWASP ASVS.** Chat 4 asked for it too, so send it once. The security block needs a requirement catalogue shaped like wings' `R-` items, and ASVS is the closest upstream shape. It is CC BY-SA, which is now adaptable.
4. **Supabase `data-pagination`, `data-upsert` and `lock-skip-locked`.** They are small, and they back the pagination, idempotency and queue rules in core. The rest of `advanced-*`, `data-*` and `monitor-*` can wait for the Supabase pack.

**Skip:** `entry-point-analyzer`. Its references cover only blockchain languages, and chat 4's Next.js entry-point classification already covers the web case.

**Not fixable by files:** the FN, TB and PG shapes and the stack decision record have no upstream source. They get written new in the master chat.