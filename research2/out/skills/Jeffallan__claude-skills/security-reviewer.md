# Jeffallan/claude-skills / security-reviewer
SOURCE: `skills/security-reviewer/SKILL.md` | commit `078a25cc5bfd8011459be7b91d004e900c1d02d3` | MIT (`LICENSE`) | 1,229 lines (`wc -l`)
FRONTMATTER: `name: security-reviewer`; `description: Identifies security vulnerabilities, generates structured audit reports with severity ratings, and provides actionable remediation guidance. Use when conducting security audits, reviewing code for vulnerabilities, or analyzing infrastructure security. Invoke for SAST scans, penetration testing, DevSecOps practices, cloud security reviews, dependency audits, secrets scanning, or compliance checks. Produces vulnerability reports, prioritized recommendations, and compliance checklists.`
FILES READ:
| Path | Lines | Role |
|---|---:|---|
| `skills/security-reviewer/SKILL.md` | 108 | Workflow |
| `skills/security-reviewer/references/vulnerability-patterns.md`; `report-template.md` | 152; 170 | Patterns; report |
| `skills/security-reviewer/references/secret-scanning.md`; `infrastructure-security.md` | 125; 268 | Secret and infrastructure |
| `skills/security-reviewer/references/penetration-testing.md`; `sast-tools.md` | 268; 117 | Testing; SAST |
| `LICENSE` | 21 | MIT |
FILES UNREAD: None referenced by the skill.
JOB: Review code, dependencies, secrets and infrastructure; outputs report and checklist. [V] (`skills/security-reviewer/SKILL.md:L22-L55`, `L81-L88`)
PROCEDURE:
1. `Scope`: map attack surface and get written authorization/rules of engagement. [V] (`skills/security-reviewer/SKILL.md:L31-L35`)
2. `Scan`, then manually review authentication, input and cryptography; validate/classify only within written scope. [V] (`skills/security-reviewer/SKILL.md:L35-L43`)
3. Confirm findings with stakeholder and report location, impact, remediation; report critical items immediately. [V] (`skills/security-reviewer/SKILL.md:L41-L43`)
DECISION RULES: Critical/High/Medium/Low/Info with CVSS; written authorization before testing; stop at proof-of-concept. [V] (`skills/security-reviewer/SKILL.md:L39-L43`, `L71-L79`)
ARTIFACT SHAPE: Summary/counts; findings with ID, location, CWE/CVSS, impact/fix; scan results and prioritized recommendations. [V] (`skills/security-reviewer/references/report-template.md:L3-L151`)
QUESTION PROTOCOL: Written scope approval and stakeholder confirmation. [V] (`skills/security-reviewer/SKILL.md:L33-L43`)
VALIDATION: Named scanners plus manual review; none run. [V] (`skills/security-reviewer/SKILL.md:L35-L43`; `references/sast-tools.md:L1-L117`)
AGENT FEATURES REQUIRED: Read/Grep/Glob declared; shell and binaries also needed for listed scans. [V] (`skills/security-reviewer/SKILL.md:L1-L8`, `L35-L40`)
STATE ON DISK: Markdown/JSON report and optional scanner outputs; no resume ledger. [V] (`references/report-template.md:L3-L151`; `references/secret-scanning.md:L6-L35`)
VOCABULARY: `FIND-NNN` example, CVSS, Critical–Info, CWE and OWASP IDs; no requirement-ID mapping. [V] (`skills/security-reviewer/SKILL.md:L90-L99`)
NON-OBVIOUS TECHNIQUES:
- Bound tests to written authorization and proof-of-concept. [V] (`skills/security-reviewer/SKILL.md:L33-L43`, `L71-L79`)
- Separate report counts, detailed findings and scan outputs. [V] (`references/report-template.md:L3-L151`)
- IDOR examples check resource ownership. [V] (`references/vulnerability-patterns.md:L72-L89`)
FAILURE MODE FOUGHT: Scanner-only reviews, unauthorized tests, unlocated or unremediated findings. [V] (`skills/security-reviewer/SKILL.md:L31-L79`)
BAGGAGE: Tool-heavy web/cloud examples; external scanner installs.
RISKS: Active scans can affect systems; authorization is required. [V] (`skills/security-reviewer/SKILL.md:L33-L43`; `references/penetration-testing.md:L3-L31`, `L208-L217`)
FIT: security — **ADAPT** scope, locations and report; use P0–P3 and offline fallbacks. [I] (`skills/security-reviewer/SKILL.md:L31-L43`, `L57-L88`)
CONFLICTS: Mandatory scans conflict with optional-binary policy. [V] (`skills/security-reviewer/SKILL.md:L35-L43`)
KEY QUOTES: None.
CONFIDENCE: High for documented guidance; no tool or penetration test was run.
