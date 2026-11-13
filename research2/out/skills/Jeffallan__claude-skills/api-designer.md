# Jeffallan/claude-skills / api-designer
SOURCE: `skills/api-designer/SKILL.md` | commit `078a25cc5bfd8011459be7b91d004e900c1d02d3` | MIT; root notice `LICENSE`; per-skill frontmatter says MIT | 2,828 total lines read (`wc -l`)
FRONTMATTER: `name: api-designer`; `description: Use when designing REST or GraphQL APIs, creating OpenAPI specifications, or planning API architecture. Invoke for resource modeling, versioning strategies, pagination patterns, error handling standards.`
FILES READ:
| Path | Lines | Role |
|---|---:|---|
| `skills/api-designer/SKILL.md` | 222 | Workflow |
| `skills/api-designer/references/error-handling.md` | 541 | Errors |
| `skills/api-designer/references/openapi.md` | 824 | OpenAPI |
| `skills/api-designer/references/pagination.md` | 494 | Pagination |
| `skills/api-designer/references/rest-patterns.md` | 335 | REST |
| `skills/api-designer/references/versioning.md` | 391 | Versions |
| `LICENSE` | 21 | Root notice |
FILES UNREAD: None. This skill declares MIT in frontmatter; no separate per-skill LICENSE was present.
JOB: Design API resources, endpoints and schemas; deliver `openapi.yaml`, auth flows, errors, pagination and version policy. [V] (`skills/api-designer/SKILL.md:L21-L28`, `L204-L216`)
PROCEDURE:
1. **Analyze domain**, then **Model resources** and sketch the entity diagram. [V] (`skills/api-designer/SKILL.md:L21-L25`)
2. **Design endpoints**; **Specify contract** as OpenAPI 3.1 and lint `openapi.yaml`. [V] (`skills/api-designer/SKILL.md:L25-L27`)
3. **Mock and verify** with Prism; **Plan evolution** for versions, deprecation, compatibility. [V] (`skills/api-designer/SKILL.md:L27-L28`)
DECISION RULES: Use plural resource nouns and HTTP semantics; paginate (default 20, max 100); major versions and announce breaking changes. [V] (`skills/api-designer/references/rest-patterns.md:L7-L32`, `L36-L45`; `skills/api-designer/references/pagination.md:L251-L275`; `skills/api-designer/references/versioning.md:L136-L160`)
ARTIFACT SHAPE: OpenAPI `info`, `servers`, `paths`, `components`; operations have parameters, requestBody, responses, security. [V] (`skills/api-designer/references/openapi.md:L12-L79`, `L139-L183`, `L313-L426`)
QUESTION PROTOCOL: Analyze business requirements, data models, client needs. [V] (`skills/api-designer/SKILL.md:L21-L25`)
VALIDATION: `npx @redocly/cli lint openapi.yaml`; `npx @stoplight/prism-cli mock openapi.yaml`; input is the spec [V]. Lint is deterministic, design judgment-based, and `npx` may resolve packages over network [I]. Commands not run. (`skills/api-designer/SKILL.md:L25-L28`)
AGENT FEATURES REQUIRED: shell for CLI commands [V]; no agent integrations specified [I] (`skills/api-designer/SKILL.md:L21-L28`).
STATE ON DISK: `openapi.yaml`; versioned specs may be `openapi-v1.yaml`, etc. [V] (`skills/api-designer/SKILL.md:L26-L27`; `skills/api-designer/references/versioning.md:L342-L352`)
VOCABULARY: RFC 7807 `type`, `title`, `status`, `detail`, `instance`; `Idempotency-Key`; `Deprecation`, `Sunset`; v1/v2. [V] (`skills/api-designer/references/error-handling.md:L21-L43`; `skills/api-designer/references/rest-patterns.md:L227-L251`; `skills/api-designer/references/versioning.md:L208-L220`)
NON-OBVIOUS TECHNIQUES:
- Compare offset, cursor, keyset and time-seek by dataset and consistency. [V] (`skills/api-designer/references/pagination.md:L13-L249`)
- Cursor contents include sort fields; apply filters before pagination. [V] (`skills/api-designer/references/pagination.md:L319-L353`)
- Error guidance separates 401 authentication from 403 authorization and forbids exposing stack traces or database errors. [V] (`skills/api-designer/references/error-handling.md:L117-L165`, `L259-L263`)
FAILURE MODE FOUGHT: Inconsistent specs, unbounded lists, unclear errors, breaking changes. [V] (`skills/api-designer/SKILL.md:L42-L62`)
BAGGAGE: CLI checks require external packages and shell access. [I]
RISKS: Error examples include request data; guidance forbids internal paths/configuration disclosure. [V] (`skills/api-designer/references/error-handling.md:L259-L263`)
FIT: backend — ADAPT REST/OpenAPI/errors/pagination/versioning; keep CLI checks optional. Take `rest-patterns.md`, `versioning.md`, `pagination.md`, `error-handling.md`, `openapi.md`. [I]
CONFLICTS: Suggested CLI validation requires optional external packages. [I]
KEY QUOTES: None.
CONFIDENCE: High; skill, all five references, and root license were read completely; commands were not run.
