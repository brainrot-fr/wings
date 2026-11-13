# obra/superpowers / requesting-code-review

SOURCE: `skills/requesting-code-review/SKILL.md` | commit `22f0b463e7a5e579904dd6211a520321035526f7` | MIT | 314 lines read
FRONTMATTER: `name: requesting-code-review`; `description: Use when completing tasks, implementing major features, or before merging to verify work meets requirements`
FILES READ:
| Path | Lines |
|---|---:|
| `skills/requesting-code-review/SKILL.md` | 95 |
| `skills/requesting-code-review/code-reviewer.md` | 198 |
| `LICENSE` | 21 |
FILES UNREAD: None referenced locally.
JOB: Dispatch a fresh reviewer with the exact implementation, requirements and git range rather than session history. [V] (`skills/requesting-code-review/SKILL.md:L1-L42`)
PROCEDURE: Capture base/head, fill reviewer prompt, evaluate findings, fix Critical/Important and record Minors. [V] (`skills/requesting-code-review/SKILL.md:L25-L66`)
DECISION RULES: Review is mandatory after major work and before merge; template requires read-only review and no nested subagents. [V] (`skills/requesting-code-review/SKILL.md:L8-L24`; `skills/requesting-code-review/code-reviewer.md:L24-L54`)
ARTIFACT SHAPE: Strengths, severity-grouped issues, recommendations, merge readiness and reasoning. [V] (`skills/requesting-code-review/code-reviewer.md:L75-L150`)
QUESTION PROTOCOL: Push back only with technical evidence; unresolved integration decisions remain with the user. [V] (`skills/requesting-code-review/SKILL.md:L55-L74`)
VALIDATION: Reviewer checks plan alignment, tests, production readiness and file:line evidence; review is read-only. [V] (`skills/requesting-code-review/code-reviewer.md:L24-L121`)
AGENT FEATURES REQUIRED: General-purpose reviewer subagent is the core mechanism. [V] (`skills/requesting-code-review/SKILL.md:L25-L42`)
STATE ON DISK: Git SHAs/range and review output; no durable issue ledger is prescribed.
VOCABULARY: Base/head SHA, critical/important/minor, plan alignment, read-only review, declined-to-judge.
NON-OBVIOUS TECHNIQUES: Require a list of considered-but-set-aside behaviors; judge against user expectations where the spec is silent. [V] (`skills/requesting-code-review/code-reviewer.md:L38-L75`)
FAILURE MODE FOUGHT: Self-review bias, vague context, ungrounded findings and severity inflation. [V] (`skills/requesting-code-review/SKILL.md:L1-L24`; `skills/requesting-code-review/code-reviewer.md:L75-L150`)
BAGGAGE: Requires a fresh context and a sufficiently capable reviewer; this costs an additional agent pass.
RISKS: Template asks reviewers to inspect diffs; it explicitly forbids mutating the checkout or spawning further reviewers. [V] (`skills/requesting-code-review/code-reviewer.md:L24-L54`)
FIT: SDLC — **ADAPT** bounded read-only review input and severity calibration; reuse reviewer tools where available. [I]
CONFLICTS: Skill recommends subagent dispatch while its template forbids reviewer-side dispatch; these are compatible if the parent is the only dispatcher. [V] (`skills/requesting-code-review/SKILL.md:L25-L42`; `skills/requesting-code-review/code-reviewer.md:L55-L67`)
KEY QUOTES: None.
CONFIDENCE: High; target, linked reviewer prompt and root license read.
