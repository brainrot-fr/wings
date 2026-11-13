# addyosmani/agent-skills / shipping-and-launch

SOURCE: `skills/shipping-and-launch/SKILL.md` | commit `301b02b12bff98e4688e6984af6556802322bbde` | MIT | 1309 lines read
FRONTMATTER: `name: shipping-and-launch`; `description: Prepares production launches. Use when preparing to deploy to production, or when asking what needs to be in place before shipping. Use when you need a pre-launch checklist, when setting up monitoring, when planning a staged rollout, or when you need a rollback strategy.`
FILES READ:
| Path | Lines |
|---|---:|
| `skills/shipping-and-launch/SKILL.md` | 336 |
| `references/definition-of-done.md` | 67 |
| `references/security-checklist.md` | 248 |
| `references/performance-checklist.md` | 239 |
| `references/accessibility-checklist.md` | 160 |
| `skills/observability-and-instrumentation/SKILL.md` | 238 |
| `LICENSE` | 21 |
FILES UNREAD: None of the direct local references; deeper skills named in those references were not expanded.
JOB: Prepare reversible, observable, incremental production launches with readiness checks, rollout and rollback plans. [V] (`skills/shipping-and-launch/SKILL.md:L1-L62`)
PROCEDURE: Complete pre-launch gates, stage and canary, compare metrics to baseline, monitor, advance/hold/rollback, then remove flags. [V] (`skills/shipping-and-launch/SKILL.md:L16-L62`, `L92-L176`)
DECISION RULES: Roll back at >2× error baseline or >50% p95 latency increase; apply error-budget and flagged rollout gates. [V] (`skills/shipping-and-launch/SKILL.md:L123-L176`, `L207-L230`)
ARTIFACT SHAPE: Checklist, rollout thresholds, monitoring plan, rollback triggers/steps and time-to-rollback. [V] (`skills/shipping-and-launch/SKILL.md:L16-L62`, `L123-L176`, `L231-L264`)
QUESTION PROTOCOL: None.
VALIDATION: Health check, errors, latency, critical flow, logs and rollback readiness; DoD plus security/performance/accessibility references. [V] (`skills/shipping-and-launch/SKILL.md:L177-L264`; `references/definition-of-done.md:L20-L67`)
AGENT FEATURES REQUIRED: None.
STATE ON DISK: Feature flags, dashboards/runbooks, rollback notes and release documentation. [V] (`skills/shipping-and-launch/SKILL.md:L62-L115`, `L231-L264`)
VOCABULARY: Canary, feature flag, error budget, SLO, baseline, hold/rollback, p95. [V] (`skills/shipping-and-launch/SKILL.md:L62-L176`)
NON-OBVIOUS TECHNIQUES: Advance only against baseline-relative thresholds; error-budget burn can hold rollout even when individual metrics look green. [V] (`skills/shipping-and-launch/SKILL.md:L123-L176`, `L207-L230`)
FAILURE MODE FOUGHT: Big-bang deploys, unobserved regressions, missing rollback plans and unowned feature flags. [V] (`skills/shipping-and-launch/SKILL.md:L16-L62`, `L177-L264`)
BAGGAGE: Numeric rollout/error-budget thresholds are example policy, not universal SLOs.
RISKS: Deployment commands and monitoring hooks can affect production; no deployment or external tool was run. [V] (`skills/shipping-and-launch/SKILL.md:L92-L176`, `L231-L264`)
FIT: SDLC — **ADAPT** explicit readiness, measurable rollout and rollback gates to project SLOs and approval policy. [I]
CONFLICTS: The checklist includes absolute thresholds; replace with service-specific baselines and authorized rollout controls. [I]
KEY QUOTES: None.
CONFIDENCE: High; target, all direct local references and root license read.
