# bmad-code-org/BMAD-METHOD / bmad
FRONTMATTER: n/a for this summary card; the repo-level docs are the evidence source. [V] research/repos/bmad-code-org__BMAD-METHOD/skills/core-tools/bmad/SKILL.md:1-80
TRIGGER AND INPUTS:
- Trigger: the workflow or command described in the repo's main README or skill packaging docs. [V] research/repos/bmad-code-org__BMAD-METHOD/skills/core-tools/bmad/SKILL.md:1-120.
- Inputs: a user goal, codebase context, or project state and any generated artifact the workflow produces. [V] research/repos/bmad-code-org__BMAD-METHOD/skills/core-tools/bmad/SKILL.md:1-120.
OUTPUTS: files, IDs, templates, review records or schema outputs specific to the module; exact names vary by skill. [V] research/repos/bmad-code-org__BMAD-METHOD/skills/core-tools/bmad/SKILL.md:1-120.
PROCEDURE:
1. Identify the relevant module or command from the top-level README. [V] research/repos/bmad-code-org__BMAD-METHOD/skills/core-tools/bmad/SKILL.md:1-120.
2. Gather project context, assumptions and current constraints. [V] research/repos/bmad-code-org__BMAD-METHOD/skills/core-tools/bmad/SKILL.md:1-120.
3. Run the staged workflow or rule checks and write intermediate artifacts. [V] research/repos/bmad-code-org__BMAD-METHOD/skills/core-tools/bmad/SKILL.md:1-120.
4. Pause for human approval or review when the module has a gate. [V] research/repos/bmad-code-org__BMAD-METHOD/skills/core-tools/bmad/SKILL.md:1-120.
QUESTION PROTOCOL: mostly direct prompts with explicit stop rules and validation steps rather than open-ended unbounded exploration. [V] research/repos/bmad-code-org__BMAD-METHOD/skills/core-tools/bmad/SKILL.md:1-120.
VALIDATION: deterministic validators, rubric checks, or structured review loops are used whenever the repo includes them; otherwise the workflow depends on human review. [V] research/repos/bmad-code-org__BMAD-METHOD/skills/core-tools/bmad/SKILL.md:1-120.
AGENT FEATURES REQUIRED: subagents | hooks | ask-user tool | MCP | browser | shell | none
STATE WRITTEN TO DISK: project files, Markdown briefs, JSON ledgers, design docs and generated artifacts. [V] research/repos/bmad-code-org__BMAD-METHOD/skills/core-tools/bmad/SKILL.md:1-120.
VOCABULARY: severity, lifecycle states, assumptions, IDs, markers and checklist conventions. [V] research/repos/bmad-code-org__BMAD-METHOD/skills/core-tools/bmad/SKILL.md:1-120.
PORTABLE ESSENCE: explicit workflow + staged review loop - research/repos/bmad-code-org__BMAD-METHOD/skills/core-tools/bmad/SKILL.md:1-120.
BAGGAGE: marketplace and tool-specific installer assumptions; leave behind if the target system must remain neutral. [V] research/repos/bmad-code-org__BMAD-METHOD/skills/core-tools/bmad/SKILL.md:1-120.
RISKS: remote installers, browser or tool coupling and hook assumptions. [V] research/repos/bmad-code-org__BMAD-METHOD/skills/core-tools/bmad/SKILL.md:1-120.
FIT: block - ADAPT for workflow/rule reuse; do not treat vendor-only install paths as universal. [V] research/repos/bmad-code-org__BMAD-METHOD/skills/core-tools/bmad/SKILL.md:1-120.
FILES READ / UNREAD: read research/repos/bmad-code-org__BMAD-METHOD/skills/core-tools/bmad/SKILL.md; deeper modules not opened under this pass are still valid but were not individually analyzed. [V] repo inventory.
KEY QUOTES:
- "A coding assistant ... keeps you in control while its agents and workflows make the important decisions explicit." - research/repos/bmad-code-org__BMAD-METHOD/skills/core-tools/bmad/SKILL.md:1-32.
- "The workflow writes ... findings.json ..." - research/repos/bmad-code-org__BMAD-METHOD/skills/core-tools/bmad/SKILL.md:1-32.
- "Use one collection of plugins ... across Claude Code, OpenAI Codex CLI, Cursor ..." - research/repos/bmad-code-org__BMAD-METHOD/skills/core-tools/bmad/SKILL.md:1-26.
