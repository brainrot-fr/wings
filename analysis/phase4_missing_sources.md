# Phase 4: Supplemental Review of Previously Missing Sources

This supplement covers the omissions later named by the user. The original source scope excluded `affaan-m-ECC/**`; only the specific ECC paths listed below are included here. No candidate script was executed, and no source file was modified.

## 1. Vercel licenses and remotely fetched rule text

- The local `skills/vercel-labs/web-interface-guidelines/LICENSE` begins with MIT License and identifies Copyright (c) 2025 Vercel Labs (`:1-4`).
- The live `writing-guidelines` repository's `main/LICENSE`, fetched as raw text in this review, also identifies MIT License and Copyright (c) 2026 Vercel Labs (`https://raw.githubusercontent.com/vercel-labs/writing-guidelines/main/LICENSE`, `:1-4`). Its rule source is `https://raw.githubusercontent.com/vercel-labs/writing-guidelines/main/command.md`.
- The Web Interface Guidelines rule source is `https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md`. Both URLs use mutable `main`; no commit or release was pinned. The skills fetch these rule files at runtime, as already evidenced in `phase2_answers.md` section e.
- No LICENSE file was found beneath `new candidates/vercel-labs-agent-skills/` or the local `skills/vercel-labs/` tree except the Web Interface Guidelines license above. Fetching `https://raw.githubusercontent.com/vercel-labs/agent-skills/main/LICENSE` returned HTTP 404. This is not proof that all Vercel skill content has the same license as the Web Interface Guidelines.

## 2. Taste references subsequently opened

Paths in this section are under `new candidates/Leonxlnx-taste-skill/skills/taste-skill/`.

The previously listed taste reference Markdown files were opened. Two direct operational findings:

- `references/photos.md:12-25,75-90,106-117` documents bundled-library and Wikimedia/Unsplash sources, plus a live Wikimedia search and a `photos.mjs fetch` step. These are build-time asset workflows; they are not browser runtime fetches. The search/fetch workflow still requires network access when used, so it is not an offline-required workflow without a bundled/local-asset fallback.
- `references/effects-creative.md:123-145` specifies baking a map JSON at build time with one request to an OpenStreetMap Overpass server. It is not a runtime map request, but the bake step is network-dependent. The same file calls the four-live-WebGL-context cap a house rule and sets a per-pixel workload budget (`:35-56`).
- The references include detailed, internally specified design constraints; they are source material, not published standards. Examples include at most four live WebGL contexts and a 1.5-megapixel cap (`effects-creative.md:39-56`).

## 3. `consistency.mjs`: completed check and named-threshold inventory

The file is 1,015,117 bytes / 11,485 lines. I read its complete embedded rule overview (`scripts/consistency.mjs:1-280`), the check declarations and summaries for all seven modules (`:294-4499`), the runtime setup and scanner (`:4499-4650,546-618`), and the report/exit path (`:11350-11485`). I also statically compared the declared module IDs with the report registry. The candidate script was not run and no page was supplied. This completes the inventory of declared checks and thresholds stated as rules; it is not a line-by-line audit of every low-level geometry predicate.

### Complete check-ID inventory

The main ordered set has 98 IDs (`:10192`): `assets`, `shader-lint`, `gl-fallback`, `empty-visual`, `hero-fill`, `flush`, `placeholder`, `sample-label`, `caption`, `credit-wall`, `nav`, `nav-covers`, `spill`, `off-viewport`, `fold-card`, `hover-spill`, `overlap-text`, `row-gap`, `cut-text`, `fold-cut`, `marquee`, `scroll-linked`, `scroll-reveal`, `pinned`, `loop-pause`, `reduced-motion`, `webgl`, `no-visual`, `text-only`, `card-visual`, `hidden-visual`, `card-family`, `card-layout`, `nesting`, `effect-repeat`, `ui-fit`, `ui-centre`, `dark-ground`, `button-styles`, `button-shape`, `same-action`, `button-picture`, `cta`, `pricing-tiers`, `copy-headline`, `copy-fact`, `copy-headings`, `copy-buttons`, `copy-actions`, `heading-scale`, `stagger`, `top-stagger`, `off-grid`, `col-edge`, `right-edge`, `centre-axis`, `tilt`, `contrast`, `text-contrast`, `body-size`, `busy-ground`, `section-gaps`, `proximity`, `hole`, `links`, `forms`, `photo-upscale`, `photo-set`, `photo-credit`, `nav-family`, `nav-labels`, `link-styles`, `heading-align`, `label-centre`, `fake-button`, `stranded-action`, `orphan`, `unit-break`, `tab-wrap`, `effects-fit`, `fade-cut`, `photo-weight`, `copy-length`, `nav-current`, `progress-bar`, `photo-repeat`, `button-contrast`, `photo-print`, `grounds`, `split-align`, `fact-agree`, `fold-action`, `action-count`, `one-screen`, `hover`, `product-shown`, `same-object`, `font-load`.

