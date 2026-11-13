# 00 READ ME FIRST
## Coverage statistics
- Cloned and inventoried: 47 repositories from the task list plus several discovery-list candidates retained for reference only.
- Deep or targeted card generation: 30 repository cards and 8 skill cards across the highest-signal repos.
- Block digests: requirements, frontend, backend, database, security, testing, sdlc-process, packaging.
- Cross files: vocabulary, license register, risk register, lineage map, compatibility matrix, question protocols, validators and artifacts.
## Top findings
- Requirements and SDLC workflows are strongest in GitHub Spec Kit, BMAD, OpenSpec and Blueprint.
- Security audit methodology is most mature in Cloudflare's security-audit-skill, with Semgrep and Trail of Bits as rule/reference peers.
- Packaging portability is strongest in wshobson/agents and the open Agent Skills standard.
- UI quality and interaction guidance is strongest in web-interface-guidelines and Impeccable.
## Top picks per block
- Requirements: Spec Kit, OpenSpec, BMAD, Blueprint
- Frontend: Web Interface Guidelines, Impeccable, UI UX Pro Max
- Backend: robust-skills, Bambu-Developers, fullstack-starter
- Database: robust-skills, Supabase skills, secondsky
- Security: Cloudflare, Semgrep, Trail of Bits, NetResearch
- Testing: mthines, Bambu, Spec Kit, BMAD
- SDLC: BMAD, Spec Kit, Superpowers
- Packaging: wshobson/agents, agentskills/agentskills, harness-engineering
## Biggest conflicts
- Multi-harness success relies on installer and adapter layers, which are more portable than a single vendor CLI but still not universally runtime-free.
- Some repos prioritize procedural workflow over explicit machine-readable traceability.
- Several repos mix platform-specific suggestions with more universal guidance; the house principles prefer extraction over direct adoption.
## License problems
- trailofbits/skills is CC BY-SA 4.0 and should be treated as reference only.
- Some repos include trademark or property notices; they are not a code license issue but an implementation constraint.
## Risks
- Remote installers, browsers and hook automation can create network and tool coupling.
- LLM-eval layers are useful but are not equivalent to deterministic rules or tests.
- The strongest repos often rely on explanation and process more than on hard formal validation, so the target suite should combine both.
## What was not analyzed
- Tier D discovery lists were mined for additional candidates but not deep-read.
- Some tier 2 and tier 3 repos were inventoried rather than individually deep-read in this pass.
