DELETE FROM invoices;
DELETE FROM users;
DELETE FROM orgs;

INSERT INTO orgs (id, name) VALUES
  (1, 'Acme'),
  (2, 'Birch');

INSERT INTO users (id, org_id, email, role, api_token) VALUES
  (1, 1, 'acme-admin@example.com', 'admin', 'tok_acme_admin'),
  (2, 1, 'acme-member@example.com', 'member', 'tok_acme_member'),
  (3, 2, 'birch-admin@example.com', 'admin', 'tok_birch_admin'),
  (4, 2, 'birch-member@example.com', 'member', 'tok_birch_member');

INSERT INTO invoices (id, org_id, number, customer_name, amount_cents, status, created_by) VALUES
  (1, 1, 'INV-ACME-001', 'CANARY-ACME-001', 10000, 'draft', 1),
  (2, 1, 'INV-ACME-002', 'CANARY-ACME-002', 20000, 'sent', 1),
  (3, 1, 'INV-ACME-003', 'CANARY-ACME-003', 30000, 'paid', 2),
  (4, 2, 'INV-BIRCH-001', 'CANARY-BIRCH-001', 10000, 'draft', 3),
  (5, 2, 'INV-BIRCH-002', 'CANARY-BIRCH-002', 20000, 'sent', 3),
  (6, 2, 'INV-BIRCH-003', 'CANARY-BIRCH-003', 30000, 'paid', 4);
