# Wshobson/agents / postgresql-table-design
SOURCE: `plugins/database-design/skills/postgresql-table-design/SKILL.md` | commit `9c61ab243def98f72da12abd41cfcf5bcd91af9d` | MIT (`LICENSE`; no per-skill notice) | 310 lines read, including root license; counts from `wc -l`
FRONTMATTER:
```yaml
---
name: postgresql-table-design
description: Use this skill when designing or reviewing a PostgreSQL-specific schema. Covers best-practices, data types, indexing, constraints, performance patterns, and advanced features
---
```
[V] `plugins/database-design/skills/postgresql-table-design/SKILL.md:L1-L4`
FILES READ:
| Path | Lines | Role |
|---|---:|---|
| `LICENSE` | 20 | root license |
| `plugins/database-design/skills/postgresql-table-design/SKILL.md` | 129 | entry |
| `plugins/database-design/skills/postgresql-table-design/references/details.md` | 161 | extended catalog and patterns |
FILES UNREAD: None; the folder contains only the entry and its directly linked reference.
JOB: Use when designing or reviewing PostgreSQL schemas, choosing types/keys/constraints/indexes, partitioning, semi-structured storage, or planning a live schema change [V] `plugins/database-design/skills/postgresql-table-design/SKILL.md:L8-L17`.
PROCEDURE:
1. Apply “Core Rules,” “PostgreSQL Gotchas,” “Constraints,” “Indexing,” and “Partitioning” [V] `plugins/database-design/skills/postgresql-table-design/SKILL.md:L19-L83`.
2. Consult `references/details.md` for detailed types, workload patterns, safe evolution, extensions, JSONB, and DDL [V] `plugins/database-design/skills/postgresql-table-design/SKILL.md:L122-L129`.
DECISION RULES: Partition above 100M rows only when queries filter on the key or maintenance follows it; index FK columns; use PG15+ `NULLS NOT DISTINCT` when duplicate NULLs are unwanted [V] `plugins/database-design/skills/postgresql-table-design/SKILL.md:L30-L31` `plugins/database-design/skills/postgresql-table-design/SKILL.md:L79-L83`.
ARTIFACT SHAPE: Example `CREATE TABLE` and index DDL for users, orders, and JSONB profiles; no output-file format [V] `plugins/database-design/skills/postgresql-table-design/SKILL.md:L85-L119`.
QUESTION PROTOCOL: n/a
VALIDATION: No scripts or formal rubric; advice is checked by model judgment and PostgreSQL DDL examples [I].
AGENT FEATURES REQUIRED: none stated [I].
STATE ON DISK: No workflow state or generated artifact is specified [I].
VOCABULARY: 3NF, PK/FK, `NOT NULL`, `TIMESTAMPTZ`, `JSONB`, GIN/GiST/BRIN, MVCC, RLS, `NULLS NOT DISTINCT`, RANGE/LIST/HASH [V] `plugins/database-design/skills/postgresql-table-design/SKILL.md:L21-L25` `plugins/database-design/skills/postgresql-table-design/SKILL.md:L59-L83` `plugins/database-design/skills/postgresql-table-design/references/details.md:L33-L35`.
NON-OBVIOUS TECHNIQUES:
- `jsonb_path_ops` trades key-existence operators for smaller, faster containment indexing [V] `plugins/database-design/skills/postgresql-table-design/references/details.md:L104-L120`.
- `CREATE INDEX CONCURRENTLY` avoids write blocking but cannot run inside a transaction [V] `plugins/database-design/skills/postgresql-table-design/references/details.md:L62-L68`.
- `fillfactor=90` leaves room for HOT updates; separating hot/cold columns can reduce bloat [V] `plugins/database-design/skills/postgresql-table-design/references/details.md:L39-L44`.
FAILURE MODE FOUGHT: Redundancy, unsuitable types, missing FK indexes, unbounded write cost, and unsafe or ill-suited partitioning [V] `plugins/database-design/skills/postgresql-table-design/SKILL.md:L21-L25` `plugins/database-design/skills/postgresql-table-design/SKILL.md:L77-L83` `plugins/database-design/skills/postgresql-table-design/references/details.md:L46-L68`.
BAGGAGE: PostgreSQL-specific versions and extensions require explicit compatibility choices; the guidance spans PG10 through PG18 [V] `plugins/database-design/skills/postgresql-table-design/SKILL.md:L30-L30` `plugins/database-design/skills/postgresql-table-design/SKILL.md:L81-L83` `plugins/database-design/skills/postgresql-table-design/references/details.md:L89-L102`.
RISKS: RLS examples show policy forms [V] `plugins/database-design/skills/postgresql-table-design/references/details.md:L33-L35`; no per-table owner/access matrix is defined in these files [I].
FIT: database — ADAPT the modeling, constraints, indexing, and migration heuristics; take the two skill files, labeling PostgreSQL/version-specific advice [I].
CONFLICTS: PG-only types/extensions need a clear scope in a universal suite; no direct conflict with the house principles [I].
KEY QUOTES: None.
CONFIDENCE: High; the complete skill, linked reference, and root license were read.
