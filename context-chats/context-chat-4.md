Before I finalize, I'm closing two items I flagged as open: the 63C-4 copyright notice and §6 (federation threats).

Closed both items. 63C-4's front matter states the text is not subject to copyright in the US, with attribution appreciated by NIST. §6 is a threat table plus a mitigation table, and it holds one trap: Table 4's cross-references use the old section numbering. For example, it cites "3.12.4", which doesn't exist, and "3.12.1" for the assertion identifier, which is actually §3.13.1.

Nothing was saved to memory.

# Context summary: NIST 800-63C-4, OWASP Tiers 4–5, linked sheets, wings as its own attack surface

**Architectural reasoning.** This chat sits at the end of the auth/security chain. Chat 3 settled passwords (63B-4) and the per-FN authorization line. Chat 5 settled authz, sessions and build-time rules. This chat adds three things on top: (1) the federation layer, which governs the login-callback FN, (2) the process and review layer (threat model, review contract, AI-agent risks), and (3) stack packs. The dependency order is: primary source (63C-4) → login-callback checklist → per-FN authorization line (with auth recency) → review lenses → stack packs. Packs sit last because they rot fastest. The unplanned finding is that wings is an AI agent writing code, so Tier 4's AI sheets apply to wings' own workflow, not only to the apps it ships.

## A. Coverage

| Item | State |
|---|---|
| NIST 63C-4 | **Read directly this chat:** §2 (FAL), §3.4 (identifiers), §3.8–3.9 (accounts, linking, resolution, sessions), §3.11 (security controls, injection), §3.13 (assertion protection), §4.7 (reauthentication), §4.9–4.11 (assertion contents, requests, presentation), §6 (threats). Copyright notice verified. |
| 63C-4 not read | §3.5–3.6 (trust agreements, key rotation), §3.12 (attributes, identity APIs), §3.14–3.17 beyond the opening lines, §4.1–4.6, §4.8, §5 (wallets), §7–8, §9 (examples, including the FAL-to-protocol mapping). |
| OWASP Tier 4 (8 files), Tier 5 (12 files), Key_Management, NoSQL_Security, DOM_based_XSS | Analyzed earlier in this chat. **The files are not in my context for this final pass, so every verdict and defect in §C and §E is carried from that read and not re-checked.** |
| Not in this chat | 63B-4 beyond what chat 3 read, 63-4, 63A-4, OWASP Prototype_Pollution (JS sheet defers to it), ASVS, RFCs. |

## B. Constraints this chat established (proposals, nothing decided)

1. **Federation is a core concern, not a pack.** Login via OAuth/OIDC is common enough that the callback FN gets a fixed checklist (§D).
2. **FAL2 behaviours are the core default** (RP-initiated, single audience, injection protection, pre-established trust). FAL3 stays a regulated-stakes pack.
3. **Auth Code + PKCE only.** No front-channel token return. 63C-4 §4.11.2 gives the normative rationale.
4. **The per-FN authorization line gains an auth-recency field** (for step-up), from §4.7.
5. **Email-based account linking:** never auto-link. Link only from an authenticated session that proves control of the existing account. `email_verified` is wings-original, because neither 63C-4 nor OWASP's Authentication sheet mentions it.
6. **Wings is its own attack surface.** The rules in §F apply to the build process itself.
7. **Stack packs carry pinned versions, `verified_at`, and a "re-verify against current docs" line.** Core stays stack-neutral.
8. **Cite CWE or category names, never Top 10 numbers** (the sheets mix 2021 and 2025).

## C. Source verdicts

### NIST 63C-4 (read directly)