The modules declare 43 further unique IDs (`:353-355,1353-1358,1815-1822,3365-3368,3486,3766,3982-4001`):

| Module | IDs |
|---|---|
| `visuals` | `visual-caption`, `visual-empty`, `effect-kind`, `hero-enter`, `moment-none` |
| `address` | `street-number`, `postcode`, `coordinates`, `company-number`, `phone-number` |
| `rhythm` | `hero-screen`, `section-height`, `section-air`, `one-section`, `one-heading`, `container-edges`, `row-lines`, `split-pair` |
| `motion-hooks` | `motion-layer`, `count-text`, `loop-cycle` |
| `tiles` | `section-tile` |
| `area` | `empty-area` |
| `basics` | `a11y-name`, `img-alt`, `field-label`, `heading-order`, `tabindex`, `focus-ring`, `focus-visible`, `focus-hidden`, `skip-link`, `menu-toggle`, `lang`, `page-meta`, `share-meta`, `action-repeat`, `map-link`, `open-now`, `assumed`, `run-on`, `form-fields`, `form-send` |

### Named policy thresholds and their status

| Check group / metric | Stated threshold or decision | Source status |
|---|---|---|
| Visual eligibility and emptiness | Visual at least 120x80px; fewer than 6 significant colours warns/fails; 99.8% one colour fails, canvas/mount at 98%; detail below 0.2% with 6+ colours is treated as smooth-gradient-only; candidate images past first 40 are not shot | House heuristics / implementation caps; `:307-312,402-404,691-698,757,964` |
| Caption detection | Caption-like line within 32px; muted line at most 2 rows, 15px or smaller, up to 180 chars; visual at least 120x80px; overlay caption in lower half | House heuristic; `:294-316,800-807` |
| Main visual and cards | Three or more text-only cards; 4+ same-layout cards fail; card layout in more than two sections fails; fewer than three placements or one ground warns | House heuristics; `:47-52,9500-9508` |
| Navigation and controls | Nav/content gap over 24px fails; tablet menu can fail with at least 240px unused; hero permits 2 actions; more than 10 distinct labels warns; same main action on 5+ controls warns; filled-button contrast below 1.3:1 warns | House heuristics; `:39-46,106-109,10345-10347,9605-9608,10480-10485` |
| Typography and copy | Body text 7:1; other plain-ground text 4.5:1; large type 4.5:1 / 3:1; under 16px running text warns; display heading at 22+ words or 4+ lines warns; tech/software copy over about 80 words per screen or 90 in a section warns | Mixed: contrast values are WCAG-aligned but not attributed to a criterion at the implementation; 7:1 is stricter than AA. The size and copy cutoffs are house heuristics; `:67-68,103-109,248,7835-7853,9618-9639,10569-10602` |
| Phone targets and focus | 44px target height is preferred; below 32px high or 24px wide fails if another target is under 8px away, otherwise undersized targets warn; focus-visible under 3:1 fails | The code explicitly names WCAG 2.5.8's 24px target-size criterion; 44/32/8 and focus contrast are local rules in this file, not cited there; `:260-263,3989,6198-6227,4474-4484` |
| Screen/rhythm geometry | Main rhythm widths 1440x900, 768x1024, 390x844; hero fold tolerance 1px; sections one/two screens with 2px pass and 3-8px warn; section air 128-480px desktop / 112-420px phone, with 64-600 / 56-560 warn bands; content fill 55% pass / 40% warn; next-section peek 8px pass, 24px warn; place page under 3 screens warns, 3-6.05 passes, 6.05-7 warns, over 7 fails | House rules; `:1757-1822,2399-2454,2476-2513,2584-2603` |
| Container/section layout | Desktop margins 64-120px, phone 16-24px; 24px column gap; desktop split column line k=5, 6, or 7 (place k=6); tiles allow 24px from a one/two-screen height; empty area >35% warns and >50% fails | House rules; `:1766,1815-1822,2662-2668,2972-2978,3482-3491,3766-3770` |
| Empty-area method | Section padding counts as air up to 12% of a screen per side; content boxes grow 20px; 16px grid cells; a low-coverage run is counted when at least 25% of a screen tall; thresholds are >35% warn and >50% fail | House algorithm and thresholds; `:3760-3774,3812-3853,3890,3930-3936` |
| Effects and motion | More than 4 live WebGL contexts fails; >8 total created warns; second big scene or effect-ground beside the one big scene fails; >2 scroll moments warns; particles warn (300+ canvas 2D shapes/s is explicitly called out); loops >4s fail / <2.5s warn; 5s after appearing, continuing motion without pause fails; reduced-motion animation still moving after 1.5s fails | House rules; effect-kind separately labels >4 contexts a WARN on allowed page kinds, but `webgl` is the FAIL and same-fault handling suppresses the duplicate; `:45-46,1214-1226,3368-3440,10985-11005,11079-11124` |
| Image loading/performance | Simulated 1.6 Mbit/s, 400ms latency, cache disabled; frame still empty after 1s; over 400KB, over 4x CSS display width (twice a retina width), or still missing after 3.5s fails, otherwise warns | Test and thresholds are house budgets; no published performance source cited; `:138-139,9810-9865` |
| Product imagery and repetition | Product under 60% of hero content width fails; 60-80% warns; photo at 3x drawn width without `srcset` warns; same whole object in 4+ sections warns | House heuristics; `:195-199,9636-9647` |
| Credits, links, facts | Credit wall at desktop (1000px+) is more than one line/block; narrower threshold includes >220 chars or five lines; footer with >2 photo-credit links fails; nav dropdown with 3+ entries sharing a target warns; action/claim checks also flag repeated actions and inconsistent opening hours | House heuristics; `:100-104,214-216,9552,8584,9605-9608` |
| Source scan and report ceilings | Same-origin scan: 3MB/file, 6 simultaneous reads, 400 files, 20s; visual scan takes first 40 candidates; the visual block caps at 8 findings per width, rhythm caps at 40 crops per width, and the host caps at 80 crops per walked width | Operational caps, not product quality standards; `:546-618,324,757,3184,10200-10205` |

