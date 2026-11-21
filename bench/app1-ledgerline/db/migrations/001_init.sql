CREATE TABLE IF NOT EXISTS orgs (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY,
  org_id INTEGER NOT NULL REFERENCES orgs(id),
  email TEXT NOT NULL UNIQUE,
  role TEXT NOT NULL CHECK (role IN ('admin', 'member')),
  api_token TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS invoices (
  id INTEGER PRIMARY KEY,
  org_id INTEGER NOT NULL REFERENCES orgs(id),
  number TEXT,
  customer_name TEXT,
  amount_cents INTEGER NOT NULL CHECK (amount_cents >= 0),
  status TEXT NOT NULL CHECK (status IN ('draft', 'sent', 'paid')),
  created_by INTEGER REFERENCES users(id),
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  UNIQUE (org_id, number)
);

CREATE INDEX IF NOT EXISTS idx_invoices_org_created
  ON invoices (org_id, created_at);
