# Phase 3: Cross-Cutting Findings

## 1. Atomic rule-file formats

| Source family | Frontmatter keys observed | Common fields | Differences |
|---|---|---|---|
| Vercel Composition Patterns | `title`, `impact`, `impactDescription`, `tags` (`rules/architecture-avoid-boolean-props.md:2-5`) | All sampled Vercel rule families use these four keys. | No separate description/body metadata beyond the Markdown content; impact vocabulary is CRITICAL/HIGH/MEDIUM/LOW. |
| Vercel React Native | `title`, `impact`, `impactDescription`, `tags` (`rules/ui-pressable.md:2-5`) | Same four keys. | Includes platform-specific tags and the same inconsistent impact levels found in section listings. |
| Vercel React Best Practices | `title`, `impact`, `impactDescription`, `tags` (`rules/async-parallel.md:2-5`) | Same four keys. | Impact metadata includes numeric improvement claims that are not always sourced in the rule. |
| Supabase-style atomic rule | Not available in the allowed scope. | Cannot compare. | No Supabase rule file was opened or found among the specified sources. |

This frontmatter does not match the Wings global-ID/severity-confidence contract; do not copy impact labels as P0-P3 severities.

## 2. Mechanical gates

| Gate | Input | Output vocabulary | Exit convention | Waiver | Safeguards against trapping an agent |
|---|---|---|---|---|---|
| Vercel signal gates | `signals.json` metrics, project/usage facts, and codebase findings (`lib/gates/index.mjs:16-37`; individual inputs in `phase2_answers.md`) | Gate modules return candidate arrays; hard-gate stage separates `allowed` and `gated` (`lib/gates/hard-gates.mjs:16-35`; `scripts/gate-investigations.mjs:46-63`). | Gate functions have no process exit code. CLI wrapper exits 1 on thrown failure; its usage/invalid input paths exit 1 or 2 (`gate-investigations.mjs:23,121,164-165`). | None found. | Hard exclusions for Vercel Flags/workflow routes; missing required method-share data disqualifies an uncached-route candidate; six-code-candidate default budget (`hard-gates.mjs:3-14`; `uncached-route.mjs:20-43`; `index.mjs:40-44`). |
| Taste page gate | Local HTML/URL, page-loaded files, browser/consistency/layout results, optional `waivers.json` (`scripts/gate.mjs:300-321,550-580`). | `PASS`, `FAIL`, `OPEN`, `QUICK`, `OFF`, `DONE`, `ERROR`, `SETUP` (`gate.mjs:63-68,813-891`). | 0 PASS/OFF/DONE (and QUICK with no finding); 1 FAIL/OPEN (and QUICK with findings); 2 ERROR; 3 SETUP (`:68,814,833,870,891`). Hook mode emits `block`/`continue` JSON and uses exit 0 (`:71-72,687`). | At most five exact check/target/reason waivers; `kit-edited` and `checker-gaming` cannot be waived (`:47-53,555-580`). | Explicit OPEN after configured rounds; not-checked/crashed checks cannot yield PASS; `--done` records the user's stop; gate documentation says it never traps an agent (`:55-72,819-833,870-891`). |

## 3. Anti-fabrication / evidence standards

| Mechanism | Required evidence | Rejection/repair path | Main limit |
|---|---|---|---|
| Vercel claim verification | Structured claims for citations, files, patterns, framework/version, project config, and cache safety (`lib/extract-claims.mjs:1-63`). | Verify → sanitize → re-extract/re-verify → grade; contradictions, unsafe cache claims, low score, or review flags withhold the recommendation (`scripts/verify-and-regen.mjs:95-215,236-267`). | Static checks are deliberately high-precision/low-recall; a `verified` disposition only proves the encoded check, not every natural-language assertion (`extract-claims.mjs:1`). |
| Vercel sanitizers/grader | Sanitizer trail; citations must survive allowlist/version checks; four scored axes (`lib/sanitizers/index.mjs:31-58`; `lib/grade-recommendation.mjs:13-25`). | Rewrite/drop unsafe content; missing citation drops; <0.55 score drops; failed safety checks trigger regen (`recommendations.md:121-140,171-184`). | `recommendations.md` says “12 sanitizers” and “Average”; the code has 11 modules in `SANITIZERS` plus separate dollar/citation/missing-citation operations and a weighted score. |
| Taste waivers | Exact check ID, target, reason (minimum 12 characters); one finding per waiver, maximum five (`scripts/gate.mjs:47-53,555-580`). | Invalid, unmatched, broad, excess, or non-waivable entries are ignored or become failures; waivers are printed in the report (`:555-580,792-800`). | Waiver syntax adjudicates a false positive; it does not prove a finding false. The gate therefore retains explicit reasons and exact targets. |

