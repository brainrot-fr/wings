# Context summary: NIST 800-63B-4 password rules, OWASP Tiers 1-3 and meta files

**Architectural reasoning.** This chat sits under the per-FN authorization line and the build-time security rules. The dependency order is: NIST password policy (primary source) → Tier 1 (authn, sessions, authz) → Tier 2 (authz matrix and regression testing) → Tier 3 (per-FN build rules and review lenses) → reviewer-agent contract shape. Tier 2 is the bridge to tooling, because it makes the authorization line checkable by `wings-lint`. OWASP is hub-and-spoke by design (one topic per sheet, no restating), so wings has to flatten the scattered rules into one rule per home. That matches the single-owner discipline from the spine (chat 2).

## A. Coverage

| Item | State |
|---|---|
| Tier 1 (15 sheets), Tier 2 (6), Tier 3 (20), `AGENTS.md`, `CLAUDE.md`, `GUIDELINE.md`, 5 reviewer agents | Read in this chat. **The files are not in my context for this final pass, so every verdict and defect below is carried from that read, not re-checked.** |
| `Access_Control_Cheat_Sheet.md` | Deprecation stub pointing to Authorization. |
| NIST 63B-4 | Confirmed the password claims against the PDF (see §D). Chat 3 read §3.1.1 in full. §5 (sessions) and §3.2.2 (throttling) are still unread by anyone. |
| NIST 63A/63C (2017) | Withdrawn Aug 1, 2025 and superseded. History only. |
| Not read | `.claude/commands/review-cheatsheet-pr.md` (not needed), ASVS, Prototype_Pollution, RFCs. |

## B. Constraints this chat established (proposals, not decisions)

1. **Flatten OWASP into one rule per home.** No restating across sheets.
2. **Every FN has an authorization line**: role, ownership predicate, tenant, allowed denial codes, and a CSRF note when it uses cookie auth. Chat 4 adds an auth-recency field.
3. **Role plus a mandatory ownership/tenant predicate.** A policy engine only past stated triggers.
4. **Tenant context is transaction-local** (`SET LOCAL` or `set_config(..., true)`). Request roles must be neither superuser nor `BYPASSRLS`.
5. **Authorization matrix generated from FN lines**, with body assertions, not status alone.
6. **List, count, export and search share one predicate.**
7. **Fail closed when no authorization decision exists.**
8. **Legacy sheets give principles only, never snippets.**

## C. Source verdicts

