# Security

## RANKED CANDIDATES
1. [Natolitech threat-model](../skills/natolitech__security-skill/threat-model.md) — concrete STRIDE, numbered trust boundaries, privacy pass, stable threat IDs and top attack paths. (`.claude/commands/threat-model.md:L53-L86`, `L87-L154`)
2. [Semgrep](../skills/semgrep__skills/semgrep.md) — deterministic rule tests, taint sources/sinks/sanitizers, CLI validation; requires the Semgrep binary. (`skills/semgrep/SKILL.md:L109-L155`, `L192-L220`)
3. [Natolitech security-review](../skills/natolitech__security-skill/security-review.md) — contextual verification and prior-finding comparison with a persistent triage ledger. (`.claude/commands/security-review.md:L293-L347`, `L419-L488`)
4. [Olanokhin agent-security](../skills/olanokhin__agent-security-skill/agent-security.md) — explicit LLM, pipeline and agent issue IDs; infra-dependent claims can remain `VERIFY`. (`skills/agent-security/SKILL.md:L43-L60`, `L310-L344`)
5. [mgiovani review-security](../skills/mgiovani__cc-arsenal/review-security.md) — scoped OWASP scan, evidence verification, deduplication and inline fallback. (`skills/review-security/SKILL.md:L87-L154`)
6. [Hov secure-webapp](../skills/hov172__secure-webapp-skill/secure-webapp.md) — four review modes, ownership-aware authorization checks, and AI-tool controls. (`SKILL.md:L8-L20`; `references/authorization.md:L18-L55`; `references/ai-and-llm.md:L51-L80`)
7. [Jeffallan security-reviewer](../skills/Jeffallan__claude-skills/security-reviewer.md) — explicit authorization, bounded validation and structured reports, with scanner-heavy dependencies. (`skills/security-reviewer/SKILL.md:L31-L43`, `L71-L99`)
8. [Addy security-and-hardening](../skills/addyosmani__agent-skills/security-and-hardening.md) — clear approval boundaries and concrete input, SSRF, dependency and privacy patterns. (`skills/security-and-hardening/SKILL.md:L21-L73`, `L109-L140`)
9. [Addy security-auditor](../skills/addyosmani__agent-skills/security-auditor.md) — persona/skill/command separation and a trust-boundary-led report. (`agents/security-auditor.md:L10-L55`, `L67-L106`)
10. [Wshobson STRIDE patterns](../skills/wshobson__agents/stride-analysis-patterns.md) — four reusable templates with typed DFD mappings and scoring examples. (`plugins/security-scanning/skills/stride-analysis-patterns/references/details.md:L164-L220`, `L435-L477`)
11. [Trail of Bits audit-context-building](../skills/trailofbits__skills/audit-context-building.md) — evidence-linked per-function dossiers that preserve unknowns and open questions. (`plugins/audit-context-building/skills/audit-context-building/SKILL.md:L25-L38`, `L58-L72`)
12. [Dralgorhythm threat-modeling](../skills/dralgorhythm__claude-agentic-framework/threat-modeling.md) — explicitly adds agent, hook, settings and MCP threat classes. (`.claude/skills/security/threat-modeling/SKILL.md:L8-L24`)

## COMPARISON MATRIX
| Candidate | Method / artifact | Severity and identity | Validation | Portability |
|---|---|---|---|---|
| Natolitech threat model | STRIDE + privacy; boundary diagram; threats and paths | `TM-NNN`; likelihood and impact | Static evidence; no validator | Shell; optional remote clone |
| Natolitech review | 20 vulnerability classes; Markdown/JSON + backlog | `SR-NNN`; five severities plus three confidence levels | Context and control checks | Local review; remote clone option |
| Semgrep | Pattern or taint rules with annotated tests | `ERROR/WARNING/INFO`; rule IDs | CLI test/validate and AST | Semgrep binary and possibly remote rules |
| Olanokhin | LLM/PIPE/ASI pattern tables | Stable family IDs; four severities; `VERIFY` | Model judgment; benchmark not reviewed | Instructions portable; installer downloads |
| mgiovani | OWASP A01–A10 scan prompts and report | Four severities; no stable finding IDs | Grep/Read; agents preferred, inline fallback | Claude-oriented tool set; network freshness check |
| Hov | Audit, quick-check, harden, design review; Markdown findings | Critical–Info; no stable IDs | Model review; optional `npm audit` | Multi-agent instructions portable; updater uses `npx` |
| Jeffallan | Authorized scans, manual review, Markdown/JSON findings | CVSS, Critical–Info; `FIND-NNN` example | SAST/dependency/secret scanners and manual validation | External binaries and active-test authorization |
| Addy hardening | STRIDE plus boundary checklists and implementation patterns | No finding IDs or severity scale | Human checklist; native package audit | Web/TypeScript examples; manager policy can age |
| Addy persona | Trust-boundary review and `Security Audit Report` | Critical–Info; no stable IDs | Model-led; optional parallel review | Requires compatible persona harness |
| Wshobson STRIDE | System/asset/DFD templates, questionnaires and sample code | Impact × likelihood; sample thresholds | Deterministic examples plus model review | Templates portable; example code needs review |
| Trail of Bits | Per-function dossiers and cross-function dependencies | No severity or finding IDs | Citation/call-path rubric; subagents required | CC BY-SA; orchestration-dependent |
| Dralgorhythm | Asset/threat table; STRIDE plus agent-specific categories | Critical–Low; no IDs | Qualitative; Sequential Thinking required | No license found; tool fallback unspecified |

