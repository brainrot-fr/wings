# Phase 2: Targeted Verifications

## a. Modern Web Guidance runtime
Yes. The skill instructs `npx -y modern-web-guidance@latest search "<query>" --skill-version 2026_11_09-5bcc021b` and `npx -y modern-web-guidance@latest retrieve "<id>"`; `legacy-scan` is also prescribed only for broad modernization (`SKILL.md:23,36,63`). `@latest` is unpinned.

## b. Open Code Review delegation
The OCR-side steps are deterministic: choose review mode/range and construct the diff (`open-code-review-delegate/SKILL.md:25-64`), filter/select files and resolve rules (`:70-127`), then account for every previewed file (`:128`). The actual review is performed by the host agent, not OCR (`:4-14,168`); the skill requires the `ocr` CLI.

Coverage fields, exactly: `total_files`, `reviewed_files`, `skipped_files`, `coverage_rate` (`open-code-review-delegate/SKILL.md:128`).

## c. Vercel Optimize

### (i) Registered gates and input signals
All 15 registrations are in `lib/gates/index.mjs:16-37`; the generated thresholds are summarized in `references/candidates.md`.

| Gate | Signal consumed |
|---|---|
| `uncached_route` | `requestsByRouteCache` + `requestsByRouteMethod` (`lib/gates/uncached-route.mjs:55-77`) |
| `slow_route` | `fnDurationP95ByRoute`, `requestsByRouteCache`, `fnStatusByRoute` (`slow-route.mjs:52,71-73`) |
| `route_errors` | `fnStatusByRoute`, or `requestsByRouteStatus` plus route request totals (`route-errors.mjs:37-42`) |
| `cold_start` | `fnStartTypeByRoute`; legacy `coldStartByRoute` (`cold-start.mjs:33,45-46`) |
| `isr_overrevalidation` | per-route `isrWritesByRoute` and `isrReadsByRoute` (`isr-overrevalidation.mjs:42-43`) |
| `cwv_poor` | `cwvCount`, `cwvCountByRoute`, `cwvLcpByRoute`, `cwvInpByRoute`, `cwvClsByRoute` (`cwv-poor.mjs:19-25`) |
| `external_api_slow` | `externalApiP75` and `externalApiCount` (`external-api-slow.mjs:37,48`) |
| `scanner-driven` | `codebase.findings`, grouped by scanner configuration and annotated observability signal (`scanner-driven.mjs:29-47,55-69`) |
| `platform_fluid_compute` | project Fluid config plus cold-start and p95-duration/request signals (`platform-fluid-compute.mjs:18-20,45-69`) |
| `platform_bot_protection` | project BotID/WAF config, request volume, `fdtByBot`, and edge usage cost (`platform-bot-protection.mjs:20-42,86-118`) |
| `middleware_heavy` | `middlewareCount` and `requestsByRouteCache` totals (`middleware-heavy.mjs:14-17`) |
| `observability_events_attribution` | billed service rows in `usage.services` (`observability-events-attribution.mjs:17-25,45`) |
| `usage_spike_triage` | daily `usage.breakdown.data[]`, including service-level cost (`usage-spike-triage.mjs:1-4,20,85`) |
| `build_minutes_fanout` | billed `usage.services` Build Minutes share and `turbo-force-bypass` scanner findings (`build-minutes-fanout.mjs:19-33,56-60`) |
| `region_misconfig` | `codebase.findings` matching `region-pin-in-config`, plus route count (`region-misconfig.mjs:22,25-31,56-61`) |

### (ii) Usable without a Vercel account/token?
Partly. Pure JS gates, hard gates, code scanners, candidate selection, sanitizers, grading, and claim checks can run against supplied local signals/repository data. Full collection cannot: `SKILL.md:22-24` requires Vercel CLI v53+, an authenticated session, and a linked/scoped project. Claim verification also invokes local `rg` (`lib/verify-claim.mjs:996-1000`).

