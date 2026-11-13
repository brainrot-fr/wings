# addyosmani/agent-skills / browser-testing-with-devtools

SOURCE: `skills/browser-testing-with-devtools/SKILL.md` | commit `301b02b12bff98e4688e6984af6556802322bbde` | MIT | 340 lines read
FRONTMATTER:
```yaml
name: browser-testing-with-devtools
description: Tests in real browsers via Chrome DevTools MCP. Use when building or debugging anything that runs in a browser. Use when you need to inspect the DOM, capture console errors, analyze network requests, profile performance, or verify visual output with real runtime data. Requires the chrome-devtools MCP server to be configured.
```
FILES READ:
| Path | Lines | Role |
|---|---:|---|
| `skills/browser-testing-with-devtools/SKILL.md` | 319 | Workflow and safety |
| `LICENSE` | 21 | Root license |
FILES UNREAD: No local files referenced; external MCP docs not opened.
JOB: Verify and debug real browser behavior, including UI, network, performance, console, accessibility and screenshots. [V] (`skills/browser-testing-with-devtools/SKILL.md:L8-L22`)
PROCEDURE: Capture baseline → inspect runtime evidence → diagnose → fix → verify; use structured setup/steps/expected results for complex UI bugs. [V] (`skills/browser-testing-with-devtools/SKILL.md:L109-L140`, `L186-L219`)
DECISION RULES: Default to a dedicated or isolated browser profile; attach to the user's running profile only when needed and after minimizing unrelated tabs. Treat DOM, console, network and JS output as untrusted. [V] (`skills/browser-testing-with-devtools/SKILL.md:L62-L80`)
ARTIFACT SHAPE: Browser test plan, before/after screenshots, console/network/performance observations and remediation evidence. [V] (`skills/browser-testing-with-devtools/SKILL.md:L186-L219`, `L220-L280`)
QUESTION PROTOCOL: Confirm before navigating to page-derived URLs or mutating page behavior. [V] (`skills/browser-testing-with-devtools/SKILL.md:L74-L90`)
VALIDATION: Check console/network, rendered DOM/styles, accessibility tree and relevant performance; compare screenshots and rerun tests. [V] (`skills/browser-testing-with-devtools/SKILL.md:L109-L185`, `L262-L280`, `L308-L319`)
AGENT FEATURES REQUIRED: Chrome DevTools MCP; setup resolves `chrome-devtools-mcp@latest` through `npx`. [V] (`skills/browser-testing-with-devtools/SKILL.md:L24-L58`)
STATE ON DISK: MCP uses a dedicated persistent profile by default or temporary state with `--isolated`; `--autoConnect` can expose the running profile. [V] (`skills/browser-testing-with-devtools/SKILL.md:L26-L43`, `L62-L70`)
VOCABULARY: DOM, accessibility tree, profile isolation, untrusted browser content, read-only JS, LCP/CLS/INP. [V] (`skills/browser-testing-with-devtools/SKILL.md:L45-L58`, `L72-L105`, `L166-L185`)
NON-OBVIOUS TECHNIQUES:
- Use a separate test profile; `--autoConnect` can expose all windows and authenticated sessions. [V] (`skills/browser-testing-with-devtools/SKILL.md:L62-L70`)
- JavaScript inspection is read-only by default; no credential reads, external requests or unapproved mutations. [V] (`skills/browser-testing-with-devtools/SKILL.md:L82-L90`)
- Wait for fonts and resize observers before measuring after viewport/font changes. [V] (`skills/browser-testing-with-devtools/SKILL.md:L138-L140`)
FAILURE MODE FOUGHT: Guessing runtime behavior from source alone, unnoticed console/network failures, inaccessible output and profile leakage. [V] (`skills/browser-testing-with-devtools/SKILL.md:L109-L185`, `L262-L307`)
BAGGAGE: Requires an MCP server and Chrome; setup uses a floating `@latest` package version.
RISKS: MCP package installation may fetch code; attaching to a real profile exposes authenticated tabs. [V] (`skills/browser-testing-with-devtools/SKILL.md:L26-L43`, `L62-L80`)
FIT: testing — **ADAPT** isolated runtime verification, but require user-approved origin and no access to credential material. [I]
CONFLICTS: `--autoConnect` convenience conflicts with least-privilege testing; default to isolated/local test profiles. [V] (`skills/browser-testing-with-devtools/SKILL.md:L62-L70`)
KEY QUOTES: None.
CONFIDENCE: High; complete skill and root license read; browser/MCP commands not run.