## CONFLICTS
- House P0–P3 must replace the incompatible Critical/High/Medium/Low, likelihood-impact, or ERROR/WARNING/INFO schemes; confidence should remain separate.
- Natolitech's command templates request secret excerpts, conflicting with this task's prohibition; reject that behavior. Semgrep's binary and remote rules, mgiovani's live OWASP/`gh` checks, and Olanokhin's `curl` installation are optional setup, not portable runtime essentials.
- None of the carded findings has an explicit source requirement ID.

## QUESTIONS ANSWERED
- **Audit phases and outputs:** Natolitech security review uses reconnaissance, vulnerability analysis, contextual threat assessment and verification, then `SR-NNN` reports and a local backlog. Threat modeling maps entrypoints and trust crossings, performs STRIDE/privacy review and reports threats and top paths. Hov separates audit, quick-check, harden and design-review outputs; Jeffallan requires written scope and structured, location-specific remediation reports. (`security-review.md`; `threat-model.md`; `secure-webapp.md`; `security-reviewer.md`)
- **Threat method / mapping:** STRIDE is tied to actual components and numbered boundary crossings (`B1…`), with stable `TM-NNN` IDs. The report template has no requirement-ID field. (`threat-model.md`)
- **Severity/confidence:** schemes conflict and are not directly convertible: Natolitech separates confidence from severity; Wshobson scores impact × likelihood; Jeffallan includes CVSS; Hov and Addy use Critical–Info; no shared crosswalk exists. No carded workflow supplies requirement IDs.
- **LLM/agent security:** Olanokhin distinguishes `LLM`, `PIPE`, and `ASI` issue families and permits `VERIFY` for unknown infrastructure. Hov treats the user, not the agent, as principal and requires AI-tool schema/ownership checks; Dralgorhythm adds hook, settings and MCP execution paths. (`agent-security.md`; `secure-webapp.md`; `threat-modeling.md`)
- **External tools:** Semgrep requires its CLI; Jeffallan names multiple scanner binaries; mgiovani has an inline fallback; Olanokhin's `curl` is installation-time. Trail of Bits and Dralgorhythm require specialized agent/reasoning tools without an evidenced fallback. No prescribed command was run.
- **Cloudflare schema fields:** all three branches share `verdict`, `fingerprint`, `title`, `description`, `trace[{kind,file,line,scope,description}]` and `evidence[{file,line,description}]`. `confirmed` adds `root_cause`, `intended_behavior`, `conditions[{kind,description}]`, `execution{attacker_perspective,payloads,instructions,observed_result}`, `remediation{strategy,code_changes[{file_name,fixed_code}]}`, `severity{likelihood{score,reason},impact{score,reason},overall_severity}` and `confidence{score,reason}`. `needs_validation` adds `claimed_root_cause`, `blockers`, `validation_plan{local,deployment}`; `rejected` adds `claimed_root_cause` and `reason`. (`skills/security-audit/report-schema.json:L9-L243`, `L249-L360`, `L366-L456`)
- **Cloudflare validator/runtime:** `validate-findings.cjs` interprets a bounded JSON Schema subset (types, required/properties, `oneOf`, `const`, `enum`, `items`, `minimum`, lengths/counts, patterns, uniqueness, visible content and extra-field policy), then enforces safe relative source paths, positive line numbers, unique/sorted fingerprints, trace order, verdict-specific allowed/required fields, visible observed results/remediation, severity no higher than demonstrated impact, and a local/deployment plan for `needs_validation`. File input must be regular, non-symlink, valid UTF-8 and at most 5 MiB; depth is capped at 64, arrays at 1,000 and diagnostics at 100. It uses only Node built-ins; Node.js is required, with `O_NOFOLLOW` and `O_NONBLOCK` support, but the validator itself does not need the audit sandbox. The broader workflow requires an OS-enforced, no-network sandbox for target-controlled code, sanitized environment, resource limits and scratch-only writes; absent it, leads stay `needs_validation`. (`skills/security-audit/validate-findings.cjs:L17-L45`, `L247-L359`, `L361-L603`, `L604-L773`; `README.md:L87-L90`; `skills/security-audit/SKILL.md:L33-L42`)
- Cloudflare was not carded: the coverage-ledger validator, several companion attack-class files and the validator tests remain unread. No validator or target code was run.

