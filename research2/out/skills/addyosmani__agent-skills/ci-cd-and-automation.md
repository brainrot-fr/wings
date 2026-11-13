# addyosmani/agent-skills / ci-cd-and-automation

SOURCE: `skills/ci-cd-and-automation/SKILL.md` | commit `301b02b12bff98e4688e6984af6556802322bbde` | MIT | 414 lines read
FRONTMATTER: `name: ci-cd-and-automation`; `description: Automates CI/CD pipeline setup. Use when setting up or modifying build and deployment pipelines. Use when you need to automate quality gates, configure test runners in CI, or establish deployment strategies.`
FILES READ:
| Path | Lines |
|---|---:|
| `skills/ci-cd-and-automation/SKILL.md` | 393 |
| `LICENSE` | 21 |
FILES UNREAD: No direct local file links; optional debugging skill was not expanded.
JOB: Automate quality gates and staged deployment for every change. [V] (`skills/ci-cd-and-automation/SKILL.md:L1-L34`)
PROCEDURE: Lint, typecheck, unit/integration/E2E, build, security and bundle gates; stage and deploy with monitoring/rollback. [V] (`skills/ci-cd-and-automation/SKILL.md:L26-L124`, `L137-L231`)
DECISION RULES: E2E is optional in its example pipeline; failures block merge, CI never receives production secrets, deployment must be reversible. [V] (`skills/ci-cd-and-automation/SKILL.md:L26-L72`, `L225-L300`)
ARTIFACT SHAPE: CI workflow, integration/E2E jobs, preview/rollout/rollback workflows and quality gate checklist. [V] (`skills/ci-cd-and-automation/SKILL.md:L36-L124`, `L137-L231`)
QUESTION PROTOCOL: None.
VALIDATION: PR/push triggers, blocking checks, tests/build/audit and rollback path; no workflows were run. [V] (`skills/ci-cd-and-automation/SKILL.md:L280-L393`)
AGENT FEATURES REQUIRED: Optional agent feedback loop for CI failures; no special runtime required. [V] (`skills/ci-cd-and-automation/SKILL.md:L126-L136`)
STATE ON DISK: CI YAML, environment secrets, flags and deployment configuration. [V] (`skills/ci-cd-and-automation/SKILL.md:L36-L124`, `L205-L280`)
VOCABULARY: Shift-left, quality gate, preview deploy, feature flag, canary, Build Cop, rollback. [V] (`skills/ci-cd-and-automation/SKILL.md:L8-L34`, `L137-L280`)
NON-OBVIOUS TECHNIQUES: Pass untrusted rollback version through an environment variable, not shell interpolation; parallelize independent jobs after pipeline exceeds 10 minutes. [V] (`skills/ci-cd-and-automation/SKILL.md:L194-L231`, `L255-L330`)
FAILURE MODE FOUGHT: Skipped checks, ignored CI failures, production secrets in CI and deployments without rollback. [V] (`skills/ci-cd-and-automation/SKILL.md:L280-L393`)
BAGGAGE: GitHub Actions/npm examples are stack-specific; thresholds and job order require local adaptation.
RISKS: Samples install packages, run audits and deploy/rollback via `npx`; credentials must be scoped and commands reviewed. [V] (`skills/ci-cd-and-automation/SKILL.md:L36-L124`, `L137-L231`)
FIT: SDLC — **EXTRACT** quality gates, secret separation and reversible rollout; keep provider-specific YAML optional. [I]
CONFLICTS: E2E is labeled optional despite a broad no-gate-skipped rule; make gate policy explicit per project. [V] (`skills/ci-cd-and-automation/SKILL.md:L26-L34`)
KEY QUOTES: None.
CONFIDENCE: High; complete skill and root license read; no workflow commands run.
