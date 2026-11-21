# MVP v0 definition

MVP = the smallest thing that can FALSIFY the central claim. Not the smallest
thing that looks complete.

## Central claim (one sentence)
An agent using wings is less able to ship work that falsely claims to be
done, than the same agent without it.

## Hypotheses (written BEFORE running anything)
H1  Without wings, agents commit seeded integrity failures at a rate high
    enough to matter (baseline failure rate >= 30%: wings judgment).
H2  With wings-MVP, that rate drops by at least half.
H3  A 20-line plain-text rules prompt (arm C in file 03) does NOT match
    wings. If it does, wings' machinery is not earning its complexity.
H4  Cost of wings (extra tokens/time) stays under 2x baseline (judgment).

If H1 fails (agents already do fine), stop and re-aim. That is a result,
not a failure. If H3 fails, shrink wings to the prompt.

## IN (v0)
- wings-lint.py, 4 subcommands, with its own unit tests:
    ids     define/reference/duplicate/withdrawn checks on R- AC- FN-
    lane    parse test result file; ZERO-RUN = fail; unknown = inconclusive
    diff    deleted tests, fewer assertions, new skip/only, ACCEPTANCE_EDITED
    matrix  generate authz cells from FN lines; compare generated vs executed
- 3 skills: requirements (audit + change modes only), testing (gate mode),
  code-review (diff mode, K5 finding shape, coverage accounting)
- kernel-lite: result vocabulary (K4), finding shape (K5), approval rules (K7)
  in ONE file, hand-copied. No build inlining yet.
- One spec file: .wings/spec.md with R-, AC-, FN- blocks.

## OUT (v0) - deliberate
Intent, Stack, Experience, Architecture, Data, Backend, Identity, Security,
Frontend, Ship blocks; capability blocks; stack packs; commands; packaging
for other harnesses; build step and hash-drift lint; recover and greenfield
modes; stakes ladder; fresh-context reviewer machinery.
Target harness: Claude Code only, skills in .claude/skills/.

## Cut rule for every proposed addition
Add it only if a logged bench failure (file 05) says it is needed.
"It would be nice / source X has it" is not a reason.

## Done = all true
[ ] lint has unit tests with seeded good and bad fixtures, all pass
[ ] each of the 4 subcommands catches its seeded bug on a fixture repo
[ ] SKILL.md files each under 200 lines (judgment; keeps the MVP small)
[ ] bench (file 03) runs end to end once on one task, all 3 arms