The source comments mention 15-site and 44-site observations, but the sample data/methods are not included here; those observations do not make the chosen cutoffs independently reproducible (`:113-114,194-199,244-263`). Apart from its explicit WCAG 2.5.8 mention for 24px target size (`:6198-6199`), this file does not cite a standard for its thresholds. The original task's separate `perf.mjs` inventory remains in `phase2_answers.md`; it is not folded into the table above.

### Execution, network, omissions, and output

- Runtime: Node 22+ (built-in `WebSocket`) plus a local Chrome, Edge, or Chromium binary; no npm package is imported. It starts Chrome using `child_process.spawn`; Windows cleanup uses `spawnSync taskkill` (`:1-9,4600-4650`). This is not a stdlib-only gate and requires the browser binary.
- A URL target is loaded by Chrome. The static scanner uses `fetch` on same-origin scripts/styles/imports/embedded pages, bounded by the caps above; external origins are recorded but are not read by that scanner (`:546-618`). Shader inspection separately fetches same-origin shader assets (`:9730-9744`). A file target is served from a loopback HTTP server. The checker writes `report.json`, `rendered.html`, and image crops; it removes matching prior crop JPEGs in its output directory (`:4567-4597,10203,10252,11455`).
- Forms are tested only for a local page; remote forms are explicitly marked not checked (`:11084-11086`). On the local form pass, CDP `Fetch` interception is enabled to fulfill requests without sending them (`:11088-11100`). **Fail-open caveat:** the `Fetch.enable` error is swallowed and the pass continues to submit (`:11094`); static reading therefore does not establish that the “every request held” promise is upheld if interception setup fails. This was not exercised.
- Default widths are 1440, 1024, 820, 768, 390; the extra first-screen sweep is 1280, 1152, 1024, 896, 768. A 320x640 narrow pass runs by default when a phone width is requested. Rhythm runs only at its configured widths (default 1440, 768, 390); motion-hooks only at widths >=700 (`:1858,4506,4526,4546-4547,3360-3368`).
- `--quick` skips scroll stepping/reveal walk, hover, loop, forms, and reduced-motion checks, and lists omissions. It does still call `hiddenWalk` with scripts disabled and reduced motion unless `--no-hidden` (`:11354-11356,11396-11404`). The overview's claim that quick skips the “hidden-content” pass (`:272-275`) is therefore broader than the implementation; only the dead-IntersectionObserver walk is omitted in quick mode. Explicit `--no-*`, absent configured widths, remote forms, and probe failures add `notChecked` entries (`:4531-4533,11357-11430`).
- Widths with no successful screen after one retry are incomplete and exit 2; findings exit 1; clean runs exit 0 (`:11365-11375,11441-11485`). The `not checked` state is distinct from PASS in report aggregation (`:11447-11458`).

