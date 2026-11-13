# obra/superpowers / finishing-a-development-branch

SOURCE: `skills/finishing-a-development-branch/SKILL.md` | commit `22f0b463e7a5e579904dd6211a520321035526f7` | MIT | 246 lines read
FRONTMATTER: `name: finishing-a-development-branch`; `description: Use when implementation is complete, all tests pass, and you need to decide how to integrate the work`
FILES READ:
| Path | Lines |
|---|---:|
| `skills/finishing-a-development-branch/SKILL.md` | 225 |
| `LICENSE` | 21 |
FILES UNREAD: None directly linked.
JOB: Complete a branch only after tests pass, then ask the user to choose merge, push/PR or keep. [V] (`skills/finishing-a-development-branch/SKILL.md:L1-L48`)
PROCEDURE: Verify tests, detect worktree state, identify base, present exact options, execute only the chosen path, clean up only owned worktrees. [V] (`skills/finishing-a-development-branch/SKILL.md:L8-L87`, `L90-L225`)
DECISION RULES: Never discard without typed `discard`; never force-remove uncommitted files; confirm base branch before merge. [V] (`skills/finishing-a-development-branch/SKILL.md:L38-L72`, `L132-L194`)
ARTIFACT SHAPE: User choice menu, merge/PR/keep outcome, test result and preserved/cleaned worktree state. [V] (`skills/finishing-a-development-branch/SKILL.md:L38-L132`)
QUESTION PROTOCOL: Wait for explicit integration choice; destructive discard requires exact confirmation. [V] (`skills/finishing-a-development-branch/SKILL.md:L38-L72`, `L132-L158`)
VALIDATION: Full suite before integration and again after local merge; failed merged tests stop cleanup. [V] (`skills/finishing-a-development-branch/SKILL.md:L8-L32`, `L90-L132`)
AGENT FEATURES REQUIRED: Forge tooling only if user selects push/PR; none for keep-as-is.
STATE ON DISK: Branch, worktree registration and git history; host-managed workspaces are left intact. [V] (`skills/finishing-a-development-branch/SKILL.md:L18-L37`, `L160-L225`)
VOCABULARY: Base branch, merge base, worktree, detached HEAD, discard, provenance-based cleanup. [V] (`skills/finishing-a-development-branch/SKILL.md:L18-L87`, `L160-L225`)
NON-OBVIOUS TECHNIQUES: Classify cleanup ownership by `.worktrees/` path; never use force when removal exposes unique uncommitted files. [V] (`skills/finishing-a-development-branch/SKILL.md:L160-L194`)
FAILURE MODE FOUGHT: Merging wrong base, deleting uncommitted work, force-pushing and removing host-owned workspaces. [V] (`skills/finishing-a-development-branch/SKILL.md:L38-L72`, `L90-L225`)
BAGGAGE: Requires a user decision at integration; exact menu is lengthy but preserves ownership.
RISKS: Includes `git pull`, push, merge, branch deletion and worktree removal; none are run without authorization. [V] (`skills/finishing-a-development-branch/SKILL.md:L90-L194`)
FIT: SDLC — **EXTRACT** user-controlled integration and ownership-aware cleanup; preserve explicit stop gates. [I]
CONFLICTS: It says delete the plan workspace after review; only delete a resolved path owned by that plan. [V] (`skills/finishing-a-development-branch/SKILL.md:L160-L225`)
KEY QUOTES: None.
CONFIDENCE: High; complete skill and root license read; no git operation run.