| Section | Take | Drop or fix |
|---|---|---|
| §3.4, §4.9 | Federated identifier = issuer + subject, never subject alone. | Federated-identifier ceremony beyond that. |
| §3.8–3.8.2 | SHALL require an authenticated session for all linking. SHOULD authenticate with an existing identifier first. Removal revokes access. Notify on add and on non-terminal remove. Account resolution must resolve uniquely and never attach data to a non-belonging identifier. | NIST doesn't say "never auto-link on email". That is wings' inference from §3.8.2. |
| §3.9 | Five conditions before a session is created. | None. Reads as a callback checklist. |
| §4.9 | Seven RP validation checks, plus the seven mandatory assertion attributes. | IAL/AAL/FAL trust-agreement checks matter only if the stack record sets assurance levels. |
| §4.10 | RP request SHALL carry an RP identifier and a nonce. | None. |
| §4.11.1 | Reference single-use, single-RP, unguessable, SHOULD be ≤5 min, RP authenticates on redemption, IdP checks redeemer is the requester. | None. |
| §4.11.2 | Front channel discouraged. Redirect-based presentation must encrypt personal data. | None. |
| §4.7 | Assertion validity ≠ session lifetime. Identity-API availability must not extend a session. IdP reports last-authentication time. RP may request fresh authentication. | None. |
| §6 | Threat list (manufacture, disclosure, redirect, reuse, substitution, stale attributes) as review-lens headings. | **Table 4's normative cross-references use stale section numbers.** Cite body sections, not Table 4. |

### OWASP Tier 4 (idea-only at the time, see §H for the license change)

| Source | Take | Drop or fix |
|---|---|---|
| Secure_Coding_with_AI | Hallucinated dependencies, out-of-scope edits, test fabrication and deletion, rules-file persistence, invisible-Unicode injection, human accountability | 30-day package-age figure unsourced. ".gitignore doesn't stop AI tools" is tool-dependent. CVE-2026-39313 unverified. |
| AI_Agent_Security | Tool authorization outside the model. Approval bound to the exact action and consumed atomically. Fail closed on unknown tools. Abuse-case matrix. | Broken Python (missing `re` import and `Optional`, deprecated pydantic v1 `validator`). The "checksum" is a concatenated hash truncated to 64 bits. All thresholds arbitrary. |
| LLM_Prompt_Injection_Prevention | Filtering is not a boundary. Five-point pipeline. Smoke-test grading with observables, counts not rates, "no violation observed" ≠ "blocked". | The "NEVER…" system prompt and typoglycemia matcher contradict its own thesis. Statistics and arXiv IDs unverified. |
| MCP_Security | Pin the whole tool definition. Annotations are hints. Audience-validate tokens, never pass through. Validate Origin. stdio is not a sandbox. | x402 section. Spec revision date unverified. Loads only when the app builds or consumes MCP. |
| Secure_Code_Review | Baseline vs diff review. Finding template remapped to FN/TB/PG, P0–P3, confidence, verdict. | Duplicated checklists. "Lockout mechanisms". Assignee, due date, metrics. |
| Threat_Modeling | Four questions, STRIDE per trust boundary, mitigate/eliminate/transfer/accept register. | Technique-comparison ceremony, advocacy essays. |
| Abuse_Case | IDs tied to a feature and a test. Business risk separate from CVSS. | Self-archived. Five-role workshop doesn't fit a solo user. |
| Secure_Product_Design | Five prompts (Context, Components, Connections, Code, Configuration), mappable to the stakes ladder. | Mostly generic. "Golden Path" and "Product Security Levels" are never defined. |

### OWASP Tier 5 (stack packs)

