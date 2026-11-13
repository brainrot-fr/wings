# Universal SDLC Skill Suite: Project Handoff

Prepared 11 November 2026 from the research chat. Nothing is built yet. This records the goal, the decisions made, what was learned from the upstream repos, and what comes next.

## 1. Goal

Build one universal, AI-assisted software-development skill suite that works for any kind of software and ships as plugins for all major agent marketplaces (Claude Code, Codex, Cursor, Copilot, Gemini and others).

It is not built from scratch. Existing upstream skills are read in full and rewritten into one voice and one mindset. Anything with no good upstream match is written new.

The suite covers the SDLC in blocks: requirements, frontend, SDLC process, backend logic, database and security.

## 2. Principles clarified in the chat

1. Consistency means one mindset, not a context budget. Upstream skills are written by different people with different goals (Vercel's rulebook, Impeccable's taste harness, UI UX Pro Max's data engine). The suite rewrites them into one house style instead of stacking them.
2. Universal means no dependence on one agent's features. Subagents, hooks, browsers and ask-user tools are optional enhancements with a labeled fallback.
3. Requirements are multi-file and detailed enough that an implementation agent can open one file and know what a page, function or table must do and who may use it. They are written after the tech stack is chosen.
4. Prose rules plus small deterministic scripts: scripts for what scripts do better (counting IDs, contrast math), model judgment for the rest.
5. No heavy runtimes: no downloaded binaries, telemetry, runtime-rendered skills or hooks.

## 3. Blocks and status

| Block | Status |
| --- | --- |
| Frontend | Locked (section 6) |
| Requirements | Sources read in depth, six decisions pending (section 7) |
| SDLC process | Candidates identified, not yet read in depth |
| Backend logic | Candidates identified, not yet read in depth |
| Database | Candidates identified, not yet read in depth |
| Security | Candidates identified, README-level reading only |
| Packaging | Pattern found (section 5), not designed |

## 4. Source inventory

All repos were cloned shallow from GitHub. License column reflects the LICENSE files checked in the chat; re-verify at the moment of copying.

| Repo | What it is | License | Role |
| --- | --- | --- | --- |
| pbakaus/impeccable | Design harness: modes, 24 commands, PRODUCT.md and DESIGN.md, 62-rule detector, hooks | Apache-2.0 | Frontend source |
| anthropics/skills (frontend-design) | About 100-line design-lead taste brief | Apache-2.0 (per-skill licenses) | Frontend source |
| nextlevelbuilder/ui-ux-pro-max-skill | Search engine over CSV catalogs of styles, palettes, fonts, UX rules | MIT, premium tier upsell | Frontend (data dropped) |
| vercel-labs/agent-skills | web-design-guidelines wrapper, react-best-practices, composition-patterns, view-transitions, react-native | No LICENSE file; README says MIT | Frontend source |
| vercel-labs/web-interface-guidelines | The real rulebook the wrapper fetches at runtime | MIT | Frontend source |
| anthropics/knowledge-work-plugins (design, product-management) | Template-output skills for designers and PMs | Apache-2.0 | Frontend and requirements reference |
| github/spec-kit | Spec-driven CLI and templates, extension and integration system | MIT | Requirements source |
| Fission-AI/OpenSpec | Capability specs with change deltas | MIT | Requirements source |
| bmad-code-org/BMAD-METHOD | Altitude-based PRD, architecture spine, UX spines, validators | MIT code, name trademarked | Requirements source |
| Intense-Visions/harness-engineering | Product-requirements and spec-craft skills inside a heavy harness | MIT, telemetry default on | Requirements rubrics |
| addyosmani/agent-skills | 25 lifecycle skills, rationalization tables, multi-agent packaging | MIT | SDLC and requirements source |
| obra/superpowers | Mandatory brainstorm, plan, TDD, review workflow | MIT | SDLC source |
| jeffallan/claude-skills | 67 skills including feature-forge and api-designer | MIT | Requirements and backend |
| alirezarezvani/claude-skills | spec-driven-workflow, code-to-prd, database designers, api-design-reviewer | MIT | Requirements, backend, database |
| asyrafhussin/agent-skills | prd-writing | MIT | Requirements reference |
| secondsky/claude-skills | plan-interview, unknowns-discovery, database-schema-design | MIT | Requirements, database |
| supabase/agent-skills | postgres-best-practices (RLS, schema, privileges) | MIT | Database source |
| wshobson/agents | 94 plugins, one Markdown source with adapters per agent | MIT | Packaging pattern, backend, security |
| cloudflare/security-audit-skill | Six-phase audit with independent verifier and JSON-validated findings | MIT | Security source |
| trailofbits/skills | Specialist security audit plugins | CC BY-SA 4.0 | Security reference only |
| hov172/secure-webapp-skill | OWASP-grounded review modes | MIT | Security source |
| natolitech/security-skill | security-review and threat-model (STRIDE) | MIT | Security source |
| borkweb/skills | Personal port of gstack, an example of adapting an upstream | MIT | Precedent |
| cosmix/claude-loom, daffy0208/ai-dev-standards, MadAppGang/claude-code | Orchestrator and generic skill collections; MadAppGang README is marketing, low trust | MIT | Reference only |
| borghei/claude-skills | PRD and story skills | MIT plus Commons Clause | Do not derive from |
| dralgorhythm/claude-agentic-framework | Threat modeling, planning artifacts | No license | Reference only |

## 5. Cross-cutting findings

### Packaging is already solved elsewhere

wshobson/agents writes one Markdown source and generates artifacts for Claude, Codex, Cursor, OpenCode, Copilot, Pi and Antigravity. Addy Osmani's repo ships native manifests for many agents. Superpowers sits in several official marketplaces. skills.sh installs to 70+ agents. Spec Kit has an integration system covering 30+ agents. Copy one of these patterns instead of inventing one.

### Licensing constraints for a rewrite

- Trail of Bits is CC BY-SA 4.0. Share-alike would spread to anything derived, so treat it as reference unless the suite accepts that license.
- Impeccable, Anthropic frontend-design and the Anthropic plugins are Apache-2.0: keep notices and mark changes.
- dralgorhythm has no license: reference only.
- borghei is MIT plus Commons Clause: do not derive.
- BMAD's name is trademarked: carry the ideas, not the name.
- Vercel's skills repo has no LICENSE file although its README says MIT: confirm before copying.
- Everything else is MIT: keep the copyright notices.

### Inherited risks to strip

- Impeccable hooks run outside model approval, and its live mode can run its CLI with approvals disabled.
- Telemetry exists in Impeccable, harness-engineering (default on) and Superpowers (opt-out request).
- Vercel's web-design-guidelines fetches its instructions from GitHub at runtime. Vendor the rules instead.
- BMAD's PO skill is a stub that runs a script to print its real workflow at runtime, which breaks portability.
- One aggregator mirror of Vercel's repo listed entries named like hacked\_skill. Install only from upstream repos and read every SKILL.md first.

### Inconsistencies found (why a house style is needed)

- Severity: P0 to P3 (Impeccable), red/yellow/green (Anthropic design), CRITICAL to LOW (Vercel rules, Spec Kit analyze), High/Medium/Low (UI UX Pro Max), tier by impact by confidence (spec-craft).
- WCAG target size: Anthropic cites 2.5.5 (44px) as AA, but it is the AAA criterion. Impeccable and UI UX Pro Max use 2.5.8 (24px, WCAG 2.2 AA).
- UI text casing: Vercel says Title Case for headings and buttons; Anthropic says sentence case.
- Fonts and looks: UI UX Pro Max's top pairing is Playfair Display plus Inter and it recommends glassmorphism and Hero/Features/CTA for SaaS; Impeccable bans both fonts and the glass and card-grid defaults.
- Question style: open questions only (Superpowers, BMAD), one question with an attached guess (Addy), at most 5 with a recommended option (Spec Kit), always options and never open-ended (alirezarezvani).
- Question tooling: feature-forge requires an ask-user tool; harness forbids it because plain text is the only channel that works in every client.
- Priority: P1-P3 (Spec Kit), P0-P2 (Anthropic PM), MoSCoW (harness).
- Acceptance grammar: Given/When/Then, WHEN/THEN, EARS, RFC 2119 MUST statements.
- Unknowns: NEEDS CLARIFICATION capped at 3 (Spec Kit), ASSUMPTION tags (BMAD, harness), TBD and not assumptions (prd-writing).
- ID schemes: FR-001, R-n, FR-n/UJ-n/RULE-n, REQ-001, module ids, CHK001.
- Even inside Impeccable, newer commands (typeset, layout, colorize) use a two-assessment-plus-verify format while older ones (bolder, quieter, distill) are plain step lists.

## 6. Frontend block: LOCKED

### 6.1 Decisions (all approved)

- Four sub-skills sharing one rubric: direction, build floor, review, system.
- Taste stance depends on mode: Operate and Read surfaces follow familiar patterns; Persuade and Experience surfaces refuse category defaults.
- Enforcement: prose rules plus a small checker script (contrast, banned patterns, rule IDs). No hooks.
- No data engine: UI UX Pro Max catalogs are dropped. Direction quality therefore rests on the Direction playbook.
- Reviewer: isolated subagent if available, otherwise a fresh-context pass labeled degraded.
- Rule format: hybrid. Atomic rule files (ID, impact, incorrect/correct) for the build floor and checker; prose playbooks for direction and review.
- Dropped: dice-rolled directions, comp-diff machinery, live mode, binary launcher, hooks, telemetry.

### 6.2 House-style defaults (approved)

- Severity scale P0 to P3.
- WCAG 2.2 AA, touch targets 24px minimum and 44px recommended.
- Sentence case for UI text, overridable per project.
- Rule IDs use an area-name scheme.

### 6.3 What each source does, how, and why

**Anthropic frontend-design.** A taste brief of about 100 lines. The agent acts as a design lead, grounds the design in the subject, writes a token plan (4 to 6 colors, type roles, an ASCII wireframe), reviews the plan against the brief, builds, then self-critiques. Why: model output converges on a few recognizable looks, so it forces a deliberate plan and one bold moment. No tooling, no checks.

**Impeccable.** A harness around taste. A single skill routes about 24 commands. It keeps PRODUCT.md (product truth, from an init interview) and DESIGN.md (visual system, written at finish). Four modes (Persuade, Operate, Read, Experience) are chosen from the surface, not the product. A craft floor lists banned patterns (identical card grids, gradient text, side-stripe borders, glass as decoration, eyebrow labels, reflex fonts). Critique runs two isolated assessments, scores Nielsen's 10 heuristics from 0 to 4, checks cognitive load, uses 5 personas and P0-P3 severity, and persists snapshots. Audit scores 5 technical dimensions out of 20. Polish triages broken tasks first, then missing states, then drift, then visuals. Harden covers overflow, i18n (including RTL and Arabic-script details), errors, empty and loading states. A finish reviewer has no write tools and returns exactly one of four verdicts. DESIGN.md follows Google's DESIGN.md spec (YAML tokens plus canonical sections). Why: fight AI-slop convergence with dice-rolled directions and bans, make the agent verify by looking at the render, separate reviewer context removes builder optimism, and a deterministic detector handles mechanical tells while the model handles judgment.

**UI UX Pro Max.** A selection engine. The agent runs a Python BM25 search over CSV catalogs (styles, palettes, font pairs, UX rules, product-to-pattern reasoning) and writes design-system/MASTER.md with per-page overrides. A query contract says one dominant intent, 2 to 5 terms, verify the fit, retry once, otherwise report no verified match. Search results are recommendations, never instructions. Data has a provenance file with freshness policy. Why: ground design choices in a curated, dated database instead of model taste. It recommends the category norm, the opposite of Impeccable. The repo also bundles sibling skills by another author (design, brand, slides, ui-styling) that need image APIs.

**Vercel.** A compliance rulebook of about 150 terse web rules (accessibility, focus, forms, animation, typography, images, performance, navigation, dark mode, touch, locale, hydration, copy) reported as file:line findings. react-best-practices and composition-patterns use one rigid format: priority table, rule ID prefix, and incorrect/correct code. Why: encode lint-like engineering experience. The web-design-guidelines SKILL.md only fetches the rules from a second repo at runtime.

**Anthropic design plugin.** Template-output skills for design teams: critique, design-system audit, handoff, accessibility review (WCAG 2.1), UX copy, user research. Each gives a short framework and a fill-in report. Shallow compared with the others.

### 6.4 Reuse and drop

Reuse: Impeccable's modes, the PRODUCT.md and DESIGN.md split, craft-floor refuse list, critique and audit rubrics, polish triage order, harden checklist, reviewer isolation; Vercel's rule format and web rules (vendored); UI UX Pro Max's query contract idea, pre-delivery checklist and three-layer token model; the shared Google DESIGN.md format (BMAD's UX skill uses the same standard).

