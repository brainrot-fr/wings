# How to grow from MVP v0

## Why this design
Growth by source ("repo X has a nice skill") produced 26 documents and no
shipped skill. Growth by evidence means each new piece has a logged reason.

## The growth rule
A new block, mode, or script enters wings only if ALL are true:
1. A logged failure (FL-n) of class F6 (missing) repeats across >= 2 tasks.
2. A seeded task exists that reproduces it, with an oracle.
3. The smallest fix is a script/slot/rule, and arm B fails the task today.
4. After adding it, arm B passes and the regression set still passes.

## Version gates
v0   MVP (file 02). Bench runs. Baseline recorded.
v0.1 Fix top failures from first full bench run. No new blocks.
v0.2 If APP-4 shows over-processing: add a "light path" (fewer gates for
     small work) BEFORE any new block.
v0.3 First new block, chosen purely from the failure log. Likely candidates
     (hypotheses, not decisions): Identity rules, Plan & Build tickets.
v1   Held-out tasks pass; two outside users have installed it and reported.
Only after v1: other harnesses, packaging, packs, capability blocks.

## Use the design work you already did
The 26 documents are an idea library, not a spec. When a failure says
"missing", pull the relevant mechanism from them and write it from a primary
source. Everything not pulled stays on the shelf. That is not waste; it is
inventory.

## Housekeeping (do now, 30 minutes)
- Merge arch-*.md and context-arch-*.md into one set (one home per fact).
- Start provenance.md: for every adapted rule, source + license + date.
- Create runs/, FAILURES.md, bench/ folders. Commit. Version tag v0.0.

## Weekly rhythm (solo)
Mon: run bench on current version.   Tue: triage failures into FAILURES.md.
Wed-Thu: one fix, rerun.            Fri: write 5 lines: what changed, what the
data says, what you will not build yet. Those 5 lines are your postmortem
habit; they are what a team would otherwise give you.
