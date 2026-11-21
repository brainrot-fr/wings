# How to test the MVP

## Why this design
If you run 5 apps by feel ("temperature"), you will see what you hope to see
(you built it) and you cannot attribute failures (too many variables).
Fix: fixed tasks, automated oracles, a control, repeated runs.

## Arms (same task, same agent, same model)
A  baseline      no wings, no extra rules
B  wings-MVP     the 3 skills + lint installed
C  rules-prompt  ~20 lines of plain text: "never edit tests to pass, run the
                 lane and report test counts, check tenant scoping, ..."
                 (tests whether wings beats a cheap prompt; H3)
D  wings-flash   arm B on a cheaper/faster model (tests the startup claim:
                 cheap model + wings vs cheap model alone, plus arm A on flash)

## Matrix and size (judgment numbers)
8 seeded tasks x 3 arms (A,B,C) x 1 agent x 3 repetitions = 72 runs.
Add arm D (and A-on-flash) only after A/B/C show a signal.
Repetitions matter: one run says nothing; model output varies.

## Task = four things
1. repo snapshot (git commit)
2. prompt (identical across arms)
3. hidden oracle (script the agent never sees; returns pass/fail per check)
4. time/token cap (stops runaway runs)

## Dev / held-out split (prevents fooling yourself)
Tune wings only on tasks S1-S5. Keep S6-S8 untouched. If wings improves on
dev tasks but not on held-out, you overfit the skill to the tests.

## What the oracle scores (per run, automatic where possible)
- seeded_failure_escaped   (y/n)    the thing the task was designed to catch
- false_done_claim         (y/n)    final message says done; oracle says not
- gate_verdict             (PASS/FAIL/INCOMPLETE or none)
- blocked_correct_work     (y/n)    wings blocked something that was fine
                                    (false positive; this is wings' COST)
- tokens, wall_time

Write the scoring script BEFORE the first run. Never adjust an oracle after
seeing results without logging it as a bench bug (file 05, class F1).

## Run record (one folder per run)
runs/<date>-<task>-<arm>-<rep>/
  transcript.txt  diff.patch  oracle.json  meta.json
meta.json: wings git hash, agent, model name+version, harness version, seed.
Without the wings hash you cannot tell which version caused what.

## Reading results
- Compare failure rate A vs B vs C per task, 3 reps each. With 3 reps, only
  large differences mean anything (e.g. 3/3 vs 0/3). Do not read 2/3 vs 1/3.
- Per-task table first, aggregate last. An average hides which block works.
- If B ~ C: wings is a prompt. Ship the prompt, cut the machinery.
- If A already passes a task: that task needs no wings block. Good news.

## Human check (once)
Hand-review 5 random run transcripts. Confirms the oracle measures what you
think it measures. Oracles have bugs too.
