# Repo: pbakaus__impeccable
HEADER: path=/home/syed-jalal/dev/wings/research/repos/pbakaus__impeccable/README.md | commit=b4bff1626c344067788c2679f048a20057c7cc5a | license=LICENSE

## Three ways to run the detector

**In your agent.** The design hook scans every UI file your agent edits and hands the findings back before the agent calls the work done.

**In CI or your terminal.** The CLI needs no agent:

```bash
npx impeccable detect src/
npx impeccable detect https://example.com
npx impeccable detect --json .
npx impeccable detect --list-rules
```

Exit code `2` means findings, `1` means a target couldn't be scanned.

**In your browser.** The Chrome extension ...

