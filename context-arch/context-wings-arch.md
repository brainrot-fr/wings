# context-wings-arch.md: Wings architecture (v1), master chat handoff

Architectural reasoning: the sources split along two axes the earlier chats blurred. Phases (intent to ship) own artifacts, IDs, gates and handoffs. Disciplines (data, backend, identity, security, frontend) own rules and attach to phase gates via FN-/TB-/PG- IDs. Structuring by SDLC stage alone duplicates rules (auth appears in four stages), so the structure is: kernel, phase blocks that own artifacts, discipline blocks that own rules, one home per fact. Dependency order for design: kernel, requirements, testing, code review, then the rest. Phase order differs from design order (see D2).

Memory: nothing is saved, per the user's standing instruction. Do not use memory tools in this project.

## A. Status and rulings (all ACCEPTED by the user)

| # | Ruling |
|---|---|
| 1 | 15 core blocks in v1. 8 capability blocks are v2: reserved, not designed in v1. |
| 2 | Sibling skills, one skill per block. Any sibling is usable standalone on an existing codebase. Testing and Code Review are separate blocks. Code Review comes before Testing in phase order. |
| 3 | Dual mode (attached / standalone) with a build-inlined kernel-lite fragment and hash-drift lint. |
| 4 | Design order: kernel, requirements, testing, code review, then remaining blocks in dependency order. Capability blocks last. |
| Reading A | One skill per block, including Requirements, Testing and Code Review. No entry-plus-satellite families. Modes live inside the skill, depth lives in references/. |
| Reading B | Phase order: Build, Code Review gate, Testing gate, Ship. Tests are still authored during Build (TDD) using Testing's author mode. The Testing gate verifies and audits. |
| Emphasis | Requirements, Code Review and Testing get the deepest engineering: scripted where possible, largest reference sets, highest QA bar. |
| Size | The 8 KB cap is not required. 500 lines / ~5k tokens per SKILL.md is a lint warning, not an error. |
| Boundary | Intent produces one confirmed statement plus the stakes ladder. Requirements owns all detail-level questioning. |

## B. decision-architecture.md (as accepted)

### D1. Product shape
- Suite of sibling skills plus a router. Not monolithic.
- Any sibling installs and works alone on an existing codebase.
- A skill never requires another skill. Cross-skill use is a soft dependency with a labeled degraded fallback.

### D2. Core blocks (v1): 15

| # | Block | Kind |
|---|---|---|
| 0 | Kernel (router + shared contracts) | all |
| 1 | Intent | phase |
| 2 | Stack & Constraints | phase |
| 3 | Requirements | phase |
| 4 | Experience Design | phase |
| 5 | Architecture | phase |
| 6 | Data | discipline |
| 7 | Backend & API | discipline |
| 8 | Identity & Access | discipline |
| 9 | Security | discipline |
| 10 | Frontend Engineering | discipline |
| 11 | Plan & Build | phase |
| 12 | Code Review | phase gate |
| 13 | Testing | phase gate |
| 14 | Ship & Operate | phase |

- Phase order: Intent, Stack, Requirements, Experience/Architecture, Plan & Build, Code Review, Testing, Ship.
- Discipline blocks (6-10) own rules and attach to phase gates. They own no phases.

### D3. One home per fact
Auth is reached from Requirements, Backend, Security and Frontend, but its rules live only in Identity & Access. Others link.

### D4. Engineering emphasis
See A. QA method: eval loop with and without the skill (2-3 prompts, baseline, assertions added after the first run, 60/40 train/validation split for descriptions).

### D5. Dual mode
- Attached: `.wings/manifest.md` exists. The skill reads spine artifacts and cites spine IDs.
- Standalone: no spec. A recon step builds a surface inventory from code (entry points, tables, pages, tests). Findings cite file:line with local F- IDs. Standalone never writes into `.wings/`.
- Recon is a shared fragment, not a skill.

### D6. Shared contracts without duplication
- One source file per contract in the wings repo.
- The build inlines kernel-lite into every sibling between markers. The lint fails on hash drift. Hand edits inside the markers are overwritten.
- Cross-skill soft dependency: Code Review loads Security, Frontend and Testing lenses if installed, otherwise runs general lenses and labels the result degraded.

### D7. Size policy
See A. Detail goes in references/, one level deep, with explicit load triggers.

### D8. Capability blocks (v2, reserved)

