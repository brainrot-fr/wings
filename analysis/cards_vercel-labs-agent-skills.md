### new candidates/vercel-labs-agent-skills/skills/vercel-optimize
- Purpose: Diagnose production Vercel cost/performance signals, then verify and grade implementation recommendations.
- Wings block fit: frontend | backend | sdlc
- Maturity: real mechanism
- Core mechanism worth taking:
  - `vercel-optimize/lib/gates/index.mjs:1-37` — composes deterministic gates and explicit hard exclusions.
  - `vercel-optimize/scripts/verify-and-regen.mjs:95-160` — extracts claims, verifies, sanitizes, then re-extracts and verifies.
  - `vercel-optimize/lib/grade-recommendation.mjs:13-25` — weights grounding/evidence above prose specificity/actionability.
- Gotchas/defects found: `references/recommendations.md:119-136,171` disagrees with code's sanitizer set and calls a weighted score an average (`lib/sanitizers/index.mjs:15-22,31-58`; `lib/grade-recommendation.mjs:13-25`).
- Hard dependencies: Node; Vercel CLI v53+, authenticated linked project and network for collection; `rg` for local claim checks.
- Portability: partial — pure gates, scans, verification, and grading work offline with supplied signals; collection is vendor/account-bound.
- Overlap: taste-skill; web-design-guidelines; react-best-practices; deploy-to-vercel.
- Verdict: TAKE-MECHANISM — deterministic evidence gates and sanitizers are the strongest reusable mechanism.
- Confidence in this card: medium

### new candidates/vercel-labs-agent-skills/skills/web-design-guidelines
- Purpose: Review UI files against a remotely fetched Web Interface Guidelines rule set.
- Wings block fit: frontend
- Maturity: vendor-specific
- Core mechanism worth taking:
  - `web-design-guidelines/SKILL.md:17-34` — asks for a target when none is provided and uses concise file/line findings.
- Gotchas/defects found: `:18-25` requires fresh network retrieval from `raw.githubusercontent.com` at every review; conflicts with the no-runtime-fetch decision.
- Hard dependencies: WebFetch/network and a changing remote rules file.
- Portability: partial — output style transfers; the rule source and runtime fetch do not.
- Overlap: writing-guidelines; taste-skill; react-best-practices.
- Verdict: TAKE-IDEAS — keep the terse evidence format but vendor and pin rules locally.
- Confidence in this card: high

### new candidates/vercel-labs-agent-skills/skills/writing-guidelines
- Purpose: Review documentation prose against a remotely fetched writing handbook.
- Wings block fit: sdlc
- Maturity: vendor-specific
- Core mechanism worth taking:
  - `writing-guidelines/SKILL.md:17-34` — requires source text and emits terse, line-specific findings.
- Gotchas/defects found: `:18-25` fetches `raw.githubusercontent.com` on every review, contrary to no-runtime-fetch.
- Hard dependencies: WebFetch/network and mutable remote rules.
- Portability: partial — review format transfers; remote source does not.
- Overlap: web-design-guidelines; shared-core `anti-ai-prose.md`.
- Verdict: TAKE-IDEAS — preserve evidence-grounded review, embed rules locally.
- Confidence in this card: high

### new candidates/vercel-labs-agent-skills/skills/composition-patterns
- Purpose: Apply React composition patterns for stateful and variant-heavy components.
- Wings block fit: frontend
- Maturity: rule catalogue
- Core mechanism worth taking:
  - `composition-patterns/rules/architecture-avoid-boolean-props.md:9-14` — replace boolean-controlled variants with explicit composition.
  - `composition-patterns/rules/architecture-compound-components.md:9-15` — share state through a provider and composable parts.
- Gotchas/defects found: Section severity is HIGH but `architecture-avoid-boolean-props.md:3` labels the same category rule CRITICAL (`AGENTS.md:38-48`).
- Hard dependencies: React; no required CLI or network in the opened skill/rules.
- Portability: partial — component principles transfer, React APIs/examples do not.
- Overlap: react-best-practices; react-native-skills; taste-skill.
- Verdict: TAKE-RULES — useful reusable component rules, with severity normalization.
- Confidence in this card: medium

### new candidates/vercel-labs-agent-skills/skills/react-view-transitions
- Purpose: Implement React View Transition patterns with CSS, Suspense, and Next.js integration.
- Wings block fit: frontend
- Maturity: rule catalogue
- Core mechanism worth taking:
  - `react-view-transitions/SKILL.md:12-28` — relate animations to spatial continuity and order implementation around use cases.
  - `react-view-transitions/references/implementation.md:158-170` — verify each navigation path and fallback.
  - `react-view-transitions/references/css-recipes.md:301-309` — supplies reduced-motion CSS.
