# Jeffallan/claude-skills / architecture-designer
SOURCE: `skills/architecture-designer/SKILL.md` | commit `078a25cc5bfd8011459be7b91d004e900c1d02d3` | MIT; root notice `LICENSE`; per-skill frontmatter says MIT | 683 total lines read (`wc -l`)
FRONTMATTER: `name: architecture-designer`; `description: Use when designing new high-level system architecture, reviewing existing designs, or making architectural decisions. Invoke to create architecture diagrams, write Architecture Decision Records (ADRs), evaluate technology trade-offs, design component interactions, and plan for scalability. Use for system design, architecture review, microservices structuring, ADR authoring, scalability planning, and infrastructure pattern selection — distinct from code-level design patterns or database-only design tasks.`
FILES READ:
| Path | Lines | Role |
|---|---:|---|
| `skills/architecture-designer/SKILL.md` | 121 | Workflow |
| `skills/architecture-designer/references/adr-template.md` | 116 | ADR |
| `skills/architecture-designer/references/architecture-patterns.md` | 111 | Patterns |
| `skills/architecture-designer/references/database-selection.md` | 102 | Databases |
| `skills/architecture-designer/references/nfr-checklist.md` | 112 | NFRs |
| `skills/architecture-designer/references/system-design.md` | 100 | System design |
| `LICENSE` | 21 | Root notice |
FILES UNREAD: No referenced files unread. No per-skill LICENSE file exists; the skill frontmatter declares MIT.
JOB: Gather requirements; design components and trade-offs; output Mermaid, ADRs, technology recommendations, and risks/mitigations. [V] (`skills/architecture-designer/SKILL.md:L34-L40`, `L71-L78`)
PROCEDURE:
1. **Understand requirements**; verify coverage. [V] (`skills/architecture-designer/SKILL.md:L34-L36`)
2. **Identify patterns**, then **Design** with explicit trade-offs and a diagram. [V] (`skills/architecture-designer/SKILL.md:L37-L38`)
3. **Document** key decisions as ADRs; **Review** with stakeholders [GATE], returning to Design with feedback if review fails. [V] (`skills/architecture-designer/SKILL.md:L39-L40`)
DECISION RULES: Pattern table anchors team sizes (Monolith 1–10, Microservices 20+, Serverless Any); avoid hypothetical-scale over-engineering. [V] (`skills/architecture-designer/references/architecture-patterns.md:L3-L12`; `skills/architecture-designer/SKILL.md:L56-L69`)
ARTIFACT SHAPE: Requirements; Mermaid; system design: Requirements, High-Level Architecture, Component Details, Key Decisions, Scaling Strategy, Security Considerations, Failure Modes; ADR: Status, Context, Decision, Consequences, Alternatives, References. [V] (`skills/architecture-designer/SKILL.md:L71-L90`; `skills/architecture-designer/references/system-design.md:L3-L91`; `skills/architecture-designer/references/adr-template.md:L3-L37`)
QUESTION PROTOCOL: NFR checklist asks about concurrency, RPS, latency, availability, auth, recovery targets, and budget. [V] (`skills/architecture-designer/references/nfr-checklist.md:L3-L70`)
VALIDATION: Requirements coverage and stakeholder review [V]; stakeholder review is judgment-based [I]. (`skills/architecture-designer/SKILL.md:L34-L40`)
AGENT FEATURES REQUIRED: none declared [I] (`skills/architecture-designer/SKILL.md:L34-L78`).
STATE ON DISK: Architecture doc; ADR examples use `docs/adr/0001-...md`. [V] (`skills/architecture-designer/references/adr-template.md:L97-L106`)
VOCABULARY: ADR status: Proposed, Accepted, Deprecated, Superseded; patterns: Monolith, Modular Monolith, Microservices, Serverless, Event-Driven, CQRS. [V] (`skills/architecture-designer/references/adr-template.md:L3-L9`; `skills/architecture-designer/references/architecture-patterns.md:L3-L12`)
NON-OBVIOUS TECHNIQUES:
- NFR targets include 99.9% availability and p95 latency. [V] (`skills/architecture-designer/references/nfr-checklist.md:L15-L32`)
- System template assigns component duties and current/future scaling. [V] (`skills/architecture-designer/references/system-design.md:L40-L75`)
- ADR records neutral alongside positive and negative consequences. [V] (`skills/architecture-designer/references/adr-template.md:L18-L29`)
FAILURE MODE FOUGHT: Missed requirements, unjustified choices, failed review without iteration. [V] (`skills/architecture-designer/SKILL.md:L34-L40`, `L56-L69`)
BAGGAGE: Technology examples and trade-offs require adaptation. [I]
RISKS: Scale thresholds are heuristics, not universal gates. [I] (`skills/architecture-designer/references/architecture-patterns.md:L3-L12`)
FIT: backend — EXTRACT patterns/system design; database — EXTRACT selection questions; SDLC — ADAPT ADR structure. [I]
CONFLICTS: No material clash found; this guide uses no mandatory hooks, downloads, or subagents. [I]
KEY QUOTES: None.
CONFIDENCE: High; complete reads, no validation tooling run.
