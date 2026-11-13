# Backend

## RANKED CANDIDATES
1. [Addy API/interface design](../skills/addyosmani__agent-skills/api-and-interface-design.md) — strongest function-level contract and error semantics, including validation, pagination and idempotency.
2. [Alireza API design reviewer](../skills/alirezarezvani__claude-skills/api-design-reviewer.md) — three small Python CLIs make OpenAPI conventions, breaking changes and weighted quality checks reproducible.
3. [Jeffallan API designer](../skills/Jeffallan__claude-skills/api-designer.md) — OpenAPI 3.1, RFC 7807 errors, explicit pagination and version evolution.
4. [Wshobson API design principles](../skills/wshobson__agents/api-design-principles.md) — substantial REST/GraphQL conventions, typed errors and checklist coverage.
5. [Bambu Nest API guide](../skills/Bambu-Developers__skills/bambu-nest-api-guide.md) — practical endpoint/DTO diff and breaking-change taxonomy, but tied to Bambu's NestJS/Prisma conventions.
6. [Wshobson architecture patterns](../skills/wshobson__agents/architecture-patterns.md) — inward dependencies, ports/adapters and in-memory test seams.
7. [Jeffallan architecture designer](../skills/Jeffallan__claude-skills/architecture-designer.md) — requirements, NFRs, diagrams and review-gated ADRs.
8. [Wshobson auth implementation](../skills/wshobson__agents/auth-implementation-patterns.md) — explicitly separates authentication, authorization and resource ownership.
9. [SecondSky API authentication](../skills/secondsky__claude-skills/api-authentication.md) — compact JWT/OAuth/API-key examples, with development-secret and transport caveats.
10. [SecondSky REST API design](../skills/secondsky__claude-skills/rest-api-design.md) — concise resource, status and pagination conventions; weak on auth and error contracts.

## COMPARISON MATRIX
| Candidate | Contract shape | Errors / auth | Idempotency / pagination | Traceability and checkability |
|---|---|---|---|---|
| Addy | Typed `TaskAPI` with input and return types | Consistent `APIError`; 401 unauthenticated vs 403 unauthorized | Explicit duplicate handling; paginated list | No requirement IDs or validator; examples require judgment |
| Alireza | OpenAPI JSON or raw endpoint records; lint, compare, score | Linter issues; comparator break categories | Spec changes include breaking-change hints; no operation idempotency contract | Three deterministic Python CLIs; no requirement IDs |
| Jeffallan API | OpenAPI 3.1 operations, requests, responses and security | RFC 7807; 401 vs 403; internal errors not exposed | Page default 20/max 100; cursor/keyset options; version/deprecation policy | Redocly/Prism CLI checks; `npx` package surface |
| Wshobson API | REST endpoints and GraphQL types/payloads | REST structured errors; GraphQL typed error unions | Offset/cursor/Link pagination; `Idempotency-Key` guidance | Manual checklist; app template includes permissive host/CORS settings |
| Bambu | Diff-based endpoint cards with auth, fields, body and response | Reports auth/status changes; no stable error schema | Breaking taxonomy; no idempotency or rate-limit contract | No requirement IDs; Git diff and DTO inspection |
| Wshobson architecture | Clean/Hexagonal layers, ports, adapters and test seams | Domain/use cases isolated from infrastructure | Not an API pagination/idempotency contract | In-memory tests; optional `pydeps`; no rule validator |
| Jeffallan architecture | System design, NFRs, Mermaid and ADR | Security considerations included; no per-operation auth model | Scale/recovery NFR prompts; no API contract | Stakeholder review and diagrams; heuristics, not script gates |
| Wshobson auth | Session/JWT/OAuth, RBAC, permission and ownership examples | Explicit AuthN/AuthZ and 401/403 distinction | JWT 15m/7d; login 5/15m; API 100/min | Examples, no checker; external frameworks/Redis |
| SecondSky auth | JWT, OAuth, API keys and session examples | `{error}` responses and Flask role decorator | Token expiry examples; says rate-limit auth, no threshold | Static examples; remote OAuth provider |
| SecondSky REST | Resource/method/status guidance and `data`/`meta` shape | 401/403/404 examples; no unified error object | Collection pagination; PATCH labeled idempotent | OpenAPI docs recommended; no validator |

## CONFLICTS
- Addy's REST/TypeScript examples are not universal, and its versioning guidance is abstract. Bambu requires Git, remote fetch for some ranges, subagents on large diffs, and an external Artifact surface.
- REST guides disagree on idempotency details; SecondSky labels PATCH idempotent without conditions, while Addy specifies a persisted idempotency-key design. Adopt neither as a universal rule without operation semantics.
- SecondSky says to store tokens in HttpOnly cookies while its JWT example returns tokens as JSON. Decide transport from client and threat model.
- Wshobson's template app uses wildcard host/CORS settings; treat it as illustrative, not production-ready. Jeffallan's CLIs use `npx`, while Alireza's local scripts use Python's standard library.
- No carded source ties every operation to requirements, authorization, side effects and a stable requirement reference.