| Source | Take | Drop or fix |
|---|---|---|
| Session_Management | Server-side store, token hashing with verifier split, `__Host-` cookies, explicit SameSite, regenerate on privilege change, logout revokes all IDs, no tokens in localStorage | Says 64-bit entropy and also 128-bit. Timeout ranges are unsourced. |
| Authentication, Credential_Stuffing | MFA first, generic errors with uniform timing, breached-password check, no security questions | "2-3 lockouts, then permanent lockout" is a DoS vector and contradicts Denial_of_Service. "Require unpredictable usernames" contradicts Authentication. Fingerprinting libraries are dated. |
| Forgot_Password, MFA, Passkey | Single-use hashed tokens, TOTP seed encrypted with replay rejection, UV verified server-side, recovery is the weakest link | Forgot_Password allows security questions. The other sheets forbid them. |
| JWT, OAuth2 | Pin alg, require `iss`/`aud`/`exp`, `typ`, key anchoring, Auth Code + PKCE only, rotation | JWT is for service tokens and OIDC. First-party web uses sessions. |
| CSRF | Framework built-in first, Fetch Metadata plus Origin fallback, signed double-submit | Naive double-submit. CSRF only applies with ambient credentials. |
| Authorization, IDOR, Mass_Assignment | Deny by default, scoped lookup, DTO allowlist | 2021 data, invalid Mongoose snippet, dead-link-era examples. Take the DTO principle only. |
| Multi_Tenant | Verified membership, transaction-local context, schema-derived RLS inventory, exact tenant-prefix storage deletion | Undefined names, offset pagination in examples. |
| Authorization_Regression_Testing | Best `wings-lint` source: YAML matrix, multi-user replay, role demotion, cross-tenant test, CI gate | Fixture hardcodes 403 while its pattern allows 404. Mixes role and tenant in `denied_roles`. The 401/403-volume monitor is noise. |
| Authorization_Testing_Automation | Matrix as source of truth, one test per point of view, failure message names service, role and expectation | Stale XML/JAXB stack. Substitutes `{messageId}`=1 for every role, so it cannot test ownership. Status-only assertions miss data leakage. |
| Authorization_Patterns, Policy_And_Data_Distribution, Decisions_And_Output_Handling | Fail closed, same predicate everywhere, intersect predicates with AND | Policy distribution is PDP/OPA infrastructure, so it becomes an optional pack. |
| Business_Logic_Security | Top requirements source: written invariants, atomic check-then-act, state machines, abuse controls, concurrency tests | Merge its idempotency section with Addy's, which is stronger. |
| Input_Validation, SQL_Injection_Prevention | Allowlists, size limits before parsing, JSON Schema `required`/`additionalProperties`, parameterize values, allowlist identifiers | Query_Parameterization has Rails 3 APIs, a PHP example that never executes, and `?` placeholders for SQLx (Postgres uses `$n`). Injection_Prevention is hub plus filler. |
| XSS, CSP | Context encoding, DOMPurify, safe sinks, Trusted Types, strict nonce CSP | XSS cites rules that don't exist. CSP generates nonces with `uuid.v4()`. |
| HTTP_Headers | `nosniff`, frame-ancestors, Referrer-Policy, nginx `add_header` inheritance gotcha | HSTS string includes `preload`. COOP/COEP/CORP defaults break OAuth popups and CDN assets, so wings makes them opt-in. |
| REST_Security | Method allowlist, content-type checks, out-of-order execution | Opens with HATEOAS. The status table lacks 409/422. Permissions-Policy names need verifying. |
| GraphQL | Per-field and per-edge authorization, `node(id)` bypass, depth/cost/batch limits | Alphanumeric-only input conflicts with Input_Validation. Introspection guidance contradicts itself. Links the deprecated stub. |
| Webhook_Security | Raw-body HMAC, constant-time compare, 5-minute tolerance, dedupe cache ≥2x that, connect-time IP check, CSRF exemption only with signature | Stripe-specific figures need re-verification. |
| SSRF | Connect-time IP validation, redirects off, IPv4-mapped and NAT64 normalization, parser disagreement | Monitoring script is invalid Python. Deny-list omits `100.64.0.0/10`. Wings uses "allow only globally reachable addresses". |
| Unvalidated_Redirects | ID-to-URL mapping, parsed-URL allowlist, reject userinfo | 2010-era. No `returnUrl` or OAuth `redirect_uri` coverage. |
| File_Upload | Allowlist, generated filenames, outside webroot, re-encode images, NTFS ADS and 8.3 names | No SVG mention. No presigned-URL or separate-origin pattern. |
| Error_Handling, Logging | Generic 5xx, server-side logging, event list, exclusions, log injection | Body cites RFC 7807 while its references cite 9457 (which obsoletes it). Logging is SIEM-oriented and over-long. |
| Secrets_Management, Cryptographic_Storage | Lifecycle, incident order, AES-GCM, CSPRNG table, DEK/KEK | Secrets discourages env vars, which PaaS stacks use. Drop Kubernetes sidecars, HSM and memory zeroing. |
| Denial_of_Service, Email_Validation | ReDoS, request-size limits, feature-level rate limits. Email: store original plus canonical form, verify before activation, email change flow | Placeholder `[Future additions...]` sections and anecdotes. |
| Meta (AGENTS.md, GUIDELINE.md, 5 reviewers) | Fixed-format reviewer output (verdict, severity, evidence, fix), claim-vs-source lens, "good over best", one topic per home | The maintainers say these sheets are AI-assisted and re-audited. Treat every line as unverified. |

Maintenance quality is uneven. Recently rewritten sheets carry pinned citations (Session, Passkey, Multi_Tenant, JWT, Webhook, Password_Storage, Business_Logic). The 2010-era sheets are Error_Handling, Injection_Prevention, Query_Parameterization, Unvalidated_Redirects, Mass_Assignment and Denial_of_Service.

