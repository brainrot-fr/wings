# alirezarezvani/claude-skills / database-schema-designer
SOURCE: `engineering/skills/database-schema-designer/SKILL.md` | commit `08cd8a9fc86cc370e2c0d448e8171fbcfdbc5a30` | MIT, root `LICENSE`; no dedicated license notice in target folder | 552 lines (`wc -l` over files below)
FRONTMATTER:
```yaml
---
name: "database-schema-designer"
description: "Use when asked for an ERD, table relationships, normalization or a schema migration plan. Produces the ERD and normalized DDL with migration steps."
---
```
FILES READ:
| Path | Lines | Role |
|---|---:|---|
| `engineering/skills/database-schema-designer/SKILL.md` | 248 | target |
| `engineering/skills/database-schema-designer/references/full-schema-examples.md` | 283 | Prisma, Drizzle, Alembic examples |
| `LICENSE` | 21 | root license |
FILES UNREAD: None.
JOB:
- Derive entities, relations, cross-cutting fields, RLS, and ERD from requirements. Trigger: schema or migration-plan requests. [V] (`engineering/skills/database-schema-designer/SKILL.md:L1-L4`, `L40-L68`, `L74-L118`, `L186-L227`)
PROCEDURE:
1. **Requirements → Entities**.
2. **Identify Relationships**.
3. **Add Cross-cutting Concerns**: tenant key, soft deletion, audit columns, version. [V] (`engineering/skills/database-schema-designer/SKILL.md:L40-L68`)
DECISION RULES: Tenant-scoped `organization_id`; `deleted_at`, audit fields, `version`; index foreign keys and test RLS as non-superuser. [V] (`engineering/skills/database-schema-designer/SKILL.md:L62-L68`, `L229-L248`)
ARTIFACT SHAPE: ERD, normalized DDL, migrations, types, seed data, RLS, indexes; Prisma/Drizzle/Alembic examples, no output paths. [V] (`engineering/skills/database-schema-designer/SKILL.md:L18-L27`, `L71-L74`, `L120-L227`, `engineering/skills/database-schema-designer/references/full-schema-examples.md:L5-L17`, `L180-L220`, `L222-L283`)
QUESTION PROTOCOL: Requirements are input; no question sequence shown. [I] (`engineering/skills/database-schema-designer/SKILL.md:L40-L52`)
VALIDATION: RLS test guidance; examples, not a deterministic checker. Not run. [V] (`engineering/skills/database-schema-designer/SKILL.md:L229-L248`)
AGENT FEATURES REQUIRED: Shell for `npx` ERD examples. [V] (`engineering/skills/database-schema-designer/SKILL.md:L186-L227`)
STATE ON DISK: Examples name `schema.prisma`, `db/schema.ts`, Alembic revision, and `db/seed.ts`; no output path. [V] (`engineering/skills/database-schema-designer/SKILL.md:L120-L154`, `engineering/skills/database-schema-designer/references/full-schema-examples.md:L5-L17`, `L180-L190`, `L222-L228`)
VOCABULARY: `organization_id`, `deleted_at`, `version`; roles `owner`/`admin`; states `TODO`/`IN_PROGRESS`/`DONE`/`CANCELLED`. [V] (`engineering/skills/database-schema-designer/SKILL.md:L62-L68`, `L74-L118`, `engineering/skills/database-schema-designer/references/full-schema-examples.md:L165-L178`)
NON-OBVIOUS TECHNIQUES:
- Uses explicit junction entities `TaskLabel` and `TaskAssignment` to express many-to-many links. [V] (`engineering/skills/database-schema-designer/SKILL.md:L42-L60`)
- Scopes tenant records, soft deletes, audit metadata, and optimistic locking as cross-cutting fields. [V] (`engineering/skills/database-schema-designer/SKILL.md:L62-L68`)
- RLS example ties task visibility to organization membership and restricts deletion to creator or admin. [V] (`engineering/skills/database-schema-designer/SKILL.md:L74-L118`)
FAILURE MODE FOUGHT: Tenant leakage, stale deletes, bad indexes, mutable keys, lost updates. [V] (`engineering/skills/database-schema-designer/SKILL.md:L74-L118`, `L229-L248`)
BAGGAGE: PostgreSQL-specific examples, plus Prisma/Drizzle/Alembic and Faker/CUID. [V] (`engineering/skills/database-schema-designer/references/full-schema-examples.md:L5-L17`, `L180-L190`, `L222-L228`, `engineering/skills/database-schema-designer/SKILL.md:L120-L154`)
RISKS: Credential-like literal appears in `engineering/skills/database-schema-designer/SKILL.md`; seed example also has incomplete syntax. [V] (`engineering/skills/database-schema-designer/SKILL.md:L120-L154`)
FIT: database — ADAPT entity/cross-cutting steps; EXTRACT RLS pattern; keep framework code optional. Worked requirement has no IDs. [I] (`engineering/skills/database-schema-designer/SKILL.md:L40-L68`)
CONFLICTS: PostgreSQL RLS and `npx` examples need an optional, platform-neutral fallback in a universal suite. [I] (`engineering/skills/database-schema-designer/SKILL.md:L74-L118`, `L186-L227`)
KEY QUOTES:
- “always test RLS with a non-superuser role” [V] (`engineering/skills/database-schema-designer/SKILL.md:L229-L238`)
CONFIDENCE: High; target, linked example, and root license read; examples not run.
