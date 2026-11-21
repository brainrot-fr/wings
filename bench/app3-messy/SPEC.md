<!-- FILE: bench/app3-messy/SPEC.md -->
# APP-3 Bookmarks (audit target: planted defects, no tests of substance)

Purpose: code-review precision and recall. NOT a wings-build task.

App: users(id, email, password_hash, is_admin, api_token), bookmarks(id,
user_id, url, title, created_at). Endpoints: POST /register, GET /bookmarks
(own), POST /bookmarks, DELETE /bookmarks/:id, GET /bookmarks/search?q=,
PATCH /users/:id, POST /bookmarks/:id/fetch-title (server fetches the URL),
GET /admin/users. Same stack and conventions.

Build order: (1) Copilot builds a CLEAN version from this spec and
tests, you review it and tag clean-v1. (2) YOU apply the defect patches from
bench-private/app3-defects.md by hand on a branch `messy`. Do not let
Copilot plant defects: it will "fix" them or leave tells.
Review input for the agent: branch `messy`, prompt below.