# Packaging

Six packaging cards are within the eight-card cap: Agent Skills, Addy, Superpowers, Spec Kit, Pulumi, and Sentry. Evidence is limited to the carded files; three broad candidates remain catalog-only.

## RANKED CANDIDATES
1. [Agent Skills standard and validator](../packaging/agentskills__agentskills.md) — precise portable `SKILL.md` format, with documented validator gaps.
2. [Pulumi Agent Skills](../packaging/pulumi__agent-skills.md) — same skill roots exposed through multiple marketplaces and a generated Gemini archive.
3. [Addy Agent Skills](../packaging/addyosmani__agent-skills.md) — several manually maintained adapters with CI checks for version and command drift.
4. [GitHub Spec Kit](../packaging/github__spec-kit.md) — shared templates rendered through 44 registered integration keys.
5. [Superpowers](../packaging/obra__superpowers.md) — broad native packaging, including a dual-generation OpenCode runtime.
6. [Sentry Skills](../packaging/getsentry__skills.md) — minimal Claude marketplace with a symlinked local skill mirror.

## COMPARISON MATRIX
| System | Source of truth / targets | Generation and validation | Versioning / install |
|---|---|---|---|
| Agent Skills | `SKILL.md` directories; no adapters mandated | `skills-ref` validates only part of documented constraints | Tool-neutral format; reference CLI is Python, version 0.1.0 |
| Addy | Shared skills plus Claude, Gemini, Antigravity, Codex, Copilot metadata | Wrappers are hand-authored; CI checks five manifest versions, command descriptions/presence and artifact paths | All checked manifests at 0.6.15; marketplaces and `npx skills` |
| Superpowers | `skills/`; Claude, Codex, Cursor, Antigravity, Devin, Kimi, Muse, OpenCode | OpenCode dynamically loads skills; shell/Python tests cover several manifests and runtime | 7.0.2; `.version-bump.json` enumerates 12 fields; Git-backed plugins |
| Spec Kit | Python `IntegrationBase` adapters, shared process templates | Renders per-host files; tracks project-owned outputs; external archives require descriptor and consent | CLI ships adapters; release tag/PyPI. External adapters are independently versioned |
| Pulumi | Four skill groups exposed through Claude/Codex/Cursor/Gemini and skills CLI | Gemini tarball built from the Claude manifest; tests check references, skills and archive | Versions differ by target (`2.0.8` Claude vs `2.0.7` Codex/Cursor) |
| Sentry | Root `skills/` and `agents/`; Claude marketplace and `.agents/skills` symlink | No manifest validator or test/workflow suite found in checkout | Manifests have no version; GitHub marketplace or skills CLI |

## CONFLICTS
- The Agent Skills standard defines content and metadata, not client discovery, installation, authorization or lifecycle hooks. `allowed-tools` is experimental and not a portable permission contract. (`agentskills__agentskills.md`)
- Addy's README documents OpenCode use, but this checkout has no `.opencode` adapter/command files; Superpowers instead ships a sizeable V1/V2 plugin runtime.
- Pulumi has different root Claude/Codex/Cursor version values; Gemini derives its version from Claude. Do not silently assume these are synchronized.
- Spec Kit's `.specify/integration.json` is project state and file-ownership tracking, not an Agent Skills marketplace manifest.
- Sentry's README gives a domain-plugin example, but only root Claude plugin/marketplace manifests are present in this checkout.
- Superpowers version configuration includes multiple targets; its runtime tests are not evidence of manifest schema validation. No workflow directory was found.

