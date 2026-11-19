# Context summary: Batch 2 remainder (backend, database, auth), NIST 800-63 review, OWASP tree

**Architectural reasoning.** This chat sits under the FN-/TB- shapes and the per-FN authorization line. Every FN needs an authorization rule, and every TB needs an access matrix with RLS behavior. Auth had the weakest source in the corpus (wshobson), so this chat's main job was to establish what must be written new and which primary sources can carry it. The dependency order is: primary sources (NIST) → auth reference → per-FN authorization line → authz matrix and wings-lint checks. The Postgres material is the reverse: strong sources, mostly a merge job.

## A. Scope and coverage

| Item | State |
|---|---|
| Batch 2 remainder (wshobson ×4, Addy `code-simplification`, Supabase `security-*`/`schema-*`/`conn-*` rules) | Analyzed in this chat's first turn. Those files are not in my context for this final pass, so the verdicts below are carried from that read and not re-checked. |
| NIST 63B-4 | **Read directly this pass**, §3.1.1 (passwords) in full plus grep hits for the rest. The PDF is a browser print of pages.nist.gov, 112 pp, so cite by section, not page. |
| NIST 63A and 63C (2017) | In context. Cover notices verified: both withdrawn Aug 1, 2025 and superseded in full by the -4 editions. History only. |
| Not read | Old 63b and 63-3 (inventoried only), 63-4, 63A-4, and 63B-4 outside §3.1.1. §3.2.2's numeric throttle limits were not read. |
| OWASP tree | I picked files by tier. **Retraction:** chats 5 and 6 already received and analyzed Tiers 1–5 and 63C-4, so those requests are moot. |

## B. Constraints this chat established (proposals, not decisions)

1. **Auth is written new.** It gets a stack-decision-record item plus a per-FN authorization line (role, ownership predicate, tenant). wings-lint checks the line. Chat 6 adds an auth-recency field.
2. **NIST 63B-4 is the normative anchor for password policy** (§D). The -4 editions are the only NIST versions to cite.
3. **Authentication is separate from authorization.** wshobson's split is worth keeping. Authorization always needs a role plus a mandatory ownership/tenant predicate.
4. **Postgres and Supabase stay optional stack packs**, not core. For the security block I assumed build-time rules plus a review lens pass using Cloudflare's verdict model.
5. **Normative claims get verified against a primary source before they are written down.** My first-turn NIST claim was only half right: the composition rules were the violation, and 12 was wrong against NIST's 15.

## C. Source verdicts

| Source | Take | Drop or fix |
|---|---|---|
| wshobson `postgresql-table-design` | Best pure-Postgres source: rules, gotchas, "types to avoid" table, SKILL/details split | "Most selective columns first" contradicts oma-db's equality-then-range. Example `orders` FK has no `ON DELETE`, against its own rule. RLS section is thin, so use Supabase's. |
| wshobson `api-design-principles` | GraphQL only: payload errors, DataLoader, depth/complexity limits, union errors. REST is covered better by Addy. | Pydantic v2 treats `_links` as private, so the HATEOAS example won't serialize. `@include(if: $isOwner)` looks like authz but is client-controlled. Rate limiter is an in-memory dict, which breaks the stateless rule. Template ships `allow_origins=["*"]`, a fail-open default. Envelopes carry `timestamp` and `path`. |
| wshobson `architecture-patterns` | Dependency rule in one sentence, troubleshooting symptoms (framework decorators in entities, use case importing an adapter), in-memory adapters for tests | `place_order` charges the card before saving, with no compensation or idempotency. `create_user` is check-then-save, a race. `pydeps` only draws a graph, so enforce with import-linter or tsarch so CI fails. |
| wshobson `auth-implementation-patterns` | Authn vs authz split, strategy comparison | See §E. |
| Addy `code-simplification` | Chesterton's Fence, scope to what changed, separate refactor from feature, unmodified tests as the red flag. Fits between Build and Review. | First TS example removes `async` and claims unchanged behavior. A sync throw then escapes instead of becoming a rejection, which breaks its own principle 1. |
| Supabase rules | Atomic format (title, impact, incorrect/correct, reference). RLS rules. `security definer` in a private schema plus `revoke execute`. FK-index rule. | `_contributing.md` mandates quantified impact, so rules carry unsourced numbers ("100-1000x faster"). Use qualitative tiers. `security-rls-basics` uses plain `set app.current_user_id`, which leaks across pooled connections. `set_config(..., true)` inside a transaction is correct. `schema-constraints` checks `pg_constraint` by name only in two of three examples, so it can match another table's constraint. `conn-limits` says 5 MB per connection, `conn-pooling` says 1–3 MB. |

