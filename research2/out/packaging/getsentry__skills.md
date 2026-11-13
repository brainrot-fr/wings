# getsentry/skills (packaging)
SOURCE: `e94f22214528d69899d09c627b3315ddc3544816` | root `LICENSE`: Apache-2.0
SINGLE SOURCE OF TRUTH: Root `skills/` is canonical for the `sentry-skills` plugin; root `agents/` is also loaded. `.agents/skills` is a symlink to `../skills`, not a generated copy. [V] `README.md:L100-L118`; `.claude-plugin/plugin.json:L1-L7`
AGENT TARGETS:
| Agent/client | Manifest or install path | Mechanism | Generated / loss | Evidence |
|---|---|---|---|---|
| Claude Code | `.claude-plugin/marketplace.json`, root `.claude-plugin/plugin.json` | Marketplace registers `sentry-skills` with source `./` | Plugin loads repo-root `skills/` and `agents/`; sparse checkout must include both | `README.md:L10-L19`, `L100-L118`; marketplace `L1-L20` |
| Skills CLI / compatible agents | `npx skills add getsentry/skills`; root `skills/` | Universal skills installer | Reads canonical skill folders; no per-agent manifest is shipped here | `README.md:L33-L38` |
GENERATION: No adapter generator or copied agent-specific output was found in the checked-in packaging files; the local `.agents/skills` alias is a symlink. README describes domain-specific plugin manifests as a future extension pattern, but this checkout contains only the two root Claude manifests. [V] `README.md:L100-L118`, `L207-L243`
VALIDATION: Both JSON manifests were read. No manifest validator, tests directory, or `.github/workflows` directory was present in the checkout; no command or install was run.
VERSIONING AND RELEASE: Neither root marketplace entry nor root plugin manifest declares a version. The inspected install docs provide marketplace update and skills CLI installation, but no pinned release/update scheme. [V] `.claude-plugin/marketplace.json:L1-L20`; `.claude-plugin/plugin.json:L1-L7`; `README.md:L21-L38`
INSTALL FOOTPRINT: Claude marketplace installation fetches GitHub content; `npx skills add` uses the external skills CLI. No hooks, binary downloads, telemetry or curl-to-shell install appears in these manifests or install instructions. External installers were not run. [V] `README.md:L10-L38`; `.claude-plugin/plugin.json:L1-L7`
PORTABLE ESSENCE: Open-format `SKILL.md` folders are reused directly by Claude Code and other compatible clients; local tooling sees the same content through a symlink.
BAGGAGE: Only Claude Code has a checked-in marketplace adapter; other hosts rely on the skills CLI. The README's domain-plugin example is not present as a checked-in plugin here.
CONFIDENCE: High for the two manifests, symlink layout and documented install paths; no validator or installation was executed.
