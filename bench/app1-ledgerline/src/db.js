const fs = require('node:fs');
const path = require('node:path');
const Database = require('better-sqlite3');

const appRoot = path.resolve(__dirname, '..');

function openDatabase(dbPath) {
  const resolved = dbPath || process.env.LEDGERLINE_DB || path.join(appRoot, 'db', 'ledgerline.sqlite');
  fs.mkdirSync(path.dirname(resolved), { recursive: true });
  const db = new Database(resolved);
  db.pragma('foreign_keys = ON');
  return db;
}

function migrate(db) {
  const migration = fs.readFileSync(
    path.join(appRoot, 'db', 'migrations', '001_init.sql'),
    'utf8',
  );
  db.exec(migration);
}

function seed(db) {
  const sql = fs.readFileSync(path.join(appRoot, 'db', 'seed.sql'), 'utf8');
  db.exec(sql);
}

module.exports = { appRoot, openDatabase, migrate, seed };