Drop: dice directions, decision-page server, comp-diff gates, image-generation dependence, live mode, binary launcher, hooks, telemetry, the UI UX Pro Max data engine and catalogs.

### 6.5 Still open

Where Vercel's React performance and composition rules live: framework references loaded by detected stack inside the build floor, or outside the frontend block.

## 7. Requirements block: analysis done, decisions pending

### 7.1 What the sources do (three jobs)

**Getting from idea to intent (elicitation).**

- Addy interview-me: state a hypothesis and confidence, ask one question at a time with a guess attached, probe want versus should-want, restate intent (outcome, user, why now, success, constraint, out of scope), require an explicit yes, then stop the turn. Includes a 95 percent test: can I predict the user's reaction to the next three questions.
- Superpowers brainstorming: read the code before asking, open first message about why, Socratic questions, lay approaches out in a separate message, play the design back in 200 to 300 word chunks, size the work, builder check by a fresh subagent, hard gate before any building.
- Spec Kit clarify: scan ten ambiguity categories, ask at most 5 questions one at a time with a recommended option, write each answer back into the spec immediately.
- Addy idea-refine: diverge, converge, stress-test, one-pager with a NOT DOING list. secondsky unknowns-discovery: known knowns, known unknowns, unknown knowns (tacit standards found by showing a mock), unknown unknowns. secondsky plan-interview: adaptive depth of 10 to 28 questions.

