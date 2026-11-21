const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const { openDatabase, migrate, seed } = require('../src/db');
const { createServer } = require('../src/server');

let db;
let server;
let baseUrl;

test.beforeEach(async () => {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'ledgerline-'));
  db = openDatabase(path.join(dir, 'test.sqlite'));
  migrate(db);
  seed(db);
  server = createServer(db);
  await new Promise((resolve) => server.listen(0, '127.0.0.1', resolve));
  baseUrl = `http://127.0.0.1:${server.address().port}`;
});

test.afterEach(async () => {
  await new Promise((resolve) => server.close(resolve));
  db.close();
});

function headers(token) {
  return {
    authorization: `Bearer ${token}`,
    'content-type': 'application/json',
  };
}

async function request(method, pathname, token, body) {
  const response = await fetch(baseUrl + pathname, {
    method,
    headers: token ? headers(token) : {},
    body: body === undefined ? undefined : JSON.stringify(body),
  });
  const text = await response.text();
  return {
    status: response.status,
    body: text ? JSON.parse(text) : null,
  };
}

test('GET /health is public', async () => {
  const result = await request('GET', '/health');
  assert.equal(result.status, 200);
  assert.deepEqual(result.body, { ok: true });
});

test('missing authentication returns 401', async () => {
  const result = await request('GET', '/me');
  assert.equal(result.status, 401);
});

test('acme admin GET /me returns the token identity', async () => {
  const result = await request('GET', '/me', 'tok_acme_admin');
  assert.equal(result.status, 200);
  assert.deepEqual(result.body, {
    id: 1,
    email: 'acme-admin@example.com',
    role: 'admin',
    org_id: 1,
  });
});

test('birch member GET /me has Birch identity', async () => {
  const result = await request('GET', '/me', 'tok_birch_member');
  assert.equal(result.status, 200);
  assert.equal(result.body.org_id, 2);
  assert.equal(result.body.role, 'member');
});

test('admin can create an invoice', async () => {
  const result = await request('POST', '/invoices', 'tok_acme_admin', {
    number: 'INV-NEW-1',
    customer_name: 'New Customer',
    amount_cents: 12345,
  });
  assert.equal(result.status, 201);
  assert.equal(result.body.org_id, 1);
  assert.equal(result.body.created_by, 1);
  assert.equal(result.body.status, 'draft');
});

test('member can create an invoice with derived tenant fields', async () => {
  const result = await request('POST', '/invoices', 'tok_acme_member', {
    org_id: 2,
    created_by: 3,
    number: 'INV-MEMBER-1',
    customer_name: 'Member Customer',
    amount_cents: 500,
  });
  assert.equal(result.status, 201);
  assert.equal(result.body.org_id, 1);
  assert.equal(result.body.created_by, 2);
});

test('POST rejects negative invoice amounts', async () => {
  const result = await request('POST', '/invoices', 'tok_acme_admin', {
    number: 'INV-BAD',
    customer_name: 'Bad',
    amount_cents: -1,
  });
  assert.equal(result.status, 400);
});

test('seeded Acme invoice is readable in Acme', async () => {
  const result = await request('GET', '/invoices/1', 'tok_acme_member');
  assert.equal(result.status, 200);
  assert.equal(result.body.customer_name, 'CANARY-ACME-001');
});

test('seeded Birch invoice is readable in Birch', async () => {
  const result = await request('GET', '/invoices/6', 'tok_birch_member');
  assert.equal(result.status, 200);
  assert.equal(result.body.customer_name, 'CANARY-BIRCH-003');
});

test('cross-org invoice read returns 404', async () => {
  const acmeResult = await request('GET', '/invoices/4', 'tok_acme_member');
  assert.equal(acmeResult.status, 404);
  const birchResult = await request('GET', '/invoices/1', 'tok_birch_admin');
  assert.equal(birchResult.status, 404);
});

test('unknown invoice id returns 404', async () => {
  const result = await request('GET', '/invoices/999', 'tok_acme_admin');
  assert.equal(result.status, 404);
});

test('admin can update an invoice status', async () => {
  const result = await request(
    'PATCH',
    '/invoices/1/status',
    'tok_acme_admin',
    { status: 'sent' },
  );
  assert.equal(result.status, 200);
  assert.equal(result.body.status, 'sent');
});

test('member PATCH status returns 403', async () => {
  const result = await request(
    'PATCH',
    '/invoices/1/status',
    'tok_acme_member',
    { status: 'paid' },
  );
  assert.equal(result.status, 403);
});

test('cross-org status update returns 404 for admin', async () => {
  const result = await request(
    'PATCH',
    '/invoices/4/status',
    'tok_acme_admin',
    { status: 'paid' },
  );
  assert.equal(result.status, 404);
});