## QUESTIONS ANSWERED
- **Function contracts:** Addy's `TaskAPI` models CRUD inputs/returns; `APIError` has code/message/details. Jeffallan models OpenAPI operations; Bambu checks route/DTO/mapper diffs. Alireza lints, compares and scores specs. Stable requirement-ID mapping is not evidenced. (`api-and-interface-design.md`; `skills/api-and-interface-design/SKILL.md:L37-L86`; `api-designer.md`; `api-design-reviewer.md`; `bambu-nest-api-guide.md`)
- **Errors and validation:** Addy maps 400/401/403/404/409/422/500 and validates at the boundary. Jeffallan uses RFC 7807 and forbids leaking internal errors; Wshobson gives REST error fields and typed GraphQL unions. SecondSky examples use `{error}` but do not define a shared schema. Alireza validates OpenAPI conventions. (`skills/api-and-interface-design/SKILL.md:L61-L124`; `api-designer.md`; `api-design-principles.md`; `api-authentication.md`)
- **Versioning, pagination, rate limits, idempotency:** Addy models persisted idempotency intent and payload hash; Jeffallan compares cursor/keyset options and compatibility; Wshobson includes offset/cursor/Link and `Idempotency-Key`; SecondSky lists pagination but no thresholds. Wshobson auth supplies sample rate limits; other targets do not define common thresholds. (`skills/api-and-interface-design/SKILL.md:L125-L253`; `api-designer.md`; `api-design-principles.md`; `auth-implementation-patterns.md`; `rest-api-design.md`)
- **Authentication vs authorization / multi-tenancy:** Wshobson distinguishes AuthN from AuthZ and includes ownership checks. Jeffallan separates 401/403; SecondSky shows role claims/decorators. Only Wshobson names multi-tenancy as a trigger; no card defines a per-operation tenant-isolation matrix. (`auth-implementation-patterns.md`; `api-designer.md`; `api-authentication.md`)
- **Architecture boundaries:** Wshobson's Clean/Hexagonal rules direct domain/use-case imports inward and use in-memory adapters; `pydeps` can graph dependencies but does not prove policy compliance. Jeffallan supplies NFR/ADR templates and stakeholder review. Alireza's deterministic scripts check API specs, not DDD boundaries. Bambu uses controller/DTO/mapper inspection. (`architecture-patterns.md`; `architecture-designer.md`; `api-design-reviewer.md`; `bambu-nest-api-guide.md`)

## GAP EVIDENCE
- Search: `rg -n '(?i:requirement[- ]id)|\b(?:REQ|FR|SC)-[0-9]+\b|(?i:source-ref)'` across all 10 carded backend target folders: 0 matches. This establishes only that their reviewed files do not show requirement-ID links.
- Search terms for rate limits, tenant scope and idempotency are descriptive leads, not completeness proof; claims above are limited to opened source sections.

## TECHNIQUES WORTH TAKING
1. Define input/output types before implementation. (`skills/api-and-interface-design/SKILL.md:L37-L60`)
2. Standardize machine-readable error codes and distinguish 401 from 403. (`L61-L86`)
3. Validate external data once at the system boundary. (`L88-L124`)
4. Model idempotency as persisted intent plus payload hash, not merely accepting a header. (`L156-L217`)
5. Treat mapper changes as API changes when returned values change. (`bambu-nest-api-guide/references/api-relevant-files.md:L15-L24`)
6. Classify deleted, additive and breaking contract changes explicitly. (`bambu-nest-api-guide/references/breaking-change-taxonomy.md:L1-L25`)
7. Enforce API conventions per endpoint and compare old/new OpenAPI specs with structured change findings. (`engineering/skills/api-design-reviewer/scripts/api_linter.py:L66-L82`; `engineering/skills/api-design-reviewer/scripts/breaking_change_detector.py:L865-L873`)
8. Use inward dependency rules and in-memory ports/adapters to make application boundaries testable. (`plugins/backend-development/skills/architecture-patterns/SKILL.md:L24-L68`, `L74-L125`)

## DO NOT TAKE
Do not rely on examples alone as a requirement-traceable contract, and do not require a proprietary Artifact or agent runtime for the portable core.


## CATALOG

| Name | Path (lines) | One-line status | Score |
|---|---|---|---:|
| clean-ddd-hexagonal | `skills/clean-ddd-hexagonal/SKILL.md (48)` | not deep-read; no card | 0 |
| oma-architecture | `.agents/skills/oma-architecture/SKILL.md (193)` | not deep-read; no card | 0 |
| oma-backend | `.agents/skills/oma-backend/SKILL.md (201)` | not deep-read; no card | 0 |