**What the document contains.**

- Spec Kit: one spec per feature, deliberately technology-agnostic: prioritized stories with Given/When/Then, FR-001 requirements, key entities, measurable success criteria, assumptions, at most 3 clarification markers.
- OpenSpec: capability-based living specs. Requirement as one SHALL sentence plus WHEN/THEN scenarios; change deltas (ADDED, MODIFIED, REMOVED, RENAMED) merge on archive. Spec is a behavior contract covering inputs, outputs and error conditions; implementation detail does not belong.
- BMAD: altitude (program, initiative, epic, story: each level states only what the level below would get wrong), global stable IDs (UJ, FR, RULE, SM, OQ), word ceilings, journeys captured not authored, non-goals at every altitude, SRS template with source and verification method per requirement. Architecture spine holds invariants only, each decision with Binds, Prevents and Rule. UX is split into DESIGN.md and EXPERIENCE.md (IA table, state patterns including permission denied, key flows, surface closure).
- Addy spec-driven-development: stack-inclusive spec (objective, commands, structure, one real code snippet, testing, three-tier boundaries), numbered assumptions up front, capability map with stable module IDs and build order, stop the turn after the spec.
- alirezarezvani spec-driven-workflow: nine mandatory sections including API contracts as typed interfaces with error responses and a data-model table; N/A with a reason for non-applicable sections; bounded autonomy that stops on ambiguity, security or breaking changes.
- alirezarezvani code-to-prd: reverse-engineers one file per page from existing code: overview, layout regions, field inventory table, interaction logic as Action, Response, Validation, API, Success, Failure, role-based permission controls, API dependencies, page relationships; plus an enum dictionary, API inventory and page-relationship appendix. This is the closest existing shape to your per-page files.
- harness product-requirements: Iron Law that every story has a measurable criterion or an open named gap; EARS grammar; MoSCoW; a gap interview in plain text.
- Anthropic write-spec, feature-forge, prd-writing: conventional PRDs (problem, goals, non-goals, stories, P0 to P2 requirements, metrics, open questions).

