# obra/superpowers / verification-before-completion
SOURCE: commit `22f0b463e7a5e579904dd6211a520321035526f7` | MIT, root `LICENSE` | 120 lines (`wc -l`)
FRONTMATTER: `name: verification-before-completion`; `description: Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and confirming output before making any success claims; evidence before assertions always`
FILES READ:
| Path | Lines | Role |
|---|---:|---|
| `skills/verification-before-completion/SKILL.md` | 120 | Procedure |
FILES UNREAD: None referenced.
JOB: Require fresh evidence before completion/pass claims, commits, PRs, delegation, or next task. [V] (`skills/verification-before-completion/SKILL.md:L14-L36`, `L106-L120`)
PROCEDURE: Gate: identify proving command → run full command → read output/exit/count → verify claim → report evidence. [V] (`skills/verification-before-completion/SKILL.md:L22-L36`)
DECISION RULES: If output does not confirm claim, state actual status; partial checks, prior runs, and agent success reports are insufficient. [V] (`skills/verification-before-completion/SKILL.md:L22-L48`)
ARTIFACT SHAPE: None prescribed; report claim plus command evidence.
QUESTION PROTOCOL: n/a.
VALIDATION: Human executes repository-native command and reads full output; no validator/tool script. [V] (`skills/verification-before-completion/SKILL.md:L22-L36`)
AGENT FEATURES REQUIRED: Shell/test runner; independent diff review when validating agent work.
STATE ON DISK: No state file.
VOCABULARY: Fresh, full verification; no severity, stable IDs, or requirement-linked checks.
NON-OBVIOUS TECHNIQUES:
- Revert fix and rerun regression test to prove it fails before restoring fix. [V] (`skills/verification-before-completion/SKILL.md:L84-L91`)
- Re-read plan and verify requirements individually. [V] (`skills/verification-before-completion/SKILL.md:L96-L102`)
- Check diff and verify agent output independently. [V] (`skills/verification-before-completion/SKILL.md:L103-L105`)
FAILURE MODE FOUGHT: Success claims based on confidence, stale runs, partial checks, or agent report alone. [V] (`skills/verification-before-completion/SKILL.md:L50-L59`)
BAGGAGE: Universal freshness gate can force unnecessary full verification before delegation or every task transition. [I]
RISKS: Blanket full-command requirement may overshoot targeted validation; “ANY” satisfaction/positive statement can interrupt workflow. [V] (`skills/verification-before-completion/SKILL.md:L22-L36`, `L50-L59`, `L106-L120`)
FIT: sdlc-process: **ADAPT** evidence-before-claim checklist from `SKILL.md`; scope checks to changed behavior and avoid needless reruns. [I]
CONFLICTS: Fresh evidence principle fits; treating every delegation/task transition as a hard gate may slow single-agent work. [V] (`skills/verification-before-completion/SKILL.md:L106-L120`)
KEY QUOTES:
- “NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE” — `skills/verification-before-completion/SKILL.md:L16-L18`
CONFIDENCE: High.
