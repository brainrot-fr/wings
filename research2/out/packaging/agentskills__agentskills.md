# agentskills/agentskills (packaging)
SOURCE: `83021e2be457` | `docs/specification.mdx` is CC BY 4.0 (`docs/LICENSE`); `skills-ref` is Apache-2.0 (`skills-ref/LICENSE`); root `LICENSE` is Apache-2.0
SINGLE SOURCE OF TRUTH: One directory per skill, with `SKILL.md` frontmatter and optional `scripts/`, `references/`, and `assets/`; the format specifies no marketplace adapters or generated agent-specific copies. [V] `docs/specification.mdx:L6-L17`; `docs/specification.mdx:L187-L214`
AGENT TARGETS:
| agent/client | manifest or install path | mechanism | generated | loss / breakage | verified at |
|---|---|---|---|---|---|
| Skills-compatible clients | Skill directory containing `SKILL.md` | Client discovers metadata, loads instructions when activated, then loads referenced resources | None mandated by format; `skills-ref to-prompt` can emit one XML listing | `allowed-tools` support varies; clients can render prompt metadata differently; no universal runtime contract | `docs/specification.mdx:L216-L245`; `skills-ref/README.md:L45-L75` |
GENERATION:
- `skills-ref validate <path>` validates metadata; `read-properties` emits JSON; `to-prompt` emits `<available_skills>` XML. [V] `skills-ref/README.md:L29-L75`; `skills-ref/src/skills_ref/cli.py:L18-L85`
- Reference package version `0.1.0`, Python `>=3.11`; dependencies are Click `>=8.0` and StrictYAML `>=1.7.3`; Hatchling builds the package. [V] `skills-ref/pyproject.toml:L1-L21`
- `to_prompt` resolves each folder, reads properties, HTML-escapes name and description, and emits the resolved `SKILL.md` location. [V] `skills-ref/src/skills_ref/prompt.py:L9-L52`
VALIDATION:
- Specification fields: `name` required (1–64 chars, lowercase alphanumeric/hyphens, no leading/trailing/consecutive hyphens, must equal parent directory); `description` required (1–1024 chars, nonempty); optional `license`; optional `compatibility` (1–500 chars); optional string-to-string `metadata`; optional experimental space-separated `allowed-tools`. [V] `docs/specification.mdx:L23-L32`; `docs/specification.mdx:L58-L90`; `docs/specification.mdx:L91-L109`; `docs/specification.mdx:L110-L175`
- Validator enforces allowed top-level fields, required name/description, name length/case/hyphen/characters/directory match, description length, and compatibility type/maximum. It does not enforce the spec's minimum compatibility length; its Unicode `isalnum` check also accepts characters beyond the docs table's ASCII examples. [V] `skills-ref/src/skills_ref/validator.py:L10-L115`
- Parser accepts uppercase or lowercase `SKILL.md`, requires opening/closing `---`, parses with StrictYAML, and converts metadata map values to strings. [V] `skills-ref/src/skills_ref/parser.py:L12-L70`
- Package README marks `skills-ref` demonstration-only, not production-ready. No validator or tests were run. [V] `skills-ref/README.md:L1-L7`
VERSIONING AND RELEASE: The reference package declares `0.1.0`; this pass did not inspect release tags or client-specific versions. [V] `skills-ref/pyproject.toml:L1-L4`
INSTALL FOOTPRINT: The documented path installs the Python package into a virtual environment using pip or uv. It does not require a hook or downloaded binary; network behavior of package installation was not tested. [V] `skills-ref/README.md:L9-L28`
PORTABLE ESSENCE: Small file contract plus progressive-disclosure guidance; clients can implement their own loader without invoking `skills-ref`. [V] `docs/specification.mdx:L216-L245`
BAGGAGE: Python/Click/StrictYAML and XML prompt generation are optional reference tooling, not part of the interchange format. [I] `skills-ref/pyproject.toml:L1-L21`; `skills-ref/src/skills_ref/prompt.py:L9-L52`
CONFIDENCE: High for the file format and static validator behavior; the library itself is explicitly a demonstration package and was not executed.
