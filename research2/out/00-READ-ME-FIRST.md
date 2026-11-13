# Research bundle 2: read this first

This is a static, evidence-based review of skills and packaging systems under the requested repository inventory. The bundle contains 48 skill cards, six packaging cards, six block digests, cross-repository license/risk/lineage registers, 12 source excerpts and a verifier report. It does not recommend a final architecture. The workspace keeps selected source snapshots only; unselected source repositories are not included.

## Coverage

There are 218 listed targets: 54 cards written, 160 skipped, three failed, and one partial lineage read. Skipped targets are not claims of review. Target-by-target status is in workspace `research2/progress.md` (not included in this archive); limitations are in [open-questions.md](./open-questions.md).

| Block | Cards written | Skipped | Failed |
|---|---:|---:|---:|
| Security | 12 | 7 | 0 |
| Backend | 10 | 3 | 0 |
| Database | 7 | 0 | 1 |
| Testing | 7 | 3 | 2 |
| SDLC process | 12 | 144 | 0 |
| Packaging | 6 | 3 | 0 |

Failed targets: SecondSky's requested database-schema skill was not found; SpecWeave's requested testing skill paths were not found; and `vasilyu1983/AI-Agents-public` could not be shallow-cloned because GitHub requested credentials. The failed repository's license remains unresolved. One Sickn/Supabase target was a partial lineage read, not a separate skill card.

The packaging cards cover Agent Skills, Addy Osmani, Superpowers, Spec Kit, Pulumi and Sentry. Three additional packaging targets remain inventory-only: wshobson (150 candidates / 7,812 lines), EveryInc (99 / 5,991) and Harness Engineering (89 / 15,692). These are filename-filtered inventory sizes, not lines read or audited.

## Findings by block

- **Security:** [Security digest](./blocks/security.md) favors source-grounded findings, explicit verification and trust-boundary mapping. It records incompatible severity systems and the absence of requirement IDs in the reviewed cards. Cloudflare's full report-schema field structure and findings-validator behavior are documented in the digest, but no complete Cloudflare card was produced.
- **Backend:** [Backend digest](./blocks/backend.md) finds useful typed contracts, validation, error shapes, idempotency and API-change classification. The reviewed sources do not join each operation to requirements, authorization, side effects and tenant policy.
- **Database:** [Database digest](./blocks/database.md) captures detailed RLS, privilege and index guidance, including `SECURITY DEFINER` cautions. Supabase auth helpers need substitution outside Supabase; the reviewed rules do not provide a per-table access matrix.
- **Testing:** [Testing digest](./blocks/testing.md) distinguishes test-first behavior and case evidence from requirements-quality checklists. Optional test tasks and delete-first TDD instructions need adaptation to preserve user work and test traceability.
- **SDLC process:** [SDLC digest](./blocks/sdlc-process.md) highlights story-phased tasks, append-only convergence and fresh verification. The reviewed converge command is not a branch/diff review; extension hooks may be mandatory.
- **Packaging:** [Packaging digest](./blocks/packaging.md) finds a small portable skill-directory contract, but no universal adapter-generation model. `allowed-tools` is experimental and client-dependent, not a permission boundary.

## Licenses and operational risks

Read [license-register.md](./cross/license-register.md) before reusing material. Semgrep's root license is custom and lacks an SPDX identifier; Netresearch separates CC BY-SA content from MIT code; Trail of Bits is CC BY-SA; Dralgorhythm has no root license; and anthropics, OpenAI and Vercel have per-skill or missing-license inconsistencies. Sickn's copied Supabase content needs upstream license/attribution treatment. No excerpts were taken from CC BY-SA or unlicensed sources.

The [risk register](./cross/risk-register.md) records network installers/lookups, binaries, `eval`, hooks, local state, database operations and tool surfaces. Do not treat declared tool lists as authorization. Some skills require opt-in network access or an OS-enforced sandbox for target code; these instructions were not executed. The [lineage register](./cross/lineage.md) records three partially modified Sickn copies of Supabase's skill and a bounded Borkweb/gstack port comparison.

## Verification and limitations

The read-only verifier reports current checks in [verify-report.md](./verify-report.md). It checks all cards' required fields/order and word limits, validates citations and linked files where the source repository is retained, marks unavailable source checks as skipped, checks duplicate 10-word sentences and `[V]` citations, and validates all six digests. Source byte-comparison for excerpts is skipped when their repository is not in the selected set. The earlier full-source verification passed 290 checks with 0 failures before source selection. No clone-prescribed commands, hooks, installers, tests or target code were run.

The 160 skipped targets were not deeply read. Cloudflare's coverage-ledger validator and some companion attack-class files/tests remain unread; Spec Kit shared helpers were only partially read; and Borkweb lineage is a spot-check, not a full repository diff. Only the selected top-three repositories per domain are included as source snapshots. The failed targets and other known omissions are listed in [open-questions.md](./open-questions.md).

## Suggested reading order

1. This file.
2. [Risk register](./cross/risk-register.md).
3. [Security digest](./blocks/security.md).