## 4. Verified contradictions

| Source A | Source B | Contradiction |
|---|---|---|
| `composition-patterns/AGENTS.md:38-48` | `composition-patterns/rules/architecture-avoid-boolean-props.md:2-5` | Architecture section is HIGH; its Boolean-prop rule is CRITICAL. |
| `react-native-skills/SKILL.md:67` | `react-native-skills/rules/_sections.md:54-58`; `rules/ui-pressable.md:2-5` | UI Patterns is HIGH, the UI section is MEDIUM, and the sample Pressable rule is LOW. |
| `vercel-optimize/references/recommendations.md:119-136,171` | `vercel-optimize/lib/sanitizers/index.mjs:15-22,31-58`; `lib/grade-recommendation.mjs:13-25` | Sanitizer inventory is stale relative to code, and documentation calls the grade an average although implementation uses weighted axes. |

Other explicit Wings conflicts: runtime-fetching guideline skills (`web-design-guidelines/SKILL.md:18-25`, `writing-guidelines/SKILL.md:18-25`), Vercel CLI/account requirements (`vercel-optimize/SKILL.md:22-24`), external/unpinned deployment commands (`deploy-to-vercel/SKILL.md:162-176`), and CRITICAL/HIGH rule labels do not meet the no-runtime-fetch/no-required-CLI/P0-P3 Wings decisions. These are conflicts, not recommendations to revisit those decisions.

## 5. Ten items worth carrying into a stdlib-only lint/gate toolkit

1. **Validate stable global IDs and severity separately from confidence.** Wings contract; upstream rule catalogues show why normalization matters (`react-native-skills/SKILL.md:31-44`; `composition-patterns/rules/_sections.md:8-29`).
2. **Check frontmatter shape, required keys, directory/name agreement, and description form.** Mechanical input is already captured in `phase0_inventory.part01.csv` and `part02.csv`.
3. **Resolve local Markdown links and `references/` paths.** Verified broken relative references include `core/execution-policy.md:18` and generated Vercel AGENTS links.
4. **Flag invisible Unicode control/format characters.** Phase 0 found one hit; the scan needs exact code-point and file-start BOM handling (`phase0_flags.part01.csv`).
5. **Detect runtime network/CLI/unpinned-exec patterns, but distinguish commands from prose and examples.** `phase0_flags.part01.csv` and `part02.csv`; guideline URLs and `npx ...@latest` are verified examples.
6. **Require an explicit gate input/output contract and finite verdict vocabulary.** Vercel `candidate/gated/disqualified` versus taste `PASS/FAIL/OPEN/...` (`gates/hard-gates.mjs:16-35`; `taste-skill/scripts/gate.mjs:63-68`).
7. **Make incomplete checks unable to report PASS.** Taste gate records not-checked/crashed states (`gate.mjs:819-833`).
8. **Use narrowly targeted, reasoned waivers with caps and unwaivable safety checks.** Taste gate (`gate.mjs:47-53,555-580`).
9. **Verify structured claims locally before accepting prose recommendations.** Vercel `extract-claims.mjs`, `verify-claim.mjs`, and `verify-and-regen.mjs:95-160`.
10. **Keep audit trails and make weights/thresholds explicit and machine-checkable.** Sanitizer trail (`lib/sanitizers/index.mjs:31-37`) and weighted grade (`lib/grade-recommendation.mjs:13-25`).

## 6. Not fully opened or truncated

