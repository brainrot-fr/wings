const { openDatabase, migrate } = require('../src/db');

const db = openDatabase();
migrate(db);
console.log('Migrations complete');
db.close();
