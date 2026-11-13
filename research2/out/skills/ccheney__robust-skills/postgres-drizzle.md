# ccheney/robust-skills / postgres-drizzle

SOURCE: `skills/postgres-drizzle/SKILL.md` | commit `0eea7b060d12e3520556a73b15fbfa79480987d1` | MIT (`LICENSE`) | 4489 lines read
FRONTMATTER: `name: postgres-drizzle`; `description: Write or review PostgreSQL schemas, queries, migrations, and Drizzle ORM code. Use for Postgres/Drizzle relations, indexing, pooling, or query performance; not for unrelated databases or generic backend work.`
FILES READ:
| Path | Lines | Role |
|---|---:|---|
| `skills/postgres-drizzle/SKILL.md` | 41 | Workflow |
| `skills/postgres-drizzle/references/SCHEMA.md` | 605 | Schema |
| `skills/postgres-drizzle/references/QUERIES.md` | 803 | Queries |
| `skills/postgres-drizzle/references/RELATIONS.md` | 742 | Relation APIs |
| `skills/postgres-drizzle/references/MIGRATIONS.md` | 589 | Migration lifecycle |
| `skills/postgres-drizzle/references/POSTGRES.md` | 660 | PG features/RLS |
| `skills/postgres-drizzle/references/PERFORMANCE.md` | 589 | Performance |
| `skills/postgres-drizzle/references/CHEATSHEET.md` | 439 | Quick reference |
| `LICENSE` | 21 | Root license |
FILES UNREAD: None local; external documentation URLs not opened.
JOB: Review or produce PostgreSQL/Drizzle schemas, queries, migrations and performance guidance. [V] (`skills/postgres-drizzle/SKILL.md:L7-L23`)
PROCEDURE:
1. Establish installed Drizzle/Kit versions, driver and PostgreSQL version before using version-specific APIs. [V] (`skills/postgres-drizzle/SKILL.md:L12-L18`)
2. Read the relevant topic reference; keep database FKs distinct from ORM relations. [V] (`skills/postgres-drizzle/SKILL.md:L27-L41`; `skills/postgres-drizzle/references/RELATIONS.md:L30-L38`)
3. Generate and review migrations; execute only against an explicitly authorized target. [V] (`skills/postgres-drizzle/SKILL.md:L20-L23`; `skills/postgres-drizzle/references/MIGRATIONS.md:L253-L277`)
DECISION RULES: Preserve applied migration history; prefer generate+migrate over production `push`; avoid mixing 0.x `relations()` with v1 `defineRelations()`. [V] (`skills/postgres-drizzle/references/MIGRATIONS.md:L253-L277`; `skills/postgres-drizzle/references/RELATIONS.md:L32-L40`)
ARTIFACT SHAPE: TypeScript schema/query, SQL migration or diagnosis; migrations include SQL and journal/snapshot metadata. [V] (`skills/postgres-drizzle/SKILL.md:L25`; `skills/postgres-drizzle/references/MIGRATIONS.md:L100-L123`)
QUESTION PROTOCOL: Request missing version/target when needed for safe version-specific code or execution. [V] (`skills/postgres-drizzle/SKILL.md:L13-L23`)
VALIDATION: `drizzle-kit check`, generated-SQL review and migration testing are described; none was run. [V] (`skills/postgres-drizzle/references/MIGRATIONS.md:L160-L166`, `L483-L498`)
AGENT FEATURES REQUIRED: None.
STATE ON DISK: Migrations, snapshots, journal; no review-resume ledger. [V] (`skills/postgres-drizzle/references/MIGRATIONS.md:L104-L123`)
VOCABULARY: FK vs ORM relation; RLS; UUIDv7; `SET LOCAL`; `generate`/`migrate`/`push`. [V] (`skills/postgres-drizzle/references/RELATIONS.md:L30-L38`; `skills/postgres-drizzle/references/POSTGRES.md:L235-L246`, `L309-L320`)
NON-OBVIOUS TECHNIQUES:
- Scope tenant context with transaction-local `set_config`; pooled-session `SET` can leak. [V] (`skills/postgres-drizzle/references/POSTGRES.md:L309-L320`)
- Use the transaction handle for every statement; outer `db` calls escape rollback. [V] (`skills/postgres-drizzle/references/QUERIES.md:L743-L757`)
- Treat `EXPLAIN ANALYZE` as execution, including writes. [V] (`skills/postgres-drizzle/SKILL.md:L22-L23`)
FAILURE MODE FOUGHT: Version-mismatched relation APIs, unreviewed migrations and queries executed against the wrong target. [V] (`skills/postgres-drizzle/SKILL.md:L12-L23`; `skills/postgres-drizzle/references/RELATIONS.md:L32-L40`)
BAGGAGE: PG17/18 and Drizzle 0.x/1.0 require version checks; references are extensive.
RISKS: Migrations/push/`EXPLAIN ANALYZE` can alter or execute against databases; `npx` may resolve packages. None run. [V] (`skills/postgres-drizzle/SKILL.md:L20-L23`; `skills/postgres-drizzle/references/MIGRATIONS.md:L128-L145`; `skills/postgres-drizzle/references/PERFORMANCE.md:L136-L145`)
FIT: database — **ADAPT** target/version gates, migration review and transaction-scoped RLS; add requirement-derived schema and per-role access records. [I] (`skills/postgres-drizzle/SKILL.md:L12-L23`; `skills/postgres-drizzle/references/POSTGRES.md:L235-L320`)
CONFLICTS: None; external docs are suggested when local sources do not establish support. [V] (`skills/postgres-drizzle/SKILL.md:L35-L41`)
KEY QUOTES: None.
CONFIDENCE: High; target and all seven local references read completely; no database/code command was run.
