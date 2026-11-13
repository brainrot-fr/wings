# Bambu-Developers/skills / bambu-nest-api-guide
SOURCE: commit `b91cd017d9304968f8642866685be62ef666738d` | MIT, root `LICENSE` | 218 skill-folder lines
FRONTMATTER: `name: bambu-nest-api-guide`; `description: Genera y publica, como Artifact, una guía de integración de API para el equipo de frontend a partir de un diff de git en el monorepo NestJS + Prisma de Bambu — endpoints nuevos/modificados/eliminados, breaking changes, y diffs de body/query/response/validadores. Usa este skill cuando el usuario pida "genera la guía de API para frontend", "documenta los cambios de API de este PR/rama", "necesito el changelog de endpoints", "qué rompe este cambio para el frontend", "publica el artifact de la API", "API integration guide", "breaking changes report for this branch". Solo aplica al monorepo NestJS de Bambu (controllers + DTOs con class-validator/@nestjs/swagger) — no es project-agnostic como bambu-readme-generator.`
FILES READ:
| Path | Lines | Role |
|---|---:|---|
| `bambu-nest-api-guide/SKILL.md` | 88 | Workflow |
| `bambu-nest-api-guide/README.md` | 81 | Scope |
| `bambu-nest-api-guide/references/api-relevant-files.md`; `bambu-nest-api-guide/references/breaking-change-taxonomy.md` | 24; 25 | Selection; classifications |
FILES UNREAD: None.
JOB: Compare refs in Bambu's NestJS + Prisma monorepo; publish an HTML guide and chat summary. [V] (`bambu-nest-api-guide/SKILL.md:L6-L75`)
PROCEDURE:
1. `Paso 0`: resolve range; ask if merge-base remains ambiguous. [V] (`bambu-nest-api-guide/SKILL.md:L22-L30`)
2. `Paso 1`: diff controllers/DTOs; `Paso 2`: classify changes; `Paso 3`: apply taxonomy. [V] (`bambu-nest-api-guide/SKILL.md:L32-L50`)
3. `Pasos 4–6`: build Artifact, publish, report endpoint counts and breaks. [V] (`bambu-nest-api-guide/SKILL.md:L52-L75`)
DECISION RULES: Breaking changes stop a previous client working; optional additions are nonbreaking. Taxonomy covers fields, types, enums, auth and status. [V] (`bambu-nest-api-guide/references/breaking-change-taxonomy.md:L1-L25`)
ARTIFACT SHAPE: Range, breaking summary, module index, endpoint cards, deleted endpoints; cards include auth, fields, JSON, client action. [V] (`bambu-nest-api-guide/SKILL.md:L54-L64`)
QUESTION PROTOCOL: `AskUserQuestion` for ambiguous refs; request a prior Artifact URL to update. [V] (`bambu-nest-api-guide/SKILL.md:L27-L30`, `bambu-nest-api-guide/SKILL.md:L68-L68`)
VALIDATION: No validator; model judges Git diffs. Reference includes DTO/controller scope and mapper changes affecting returned values. [V] (`bambu-nest-api-guide/references/api-relevant-files.md:L1-L24`)
AGENT FEATURES REQUIRED: Git shell, subagents, `Artifact`, `artifact-design`. [V] (`bambu-nest-api-guide/SKILL.md:L32-L68`)
STATE ON DISK: Scratchpad HTML; published Artifact. [V] (`bambu-nest-api-guide/SKILL.md:L68-L68`)
VOCABULARY: `NUEVO`, `ELIMINADO`, `MODIFICADO`; breaking/additive; no severity or stable IDs. [V] (`bambu-nest-api-guide/SKILL.md:L42-L50`)
NON-OBVIOUS TECHNIQUES:
- Nearest common ancestor across four named long-lived branches. [V] (`bambu-nest-api-guide/SKILL.md:L24-L30`)
- Mapper changes count when API responses change. [V] (`bambu-nest-api-guide/references/api-relevant-files.md:L15-L24`)
- Breaking summary appears before details and in chat. [V] (`bambu-nest-api-guide/SKILL.md:L57-L75`)
FAILURE MODE FOUGHT: Missed or guessed frontend contract changes. [I] (`bambu-nest-api-guide/SKILL.md:L32-L64`)
BAGGAGE: Bambu NestJS conventions, remote `git fetch`, nonportable Artifact. [V] (`bambu-nest-api-guide/SKILL.md:L10-L68`)
RISKS: Large diffs mandate agents without fallback. [V] (`bambu-nest-api-guide/SKILL.md:L38-L40`). Artifact publishing is external. [V] (`bambu-nest-api-guide/SKILL.md:L68-L68`)
FIT: backend — **ADAPT** diff review and taxonomy; no requirement IDs or side-effect contracts. [V] (`bambu-nest-api-guide/SKILL.md:L42-L50`); [I] gap.
CONFLICTS: Agent mandate and Artifact conflict with portability; Git fetch needs network. [V] (`bambu-nest-api-guide/SKILL.md:L24-L68`)
KEY QUOTES:
None.
CONFIDENCE: High.
