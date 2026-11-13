# Wshobson/agents / api-design-principles
SOURCE: `plugins/backend-development/skills/api-design-principles/SKILL.md` | commit `9c61ab243def98f72da12abd41cfcf5bcd91af9d` | MIT (`LICENSE`; no per-skill notice) | 1,880 lines read, including root license; counts from `wc -l`
FRONTMATTER:
```yaml
---
name: api-design-principles
description: Master REST and GraphQL API design principles to build intuitive, scalable, and maintainable APIs that delight developers. Use when designing new APIs, reviewing API specifications, or establishing API design standards.
---
```
[V] `plugins/backend-development/skills/api-design-principles/SKILL.md:L1-L4`
FILES READ:
| Path | Lines | Role |
|---|---:|---|
| `LICENSE` | 20 | root license |
| `plugins/backend-development/skills/api-design-principles/SKILL.md` | 110 | entry |
| `plugins/backend-development/skills/api-design-principles/references/details.md` | 413 | patterns |
| `plugins/backend-development/skills/api-design-principles/references/rest-best-practices.md` | 408 | REST |
| `plugins/backend-development/skills/api-design-principles/references/graphql-schema-design.md` | 589 | GraphQL |
| `plugins/backend-development/skills/api-design-principles/assets/api-design-checklist.md` | 155 | checklist |
| `plugins/backend-development/skills/api-design-principles/assets/rest-api-template.py` | 185 | app template |
FILES UNREAD: None; all skill files and referenced resources were opened.
JOB: Use for REST/GraphQL design, API review, or standards [V] `plugins/backend-development/skills/api-design-principles/SKILL.md:L10-L19`; covers REST, GraphQL, and versioning [V] `plugins/backend-development/skills/api-design-principles/SKILL.md:L22-L73`.
PROCEDURE:
1. Shape REST resources and choose pagination, versioning, errors, and rate limits [V] `plugins/backend-development/skills/api-design-principles/references/rest-best-practices.md:L3-L251`.
2. Define GraphQL types, payloads, DataLoaders, and query protections [V] `plugins/backend-development/skills/api-design-principles/references/graphql-schema-design.md:L3-L589`.
3. Use “Pre-Implementation Review” and “GraphQL-Specific Checks” [V] `plugins/backend-development/skills/api-design-principles/assets/api-design-checklist.md:L3-L155`.
DECISION RULES: Page size defaults to 20, max 100; HTTP distinguishes 401/403; POST retries may use `Idempotency-Key` [V] `plugins/backend-development/skills/api-design-principles/references/details.md:L26-L85` `plugins/backend-development/skills/api-design-principles/references/rest-best-practices.md:L235-L246` `plugins/backend-development/skills/api-design-principles/references/rest-best-practices.md:L328-L338`.
ARTIFACT SHAPE: REST error fields: `error`, `message`, `details`, `timestamp`, `path`; GraphQL uses typed mutation payloads and `errors` [V] `plugins/backend-development/skills/api-design-principles/references/details.md:L87-L146` `plugins/backend-development/skills/api-design-principles/references/graphql-schema-design.md:L193-L217`.
QUESTION PROTOCOL: n/a
VALIDATION: Manual checklist; app template imports FastAPI/Pydantic and starts Uvicorn on `0.0.0.0:8000` if launched; this exposes a network listener. No check command is specified [V/I] `plugins/backend-development/skills/api-design-principles/assets/api-design-checklist.md:L3-L155` `plugins/backend-development/skills/api-design-principles/assets/rest-api-template.py:L1-L15` `plugins/backend-development/skills/api-design-principles/assets/rest-api-template.py:L176-L185`. Not run.
AGENT FEATURES REQUIRED: none stated [I].
STATE ON DISK: No workflow-state format [I]; examples include API responses and a standalone template [V] `plugins/backend-development/skills/api-design-principles/references/details.md:L87-L146` `plugins/backend-development/skills/api-design-principles/assets/rest-api-template.py:L1-L15`.
VOCABULARY: REST, GraphQL, Relay, `@deprecated`, status codes, `Idempotency-Key`; error shapes differ by paradigm [V] `plugins/backend-development/skills/api-design-principles/references/graphql-schema-design.md:L131-L190` `plugins/backend-development/skills/api-design-principles/references/graphql-schema-design.md:L193-L217` `plugins/backend-development/skills/api-design-principles/references/graphql-schema-design.md:L543-L589`.
NON-OBVIOUS TECHNIQUES:
- REST lists pair `page`, `page_size`, `total`, `pages`; GraphQL fetches one extra result for `hasNextPage` [V] `plugins/backend-development/skills/api-design-principles/references/details.md:L26-L85` `plugins/backend-development/skills/api-design-principles/references/details.md:L277-L369`.
- Typed payloads carry field errors; unions model validation, not-found, and authorization [V] `plugins/backend-development/skills/api-design-principles/references/graphql-schema-design.md:L193-L217` `plugins/backend-development/skills/api-design-principles/references/graphql-schema-design.md:L416-L487`.
- The REST guide illustrates cursor and Link-header pagination alongside offset pagination [V] `plugins/backend-development/skills/api-design-principles/references/rest-best-practices.md:L107-L147`.
FAILURE MODE FOUGHT: Inconsistent errors, accidental breaking changes, unbounded collections, N+1 fetching, and misuse of HTTP semantics [V] `plugins/backend-development/skills/api-design-principles/SKILL.md:L80-L109`.
BAGGAGE: Mock FastAPI/Pydantic app has wildcard host/CORS settings [V] `plugins/backend-development/skills/api-design-principles/assets/rest-api-template.py:L18-L34`.
RISKS: Do not lift `allowed_hosts=["*"]` or `allow_origins=["*"]` from the template into production [V] `plugins/backend-development/skills/api-design-principles/assets/rest-api-template.py:L18-L34`.
FIT: backend — ADAPT its REST/GraphQL conventions and typed error examples; use the checklist as judgment support, not as requirement-to-test traceability [I].
CONFLICTS: No requirement-ID mapping [I].
KEY QUOTES: “Resources are nouns (users, orders, products), not verbs” `plugins/backend-development/skills/api-design-principles/SKILL.md:L26-L26`
CONFIDENCE: High; the skill, all local references/assets, and root license were read completely.
