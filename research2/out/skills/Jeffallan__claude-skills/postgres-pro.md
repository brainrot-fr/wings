# Jeffallan/claude-skills / postgres-pro
SOURCE: `skills/postgres-pro/SKILL.md` | commit `078a25cc5bfd8011459be7b91d004e900c1d02d3` | MIT (`license: MIT` frontmatter; root `LICENSE`; no separate per-skill notice found) | 2095 total lines read (`wc -l`)
FRONTMATTER:
`name: postgres-pro`
`description: Use when optimizing PostgreSQL queries, configuring replication, or implementing advanced database features. Invoke for EXPLAIN analysis, JSONB operations, extension usage, VACUUM tuning, performance monitoring.`
FILES READ:
| Path | Lines | Role |
|---|---:|---|
| `skills/postgres-pro/SKILL.md` | 157 | Workflow and examples |
| `skills/postgres-pro/references/performance.md` | 265 | Plans, indexes and tuning |
| `skills/postgres-pro/references/jsonb.md` | 321 | JSONB operations |
| `skills/postgres-pro/references/extensions.md` | 404 | Extension use cases |
| `skills/postgres-pro/references/replication.md` | 446 | HA, backup and recovery |
| `skills/postgres-pro/references/maintenance.md` | 481 | Vacuum and monitoring |
| `LICENSE` | 21 | Root license |
FILES UNREAD: None referenced.
JOB: Advise on PostgreSQL performance, JSONB, replication, extensions and maintenance; output is SQL/configuration and monitoring recommendations, no named file. [V] (`skills/postgres-pro/SKILL.md:L16-L29`, `L142-L149`)
PROCEDURE:
1. **Analyze performance** with `EXPLAIN (ANALYZE, BUFFERS)`.
2. **Design indexes**, **Optimize queries**, and verify before deployment.
3. **Setup replication** for requirements; **Monitor and maintain** lag, VACUUM and bloat. [V] (`skills/postgres-pro/SKILL.md:L31-L37`)
DECISION RULES: Autovacuum triggers at threshold + scale_factor × tuples (example: 50 + 0.2 × 1M = 200050); wraparound distance should stay under 1 billion. `jsonb_path_ops` optimizes containment but not `?`. [V] (`skills/postgres-pro/references/maintenance.md:L66-L72`, `L396-L402`; `skills/postgres-pro/references/jsonb.md:L110-L120`)
ARTIFACT SHAPE: Query/plan interpretation; index rationale and pre/post verification; config deltas; monitoring queries; impact explanation. [V] (`skills/postgres-pro/SKILL.md:L142-L149`)
QUESTION PROTOCOL: n/a.
VALIDATION: `EXPLAIN`, `pg_stat` and post-change checks; measurements are deterministic, plan/index choice requires judgment. [V] (`skills/postgres-pro/SKILL.md:L31-L37`, `L122-L140`)
AGENT FEATURES REQUIRED: SQL/database access; shell commands for replication setup. [V] (`skills/postgres-pro/references/replication.md:L31-L56`)
STATE ON DISK: Config, `pg_hba.conf`, standby/recovery signals and backups appear in examples. [V] (`skills/postgres-pro/references/replication.md:L3-L39`, `L368-L390`)
VOCABULARY: `pg_stat_*`, LSN/lag, GIN/GiST/BRIN, JSONB, VACUUM; no severity scale surfaced. [I]
NON-OBVIOUS TECHNIQUES:
- Pick `jsonb_path_ops` only for containment-only workloads; use a separate table for arrays over 10k elements. [V] (`skills/postgres-pro/references/jsonb.md:L110-L120`, `L280-L290`)
- Compare lag and retained WAL on primary and replay state on standby. [V] (`skills/postgres-pro/references/replication.md:L54-L77`)
- Use `VACUUM FULL` cautiously because it locks; reference offers `pg_repack` as online alternative. [V] (`skills/postgres-pro/references/maintenance.md:L17-L23`, `L197-L203`)
FAILURE MODE FOUGHT: Slow plans, unused indexes, bloat, stale statistics and unobserved replication lag. [V] (`skills/postgres-pro/SKILL.md:L120-L140`)
BAGGAGE: PostgreSQL-only; assumes config access and optional extensions/utilities.
RISKS: Replication/PITR examples delete data-directory contents and install a failover package; review before execution. [V] (`skills/postgres-pro/references/replication.md:L31-L45`, `L237-L247`, `L368-L380`)
FIT: database — **EXTRACT** plan/index and maintenance guidance; keep vendor/extension instructions optional and version-scoped. [I]
CONFLICTS: Examples require shell/binaries and include destructive operations, unlike offline-by-default guidance. [V] (`skills/postgres-pro/references/replication.md:L31-L45`, `L237-L247`)
KEY QUOTES: None.
CONFIDENCE: High; complete skill, all five references and root license read; no commands or SQL executed.
