# secondsky/claude-skills / rest-api-design

SOURCE: `plugins/rest-api-design/skills/rest-api-design/SKILL.md` | commit `88378361314f558fb719aec0af9fd898ab36f0b2` | MIT (`LICENSE`) | 123 lines read
FRONTMATTER: `name: rest-api-design`; `description: Designs RESTful APIs with proper resource naming, HTTP methods, status codes, and response formats. Use when building new APIs, establishing API conventions, or designing developer-friendly interfaces.`
FILES READ:
| Path | Lines | Role |
|---|---:|---|
| `plugins/rest-api-design/skills/rest-api-design/SKILL.md` | 102 | Complete target |
| `LICENSE` | 21 | Root license |
FILES UNREAD: None referenced; target folder contains only `SKILL.md`.
JOB: Design REST endpoints with resource naming, method, status and response conventions. Trigger: new API or conventions. No named output file. [V] (`plugins/rest-api-design/skills/rest-api-design/SKILL.md:L7-L10`, `L96-L102`)
PROCEDURE:
1. Name plural hierarchical resource nouns; avoid action URLs. [V] (`plugins/rest-api-design/skills/rest-api-design/SKILL.md:L11-L26`)
2. Select method semantics, including an idempotency column; choose from the listed status codes. [V] (`plugins/rest-api-design/skills/rest-api-design/SKILL.md:L28-L49`)
3. Use a `data`/`meta` response, paginate collections, and support filtering, sorting and field selection. [V] (`plugins/rest-api-design/skills/rest-api-design/SKILL.md:L51-L95`)
DECISION RULES: GET/PUT/PATCH/DELETE are labeled idempotent and POST non-idempotent; validation uses 400, missing auth 401, insufficient permission 403, missing resource 404 and throttling 429. [V] (`plugins/rest-api-design/skills/rest-api-design/SKILL.md:L30-L49`)
ARTIFACT SHAPE: JSON `data` and `meta.requestId`; collection pagination and `self`/`next` links. [V] (`plugins/rest-api-design/skills/rest-api-design/SKILL.md:L51-L85`)
QUESTION PROTOCOL: None specified.
VALIDATION: OpenAPI/Swagger documentation is recommended; no validator or test procedure named. Nothing was run. [V] (`plugins/rest-api-design/skills/rest-api-design/SKILL.md:L96-L102`)
AGENT FEATURES REQUIRED: None specified.
STATE ON DISK: No persistence or resumability format specified.
VOCABULARY: plural resources, HTTP methods/status codes, API path versioning, pagination; no requirement or finding IDs. [V] (`plugins/rest-api-design/skills/rest-api-design/SKILL.md:L11-L49`, `L96-L102`)
NON-OBVIOUS TECHNIQUES:
- Lists filtering, sorting and sparse field selection as query concerns. [V] (`plugins/rest-api-design/skills/rest-api-design/SKILL.md:L87-L94`)
- Collection responses include totals, page count and navigation links. [V] (`plugins/rest-api-design/skills/rest-api-design/SKILL.md:L69-L85`)
- Gives endpoint examples spanning parent/child resources and CRUD methods. [V] (`plugins/rest-api-design/skills/rest-api-design/SKILL.md:L13-L26`)
FAILURE MODE FOUGHT: Verb-based resource URLs and inconsistent HTTP conventions. [V] (`plugins/rest-api-design/skills/rest-api-design/SKILL.md:L11-L49`, `L98-L102`)
BAGGAGE: Compact examples omit authorization, tenant scope, error schema, rate-limit policy and compatibility rules.
RISKS: Marks PATCH idempotent without defining conditions; verify semantics for the specific operation. [V] (`plugins/rest-api-design/skills/rest-api-design/SKILL.md:L30-L36`)
FIT: backend — **ADAPT** resource/method/status guidance and pagination; add requirement links, authorization, error contracts and compatibility rules. [I] (`plugins/rest-api-design/skills/rest-api-design/SKILL.md:L11-L49`, `L51-L102`)
CONFLICTS: The PATCH idempotency label is unconditional and underspecified for implementations. [V] (`plugins/rest-api-design/skills/rest-api-design/SKILL.md:L30-L36`)
KEY QUOTES: None.
CONFIDENCE: High for the standalone target; no referenced files.
