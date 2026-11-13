# Wshobson/agents / auth-implementation-patterns
SOURCE: `plugins/developer-essentials/skills/auth-implementation-patterns/SKILL.md` | commit `9c61ab243def98f72da12abd41cfcf5bcd91af9d` | MIT (`LICENSE`; no per-skill notice) | 671 lines read, including root license; counts from `wc -l`
FRONTMATTER:
```yaml
---
name: auth-implementation-patterns
description: Master authentication and authorization patterns including JWT, OAuth2, session management, and RBAC to build secure, scalable access control systems. Use when implementing auth systems, securing APIs, or debugging security issues.
---
```
[V] `plugins/developer-essentials/skills/auth-implementation-patterns/SKILL.md:L1-L4`
FILES READ:
| Path | Lines | Role |
|---|---:|---|
| `LICENSE` | 20 | root license |
| `plugins/developer-essentials/skills/auth-implementation-patterns/SKILL.md` | 83 | entry |
| `plugins/developer-essentials/skills/auth-implementation-patterns/references/details.md` | 568 | examples |
FILES UNREAD: None; all skill files and referenced resources were opened.
JOB:
- Use for auth implementation, API protection, OAuth2/social login, RBAC, sessions, SSO, multi-tenancy, migration, or debugging [V] `plugins/developer-essentials/skills/auth-implementation-patterns/SKILL.md:L10-L19`.
- Distinguishes identity verification (AuthN) from permission/ownership enforcement (AuthZ) [V] `plugins/developer-essentials/skills/auth-implementation-patterns/SKILL.md:L23-L45`.
PROCEDURE:
1. Select among Session-Based, Token-Based (JWT), or OAuth2/OpenID Connect [V] `plugins/developer-essentials/skills/auth-implementation-patterns/SKILL.md:L38-L56`.
2. Consult `references/details.md` for JWT/refresh, Express Session, OAuth2, RBAC, permission, ownership, password, and rate-limit patterns [V] `plugins/developer-essentials/skills/auth-implementation-patterns/references/details.md:L3-L568`.
3. Apply numbered Best Practices and check Common Pitfalls; no human gate is specified [I].
DECISION RULES: Access JWT: 15m; refresh JWT: 7d. Login: 5 attempts/15m; API: 100/min [V] `plugins/developer-essentials/skills/auth-implementation-patterns/references/details.md:L24-L31` `plugins/developer-essentials/skills/auth-implementation-patterns/references/details.md:L548-L558`. 401 means unauthenticated; 403 means insufficient permission [V] `plugins/developer-essentials/skills/auth-implementation-patterns/references/details.md:L326-L340` `plugins/developer-essentials/skills/auth-implementation-patterns/references/details.md:L389-L402`.
ARTIFACT SHAPE: No report/file; examples return `accessToken`, `refreshToken`, `user`, `success`, or `error` [V] `plugins/developer-essentials/skills/auth-implementation-patterns/references/details.md:L14-L75` `plugins/developer-essentials/skills/auth-implementation-patterns/references/details.md:L471-L537`.
QUESTION PROTOCOL: n/a
VALIDATION: No validator or rubric; worked examples are implementation guidance, not executed checks [I].
AGENT FEATURES REQUIRED: none stated [I].
STATE ON DISK: No workflow-state format [I]; examples persist refresh-token records in a database and sessions in Redis [V] `plugins/developer-essentials/skills/auth-implementation-patterns/references/details.md:L78-L122` `plugins/developer-essentials/skills/auth-implementation-patterns/references/details.md:L172-L242`.
VOCABULARY: AuthN/AuthZ, RBAC, permissions, ownership, JWT, sessions; responses distinguish `401`/`403` [V] `plugins/developer-essentials/skills/auth-implementation-patterns/SKILL.md:L23-L45` `plugins/developer-essentials/skills/auth-implementation-patterns/references/details.md:L326-L340`.
NON-OBVIOUS TECHNIQUES:
- Hash stored refresh tokens and check database expiry before minting another access token [V] `plugins/developer-essentials/skills/auth-implementation-patterns/references/details.md:L78-L137`.
- Separate role hierarchy, permission lists, and resource-owner checks, with an admin bypass in the ownership example [V] `plugins/developer-essentials/skills/auth-implementation-patterns/references/details.md:L314-L469`.
- Store OAuth callback access tokens in an HttpOnly cookie rather than the URL [V] `plugins/developer-essentials/skills/auth-implementation-patterns/references/details.md:L286-L309`.
FAILURE MODE FOUGHT: Plaintext passwords, missing expiry/rate limits, trusting client-only checks, and JWTs in localStorage [V] `plugins/developer-essentials/skills/auth-implementation-patterns/SKILL.md:L62-L83`.
BAGGAGE: Examples assume Express, Passport, Redis, bcrypt, and database APIs [V] `plugins/developer-essentials/skills/auth-implementation-patterns/references/details.md:L7-L19` `plugins/developer-essentials/skills/auth-implementation-patterns/references/details.md:L174-L182` `plugins/developer-essentials/skills/auth-implementation-patterns/references/details.md:L246-L250` `plugins/developer-essentials/skills/auth-implementation-patterns/references/details.md:L473-L479`.
RISKS: None identified [I].
FIT: security/backend — EXTRACT the AuthN/AuthZ distinction, ownership checks, and bounded token/rate-limit examples; adapt them to requirement-linked contracts and the house severity vocabulary [I].
CONFLICTS: No requirement-ID mapping [I].
KEY QUOTES: “Who are you?” `plugins/developer-essentials/skills/auth-implementation-patterns/SKILL.md:L25-L25`
CONFIDENCE: High; the complete entry and referenced details file were read, along with the root license.
