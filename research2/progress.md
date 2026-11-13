RESEARCH2 PROGRESS
===================

Format: block | repo | skill path | status (TODO, READ, CARDED, SKIPPED, FAILED) | lines read | notes

Phase 0: Existing clones verified against research/out/inventory.csv; all present target clones match inventory except vasily repo missing.

security | cloudflare/security-audit-skill | skills/security-audit/ | SKIPPED | 1898 | Full 773-line findings validator and schema/README details read; coverage validator, companion attack classes and tests remain unread; no card
security | natolitech/security-skill | .claude/commands/security-review.md | CARDED | 501 | Full command read; card written
security | natolitech/security-skill | .claude/commands/threat-model.md | CARDED | 236 | Full command read; card written
security | hov172/secure-webapp-skill | SKILL.md + all modes, linked assets/references and licenses | CARDED | 3507 | Reviewed full card scope, README mode documentation and attribution; card written
security | semgrep/skills | skills/llm-security/SKILL.md | SKIPPED | 80 | SKILL.md read; its 10 rules total several thousand lines and AGENTS.md is 3,373 lines; catalog only, no card
security | semgrep/skills | skills/semgrep/SKILL.md + README + 2 references | CARDED | 1163 | All four files read; custom root license text, not SPDX; card written
security | semgrep/skills | skills/code-security/SKILL.md | SKIPPED | 82 | SKILL.md read; its 10,646-line rule directory not read; catalog only, no card
security | mgiovani/cc-arsenal | skills/review-security/SKILL.md + references + evals | CARDED | 712 | Full folder read; MIT; card written
security | olanokhin/agent-security-skill | skills/agent-security/SKILL.md + AI_SECURITY.md | CARDED | 1135 | Actual path verified; full skill and shared instructions/readme/license; MIT; card written
security | trailofbits/skills | plugins/audit-context-building/skills/audit-context-building/SKILL.md | CARDED | 820 | Skill and linked resources read by delegated pass; card written; CC BY-SA paraphrase only
security | trailofbits/skills | plugins/agentic-actions-auditor/skills/agentic-actions-auditor/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
security | trailofbits/skills | plugins/building-secure-contracts/skills/audit-prep-assistant/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
security | netresearch/security-audit-skill | skills/security-audit/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
security | wshobson/agents | plugins/security-scanning/skills/stride-analysis-patterns/SKILL.md | CARDED | 663 | Skill and linked details read by delegated pass; card written
security | Jeffallan/claude-skills | skills/security-reviewer/SKILL.md | CARDED | 1229 | Full skill and every linked reference read; MIT; static only
security | Jeffallan/claude-skills | skills/secure-code-guardian/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
security | addyosmani/agent-skills | skills/security-and-hardening/SKILL.md + hardening-patterns.md + security-checklist.md | CARDED | 816 | Full target and linked resources read; MIT; card written
security | addyosmani/agent-skills | agents/security-auditor.md + docs/agents.md | CARDED | 256 | Persona and linked invocation guide read; MIT; card written
security | dralgorhythm/claude-agentic-framework | .claude/skills/security/threat-modeling/SKILL.md + .claude/rules/security.md | CARDED | 121 | Reference-only, no license found; paraphrased; card written
backend | addyosmani/agent-skills | skills/api-and-interface-design/SKILL.md | CARDED | 369 | Full target read plus 252-line linked deprecation guide; MIT; card written
backend | Jeffallan/claude-skills | skills/architecture-designer/SKILL.md | CARDED | 683 | Full target, five linked references and root MIT license read; card written
backend | Jeffallan/claude-skills | skills/api-designer/SKILL.md | CARDED | 2828 | Full target, five linked references and root MIT license read; card written
backend | wshobson/agents | plugins/developer-essentials/skills/auth-implementation-patterns/SKILL.md | CARDED | 671 | Full target and linked resources read; MIT root license; card written
backend | wshobson/agents | plugins/backend-development/skills/api-design-principles/SKILL.md | CARDED | 1880 | Full target and linked resources read; MIT root license; card written
backend | wshobson/agents | plugins/backend-development/skills/architecture-patterns/SKILL.md | CARDED | 919 | Full target and linked resources read; MIT root license; card written
backend | alirezarezvani/claude-skills | engineering/skills/api-design-reviewer/SKILL.md | CARDED | 5369 | Full skill, linked references/scripts and root MIT license read; card written
backend | secondsky/claude-skills | plugins/rest-api-design/skills/rest-api-design/SKILL.md | CARDED | 123 | Full target and root MIT license read; standalone card written
backend | secondsky/claude-skills | plugins/api-authentication/skills/api-authentication/SKILL.md + references/python-flask.md | CARDED | 335 | Full target, linked Flask examples and root MIT license read; card written
backend | ccheney/robust-skills | skills/clean-ddd-hexagonal/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
backend | first-fluke/fullstack-starter | .agents/skills/oma-architecture/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
backend | first-fluke/fullstack-starter | .agents/skills/oma-backend/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
backend | Bambu-Developers/skills | bambu-nest-api-guide/SKILL.md + README + 2 references | CARDED | 218 | Full skill-folder read; MIT root LICENSE; card: out/skills/Bambu-Developers__skills/bambu-nest-api-guide.md
database | supabase/agent-skills | skills/supabase-postgres-best-practices/SKILL.md + all 31 rules | CARDED | 1751 | Complete rule set read; entry and 31 rule files carded
database | wshobson/agents | plugins/database-design/skills/postgresql-table-design/SKILL.md + reference | CARDED | 310 | Complete skill, linked reference and root license read; card created; no commands run
database | alirezarezvani/claude-skills | engineering/skills/database-designer/SKILL.md + 15 supporting files | CARDED | 6811 | Complete target, README, scripts, references, assets, examples and root license read; no tools run
database | alirezarezvani/claude-skills | engineering/skills/database-schema-designer/SKILL.md + reference | CARDED | 552 | Complete target, linked examples and root license read; examples not run
database | secondsky/claude-skills | database-schema-design | FAILED | 0 | Search found no database schema SKILL.md; only unrelated better-auth reference database-schema.ts
database | ccheney/robust-skills | skills/postgres-drizzle/SKILL.md + all 7 references | CARDED | 4489 | Full target, seven linked references and root MIT license read; no code/database commands run
database | Jeffallan/claude-skills | skills/database-optimizer/SKILL.md + 5 references | CARDED | 2121 | Complete skill, five linked references and root license read; card created; no SQL run
database | Jeffallan/claude-skills | skills/postgres-pro/SKILL.md + 5 references | CARDED | 2095 | Complete skill, five linked references and root license read; card created; no SQL or shell commands run
database | sickn33/agentic-awesome-skills | plugins/agentic-awesome-skills-claude/skills/supabase-postgres-best-practices/; plugins/agentic-awesome-skills/skills/supabase-postgres-best-practices/; skills/supabase-postgres-best-practices/ | READ | 78 | Compared three 36-file copies with Supabase: 18 identical and 18 modified in each; lineage recorded as partial copies; no separate card
testing | mthines/agent-skills | skills/testing/e2e-testing-mobile/SKILL.md | SKIPPED | 0 | Not a listed target; left untouched
testing | mthines/agent-skills | skills/testing/e2e-testing/SKILL.md | SKIPPED | 1383 | Skill and local rules/references/templates read; full confidence/trace-analyzer dependencies were not expanded; Bambu already covers E2E; no card
testing | mthines/agent-skills | skills/quality/tdd/SKILL.md + all 6 local references | CARDED | 691 | Complete target, six local references and MIT license read; no tests/scripts run
testing | Bambu-Developers/skills | bambu-e2e-test-matrix/SKILL.md + all 14 supporting files | CARDED | 1073 | Full folder read incl. 4 agent profiles, templates, README and setup script (not run); MIT
testing | obra/superpowers | skills/test-driven-development/SKILL.md + writing-good-tests.md | CARDED | 528 | Full target and linked reference read; MIT; card written
testing | addyosmani/agent-skills | skills/test-driven-development/SKILL.md + linked testing-patterns.md | CARDED | 657 | Complete target, linked JS/TS reference and root MIT license read; no tests run
testing | addyosmani/agent-skills | skills/browser-testing-with-devtools/SKILL.md | CARDED | 340 | Complete skill and root MIT license read; external docs not opened; no browser/MCP commands run
testing | anton-abyzov/specweave | test; testing | FAILED | 0 | Search found no testing-related SKILL.md path in this clone
testing | wshobson/agents | plugins/accessibility-compliance/skills/wcag-audit-patterns/SKILL.md + details.md | CARDED | 573 | Complete skill, linked details and root MIT license read; no audit tools run
testing | wshobson/agents | plugins/accessibility-compliance/skills/screen-reader-testing/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
testing | vasilyu1983/AI-Agents-public | qa-testing-strategy; qa-testing-playwright | FAILED | 0 | Required shallow-clone retry failed: `git clone --depth 1` could not get GitHub password; no skill files available
testing | github/spec-kit | templates/commands/checklist.md + templates/checklist-template.md | CARDED | 1167 | Commands/templates and Bash/PowerShell/Python prerequisite helpers read; common helpers partial; card written
sdlc-process | github/spec-kit | templates/commands/tasks.md + converge.md + templates/tasks-template.md | CARDED | 1857 | Commands/template and Bash/PowerShell/Python setup/prerequisite helpers read; common helpers partial; card written
sdlc-process | addyosmani/agent-skills | skills/planning-and-task-breakdown/SKILL.md + definition-of-done.md | CARDED | 345 | Complete skill, DoD reference and root MIT license read
sdlc-process | addyosmani/agent-skills | skills/git-workflow-and-versioning/SKILL.md + code-review-and-quality + shipping skills | CARDED | 1112 | Complete target and two linked skills read; no git commands run
sdlc-process | addyosmani/agent-skills | skills/shipping-and-launch/SKILL.md + 5 references | CARDED | 1309 | Complete target and all direct local references read; no deploys/tools run
sdlc-process | addyosmani/agent-skills | skills/ci-cd-and-automation/SKILL.md | CARDED | 414 | Complete skill and root MIT license read; no workflow commands run
sdlc-process | addyosmani/agent-skills | skills/code-review-and-quality/SKILL.md + security/performance checklists | CARDED | 908 | Complete target and two direct references read; named deep-dive skills not expanded
sdlc-process | addyosmani/agent-skills | skills/documentation-and-adrs/SKILL.md | CARDED | 319 | Complete skill and root MIT license read
sdlc-process | addyosmani/agent-skills | skills/incremental-implementation/SKILL.md + definition-of-done.md | CARDED | 337 | Complete skill, DoD reference and root MIT license read
sdlc-process | obra/superpowers | skills/executing-plans/SKILL.md | SKIPPED | 323 | Skill read; scripts and dependent worktree/review protocols not expanded; no card
sdlc-process | obra/superpowers | skills/finishing-a-development-branch/SKILL.md | CARDED | 246 | Complete skill and root MIT license read; no git operations run
sdlc-process | obra/superpowers | skills/verification-before-completion/SKILL.md | CARDED | 120 | Full standalone skill read; MIT; card written
sdlc-process | obra/superpowers | skills/requesting-code-review/SKILL.md + code-reviewer.md | CARDED | 314 | Complete target, linked reviewer template and root MIT license read; no reviewer dispatched
sdlc-process | obra/superpowers | skills/writing-plans/SKILL.md | CARDED | 225 | Full skill and root license read; referenced definition-of-done.md absent; named subskills not expanded
sdlc-process | obra/superpowers | skills/systematic-debugging/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | EveryInc/compound-engineering-plugin | skills/ce-work/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | EveryInc/compound-engineering-plugin | skills/ce-plan/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | EveryInc/compound-engineering-plugin | skills/ce-code-review/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | EveryInc/compound-engineering-plugin | skills/ce-worktree/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | EveryInc/compound-engineering-plugin | skills/ce-compound-refresh/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | EveryInc/compound-engineering-plugin | skills/ce-babysit-pr/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | EveryInc/compound-engineering-plugin | skills/ce-compound/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | garrytan/gstack | plan-devex-review/SKILL.md | SKIPPED | 157 | Partial lineage comparison only (startup, telemetry and selected mode sections); no card
sdlc-process | garrytan/gstack | plan-ceo-review/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | garrytan/gstack | plan-design-review/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | garrytan/gstack | retro/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | garrytan/gstack | design-review/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | garrytan/gstack | openclaw/skills/gstack-openclaw-ceo-review/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | garrytan/gstack | openclaw/skills/gstack-openclaw-retro/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | garrytan/gstack | ship/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | garrytan/gstack | ios-design-review/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | garrytan/gstack | autoplan/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | garrytan/gstack | devex-review/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | garrytan/gstack | plan-eng-review/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | garrytan/gstack | review/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | bmad-code-org/BMAD-METHOD | skills/method/bmad-code-review/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | Intense-Visions/harness-engineering | agents/skills/claude-code/harness-verification/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | getsentry/skills | skills/iterate-pr/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | getsentry/skills | skills/pr-writer/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | getsentry/skills | skills/commit/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | getsentry/skills | skills/code-review/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | anton-abyzov/specweave | plugins/specweave/skills/done/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | anton-abyzov/specweave | plugins/specweave/skills/handoff/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | anton-abyzov/specweave | plugins/specweave/skills/do/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | anton-abyzov/specweave | plugins/specweave/skills/auto/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | anton-abyzov/specweave | skills/sw-done/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | anton-abyzov/specweave | skills/sw-auto/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | anton-abyzov/specweave | skills/sw-handoff/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | anton-abyzov/specweave | skills/sw-do/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | borkweb/skills | skills/gstack/qa-only/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | borkweb/skills | skills/gstack/plan-devex-review/SKILL.md | SKIPPED | 47 | Full target read; linked checks.md and hall-of-fame, README read for lineage only; no card
sdlc-process | borkweb/skills | skills/gstack/plan-design-review/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | borkweb/skills | skills/gstack/design-review/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | borkweb/skills | skills/gstack/design-consultation/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | borkweb/skills | skills/gstack/plan-session/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | borkweb/skills | skills/gstack/investigate/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | borkweb/skills | skills/gstack/plan-deep-review/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | borkweb/skills | skills/gstack/plan-eng-review/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | borkweb/skills | skills/gstack/review/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | borkweb/skills | skills/gstack/qa/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | borkweb/skills | skills/core/humanize/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | borkweb/skills | skills/core/handoff/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | borkweb/skills | skills/core/red-pen/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | borkweb/skills | skills/core/do/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | borkweb/skills | skills/core/prototype/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | borkweb/skills | skills/core/pr-review/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | borkweb/skills | skills/core/offload/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | borkweb/skills | skills/core/desk/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | borkweb/skills | skills/core/agents-md-lint/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | borkweb/skills | skills/core/session-budget/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | borkweb/skills | skills/core/caveman/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | borkweb/skills | skills/core/council/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | borkweb/skills | skills/core/layman/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | borkweb/skills | skills/core/writing-commits/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | borkweb/skills | skills/core/writing-plans/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | borkweb/skills | skills/core/discernment/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | borkweb/skills | skills/core/review-security/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | borkweb/skills | skills/core/auto-scope/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | borkweb/skills | skills/core/writing-sql/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | borkweb/skills | skills/core/complete/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | codex/skills/loom-skills/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | codex/skills/pressure/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-python/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-prompt-engineering/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-c/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-concurrency/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-kustomize/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-crossplane/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-skills/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-csharp/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-swift/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-testing/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-plan-writer/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-data-visualization/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-fluxcd/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-webhooks/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-database-design/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-code-migration/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-istio/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-diagramming/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-search/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-grafana/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-i18n/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-threat-model/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-rate-limiting/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-ci-cd/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-karpenter/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-ruby/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-sql-optimization/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-orchestration/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-performance-testing/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-wiring-test/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-php/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-golang/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-md-tables/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-prometheus/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-caching/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-model-evaluation/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-typescript/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-before-after/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-api-documentation/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-kubernetes/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-cpp/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-code-review/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-dead-code-check/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-docker/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-data-validation/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-security-scan/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-scala/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-git-workflow/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-dependency-scan/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-e2e-testing/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-auth/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-security-audit/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-argocd/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-javascript/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-test-strategy/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-technical-writing/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-accessibility/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-usage/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-background-jobs/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-event-driven/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-dart/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-serialization/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-logging-observability/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-refactoring/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-documentation/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-feature-flags/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-api-design/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-kotlin/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-rust/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-elixir/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-debugging/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-java/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-react/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-error-handling/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
sdlc-process | cosmix/claude-loom | skills/loom-terraform/SKILL.md | SKIPPED | 0 | Not deep-read due scope cap; catalog-only; no card
packaging | agentskills/agentskills | specification + skills-ref validator | CARDED | 1244 | Packaging card written; root and skills-ref Apache-2.0 licenses reviewed
packaging | wshobson/agents | Makefile + adapter generators + manifests | SKIPPED | 0 | Filename-filtered inventory: 150 candidates / 7,812 lines; not deep-read due scope cap
packaging | addyosmani/agent-skills | marketplace manifests | CARDED | 743 | Read all 14 manifest/Gemini TOML files and three validators; targeted README, install and CI refs checked
packaging | obra/superpowers | manifests + marketplace entries | CARDED | 936 | Read all 10 target manifests, OpenCode install/runtime files, version config/script, hook and targeted validation files
packaging | github/spec-kit | integration system | CARDED | 1076 | Read integration index/API, registry, Copilot example, install/CLI excerpts and root MIT license; not every adapter implementation
packaging | EveryInc/compound-engineering-plugin | converter CLI | SKIPPED | 0 | Filename-filtered inventory: 99 candidates / 5,991 lines; converter target list not traced
packaging | Intense-Visions/harness-engineering | plugin manifests | SKIPPED | 0 | Filename-filtered inventory: 89 candidates / 15,692 lines; manifest families not deep-read
packaging | pulumi/agent-skills | plugin manifests + .agents/skills | CARDED | 1039 | Read all 13 plugin/marketplace manifests, Gemini builder/metadata, manifest tests, targeted CI/README refs and root Apache-2.0 license; .agents/skills absent
packaging | getsentry/skills | plugin manifests + .agents/skills | CARDED | 329 | Read both Claude manifests, root Apache-2.0 license, README install/layout sections; verified .agents/skills symlink to ../skills
