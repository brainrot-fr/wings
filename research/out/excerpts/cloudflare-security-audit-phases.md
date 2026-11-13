# Repo: cloudflare__security-audit-skill
HEADER: path=/home/syed-jalal/dev/wings/research/repos/cloudflare__security-audit-skill/README.md | commit=c1c8a8c1471069fb0e188eeaff69b8e8db6564a8 | license=LICENSE

## What it does

The skill runs a structured audit in six phases:

1. Reconnaissance -- map architecture, trust boundaries, input surfaces, prior evidence, and deterministic coverage in `architecture.md` and `coverage-ledger.json`.
2. Coverage-led hunting -- assign isolated hunters from ledger units, record their checks, and use coverage critics to find gaps.
3. Candidate validation -- give every unique candidate to a fresh verifier that tries to disprove it.
4. Structured output -- write `confirmed`, `needs_validation`, and `rejected` records to `findings.json` and validate them against `report-schema.json`.
5. Independent record verification -- fresh agents verify final source claims. Material replacements receive another independent verifier.
6. Target-neutral reporting -- derive `REPORT.md`, `FINDINGS-DETAIL.md`, and `NEEDS-VALIDATION.md` from the verified records and coverage ledger.

