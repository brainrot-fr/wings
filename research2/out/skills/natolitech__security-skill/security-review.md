# natolitech/security-skill / security-review
SOURCE: commit `3bdb1dc1922902a8907821ea663f0bbbfea79728` | MIT, root `LICENSE` | 501 lines
FRONTMATTER: `name: security-review`; `description: Application security review of a codebase, a directory, a diff/PR, or a git repository URL. Use when asked for a security review, vulnerability review, secure code review, or static security analysis of an application or repo.`
FILES READ:
| Path | Lines | Role |
|---|---:|---|
| `.claude/commands/security-review.md` | 501 | Command |
FILES UNREAD: None in command; external OWASP/CWE material not retrieved.
JOB: Static review of a project, directory, diff, PR, or repo URL; writes timestamped report/JSON and local triage backlog. [V] (`.claude/commands/security-review.md:L3-L4`, `.claude/commands/security-review.md:L435-L488`)
PROCEDURE:
1. `Step 1: Reconnaissance`: map stack, entrypoints, sensitive operations and prior review. [V] (`.claude/commands/security-review.md:L27-L65`)
2. `Step 2: Vulnerability Analysis`: trace 20 named vulnerability classes. [V] (`.claude/commands/security-review.md:L67-L283`)
3. `Step 3: Contextual Threat Assessment`; `Step 4: Verification Pass`: assess impact, search controls, downgrade uncertainty. [V] (`.claude/commands/security-review.md:L284-L303`)
4. `Step 5: Report Findings`: source-backed `SR-NNN` records. [V] (`.claude/commands/security-review.md:L304-L336`)
DECISION RULES: Confidence Confirmed/Likely/Suspected; severity Critical/High/Medium/Low/Informational. URL clones are shallow. [V] (`.claude/commands/security-review.md:L323-L347`, `.claude/commands/security-review.md:L406-L417`)
ARTIFACT SHAPE: Report sections include summary, severity groups, positives and recommendations; findings carry location, category, confidence, evidence, remediation. [V] (`.claude/commands/security-review.md:L306-L392`)
QUESTION PROTOCOL: Invocation scope; defaults to full project. [V] (`.claude/commands/security-review.md:L394-L404`)
VALIDATION: Manual trace/control search; no bundled checker. Scanner follow-up only. [V] (`.claude/commands/security-review.md:L15-L24`, `.claude/commands/security-review.md:L293-L303`)
AGENT FEATURES REQUIRED: Shell for source and report; no subagents or hooks.
STATE ON DISK: Timestamped Markdown/JSON; local backlog. [V] (`.claude/commands/security-review.md:L435-L488`)
VOCABULARY: IDs `SR-NNN`; status `open|confirmed|false-positive|risk-accepted|resolved`; five severities and three confidence levels. [V] (`.claude/commands/security-review.md:L309-L347`, `.claude/commands/security-review.md:L435-L455`)
NON-OBVIOUS TECHNIQUES:
- Cross-check apparent vulnerabilities against upstream controls. [V] (`.claude/commands/security-review.md:L293-L303`)
- Compare prior findings by file/nature, not line number. [V] (`.claude/commands/security-review.md:L419-L434`)
- Shallow clone limits secret-history claims. [V] (`.claude/commands/security-review.md:L406-L417`)
FAILURE MODE FOUGHT: Checklist findings, false positives, and stale triage. [I] (`.claude/commands/security-review.md:L67-L70`, `.claude/commands/security-review.md:L293-L303`)
BAGGAGE: Append-only backlog; remote clone; severity scale differs from P0–P3. [V] (`.claude/commands/security-review.md:L406-L417`, `.claude/commands/security-review.md:L435-L488`)
RISKS: URL cloning uses network; partial secret excerpts are requested, forbidden by this pass. [V] (`.claude/commands/security-review.md:L406-L417`, `.claude/commands/security-review.md:L329-L334`)
FIT: security — **ADAPT** source verification and prior-finding comparison; replace severity/confidence with house vocabulary. [I] (`.claude/commands/security-review.md:L293-L347`, `.claude/commands/security-review.md:L419-L434`)
CONFLICTS: Severity combines priority and confidence; the task requires these separate.
KEY QUOTES:
- “False positives erode trust in real findings.” — `.claude/commands/security-review.md:L301-L303`
CONFIDENCE: High for documented process; not executed.
