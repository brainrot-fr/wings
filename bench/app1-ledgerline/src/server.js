const http = require('node:http');
const { URL } = require('node:url');
const { openDatabase, migrate } = require('./db');

function sendJson(res, status, body) {
  const payload = JSON.stringify(body);
  res.writeHead(status, {
    'content-type': 'application/json',
    'content-length': Buffer.byteLength(payload),
  });
  res.end(payload);
}

function readJson(req) {
  return new Promise((resolve, reject) => {
    let raw = '';
    req.setEncoding('utf8');
    req.on('data', (chunk) => {
      raw += chunk;
      if (raw.length > 1_000_000) reject(new Error('Request body too large'));
    });
    req.on('end', () => {
      try {
        resolve(raw ? JSON.parse(raw) : {});
      } catch {
        reject(new Error('Invalid JSON'));
      }
    });
  });
}

function authenticate(db, req) {
  const authorization = req.headers.authorization || '';
  const bearer = authorization.startsWith('Bearer ') ? authorization.slice(7).trim() : '';
  const token = bearer || req.headers['x-api-token'];
  if (!token) return null;
  return db.prepare(
    'SELECT id, email, role, org_id FROM users WHERE api_token = ?',
  ).get(token) || null;
}

function createServer(db) {
  migrate(db);

  return http.createServer(async (req, res) => {
    try {
      const url = new URL(req.url, 'http://localhost');
      if (req.method === 'GET' && url.pathname === '/health') {
        sendJson(res, 200, { ok: true });
        return;
      }

      const user = authenticate(db, req);
      if (!user) {
        sendJson(res, 401, { error: 'Unauthorized' });
        return;
      }

      if (req.method === 'GET' && url.pathname === '/me') {
        sendJson(res, 200, {
          id: user.id,
          email: user.email,
          role: user.role,
          org_id: user.org_id,
        });
        return;
      }

      if (req.method === 'POST' && url.pathname === '/invoices') {
        const body = await readJson(req);
        const number = body.number;
        const customerName = body.customer_name;
        const amountCents = body.amount_cents;
        const status = body.status || 'draft';

        if (
          typeof number !== 'string' ||
          typeof customerName !== 'string' ||
          !Number.isInteger(amountCents) ||
          amountCents < 0 ||
          !['draft', 'sent', 'paid'].includes(status)
        ) {
          sendJson(res, 400, { error: 'Invalid invoice' });
          return;
        }

        try {
          const result = db.prepare(`
            INSERT INTO invoices
              (org_id, number, customer_name, amount_cents, status, created_by)
            VALUES (?, ?, ?, ?, ?, ?)
          `).run(user.org_id, number, customerName, amountCents, status, user.id);
          const invoice = db.prepare(
            'SELECT * FROM invoices WHERE id = ? AND org_id = ?',
          ).get(result.lastInsertRowid, user.org_id);
          sendJson(res, 201, invoice);
        } catch (error) {
          if (String(error.message).includes('UNIQUE')) {
            sendJson(res, 409, { error: 'Invoice number already exists' });
          } else {
            throw error;
          }
        }
        return;
      }

      const getMatch = url.pathname.match(/^\/invoices\/(\d+)$/);
      if (getMatch && req.method === 'GET') {
        const invoice = db.prepare(
          'SELECT * FROM invoices WHERE id = ? AND org_id = ?',
        ).get(Number(getMatch[1]), user.org_id);
        if (!invoice) {
          sendJson(res, 404, { error: 'Invoice not found' });
          return;
        }
        sendJson(res, 200, invoice);
        return;
      }

      const statusMatch = url.pathname.match(/^\/invoices\/(\d+)\/status$/);
      if (statusMatch && req.method === 'PATCH') {
        if (user.role !== 'admin') {
          sendJson(res, 403, { error: 'Forbidden' });
          return;
        }

        const body = await readJson(req);
        if (!['draft', 'sent', 'paid'].includes(body.status)) {
          sendJson(res, 400, { error: 'Invalid status' });
          return;
        }

        const invoice = db.prepare(
          'SELECT * FROM invoices WHERE id = ? AND org_id = ?',
        ).get(Number(statusMatch[1]), user.org_id);
        if (!invoice) {
          sendJson(res, 404, { error: 'Invoice not found' });
          return;
        }

        db.prepare(
          'UPDATE invoices SET status = ? WHERE id = ? AND org_id = ?',
        ).run(body.status, Number(statusMatch[1]), user.org_id);
        sendJson(res, 200, db.prepare(
          'SELECT * FROM invoices WHERE id = ? AND org_id = ?',
        ).get(Number(statusMatch[1]), user.org_id));
        return;
      }

      sendJson(res, 404, { error: 'Not found' });
    } catch (error) {
      sendJson(res, 400, { error: error.message || 'Bad request' });
    }
  });
}

if (require.main === module) {
  const db = openDatabase();
  const server = createServer(db);
  const port = Number(process.env.PORT || 3000);
  server.listen(port, () => {
    console.log(`Ledgerline listening on port ${port}`);
  });
}

module.exports = { createServer };
