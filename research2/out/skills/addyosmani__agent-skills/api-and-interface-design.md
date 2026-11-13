# Addy Osmani/agent-skills / api-and-interface-design
SOURCE: commit `301b02b12bff98e4688e6984af6556802322bbde` | MIT, root `LICENSE` | 369 target lines; 252 linked lines
FRONTMATTER: `name: api-and-interface-design`; `description: Guides stable API and interface design. Use when designing APIs, module boundaries, or any public interface. Use when creating REST or GraphQL endpoints, defining type contracts between modules, or establishing boundaries between frontend and backend.`
FILES READ:
| Path | Lines | Role |
|---|---:|---|
| `skills/api-and-interface-design/SKILL.md` | 369 | Target |
| `skills/deprecation-and-migration/SKILL.md` | 252 | Linked guidance |
FILES UNREAD: None referenced.
JOB: Design REST/GraphQL, module and component interfaces; outputs are typed examples and a checklist. [V] (`skills/api-and-interface-design/SKILL.md:L8-L18`, `L354-L369`)
PROCEDURE:
1. `Contract First`: define inputs/outputs; standardize errors and validate external boundaries. [V] (`skills/api-and-interface-design/SKILL.md:L37-L124`)
2. Prefer additive fields, predictable names, REST resources and pagination. [V] (`skills/api-and-interface-design/SKILL.md:L125-L155`, `L219-L253`)
3. Idempotency: stable intent key, atomic claim, payload hash, duplicate policy, retention beyond retry horizon. [V] (`skills/api-and-interface-design/SKILL.md:L156-L217`)
DECISION RULES: Errors map 400/401/403/404/409/422/500; in-flight duplicates use 409, bounded wait, or 202. No rate-limit threshold. [V] (`skills/api-and-interface-design/SKILL.md:L61-L86`, `L188-L193`)
ARTIFACT SHAPE: TypeScript interfaces, `APIError`, REST examples, checklist. [V] (`skills/api-and-interface-design/SKILL.md:L37-L86`, `L354-L369`)
QUESTION PROTOCOL: None.
VALIDATION: Checklist and human judgment; no scripts or schema checker.
AGENT FEATURES REQUIRED: None.
STATE ON DISK: None specified.
VOCABULARY: `TaskAPI`, `CreateTaskInput`, `APIError`; 401/403 separate authentication from authorization. No requirement IDs. [V] (`skills/api-and-interface-design/SKILL.md:L37-L86`)
NON-OBVIOUS TECHNIQUES:
- Treat observable quirks as future contracts. [V] (`skills/api-and-interface-design/SKILL.md:L22-L31`)
- Persist intent before uncertain external effects. [V] (`skills/api-and-interface-design/SKILL.md:L206-L217`)
- Use unique constraints and payload hashes for retries. [V] (`skills/api-and-interface-design/SKILL.md:L174-L205`)
FAILURE MODE FOUGHT: Inconsistent contracts/errors and duplicate effects. [I] (`skills/api-and-interface-design/SKILL.md:L61-L86`, `L156-L217`)
BAGGAGE: REST/TypeScript-biased examples; one-version principle lacks migration detail. [I] (`skills/api-and-interface-design/SKILL.md:L33-L35`, `L219-L324`)
RISKS: Linked guide shows `npx migrate-check`, but target skill does not invoke it. [V] (`skills/deprecation-and-migration/SKILL.md:L91-L104`)
FIT: backend — **ADAPT** contract, error, boundary, pagination and idempotency patterns; lacks requirement links, operation authorization, tenant model, and rate limits. [V] (`skills/api-and-interface-design/SKILL.md:L37-L124`, `L156-L217`, `L234-L253`)
CONFLICTS: Versioning is abstract; assumptions/decisions are not separated. [I] (`skills/api-and-interface-design/SKILL.md:L88-L124`, `L325-L339`)
KEY QUOTES:
- “The contract is the spec — implementation follows.” — `skills/api-and-interface-design/SKILL.md:L37-L40`
CONFIDENCE: High.