- `taste-skill/scripts/consistency.mjs` is 1,015,117 bytes / 11,485 lines. Its complete check-ID and named-policy-threshold inventory is recorded in `phase4_missing_sources.md`, section 3; selected implementation probes and the report/runtime paths were inspected. The implementation was not read line by line, so low-level branches and every internal comparator are not audited. `taste-skill/assets/**` was intentionally not opened.
- `react-best-practices/AGENTS.md` is 108,261 bytes / 3,810 lines; only head/tail were reviewed. Do not treat it as fully analyzed.
- All taste-skill Markdown reference files listed in the earlier version of this section were subsequently opened, including `references/effects-creative.md`, `photos.md`, and `sections-library.md`; selected evidence is in `analysis/phase4_missing_sources.md`. This does not imply a semantic audit of every referenced implementation or the excluded `assets/**`.
- Taste-skill scripts not substantively reviewed: `scripts/copy-lint.mjs`, `effects.mjs`, `icons.mjs`, `moments.mjs`, `photos.mjs`, `shoot.mjs`, `start.mjs`; `library/palettes.json`, `library/type.json`. `perf.md`, `gate.mjs`, and `perf.mjs` were inspected; the script inventory is not a full semantic audit.
- Mobile variant files not substantively reviewed: `flutter/snippets.md`, `flutter/api-template.dart`, `react-native/snippets.md`, `react-native/api-template.ts`, `swift-ios/snippets.md`, `swift-ios/api-template.swift`. Stack manifests and tech-stack references were inspected.
- Vercel Optimize support-topic samples read: `astro-edge-middleware-scope.md`, `astro-output-mode-and-isr.md`, `auth-preserving-parallelization.md`. Other filenames (not opened): `bot-protection-product-guardrails.md`, `build-minutes-monorepo-fanout.md`, `cache-components-static-shell-boundaries.md`, `cache-components-suspense-dedupe-pitfall.md`, `cdn-cache-auth-safety.md`, `cold-start-initialization-bundle.md`, `core-web-vitals-client-bottlenecks.md`, `database-egress-pooling-region.md`, `dynamic-rendering-traps.md`, `external-api-critical-path-platform.md`, `external-api-critical-path.md`, `fast-data-transfer-payloads.md`, `fluid-compute-caveats.md`, `function-duration-io-and-after.md`, `function-invocation-reduction.md`, `function-region-misconfiguration-ttfb.md`, `image-optimization-cost-control.md`, `isr-revalidation-static-generation.md`, `middleware-proxy-edge-cost.md`, `next-fetch-revalidate-floor.md`, `next-font-cls-self-hosting.md`, `next-heavy-ui-lazy-load-boundaries.md`, `next-image-lcp-preload-sizes.md`, `next-route-handler-get-cache-defaults.md`, `next-script-third-party-strategy.md`, `nextjs-version-cache-semantics.md`, `not-found-catchall-request-waste.md`, `nuxt-route-rules-cache-isr.md`, `observability-events-cost-attribution.md`, `post-response-work-waituntil.md`, `route-error-durable-offload.md`, `route-error-runtime-limits.md`, `runtime-cache-reusable-data.md`, `sveltekit-isr-prerender-safety.md`, `sveltekit-split-cold-start-tradeoff.md`, `usage-spike-triage.md`, `use-cache-date-stamp-isr-write-amplifier.md`, `use-cache-remote-shared-origin-data.md`, `workflow-resumable-stream-routes.md`.
- Vercel Optimize playbook samples read: `ai-application.md`, `api-service.md`, `content-site.md`. Other filenames (not opened): `marketing.md`, `saas.md`, `sveltekit.md`, `ecommerce.md`.
- Vercel Optimize scripts read for this dossier: `collect-signals.mjs`, `gate-investigations.mjs`, `verify-and-regen.mjs`; other `scripts/*` were mechanically inventoried but not substantively reviewed.
- The original scope excluded `affaan-m-ECC/**`; the separately requested ECC paths are examined in `analysis/phase4_missing_sources.md`. No candidate script was executed and no source file was modified.