- Gotchas/defects found: Skill requires stable React 19.3+ outside Next.js (`SKILL.md:43-46`); availability is framework-version-specific.
- Hard dependencies: React 19.3+ or Next.js bundled React; browser support; no required CLI/network.
- Portability: partial — API and CSS are web-specific; progressive no-animation fallback is described.
- Overlap: react-best-practices; composition-patterns; web-design-guidelines.
- Verdict: SAMPLE-ONLY — specialist API guidance, not a general frontend baseline.
- Confidence in this card: medium

### new candidates/vercel-labs-agent-skills/skills/react-native-skills
- Purpose: Provide prioritized React Native rules for lists, animation, navigation, UI, and configuration.
- Wings block fit: frontend
- Maturity: rule catalogue
- Core mechanism worth taking:
  - `react-native-skills/SKILL.md:31-44` — prioritizes grouped rules for quick routing.
  - `react-native-skills/rules/state-ground-truth.md:8-17` — stores ground-truth state and derives visual values.
- Gotchas/defects found: UI severity conflicts: HIGH in `SKILL.md:67`, MEDIUM in `rules/_sections.md:54-58`, LOW for Pressable at `rules/ui-pressable.md:2-5`.
- Hard dependencies: React Native ecosystem and native platform toolchains for implementation; no skill CLI/network required in opened files.
- Portability: no — native APIs and component rules require React Native.
- Overlap: composition-patterns; react-best-practices; mobile variants.
- Verdict: TAKE-RULES — adapt relevant rules only to a React Native block and reconcile impact levels.
- Confidence in this card: medium

### new candidates/vercel-labs-agent-skills/skills/react-best-practices
- Purpose: Route React/Next.js performance work through prioritized optimization rules.
- Wings block fit: frontend | backend
- Maturity: rule catalogue
- Core mechanism worth taking:
  - `react-best-practices/SKILL.md:23-35` — orders rule categories by impact for task-focused review.
  - `react-best-practices/rules/async-parallel.md:8-17` — parallelizes independent async operations.
  - `react-best-practices/rules/server-parallel-fetching.md:8-20` — uses component composition to remove server fetch waterfalls.
- Gotchas/defects found: `async-parallel.md:2` asserts a 2–10× improvement without a source; `bundle-barrel-imports.md:2-5` generalizes numeric performance claims.
- Hard dependencies: React/Next.js knowledge; no runtime CLI or network for the opened rules.
- Portability: partial — many mechanisms generalize, but Next.js/version-specific rules need gates.
- Overlap: composition-patterns; react-view-transitions; web-design-guidelines.
- Verdict: TAKE-RULES — strong performance catalogue, but validate numeric and framework-version claims.
- Confidence in this card: low

### new candidates/vercel-labs-agent-skills/skills/deploy-to-vercel
- Purpose: Deploy projects to Vercel with preview-first flows and project/link-state checks.
- Wings block fit: packaging
- Maturity: vendor-specific
- Core mechanism worth taking:
  - `deploy-to-vercel/SKILL.md:11,84-100` — defaults to preview and makes production an explicit user request.
  - `deploy-to-vercel/SKILL.md:45-51` — checks link state before commands that can link or prompt.
- Gotchas/defects found: Temporary fallback runs unpinned `npx vercel@latest` (`:162-176`).
- Hard dependencies: Vercel CLI/account or temporary deployment service, network; temporary flow requires npx.
- Portability: no — deployment methods and account state are Vercel-specific.
- Overlap: vercel-cli-with-tokens; vercel-optimize.
- Verdict: TAKE-IDEAS — preview-first and side-effect-aware deployment consent are portable.
- Confidence in this card: medium

### new candidates/vercel-labs-agent-skills/skills/vercel-cli-with-tokens
- Purpose: Run Vercel CLI operations with token-based authentication and project/team scoping.
- Wings block fit: packaging | security
- Maturity: vendor-specific
- Core mechanism worth taking:
  - `vercel-cli-with-tokens/SKILL.md:57-65` — keeps secrets out of command arguments and reads them from environment.
  - `vercel-cli-with-tokens/SKILL.md:108-127` — defaults to preview deployments and scopes team commands.
- Gotchas/defects found: It instructs CLI operations that can create/link projects; those side effects need explicit scope review (`:138-174`).
- Hard dependencies: Vercel CLI, account/token, network; no portable deploy target.
- Portability: no — Vercel token and CLI contracts are vendor-bound.
- Overlap: deploy-to-vercel; vercel-optimize.
- Verdict: TAKE-IDEAS — environment-based secret handling and explicit scope checks transfer.
- Confidence in this card: medium
