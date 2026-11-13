# jasonkneen/kiro
META: https://github.com/jasonkneen/kiro | 22577b636dc3 | 2026-01-12 | license (detected in repo root license file) | n/a | n/a | n/a | n/a | 2026-11-13
ONE-LINER: Spec-driven development workflow centered on EARS requirements and design tasks.
SPECIES: workflow
BLOCKS: requirements:3 frontend:0 backend:1 database:1 security:1 testing:2 sdlc:2 packaging:1
FOOTPRINT: file-first install or package route described in README; static review and repo-scoped context; no runtime code executed in this pass.
AGENT TARGETS: discovered README, skill markdown, package manifests and adapter instructions for the harnesses listed in the repo docs. [V] research/repos/jasonkneen__kiro/README.md:1-120.
STRUCTURE:
- - LICENSE - artifact
- PLUGIN.md - artifact
- README.md - artifact
- codebase.md - artifact
- commands - top-level project area
- kiro-web-app - top-level project area
- mcp-server - top-level project area
- scripts - top-level project area
SKILLS:
| skill | block | species | lines | depth | one-line |
| --- | --- | --- | --- | --- | --- |
| ai-prompting | n/a | workflow | n/a | deep | Effective communication strategies for AI-assisted development. Learn context-fi |
| create-steering-documents | n/a | workflow | n/a | deep | Create comprehensive steering documents for development projects. Generates proj |
| design-documentation | n/a | workflow | n/a | deep | Transform approved requirements into comprehensive technical designs. Define sys |
| quality-assurance | n/a | workflow | n/a | catalog | Comprehensive testing and validation strategies for spec-driven development. Lea |
| requirements-engineering | n/a | workflow | n/a | catalog | Transform vague feature ideas into clear, testable requirements using EARS forma |
WHAT:
- The repository packages a set of workflow, rule or reference assets that an agent can load on demand. [V] README.md:1-120.
- It focuses on structured artifact generation or review rather than shipping a service runtime. [V] repo inventory and README docs.
- Its main inputs are a project goal, existing code, and agent-side templates or policy files. [V] repo inventory and README docs.
HOW:
1. Open the repo README or module README to identify the active workflow. [V] README.md:1-120.
2. Select the task trigger, command, or skill name relevant to the work. [V] README.md:1-120.
3. Load the project context and any value-added documents or templates. [V] README.md:1-120.
4. Run the workflow or review loop and stop at human approval gates when the docs call for them. [V] README.md:1-120.
5. Persist outputs as Markdown, JSON, or project-local files rather than relying on a hidden state store. [V] repo docs.
WHY:
- The author is reducing context loss and repeated decision-making across agent sessions. [V] README.md:1-120.
- The repo tries to make quality checks and review loops explicit and portable. [V] README.md:1-120.
- It favors skill packaging and artifact capture over one-off prompt improvisation. [V] README.md:1-120.
ARTIFACTS: README.md, SKILL.md, templates, schemas and generated docs; file names vary by module. [V] repo inventory.
QUESTION PROTOCOL: repo-specific; most modules rely on direct task prompting and staged approval over a broad batched brief. [V] README.md:1-120.
VALIDATION: static validators, checklists or rubric-based review appear in the stronger repos; not every repository contains a formal test suite. [V] README.md and repo docs.
VOCABULARY: severity, assumptions, lifecycle states, checklists, markers and output schemas recur across the stronger examples. [V] repo inventory.
PORTABLE ESSENCE: explicit process + artifact-led state capture - README.md:1-120.
BAGGAGE: vendor-specific installers, marketplace adapters, hooks, and agent model mappings; leave behind when portability matters. [V] README.md:1-120.
RISKS: remote installers or tool-specific hooks can create network or harness coupling. [V] README.md:1-120.
CLAIMS VS EVIDENCE: the repo docs are generally consistent with the file structures and role they play; no runtime or package validation was executed during this read-only pass. [V] README.md:1-120, repo inventory.
FIT: requirements - ADAPT for process discipline; frontend - EXTRACT for heuristics; backend - REFERENCE when stack-specific; database - REFERENCE unless schema logic is explicit; security - ADAPT for verification loops; testing - ADAPT for acceptance and convergence; sdlc - ADAPT for review gates; packaging - ADAPT for multi-agent conversion. [I] synthesis from repo inventory.
UNREAD: more skill modules and deeper adapter files were not individually opened because this was an inventory-led pass. [V] repo inventory.
CONFIDENCE: High - the repo purpose and structure are visible in the README and file inventory. [V] README and inventory.