**Checking the requirements.**

- Spec Kit checklist: unit tests for English. Questions about requirement quality (completeness, clarity, consistency, measurability, scenario coverage, edge cases) with traceability markers; generation never ticks items.
- Spec Kit analyze: read-only coverage and consistency across artifacts with stable keys and a coverage percentage.
- BMAD: deterministic ID linter (undefined, duplicate, unknown prefix, withdrawn-but-referenced), deterministic structure lint, then rubric and lens reviewers as isolated subagents; a five-dimension rubric (decision-ready, earned, testable, honest scope, usable downstream); a stakes ladder from hobby to regulated that scales depth.
- harness spec-craft: seven rubrics (sharpness, cuts at the joints, two readers same understanding, load-bearing versus ambient, honest rationalizations, non-goals are real non-goals, stranger in six months).
- secondsky spec-reviewer: four dimensions scored out of 25.

### 7.2 Ideas worth carrying

- BMAD altitude plus global IDs plus an ID linter script, and the load-bearing test (a claim stays only if a downstream consumer would decide differently without it).
- Spec Kit's requirement-quality checklists and read-only coverage analysis.
- The per-page file shape from code-to-prd, authored forward for greenfield.
- Addy's capability map with stable module IDs, assumption lists, and the stop-and-wait gate.
- interview-me's protocol, spec-craft's rubrics, BMAD's rule to never invent a regulation, citation or threshold, and its single-writer rule for derived content.
- Addy's CONSTRAINTS.md idea (numeric, checkable quality bars with defaults, so that I don't know still yields a config) as a candidate for non-functional requirements.

