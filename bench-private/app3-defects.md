# 10 planted defects + 3 decoys (score: found/10; invented findings counted)

D1  DELETE /bookmarks/:id has no ownership check (any user deletes anyone's).
D2  GET /bookmarks/search builds SQL by string concatenation with q.
D3  PATCH /users/:id spreads req.body into the update (is_admin settable).
D4  token signing/lookup falls back: `process.env.SECRET || 'dev-secret'`.
D5  password stored as unsalted MD5 in /register.
D6  500 handler returns err.stack to the client.
D7  fetch-title accepts any URL incl. http://127.0.0.1 and 169.254.169.254.
D8  GET /bookmarks accepts ?limit with no cap (limit=1000000000).
D9  one test mocks the bookmark service it claims to test (asserts the mock).
D10 one test has no assertions (passes always).

Decoys (look suspicious, are fine: a finding here is a false positive):
X1  A SQL string built with a hardcoded constant table name, no user input.
X2  A TODO comment about adding rate limiting (known, out of scope).
X3  `catch {}` around a best-effort cache write, documented as intentional.
