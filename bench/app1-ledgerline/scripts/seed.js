const { openDatabase, migrate, seed } = require('../src/db');

const db = openDatabase();
migrate(db);
seed(db);
console.log('Seed complete');
db.close();
