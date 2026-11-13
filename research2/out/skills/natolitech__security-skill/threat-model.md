# natolitech/security-skill / threat-model
SOURCE: commit `3bdb1dc1922902a8907821ea663f0bbbfea79728` | MIT, root `LICENSE` | 236 lines
FRONTMATTER: `name: threat-model`; `description: Architecture-level STRIDE threat model derived from actual code, or from a git repository URL. Use when asked to threat model, model security threats, map an attack surface, or analyze trust boundaries and data flows.`
FILES READ:
| Path | Lines | Role |
|---|---:|---|
| `.claude/commands/threat-model.md` | 236 | Command |
FILES UNREAD: None in command; external standards not retrieved.
JOB: Build source-grounded STRIDE/privacy model, boundary map, ranked threats and top attack paths; save dated Markdown report. [V] (`.claude/commands/threat-model.md:L53-L55`, `.claude/commands/threat-model.md:L87-L154`, `.claude/commands/threat-model.md:L216-L223`)
PROCEDURE:
1. `Step 1`: map system, data and prior report. [V] (`.claude/commands/threat-model.md:L38-L52`)
2. `Step 2`: table entrypoints/auth/data/boundaries; draw Mermaid DFD with numbered crossings. [V] (`.claude/commands/threat-model.md:L53-L86`)
3. `Steps 3–4`: apply plausible STRIDE classes and privacy review. [V] (`.claude/commands/threat-model.md:L87-L135`)
4. `Steps 5–6`: assign `TM-NNN`, score, detail top 2–3 paths. [V] (`.claude/commands/threat-model.md:L136-L205`)
DECISION RULES: Likelihood Low/Medium/High; impact Low/Medium/High/Critical; combine with impact weight. Unknown deployment facts stay explicit. [V] (`.claude/commands/threat-model.md:L136-L154`, `.claude/commands/threat-model.md:L207-L215`)
ARTIFACT SHAPE: System/data overview, attack surface, boundaries/DFD, severity-grouped threats, paths, controls, mitigations and regulatory notes. [V] (`.claude/commands/threat-model.md:L160-L205`)
QUESTION PROTOCOL: None; record missing deployment facts. [V] (`.claude/commands/threat-model.md:L207-L215`)
VALIDATION: Static code/control review; no validator. [V] (`.claude/commands/threat-model.md:L207-L215`)
AGENT FEATURES REQUIRED: Shell only.
STATE ON DISK: Dated `security-reviews/threat-model-*.md`; prior reports inform reruns. [V] (`.claude/commands/threat-model.md:L38-L52`, `.claude/commands/threat-model.md:L216-L223`)
VOCABULARY: `TM-NNN`, `B1`… boundary IDs, STRIDE classes, likelihood/impact scales. [V] (`.claude/commands/threat-model.md:L53-L86`, `.claude/commands/threat-model.md:L87-L154`)
NON-OBVIOUS TECHNIQUES:
- Number trust-zone crossings for threat references. [V] (`.claude/commands/threat-model.md:L53-L86`)
- Run privacy pass when personal data exists. [V] (`.claude/commands/threat-model.md:L123-L135`)
- Detail top 2–3 paths; allow a composite chain. [V] (`.claude/commands/threat-model.md:L155-L205`)
FAILURE MODE FOUGHT: Theoretical diagrams and unsupported scores. [I] (`.claude/commands/threat-model.md:L53-L86`, `.claude/commands/threat-model.md:L207-L215`)
BAGGAGE: Clone workflow, dated report, likelihood/impact labels. [V] (`.claude/commands/threat-model.md:L27-L37`, `.claude/commands/threat-model.md:L136-L154`)
RISKS: Remote clone uses network; command suggests partial secrets, forbidden here. [V] (`.claude/commands/threat-model.md:L27-L37`, `.claude/commands/threat-model.md:L212-L214`)
FIT: security — **EXTRACT** boundary map, control inventory, privacy pass; add requirement links. [I] Template lacks requirement fields. [V] (`.claude/commands/threat-model.md:L160-L205`)
CONFLICTS: Likelihood/impact blend does not map directly to P0–P3.
KEY QUOTES:
- “Only document threats that are plausible given the actual implementation” — `.claude/commands/threat-model.md:L87-L90`
- “Verify before rating.” — `.claude/commands/threat-model.md:L212-L212`
CONFIDENCE: High for the documented method and artifact structure; no model run or quality evaluation was performed.
