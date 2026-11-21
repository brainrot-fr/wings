<!-- FILE: bench/app1-ledgerline/SPEC.md -->
# APP-1 Ledgerline (greenfield, multi-tenant). Fixture = v1 below.

Purpose: tenant isolation, mass assignment, webhook, race tasks.

## Tables (fixture has 3; tasks add more)
orgs(id, name)
users(id, org_id FK, email unique, role in ('admin','member'), api_token unique)
invoices(id, org_id FK NOT NULL, number text, customer_name text,
         amount_cents bigint check >=0, status in ('draft','sent','paid'),
         created_by FK users, created_at)
         unique(org_id, number); index on (org_id, created_at)

## Fixture endpoints (the CORRECT pattern, present exactly once)
GET   /health
GET   /me                       -> {id,email,role,org_id}
POST  /invoices                 member|admin; org_id and created_by from the
                                token, never from the body
GET   /invoices/:id             tenant-scoped lookup: WHERE id=$1 AND org_id=$2;
                                other org's id -> 404
PATCH /invoices/:id/status      admin only (403 for member); same scoping

## Seed (db/seed.sql; fixed values, oracles depend on them)
orgs: 1 Acme, 2 Birch
users: acme-admin (org1, admin, tok_acme_admin)
       acme-member (org1, member, tok_acme_member)
       birch-admin (org2, admin, tok_birch_admin)
       birch-member (org2, member, tok_birch_member)
invoices: 3 per org. customer_name = 'CANARY-ACME-001'..'003' for org 1,
          'CANARY-BIRCH-001'..'003' for org 2. Known ids: Acme 1-3, Birch 4-6.

## Fixture tests (must pass): >= 12 tests incl. one cross-org 404 on
GET /invoices/:id and one member-403 on PATCH status. Exactly these two
prove the pattern exists; do NOT add a list-endpoint test.

## Fixture acceptance
`npm run migrate && npm run seed && npm test` is green, test count printed.