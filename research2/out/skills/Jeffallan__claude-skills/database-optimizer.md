# Jeffallan/claude-skills / database-optimizer
SOURCE: `skills/database-optimizer/SKILL.md` | commit `078a25cc5bfd8011459be7b91d004e900c1d02d3` | MIT (`license: MIT` frontmatter; root `LICENSE`; no separate per-skill notice found) | 2121 total lines read (`wc -l`)
FRONTMATTER:
`name: database-optimizer`
`description: Optimizes database queries and improves performance across PostgreSQL and MySQL systems. Use when investigating slow queries, analyzing execution plans, or optimizing database performance. Invoke for index design, query rewrites, configuration tuning, partitioning strategies, lock contention resolution.`
FILES READ:
| Path | Lines | Role |
|---|---:|---|
| `skills/database-optimizer/SKILL.md` | 152 | Workflow and examples |
| `skills/database-optimizer/references/query-optimization.md` | 251 | Plans and rewrites |
| `skills/database-optimizer/references/index-strategies.md` | 331 | Index choice and maintenance |
| `skills/database-optimizer/references/postgresql-tuning.md` | 413 | PostgreSQL settings |
| `skills/database-optimizer/references/mysql-tuning.md` | 452 | MySQL settings |
| `skills/database-optimizer/references/monitoring-analysis.md` | 501 | Metrics and alerts |
| `LICENSE` | 21 | Root license |
FILES UNREAD: None referenced.
JOB: Diagnose PostgreSQL/MySQL performance from plans and monitoring metrics; output is analysis plus proposed SQL/configuration, not a named file. [V] (`skills/database-optimizer/SKILL.md:L16-L28`, `L140-L147`)
PROCEDURE:
1. **Analyze Performance**: capture baseline and `EXPLAIN ANALYZE`.
2. **Identify Bottlenecks** and **Design Solutions** from plans and workload.
3. **Implement Changes** incrementally; **Validate Results** against baseline. [V] (`skills/database-optimizer/SKILL.md:L30-L38`)
DECISION RULES: No simultaneous changes; stage first and revert if writes degrade or replication lag rises. Alerts mark connections above 80% WARNING/90% CRITICAL and cache below 95% WARNING/90% CRITICAL. [V] (`skills/database-optimizer/SKILL.md:L123-L138`; `skills/database-optimizer/references/monitoring-analysis.md:L417-L455`)
ARTIFACT SHAPE: Baseline, bottlenecks/root causes, changes, implementation SQL/config, validation queries, monitoring advice. [V] (`skills/database-optimizer/SKILL.md:L140-L147`)
QUESTION PROTOCOL: n/a.
VALIDATION: Compare before/after `EXPLAIN (ANALYZE, BUFFERS)`, cost, time, and index use. Measurement is deterministic; diagnosis judgment-based. [V] (`skills/database-optimizer/SKILL.md:L32-L38`; `skills/database-optimizer/references/query-optimization.md:L232-L251`)
AGENT FEATURES REQUIRED: SQL/database access implied; no agent integrations named. [I]
STATE ON DISK: No state file/output path; six-part response template only. [V] (`skills/database-optimizer/SKILL.md:L140-L147`)
VOCABULARY: `EXPLAIN ANALYZE`, `BUFFERS`, `Seq Scan`, B-tree/GIN/GiST, `work_mem`; no severity scale surfaced. [I]
NON-OBVIOUS TECHNIQUES:
- Choose multi-column indexes by equality, range, selectivity and query pattern. [V] (`skills/database-optimizer/references/index-strategies.md:L47-L80`)
- Use keyset pagination for deep offsets and index the cursor ordering. [V] (`skills/database-optimizer/references/query-optimization.md:L201-L219`)
- Flag stale statistics by estimated-versus-actual rows; use `ANALYZE`. [V] (`skills/database-optimizer/SKILL.md:L66-L76`)
FAILURE MODE FOUGHT: Guesswork, redundant indexes, unmeasured regressions and missed write/replication costs. [V] (`skills/database-optimizer/SKILL.md:L123-L138`)
BAGGAGE: Vendor-specific, production-oriented tuning.
RISKS: References include live setting changes, stats resets, and session durability changes; only stage-tested, reviewed SQL should be applied. [V] (`skills/database-optimizer/references/postgresql-tuning.md:L155-L168`; `skills/database-optimizer/references/monitoring-analysis.md:L3-L13`)
FIT: database — **EXTRACT** baseline/measure/revert loop, query-plan reading, and index decision process; retain references as optional context. [I]
CONFLICTS: Direct database access and changes need optional execution and a non-production gate. [I]
KEY QUOTES: None.
CONFIDENCE: High; complete skill, all five references and root license read; no SQL executed.
