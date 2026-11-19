### new candidates/alibaba-open-code-review/skills/open-code-review-delegate
- Purpose: Prepare a deterministic, coverage-accounted review for a host LLM.
- Wings block fit: sdlc | security
- Maturity: real mechanism
- Core mechanism worth taking:
  - `skills/open-code-review-delegate/SKILL.md:25-33` — separates range/workspace selection from review execution.
  - `skills/open-code-review-delegate/SKILL.md:62-64` — produces plain diffs with external diff/text conversion disabled.
  - `skills/open-code-review-delegate/SKILL.md:128` — requires explicit per-file coverage accounting.
- Gotchas/defects found: None verified in the opened file.
- Hard dependencies: `ocr` CLI, Git; host agent/LLM performs the actual review.
- Portability: partial — deterministic approach transfers, but OCR CLI and its diff/rule interfaces do not.
- Overlap: open-code-review; wings security and SDLC review processes.
- Verdict: TAKE-MECHANISM — bounded deterministic preprocessing plus explicit coverage is reusable.
- Confidence in this card: high

### new candidates/alibaba-open-code-review/skills/open-code-review
- Purpose: Run an LLM-backed review through the Open Code Review CLI and format findings.
- Wings block fit: sdlc | security
- Maturity: vendor-specific
- Core mechanism worth taking:
  - `skills/open-code-review/SKILL.md:27-37` — pass business context into the review rather than reviewing in a vacuum.
  - `skills/open-code-review/SKILL.md:75-89` — group findings by severity and require user verification before committing fixes.
- Gotchas/defects found: `:202` supplies fixed token figures as defaults; they are not established as general limits in this file.
- Hard dependencies: `ocr` CLI, Node/npm for installation, configured external LLM provider, network.
- Portability: no — workflow is coupled to OCR commands and its supported providers.
- Overlap: open-code-review-delegate; wings SDLC and security review.
- Verdict: SAMPLE-ONLY — useful review-flow examples, but CLI/provider/runtime requirements conflict with wings decisions.
- Confidence in this card: medium