## GAP EVIDENCE
- Requirement mapping search: `rg -n -i 'requirement[- ]id|FR-[0-9]+|SC-[0-9]+|source-ref'` across all opened security-card target directories (Natolitech, Hov, Semgrep, mgiovani, Olanokhin, Trail of Bits, Wshobson, Jeffallan, Addy and Dralgorhythm): 0 matches.
- Cloudflare coverage: `research2/progress.md` records 1,898 lines read, including the complete 773-line findings validator; the coverage-ledger validator, remaining attack-class files and tests were not opened. No card was produced.

## TECHNIQUES WORTH TAKING
1. Number trust-boundary crossings and cite them from each threat path. (`.claude/commands/threat-model.md:L53-L86`)
2. Keep unknown deployment facts as `VERIFY`, not confirmed findings. (`skills/agent-security/SKILL.md:L60`)
3. Independently search for mitigating controls before confirming a report item. (`.claude/commands/security-review.md:L293-L303`)
4. Separate pattern rules from taint-flow rules and test safe/unsafe examples. (`skills/semgrep/SKILL.md:L109-L155`, `L206-L220`)
5. Compare prior findings by location/nature rather than stale line number. (`.claude/commands/security-review.md:L419-L434`)
6. Add a privacy/data-protection pass when personal data is present. (`.claude/commands/threat-model.md:L123-L135`)
7. Treat the user as the principal for AI tools; check schema and object ownership. (`references/ai-and-llm.md:L51-L80`)
8. Let DFD element type and endpoint trust levels determine STRIDE coverage. (`plugins/security-scanning/skills/stride-analysis-patterns/references/details.md:L435-L477`)

## DO NOT TAKE
Do not adopt a source's severity scale unchanged, run network lookups without approval, include secret values in reports, or make isolated-agent review a hard dependency.


## CATALOG

| Name | Path (lines) | One-line status | Score |
|---|---|---|---:|
| security-audit | `skills/security-audit/SKILL.md (192)` | partial read; full report schema and findings validator read; no card | 0 |
| secure-webapp | `SKILL.md (83); assets/audit-checklist.md (90)` | carded; modes, linked assets/references and licenses read | four review modes |
| llm-security | `skills/llm-security/SKILL.md (80)` | partial read; no card | 0 |
| code-security | `skills/code-security/SKILL.md (82)` | partial read; no card | 0 |
| audit-context-building | `plugins/audit-context-building/skills/audit-context-building/SKILL.md (72)` | carded; CC BY-SA reference-only | evidence dossiers |
| agentic-actions-auditor | `plugins/agentic-actions-auditor/skills/agentic-actions-auditor/SKILL.md (325)` | not deep-read; no card | 0 |
| audit-prep-assistant | `plugins/building-secure-contracts/skills/audit-prep-assistant/SKILL.md (409)` | not deep-read; no card | 0 |
| security-audit | `skills/security-audit/SKILL.md (70)` | not deep-read; no card | 0 |
| stride-analysis-patterns | `plugins/security-scanning/skills/stride-analysis-patterns/SKILL.md (66)` | carded | STRIDE templates |
| security-reviewer | `skills/security-reviewer/SKILL.md (108)` | carded | authorized scan/report workflow |
| secure-code-guardian | `skills/secure-code-guardian/SKILL.md (196)` | not deep-read; no card | 0 |
| security-and-hardening | `skills/security-and-hardening/SKILL.md (216)` | carded | patterns and controls |
| security-auditor | `agents/security-auditor.md (112)` | carded | persona and composition |
| threat-modeling | `.claude/skills/security/threat-modeling/SKILL.md (36)` | carded; no license found | agent threats |
