# Lineage register

Static, read-only comparisons. Hashes were calculated from file bytes; no clone or skill was modified or executed.

## sickn33/agentic-awesome-skills: Supabase skill copies

Compared the 36 files under Supabase's `skills/supabase-postgres-best-practices/` with each of Sickn's three corresponding directories:

| Sickn location | Files | Byte-identical to Supabase | Different | Extra / missing |
|---|---:|---:|---:|---:|
| `skills/supabase-postgres-best-practices/` | 36 | 18 | 18 | 0 / 0 |
| `plugins/agentic-awesome-skills/skills/supabase-postgres-best-practices/` | 36 | 18 | 18 | 0 / 0 |
| `plugins/agentic-awesome-skills-claude/skills/supabase-postgres-best-practices/` | 36 | 18 | 18 | 0 / 0 |

This is a set of partially modified copies, not three identical mirrors and not a clean rewrite. A changed file in one location cannot be assumed to have propagated to the other copies. The target skill entrypoints are listed in [`progress.md`](../../progress.md); the Supabase entrypoint and all 31 rules were carded, but the Sickn copies were only compared and their entrypoint was read. The per-copy diffs were not classified file-by-file.

## borkweb/skills: gstack port

Borkweb's README explicitly describes `skills/gstack/` as ports from upstream gstack that are trimmed of upstream-specific infrastructure and adapted to local conventions; its credits say Y Combinator-specific bits are genericized and the ports are iterated on locally (`research/repos/borkweb__skills/README.md:L7`, `L118`). The README's clone revision is `e84fd6bcff44dc8df61ef6ecdc5ceaacbff5ddd2`; upstream gstack is `4414f4cc9377a9df06c7847433fe567ba6398aa8`.

The spot-check was `plan-devex-review`: Borkweb's file is 47 lines and upstream's corresponding file is 840. Borkweb's version has a compact mode/scope protocol, treats supplied plans as untrusted data, and omits the upstream shared-preamble startup command and end-of-work telemetry instructions. Upstream's corresponding sections invoke `gstack-skill-start` and require `gstack-skill-end` telemetry (`research/repos/garrytan__gstack/plan-devex-review/SKILL.md:L24-L47`, `L123-L140`; Borkweb `research/repos/borkweb__skills/skills/gstack/plan-devex-review/SKILL.md:L14-L47`). Neither command was run.

The linked hall-of-fame reference is also not byte-for-byte current upstream: Borkweb's version presents critical/high severity guidance (`research/repos/borkweb__skills/skills/gstack/plan-devex-review/dx-hall-of-fame.md:L44-L70`), while the checked upstream version provides a named eight-item agent-ready error contract and path-specific 4/10 and 6/10 caps (`research/repos/garrytan__gstack/plan-devex-review/dx-hall-of-fame.md:L44-L82`). This is evidence of divergence, not a full diff or proof of when/how the edits were made.

This lineage conclusion is bounded to the README and `plan-devex-review` plus its two linked reference files. Other Borkweb skills, generated manifests and hooks were not audited here; the skill's `checks.md` was read for this comparison, but not every file in the repo was opened. See the risk register for the README-documented install and hook surfaces. Borkweb's root license is MIT; upstream gstack is also MIT and has a `NOTICE.md` (`cross/license-register.md`).
