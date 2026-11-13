# Repo: agentskills__agentskills
HEADER: path=/home/syed-jalal/dev/wings/research/repos/agentskills__agentskills/README.md | commit=83021e2be457a9b6679148719c1f6074f0ad975e | license=LICENSE

# Agent Skills

A standardized way to give AI agents new capabilities and expertise.

## What are Agent Skills?

Agent Skills are a lightweight, open format for extending AI agent capabilities with specialized knowledge and workflows.

At its core, a skill is a folder containing a `SKILL.md` file. This file includes metadata (`name` and `description`, at minimum) and instructions that tell an agent how to perform a specific task. Skills can also bundle scripts, reference materials, templates, and other resources.

```
my-skill/
├── SKILL.md          # Required: metadata + instructions
├── scripts/          # Optional: executable code
├── references/       # Optional: documentation
├── assets/           # Optional: templates, resources
└── ...               # Any additional files or directories
```

## How do Agent Skills work?

Agents load skills through progressive disclosure, in three stages:

1. Discovery: At startup, agents load only the name and description of each available skill.
2. Activation: When a task matches a skill's description, the agent reads the full `SKILL.md` instructions.
3. Execution: The agent follows the instructions, optionally executing bundled code or loading referenced files.

