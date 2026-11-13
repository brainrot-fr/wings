# addyosmani/agent-skills / security-and-hardening
SOURCE: `skills/security-and-hardening/SKILL.md` | commit `301b02b12bff98e4688e6984af6556802322bbde` | MIT (`LICENSE`) | 816 lines (`wc -l`)
FRONTMATTER: `name: security-and-hardening`; `description: Hardens code against vulnerabilities. Use when auditing an input handler for vulnerabilities, when handling user input, authentication, data storage, or external integrations, or when checking a login flow is safe against the OWASP Top Ten. Use when building any feature that accepts untrusted data, manages user sessions or session cookies, or interacts with third-party services. Use when auditing dependencies for known vulnerabilities, triaging package-manager audit findings, or assessing supply-chain risk in a new package. Use when personal data or privacy compliance (GDPR, CCPA) is involved.`
FILES READ:
| Path | Lines | Role |
|---|---:|---|
| `skills/security-and-hardening/SKILL.md` | 216 | Workflow |
| `skills/security-and-hardening/references/hardening-patterns.md` | 331 | Patterns |
| `references/security-checklist.md` | 248 | Checklist |
| `LICENSE` | 21 | MIT |
FILES UNREAD: `skills/debugging-and-error-recovery/SKILL.md`, `skills/observability-and-instrumentation/SKILL.md` (named companion skills).
JOB: Harden web apps at input, auth, integration, dependency and personal-data boundaries; produces checklist/review findings. [V] (`skills/security-and-hardening/SKILL.md:L1-L19`, `L201-L215`)
PROCEDURE:
1. `Threat Model First`: map trust boundaries and assets; apply STRIDE per boundary; turn abuse cases into tests. [V] (`skills/security-and-hardening/SKILL.md:L21-L40`)
2. Apply `Always Do`, `Ask First`, and `Never Do` boundaries before choosing hardening patterns. [V] (`skills/security-and-hardening/SKILL.md:L42-L73`)
3. Use the linked patterns for boundary validation, access control, SSRF, destructive paths, dependencies, privacy and LLM output. [V] (`skills/security-and-hardening/SKILL.md:L75-L167`)
DECISION RULES: Approval required for auth, sensitive data, integrations, CORS, uploads, rate limits and elevated roles; never auto-force dependency fixes. Auth limit ~10/15m; shared store beyond one process. [V] (`skills/security-and-hardening/SKILL.md:L55-L73`, `L121-L140`; `references/hardening-patterns.md:L244-L276`)
ARTIFACT SHAPE: Abuse cases and implementation checklist; no stable finding schema.
QUESTION PROTOCOL: Human approval gates only. [V] (`skills/security-and-hardening/SKILL.md:L55-L63`)
VALIDATION: Human checklist and native package audit; no dedicated validator. Nothing was run. [V] (`skills/security-and-hardening/SKILL.md:L49-L53`, `L133-L140`; `references/security-checklist.md:L145-L190`)
AGENT FEATURES REQUIRED: None; DevTools suggested. [V] (`skills/security-and-hardening/SKILL.md:L201-L215`)
STATE ON DISK: None specified; covers `.env.example`, ignored secrets and lockfiles. [V] (`references/hardening-patterns.md:L278-L302`)
 VOCABULARY: STRIDE; OWASP/LLM Top 10; no severity or finding IDs.
NON-OBVIOUS TECHNIQUES:
- Ownership proof precedes destructive path actions; markers can self-attest. [V] (`references/hardening-patterns.md:L209-L215`)
- SSRF checks all DNS answers, forbids redirects; high-risk flows pin IP. [V] (`skills/security-and-hardening/SKILL.md:L109-L113`; `references/hardening-patterns.md:L126-L159`)
- Stop if workspace, lockfile and CI disagree on manager. [V] (`references/security-checklist.md:L145-L156`)
FAILURE MODE FOUGHT: Mistaking shape checks, prompts or advisory scans for security assurance. [V] (`skills/security-and-hardening/SKILL.md:L21-L40`, `L115-L140`, `L154-L166`)
BAGGAGE: Web/TypeScript examples; manager matrix is point-in-time. [V] (`references/hardening-patterns.md:L11-L24`; `references/security-checklist.md:L164-L190`)
RISKS: Native audits/signature checks may use network; defaults age. Nothing was run. [V] (`skills/security-and-hardening/SKILL.md:L133-L140`; `references/security-checklist.md:L164-L190`)
FIT: security — **ADAPT** STRIDE, approval tiers and privacy rules; add requirement-linked findings and tool fallbacks. [I] (`skills/security-and-hardening/SKILL.md:L21-L40`, `L55-L73`)
CONFLICTS: Release audits need a network/tool gate; security-sensitive changes do require approval. [V] (`skills/security-and-hardening/SKILL.md:L49-L63`)
KEY QUOTES: None.
CONFIDENCE: High; companion skills unread.
