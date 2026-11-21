<!-- FILE: bench/app1-ledgerline/COPILOT-BUILD-PROMPT.md -->
Build the repository described in SPEC.md and 00-conventions.md exactly.
Do not add endpoints, tables, or features beyond SPEC.md. Follow the
conventions file. Requirements:
1. Implement the 5 fixture endpoints, migrations, seed.sql with the exact
   seed values, and the tests listed.
2. Derive org_id and created_by from the authenticated token only.
3. Every query touching invoices must be scoped by org_id.
4. Write a README with the commands to migrate, seed, and test.
5. Run migrate, seed and tests; paste the test count in the README.
Do not create any file named like an oracle, bench, or attack test.
Stop when the fixture acceptance line is true.
Then I will review it and tag it v1.