## D. Facts settled in this chat

- **Passwords (NIST 63B-4, verified in chat 3 §3.1.1).** At least 15 characters single-factor, at least 8 inside MFA, a maximum of at least 64, no composition rules, no periodic rotation, a breached/common/context-specific blocklist, no truncation, and NFC normalization.
- **Argon2id by default** (OWASP minimum m=19456, t=2, p=1, which I have not verified against RFC 9106). bcrypt is legacy-only with a 72-byte cap. The truncation conflict is real only for multibyte input, since 72 bytes is at least 64 ASCII characters.
- **Pooled-connection tenant leak** is confirmed by Multi_Tenant. Supabase's plain `set` is wrong.
- **IDOR:** authorization, not ID type, stops enumeration.
- **OAuth linking:** key on `iss`+`sub` and never link by email alone. `email_verified` is a wings-original rule, because neither OWASP nor 63C-4 mentions it. Chat 4 corrected my claim that NIST says "never auto-link". That is my inference from 63C-4 §3.8.2.

## E. Mechanisms worth carrying

1. **Matrix as source of truth.** The YAML matrix is generated from FN lines, with one test per role and ownership perspective, and failure messages that name the service, role and expectation.
2. **Required cells.** Every ownership-scoped FN needs cross-user and cross-tenant cells, and role-demotion replay is part of the regression set.
3. **Denial codes.** 401 unauthenticated, 403 function-level role denial, 404 for another owner's object. The matrix models an allowed set of codes.
4. **Reviewer output** is fixed-format: verdict, severity, evidence, fix. This matches the findings-carry-their-fix idea in chat 9.
5. **Claim-vs-source lens** as a review pass over any rule text wings ingests.

## F. House rules proposed (nothing decided)

| Topic | Proposal |
|---|---|
| 403 vs 404 | As in §E.3 |
| Token storage at rest | Random tokens of at least 128 bits use SHA-256. Passwords use Argon2id. |
| Lockout | Per-account and per-IP throttle with escalating delay, no permanent lockout, recovery stays available |
| Security questions | Never |
| Nonces and tokens | CSPRNG, at least 128 bits. Never `uuid.v4()` or `Math.random`. |
| Env vars | Fine on managed platforms via the platform secret store. Never in images, `ARG`/`ENV` or client bundles. The client-bundle rule has no upstream source. |
| Unicode input | Input_Validation wins over GraphQL's alphanumeric advice |
| HTTP headers | COOP/COEP/CORP and HSTS `preload` are opt-in |
| Error envelope | Addy's `{error:{code,message,details}}` plus `requestId`, serialized as RFC 9457 problem+json with `code` and `requestId` as extension members. **Not confirmed by you.** |

## G. wings-lint additions from this chat

1. Every FN has an authorization line, plus a CSRF note for cookie auth.
2. Generate the YAML matrix from FN lines, with cross-user, cross-tenant and body-assertion cells.
3. List, count and export FNs share one predicate.
4. Every tenant-scoped TB appears in a schema-derived RLS inventory, and a test asserts the request role is neither superuser nor `BYPASSRLS`.
5. Webhook FNs declare signature, timestamp tolerance and dedupe.
6. Pattern scans: `jwt.verify` without pinned alg/`iss`/`aud`, `uuid`/`Math.random` for tokens, `redirect(req.query…)`, fail-open secret defaults.

## H. Cross-chat reconciliation for the master chat

