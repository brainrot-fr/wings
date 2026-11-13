# alirezarezvani/claude-skills / api-design-reviewer
SOURCE: `engineering/skills/api-design-reviewer/SKILL.md` | commit `08cd8a9fc86cc370e2c0d448e8171fbcfdbc5a30` | MIT (root `LICENSE`; no per-skill notice) | 5,369 lines read (`wc -l`)
FRONTMATTER: name and description, verbatim
```yaml
---
name: "api-design-reviewer"
description: "Use for any PR or spec that adds or changes REST endpoints, before approving it. Lints conventions with api_linter.py, detects breaking changes with breaking_change_detector.py and scores the design with api_scorecard.py."
---
```
[V] `engineering/skills/api-design-reviewer/SKILL.md:L1-L4`
FILES READ:
| Path | Lines | Role |
|---|---:|---|
| `engineering/skills/api-design-reviewer/SKILL.md` | 440 | Workflow |
| `engineering/skills/api-design-reviewer/references/api_antipatterns.md` | 679 | Anti-patterns |
| `engineering/skills/api-design-reviewer/references/rest_design_rules.md` | 486 | REST rules |
| `engineering/skills/api-design-reviewer/scripts/api_linter.py` | 964 | Linter |
| `engineering/skills/api-design-reviewer/scripts/api_scorecard.py` | 1669 | Scorer |
| `engineering/skills/api-design-reviewer/scripts/breaking_change_detector.py` | 1110 | Comparator |
| `LICENSE` | 21 | Root license |
FILES UNREAD: External Further Reading URLs (not local files); all skill-folder files read. [V] `engineering/skills/api-design-reviewer/references/rest_design_rules.md:L481-L486`
JOB: Review REST endpoint PRs/specs before approval; lint, compare versions, score, attach reports. [V] `engineering/skills/api-design-reviewer/SKILL.md:L16-L29`
PROCEDURE: Run linter → compare old/new specs → score; report, fix, rerun. [GATE] Clean lint, no unversioned breaking change, agreed minimum grade. [V] `engineering/skills/api-design-reviewer/SKILL.md:L16-L29`
DECISION RULES: Weights 30/20/20/15/15; linter error/warning/info penalties 10/3/1 per endpoint; grades A/B/C/D start at 90/80/70/60. Comparator severities critical/high/medium/low/info; `--exit-on-breaking` and `--min-grade` gate. [V] `engineering/skills/api-design-reviewer/SKILL.md:L49-L54`; `engineering/skills/api-design-reviewer/scripts/api_linter.py:L66-L78`; `engineering/skills/api-design-reviewer/scripts/api_scorecard.py:L54-L99`; `engineering/skills/api-design-reviewer/scripts/api_scorecard.py:L1611-L1661`; `engineering/skills/api-design-reviewer/scripts/breaking_change_detector.py:L35-L50`; `engineering/skills/api-design-reviewer/scripts/breaking_change_detector.py:L1042-L1053`
ARTIFACT SHAPE: lint `summary/issues`; breaking `summary/hasBreakingChanges/changes`; scorecard `overall/api_info/categories/topRecommendations`. [V] `engineering/skills/api-design-reviewer/scripts/api_linter.py:L730-L757`; `engineering/skills/api-design-reviewer/scripts/breaking_change_detector.py:L865-L873`; `engineering/skills/api-design-reviewer/scripts/api_scorecard.py:L1454-L1477`
QUESTION PROTOCOL: No question set; workflow expects an agreed minimum grade. [V] `engineering/skills/api-design-reviewer/SKILL.md:L25-L29`
VALIDATION: Linter: one OpenAPI JSON or `--raw-endpoints`, checks conventions/responses/docs. Comparator: two JSON specs, change findings/migration hints. Scorecard: one JSON spec, five-dimension grade. Python standard-library imports; text/JSON stdout or `--output`; no network/subprocess [I]. [V] `engineering/skills/api-design-reviewer/scripts/api_linter.py:L17-L23`; `engineering/skills/api-design-reviewer/scripts/api_linter.py:L867-L964`; `engineering/skills/api-design-reviewer/scripts/breaking_change_detector.py:L18-L23`; `engineering/skills/api-design-reviewer/scripts/breaking_change_detector.py:L1012-L1110`; `engineering/skills/api-design-reviewer/scripts/api_scorecard.py:L18-L25`; `engineering/skills/api-design-reviewer/scripts/api_scorecard.py:L1580-L1669`
AGENT FEATURES REQUIRED: None; Python CLI.
STATE ON DISK: No review state; optional report files.
VOCABULARY: Linter `error/warning/info`; comparator `breaking/potentially_breaking/non_breaking/enhancement`, severity `critical/high/medium/low/info`. No requirement IDs evident. [V] `engineering/skills/api-design-reviewer/scripts/api_linter.py:L28-L35`; `engineering/skills/api-design-reviewer/scripts/breaking_change_detector.py:L35-L50`; `engineering/skills/api-design-reviewer/SKILL.md:L1-L440`
NON-OBVIOUS TECHNIQUES: Penalties normalized per endpoint [V] `engineering/skills/api-design-reviewer/scripts/api_linter.py:L66-L82`; replacement hints for paths ≥50% segment-similar [V] `engineering/skills/api-design-reviewer/scripts/breaking_change_detector.py:L823-L845`; weighted category grades [V] `engineering/skills/api-design-reviewer/scripts/api_scorecard.py:L54-L99`; `engineering/skills/api-design-reviewer/scripts/api_scorecard.py:L129-L139`.
FAILURE MODE FOUGHT: Convention drift, breaking changes, thin docs, prose-only review. [V] `engineering/skills/api-design-reviewer/SKILL.md:L16-L54`
BAGGAGE: Quick-start `-o` fails: CLIs declare `--output` only. Linter warns only above six path segments; reference advises max 3–4. [V] `engineering/skills/api-design-reviewer/SKILL.md:L18-L26`; `engineering/skills/api-design-reviewer/scripts/api_linter.py:L907-L909`; `engineering/skills/api-design-reviewer/scripts/api_linter.py:L351-L360`; `engineering/skills/api-design-reviewer/scripts/breaking_change_detector.py:L1042-L1045`; `engineering/skills/api-design-reviewer/scripts/api_scorecard.py:L1605-L1608`; `engineering/skills/api-design-reviewer/references/rest_design_rules.md:L8-L17`
RISKS: Scorecard security/DX are spec heuristics, not implementation verification; cannot establish authorization or tenant isolation. [I] `engineering/skills/api-design-reviewer/scripts/api_scorecard.py:L821-L927`; `engineering/skills/api-design-reviewer/scripts/api_scorecard.py:L997-L1105`
FIT: API review — ADAPT optional flow; EXTRACT naming checks from `api_linter.py`, compatibility logic from `breaking_change_detector.py`; REFERENCE `rest_design_rules.md`; REJECT mandatory CLI/letter-grade policy. Needs fallback judgment and P0–P3 scale. [I]
CONFLICTS: Required three-script sign-off and letter grades conflict with optional-tool portability and house P0–P3 findings.
KEY QUOTES: “Never sign off an API review on prose alone” [V] `engineering/skills/api-design-reviewer/SKILL.md:L29-L29`
CONFIDENCE: High; full skill, references, scripts, and root license read.