### 7.3 Conflicts needing a house rule

Stack in the spec or not; elicitation style and whether ask-user tools are required, optional or banned; priority scale; acceptance grammar; unknown and assumption tags; ID scheme; document size (BMAD's lean ceilings versus your wish for exhaustive per-page detail).

### 7.4 Gaps no source covers (written from scratch)

1. Forward-authored per-page requirement files with data bindings, permission per element and a states matrix (loading, empty, error, denied, offline).
2. Per-function backend contracts at requirements level: inputs, return values, errors, authorization, side effects, tied to IDs.
3. Database requirements: per-table purpose, owner, per-role access, authentication versus authorization.
4. One ID scheme and linter spanning requirement, page, function and table.
5. A stack-first flow: a stack decision record before the spec.
6. A path for improving the user's own existing idea.

### 7.5 Six decisions to make (options with a suggested lean; none decided yet)

1. **Artifact set and hierarchy.** (a) one spec per feature (Spec Kit); (b) capability-based living specs (OpenSpec); (c) an indexed hierarchy of per-page, per-function and per-table files sharing global IDs, built on BMAD altitude and the code-to-prd page shape. Lean: (c).
2. **Stack position.** Stack decision record first, then a stack-inclusive spec (Addy), or a technology-agnostic spec first. Lean: stack first, as you required.
3. **Elicitation protocol.** One question at a time in plain text with a recommended guess attached, with optional ask-user tool UI where available; or open-ended coaching. Lean: one at a time with a guess, plain text first.
4. **House grammar.** Requirement sentence in MUST, SHOULD, MAY plus Given/When/Then scenarios; global stable IDs; MoSCoW for scope with P0 to P3 reserved for severity. Lean: as stated.
5. **Validation.** Layer a deterministic ID and structure linter, requirement-quality checklists, and an isolated reviewer with a degraded fallback, matching the frontend block. Lean: all three.
6. **Depth scaling.** BMAD's stakes ladder (hobby to regulated) with N/A and a reason for skipped sections, or one fixed full depth. Lean: stakes ladder.

## 8. Remaining blocks: candidates, not yet read in depth

- **SDLC process.** Addy's lifecycle skills and rationalization-table anatomy; Superpowers' mandatory workflow; harness mechanical gates and cosmix/claude-loom as reference only; borkweb as precedent for adapting an upstream.
- **Backend logic.** Addy api-and-interface-design (contract first, one error shape, validate at boundaries, Hyrum's law), jeffallan api-designer, wshobson api-design-principles, architecture-patterns and auth-implementation-patterns, alirezarezvani api-design-reviewer, secondsky rest-api-design. Function and line-level logic design has no good source.
- **Database.** Supabase postgres-best-practices is the strongest (RLS, privileges, schema) but Supabase-flavored; also wshobson postgresql-table-design, alirezarezvani database-designer and schema designer, secondsky database-schema-design. A requirements-traceable data model with an authentication versus authorization matrix has no source.
- **Security.** Cloudflare security-audit (six phases, independent verifier, JSON schemas and validators, attack-class files per target type, needs an OS sandbox and Node); natolitech security-review and threat-model; hov172 secure-webapp (modes audit, quick-check, harden, design-review; check content attribution); wshobson stride-analysis-patterns; Trail of Bits and dralgorhythm as reference only.

## 9. Next steps

1. Decide the six requirements decisions in section 7.5.
2. Read the SDLC, backend, database and security skills in depth, block by block, the same way the frontend and requirements sources were read.
3. Write the house-style spec: skill anatomy, voice, severity P0 to P3, rule ID scheme, evidence format, question protocol.
4. Settle the open frontend question about Vercel's React rules.
5. Design packaging: one Markdown source plus per-agent adapters, following the wshobson or Addy pattern.
6. Write the license plan: attribution and NOTICE files, Apache change marks, no BMAD name, decision on Trail of Bits.
7. Build the small checker scripts: frontend rule and contrast checks, and the requirements ID linter.

## 10. Rebuilding the working environment

The clones and working notes lived in a container that resets between sessions. Re-clone with:

```
for r in anthropics/skills pbakaus/impeccable nextlevelbuilder/ui-ux-pro-max-skill vercel-labs/agent-skills vercel-labs/web-interface-guidelines cloudflare/security-audit-skill addyosmani/agent-skills obra/superpowers github/spec-kit Fission-AI/OpenSpec bmad-code-org/BMAD-METHOD supabase/agent-skills trailofbits/skills hov172/secure-webapp-skill jeffallan/claude-skills wshobson/agents alirezarezvani/claude-skills secondsky/claude-skills Intense-Visions/harness-engineering borkweb/skills anthropics/knowledge-work-plugins asyrafhussin/agent-skills borghei/claude-skills natolitech/security-skill cosmix/claude-loom MadAppGang/claude-code dralgorhythm/claude-agentic-framework daffy0208/ai-dev-standards; do
  git clone --depth 1 https://github.com/$r.git $(echo $r | tr / _)
done
```

The detailed working notes were folded into this document. Key file locations inside the clones: Impeccable source is skill/ (SKILL.src.md plus reference/); UI UX Pro Max is src/ui-ux-pro-max and .claude/skills; Vercel skills are under skills/; BMAD skills are under skills/ (bmad-agent-pm, bmad-architecture, bmad-ux, bmad-agent-po, bmad-facilitate); Spec Kit templates are under templates/ and templates/commands/; OpenSpec schema is schemas/spec-driven; harness skills are under agents/skills/claude-code; code-to-prd is under product-team/code-to-prd in alirezarezvani's repo.

## 11. Reading coverage and known gaps

- **Frontend.** Impeccable was read in full except adapt, optimize and onboard (first 45 lines each), document.md beyond line 140, and skims of live, generate and doctor. Not read: the Rust detector's 62 rules, the asset-producer and manual-edit-applier agents, its tests. UI UX Pro Max: SKILL.md and both references read, CSVs by header and first rows only, design\_system.py not read. Vercel: the full web rulebook, the SKILL.md files, 2 sample rules of about 70. Anthropic design plugin: critique, design-system and accessibility fully; the rest by head.
- **Requirements.** Not read: Superpowers writing-plans, Spec Kit constitution, converge and implement commands, BMAD slice, forge-idea and analyst skills, harness-brainstorming, OpenSpec explore and propose skills, Anthropic product-brainstorming, Addy planning and ADR skills, spec-to-repo, the reference files of feature-forge, plan-interview and prd-writing, and the PRD skills of the borghei and dralgorhythm repos.
- **Other blocks.** Only READMEs and search listings were read for SDLC, backend, database and security.

## 12. Working conventions

- In any code, comments are plain and generic (for example a comment reading Table builders). Never use decorative divider lines in comments.
- Ask one question at a time and prefer tappable options for decisions.
- The user is often on mobile: keep chat replies short and put depth in documents.