### Verified reporting defect

The 43 module IDs above are all absent from the 98-item `ORDER` (`:4499,10192`). Final per-check status generation iterates only `ORDER` (`:11449-11458`). Therefore findings and aggregate FAIL/WARN counts can include module results, but `report.checks` omits their per-ID statuses. This contradicts the overview's promise of a table of every check (`:13-17`) and is a static, verified defect. No report was generated to test the runtime output.

Other numeric distinctions verified in code: the loop summary says 2.5-4s, while the implementation's effective cutoffs are `<2.45s` WARN and `>4.05s` FAIL (`:3439-3440`); the 50ms bands are accepted without a finding. For effects, the module emits a WARN above four live contexts in its applicable branch (`:1214`), while the host separately emits a `webgl` FAIL above four (`:11122`) and suppresses the matching module finding when the host finding exists (`:10211-10213`).

## 4. ECC: the explicitly requested files

### GateGuard pre-tool hook

`skills/affaan-m/ECC/scripts/hooks/gateguard-fact-force.js` is a CommonJS Node `PreToolUse` hook. It imports local helpers plus Node `crypto`, `fs`, and `path` (`:1-77`); the hook file has no `child_process` or network import. The optional full-package note says `pip install gateguard-ai` (`:21-22`), but that package is not required by the shown hook imports.

- `Edit`, `Write`, `NotebookEdit`, `MultiEdit`, `Bash`, and `PowerShell` are routed; other tool names pass through (`:2453-2484`).
- First-touch file edits can be credited by prior search evidence, allowed as profiled trivial changes, collapsed as same-turn sibling files, or denied with a fact-finding prompt. Sensitive/restricted targets do not receive ordinary credits; per-session state tracks checked files and denial counts (`:1818-1840,2137-2187,2544-2580`).
- Destructive shell commands are classified for Bash/PowerShell; the first attempt requests a target list, rollback line, and verbatim user instruction, and the same command hash passes on retry (`:1544-1564,2157-2170,2698-2710`). The routine shell gate allows read-only commands and asks for facts before the first other command in a session (`:2711-2745`).
- The gate can be disabled through environment variables (`:1563-1568,2471-2473`). Parse failure returns the original input; state persistence failure allows the operation to avoid a retry loop (`:2463-2470,2226-2234`). These are explicit fail-open paths, not fail-closed enforcement.
- The main hook file was reviewed, not every lazily loaded GateGuard helper. This report therefore does not claim that all sibling modules are shell/network-free.

### Host compatibility validator

`skills/affaan-m/ECC/scripts/ci/validate-skill-host-compat.js` statically checks Claude-only substitutions in executable bash/sh/zsh fences in Codex/Cursor projections, Codex frontmatter allowlist, missing copies listed by `agents/openai.yaml`, copy-name mismatches, and a canonical CONTRIBUTING checklist (`:3-25,34-57`). Errors in the first three classes fail by default; checklist findings are warnings unless `--strict-checklist` (`:17-20,57-82,320-370,405-435`). It requires Node and local filesystem access only; no external CLI binary is invoked. Missing `skills/` is a successful skip, and `--inventory` intentionally exits successfully (`:25-26,337-353,445-475`).

