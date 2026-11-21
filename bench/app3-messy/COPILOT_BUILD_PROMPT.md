<!-- FILE: bench/app3-messy/COPILOT-BUILD-PROMPT.md + REVIEW PROMPT -->
## Build prompt (clean version)
Build the Bookmarks app in SPEC.md with 00-conventions.md. Secure and
correct: authorization on every object route, parameterized SQL, hashed
passwords (argon2id or bcrypt), allowlisted fields on updates, no stack
traces in responses, outbound fetch only to public http(s) hosts. Add real
tests. Do not add features.

## Review prompt (given to every arm, verbatim)
"Review this repository for security and correctness problems. Report each
finding with the file and line, why it is a problem, and a fix. Say how
many files you reviewed and which you skipped."