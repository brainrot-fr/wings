<!-- repo: agentskills/agentskills | path: docs/specification.mdx | lines: 1-160 | commit: 83021e2be457a9b6679148719c1f6074f0ad975e | license: CC BY 4.0 (docs/LICENSE) -->
<!-- SOURCE BODY -->
---
title: "Specification"
description: "The complete format specification for Agent Skills."
---

## Directory structure

A skill is a directory containing, at minimum, a `SKILL.md` file:

```
skill-name/
├── SKILL.md          # Required: metadata + instructions
├── scripts/          # Optional: executable code
├── references/       # Optional: documentation
├── assets/           # Optional: templates, resources
└── ...               # Any additional files or directories
```

## `SKILL.md` format

The `SKILL.md` file must contain YAML frontmatter followed by Markdown content.

### Frontmatter

| Field | Required | Constraints |
|-------|----------|-------------|
| `name` | Yes | Max 64 characters. Lowercase letters, numbers, and hyphens only. Must not start or end with a hyphen. |
| `description` | Yes | Max 1024 characters. Non-empty. Describes what the skill does and when to use it. |
| `license` | No | License name or reference to a bundled license file. |
| `compatibility` | No | Max 500 characters. Indicates environment requirements (intended product, system packages, network access, etc.). |
| `metadata` | No | Arbitrary key-value mapping for additional metadata (a map from string keys to string values). |
| `allowed-tools` | No | Space-separated string of pre-approved tools the skill may use. (Experimental) |

<Card>
**Minimal example:**

```markdown SKILL.md
---
name: skill-name
description: A description of what this skill does and when to use it.
---
```

**Example with optional fields:**

```markdown SKILL.md
---
name: pdf-processing
description: Extract PDF text, fill forms, merge files. Use when handling PDFs.
license: Apache-2.0
metadata:
  author: example-org
  version: "1.0"
---
```
</Card>

#### `name` field

The required `name` field:
- Must be 1-64 characters
- May only contain unicode lowercase alphanumeric characters (`a-z`, `0-9`) and hyphens (`-`)
- Must not start or end with a hyphen (`-`)
- Must not contain consecutive hyphens (`--`)
- Must match the parent directory name

<Card>
**Valid examples:**
```yaml
name: pdf-processing
```
```yaml
name: data-analysis
```
```yaml
name: code-review
```

**Invalid examples:**
```yaml
name: PDF-Processing  # uppercase not allowed
```
```yaml
name: -pdf  # cannot start with hyphen
```
```yaml
name: pdf--processing  # consecutive hyphens not allowed
```
</Card>

#### `description` field

The required `description` field:
- Must be 1-1024 characters
- Should describe both what the skill does and when to use it
- Should include specific keywords that help agents identify relevant tasks

<Card>
**Good example:**
```yaml
description: Extracts text and tables from PDF files, fills PDF forms, and merges multiple PDFs. Use when working with PDF documents or when the user mentions PDFs, forms, or document extraction.
```

**Poor example:**
```yaml
description: Helps with PDFs.
```
</Card>

#### `license` field

The optional `license` field:
- Specifies the license applied to the skill
- We recommend keeping it short (either the name of a license or the name of a bundled license file)

<Card>
**Example:**
```yaml
license: Proprietary. LICENSE.txt has complete terms
```
</Card>

#### `compatibility` field

The optional `compatibility` field:
- Must be 1-500 characters if provided
- Should only be included if your skill has specific environment requirements
- Can indicate intended product, required system packages, network access needs, etc.

<Card>
**Examples:**
```yaml
compatibility: Designed for Claude Code (or similar products)
```
```yaml
compatibility: Requires git, docker, jq, and access to the internet
```
```yaml
compatibility: Requires Python 3.14+ and uv
```
</Card>

<Note>
Most skills do not need the `compatibility` field.
</Note>

#### `metadata` field

The optional `metadata` field:
- A map from string keys to string values
- Clients can use this to store additional properties not defined by the Agent Skills spec
- We recommend making your key names reasonably unique to avoid accidental conflicts

<Card>
**Example:**
```yaml
metadata:
  author: example-org
  version: "1.0"
```
