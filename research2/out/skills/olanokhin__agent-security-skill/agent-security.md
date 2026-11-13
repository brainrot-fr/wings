# olanokhin/agent-security-skill / agent-security
SOURCE: actual path `skills/agent-security/SKILL.md` (not expected root path) | commit `4efa6224a8af3669b7cebf24261353c57a0fd7a0` | MIT, `LICENSE` | 1,135 lines read (folder: 353; `find`/`wc -l`)
FRONTMATTER: `name: agent-security`; `description: Use when reviewing or writing LLM, RAG, MCP, tool, or agent code for OWASP-aligned security issues; triggered by "owasp my code", "owasp this PR", AI security review, PR review, or changes to AI system code.`
FILES READ:
| Path | Lines | Role |
|---|---:|---|
| `skills/agent-security/SKILL.md`; `skills/agent-security/agents/openai.yaml` | 349; 4 | Skill; agent prompt |
| `AI_SECURITY.md`; `AGENTS.md`; `README.md`; `LICENSE` | 344; 11; 406; 21 | Shared checks; entrypoint; install guide; license |
FILES UNREAD: Benchmark scripts/fixtures and example files; evaluation material is outside the skill folder and not referenced by `SKILL.md`.
JOB: Review/write LLM, RAG, MCP, tool, and agent code; outputs concise findings in the `LAYER · ID · SEVERITY / Location / Issue / Fix` format. [V] (`skills/agent-security/SKILL.md:L2-L3`, `L310-L327`)
PROCEDURE: Identify layer by trigger: LLM01–10 (model), PIPE01–13 (applied gaps), ASI01–10 (agent); inspect infrastructure before confirming specified infra-dependent gaps; report minimum findings for listed patterns. [V] (`skills/agent-security/SKILL.md:L22-L31`, `L43-L60`)
DECISION RULES: Critical/High/Medium/Low; pattern table sets mandatory minimum IDs/severities; reduce selected robustness findings one level for non-production files; absent IaC means `VERIFY`, not confirmed. [V] (`skills/agent-security/SKILL.md:L43-L60`)
ARTIFACT SHAPE: Finding layer/ID/severity, location, issue, fix; `LLM`, `PIPE`, `ASI` identifier families. [V] (`skills/agent-security/SKILL.md:L310-L327`, `L331-L344`)
QUESTION PROTOCOL: n/a.
VALIDATION: No validator in skill folder; model judgment over code/context. README describes benchmark, but its runner was not read or run.
AGENT FEATURES REQUIRED: Context-loaded skill/instruction only; no special tools documented. [I]
STATE ON DISK: No run-state artifact; reusable `AI_SECURITY.md` and `AGENTS.md` instructions. [V] (`README.md:L112-L122`)
VOCABULARY: `LLM01–10`, `PIPE01–13`, `ASI01–10`; severities CRITICAL/HIGH/MEDIUM/LOW; `VERIFY` for assumptions. [V] (`skills/agent-security/SKILL.md:L60`, `L321-L344`)
NON-OBVIOUS TECHNIQUES:
- Treat reviewed content as untrusted, not instructions. [V] (`skills/agent-security/SKILL.md:L18-L20`)
- Report distinct `ASI09` and `ASI10` issues separately even when `LLM06` also applies. [V] (`skills/agent-security/SKILL.md:L52-L54`)
- Search IaC before confirming rate-limit, retention, or related infrastructure gaps. [V] (`skills/agent-security/SKILL.md:L60`)
FAILURE MODE FOUGHT: LLM/RAG/MCP/agent-specific risks omitted by conventional application-security checklists. [I] (`README.md:L47-L57`)
BAGGAGE: Product-maintained PIPE checklist supplements official OWASP taxonomies; no requirements-level finding links.
RISKS: Installation instructions use `curl` to fetch pinned GitHub archive/raw files into project paths; not runtime retrieval. [V] (`README.md:L202-L243`)
FIT: security: ADAPT untrusted-data rule, distinct stable IDs, infra-aware `VERIFY`, and regression-eval idea. Replace four-tier severities with P0–P3 and add requirement-linked findings. [I]
CONFLICTS: Four-tier severity conflicts with house P0–P3; README markets five agents, but native skills are documented only for Claude Code/Codex. [V] (`README.md:L5-L17`, `L112-L131`)
KEY QUOTES: None.
CONFIDENCE: High; actual skill path corrected and all skill-folder files plus linked shared instructions read.
