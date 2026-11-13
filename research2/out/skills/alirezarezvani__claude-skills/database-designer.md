# alirezarezvani/claude-skills / database-designer
SOURCE: `engineering/skills/database-designer/SKILL.md` | commit `08cd8a9fc86cc370e2c0d448e8171fbcfdbc5a30` | MIT root `LICENSE`; README collection terms | 6811 lines (`wc -l` over files below)
FRONTMATTER:
```yaml
---
name: "database-designer"
description: "Design a database schema: tables, relationships, indexes, normalization, SQL vs NoSQL, migration plans. Use whenever the user asks how to structure their data, which database to pick, or before writing DDL."
---
```
FILES READ:
| Path | Lines | Role |
|---|---:|---|
| `engineering/skills/database-designer/SKILL.md` | 321 | target |
| `engineering/skills/database-designer/README.md` | 387 | guide |
| `engineering/skills/database-designer/schema_analyzer.py` | 981 | analyzer |
| `engineering/skills/database-designer/index_optimizer.py` | 925 | optimizer |
| `engineering/skills/database-designer/migration_generator.py` | 1198 | generator |
| `engineering/skills/database-designer/references/database-design-reference.md` | 476 | principles |
| `engineering/skills/database-designer/references/database_selection_decision_tree.md` | 372 | selection |
| `engineering/skills/database-designer/references/index_strategy_patterns.md` | 423 | indexes |
| `engineering/skills/database-designer/references/normalization_guide.md` | 353 | normalization |
| `engineering/skills/database-designer/assets/sample_schema.sql` | 206 | DDL |
| `engineering/skills/database-designer/assets/sample_schema.json` | 371 | schema |
| `engineering/skills/database-designer/assets/sample_query_patterns.json` | 374 | queries |
| `engineering/skills/database-designer/expected_outputs/schema_analysis_sample.txt` | 221 | report |
| `engineering/skills/database-designer/expected_outputs/index_optimization_sample.txt` | 59 | index |
| `engineering/skills/database-designer/expected_outputs/migration_sample.txt` | 123 | migration |
| `LICENSE` | 21 | root |
FILES UNREAD: None.
JOB:
- Select a store; analyze DDL/JSON, indexes, and migration changes. Trigger: schema or database-choice requests. [V] (`engineering/skills/database-designer/SKILL.md:L1-L4`, `L36-L68`)
PROCEDURE:
1. **Analyze the schema**; fix findings.
2. **Optimize indexes against real query patterns**.
3. **Generate the migration**; **Verification loop**. [V] (`engineering/skills/database-designer/SKILL.md:L36-L68`)
DECISION RULES: PostgreSQL default; NoSQL only for fitting access patterns. Migration phases: Expand, Migrate data, Transition, Contract. [V] (`engineering/skills/database-designer/SKILL.md:L178-L199`, `L254-L280`)
ARTIFACT SHAPE: JSON/text report, Mermaid ERD, index SQL, migration SQL, optional validations. [V] (`engineering/skills/database-designer/SKILL.md:L40-L64`)
QUESTION PROTOCOL: No interview script; schema and query files are inputs. [I] (`engineering/skills/database-designer/SKILL.md:L36-L55`)
VALIDATION: `schema_analyzer.py`: DDL/JSON → findings/ERD; `index_optimizer.py`: schema/query JSON → index advice; `migration_generator.py`: two JSON schemas → SQL/rollback/checks. Python stdlib, local I/O; no network or external commands observed; not run. [V] (`engineering/skills/database-designer/schema_analyzer.py:L908-L972`, `engineering/skills/database-designer/index_optimizer.py:L866-L918`, `engineering/skills/database-designer/migration_generator.py:L1117-L1198`)
AGENT FEATURES REQUIRED: Shell for Python CLIs. [V] (`engineering/skills/database-designer/SKILL.md:L36-L59`)
STATE ON DISK: `analysis.json`, `indexes.json`, `migration.sql`; query JSON is supplied. [V] (`engineering/skills/database-designer/SKILL.md:L43-L60`)
VOCABULARY: Findings HIGH/MEDIUM/LOW/WARNING; priorities 1–4; migration risks LOW/MEDIUM/HIGH. [V] (`engineering/skills/database-designer/schema_analyzer.py:L383-L464`, `engineering/skills/database-designer/index_optimizer.py:L46-L60`, `engineering/skills/database-designer/migration_generator.py:L64-L69`)
NON-OBVIOUS TECHNIQUES:
- BCNF is a warning for keys over two columns. [V] (`engineering/skills/database-designer/schema_analyzer.py:L456-L464`)
- Composite index order uses estimated selectivity; overlap threshold is 0.8. [V] (`engineering/skills/database-designer/index_optimizer.py:L160-L174`, `L615-L651`)
- Expand-contract copies to a temporary column, drops old, renames new. [V] (`engineering/skills/database-designer/migration_generator.py:L644-L700`)
FAILURE MODE FOUGHT: Missing constraints/indexes, anomalies, unsafe changes. [V] (`engineering/skills/database-designer/references/database-design-reference.md:L3-L39`, `L298-L328`)
BAGGAGE: PostgreSQL examples; priority/risk labels differ from P0–P3. [V] (`engineering/skills/database-designer/SKILL.md:L204-L280`)
RISKS: Dropped-table rollback is a placeholder. [V] (`engineering/skills/database-designer/migration_generator.py:L930-L947`)
FIT: database — ADAPT design; EXTRACT normalization/index refs; REFERENCE migrations. [I]
CONFLICTS: “run these” requires shell; no fallback is documented. [V] (`engineering/skills/database-designer/SKILL.md:L36-L68`)
KEY QUOTES: “Use SQL as default.” [V] (`engineering/skills/database-designer/SKILL.md:L270-L280`)
CONFIDENCE: High; files read; tools not run.
