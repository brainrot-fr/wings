# semgrep/skills / semgrep
SOURCE: `research/repos/semgrep__skills` | commit `68177b8830f96cd9d10dacbb14dde2566360503d` | `LICENSE` says Semgrep Rules License v1.0; no SPDX identifier | 1,163 lines, `find .../skills/semgrep -type f -print0 | xargs -0 wc -l`
FRONTMATTER: `name: semgrep`; `description: "Run Semgrep static analysis scans and create custom detection rules. Use when asked to scan code with Semgrep, find security vulnerabilities, write custom YAML rules, or detect specific bug patterns. IMPORTANT: Also use this skill when users ask to 'scan for bugs', 'check code quality', 'find vulnerabilities', 'static analysis', 'lint for security', 'audit this code', or want to enforce coding standards — even if they don't mention Semgrep by name. Semgrep is the right tool for pattern-based code scanning across 30+ languages."`
FILES READ:
| Path | Lines | Role |
|---|---:|---|
| `skills/semgrep/SKILL.md`; `README.md` | 321; 109 | Scan/rule workflow; usage |
| `skills/semgrep/references/quick-reference.md`; `workflow.md` | 322; 411 | Syntax; detailed rule lifecycle |
FILES UNREAD: None inside skill folder. Root `LICENSE` read.
JOB: Scan code or author detection rules; output findings or rule/test files. [V] (`skills/semgrep/SKILL.md:L47-L80`, `L109-L127`, `L215-L220`)
PROCEDURE:
1. `Part 1`: select ruleset/paths. [V] (`skills/semgrep/SKILL.md:L47-L87`)
2. `Part 2`: classify taint vs pattern; test, inspect AST, iterate rule. [V] (`skills/semgrep/SKILL.md:L109-L155`, `L206-L220`)
3. GitHub Actions uses base-commit baseline for PR. [V] (`skills/semgrep/SKILL.md:L269-L308`)
DECISION RULES: Taint for source→sink dataflow; patterns for syntax. Require 100% test pass, no missed/incorrect lines. [V] (`skills/semgrep/SKILL.md:L118-L125`, `L206-L220`)
ARTIFACT SHAPE: YAML fields `id,languages,severity,message` + patterns; annotated test; optional JSON/SARIF. [V] (`skills/semgrep/SKILL.md:L127-L155`, `L73-L78`, `L215-L220`)
QUESTION PROTOCOL: n/a.
VALIDATION: CLI `--test`, `--validate`, `--dump-ast`, `--dataflow-traces`; binary needed. Immediate `ruleid:`/`ok:` annotations; external rulesets. [V] (`skills/semgrep/SKILL.md:L192-L204`, `references/workflow.md:L198-L245`, `L327-L389`)
AGENT FEATURES REQUIRED: shell + Semgrep CLI; MCP is preferred only when available, otherwise CLI fallback. [V] (`skills/semgrep/SKILL.md:L10-L20`)
STATE ON DISK: `<rule-id>.yaml` + test file; optional text/SARIF/JSON findings. [V] (`skills/semgrep/SKILL.md:L73-L78`, `L215-L220`)
VOCABULARY: severity `ERROR|WARNING|INFO`; rule IDs lowercase hyphenated; test markers `ruleid`, `ok`, `todoruleid`, `todook`. [V] (`references/quick-reference.md:L7-L16`, `L186-L203`)
NON-OBVIOUS TECHNIQUES:
- Test safe and vulnerable cases before the rule; annotation must immediately precede code. [V] (`references/workflow.md:L38-L75`)
- Taint rules explicitly model sources, sinks, sanitizers, and optionally propagators. [V] (`references/quick-reference.md:L130-L184`)
- Optimize equivalences only after all tests pass, then rerun tests after each change. [V] (`references/workflow.md:L241-L325`)
FAILURE MODE FOUGHT: False positives/negatives from untested or broad rules. [V] (`skills/semgrep/SKILL.md:L118-L125`, `L232-L267`)
BAGGAGE: Semgrep-specific syntax and runtime.
RISKS: README installs via `npx`; SKILL offers pip/Brew/Docker and external rulesets. [V] (`skills/semgrep/README.md:L34-L37`, `skills/semgrep/SKILL.md:L32-L44`, `L55-L71`)
FIT: security: ADAPT test-first, taint components, test markers. No requirement mapping. [I]
CONFLICTS: `npx`/package install, external rules, and binary conflict with no-download principles.
KEY QUOTES: None.
CONFIDENCE: High for skill and local workflow; license terms need a human/legal check because root `LICENSE` names a custom license without SPDX.
