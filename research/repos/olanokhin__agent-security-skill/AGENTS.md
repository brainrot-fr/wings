# Agent Security Skill

Load and follow `AI_SECURITY.md` from the project root (also referenced as `@AI_SECURITY.md` in CLAUDE.md-style imports — if your agent does not support `@`-imports, read the file directly).

When the user says `owasp my code`, `owasp this`, `owasp this PR`, or `ai security review`, audit the current file, diff, branch, or PR against:

- `LLM01-LLM10`
- `PIPE01-PIPE13`
- `ASI01-ASI10`

Report `CRITICAL` and `HIGH` findings first with file/line location, issue, and fix.