## D. NIST 63B-4 facts, verified in text (§3.1.1.1–3.1.1.2)

- Single-factor password: minimum **15** characters. Password used only inside MFA: minimum **8** (SHALL).
- Verifiers SHOULD permit a maximum of at least **64** characters. SHOULD accept all printing ASCII, space and Unicode, with each code point counted as one character.
- **No other composition rules** (SHALL NOT). **No periodic rotation** (SHALL NOT), but a forced change on evidence of compromise (SHALL).
- No stored hints reachable by an unauthenticated claimant. No KBA or security questions when choosing passwords.
- Verify the **entire** password and **do not truncate** (SHALL). NFC-normalize before hashing (SHOULD).
- Blocklist (SHALL): compare the entire password against breached, common and context-specific values (service name, username). Rejection must give the reason. Guidance must be offered.
- Rate limiting is mandatory (§3.2.2). Password managers and autofill must be allowed, and paste is permitted (SHOULD).
- NIST notes that passwords are not phishing-resistant.
- Copyright text ("not subject to copyright in the US, attribution appreciated") is verified only in the old 63A and 63C. 63B-4's front matter was not checked.

**Inference, not NIST text:** bcrypt silently truncates at 72 bytes, which conflicts with "do not truncate" for long or multibyte input. So Argon2id by default, and bcrypt only with an enforced byte cap that rejects instead of truncating. Chat 5 carries OWASP's Argon2id minimum (m=19456, t=2, p=1), which I haven't seen myself.

## E. Defects in wshobson `auth-implementation-patterns` (read in first turn)

- Refresh flow has no rotation and no reuse detection. It looks tokens up by `hash(token)`, which only works if the hash is deterministic. With bcrypt it fails, and the file never says which.
- `jwt.verify` pins no algorithm, issuer or audience.
- Login sets `req.session.userId` with no regenerate (session fixation).
- Login short-circuits on unknown user (timing leak). Register returns "Email already registered" (enumeration).
- Google callback has no `state`, no `email_verified` check and no linking policy, which is the account-takeover setup.
- `requireOwnership` is followed by `db.posts.update(req.params.id, req.body)`, so a client can overwrite `userId`.
- Recommends httpOnly cookies with no CSRF discussion.
- Password policy is 12 characters plus composition rules, and bcrypt's 72-byte limit is never handled.
- Gaps: SSO and multi-tenancy are listed in "when to use" but not covered. Password reset, email verification, MFA and passkeys are missing.

## F. Conflict-table changes this chat made (proposals)

| Topic | Rule |
|---|---|
| PK type (revised) | Default `bigint generated always as identity`. UUIDv7 only for IDs that are exposed or distributed. ID type doesn't stop enumeration, authorization does. Supersedes chat 3's "UUIDv7 on PG18+". |
| Composite index order | Equality columns first, then range or sort. Reject "most selective first" wherever it appears (alirezarezvani `database-designer`, wshobson). |
| Error envelope | Addy's `{error:{code,message,details}}` plus `requestId`, no `timestamp` or `path`. Chat 5 refines this to RFC 9457 problem+json. |
| Pagination | Cursor/keyset by default. |
| Impact claims in rules | Qualitative tiers unless sourced. |

## G. wings-lint and reference-content additions from this chat

1. FN authorization line: role, ownership predicate, tenant, plus a CSRF note when it uses cookie auth.
2. Pattern scans: request body passed straight to an update (mass assignment), `jwt.verify` without pinned alg/iss/aud, and plain `set` for tenant context where `set_config(..., true)` or `SET LOCAL` is required.
3. SQL checks: FK without `ON DELETE`, FK without an index, `security definer` outside a private schema or without `revoke execute`, `TO authenticated` without an ownership predicate (BOLA), `user_metadata` in a policy, and money columns typed float/real.
4. Password-policy conformance for generated validators: reject composition rules, enforce the 15/8 minimums, no truncation, and a byte cap for bcrypt.
5. Auth checklist for the new reference: session regeneration on login, refresh-token rotation with reuse detection, `state` plus `email_verified` plus explicit linking policy on OAuth callbacks, uniform login timing, and generic registration responses.
6. Layer rule enforced by a failing CI check (import-linter, tsarch or dependency-cruiser), not a diagram.
7. Advisory: check-then-act without a unique constraint, and payment FNs without an idempotency key or a persist-before-charge ordering.

