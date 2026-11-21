<!-- FILE: bench/app2-shopkeep/COPILOT-BUILD-PROMPT.md -->
Build the repository in SPEC.md with 00-conventions.md. Fixture only: no
discount logic, no extra endpoints. Write >= 30 meaningful tests: each must
assert on observable behavior (status codes, response bodies, DB state).
No assertion-free tests, no toBeDefined/toBeTruthy on non-booleans, no
mocking of the code under test; only the database is real. Include the
cancel test named exactly as in SPEC.md. Run `npm test`, put the real
test count in the README. I will tag it v1 and create the task branches.