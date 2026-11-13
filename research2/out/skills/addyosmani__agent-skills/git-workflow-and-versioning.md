# addyosmani/agent-skills / git-workflow-and-versioning

SOURCE: `skills/git-workflow-and-versioning/SKILL.md` | commit `301b02b12bff98e4688e6984af6556802322bbde` | MIT | 1112 lines read
FRONTMATTER: `name: git-workflow-and-versioning`; `description: Structures git workflow practices. Use when making any code change. Use when committing, branching, resolving conflicts, splitting uncommitted work in a messy working tree into clean atomic commits, opening or reviewing a pull request (PR), pushing to a remote, or when you need to organize work across multiple parallel streams. Use when cutting a release, choosing a semantic version bump, tagging, or writing a changelog. Use when asked to write a commit message or a changelog entry for a change, or to split a change into commits, even when the diff is pasted inline and the message seems easy to write from it.`
FILES READ:
| Path | Lines |
|---|---:|
| `skills/git-workflow-and-versioning/SKILL.md` | 355 |
| `skills/code-review-and-quality/SKILL.md` | 400 |
| `skills/shipping-and-launch/SKILL.md` | 336 |
| `LICENSE` | 21 |
FILES UNREAD: No additional local files linked by this target.
JOB: Govern commits, branches, worktrees, PRs, conflict handling and releases. [V] (`skills/git-workflow-and-versioning/SKILL.md:L1-L80`)
PROCEDURE: Commit tested increments atomically; use short-lived branches/worktrees; keep concerns separate; tag immutable releases and curate changelogs. [V] (`skills/git-workflow-and-versioning/SKILL.md:L38-L190`, `L250-L334`)
DECISION RULES: Trunk-based short-lived branches are recommended, but teams can adapt; SemVer follows consumer-visible compatibility. [V] (`skills/git-workflow-and-versioning/SKILL.md:L28-L70`, `L270-L316`)
ARTIFACT SHAPE: Atomic commits with why/context, clean branch/PR history, version tag and impact-grouped changelog. [V] (`skills/git-workflow-and-versioning/SKILL.md:L74-L126`, `L294-L334`)
QUESTION PROTOCOL: Conflicts and messy uncommitted work should be inspected and summarized rather than auto-reorganized. [V] (`skills/git-workflow-and-versioning/SKILL.md:L166-L240`)
VALIDATION: Pre-commit diff/secret-name review, tests, lint, typecheck; review size and release/tag alignment. [V] (`skills/git-workflow-and-versioning/SKILL.md:L189-L230`, `L320-L355`)
AGENT FEATURES REQUIRED: Worktrees support independent parallel agents; no agent is required. [V] (`skills/git-workflow-and-versioning/SKILL.md:L140-L165`)
STATE ON DISK: Git history, branches, tags, worktrees and changelog; no task ledger. [V] (`skills/git-workflow-and-versioning/SKILL.md:L74-L190`, `L294-L334`)
VOCABULARY: Atomic commit, trunk-based, worktree, feature flag, SemVer, changelog, save point. [V] (`skills/git-workflow-and-versioning/SKILL.md:L28-L190`, `L250-L334`)
NON-OBVIOUS TECHNIQUES: Pass untrusted rollback version through an environment variable, not inline into shell; derive release version from immutable tag. [V] (`skills/git-workflow-and-versioning/SKILL.md:L225-L240`, `L294-L316`)
FAILURE MODE FOUGHT: Giant mixed commits, long-lived branches, unreviewed changes and hand-edited version drift. [V] (`skills/git-workflow-and-versioning/SKILL.md:L38-L126`, `L270-L334`)
BAGGAGE: Recommends a 1–3 day feature-branch window and ~100-line commit size as heuristics.
RISKS: Examples include `git reset --hard`, `git push`, `git pull` and worktree removal; inspect scope and obtain authorization before destructive/shared effects. [V] (`skills/git-workflow-and-versioning/SKILL.md:L170-L190`, `L216-L230`)
FIT: SDLC — **ADAPT** atomic history and release provenance; preserve explicit user control of destructive git operations. [I]
CONFLICTS: Universal “every change flows through git” and trunk-based defaults need exceptions for repositories with different policy. [I]
KEY QUOTES: None.
CONFIDENCE: High; target and two linked skills read; git commands not run.