| Source | Take | Drop or fix |
|---|---|---|
| Nextjs_Security | Best stack source. Entry-point classification. Server Actions are public POST endpoints. Return DTOs. Cache keys carry the audience. Test by calling entry points directly. | Version claims (`proxy.ts` in Next 16, `use cache`, `updateTag`) need re-verification. |
| Backend_as_a_Service (draft) | Credential classes by holder. Inventory every surface. Privileged credentials bypass policy. Six-column request-path inventory. | Draft. Verify provider claims at use. |
| GitHub_Actions_Security | `permissions: {}`, SHA pins, avoid `pull_request_target`, env-var passthrough, OIDC, `persist-credentials: false`. | Unverified post-mortem links. |
| NPM_Security | `npm ci`, `--ignore-scripts` plus allowlist, `files` allowlist, scoped registries, slopsquatting, README examples are untrusted. | Unverified token and download claims. |
| Docker_Security | Non-root, `--cap-drop all`, no-new-privileges, read-only fs, no `docker.sock`, bind ports to `127.0.0.1`, BuildKit secrets. | Alpine example uses Debian commands. `//` typo. |
| JavaScript_and_TypeScript | `eval`, prototype pollution, `postMessage`, types are erased so validate at the boundary. | Defers to Prototype_Pollution (not sent). |
| FastAPI_Security | `OAuth2PasswordBearer` doesn't validate. Router-level deny-by-default. `extra="forbid"`. | `is_admin` boolean, HS256 default. |
| Django_Security | `check --deploy` as a gate. | `min_length: 8` fails NIST's 15. "Change admin URL" is obscurity. CSP claim unverified. |
| Nodejs_Security | Express query-shape type confusion. Exit on `uncaughtException`. | Legacy modules, wrong winston 3 API, hardcoded cookie secret. |
| Database_Security | Per-app, per-environment accounts. App must not own tables. Verify TLS. | MySQL/MSSQL material. Links PostgreSQL 7.0 docs. |
| Supply_Chain, CI_CD | Four threat categories as lens headings. OpenSSF supplier checklist. | Rest duplicated. |
| DOM_based_XSS, NoSQL, Key_Management | DOM rules 6–7 and guidelines 1/6/8/10. Operator injection via object-typed values. One key one purpose, AES-GCM 2^32 limit. | ESAPI rules, invalid JS, FIPS key-generation rule. |

## D. Login-callback FN checklist (from 63C-4, proposal)

1. RP initiates the transaction. Request carries an RP identifier, `state` and a nonce. No unsolicited IdP-initiated logins.
2. Callback bound to the pre-login session by an unguessable value. Reject callbacks outside the right stage.
3. Back-channel code redemption with RP authentication and PKCE. Code single-use, ≤5 min.
4. Validate: signature with the IdP's key, issuer, time window, audience, nonce, replay via assertion identifier.
5. Resolve the account by issuer + subject. Never subject alone, never email alone.
6. Create a session only when all five §3.9 conditions hold. Regenerate the session ID.
7. Linking only from an authenticated session. Notify on every add or remove.
8. Record auth time. Sensitive FNs carry an auth-recency requirement.

## E. Verified defects and corrections

