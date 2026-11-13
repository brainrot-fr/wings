# Repo: wshobson__agents
HEADER: path=/home/syed-jalal/dev/wings/research/repos/wshobson__agents/README.md | commit=9c61ab243def98f72da12abd41cfcf5bcd91af9d | license=LICENSE

## Multi-harness support

Choose the harness you use and follow its setup route. Available components depend on the installation route and the harness's capabilities.

| Tool | Installation | Components and limits |
| --- | --- | --- |
| Claude Code | Plugin marketplace | Source agents, skills, and commands; plugin-specific hooks and MCP configuration |
| OpenAI Codex CLI | Native marketplace or generated artifacts | Native source skills; generated TOML agents and commands as skills use a separate route |
| Cursor | Plugin marketplace | Source agents, skills, and commands, with curated project rules |
| OpenCode | `make install-opencode` | Generated agents, skills, and commands |
| GitHub Copilot | `make install-copilot` | Generated agent profiles and skills; commands also become invocable skills |

This repo maintains one source and uses adapters to generate each target harness format.

