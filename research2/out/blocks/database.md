# Database

Seven cards are within the eight-card cap. Source commands and database operations were not run; findings below are from static reading.

## RANKED CANDIDATES
1. [Supabase Postgres best practices](../skills/supabase__agent-skills/supabase-postgres-best-practices.md) — strongest reviewed rule library for Postgres schema, indexes, RLS and privileges.
2. [Alireza database-schema-designer](../skills/alirezarezvani__claude-skills/database-schema-designer.md) — most direct requirements-to-entities/ERD workflow and tenant-aware RLS example.
3. [Alireza database-designer](../skills/alirezarezvani__claude-skills/database-designer.md) — broad workflow plus local schema, index and migration generators; scripts were inspected, not run.
4. [Ccheney postgres-drizzle](../skills/ccheney__robust-skills/postgres-drizzle.md) — useful version-aware Drizzle/Postgres guidance, migrations, transaction discipline and tenant-scoped RLS.
5. [Wshobson postgresql-table-design](../skills/wshobson__agents/postgresql-table-design.md) — concise practical schema and indexing conventions, with partitioning criteria.
6. [Jeffallan database-optimizer](../skills/Jeffallan__claude-skills/database-optimizer.md) — measurement-driven PostgreSQL/MySQL optimization process.
7. [Jeffallan postgres-pro](../skills/Jeffallan__claude-skills/postgres-pro.md) — specialized PostgreSQL maintenance, JSONB, extension and replication guidance.

## COMPARISON MATRIX
| Area | Evidence | Portability / gap |
|---|---|---|
| Requirements and entities | Alireza schema designer derives entities/relationships and cross-cutting fields from requirements, then emits ERD and DDL; Alireza database-designer analyzes provided DDL/JSON and query patterns. | Neither card establishes requirement-ID traceability; Supabase and Ccheney chiefly provide rule/reference workflows. |
| Naming and schema rules | Supabase covers lowercase identifiers, types, constraints and FK indexes; Alireza provides normalization and constraint analysis; Wshobson covers keys, constraints, types and partition design. | Largely Postgres; no single portable schema checklist spanning engines. |
| Migrations | Alireza database-designer models expand/data migration/transition/contract and emits SQL/rollback/checks; Ccheney distinguishes `generate`/`migrate` from direct `push`; Supabase offers rule-level migration guidance. | Review and target authorization remain necessary; Alireza rollback for dropped tables is a placeholder. |
| Indexing and thresholds | Supabase and Wshobson use a 100M-row partitioning trigger; Ccheney says partition tables over 100GB; Alireza's optimizer ranks selectivity and detects 0.8 index overlap; Jeffallan recommends workload/plan-driven tuning. | The 100M-row and 100GB triggers are different heuristics, not universal equivalents. Index choice requires actual query/workload evidence. |
| RLS and tenant isolation | Supabase enables/forces RLS, uses `auth.uid()` examples and separates grants; Alireza schema designer models `organization_id` policies and asks for non-superuser RLS tests; Ccheney sets tenant context transaction-locally. | Supabase auth helpers need a non-Supabase adapter; PostgreSQL RLS mechanics transfer. Tenant context must be correctly scoped per request/transaction. |
| Privileges and access model | Supabase covers least-privilege grants and `SECURITY DEFINER`; Alireza's example distinguishes owner/admin actions. | No authentication-versus-authorization matrix or complete per-table owner/per-role access artifact was found. Example roles/policies are not a full access matrix. |
| Performance and operations | Jeffallan uses baseline/plan/measure/revert; Ccheney covers plans, pooling and transaction safety; Jeffallan postgres-pro covers vacuum, replication and JSONB. | Tuning and live operations require an authorized test/production target and environment-specific review. |
| Validation | Alireza includes local Python analyzers/generators and sample outputs; Ccheney documents migration checks and generated-SQL review; Supabase rules contain examples/diagnostics. | No deterministic end-to-end checker across these cards; none was executed in this research. |

## CONFLICTS
- Partitioning thresholds vary by measure: 100M rows (Supabase/Wshobson) versus 100GB (Ccheney); treat as workload prompts, not hard universal defaults.
- Supabase `auth.uid()`/`auth.role()` are platform-specific; do not export them as generic PostgreSQL identity functions.
- Alireza database-designer and Jeffallan optimizer/pro describe running SQL, Python tools or shell commands; this task was static-only. Keep execution separately authorized. Ccheney explicitly treats `EXPLAIN ANALYZE` as execution, including writes.
- PostgreSQL/Drizzle version-specific features need version checks. Ccheney distinguishes Drizzle 0.x/1.0 APIs and PG versions; do not combine examples blindly.

