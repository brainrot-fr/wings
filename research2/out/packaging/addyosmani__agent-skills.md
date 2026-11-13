# addyosmani/agent-skills (packaging)
SOURCE: `301b02b12bff98e4688e6984af6556802322bbde` | root `LICENSE`: MIT
SINGLE SOURCE OF TRUTH: Shared `skills/` is the portable workflow source; command wrappers and plugin metadata are parallel, hand-maintained adapters. The root README lists skills, agents and references as shared content. [V] `README.md:L355-L368`
AGENT TARGETS:
| Agent/client | Manifest or install path | Mechanism | Generated / loss | Evidence |
|---|---|---|---|---|
| Claude Code | `.claude-plugin/`, `.claude/commands/` | GitHub marketplace plugin; `skills` + commands | Manifest points at shared content; wrapper syntax and hooks are host-specific | `.claude-plugin/marketplace.json:L1-L20`; `.claude-plugin/plugin.json:L1-L16`; `README.md:L73-L97` |
| Gemini CLI | `.gemini/commands/*.toml`; `skills/` | Native commands and skill install | 9 authored wrappers; Gemini-specific prompts | `README.md:L130-L143`; `.gemini/commands/*.toml` |
| Antigravity CLI | root `plugin.json`, `commands/*.toml` | Native plugin install | Legacy command wrappers have a documented discoverability limitation | `README.md:L112-L124`, `L360-L364` |
| Codex | `.codex-plugin/`, `.agents/plugins/` | Native plugin + marketplace | Codex reads `skills/`; Claude commands/personas do not transfer | `.codex-plugin/plugin.json:L1-L29`; `.agents/plugins/marketplace.json:L1-L22`; `README.md:L179-L188` |
| Copilot CLI | root `plugin.json` | Plugin metadata / skill directory convention | Lifecycle slash wrappers are absent | `plugin.json:L1-L11`; `README.md:L164-L169`, `L360-L364` |
| OpenCode | Manual copy to `.opencode/skills/` | Community `skills` CLI or copy | No checked-in `.opencode` adapter/command files; users must add project guidance | `docs/opencode-setup.md:L10-L19`, `L180-L184`; `README.md:L156-L160` |
GENERATION: No manifest generator was found. All five version-bearing manifests are separately authored at `0.6.15`; `validate-versions.js` compares them to root `plugin.json`. Command wrappers are likewise hand-maintained; the checker enforces filename parity, matching descriptions and Claude YAML frontmatter, not body equivalence. [V] `scripts/validate-versions.js:L6-L34`; `scripts/validate-commands.js:L1-L15`, `L60-L212`
VALIDATION: CI runs version, command-parity and artifact-path validators plus tests. The artifact checker guards a fixed spec/plan/todo path allowlist; it skips missing guarded files. [V] `.github/workflows/test-plugin-install.yml:L23-L32`, `L58-L79`, `L103-L124`; `scripts/validate-artifact-paths.js:L20-L62`
VERSIONING AND RELEASE: Shared `0.6.15` checked across root, Claude, Codex and marketplace manifests; release automation/tag policy was not inspected. [V] `scripts/validate-versions.js:L6-L34`
INSTALL FOOTPRINT: Remote install through Claude/Codex marketplace or `npx skills add`; setup instructions may clone GitHub over SSH/HTTPS. `hooks/session-start.sh` is a manual standalone helper, not wired by either plugin. No curl-to-shell install appears in inspected instructions; external installers were not run. [V] `README.md:L48-L88`; `docs/codex-setup.md:L35-L35`; `docs/gemini-cli-setup.md:L94-L96`
PORTABLE ESSENCE: Shared skill directories, independent from agent-specific marketplace metadata.
BAGGAGE: Wrapper parity is not behavioral parity; Gemini/Antigravity prompts differ intentionally. OpenCode has no checked-in adapter and relies on manual setup.
CONFIDENCE: High for checked-in manifests, wrappers and CI validators; no validator, installer or workflow was executed.
