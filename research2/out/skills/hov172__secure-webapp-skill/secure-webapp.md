# hov172/secure-webapp-skill / secure-webapp
SOURCE: `research/repos/hov172__secure-webapp-skill` | commit `09854eaa665d60ec376dee3844572c4d26408b8e` | MIT, root `LICENSE` (2026 hov172); `LICENSE.txt` lists OWASP licenses/trademark [LICENSE.txt:L3-L28] | 3,507 lines (`wc -l`; README slice `sed -n '470,630p' README.md | wc -l`).
FRONTMATTER: [V] `name: secure-webapp`; `description: Use for OWASP-grounded security guidance when building, editing, or reviewing web applications. Trigger proactively for auth, sessions, JWT/OAuth/OIDC, user input, DB queries, file uploads, API endpoints, cookies/CORS/CSP/security headers, secrets, redirects, external URL fetches, logging/errors, dependencies, threat modeling, hardening, audits, LLM/AI features such as prompt handling, agent tools, and MCP servers, or vulnerability classes such as XSS, SQLi, IDOR, CSRF, SSRF, open redirect, prototype pollution, deserialization, prompt injection, and supply chain risk.` [SKILL.md:L2-L3]
FILES READ:
| Path | Lines | Role |
|---|---:|---|
| `SKILL.md`; `README.md`; `AGENTS.md`; `GEMINI.md` | 83; 1131; 51; 47 | Modes/agent mapping; README lines read:L470-L630 (161 lines) [SKILL.md:L6-L24; README.md:L484-L591] |
| `assets/audit-checklist.md`; `assets/remediate-checklist.md`; `assets/report-template.md`; `assets/secure-webapp-small.svg`; `assets/secure-webapp-large.svg` | 90; 85; 275; 6; 10 | Checklist/templates/icons |
| `references/ai-and-llm.md`; `references/apis-and-files.md`; `references/auth-and-sessions.md`; `references/authorization.md`; `references/data-and-crypto.md`; `references/frontend-and-headers.md`; `references/input-handling.md`; `references/insecure-design.md`; `references/logging-and-errors.md`; `references/secrets-and-config.md`; `references/secure-coding.md`; `references/supply-chain.md`; `references/tokens-and-oauth.md` | 141; 238; 216; 199; 183; 309; 195; 177; 270; 145; 178; 220; 179 | All routed guides [SKILL.md:L28-L42] |
| `LICENSE`; `LICENSE.txt` | 21; 28 | License/attribution |
FILES UNREAD: `scripts/README.md` (maintain mode); `README.md:L1-L469,L631-L1131` (install/update/report/maintenance).
JOB: [V] `audit`; seven-area `quick-check`; authorized `harden`; pre-build `design-review` [SKILL.md:L8-L20; assets/audit-checklist.md:L3-L5; README.md:L484-L591].
PROCEDURE: [V] Audit: scope + 12 categories; quick-check: subset; harden: architecture-preserving edits/approval flags; design: trust-boundary STRIDE/control/test review [assets/audit-checklist.md:L7-L9; assets/audit-checklist.md:L18-L58; README.md:L503-L588; references/insecure-design.md:L27-L45].
DECISION RULES: [V] Critical/High/Medium/Low/Info: week/sprint/quarter/track/observe; quick-check omits full report [assets/audit-checklist.md:L11-L16; SKILL.md:L16]. [I] Map to P0-P3/IDs.
ARTIFACT SHAPE: [V] Audit: Summary/findings/Not Reviewed/Roadmap; design: spec-side note; harden: patch; quick-check: no full report [assets/audit-checklist.md:L64-L90; references/insecure-design.md:L43-L45; SKILL.md:L16-L19].
QUESTION PROTOCOL: [V] Audit scopes; design-review records open questions [assets/audit-checklist.md:L7-L9; README.md:L571-L588].
VALIDATION: [I] Model-judged review; [V] supply-chain calls `npm audit --omit=dev --audit-level=high` per lockfile dir [assets/audit-checklist.md:L48-L49].
AGENT FEATURES REQUIRED: [V] None mode-specific; file/edit/shell/search equivalents [AGENTS.md:L46-L51; GEMINI.md:L43-L47].
STATE ON DISK: [V] Design note by feature spec; audit report is Markdown [references/insecure-design.md:L43-L45; assets/audit-checklist.md:L64-L88].
VOCABULARY: [V] Five severities; finding fields include path:line, evidence, impact, fix [assets/audit-checklist.md:L11-L16; assets/audit-checklist.md:L69-L73].
NON-OBVIOUS TECHNIQUES:
- [V] Split auth/function/object checks; query-scope and return 404 for hidden objects [references/authorization.md:L18-L21; references/authorization.md:L38-L55].
- [V] Trace trust boundaries; STRIDE prompts; verify controls and abuse tests [references/insecure-design.md:L27-L45].
- [V] Authorize AI tools as user; validate schema, ownership, redact logs [references/ai-and-llm.md:L51-L80].
FAILURE MODE FOUGHT: [V] Missing ownership checks; insecure design [references/authorization.md:L18-L23; references/insecure-design.md:L8-L19].
BAGGAGE: [V] `remediate`/`report` excluded [SKILL.md:L18-L20].
RISKS: [V] `update` runs network `npx --yes github:hov172/secure-webapp-skill --global` [SKILL.md:L21].
FIT: [I] Security ADAPT: `SKILL.md`, `assets/audit-checklist.md`, `references/insecure-design.md`.
CONFLICTS: [I] Five tiers/no IDs versus house P0-P3/stable IDs/requirement links [assets/audit-checklist.md:L11-L16; assets/audit-checklist.md:L64-L90].
KEY QUOTES: “The agent is not a principal. The user is.” [references/ai-and-llm.md:L55]
CONFIDENCE: High; modes, refs, licenses opened.