| Block | Existing source coverage | Honest gap |
|---|---|---|
| Payments | Webhook_Security, Addy idempotency, money-type rule, Business_Logic | No payments source. Provider docs needed. |
| Email & Notifications | Email_Validation, Forgot_Password | Deliverability, templates, preferences, unsubscribe |
| Background Jobs | Addy idempotency, ccheney outbox, Supabase lock-skip-locked | Queues, retries, DLQ, scheduling partial |
| File Storage | File_Upload, Multi_Tenant storage deletion | Presigned URLs, separate origin, SVG, quotas thin |
| Search | none | Nothing |
| i18n | oma i18n-guide (unread beyond the name) | Nearly all |
| Privacy & Compliance | none | Retention, deletion, consent, DSAR |
| LLM Features | AI_Agent_Security, MCP_Security, LLM_Prompt_Injection, Cloudflare AI/LLM, Semgrep llm-security | Eval, cost, output handling |

- v1 reserves ID prefixes and the pack interface only.
- Each needs primary documentation before design. Not synthesized from memory.
- Mobile is out of v1 unless the user adds it.

### D9. Stack packs
Optional, loaded only when the stack record names the stack. Each rule carries applies_to, status, verified_at, source. An expired verified_at loads with a re-verify warning. Proposed v1 packs (not yet confirmed): Next.js, Supabase/BaaS, Postgres-Drizzle, GitHub Actions, Docker. Deferred: FastAPI, Django, Node-Express, NoSQL.

### D10. Tooling
- wings-lint and gates: stdlib-only, no runtime fetch.
- Browser-bound or CLI-bound checks are optional enhancers with a labeled fallback.
- Build-time tools (rule distillation, comply/eval harness, upstream audit) may use more.
- Packaging is a thin layer over one skills directory. Skills are the portable surface. Commands are optional and generated.

### D11. Provenance and licensing
- Upstream is read in full and rewritten into one voice. No machinery is ported.
- MIT/Apache text carried with notice.
- CC BY-SA (OWASP, Trail of Bits): adapted only in separate credited files with a change notice. Do not blend into MIT files. Trail of Bits brand SVG never ships.
- NIST text reusable with attribution (verified for 63C-4; 63B-4 front matter not checked).
- BMAD's name is trademarked: carry ideas, not the name. pstack attribution (Lauren Tan, MIT) needs a NOTICE entry if design-it-twice text is reused.
- Normative claims are verified against a primary source before being written down.

### D12. Source-reliability policy
- Claims carried from earlier reads are not rules until re-checked.
- Contrast ratios and similar numbers are generated by script, never typed.
- Unsourced thresholds are labeled "wings judgment".

## C. Per-block ownership and main sources

| Block | Owns | Main sources | Status |
|---|---|---|---|
| 0 Kernel | See context-kernel-arch.md | Addy, gstack ETHOS, ECC | Adapt and merge |
| 1 Intent | Confirmed intent, stakes ladder, size classifier | mattpocock grilling, Addy interview-me, idea-refine, ECC orch-* | Protocol choice OPEN |
| 2 Stack & Constraints | Stack decision record, NFR numbers, package admission, verified_at pins | oma-mobile stack.schema.json, senior-frontend 7 forcing questions, Addy constraint-driven | New |
| 3 Requirements | R-, US-, AC-, FLOW-, MUST/SHOULD/MAY plus Given/When/Then, NFRs as numbers, assumptions, glossary, ADRs, MoSCoW, clarify, checklist | spec-kit, BMAD, mattpocock | Adapt. Modes: greenfield, quality audit, recover (brownfield), change. |
| 4 Experience Design | DESIGN.md, EXPERIENCE.md, PG- files (delta only), journeys, surface closure | bmad-ux, oma-design, Anthropic frontend-design | PG- shape new |
| 5 Architecture | AD- spine, design-it-twice, 8 red flags, layering enforced by failing CI | BMAD, gstack plan-eng-review, wshobson architecture-patterns, mattpocock | Adapt |
| 6 Data | TB-, Postgres rules, migrations, RLS inventory | wshobson, Supabase, oma-db, ccheney | Adapt |
| 7 Backend & API | FN-, contracts, errors, pagination, idempotency | Addy, oma, spec-kit contract-driven | FN- shape new |
| 8 Identity & Access | Authn, authz, sessions, federation, tenancy, per-FN authorization line | NIST 63B-4, 63C-4, OWASP | Mostly new |
| 9 Security | TH-, AB-, build rules, review lenses, verdicts, wings-as-attack-surface | Cloudflare, Addy, OWASP, Trail of Bits (BY-SA, separate files) | Adapt |
| 10 Frontend Eng. | Components, state, CSS, a11y, perf, countable checks | Vercel, oma-frontend, modern-css, taste mechanisms | Adapt |
| 11 Plan & Build | Tickets (seams, ACs, required checks, scope paths), TDD, simplify step | spec-kit tasks, mattpocock to-tickets, oma, Addy | Merge |
| 12 Code Review | Modes: diff, baseline, PR. Recon, candidate gate, dedup by fingerprint, verdict/severity/confidence, mandatory coverage accounting, general lenses, fresh-context re-verification, respond rules | gstack, Cloudflare, open-code-review delegate, ponytail, BMAD, Addy | Merge |
| 13 Testing | Value bar, lane states, failure triage, weak-assertion ban, case design from ACs, authz matrix from FN lines, TDD author mode, test audit, UI/e2e | gstack, Addy, mattpocock tdd, oma, ECC, OWASP authz regression | Merge |
| 14 Ship & Operate | CI/CD, rollout, rollback, observability, runbooks, deprecation | Addy, GitHub Actions and Docker sheets | Adapt |

