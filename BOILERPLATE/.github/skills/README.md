# Skills Directory

Agent Skills are portable, task-specific capabilities that AI agents can load on-demand. Unlike rules (always applied) or agents (persona-based), skills provide specialized workflows with supporting resources.

## What Are Skills?

Skills are self-contained directories containing:
- **SKILL.md** - Instructions and guidelines (required)
- **scripts/** - Automation helpers (optional)
- **references/** - Additional documentation (optional)
- **assets/** - Templates, data files, images (optional)

## Skills vs Other ARC Components

| Component | Scope | Content | Activation |
|-----------|-------|---------|------------|
| Instructions | Always applied (or glob-matched) | Guidelines only | Automatic |
| Agents | Persona-based orchestration | Role + behaviors | User-invoked via `@agent` |
| Prompts | User-triggered workflows | Single-use instructions | Manual `/` command |
| **Skills** | Task-specific capabilities | Instructions + resources | Auto-detected from context |

## How Skills Work

Skills use progressive disclosure for efficient context usage:

1. **Discovery** - Agent reads skill names/descriptions from frontmatter
2. **Loading** - When relevant, full SKILL.md instructions load
3. **Resources** - Scripts and examples load only when referenced

## Creating Skills

Use the skill template to create new skills:

```
/.github/templates/skill.template.md
```

### Directory Structure

```
.github/skills/
├── README.md                 # This file
├── my-skill/
│   ├── SKILL.md              # Required: skill definition
│   ├── scripts/              # Optional: automation scripts
│   │   └── helper.sh
│   ├── references/           # Optional: additional documentation
│   │   └── guide.md
│   └── assets/               # Optional: templates, data files, images
│       └── template.md
```

### Naming Conventions

- Skill directory: lowercase with hyphens (e.g., `webapp-testing`)
- Skill name in frontmatter: must match directory name
- Maximum 64 characters for skill name

## Portability

Skills are part of the [Agent Skills open standard](https://agentskills.io/) and work across various platforms, IDEs, and LLMs.

## Finding Shared Skills

- [github/awesome-copilot](https://github.com/github/awesome-copilot) - Community collection
- [anthropics/skills](https://github.com/anthropics/skills) - Reference implementations

Always review shared skills before use to ensure they meet your security standards.