## QUESTIONS ANSWERED
- **How are schemas derived?** Alireza schema-designer starts from requirements, derives entities/relationships, adds tenant/soft-delete/audit/version fields, and produces ERD/DDL. Alireza database-designer instead analyzes supplied DDL/JSON and query patterns. Neither reviewed card provides requirement-ID linkage.
- **Naming, migrations, indexes and thresholds?** Supabase specifies lowercase identifiers, constraints and FK indexes. Alireza supplies normalization and index analysis; migration phases follow expand, migrate, transition, contract. Partitioning examples give 100M rows (Supabase/Wshobson) or 100GB (Ccheney); these are differing heuristics. The optimizer's 0.8 index-overlap measure is a tool threshold, not a universal index rule.
- **How should row policies be written/tested/reviewed?** Supabase uses RLS with explicit identity/privilege checks and recommends enforcing policies at the database. Alireza's example scopes by organization and says test as a non-superuser. Ccheney demonstrates transaction-local tenant context with `set_config`. Review policy identity, grants, function ownership and session/transaction scoping together.
- **What is the privilege model?** Supabase separates grants from row predicates and restricts unsafe `SECURITY DEFINER` execution. Other cards show roles/actions but do not define a general service-role or grant matrix.
- **Portable Postgres vs Supabase-specific?** SQL constraints, indexes, transactions and native RLS are broadly PostgreSQL concepts. `auth.uid()`/`auth.role()` and Supabase platform references require adaptation.
- **Authentication/authorization or per-table access matrix?** None found. The Alireza owner/admin example and Supabase grant/policy rules are useful inputs, not a complete table-by-role artifact. [V] (See the card evidence in [database-schema-designer](../skills/alirezarezvani__claude-skills/database-schema-designer.md), [supabase-postgres-best-practices](../skills/supabase__agent-skills/supabase-postgres-best-practices.md), and [postgres-drizzle](../skills/ccheney__robust-skills/postgres-drizzle.md).)
- **Sickn lineage?** Three Sickn copies each contain 36 files; 18 match Supabase and 18 differ per copy. Treat as partial copies with modifications, not a clean rewrite; lineage is recorded in [lineage.md](../cross/lineage.md). No separate card was created.

## GAP EVIDENCE
- Across the reviewed cards, no requirements-to-schema traceability field/ID workflow and no complete authentication-versus-authorization or per-table owner/role matrix appears.
- Static review only: generated SQL, Python scripts, migration commands, `npx` examples and database queries were not run. Alireza's schema-designer card flags a credential-like literal and incomplete seed-example syntax; do not copy the example without review.

## TECHNIQUES WORTH TAKING
1. Derive entities and relationships from requirements, then explicitly add tenant, audit, soft-delete and version fields. (Alireza schema-designer)
2. Separate grants from RLS row predicates; test policies as a non-superuser and verify function ownership/`EXECUTE`. (Supabase, Alireza schema-designer)
3. Bind tenant identity transaction-locally; use the transaction handle for all statements in a transaction. (Ccheney)
4. Use expand/data-migrate/transition/contract for risky schema changes and review generated SQL before applying. (Alireza database-designer, Ccheney)
5. Choose indexes from real query patterns and measured plans; stage one change at a time and compare before/after. (Jeffallan database-optimizer)
6. Treat partition thresholds as evidence prompts; confirm workload, retention, maintenance and partition-key filtering before partitioning. (Supabase, Wshobson, Ccheney)

## DO NOT TAKE
Do not treat example roles or RLS snippets as a complete access matrix, copy Supabase auth functions into generic Postgres, assume sample thresholds are universal, or run database/shell commands without target authorization and review. Do not use the dropped-table rollback placeholder as a recovery plan.

## CATALOG
| Name | Path (lines) | Status |
|---|---|---|
| supabase-postgres-best-practices | `skills/supabase-postgres-best-practices/SKILL.md (78; 31 rules)` | carded; all rules read |
| postgresql-table-design | `plugins/database-design/skills/postgresql-table-design/SKILL.md (129) + details.md (161)` | carded |
| database-designer | `engineering/skills/database-designer/SKILL.md (321)` | carded; 6811 lines across 16 files |
| database-schema-designer | `engineering/skills/database-schema-designer/SKILL.md (248)` | carded; 552 lines across 3 files |
| database-schema-design | `—` | failed; no target skill path found |
| postgres-drizzle | `skills/postgres-drizzle/SKILL.md (41; 7 references)` | carded; 4489 lines including license |
| database-optimizer | `skills/database-optimizer/SKILL.md (152; 5 references)` | carded; 2121 lines including license |
| postgres-pro | `skills/postgres-pro/SKILL.md (157; 5 references)` | carded; 2095 lines including license |
| Sickn Supabase copies | Three 36-file copies | lineage read; 18 identical and 18 modified files per copy; no separate card |
