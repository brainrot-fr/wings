# License register

Root `LICENSE`/`NOTICE` files were located with `find` and opened for the target repositories. Canonical identifiers below are recognized from the license titles; most source files do not contain an SPDX tag. This is an inventory, not legal advice. Entries for the four pre-flagged repositories at the end were checked even though they are not deep-read targets.

## Target repositories

| Repository | License file and identification | Exceptions / trademark notes |
|---|---|---|
| Bambu-Developers/skills | `research/repos/Bambu-Developers__skills/LICENSE:L1-L21` — MIT | No separate skill exception found for reviewed E2E/API targets. |
| EveryInc/compound-engineering-plugin | `research/repos/EveryInc__compound-engineering-plugin/LICENSE:L1-L21` — MIT | No per-skill exception reviewed. |
| Intense-Visions/harness-engineering | `research/repos/Intense-Visions__harness-engineering/LICENSE:L1-L21` — MIT | No per-skill exception reviewed. |
| Jeffallan/claude-skills | `research/repos/Jeffallan__claude-skills/LICENSE:L1-L21` — MIT | Security-reviewer and both backend targets carded; no separate skill exception found. |
| addyosmani/agent-skills | `research/repos/addyosmani__agent-skills/LICENSE:L1-L21` — MIT | No per-skill exception found for the reviewed API, hardening and security-auditor targets. |
| agentskills/agentskills | Root `LICENSE:L1-L201` and `skills-ref/LICENSE:L1-L201` — Apache-2.0; `docs/LICENSE:L1-L395` — CC BY 4.0 | The specification document excerpt requires CC BY attribution and a note if modified; Apache-2.0 Section 6 does not grant trademark rights. |
| alirezarezvani/claude-skills | `research/repos/alirezarezvani__claude-skills/LICENSE:L1-L21` — MIT | API-design-reviewer carded; no per-skill exception found. |
| anton-abyzov/specweave | `research/repos/anton-abyzov__specweave/LICENSE:L1-L21` — MIT | No testing skill path was found; no testing card. |
| bmad-code-org/BMAD-METHOD | `research/repos/bmad-code-org__BMAD-METHOD/LICENSE:L1-L21` — MIT | No per-skill exception reviewed. |
| borkweb/skills | `research/repos/borkweb__skills/LICENSE:L1-L21` — MIT | Lineage spot-check confirms a gstack port; upstream gstack is also MIT and has `NOTICE.md`. No full copied-content or notice applicability review; see `lineage.md`. |
| ccheney/robust-skills | `research/repos/ccheney__robust-skills/LICENSE:L1-L21` — MIT | No per-skill exception reviewed. |
| cloudflare/security-audit-skill | `research/repos/cloudflare__security-audit-skill/LICENSE:L1-L21` — MIT | Excerpted report schema is MIT; no full skill card due incomplete deep read. |
| cosmix/claude-loom | `research/repos/cosmix__claude-loom/LICENSE:L1-L21` — MIT | Reference-only target; not deeply read. |
| dralgorhythm/claude-agentic-framework | No root `LICENSE`/`NOTICE` found | No license identified; paraphrase only, no excerpts. |
| first-fluke/fullstack-starter | `research/repos/first-fluke__fullstack-starter/LICENSE:L1-L21` — MIT | No per-skill exception reviewed. |
| garrytan/gstack | `LICENSE:L1-L21` — MIT; `NOTICE.md` also present | Notice records third-party files derived from Apache-2.0 and MIT works; inspect notices before reuse. |
| getsentry/skills | `research/repos/getsentry__skills/LICENSE:L1-L190` — Apache-2.0 | Section 6 trademark limitation applies. |
| github/spec-kit | `research/repos/github__spec-kit/LICENSE:L1-L21` — MIT | The reviewed command/template sources use root license. |
| hov172/secure-webapp-skill | Root `LICENSE:L1-L21` — MIT; `LICENSE.txt:L1-L28` | Attribution lists OWASP Top 10:2025 (CC BY 3.0), ASVS 5.0 (CC BY-SA 4.0), Cheat Sheet Series (CC BY 4.0), and WSTG (CC BY-SA 4.0); it names OWASP trademarks and disclaims official-project status. |
| mgiovani/cc-arsenal | `research/repos/mgiovani__cc-arsenal/LICENSE:L1-L21` — MIT | No per-skill exception found for review-security. |
| mthines/agent-skills | `research/repos/mthines__agent-skills/LICENSE:L1-L21` — MIT | Targets skipped. |
| natolitech/security-skill | `research/repos/natolitech__security-skill/LICENSE:L1-L21` — MIT | Carded commands covered by root license. |
| netresearch/security-audit-skill | `LICENSE-CC-BY-SA-4.0:L1-L19` — CC BY-SA 4.0; `LICENSE-MIT:L1-L21` — MIT | Content and code are separately licensed; paraphrase only and no excerpt, per task constraints. |
| obra/superpowers | `research/repos/obra__superpowers/LICENSE:L1-L21` — MIT | Carded skills covered by root license. |
| olanokhin/agent-security-skill | `research/repos/olanokhin__agent-security-skill/LICENSE:L1-L21` — MIT | Installation instructions download files, but do not alter the license. |
| pulumi/agent-skills | `research/repos/pulumi__agent-skills/LICENSE:L1-L201` — Apache-2.0 | Section 6 trademark limitation applies. |
| secondsky/claude-skills | `research/repos/secondsky__claude-skills/LICENSE:L1-L21` — MIT | REST API and API-authentication targets carded; requested database-schema target was not found. |
| semgrep/skills | Root `LICENSE:L1` — “Semgrep Rules License v1.0” | Custom terms, no SPDX identifier; legal review required before reuse. |
| sickn33/agentic-awesome-skills | Root `LICENSE:L1-L21` — MIT; `LICENSE-CONTENT:L1-L15` — CC BY 4.0 | Content file says original non-code text is CC BY 4.0 unless a more specific upstream license/attribution applies. The copied Supabase skill needs upstream attribution/license treatment; see lineage. |
| supabase/agent-skills | `research/repos/supabase__agent-skills/LICENSE:L1-L21` — MIT | Carded Postgres rules covered by root license. |
| trailofbits/skills | `research/repos/trailofbits__skills/LICENSE:L1-L427` — CC BY-SA 4.0 | Reference-only card produced; paraphrase only and no excerpt, per task constraints. |
| vasilyu1983/AI-Agents-public | No clone or license file; shallow-clone retry failed | License unresolved; do not reuse. |
| wshobson/agents | `research/repos/wshobson__agents/LICENSE:L1-L21` — MIT | STRIDE-analysis-patterns and three backend targets carded; other listed targets remain skipped. |