## QUESTIONS ANSWERED
- **Mechanism and coverage:** Agent Skills standardizes `SKILL.md`; Addy and Pulumi add native plugin metadata; Superpowers adds native adapters; Spec Kit registers 44 keys (42 named agents plus `none` and `generic`); Sentry has Claude marketplace plus a universal skills CLI path. (`agentskills__agentskills.md`; `README.md:L355-L368` in Addy card; `docs/integrations/index.md:L76-L126`; Pulumi and Sentry packaging cards)
- **Generation and loss:** Addy wrappers are authored separately and validated for name/description parity, not prompt-body equality. Spec Kit renders shared templates into host-specific formats and tracks ownership. Pulumi generates three Gemini archives from its combined plugin's skill roots; `skills` CLI installs each group separately. Sentry's `.agents/skills` is a symlink; it does not generate another copy. (Addy `scripts/validate-commands.js:L1-L15`; Spec Kit `docs/integrations/api.md:L49-L70`, `L295-L330`; Pulumi `scripts/build_gemini_extension.py:L14-L61`; Sentry `README.md:L100-L118`)
- **Manifest validation:** `skills-ref` checks a subset of its spec. Addy CI validates a five-manifest version set, command parity/descriptions and artifact paths. Pulumi tests Claude/Codex/Cursor manifests, referenced paths, marketplace entries and Gemini archives. Superpowers uses host-specific tests and a version-bump registry. Spec Kit validates trusted external adapter archives/descriptors; built-ins are shipped as code. No Sentry manifest test was found. (Each linked packaging card)
- **Versions/releases:** Agent Skills reference tool `0.1.0`; Addy manifests `0.6.15`; Superpowers `7.0.2`; Spec Kit follows CLI tags/PyPI; Pulumi has the noted host skew and derives Gemini version from Claude; Sentry manifests omit version. Version facts are from checked-in manifests/docs, not a check of the latest upstream release.
- **Install footprint and hooks:** Marketplace/skills CLI installs for Addy, Pulumi and Sentry fetch hosted repository content; Superpowers OpenCode is Git-backed and Cursor/Muse invoke a local session-start hook. Spec Kit external adapters can download and import Python only after trust authorization. No installation, adapter execution or release workflow was run. (Addy `README.md:L48-L88`; Superpowers `.opencode/INSTALL.md:L7-L33`, `hooks/hooks-cursor.json:L1-L8`; Spec Kit `docs/integrations/cli.md:L90-L131`)
- **Comparison to the SKILL.md standard:** The standard is the cleanest portable content contract. Native marketplaces improve discovery and install UX but add per-host metadata, validation and version drift; Spec Kit is a different rendering/management system rather than a direct skills format.

## GAP EVIDENCE
- **wshobson/agents:** filename-filtered packaging inventory found 150 candidates / 7,812 lines; the Makefile, adapter generators and every manifest were not read.
- **EveryInc/compound-engineering-plugin:** 99 filename-filtered candidates / 5,991 lines; converter CLI target list was not traced.
- **Intense-Visions/harness-engineering:** 89 filename-filtered candidates / 15,692 lines; manifest families were not deep-read.
- Spec Kit coverage is architectural, not a review of all 44 adapter implementations. Sentry has only its two root manifests; no domain plugin manifest was found.
- The candidate inventories are counts from the filename-filtered `find` output, not lines read. Repositories not carded remain skipped in `progress.md`.

## TECHNIQUES WORTH TAKING
1. Separate portable authored content from optional host adapters. (`docs/specification.mdx:L6-L17`)
2. Compare duplicated manifest versions against one explicit source. (Addy `scripts/validate-versions.js:L6-L34`)
3. Validate referenced directories, containment and frontmatter—not only JSON syntax. (Pulumi `tests/test_manifests.py:L16-L98`)
4. Preserve user edits through tracked ownership on install, switch and uninstall. (Spec Kit `docs/integrations/api.md:L295-L330`)
5. Validate metadata parity while treating agent-specific prompt bodies as intentionally distinct. (Addy `scripts/validate-commands.js:L1-L15`)
6. Make grouped plugin bundles explicit and avoid duplicate installation of overlapping skills. (Pulumi `README.md:L77-L89`)
7. Prefer symlinks or shared references to duplicated copies when local tooling needs a second path. (Sentry `README.md:L100-L118`)
8. Require explicit review/consent before importing downloaded executable adapters. (Spec Kit `docs/integrations/cli.md:L114-L131`)

## DO NOT TAKE
Do not treat a valid manifest as proof that a client supports every field; do not silently version-skew adapters; do not claim generated files are synced when only names/descriptions are checked; do not treat a local install manifest as a trust boundary.

## CATALOG
Scores below are shallow relevance estimates from the filename inventory; files were not deep-read.
| Target | Path / line count | One-line status | Score |
|---|---|---|---:|
| wshobson/agents | `research/repos/wshobson__agents` — 150 candidate files, 7,812 lines | Makefile, adapters and manifests not read; exceeds remaining research budget | 3 |
| EveryInc/compound-engineering-plugin | `research/repos/EveryInc__compound-engineering-plugin` — 99 candidate files, 5,991 lines | Converter target list not traced | 3 |
| Intense-Visions/harness-engineering | `research/repos/Intense-Visions__harness-engineering` — 89 candidate files, 15,692 lines | Manifest families not deep-read | 2 |
