# supabase/agent-skills / supabase-postgres-best-practices
SOURCE: commit `c9be0e931b7930f7d02126d04774d904c381e7d7` | MIT, root `LICENSE` | 1,751 lines; `find ... -name '*.md' -print0 | xargs -0 wc -l`
FRONTMATTER: `name: supabase-postgres-best-practices`; `description: "Postgres best practices maintained by Supabase, for Postgres running anywhere. Load this skill BEFORE writing or changing anything that lives in a Postgres database: creating or altering tables and columns (including choosing column types), schema design, migrations and declarative schema files, RLS policies and the tests that verify them, indexes, triggers, database functions, queues and scheduled jobs (pg_cron, pgmq), vector/semantic search (pgvector), and restoring dumps (pg_restore) or importing data. Also load it when diagnosing slow queries, high CPU, timeouts, EXPLAIN plans, connection exhaustion, locking, bloat, or rows visible to the wrong user or tenant. This is not just a performance guide — schema, migration, security, and SQL authoring tasks need these rules too, even for a one-column change or a single query."`
FILES READ:
| Path | Lines | Role |
|---|---:|---|
| `skills/supabase-postgres-best-practices/SKILL.md` | 64 | Entry |
| `skills/supabase-postgres-best-practices/references/advanced-full-text-search.md`; `skills/supabase-postgres-best-practices/references/advanced-jsonb-indexing.md` | 55; 49 | Search |
| `skills/supabase-postgres-best-practices/references/conn-idle-timeout.md`; `skills/supabase-postgres-best-practices/references/conn-limits.md`; `skills/supabase-postgres-best-practices/references/conn-pooling.md`; `skills/supabase-postgres-best-practices/references/conn-prepared-statements.md` | 46; 44; 41; 46 | Connections |
| `skills/supabase-postgres-best-practices/references/data-batch-inserts.md`; `skills/supabase-postgres-best-practices/references/data-n-plus-one.md`; `skills/supabase-postgres-best-practices/references/data-pagination.md`; `skills/supabase-postgres-best-practices/references/data-upsert.md` | 54; 53; 50; 50 | Data |
| `skills/supabase-postgres-best-practices/references/lock-advisory.md`; `skills/supabase-postgres-best-practices/references/lock-deadlock-prevention.md`; `skills/supabase-postgres-best-practices/references/lock-short-transactions.md`; `skills/supabase-postgres-best-practices/references/lock-skip-locked.md` | 56; 68; 50; 54 | Locks |
| `skills/supabase-postgres-best-practices/references/monitor-explain-analyze.md`; `skills/supabase-postgres-best-practices/references/monitor-pg-stat-statements.md`; `skills/supabase-postgres-best-practices/references/monitor-vacuum-analyze.md` | 45; 55; 55 | Monitor |
| `skills/supabase-postgres-best-practices/references/query-composite-indexes.md`; `skills/supabase-postgres-best-practices/references/query-covering-indexes.md`; `skills/supabase-postgres-best-practices/references/query-index-types.md`; `skills/supabase-postgres-best-practices/references/query-missing-indexes.md`; `skills/supabase-postgres-best-practices/references/query-partial-indexes.md` | 44; 40; 48; 43; 45 | Query |
| `skills/supabase-postgres-best-practices/references/schema-constraints.md`; `skills/supabase-postgres-best-practices/references/schema-data-types.md`; `skills/supabase-postgres-best-practices/references/schema-foreign-key-indexes.md`; `skills/supabase-postgres-best-practices/references/schema-lowercase-identifiers.md`; `skills/supabase-postgres-best-practices/references/schema-partitioning.md`; `skills/supabase-postgres-best-practices/references/schema-primary-keys.md` | 80; 46; 59; 55; 55; 61 | Schema |
| `skills/supabase-postgres-best-practices/references/security-privileges.md`; `skills/supabase-postgres-best-practices/references/security-rls-basics.md`; `skills/supabase-postgres-best-practices/references/security-rls-performance.md` | 54; 50; 63 | Security |
| `skills/supabase-postgres-best-practices/references/_sections.md`; `skills/supabase-postgres-best-practices/references/_template.md` | 39; 34 | Format |
FILES UNREAD: `skills/supabase-postgres-best-practices/references/_contributing.md` (contrib); `skills/supabase-postgres-best-practices/CHANGELOG.md` (history).
JOB: Route Postgres tasks through 31 category rules. [V] (`skills/supabase-postgres-best-practices/SKILL.md:L26-L64`)
PROCEDURE:
1. Select a category. [V] (`skills/supabase-postgres-best-practices/SKILL.md:L26-L54`)
2. Compare SQL examples. [V] (`skills/supabase-postgres-best-practices/references/schema-constraints.md:L1-L80`)
3. RLS: `auth.uid()`; separate grants. [V] (`skills/supabase-postgres-best-practices/references/security-rls-basics.md:L1-L50`)
DECISION RULES: query5, conn4, security3, schema6, lock4, data4, monitor3, advanced2; partitioning: 100M rows. [V] (`skills/supabase-postgres-best-practices/SKILL.md:L26-L45`; `skills/supabase-postgres-best-practices/references/schema-partitioning.md:L37-L47`)
ARTIFACT SHAPE: SQL examples; no requirements artifact. [I]
QUESTION PROTOCOL: None.
VALIDATION: Examples/diagnostics; no checker or SQL run. [V] (`skills/supabase-postgres-best-practices/references/monitor-explain-analyze.md:L1-L45`)
AGENT FEATURES REQUIRED: None.
STATE ON DISK: None.
VOCABULARY: CRITICAL–LOW impact labels; no requirement IDs. [V] (`skills/supabase-postgres-best-practices/SKILL.md:L26-L45`)
NON-OBVIOUS TECHNIQUES:
- `SECURITY DEFINER`: identity check, revoke execute. [V] (`skills/supabase-postgres-best-practices/references/security-rls-performance.md:L17-L49`)
- Catalog query flags unindexed foreign keys. [V] (`skills/supabase-postgres-best-practices/references/schema-foreign-key-indexes.md:L35-L55`)
- `ON CONFLICT` avoids check/insert races. [V] (`skills/supabase-postgres-best-practices/references/data-upsert.md:L1-L50`)
FAILURE MODE FOUGHT: Unsafe grants, tenant leakage, query problems. [V] (`skills/supabase-postgres-best-practices/references/security-rls-basics.md:L1-L50`)
BAGGAGE: Supabase auth; non-house impact scale. [V] (`skills/supabase-postgres-best-practices/references/security-rls-basics.md:L26-L42`)
RISKS: Explicit warning: `SECURITY DEFINER` bypasses RLS. [V] (`skills/supabase-postgres-best-practices/references/security-rls-performance.md:L17-L35`)
FIT: database — **ADAPT** SQL/RLS/grants; **EXTRACT** catalog checks; lacks requirement links and table-access artifact. [I]
CONFLICTS: Supabase identity calls need wrappers. [V] (`skills/supabase-postgres-best-practices/references/security-rls-basics.md:L26-L42`)
KEY QUOTES:
CONFIDENCE: High.
