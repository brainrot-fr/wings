# addyosmani/agent-skills / documentation-and-adrs

SOURCE: `skills/documentation-and-adrs/SKILL.md` | commit `301b02b12bff98e4688e6984af6556802322bbde` | MIT | 319 lines read
FRONTMATTER: `name: documentation-and-adrs`; `description: Records decisions and documentation. Use when you need to document an architecture decision (ADR) or the reasoning behind a design choice, when changing public APIs, shipping features, or when you need to record context that future engineers and agents will need to understand the codebase.`
FILES READ:
| Path | Lines |
|---|---:|
| `skills/documentation-and-adrs/SKILL.md` | 298 |
| `LICENSE` | 21 |
FILES UNREAD: None directly linked.
JOB: Preserve decision rationale, public API contracts, project guidance and user-facing documentation. [V] (`skills/documentation-and-adrs/SKILL.md:L1-L42`)
PROCEDURE: Match existing ADR conventions; document context/decision/alternatives/consequences; update API, README and changelog; review prose against source facts. [V] (`skills/documentation-and-adrs/SKILL.md:L20-L118`, `L180-L248`)
DECISION RULES: Follow existing ADR directory, numbering and headings; supersede rather than delete old decisions. [V] (`skills/documentation-and-adrs/SKILL.md:L28-L82`)
ARTIFACT SHAPE: ADR, typed API docs, README, changelog, gotcha/rule docs and prose-review changes. [V] (`skills/documentation-and-adrs/SKILL.md:L40-L180`)
QUESTION PROTOCOL: Surface conflicts in conventions and unsupported claims rather than silently choosing or polishing them away. [V] (`skills/documentation-and-adrs/SKILL.md:L28-L42`, `L248-L274`)
VALIDATION: Verify API params/returns/errors, README quick-start/commands, current ADRs and that prose preserves facts/trade-offs. [V] (`skills/documentation-and-adrs/SKILL.md:L248-L298`)
AGENT FEATURES REQUIRED: None.
STATE ON DISK: ADR directory, README, changelog, API docs and project instruction files; no workflow ledger. [V] (`skills/documentation-and-adrs/SKILL.md:L40-L180`)
VOCABULARY: ADR; proposed/accepted/superseded/deprecated; context/decision/alternatives/consequences; gotcha. [V] (`skills/documentation-and-adrs/SKILL.md:L28-L118`)
NON-OBVIOUS TECHNIQUES: Mark source details that must survive copy edits, then compare revised prose against original and restore lost qualifiers. [V] (`skills/documentation-and-adrs/SKILL.md:L212-L248`)
FAILURE MODE FOUGHT: Re-deciding old choices, unversioned rationale, stale docs and polished but unsupported claims. [V] (`skills/documentation-and-adrs/SKILL.md:L20-L82`, `L212-L298`)
BAGGAGE: Example ADR and README content is illustrative; do not copy it as project fact.
RISKS: Changelog/API examples contain dates and sample identifiers; keep examples clearly illustrative. [V] (`skills/documentation-and-adrs/SKILL.md:L40-L180`)
FIT: SDLC — **EXTRACT** ADR lifecycle and fact-preserving documentation review; keep the project’s existing format authoritative. [I]
CONFLICTS: Prescriptive README sections can conflict with existing project documentation standards; adapt to established conventions. [I]
KEY QUOTES: None.
CONFIDENCE: High; complete skill and root license read.
