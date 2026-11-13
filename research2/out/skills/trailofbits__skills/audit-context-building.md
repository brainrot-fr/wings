# trailofbits/skills / audit-context-building

SOURCE: `plugins/audit-context-building/skills/audit-context-building/` | commit `149d7b21f4067765b82e67029730b42d228ef4b4` | CC-BY-SA-4.0 (`LICENSE:L1`) | 820 lines read: target 393, root license 427; target counts by `find ... -print0 | sort -z | xargs -0 wc -l`.

FRONTMATTER: name `audit-context-building`; description paraphrase: map code assumptions/dependencies before audits [V] `plugins/audit-context-building/skills/audit-context-building/SKILL.md:L2-L4`.

FILES READ:
| Path | Lines | Role |
|---|---:|---|
| `plugins/audit-context-building/skills/audit-context-building/SKILL.md` | 72 | Workflow |
| `plugins/audit-context-building/skills/audit-context-building/resources/ANALYSIS_FORMAT.md` | 68 | Record schema/rubric |
| `plugins/audit-context-building/skills/audit-context-building/resources/DOMAIN_NOTES.md` | 73 | Domain guidance |
| `plugins/audit-context-building/skills/audit-context-building/resources/FUNCTION_MICRO_ANALYSIS_EXAMPLE.md` | 174 | C/Solidity examples |
| `plugins/audit-context-building/skills/audit-context-building/agents/openai.yaml` | 6 | Agent metadata |
| `LICENSE` | 427 | License text |

FILES UNREAD: `plugins/audit-context-building/skills/audit-context-building/assets/trail-of-bits-mark.svg` (1 line; icon identified only); `/audit-context-building:audit-context` and `audit-context-building:function-analyzer` definitions (not opened; outside target).

JOB:
- Trigger: unfamiliar-code audit, threat model, or architecture review.
- Input: code path; output: `audit-context/DOSSIER.md` and per-function files in `audit-context/functions/` [V] `plugins/audit-context-building/skills/audit-context-building/SKILL.md:L11-L16,L25-L33`.

PROCEDURE:
1. `When to Use`: orient before hunting.
2. `Do not analyze in this context`: dispatch multiple functions to `/audit-context-building:audit-context <path>`; dispatch one to `audit-context-building:function-analyzer`.
3. `What comes back, and how to read it`: use records and dossier; preserve disagreements and open questions.
4. `The format`: follow calls; mark unsupported assumptions `nothing found`. [V] `plugins/audit-context-building/skills/audit-context-building/SKILL.md:L11-L16,L25-L35,L41-L56,L58-L72`.

DECISION RULES: No vulnerability, fix, PoC, or severity; skip familiar code; every claim needs a line or open question; follow all callee paths; no thresholds. [V] `plugins/audit-context-building/skills/audit-context-building/SKILL.md:L17-L23,L68-L72` `plugins/audit-context-building/skills/audit-context-building/resources/ANALYSIS_FORMAT.md:L46-L67`.

ARTIFACT SHAPE: `Purpose`; `Inputs & Assumptions`; `Outputs & Effects`; `Block-by-Block`; `Cross-Function Dependencies`; `Open Questions`. Dossier adds cross-function rules/reachability/complexity [V] `plugins/audit-context-building/skills/audit-context-building/resources/ANALYSIS_FORMAT.md:L11-L42` `plugins/audit-context-building/skills/audit-context-building/SKILL.md:L43-L46`.

QUESTION PROTOCOL: No user interview; unresolved issues remain in `Open Questions`.

VALIDATION: No scripts in `find` inventory. Rubric: citation and call-path review; model-judged, no deterministic validator named [V] `plugins/audit-context-building/skills/audit-context-building/resources/ANALYSIS_FORMAT.md:L46-L67`.

AGENT FEATURES REQUIRED: subagents; hooks/ask-user/MCP/browser/shell none specified; allowed tools `Workflow Task Read Grep Glob` [V] `plugins/audit-context-building/skills/audit-context-building/SKILL.md:L4,L25-L38`.

STATE ON DISK: `audit-context/DOSSIER.md`; per-function files under `audit-context/functions/` [V] `plugins/audit-context-building/skills/audit-context-building/SKILL.md:L25-L33`.

VOCABULARY: severity deferred; priority/IDs unspecified; trust `untrusted | semi-trusted | trusted`; marker `nothing found`; `Open Questions`; line citations [V] `plugins/audit-context-building/skills/audit-context-building/SKILL.md:L17-L21,L68-L72` `plugins/audit-context-building/skills/audit-context-building/resources/ANALYSIS_FORMAT.md:L6-L19,L42-L49`.

NON-OBVIOUS TECHNIQUES: [V] Follow all callee paths `plugins/audit-context-building/skills/audit-context-building/SKILL.md:L68-L72`; [V] map unknown contract/firmware callees as black boxes `plugins/audit-context-building/skills/audit-context-building/resources/DOMAIN_NOTES.md:L16-L28,L55-L60`; [V] start firmware coverage from task and handler entry points `plugins/audit-context-building/skills/audit-context-building/resources/DOMAIN_NOTES.md:L46-L58`.

FAILURE MODE FOUGHT: Caller-only reading can mistake a callee's name or success path for an established guarantee. [I] `plugins/audit-context-building/skills/audit-context-building/SKILL.md:L50-L56,L68-L72`.

BAGGAGE: Per-function analysis plus mandatory dispatch creates orchestration cost. [I] `plugins/audit-context-building/skills/audit-context-building/SKILL.md:L25-L38`.

RISKS: Output enforcement depends on a subagent return schema. [V] `plugins/audit-context-building/skills/audit-context-building/SKILL.md:L35-L38`.

FIT: Security — ADAPT evidence-linked assumptions/call continuity; take `SKILL.md`, `resources/ANALYSIS_FORMAT.md`, `resources/DOMAIN_NOTES.md`.

CONFLICTS: [I] The skill makes subagent schema enforcement central, limiting portability when that mechanism is unavailable `plugins/audit-context-building/skills/audit-context-building/SKILL.md:L25-L38`.

KEY QUOTES: None; paraphrase only.

CONFIDENCE: Medium; in-folder text resources read; named companion implementations not opened.
