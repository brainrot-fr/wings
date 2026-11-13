# addyosmani/agent-skills / code-review-and-quality

SOURCE: `skills/code-review-and-quality/SKILL.md` | commit `301b02b12bff98e4688e6984af6556802322bbde` | MIT | 908 lines read
FRONTMATTER: `name: code-review-and-quality`; `description: Conducts multi-axis code review. Use before merging any change. Use when reviewing code written by yourself, another agent, or a human. Use when you need to assess code quality across multiple dimensions before it enters the main branch. Use when asked to review a diff or a pull request, even when the diff is pasted inline.`
FILES READ:
| Path | Lines |
|---|---:|
| `skills/code-review-and-quality/SKILL.md` | 400 |
| `references/security-checklist.md` | 248 |
| `references/performance-checklist.md` | 239 |
| `LICENSE` | 21 |
FILES UNREAD: Named `security-and-hardening` and `performance-optimization` skills are optional deep dives, not opened.
JOB: Review correctness, readability, architecture, security and performance before merge. [V] (`skills/code-review-and-quality/SKILL.md:L1-L80`)
PROCEDURE: Understand intent, review tests, inspect implementation, filter findings against callers/tests, label severity, verify evidence and dependencies. [V] (`skills/code-review-and-quality/SKILL.md:L178-L278`)
DECISION RULES: Approve if code health improves; report zero findings when warranted; distinguish base defects from regressions; use Critical/Required/Optional/Nit labels. [V] (`skills/code-review-and-quality/SKILL.md:L1-L18`, `L220-L278`)
ARTIFACT SHAPE: Review checklist with context, five axes, findings, verification and verdict. [V] (`skills/code-review-and-quality/SKILL.md:L350-L400`)
QUESTION PROTOCOL: Ask before removing potentially dead code; otherwise surface disagreements with technical evidence. [V] (`skills/code-review-and-quality/SKILL.md:L280-L322`)
VALIDATION: Review test intent, run evidence, build, manual checks and screenshots; mutation probe is proposed for review tests. [V] (`skills/code-review-and-quality/SKILL.md:L190-L218`, `L230-L278`)
AGENT FEATURES REQUIRED: Multi-model review is recommended; not mandatory for the five-axis checklist. [V] (`skills/code-review-and-quality/SKILL.md:L294-L305`)
STATE ON DISK: Review comments/checklist only; no persistent ledger specified.
VOCABULARY: Five axes; structural remedy; Critical/Required/Optional/Nit; mutation; base defect vs regression. [V] (`skills/code-review-and-quality/SKILL.md:L20-L80`, `L220-L278`)
NON-OBVIOUS TECHNIQUES: Grade findings against callers/guards/tests; propose structural remedies, not just symptoms; assess resulting file size, not only diff size. [V] (`skills/code-review-and-quality/SKILL.md:L90-L178`, `L220-L242`)
FAILURE MODE FOUGHT: Rubber-stamping, nit-heavy reviews, false positives and structural complexity relocation. [V] (`skills/code-review-and-quality/SKILL.md:L220-L305`)
BAGGAGE: 100/300/1000-line sizing and review cadence are heuristics.
RISKS: Recommends source mutation to test quality and `npm audit`; these can affect the working tree or access registries. No tools were run. [V] (`skills/code-review-and-quality/SKILL.md:L190-L218`, `L322-L350`)
FIT: SDLC — **ADAPT** evidence-based findings and structural remedies; gate any mutation test with a safe-copy/restore plan. [I]
CONFLICTS: Every-change review and mutation examples can overreach small-risk changes; use project risk policy. [I]
KEY QUOTES: None.
CONFIDENCE: High; target, direct security/performance references and license read.