Lens ownership: security lenses in Security, a11y lenses in Frontend, test-quality lenses in Testing. Code Review loads them if present.

### Requirements modes (inside one skill)
greenfield, quality audit (standalone-capable: requirement-quality checklist, testability gate, ambiguity scan, two-pass rubric), recover (brownfield: code-to-prd shape, every item tagged inferred or confirmed-by-user, nothing invented), change (delta, impact analysis over the trace graph, ACCEPTANCE_EDITED detection, supersede/withdraw).

### Testing scope
Owns: value bar (4 questions: behavior protected, credible regression, why existing coverage misses it, whether it needs a production seam), test-count lane states, failure ownership triage (in-branch vs pre-existing, ambiguous defaults to in-branch), no weak assertions, coverage as diagnostic only, first move by change type (add: new failing tests; change: update existing tests first; fix: reproduce as failing regression test; refactor: stay green), mock only at boundaries, role-first queries.
Gaps with no source: performance and load testing, fixtures and determinism, migration testing, mutation and property-based testing (Trail of Bits reference-only files never sent).

## D. Accepted house rules from earlier chats (still proposals until re-verified where noted)

| Topic | Rule |
|---|---|
| Spec holds stack | Stack decision record first, then a stack-inclusive spec |
| Scope vs severity | MoSCoW for scope. P0-P3 reserved for severity. |
| Unknown markers | [NEEDS CLARIFICATION] max 3, resolved before plan, plus Assumption: lines |
| Acceptance grammar | MUST/SHOULD/MAY plus Given/When/Then |
| Question protocol | One at a time, plain text, recommended answer attached, max 5 in clarify |
| Artifact lifecycle | Living spec, immutable IDs, withdrawn not deleted. Plan and tasks are disposable. |
| Coverage | Value bar. Coverage is a diagnostic, never a target. |
| Test-first | Default, with a one-line opt-out |
| Visual direction | Wings recommends with a reason, user overrides. Elicit-only stays for product intent. |
| Accessibility | WCAG 2.2 AA floor. Contrast generated by script. |
| Passwords | NIST 63B-4: min 15 single-factor, min 8 inside MFA, max accept >=64, no composition rules, no periodic rotation, breached/common/context blocklist, no truncation, NFC. Argon2id default (OWASP min m=19456, t=2, p=1, unverified against RFC 9106). bcrypt legacy only, with byte cap that rejects. |
| PK type | bigint generated always as identity by default. UUIDv7 only for exposed or distributed IDs. |
| Index order | Equality columns first, then range or sort. |
| Money | Never float. NUMERIC or integer minor units. |
| Pagination | Cursor/keyset default, offset only for small bounded lists |
| Validation status | 400 malformed, 422 failed validation |
| Soft delete | Only where retention or restore is a stated requirement, with a partial index |
| Layering | Layered by default. DDD only on trigger criteria. Enforced by failing CI. |
| Denial codes | 401 unauthenticated, 403 function-level role denial, 404 another owner's object |
| Lockout | Throttle per account and per IP with escalating delay. No permanent lockout. |
| Security questions | Never |
| Tokens/nonces | CSPRNG, >=128 bits. Never uuid.v4 or Math.random. |
| Secrets | Env vars OK via platform secret store. Never in images, ARG/ENV, or client bundles. Never fall back for signing, session or encryption secrets. |
| Tenant context | Transaction-local (SET LOCAL or set_config(...,true)). Request role neither superuser nor BYPASSRLS. |
| Authorization | Role plus mandatory ownership/tenant predicate. List, count, export, search share one predicate. Fail closed. |
| First-party web auth | Server-side sessions. JWT only for service tokens and OIDC. Auth Code + PKCE only. |
| OAuth linking | Key on issuer+subject. Never auto-link on email. Link only from an authenticated session. email_verified check is wings-original. |
| Top 10 citing | CWE or category names, never "A05" |
| Baseline policy | Baseline Widely available features by default. Newer features opt-in per browser target in the stack record. |
| Impact claims in rules | Qualitative tiers unless sourced |
| Test-independence | Security tests generated from FN authorization lines by script, not authored by the code-writing step |
| Seams | Carried in the ticket (tdd needs user-confirmed seams, implement-spec runs unattended) |

