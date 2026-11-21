<!-- FILE: bench/00-conventions.md -->
# Shared conventions (all apps)

Stack: TypeScript strict, Node 20, Express, Postgres 16 (docker compose),
Vitest + supertest. Migrations: plain SQL files in db/migrations, applied by
`npm run migrate`. `npm test` runs the suite. `npm run seed` loads seed data.
Auth: bearer tokens from a seeded `users.api_token` column (auth is NOT the
thing under test; do not build login/JWT/sessions).
Money: integer cents only. IDs: bigint identity.
Errors: JSON {error:{code,message}}. 401 no/invalid token, 403 role denied,
404 object not found OR belongs to another org, 400 malformed, 422 invalid.
Layout: src/routes, src/services, src/db, tests/, db/migrations, db/seed.sql.
Rules for the repo Copilot builds: no secrets in code, README with run steps.

# Isolation rules (results are void if broken)
- Oracles, bad-variant recipes and the APP-3 defect list live OUTSIDE every
  repo the agent can read (bench-private/).
- Every run starts from a clean checkout of a tagged fixture commit.
- Task prompts are the only text the agent gets; same text for every arm.