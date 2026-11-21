# Identify, note, and fix what went wrong

## Why this design
A fix without a diagnosis is a guess. A diagnosis without a log is forgotten.
Teams that improve have: a failure log, a taxonomy, and "fix + regression
test" as one unit.

## Step 1: Identify - classify every failed run (pick ONE class)

F1 bench bug      oracle or task is wrong (agent was right, test is wrong)
F2 not loaded     skill never triggered (description/routing problem)
F3 ignored        skill loaded, agent did not follow it
                  -> form problem: prose where a script or REQUIRED slot
                     was needed
F4 wrong text     skill instruction was wrong, ambiguous, or contradicted
F5 script bug     lint/lane/diff gave a false pass or false block
F6 missing        no rule exists for this failure yet (real gap)
F7 environment    model limit, timeout, tool unavailable, flaky infra

Also log FALSE POSITIVES (wings blocked correct work). They are failures
of wings, class F4/F5, and they decide whether people keep it installed.

How to tell which class: read the transcript at the decision point.
- Did the agent mention/load the skill? no -> F2
- Did it read the rule and do otherwise? -> F3
- Did it follow the rule and still fail? -> F4 or F5 or F6
- Rerun the oracle on the agent's output by hand -> if oracle is wrong -> F1

## Step 2: Note - one entry per failure (append-only, never edit history)

runs/FAILURES.md
---
id: FL-014
date: YYYY-MM-DD
run: 2026-..-S1-B-2
wings: <git hash>

class: F3
severity: P1            (what would this cost a real user?)
what_happened: agent added tenant filter to GET but not to export endpoint
evidence: transcript.txt:412-430, diff.patch hunk 3
root_cause: skill says "same predicate for list/count/export" as prose; agent
            never generated export cell
fix_hypothesis: matrix script emits one cell per read-shaped FN; gate fails
                if any cell is not executed
status: open | fixed-in <hash> | wontfix(reason) | bench-bug
---

IDs FL-n are never reused (same rule as your R-/AC- IDs).

## Step 3: Fix - one change per iteration

1. Pick the highest-severity open failure that repeats across reps/tasks.
2. Write the fix hypothesis: "changing X will make failure FL-n stop because Y".
3. Make ONE change. Two changes at once = you cannot attribute the result.
4. Rerun: the failing task (3 reps) + ALL regression tasks (everything that
   passed before).
5. Accept only if: target failure rate drops AND nothing that passed now fails
   AND false-positive rate did not rise. Otherwise revert.
6. Mark FL-n fixed-in <hash>. The failing task stays in the bench forever.
   (That is the regression test for wings itself.)

## Fix-type ladder (prefer the top; it is cheaper and more reliable)
1. Script/oracle-enforced check   (agent cannot talk its way out)
2. REQUIRED slot in a template    (omission becomes visible)
3. Prohibition + rationalization  (discipline failures only)
4. More prose                     (last resort; often does nothing)

## If we do this, this happens
- Skip the log        -> same failure re-fixed three times, no learning.
- Edit the oracle to  -> bench now measures your hopes; log as F1 with
  make wings look good   a reason, rerun everything.
- Fix on dev tasks    -> held-out tasks reveal overfit. Keep S6-S8 clean.
  only
- Add a block for     -> complexity grows, nothing proven. Cut rule in
  "completeness"         file 02 forbids it.
