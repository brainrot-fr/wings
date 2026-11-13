# dralgorhythm/claude-agentic-framework / threat-modeling
SOURCE: `.claude/skills/security/threat-modeling/SKILL.md` | commit `6436a20fadad6de8e48aebfb6821d7269341c057` | no root license found; 121 lines across skill and linked security rule (`wc -l`)
FRONTMATTER: `name: threat-modeling`; `description: Identify and analyze security threats. Use when designing a feature with security implications, before implementing auth/input-handling code, or when an audit calls for a threat model. Covers STRIDE methodology.`
FILES READ:
| Path | Lines | Role |
|---|---:|---|
| `.claude/skills/security/threat-modeling/SKILL.md` | 36 | Procedure and threat-model example |
| `.claude/rules/security.md` | 85 | Severity, enforcement and output constraints |
FILES UNREAD: `docs/hooks.md` (nested reference from the security rule, not directly required by this skill); no root LICENSE/NOTICE was found.
JOB: Threat-model features with security implications before coding or during audits. The example is a Markdown asset/threat table, not a named output file. [V] (`.claude/skills/security/threat-modeling/SKILL.md:L2-L3`, `L26-L36`)
PROCEDURE:
1. `Map Attack Surface`: locate entry points and trust boundaries; sketch data flow. [V] (`.claude/skills/security/threat-modeling/SKILL.md:L8-L10`)
2. `Enumerate Threats`: apply all six STRIDE categories per component, using Sequential Thinking. [V] (`.claude/skills/security/threat-modeling/SKILL.md:L11-L12`)
3. `Trace Data Flow`, rate against `.claude/rules/security.md`, then record STRIDE type, severity and remediation. [V] (`.claude/skills/security/threat-modeling/SKILL.md:L12-L14`)
DECISION RULES: Critical/High must be fixed before merge; Medium should be fixed or negotiated; Low is optional. [V] (`.claude/rules/security.md:L60-L67`)
ARTIFACT SHAPE: `Asset` heading; threat table with Threat, Type, Severity, Remediation. [V] (`.claude/skills/security/threat-modeling/SKILL.md:L26-L36`)
QUESTION PROTOCOL: None specified.
VALIDATION: Grep/Glob-guided source tracing and qualitative STRIDE analysis; no validator or test procedure.
AGENT FEATURES REQUIRED: Sequential Thinking tool is explicitly named; no fallback is described. [V] (`.claude/skills/security/threat-modeling/SKILL.md:L8-L12`)
STATE ON DISK: No state or resumability format specified.
VOCABULARY: STRIDE; Critical/High/Medium/Low; severity rules are in `.claude/rules/security.md`; no finding IDs or requirement links. [V] (`.claude/skills/security/threat-modeling/SKILL.md:L11-L14`; `.claude/rules/security.md:L60-L80`)
NON-OBVIOUS TECHNIQUES:
- Add five agent-specific threat classes when a tool/model boundary exists. [V] (`.claude/skills/security/threat-modeling/SKILL.md:L16-L24`)
- Treat hooks, settings and MCP definitions as automatic execution paths. [V] (`.claude/skills/security/threat-modeling/SKILL.md:L18-L24`)
- Distinguish prose/skill advice from hooks and CI enforcement. [V] (`.claude/rules/security.md:L5-L14`)
FAILURE MODE FOUGHT: Omitting agent/tool boundary threats and modeling without tracing inputs through processing to storage. [V] (`.claude/skills/security/threat-modeling/SKILL.md:L8-L24`)
BAGGAGE: Relies on Sequential Thinking and framework-specific security rules; no license was found, so paraphrase only.
RISKS: The procedure names a specialized reasoning tool without an inline fallback. [V] (`.claude/skills/security/threat-modeling/SKILL.md:L8-L12`)
FIT: security — **REFERENCE** the agent-specific threat categories, but do not reuse unlicensed text; portability requires a tool-optional STRIDE alternative. [I] (`.claude/skills/security/threat-modeling/SKILL.md:L16-L24`)
CONFLICTS: Critical/High/Medium/Low does not match P0–P3; mandatory Sequential Thinking conflicts with optional-tool portability. [V] (`.claude/rules/security.md:L60-L67`; `.claude/skills/security/threat-modeling/SKILL.md:L11-L12`)
KEY QUOTES: None.
CONFIDENCE: High for the skill and linked severity rules; nested hooks documentation was not read.