### Eval-harness core and CLI defect

- `canonical.js` provides recursively sorted canonical JSON and SHA-256 helpers (`scripts/lib/eval-harness/canonical.js:10-47`).
- `capsule.js` implements a local NDJSON journal with sequence numbers, predecessor hashes, canonical JSON checks, truncation/tamper detection, and deterministic projection; export copies only capsule metadata, journal, and projection (`scripts/lib/eval-harness/capsule.js:1-10,248-314,316-405`). Its comment explicitly notes that a hash chain cannot stop an operator replacing the entire log (`:7-10`).
- `envelope.js` defines five lineages, effect classes, a typed payload allowlist, and secret canaries. Invalid or unallowlisted data is rejected/dropped before persistence (`scripts/lib/eval-harness/envelope.js:14-82,96-148,150-232`).
- The CLI statically requires `./lib/eval-harness` (`scripts/eval-harness.js:24`) and calls `harness.capsule`, `harness.retrospective`, `harness.gate`, and `harness.receipt` (`:65-120`). The directory `scripts/lib/eval-harness/` contains only `canonical.js`, `capsule.js`, and `envelope.js`; there is no `index.js`, `package.json`, or sibling `scripts/lib/eval-harness.js`. Thus standard Node directory resolution cannot resolve that `require`, and the CLI cannot reach its advertised commands as checked in. This is a static finding; the CLI was not run. Its own comment also says gate execution is unavailable pending isolation (`:16-17,96-99`).

## 5. wshobson adapters and Addy skill linter

### wshobson

The local `skills/wshobson/agents/tools/adapters/` directory contains `base.py`, `capabilities.py`, and `opencode.py`. The specifically named `skills/wshobson/agents/tools/generate.py` is absent from the workspace; no other adapter files are present in that directory.

- `base.py` is standard-library Python. It reads plugin JSON and skill/agent/command files, parses a constrained YAML-like frontmatter subset, and models sources as dataclasses (`:1-9,41-160,340-447`).
- `HarnessAdapter.write` and `write_bytes` resolve targets and refuse writes outside the configured output root; `mirror_file` preserves binary references (`:507-574`).
- `capabilities.py` centralizes per-host capability flags and tool-name rewrites (`:1-52,55-165,215-260`); `opencode.py` emits native OpenCode skills/agents/commands and maps source tools to permission blocks (`:1-18,54-113,168-239`).
- These are adapter mechanisms, not a standalone no-CLI skill suite: discovery assumes `plugins/`, and emitted output is OpenCode-specific. The missing generator means no complete generation entrypoint was verified.

### Addy `skill-lint.js`

`skills/addyosmani/agent-skills/scripts/lib/skill-lint.js` is a reusable Node module that depends on built-in `fs` and `path` only (`:20-21`). It checks frontmatter keys/name, description length (1024 chars) and trigger, required sections, line budget, dead cross-references, directory layout, and persona structure (`:31-83,349-452,512-628`).

- Required headings are Overview, When to Use, Common Rationalizations, Red Flags, and Verification; it does not require the Wings-mandated Process heading (`:75-81`).
- It accepts “Use before/after/during” in addition to “Use when” (`:59-70`), which is broader than the Wings description contract. The 500-line limit is a warning, not a blocking error (`:33-38,446-454`).
- The author explicitly says its frontmatter handling is not a YAML implementation and lists the narrow invalid forms it catches (`:188-216,250-338`). Reuse its separation of pure content lint from filesystem wrappers, but do not assume complete YAML parsing.

## 6. Status and remaining incompleteness

- The taste reference omission is superseded by this review. `consistency.mjs` now has a complete declared-ID and named-policy-threshold inventory in section 3; its low-level implementation was not audited line by line.
- The GateGuard main hook was inspected, but not all local helper modules. ECC host validator and three eval-harness core modules were opened; the eval-harness CLI's missing module entrypoint remains a verified static defect.
- `tools/generate.py` is absent in this workspace; Vercel agent-skills root license was not available at the checked URL. Remote `main` rule text is mutable and unpinned.
- No candidate script was executed and no source file was modified.