## Pre-flagged license checks

| Repository | Evidence | Status |
|---|---|---|
| anthropics/skills | No root license; numerous per-skill `LICENSE.txt` files exist (for example `skills/pdf/LICENSE.txt`). | Per-skill licensing only; check the exact skill's notice before reuse. |
| openai/skills | No root license or skill `LICENSE.txt` was found in the clone; README says each skill's license is in its own directory (`README.md:L41-L43`). | README and files are inconsistent/incomplete; do not assume a license. |
| vercel-labs/agent-skills | No root `LICENSE`; README says MIT (`README.md:L214-L216`). | Claim is not a substitute for an actual license file; not a carded target. |

## Carded material

The 54 cards comprise 48 skill cards and six packaging cards. Their sources include MIT-licensed material, Semgrep's custom license, Trail of Bits' CC BY-SA reference material, an unlicensed Dralgorhythm reference, and Agent Skills packaging (CC BY 4.0 specification text plus Apache-2.0 validator). Hov's MIT repository also attributes OWASP material under separate CC BY/CC BY-SA terms; follow its attribution notice. Semgrep remains the only carded repository with custom non-SPDX terms; obtain legal review before reuse. No excerpts were taken from CC BY-SA or unlicensed sources. The excerpt bundle uses MIT, Apache-2.0, and the attributed CC BY 4.0 specification excerpt.

