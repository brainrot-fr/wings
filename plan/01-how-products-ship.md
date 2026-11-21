# How a real product ships, breaks, and gets fixed

Read this first. Everything else in wings exists to protect one step in this loop.

## The loop (every team that ships, at any size)

  plan -> build -> review -> CI (automated checks) -> deploy -> monitor
                                                        |
        regression test <- fix <- diagnose <- incident <-+

Each arrow is a place where something can fail silently.

## A concrete story (read it as "if we do this, this happens")

1. Task: "add GET /invoices". An agent writes it, writes a test, CI is green.
2. The endpoint filters by invoice id but not by tenant.
3. Org B's user requests an id belonging to Org A. It returns Org A's data.
4. Nobody noticed: the test only used one tenant. Green CI proved nothing.
5. A customer reports it (this is the incident). Severity P0: data leak.
6. Diagnose: "why did CI pass?" -> no cross-tenant test existed.
7. Fix the code. THEN add the cross-tenant test (regression test) so this
   class of bug cannot return unnoticed.
8. Postmortem (blameless): write what happened, why checks missed it, and
   which new check now exists. The check is the real output, not the apology.

## What wings is, in this model

Wings is not "a faster way to build". It is steps 3, 6 and 7 done BEFORE
the customer does them:
- generate the cross-tenant test from the spec (so the agent cannot skip it)
- refuse to call a lane "pass" if zero tests ran
- refuse to let an agent edit a test/AC to turn red into green

Your differentiator is: the agent is not allowed to grade its own work.

## Vocabulary you will see in real teams
- Oracle: independent source of truth for "correct" (a hidden test, a human).
- Regression: something that worked and broke. Regression test: guards it.
- Severity: P0 data loss/leak/outage ... P3 cosmetic. Decides fix order.
- Rollback: undo a deploy. Always plan it before you deploy.
- Postmortem: written record of an incident. Blameless = about systems.
- Flaky: test that fails/passes randomly. Never "fix" by retrying to green.

## How to learn this without a team (do these, in order)
1. Read 3-5 real public postmortems. (danluu/post-mortems on GitHub is a
   curated list; Google's SRE book is free online. Verify both yourself.)
2. Ship AcadFlow to a few real users. Let something break. Run the loop above
   on it, on paper, including the postmortem.
3. Once: get one working engineer to review a seeded-bug PR from the bench
   and compare their findings to wings'. Their misses/catches are calibration
   data you cannot get from an AI.

## Rule for working with AI when you lack experience
For every AI-made decision, write down: "how would I detect that this is
wrong?" If the answer is "I wouldn't", it needs an oracle before it goes in.