## E. OPEN items (not decided; carry to the relevant block design)

| Item | Where it lands |
|---|---|
| Intent protocol: Addy interview-me vs mattpocock grilling (pick one) | Intent |
| Ticket shape: spec-kit tasks.md vs mattpocock tickets vs oma required_checks (one shape carrying seams, ACs, required checks, scope paths, blocking edges) | Plan & Build |
| Replacement for mattpocock /setup (wings tracker and label config) | Plan & Build |
| DESIGN.md format: Google Labs YAML tokens (referenced by {token}) vs oma 9-section prose | Experience Design. Needs google-labs-code/design.md. |
| Token source (hex, OKLCH, Tailwind v4 @theme), icon library, default typography | Experience Design / Frontend |
| Rule atom: merge title/impact/incorrect/correct/reference with applies_to/status/verified_at/source | Kernel references / all rule blocks |
| Error envelope: bare Addy {error:{code,message,details}}+requestId vs RFC 9457 problem+json (its instance member is path-like) | Backend & API |
| Password minimum 15 regardless of MFA (would settle Django min_length 8 and Zod composition findings) | Identity & Access |
| FAL2 default with FAL3 as pack; auth-recency field on the FN authorization line; no email auto-link | Identity & Access |
| Session timeouts and throttle limits: no primary source (63B-4 section 5 and 3.2.2 unread; 63C-4's 5 minutes applies only to the authorization code) | Identity & Access |
| Package-age default (judgment number; user has not chosen) | Stack & Constraints |
| Layer enforcement tooling per pack (import-linter, tsarch, dependency-cruiser) | Architecture |
| Review-depth mechanism (one: fresh-context subagent with labeled sequential fallback, 3-4 lenses) | Code Review |
| Shared-code rubric, simplify step slot (Build, Simplify, Review) | Plan & Build / Code Review |
| Router bootstrap: native description routing (leading) vs hook injection | Kernel references / Packaging |
| Naming: bare vs prefixed, collisions (Addy and superpowers both ship test-driven-development) | Packaging |
| Skills only vs skills plus generated commands | Packaging |
| Description style: "Use when", no workflow summary (current resolution) vs pushy wording | Kernel K9 (resolved for wings; confirm in QA) |
| Stack packs for v1 (proposed list above) | Stack packs |

## F. Source reliability tiers (carry forward)

| Tier | Content | Trust |
|---|---|---|
| A, read directly | NIST 63B-4 section 3.1.1, 63C-4 (sections 2, 3.4, 3.8, 3.9, 3.11, 3.13, 4.7, 4.9-4.11, 6), spec-kit, Addy Batch 1, BMAD real files, check_ids.py, lint_spine.py, Addy skill-lint.js, ECC (38 skills), batch 5 packaging | High |
| B, carried, not re-checked | Batches 2-4 verdicts, OWASP Tiers 1-5 verdicts and defects, gstack, Supabase and wshobson defects, a11y data defects | Medium. Re-check before any becomes a rule. |
| C, secondhand | Copilot dossier (Vercel, taste, oma-mobile), Codex 8 KB cap (now moot), consistency.mjs | Low until spot-checked |
| D, never read | OpenSpec, Impeccable, google-labs-code/design.md, BMAD stub workflows (bmad-build, bmad-build-auto, bmad-code-review, bmad-agent-po), Trail of Bits reference-only/* (spec-to-code-compliance, mutation-testing, property-based-testing), NIST 63B-4 sections 5 and 3.2.2, OWASP ASVS, wshobson generate.py and other adapters, GateGuard helper libs, validate-skill-host-compat.js, mattpocock setup/wayfinder/improve-codebase-architecture/pr/research, taste assets/layout/check.mjs, Vercel LICENSE | Gaps |

Suspicions, not findings: "fabricated citations" in alirezarezvani senior-backend and senior-frontend; hand-computed contrast ratios.

## G. Files that would improve the design (priority for the next chats)

1. For Requirements: OpenSpec, BMAD stub renders (bmad-code-review, bmad-build), google-labs-code/design.md, BMAD validate_skills.py.
2. For Testing: Trail of Bits reference-only mutation-testing, property-based-testing, spec-to-code-compliance (BY-SA, separate files).
3. For Code Review: mattpocock remaining skills, open-code-review preview/rule docs, BMAD bmad-code-review render.
4. For Identity: NIST 63B-4 sections 5 and 3.2.2, OWASP ASVS, RFC 9700, 7636, 9106, 9457.
5. For Data: PostgreSQL primary docs (multicolumn indexes, row security, set_config, identity columns).
6. For Experience/Frontend: Impeccable, WCAG 2.2 criteria list, Core Web Vitals and Baseline definitions, Tailwind v4 and shadcn theming docs.
7. Packaging: wshobson tools/generate.py, Vercel LICENSE.
Optionally a real app's UI as a QA fixture (AcadFlow).

## H. wings-lint requirements by block (consolidated, all stdlib Python)

- Skills: strict scalar frontmatter subset (block scalars fail), spec-key allowlist, name equals directory, description <=1024 chars with positive "Use when", no angle brackets or [TODO, required sections including Process, workflow-step check (declared Step N needs a matching section), resolve markdown links and backticked references/ paths, reject $N / $ARGUMENTS / ${CLAUDE_*} outside literal context, size warnings, no hand-written counts in prose, kernel-lite hash drift, name uniqueness and per-host length/reserved names, manifest schema and version drift, selector-pinning scan.
- Spine: ID define/reference/duplicate/withdrawn/superseded checks, --prefixes, typed coverage (R- to AC- to check to test name; FN- cites R-, has authorization line and error list; TB- used by an FN-, has per-role access matrix and RLS/equivalent; every PG- has a journey and every stated need has a PG-), required fields as labeled lines, DESIGN.md token-reference resolution and duplicated-hex flag, TH- needs a response and test reference when "mitigate", AB- links to FN- and a test name.
- Security/identity: generated authz matrix cells (cross-user, cross-tenant, body assertions), shared predicate for list/count/export, webhook FN declares signature, tolerance, dedupe, callback FN declares each federation check, pattern scans (jwt.verify without pinned alg/iss/aud, uuid/Math.random for tokens, redirect(req.query), fail-open secret defaults, mass assignment, plain SET for tenant context, FK without ON DELETE or index, security definer outside private schema, money as float).
- Gates: finite verdicts, unrun check cannot pass, waiver checks, review-report coverage_rate present, diff gate (out-of-scope paths, deleted tests, reduced assertion counts, protected-file changes), invisible-character scan (BOM allowance), workflow and Dockerfile pattern scans, stub scan, debt ledger (shortcut: comments with limit and upgrade path).
- Contrast script: extend to rgba, hsl, oklch, 8-digit hex. Check 1.4.11 on input borders. Do not emit borderline-only suggestions.
- Do not use: a11y_scanner.py as a gate (keep the rule catalogue), consistency.mjs reporting, plugin-eval composite score.

## I. Unverified, do not carry forward

- Every Batch 2-4 and OWASP defect (not re-checked).
- Python being more widely present than Node (judgment).
- Argon2id parameters, session timeout ranges, 63B-4 outside section 3.1.1.
- Codex 8 KB cap, Vercel numeric impact claims, GateGuard A/B result, the Claude manifest experimental key.
- All claims marked "as far as I know" in earlier chats.

## J. Next step
Design the Requirements block: artifact chain, ID rules and trace graph (from kernel K3, K4, K10), the five modes, the R-/US-/AC- shapes, the Intent boundary, and the linter spec. Then Testing, Code Review, and the remaining blocks in dependency order. Capability blocks last (v2).