## H. Cross-chat reconciliation for the master chat

- **License.** My last-turn OWASP flag is superseded. The CC BY-SA ruling in chat 8 says adapt it as separate credited files with a change notice. NIST is reusable with attribution.
- **Error envelope.** Chat 4 (this chat) says bare Addy envelope, chat 5 says RFC 9457 with `code` and `requestId` as extension members. 9457's `instance` member is path-like, so decide whether "no path" still holds.
- **Password minimum.** Chat 6 flagged Django's `min_length: 8` against NIST's 15 for single-factor, and chat 7 flagged composition rules in senior-frontend's Zod example. A house default of 15 regardless of MFA would settle both. That is the master's call.
- **Rule atom.** This chat has title/impact/incorrect/correct/reference. Chats 7 and 9 add `applies_to`, `status`, `verified_at` and `source`. Merge into one format.
- **Unsourced numbers.** Supabase (this chat), Vercel (chat 9) and oma perf (chat 7) all carry them. One house rule covers all.
- **`$1` placeholders.** Chat 9 found hosts substitute `$N` in skill text, which hits this chat's SQL examples and the SQL rules generally. The packaging lint needs a literal-context exemption.
- **Layer enforcement tooling.** This chat names import-linter and tsarch. Chat 8 has mattpocock's dependency-cruiser config (TS-only, five rules against four documented). Pick per stack pack.
- **Phase slot.** `code-simplification` has no slot in chat 2's spine. Proposal: Build → Simplify → Review. ponytail's "never add layers" (chat 8) conflicts with wshobson's hexagonal layering. The "layered by default, DDD only on trigger" rule covers it.
- **Money type.** ECC `contract-first` (chat 9) used float for money, which supports "never float".

## I. Unverified, do not carry forward

- Every Batch 2 defect above rests on my first-turn read. The files aren't in this context to re-check.
- The 63B-4 throttle numbers (§3.2.2), anything in 63B-4 outside §3.1.1, and 63B-4's copyright notice.
- The bcrypt/truncation conclusion and the Argon2id parameters (inference and secondhand, respectively).
- PG18 `uuidv7()` availability (as far as I know, unverified).

---

# Do I need more files?

I checked the other chats first. Nothing is blocking for this chat's scope.

**Already covered elsewhere, so I withdraw my last-turn requests:** OWASP Tiers 1–5, 63C-4 and the OWASP LICENSE (chats 5, 6, 8). Other open gaps belong to other chats: BMAD stubs, OpenSpec and design.md (chat 2), mattpocock's remaining skills, taste assets, oma-mobile variants and Vercel agent-skills (chat 8), and the wshobson adapters and GateGuard helpers (chat 9).

**Optional, in order of value:**
1. **Primary-source pages for claims that currently rest on secondary sources:** PostgreSQL docs on multicolumn indexes (equality-then-range), Row Security Policies and CREATE POLICY (BYPASSRLS/FORCE), `set_config` and `SET LOCAL`, identity columns, and `uuidv7()`. I can fetch these myself if you allow it. Otherwise skip, and the master treats them as secondhand.
2. **RFC 9457 and RFC 9106.** These are primary sources for the error envelope and the Argon2id default. Same arrangement.
3. **Chat 3's optional Trail of Bits plugins** (entry-point-analyzer, spec-to-code-compliance, mutation-testing, property-based-testing). I can't tell from project knowledge whether they were sent. They would only feed surface closure, the AC-to-check lint and the test value bar, so skip them unless the master wants them.
4. **Supabase `advanced-*`, `data-*` and `monitor-*` rules.** Defer until the Supabase pack is drafted.

**Not fixable by files:** the PG-/FN-/TB- requirement shapes and the stack decision record have no upstream source. They get written new in the master chat. No additional upload would improve that.