- **License (superseded).** I treated OWASP as idea-only here. Chats 6 and 8 settled it: OWASP is CC BY-SA 4.0 and adaptable. ShareAlike still applies, so keep OWASP-derived text in **separate credited files with a change notice**. NIST text is reusable with attribution, verified for 63C-4 in chat 4.
- **Error envelope.** Chat 3 says bare Addy, and this chat refines it to RFC 9457. The 9457 `instance` member is path-like, so decide whether "no path" still holds.
- **Password minimum.** Chat 3 flagged Django's `min_length: 8` and senior-frontend's Zod composition rules (chat 7). A house default of 15 regardless of MFA settles both.
- **Session timeouts.** The Session sheet's ranges are unsourced and chat 4 retracted the 63C-4 5-minute substitute (that applies only to the authorization code). NIST 63B-4 §5 would be the primary source, and nobody has read it.
- **Lockout vs throttling.** 63B-4 §3.2.2 is the unread primary source for the no-permanent-lockout rule.
- **Test independence.** Chat 4's proposal (security tests generated from FN lines by script, not by the code-writing step) is exactly what the generated matrix delivers. It carries into mattpocock's "seams in the ticket" (chat 8).
- **Next.js and Supabase packs.** They overlap this chat's CSRF, headers, RLS and tenant rules. One owner per fact.
- **SameSite.** ECC `security-review` (chat 9) says `SameSite=Strict` on all cookies, which breaks login after cross-site navigation. This chat's rule is explicit SameSite plus `__Host-`.
- **Env-var secrets.** ECC `security-review` conflicts with the platform-secret-store rule here.
- **Role-only authorization.** Appears in ECC `security-review`, FastAPI's `is_admin` (chat 4) and the wshobson examples. The mandatory ownership predicate answers all of them.
- **`$n` and `$1` placeholders.** Query_Parameterization and SQL rules use them, and chat 9 found hosts substitute `$N` in skill text, so the packaging lint needs a literal-context exemption.
- **Idempotency.** Merge Business_Logic with Addy's recipe (chat 3), with Addy's as the base.
- **New IDs.** `TH-n` and `AB-n` (chat 4) fit the linter pattern. A matrix cell ID scheme must fit it too, and ECC's `TEST-ORDER-001` shape does not.
- **Rule atom.** Findings in the rule format need `applies_to`, `status`, `verified_at` and `source` (chats 7 and 9). OWASP's pinned citations are the right input for `source`.
- **Severity and result states.** Review findings use P0-P3 plus confidence, and one of the seven result vocabularies from chat 9.

## I. Unverified, do not carry forward

- Every Tier 1-3 and meta verdict and defect above (carried, not re-checked).
- ASVS 6.4.2, which several sheets cite and I never saw.
- Argon2id parameters, the 5-minute webhook tolerance and the Stripe-specific figures.
- Permissions-Policy directive names.
- 63B-4 outside §3.1.1 (including its copyright notice and §3.2.2 limits).
- All timeout and entropy ranges in Session_Management.

---

# Do I need more files?

I checked the other chats first. Tier 4-5, 63C-4 and the OWASP LICENSE are already covered (chats 4 and 6, and your CC BY-SA ruling). The BMAD stub renders, OpenSpec, `design.md`, mattpocock's remaining skills, taste assets and the GateGuard helpers belong to other chats, so I'm not duplicating those.

**Worth sending for this chat, in priority order:**
1. **NIST 63B-4 §5 (session management) and §3.2.2 (throttling).** This is the highest-value item. Three of this chat's open rules (session timeouts, throttling, no permanent lockout) lack a primary source. Chats 3 and 4 both flagged it and nobody owns it. Re-upload the PDF, or confirm the master chat has it.
2. **OWASP ASVS** (chats 3, 4 and 5 asked too, so send it once). It's a numbered requirement catalogue, close to the shape of wings' `R-` security items. It would also verify the ASVS 6.4.2 citation these sheets rely on.
3. **Primary sources for secondhand numbers.** RFC 9106 (Argon2id), RFC 9457 (error envelope), RFC 9700 and 7636 (OAuth/PKCE). I can fetch these myself if you allow it.
4. **Any CORS or Clickjacking sheet in the OWASP tree.** Tiers 1-3 had no CORS coverage, and the wshobson template shipped `allow_origins=["*"]` (chat 4). I can't tell from the tree whether a sheet exists, so check and send it if so.

**Not needed:**
- Tier 1-3 again, unless the master chat will quote them. My verdicts rest on a read I can't re-check now.
- The `review-cheatsheet-pr.md` command.
- OWASP `LICENSE.md` (settled).
- More 63C-4 or 63A-4/63-4.

**Not fixable by files:** the FN authorization-line shape, the TB access-matrix shape and the stack decision record have no upstream source. They get written new in the master chat.