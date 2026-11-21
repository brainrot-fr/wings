<!-- FILE: wings/HANDOFF.md  (feed this + plan/01-06 + the 3 arch excerpts above) -->
# Wings handoff: where we are

## Who and constraints
- Builder: Syed Jalal, final-year ECE student, sole builder. Not experienced
  in UI design; has never worked on a team shipping a product; relies heavily
  on AI and wants ground-truth checks instead of trust.
- Style: terse, direct, professional engineering depth. Lead with
  architectural reasoning and dependency order, then structured output.
  Verified, cited sources preferred over unverified claims. Generic output
  is unacceptable.
- Deliverables are FENCED CODE BLOCKS (files), not prose docs.
- Do NOT use memory tools in this project.
- Plan to use GitHub Copilot as the implementing agent for apps; user runs
  oracles and tests by hand too.

## What wings is
A skill suite meant to make AI agents ship production-ready full-stack
apps. Reframed after review: its real differentiator is AGENT INTEGRITY,
i.e. an agent is not allowed to grade its own work. Mechanisms: incomplete
check never passes; measured vs attested evidence; ACCEPTANCE_EDITED and
TEST_EDITED detection; lane pass needs test count > 0; approvals bound to a
diff hash; generated authz matrix the code-writing step cannot edit.
A startup is planned later around wings (open-core suggested; hosted
verification/CI gates/benchmark as the proprietary layer). Startup claim to
TEST, not assume: cheap/flash models + wings still survive a security review.

## State of the work
- Analysis phase: done. 9 analysis chats, ~40 sources read. Corpus is FROZEN.
  No more reading except primary sources at write time (NIST, RFCs, WCAG).
- Design phase: kernel, requirements, testing designed as first-pass
  proposals (arch-*.md). Nothing shipped. Zero skills, zero evals so far.
- Prior mistake acknowledged: design ran ahead of evidence; "MVP" was 15
  blocks. Corrected: MVP = smallest build that can FALSIFY the central claim.
- Licensing: user will rewrite CC BY-SA sources (OWASP, Trail of Bits) in own
  words from primary sources; MIT/Apache with notices. Caveat given: a model
  paraphrase can still be a derivative; prefer writing from primary sources +
  own failure log, record provenance (provenance.md), confirm with a lawyer
  before going proprietary. Unlicensed repos (e.g. Vercel skill folders) not
  copied.

## Central claim and hypotheses (plan/02)
Claim: an agent with wings is less able to ship falsely-"done" work than
the same agent without it. H1 baseline failure >=30%; H2 wings halves it;
H3 a 20-line rules prompt (arm C) does NOT match wings; H4 cost < 2x.
(Thresholds are wings judgment, not sourced.)

## MVP v0 scope (plan/02)
IN: wings-lint.py (subcommands ids, lane, diff, matrix) with unit tests;
3 skills: requirements (audit+change modes), testing (gate mode),
code-review (diff mode, finding shape, coverage accounting); kernel-lite in
one hand-copied file; one spec file .wings/spec.md (R-, AC-, FN- blocks).
Target: Claude Code only (.claude/skills/).
OUT: everything else (Intent, Stack, Experience, Architecture, Data, Backend,
Identity, Security, Frontend, Ship, capability blocks, packs, commands,
other harnesses, build inlining, recover/greenfield, stakes ladder).
Cut rule: add only if a logged bench failure requires it.

## REVISED FLOW (supersedes the user's MVP-first order)
1. APP-1 spec ("Ledgerline": multi-tenant invoices, roles, one webhook;
   <=4 tables, <=8 endpoints, thin form; ONE stack for all runs).
2. Oracles for S1-S5 (written before any run; hidden from agents).
3. ORACLE SELF-TEST: each oracle must PASS a known-good APP-1 and FAIL a
   known-bad variant with the bug planted. Fix oracles until both hold.
4. Build APP-1 to a known-good state with Copilot, commit it = frozen
   fixture. Every run starts from that commit + task prompt only.
5. Baseline: arm A (no wings), 5 dev tasks x 3 reps. Record failure rates.
   Drop tasks agents never fail. This decides what the MVP must contain.
6. Build MVP (lint + tests can start in parallel with steps 1-5; SKILL.md
   text only AFTER baseline).
7. Run arms B (wings) and C (rules prompt), 3 reps. Then held-out S6-S8.
8. Fix loop (plan/05): classify F1-F7, log FL-n, ONE change per iteration,
   rerun target + all regression tasks, accept only if no regressions and
   false-positive rate does not rise.
9. Later: arm D (flash model) for the startup claim; APP-2 AcadFlow
   (brownfield), APP-3 messy repo (audit, 10 planted defects), APP-4 Notes
   (over-processing check).

## Bench design (plan/03, 04, 05)
Arms: A baseline, B wings, C rules-prompt, D wings-on-flash (+A on flash).
Tasks S1 cross-tenant read, S2 mass assignment, S3 weakened test,
S4 zero-run lane, S5 forged webhook (dev); S6 check-then-act race,
S7 false completion, S8 mocked unit (held-out; do not tune on them).
Score per run: seeded_failure_escaped, false_done_claim, gate_verdict,
blocked_correct_work (false positive = wings' cost), tokens, wall time.
Run record: transcript, diff, oracle.json, meta.json (wings hash, agent,
model+version, harness version). With 3 reps only read large differences
(3/3 vs 0/3). Hand-review 5 transcripts once to validate the oracles.

## Design decisions still in force (from arch files, all PROPOSED not final)
- IDs: prefix-hyphen-number, pattern [A-Z][A-Z0-9]{0,5}-\d+; never reuse or
  renumber; withdrawn / superseded by X (X must exist).
- Result vocab: check state pass/fail/not_run/inconclusive/n-a(reason);
  gate verdict PASS/FAIL/INCOMPLETE; finding verdict confirmed/
  needs_validation/rejected; evidence measured vs attested; severity P0-P3
  with confidence 1-10 separate.
- Gates: unrun check cannot pass; waivers human-only, logged; cycle cap 3
  ends in stop-and-report, never release.
- AC- ID goes in the test name (no test ID prefix); authz matrix in JSON,
  attached-mode only, generated from FN authorization lines.
- Auth/security house rules (e.g. NIST 63B-4 password minimums, 401/403/404
  denial codes, transaction-local tenant context) were carried from earlier
  reads and are NOT re-verified; re-check against primary sources before
  writing any as a rule.

## Known unverified items (do not treat as fact)
- All OWASP/Supabase/wshobson/gstack defect claims (summaries of summaries).
- Hand-computed contrast ratios. "Fabricated citation" suspicions.
- Codex 8 KB cap. Competitor landscape (Lovable, Bolt, Replit, v0, Cursor)
  not checked; "nobody focuses on this" must be verified.
- All numeric thresholds in plan/ are judgment.

## Housekeeping owed
Merge arch-*.md with context-arch-*.md (near duplicates); start
provenance.md; create bench/, runs/, FAILURES.md; move non-needed docs to
shelf/; commit and tag v0.0.

## NEXT CHAT: produce, as separate fenced files, in this order
1. APP-1 spec (Ledgerline): entities, endpoints, roles, webhook contract,
   stack choice rationale, seed data with tenant canary values.
2. Oracles S1-S5 (+ the shared harness) AND the known-bad variant recipe
   for each, so the self-test can run.
3. Copilot build prompt for the frozen APP-1 fixture.
4. Baseline run protocol (arm A) + run record templates.
Only after baseline results arrive: MVP files (wings-lint with tests,
the 3 skills, kernel-lite), shaped by observed failures.