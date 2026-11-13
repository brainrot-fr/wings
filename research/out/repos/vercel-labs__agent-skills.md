# vercel-labs/agent-skills
META: https://github.com/vercel-labs/agent-skills | 1a2c79d4e6c4 | 2026-10-27 | license (detected in repo root license file) | n/a | n/a | n/a | n/a | 2026-11-13
ONE-LINER: Vercel skill catalog emphasizing coding rules and front-end guidance patterns.
SPECIES: collection
BLOCKS: requirements:1 frontend:2 backend:1 database:0 security:1 testing:1 sdlc:1 packaging:1
FOOTPRINT: file-first install or package route described in README; static review and repo-scoped context; no runtime code executed in this pass.
AGENT TARGETS: discovered README, skill markdown, package manifests and adapter instructions for the harnesses listed in the repo docs. [V] research/repos/vercel-labs__agent-skills/README.md:1-120.
STRUCTURE:
- - AGENTS.md - artifact
- CLAUDE.md - artifact
- README.md - artifact
- package-lock.json - artifact
- package.json - artifact
- packages - top-level project area
- scripts - top-level project area
- skills - top-level project area
- skills.sh.json - artifact
SKILLS:
| skill | block | species | lines | depth | one-line |
| --- | --- | --- | --- | --- | --- |
| vercel-composition-patterns | n/a | collection | n/a | deep | React composition patterns that scale. Use when refactoring components with |
| deploy-to-vercel | n/a | collection | n/a | deep | Deploy applications and websites to Vercel. Use when the user requests deploymen |
| vercel-react-best-practices | n/a | collection | n/a | deep | React and Next.js performance optimization guidelines from Vercel Engineering. T |
| vercel-react-native-skills | n/a | collection | n/a | catalog | React Native and Expo best practices for building performant mobile apps. Use |
| vercel-react-view-transitions | n/a | collection | n/a | catalog | Guide for implementing smooth, native-feeling animations using React's View Tran |
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
