# wshobson/agents / stride-analysis-patterns

SOURCE: `plugins/security-scanning/skills/stride-analysis-patterns/` | commit `9c61ab243def98f72da12abd41cfcf5bcd91af9d` (`git rev-parse HEAD`) | MIT (root `LICENSE`; no per-skill notice) | 663 lines (`wc -l` on both skill files)
FRONTMATTER: name: stride-analysis-patterns; description: Apply STRIDE methodology to systematically identify threats. Use when analyzing system security, conducting threat modeling sessions, or creating security documentation. [V] (`plugins/security-scanning/skills/stride-analysis-patterns/SKILL.md:L2-L3`)
FILES READ:

| Path | Lines | Role |
|---|---:|---|
| `plugins/security-scanning/skills/stride-analysis-patterns/SKILL.md` | 66 | Scope, STRIDE, practices |
| `plugins/security-scanning/skills/stride-analysis-patterns/references/details.md` | 597 | Four templates, code |

FILES UNREAD: None; `SKILL.md` points to `references/details.md`, both opened. [V] (`plugins/security-scanning/skills/stride-analysis-patterns/SKILL.md:L46-L48`)

JOB:
- Identify threats with STRIDE; triggers include architecture analysis, design review, documentation, training and audit. [V] (`plugins/security-scanning/skills/stride-analysis-patterns/SKILL.md:L8-L17`)
- Input: system, assets, flows, boundaries; output: threat-model document/report. [V] (`plugins/security-scanning/skills/stride-analysis-patterns/references/details.md:L8-L16`, `plugins/security-scanning/skills/stride-analysis-patterns/references/details.md:L31-L41`, `plugins/security-scanning/skills/stride-analysis-patterns/references/details.md:L146-L160`, `plugins/security-scanning/skills/stride-analysis-patterns/references/details.md:L257-L281`)

PROCEDURE:
1. **System Overview**: describe system, diagram data flows and trust boundaries. [V] (`plugins/security-scanning/skills/stride-analysis-patterns/references/details.md:L10-L29`)
2. **Assets; STRIDE Analysis**: enumerate assets, threats and mitigations across six categories. [V] (`plugins/security-scanning/skills/stride-analysis-patterns/references/details.md:L31-L119`)
3. **Risk Assessment; Recommendations**: prioritize threats; assign immediate, 30-day, 90-day actions. [V] (`plugins/security-scanning/skills/stride-analysis-patterns/references/details.md:L121-L160`)

DECISION RULES: Sample code multiplies impact × likelihood (each 1–4); score ≥12 Critical, ≥6 High, ≥3 Medium, else Low; report ranks top 10. [V] (`plugins/security-scanning/skills/stride-analysis-patterns/references/details.md:L168-L220`, `plugins/security-scanning/skills/stride-analysis-patterns/references/details.md:L257-L281`)
ARTIFACT SHAPE: Template 1 headings: System Overview, Assets, STRIDE Analysis, Risk Assessment, Recommendations; fields ID/Threat/Target/Impact/Likelihood. Report fields: summary/by_category/top_risks. [V] (`plugins/security-scanning/skills/stride-analysis-patterns/references/details.md:L8-L160`, `plugins/security-scanning/skills/stride-analysis-patterns/references/details.md:L257-L281`)
QUESTION PROTOCOL: Yes—category-specific prompts; questionnaire fields `component`, `category`, `question`, `answer`, `notes`. [V] (`plugins/security-scanning/skills/stride-analysis-patterns/SKILL.md:L37-L44`; `plugins/security-scanning/skills/stride-analysis-patterns/references/details.md:L283-L338`)
VALIDATION: Python examples (Templates 2–4) take components, models, DFDs or interactions; produce reports/questionnaires/threat lists. Imports: standard-library `dataclasses`, `enum`, `typing`, `json`. Rubric: cover categories, prioritize impact, update, use DFDs; scoring deterministic. Network use [U]: not stated. [V] (`plugins/security-scanning/skills/stride-analysis-patterns/references/details.md:L164-L597`; `plugins/security-scanning/skills/stride-analysis-patterns/SKILL.md:L52-L66`)
AGENT FEATURES REQUIRED: None evidenced; `subagent|hook|ask-user|MCP|browser|shell` search returned 0 matches in both files. [V] (`plugins/security-scanning/skills/stride-analysis-patterns/SKILL.md:L1-L66`; `plugins/security-scanning/skills/stride-analysis-patterns/references/details.md:L1-L597`)
STATE ON DISK: Template 1 document outline; Template 2 report dictionary. [V] (`plugins/security-scanning/skills/stride-analysis-patterns/references/details.md:L5-L8`, `plugins/security-scanning/skills/stride-analysis-patterns/references/details.md:L257-L281`)
VOCABULARY: Codes S/T/R/I/D/E; sample IDs S1/T1/R1/I1/D1/E1; Low–Critical impact/likelihood; `status: open`; `- [ ]` mitigation marker. [V] (`plugins/security-scanning/skills/stride-analysis-patterns/SKILL.md:L21-L33`; `plugins/security-scanning/skills/stride-analysis-patterns/references/details.md:L43-L119`, `plugins/security-scanning/skills/stride-analysis-patterns/references/details.md:L168-L220`)
NON-OBVIOUS TECHNIQUES:
- Crossings use unequal endpoint `trust_level`; rank by absolute difference. [V] (`plugins/security-scanning/skills/stride-analysis-patterns/references/details.md:L435-L444`)
- DFD element type selects applicable STRIDE categories. [V] (`plugins/security-scanning/skills/stride-analysis-patterns/references/details.md:L446-L477`)
- Interaction mappings key threats by `(source_type, target_type)`. [V] (`plugins/security-scanning/skills/stride-analysis-patterns/references/details.md:L527-L553`)
FAILURE MODE FOUGHT: Omitting threat categories or stopping before mitigations. [V] (`plugins/security-scanning/skills/stride-analysis-patterns/SKILL.md:L60-L66`)
BAGGAGE: Four templates include canned threats and Python examples. [V] (`plugins/security-scanning/skills/stride-analysis-patterns/references/details.md:L5-L7`, `plugins/security-scanning/skills/stride-analysis-patterns/references/details.md:L164-L165`, `plugins/security-scanning/skills/stride-analysis-patterns/references/details.md:L388-L389`, `plugins/security-scanning/skills/stride-analysis-patterns/references/details.md:L510-L511`)
RISKS: Template 3 uses `Dict` in annotations but imports only `List, Set, Tuple`; as written, the snippet lacks that import. [V] (`plugins/security-scanning/skills/stride-analysis-patterns/references/details.md:L392-L392`, `plugins/security-scanning/skills/stride-analysis-patterns/references/details.md:L422-L427`)
FIT: Security: EXTRACT Templates 1–4 from `plugins/security-scanning/skills/stride-analysis-patterns/SKILL.md` and `plugins/security-scanning/skills/stride-analysis-patterns/references/details.md`; ADAPT the Low–Critical sample scale. CONFLICTS: [I] it does not map directly to target P0–P3. [V] (`plugins/security-scanning/skills/stride-analysis-patterns/references/details.md:L5-L597`, `plugins/security-scanning/skills/stride-analysis-patterns/references/details.md:L208-L220`)
KEY QUOTES: “Don't stop at identification” (`plugins/security-scanning/skills/stride-analysis-patterns/SKILL.md:L66-L66`).
CONFIDENCE: High; both files read completely. [V] (`plugins/security-scanning/skills/stride-analysis-patterns/SKILL.md:L1-L66`; `plugins/security-scanning/skills/stride-analysis-patterns/references/details.md:L1-L597`)
