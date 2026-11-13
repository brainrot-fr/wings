# addyosmani/agent-skills / security-auditor
SOURCE: `agents/security-auditor.md` | commit `301b02b12bff98e4688e6984af6556802322bbde` | MIT (`LICENSE`) | 256 lines (`wc -l`)
FRONTMATTER: `name: security-auditor`; `description: Security engineer focused on vulnerability detection, threat modeling, and secure coding practices. Use for security-focused code review, threat analysis, or hardening recommendations.`
FILES READ:
| Path | Lines | Role |
|---|---:|---|
| `agents/security-auditor.md` | 112 | Persona prompt |
| `docs/agents.md` | 123 | Invocation and composition model |
| `LICENSE` | 21 | MIT |
FILES UNREAD: `references/orchestration-patterns.md` (linked by `docs/agents.md`); other personas and commands.
JOB: Review a change or component directly, or in `/ship`; outputs a report with findings, positives and recommendations. [V] (`agents/security-auditor.md:L67-L95`, `L108-L112`; `docs/agents.md:L26-L45`)
PROCEDURE:
1. Review six scopes: input handling, auth/authz, data protection, infrastructure, third-party integrations and conditional AI/LLM features. [V] (`agents/security-auditor.md:L10-L55`)
2. Begin from trust boundaries and reason with STRIDE before enumerating findings. [V] (`agents/security-auditor.md:L97-L106`)
3. Give each finding location, impact and actionable recommendation; Critical/High findings include a proof-of-concept or exploitation scenario. [V] (`agents/security-auditor.md:L78-L95`)
DECISION RULES: Critical blocks release; High before release; Medium current sprint; Low next sprint; Info optional. [V] (`agents/security-auditor.md:L57-L65`)
ARTIFACT SHAPE: `Security Audit Report`; severity counts; findings with location, impact, proof and fix; positives and recommendations. [V] (`agents/security-auditor.md:L67-L95`)
QUESTION PROTOCOL: None.
VALIDATION: Model-led OWASP/source review; no deterministic checker.
AGENT FEATURES REQUIRED: Compatible persona harness; optional `/ship` fan-out, with one merge step. [V] (`docs/agents.md:L12-L20`, `L41-L45`, `L99-L115`)
STATE ON DISK: None specified.
VOCABULARY: Critical/High/Medium/Low/Info, OWASP Top 10 and LLM Top 10; no stable finding IDs or requirement references. [V] (`agents/security-auditor.md:L57-L65`, `L78-L95`)
NON-OBVIOUS TECHNIQUES:
- Include AI/LLM checks only when relevant. [V] (`agents/security-auditor.md:L48-L55`)
- Separate persona (who), skill (how) and command (when). [V] (`docs/agents.md:L12-L20`)
- Fan out only independent work; merge centrally. [V] (`docs/agents.md:L41-L45`, `L64-L84`)
FAILURE MODE FOUGHT: Untethered threat lists and findings without actionable fixes. [V] (`agents/security-auditor.md:L5-L10`, `L97-L106`)
BAGGAGE: Five levels vs P0–P3; PoC format is not bounded.
RISKS: Findings may contain exploit reproduction detail; keep validation authorized and bounded. [I] (`agents/security-auditor.md:L78-L85`)
FIT: security — **ADAPT** scope checklist and composition; replace severity with P0–P3 and add stable IDs and requirement links. [I] (`agents/security-auditor.md:L10-L65`, `L67-L95`)
CONFLICTS: A mandatory parallel fan-out would violate optional-subagent portability; the persona guide's direct invocation is a fallback. [V] (`docs/agents.md:L26-L45`)
KEY QUOTES: None.
CONFIDENCE: High; orchestration-patterns unread.
