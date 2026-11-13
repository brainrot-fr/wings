# mgiovani/cc-arsenal / review-security
SOURCE: commit `00280650a489923032468ca05b776e3c4f3496a0` | MIT, root `LICENSE` | 712 lines; `find .../skills/review-security -type f -print0 | xargs -0 wc -l`
FRONTMATTER: `name: review-security`; `description: Perform an OWASP Top 10-focused static security review of a PR, commit, or entire codebase, grep for vulnerable patterns (injection, broken access control, crypto failures, hardcoded secrets), verify each match by reading it in context, and produce a severity-ranked report with file:line evidence and fix suggestions. Use to audit code security, scan for vulnerabilities, or check OWASP compliance, "security review", "scan for vulnerabilities", "check OWASP top 10", "audit for XSS/SQLi/hardcoded secrets", "is this PR safe to ship security-wise". Analysis only, never modifies code. Not for general code quality review (use review-code), or dependency CVE/license/staleness auditing (use review-deps).`
FILES READ:
| Path | Lines | Role |
|---|---:|---|
| `skills/review-security/SKILL.md`; `references/agent-prompts.md`; `references/report-template.md` | 209; 302; 123 | Procedure; six scan prompts; report structure |
| `skills/review-security/evals/trigger-eval.json`; `evals/evals.json` | 23; 55 | Trigger and behavior cases |
FILES UNREAD: None within skill folder. Root `LICENSE` read.
JOB: Static PR/commit/repository review; output evidence-backed report. [V] (`skills/review-security/SKILL.md:L45-L64`, `L142-L154`)
PROCEDURE: Scope → stack → progress → six agent scans or inline fallback → dedupe/count → report → verify. [V] (`skills/review-security/SKILL.md:L45-L154`)
DECISION RULES: `--scope` selects categories; A03 excludes CVEs. Severity Critical/High/Medium/Low; require file/line, snippet and 2–3 fixes. [V] (`skills/review-security/SKILL.md:L87-L122`, `L124-L140`)
ARTIFACT SHAPE: Scope, stats, A01–A10 groups; finding severity/file/explanation/snippet/fixes; prioritized recommendations. [V] (`references/report-template.md:L10-L92`)
QUESTION PROTOCOL: n/a.
VALIDATION: Grep/Read-based verification; report checklist checks evidence, scope, duplicates, severity, and counted statistics. Eval JSON specifies trigger and behavior checks; no executable validator. [V] (`skills/review-security/SKILL.md:L33-L43`, `L146-L152`, `evals/evals.json:L1-L55`)
AGENT FEATURES REQUIRED: Explore subagents preferred; inline fallback. Bash/Grep/Read/TodoWrite named. [V] (`skills/review-security/SKILL.md:L66-L78`, `L106-L117`)
STATE ON DISK: Progress tracked during scan; final Markdown report; no mandated persistent state file. [V] (`skills/review-security/SKILL.md:L75-L78`, `L142-L154`)
VOCABULARY: OWASP A01–A10; severities Critical/High/Medium/Low; no stable finding IDs or requirement IDs. [V] (`skills/review-security/SKILL.md:L80-L105`, `L130-L140`)
NON-OBVIOUS TECHNIQUES:
- Scope/category/agent matrix with inline fallback. [V] (`skills/review-security/SKILL.md:L87-L117`)
- Deduplicate; compute statistics from findings. [V] (`skills/review-security/SKILL.md:L124-L140`)
- Defer CVE/version/license scan to `review-deps`. [V] (`skills/review-security/SKILL.md:L115-L123`)
FAILURE MODE FOUGHT: Hallucinations, scope drift, false positives, inflated counts. [V] (`skills/review-security/SKILL.md:L33-L43`)
BAGGAGE: Claude metadata, six-agent plan, OWASP taxonomy.
RISKS: Live OWASP check and `gh` PR lookup; prompt file includes exploit-payload examples. [V] (`skills/review-security/SKILL.md:L28-L31`, `L51-L64`, `references/agent-prompts.md:L115-L130`)
FIT: security: ADAPT evidence, scope, fallback, counted findings; replace four-tier severity and add stable IDs/requirement links. [I]
CONFLICTS: OWASP freshness check uses network; required isolated-agent review is not guaranteed when the fallback runs inline.
KEY QUOTES: None.
CONFIDENCE: High; all five skill-folder files read.