| Item | Defect |
|---|---|
| **My earlier claim (retracted)** | I said NIST's 5-minute cap could replace the unsourced timeout ranges in OWASP's Session sheet. It can't. The 5 minutes applies only to the assertion reference (the authorization code), and it is a SHOULD. Session timeouts live in 63B-4 §5, which nobody has read. |
| **My earlier claim (corrected)** | I wrote "failing to reach an identity API must not extend or end a session". The text is SHALL NOT for establishing or extending, but only SHOULD NOT for ending. |
| **My earlier framing (corrected)** | I presented the §3.11.1 injection measures as requirements. That list is "common best practices". What is mandatory at FAL2+ is the protection outcome and RP-initiated transactions. |
| 63C-4 Table 4 | Cross-references point at stale section numbers (3.12.4 doesn't exist; 3.12.1 is Attribute Bundles, not the assertion identifier). |
| OWASP sheets (carried, not re-checked) | See §C. The broken-Python and wrong-API items are the strongest: AI_Agent_Security, Docker_Security, Nodejs_Security. |

## F. Wings as its own attack surface (proposals)

| Rule | Basis |
|---|---|
| Upstream and fetched text is data, never instructions. One shared statement in the core skill. | Secure_Coding_with_AI, AI_Agent_Security |
| Invisible-character scan (bidi, zero-width, tag characters) over generated code and ingested upstream text. | Secure_Coding_with_AI |
| Test independence: security tests derived from FN authorization lines by script, not authored by the code-writing step. Mechanical gate fails deleted tests, reduced assertion counts, newly mocked units under test. | Secure_Coding_with_AI, gstack |
| Scope gate: each task declares allowed paths. Edits outside them, or to lockfiles, CI, Dockerfiles, package scripts, rules files, stop for sign-off. | oma per-task scope |
| Dependency admission log: exists on registry, age, maintenance, license, lockfile commit. | Secure_Coding_with_AI, NPM_Security |
| Autonomy boundary: reversible local edits autonomous. Destructive or irreversible actions need explicit approval. No gate weakened by the agent that owns the work. | AI_Agent_Security, gstack |

## G. Conflicts and house rules (proposed, not decided)

| Conflict | Proposed rule |
|---|---|
| Top 10 numbering (2021 vs 2025) | Cite CWE or category names |
| Package age: 30 days vs "a few days" | One default, parameterized in the stack record, labeled a wings judgment. **You haven't picked the number.** |
| "Lockout mechanisms" (Code Review) | Throttle with escalating delay, no permanent lockout |
| `node-esapi` (DOM XSS) vs avoid (Node) | Avoid. Framework escaping plus DOMPurify |
| "Never auto-approve" vs autonomous shipping | The autonomy boundary above |
| HS256 / `is_admin` examples | Stack record chooses. Role plus ownership/tenant predicate stays mandatory |
| ".gitignore hides nothing from AI tools" | Tool-specific. Use the tool's own ignore file |

## H. Cross-chat reconciliation for the master chat

- **License (superseded).** I treated OWASP as idea-only in this chat. Your later ruling (chat 8) allows CC BY-SA sources to be adapted if open and credited. ShareAlike still applies to adaptations, so keep OWASP-derived text in **separate credited files with a change notice**, not blended into MIT files. 63C-4 is reusable with attribution (verified here).
- **Autonomy boundary overlaps three sources:** ECC `orch-*` gates and `operator-approval-loop` (chat 9), Addy `/build auto` (chat 9), GateGuard's fail-open behaviour (chat 9). The master picks one gate model. GateGuard's denial cap and fail-open design conflict with "no gate weakened by the agent".
- **Scope gate** overlaps oma per-task prefixes (chat 3) and GateGuard's protected-target classes (chat 9).
- **Invisible-character scan** is already a wings-lint item in chat 9 (§I item 10), with one known BOM-regex false positive. One script serves both.
- **Workflow and Dockerfile pattern scans** overlap chat 9's selector-pinning scan (`mcp-dependency-review` table). Merge into one pin-checker.
- **Dependency admission** overlaps ponytail's debt ledger and mcp-dependency-review. One log format.
- **Test independence** vs mattpocock `tdd` seam confirmation and `implement-spec` unattended subagents (chat 8): seams must be carried in the ticket, and the authorization matrix generated from FN lines can be one such seam.
- **Auth-recency field** extends chat 3's per-FN authorization line. Chat 5 added CSRF note and denial-code set. The master merges these into one line shape.
- **Password minimum:** chat 3 flagged that a house default of 15 regardless of MFA would settle Django's `min_length: 8` (here) and senior-frontend's Zod composition rules (chat 7).
- **Error envelope:** chat 3 and chat 5 disagree on bare Addy envelope vs RFC 9457 serialization. Unchanged by this chat.
- **New IDs `TH-` and `AB-`** fit the linter pattern `[A-Z][A-Z0-9]{0,5}-\d+`. Chat 9 notes ECC's `TEST-ORDER-001` does not.
- **Stack pack rot:** the `applies_to`, `status`, `verified_at`, `source` fields from chats 7 and 9 are the mechanism this chat's packs need.
- **Next.js and Supabase packs** overlap chat 5's ground (Supabase rules, RLS, pooled-connection leak). One owner per fact.

## I. wings-lint additions from this chat

1. Callback FN declares each §D check (signature, issuer, time, audience, nonce, replay, state, PKCE).
2. FN authorization line includes auth recency for sensitive FNs.
3. Diff gate: out-of-scope paths, deleted tests, reduced assertion counts, protected-file changes.
4. Invisible-character scan on generated and ingested text.
5. Workflow patterns: unpinned `uses:`, missing `permissions`, `pull_request_target` with PR-head checkout, `${{ github.event.* }}` inside `run:`.
6. Dockerfile patterns: missing `USER`, unpinned base, secrets in `ARG`/`ENV`, `curl | sh`.
7. JS patterns: `eval`, `new Function`, `innerHTML`, `dangerouslySetInnerHTML` without a sanitizer.
8. Next.js pack: every server action and route handler carries an authorization classification, inventory derived from the file tree.
9. AI features: if the repo imports an LLM SDK, the FN needs a tool allowlist and an authorization line enforced outside the model.
10. `TH-n` requires a response, plus a test reference when "mitigate". `AB-n` links to an FN and a test name.

## J. Unverified, do not carry forward

- Every OWASP Tier 4/5 verdict and defect (not re-checked this pass).
- CVE-2026-39313, the 89%/78% jailbreak figures, the arXiv 2605.x IDs, the MCP spec revision date, Next.js 16 `proxy.ts`, Django 6.0 built-in CSP, npm classic-token revocation, the Node permission model stability claim, the Trivy and Cline post-mortems, the "195M downloads" figure.
- Anything in 63C-4 outside the sections listed in §A.
- The FAL2-as-default call: that's my recommendation, not a NIST requirement.

## Open decisions (carried, as you intended)

FAL2 default with FAL3 as a pack; auth-recency field; no email auto-link; package-age default (no number picked); test-independence rule; autonomy boundary; v1 stack packs (Next.js, Supabase/BaaS, Postgres-Drizzle, GitHub Actions, Docker).

---

# Do I need more files?

I checked the other chats first. Already owned elsewhere, so I'm not asking again: BMAD stub renders, OpenSpec, `google-labs-code/design.md`, `validate_skills.py` (chat 2); Postgres primary docs, RFC 9457/9106, Trail of Bits optional plugins, Supabase `advanced-*` rules (chat 3); mattpocock remaining skills, taste assets, oma-mobile, Vercel agent-skills (chat 8); `generate.py`, GateGuard helpers (chat 9).

**Worth adding for this chat, in priority order:**

1. **NIST 63B-4 §5 (session management) and §3.2.2 (throttling).** This is a gap nobody owns. Chat 3 read only §3.1.1 and says §3.2.2 is unread. 63C-4 defers session rules to 63B-4 §5, and my retracted claim above shows the Session timeout numbers still have no primary source. This is the highest-value file for the auth block. Re-upload 63B-4, or confirm the master chat has it.
2. **OAuth primary sources: RFC 9700 (OAuth 2.0 Security BCP), RFC 7636 (PKCE), and OIDC Core §3.1.3.7 (ID Token validation).** 63C-4 is written for federal RPs and IdPs. The concrete rules for Auth Code + PKCE, exact redirect-URI matching and ID Token checks come from these. I can fetch them myself if you allow it.
3. **OWASP ASVS (CC BY-SA, now adaptable).** Chat 5 cited ASVS 6.4.2 secondhand. It is a numbered verification-requirement catalogue, the closest upstream shape to wings' `R-` security requirements and to review-lens coverage. I haven't read it.
4. **OWASP Prototype_Pollution sheet**, because JavaScript_and_TypeScript defers to it. Low priority, only if the JS pack ships in v1.

**Not needed:** the OWASP Tier 4/5 sheets again. Send them only if the master chat will quote them, since my verdicts rest on a read I can't re-check. Also not needed: more 63C-4 sections (§3.5–3.6 and §5 don't matter for a single-app builder), 63A-4 and 63-4.