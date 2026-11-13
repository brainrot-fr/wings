# secondsky/claude-skills / api-authentication

SOURCE: `plugins/api-authentication/skills/api-authentication/SKILL.md` | commit `88378361314f558fb719aec0af9fd898ab36f0b2` | MIT (`LICENSE`) | 335 lines read
FRONTMATTER: `name: api-authentication`; `description: Secure API authentication with JWT, OAuth 2.0, API keys. Use for authentication systems, third-party integrations, service-to-service communication, or encountering token management, security headers, auth flow errors.`
FILES READ:
| Path | Lines | Role |
|---|---:|---|
| `plugins/api-authentication/skills/api-authentication/SKILL.md` | 98 | Complete target |
| `plugins/api-authentication/skills/api-authentication/references/python-flask.md` | 216 | Three implementation examples |
| `LICENSE` | 21 | Root license |
FILES UNREAD: None referenced by the target.
JOB: Guide JWT, OAuth 2.0, API-key and session authentication, including security headers and token handling. [V] (`plugins/api-authentication/skills/api-authentication/SKILL.md:L7-L18`, `L65-L95`)
PROCEDURE:
1. Choose an auth mechanism by use case; generate short-lived access and longer-lived refresh tokens. [V] (`plugins/api-authentication/skills/api-authentication/SKILL.md:L11-L18`, `L22-L26`)
2. Validate bearer-header format and token; return 401 for malformed or invalid credentials. [V] (`plugins/api-authentication/skills/api-authentication/SKILL.md:L28-L62`)
3. Apply role checks, HTTPS, HttpOnly cookie guidance, rate limiting, secret rotation and security headers. [V] (`plugins/api-authentication/skills/api-authentication/SKILL.md:L65-L83`; `plugins/api-authentication/skills/api-authentication/references/python-flask.md:L31-L42`)
DECISION RULES: JWT for stateless/SPA, OAuth for third parties, API keys for service-to-service; rate-limit auth and never place tokens in URLs. [V] (`plugins/api-authentication/skills/api-authentication/SKILL.md:L11-L18`, `L65-L72`)
ARTIFACT SHAPE: Example JSON token response, middleware errors, role-gated routes, and response headers; no named output file. [V] (`plugins/api-authentication/skills/api-authentication/SKILL.md:L28-L83`; `plugins/api-authentication/skills/api-authentication/references/python-flask.md:L31-L42`, `L91-L109`)
QUESTION PROTOCOL: None.
VALIDATION: Examples perform basic input, JWT and role checks; no checker or test suite named. Nothing was run. [V] (`plugins/api-authentication/skills/api-authentication/references/python-flask.md:L44-L79`)
AGENT FEATURES REQUIRED: None specified; examples require framework libraries and an application database.
STATE ON DISK: No review state or report persistence specified.
VOCABULARY: access/refresh tokens, role claims, OAuth scopes, hashed API keys; no stable finding or requirement IDs. [V] (`plugins/api-authentication/skills/api-authentication/SKILL.md:L22-L26`, `L85-L95`; `plugins/api-authentication/skills/api-authentication/references/python-flask.md:L31-L42`, `L163-L204`)
NON-OBVIOUS TECHNIQUES:
- Reject malformed bearer headers before token verification. [V] (`plugins/api-authentication/skills/api-authentication/SKILL.md:L38-L56`)
- Hash API keys at rest and update a last-used timestamp. [V] (`plugins/api-authentication/skills/api-authentication/references/python-flask.md:L174-L204`)
- Separate JWT role enforcement into a reusable decorator. [V] (`plugins/api-authentication/skills/api-authentication/references/python-flask.md:L31-L42`)
FAILURE MODE FOUGHT: Plain-text passwords, weak secrets, missing expiration, HTTP transport and token leakage in URLs/logs. [V] (`plugins/api-authentication/skills/api-authentication/SKILL.md:L92-L98`, `L65-L72`)
BAGGAGE: Flask examples assume application models/database and required packages; the main JWT sample is Node.js.
RISKS: Flask samples include development-secret fallbacks and broad exception handling; OAuth metadata uses a remote identity provider. [V] (`plugins/api-authentication/skills/api-authentication/references/python-flask.md:L20-L21`, `L44-L45`, `L120-L137`)
FIT: backend — **ADAPT** auth-method guidance and validation patterns; add explicit tenant/resource authorization and a shared error contract. [I] (`plugins/api-authentication/skills/api-authentication/SKILL.md:L11-L83`)
CONFLICTS: The policy prefers HttpOnly cookies while the JWT example returns tokens in JSON; define transport per client and threat model. [V] (`plugins/api-authentication/skills/api-authentication/SKILL.md:L65-L72`; `plugins/api-authentication/skills/api-authentication/SKILL.md:L22-L26`)
KEY QUOTES: None.
CONFIDENCE: High for target and linked Flask examples; no code was executed.