### (iii) Finding-verification protocol
1. `extractClaims` turns citations, affected-file paths, finding references, framework/version use, cache policy, and project facts into typed checks (`lib/extract-claims.mjs:1-63`).
2. `verify-claim` returns explicit `verified`, `failed`, `unsupported`, or `unverifiable` dispositions; checks include file/pattern/citation/version and cache/auth-safety validation (`lib/verify-claim.mjs:14-28,724-739`).
3. `verify-and-regen.mjs` verifies claims, applies deterministic sanitizers, then re-extracts and re-verifies the sanitized recommendation before grading (`:95-160`).
4. Project-config contradiction and cache-safety failures trigger regeneration/withholding; low quality (<0.55) and `needsReview` recommendations are also withheld (`:167-215,236-267`; `lib/grade-recommendation.mjs:13-25,145-151`).

Sanitizers strip or rewrite unsupported money/counts, directives, dependencies, version-inapplicable/unknown citations, and unsafe phrasing; missing citations drop the item (`lib/sanitizers/index.mjs:31-58`; `references/recommendations.md:121-140`). Grading weights grounding 0.35 and evidence 0.30, versus specificity 0.20 and actionability 0.15 (`lib/grade-recommendation.mjs:13-25`).

### (iv) Network, shell, and trust boundary
Collection uses the Vercel CLI through `child_process.execFile`, not shell interpolation (`lib/vercel.mjs:1-3,310-313`); the CLI makes authenticated Vercel API/network requests. The collector checks project/account scope before metrics (`scripts/collect-signals.mjs:128-137,368-393`), and the skill forbids putting tokens in echoed commands (`SKILL.md:28`). Local claim verification separately invokes `rg` with a file allowlist (`lib/verify-claim.mjs:996-1000`); no candidate script was run.

## d. `observation-safety.mjs`
`splitCustomerSafeObservations` separates unsafe observations and returns a holdback reason plus `needsEvidence: true` (`:1-16`). It rejects contradictions of prior abstentions, unsupported WAF/bot-category claims, Bot Protection actions lacking staged rollout and allowlist evidence, stale framework APIs, unsupported framework/static-generation/source-absence/cache-life/runtime-cause claims, and implementation-grade actions that lack the recommendation evidence bar (`:19-52,68-106,129-176`).

## e. Web Design / Writing Guidelines runtime fetch
Both fetch current rules before each review. Web Design uses `https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md`; Writing uses `https://raw.githubusercontent.com/vercel-labs/writing-guidelines/main/command.md` (`web-design-guidelines/SKILL.md:17-25`; `writing-guidelines/SKILL.md:17-25`).

## f. Taste `scripts/gate.mjs`
Non-waivable FAIL IDs: `kit-edited` detects page-loaded files differing from the skill's asset copy (`gate.mjs:34-35,365`); `checker-gaming` detects page code branching on headless-browser/automation checks (`:35-36,374`). The gate explicitly says these cannot be waived (`:47-53`).

It reads/compares the `assets/` kit and invokes `assets/layout/check.mjs` (`gate.mjs:31-35,310-321,511`). These assets are outside the allowed source scope. Minimum change to run without them: guard the asset-dependent checks as explicit `NOT_CHECKED`/skip outcomes and ensure an incomplete asset check cannot report PASS; do not make absent assets look like a successful check.

## g. Taste performance thresholds and evidence status
`perf.md:14-30` and `scripts/perf.mjs:58-66,245-337` list the following. Numeric thresholds are house budgets: the source names no published standard for them. The file explicitly says CPU FCP/LCP are comparative, not field data (`perf.md:7-11`).

| Metric | WARN / FAIL | Source status |
|---|---|---|
| Gzipped text transfer | >1500 / >3000 KiB | House budget; no standard cited |
| Total / largest image | >1200 / >350; >2400 / >700 KiB | House budget; no standard cited |
| Parsed JS / CSS | >450 / >120; >900 / >250 KiB | House budget; no standard cited |
| Requests | >60 / >110 | House budget; no standard cited |
| Font families / files / bytes | >2 / >4 / >160; >3 / >6 / >320 KiB | House budget; no standard cited |
| `<img>` missing dimensions; below-fold non-lazy; oversized; background photo below fold | 1–3 / >=4 findings | House count rules; no standard cited |
| Live WebGL contexts | >4 hard cap | House rule (`perf.md:40`) |
| WebGL contexts created over scroll | >12 / >24 | House budget; no standard cited |
| Long tasks / blocking time | >8 / >1.5 s; >20 / >4 s | House budget; no standard cited |
| CPU FCP / LCP | >2.5 / >4.5 s; >4.5 / >8 s | House budget; expressly not field data |
| Layout shift | >0.1 / >0.25 | No source cited in this file |
| Loaded entry modules never mounted | 1–2 / >=3 | House count rule; no standard cited |
| Broken request / horizontal overflow | any = FAIL | House binary checks; no standard cited |

