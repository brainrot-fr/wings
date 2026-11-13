# wshobson/agents / wcag-audit-patterns

SOURCE: `plugins/accessibility-compliance/skills/wcag-audit-patterns/SKILL.md` | commit `9c61ab243def98f72da12abd41cfcf5bcd91af9d` | MIT | 573 lines read
FRONTMATTER:
```yaml
name: wcag-audit-patterns
description: Conduct WCAG 2.2 accessibility audits with automated testing, manual verification, and remediation guidance. Use when auditing websites for accessibility, fixing WCAG violations, or implementing accessible design patterns.
```
FILES READ:
| Path | Lines | Role |
|---|---:|---|
| `plugins/accessibility-compliance/skills/wcag-audit-patterns/SKILL.md` | 80 | Overview and audit approach |
| `plugins/accessibility-compliance/skills/wcag-audit-patterns/references/details.md` | 473 | Checklist, automation and fixes |
| `LICENSE` | 20 | Root license |
FILES UNREAD: None referenced locally.
JOB: Audit WCAG 2.2 accessibility with automated checks, manual verification and remediation patterns. [V] (`plugins/accessibility-compliance/skills/wcag-audit-patterns/SKILL.md:L3-L18`)
PROCEDURE: Organize by POUR principles and conformance level; check common issues, use available automation, then manually verify and remediate. [V] (`plugins/accessibility-compliance/skills/wcag-audit-patterns/SKILL.md:L19-L78`; `plugins/accessibility-compliance/skills/wcag-audit-patterns/references/details.md:L3-L28`, `L360-L399`)
DECISION RULES: Native semantic HTML before ARIA; automate only detectable issues, and do not rely on automated results alone. [V] (`plugins/accessibility-compliance/skills/wcag-audit-patterns/SKILL.md:L64-L78`)
ARTIFACT SHAPE: Checklist by success criterion, automated findings, manual verification and remediation examples; no report template. [V] (`plugins/accessibility-compliance/skills/wcag-audit-patterns/references/details.md:L3-L28`, `L360-L399`, `L401-L472`)
QUESTION PROTOCOL: None.
VALIDATION: axe-core example filters WCAG tags; CLI options include axe, pa11y and Lighthouse. Manual keyboard/assistive-technology checks remain required. No tools were run. [V] (`plugins/accessibility-compliance/skills/wcag-audit-patterns/SKILL.md:L64-L78`; `plugins/accessibility-compliance/skills/wcag-audit-patterns/references/details.md:L360-L399`)
AGENT FEATURES REQUIRED: None.
STATE ON DISK: No workflow state or output path.
VOCABULARY: WCAG 2.2; A/AA/AAA; POUR; contrast; keyboard access; name/role/value; status messages. [V] (`plugins/accessibility-compliance/skills/wcag-audit-patterns/SKILL.md:L19-L58`; `plugins/accessibility-compliance/skills/wcag-audit-patterns/references/details.md:L91-L123`, `L322-L359`)
NON-OBVIOUS TECHNIQUES:
- Contrast thresholds: 4.5:1 for text, 3:1 for large text and UI components. [V] (`plugins/accessibility-compliance/skills/wcag-audit-patterns/references/details.md:L97-L123`)
- Use axe-core for automated tags but supplement with keyboard, focus, reflow and manual assistive-tech checks. [V] (`plugins/accessibility-compliance/skills/wcag-audit-patterns/references/details.md:L136-L151`, `L360-L399`)
- WCAG 2.2 marks Parsing (4.1.1) obsolete; do not count it as a 2.2 failure. [V] (`plugins/accessibility-compliance/skills/wcag-audit-patterns/references/details.md:L322-L332`)
FAILURE MODE FOUGHT: Automated-only audits, inaccessible keyboard/focus behavior, missing semantic labels and contrast issues. [V] (`plugins/accessibility-compliance/skills/wcag-audit-patterns/SKILL.md:L38-L78`; `plugins/accessibility-compliance/skills/wcag-audit-patterns/references/details.md:L91-L151`)
BAGGAGE: Scope is web accessibility; no severity rubric or finding/report schema is defined.
RISKS: CLI examples resolve external packages and target example URLs; snippets/tools were not run. The claimed 30–50% automation rate has no supporting citation in the skill. [V] (`plugins/accessibility-compliance/skills/wcag-audit-patterns/SKILL.md:L64-L72`; `plugins/accessibility-compliance/skills/wcag-audit-patterns/references/details.md:L360-L399`)
FIT: testing — **ADAPT** criterion checklist and manual/automated split; add finding severity, owner, evidence and requirement traceability. [I]
CONFLICTS: The source labels 4.1.1 Parsing Level A but correctly notes it is obsolete in WCAG 2.2; consumers must scope criteria to the adopted standard/version. [V] (`plugins/accessibility-compliance/skills/wcag-audit-patterns/references/details.md:L322-L332`)
KEY QUOTES: None.
CONFIDENCE: High; complete skill, linked details and root license read; no audit commands run.