The 1,015,117-byte / 11,485-line `consistency.mjs` check-ID and named-policy-threshold inventory is in `phase4_missing_sources.md`, section 3. It includes all 98 ordered IDs and all 43 module IDs, plus the stated rule thresholds. The implementation was not read line by line, so this is not a branch-by-branch audit of every internal comparator. The metric inventory above is specifically for `perf.mjs`.

## h. Mobile variant stack schemas
Yes. All three `stack.yaml` files point to `variants/stack.schema.json` (for example `variants/flutter/stack.yaml:1`); the shared schema declares language, framework, UI, state, navigation, HTTP client, data fetching, local storage, API generator/spec, response cache, structure, source, and `verify` (`variants/stack.schema.json:1-56`). Generic stack-decision fields: `$schema`, `language`, `framework`, `ui`, `state`, `navigation`, `http_client`, `data_fetching`, `local_storage`, `api_generator`, `api_spec`, `response_cache`, `structure`, `source`, `verify`; `verify` has `detect`, `syntax`, `tests`, with checks using `cmd`, optional `pass_signal`, and `skip_if_missing` (`_shared/core/stack-verify.schema.json:5-34`).

## i. `_shared/core` standalone/no-CLI dispositions
No explicit Serena MCP dependency was found in the 18 opened core files. OMA CLI, `.agents/`, MCP, and runtime dependencies are called out per row.

| File | Disposition for a standalone suite |
|---|---|
| `anti-ai-prose.md` | keep — portable editing/evidence constraints (`:7-18`); no CLI/MCP dependency. |
| `api-contracts/README.md` | merge-into-backend-contracts — useful contract lifecycle, but transient output path is `.agents/results/...` (`:11-24`). |
| `api-contracts/template.md` | drop — placeholder CRUD/auth/schema example can be mistaken for required architecture (`:10-85`); no runtime dependency. |
| `clarification-protocol.md` | keep — generic ask/pause rules (`:5-21`); tool transport is runtime-specific, no OMA CLI dependency. |
| `code-intelligence.md` | drop — mandates configured provider, `.agents` config, OMA install/update, hook, and MCP capability (`:7-15,30-36`); no Serena name found. |
| `common-checklist.md` | merge-into-security-and-qa — portable checklist; authorization delegates to `execution-policy.md` (`:1-29`). |
| `context-budget.md` | merge-into-skill-context-loading — useful size-vs-utility warning, but invokes Bun script and `oma skill audit` (`:7-13`). |
| `context-loading.md` | merge-into-skill-routing — selection principles transfer; injected CLI/runtime and `.agents` resources are OMA-specific (`:5-32`). |
| `difficulty-guide.md` | merge-into-sdlc-process — behavior-based decomposition transfers; OMA CLI classifier is product-specific (`:5-22`). |
| `execution-policy.md` | keep — authorization and verification principles transfer (`:5-18`); remove `oma verify`/CLI test references (`:18-21`). |
| `lessons-learned.md` | merge-into-sdlc-retrospective — evidence and applicability rules transfer; storage assumes `.agents/state` (`:5-19`). |
| `prompt-structure.md` | merge-into-sdlc-handoffs — generic task/context/done criteria (`:5-19`); result identity is runtime-injected (`:20-23`). |
| `quality-principles.md` | keep — generic scope, correctness, and verification principles (`:1-12`); no explicit CLI/MCP dependency. |
| `session-metrics.md` | drop — OMA session storage, `oma stats`, and `oma retro` semantics (`:7-33`). |
| `skill-routing.md` | drop — route table is OMA skill-name-specific and dispatch follows vendor runtime (`:5-37`). |
| `stack-verify.schema.json` | drop — schema is consumed by OMA `cli/commands/verify/verify.ts` and describes shell commands via child process (`:1-28`). |
| `test-approach.md` | merge-into-sdlc-verification — optional TDD/coverage principles transfer; plan fields and enforcement use OMA PM/CLI (`:1-50`). |
| `vendor-detection.md` | drop — requires `.agents/oma-config.*`, vendor-specific agent runtime, `oma agent spawn`, and MCP polling (`:4-51`). |
