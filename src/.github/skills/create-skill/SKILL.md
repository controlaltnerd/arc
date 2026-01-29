---
name: create-skill
description: Create new agent skills with proper structure, naming, and organization, following the Agent Skills open standard.
---

# Creating Agent Skills

## Overview

Create new agent skills—portable, task-specific capabilities that agents load on-demand. Skills provide specialized workflows with supporting resources and follow the Agent Skills open standard for cross-platform compatibility.

## When to Use This Skill

Use this skill when you need to create a new agent skill:

- Extracting reusable workflows from agent instructions
- Standardizing a common task across multiple projects
- Creating specialized capabilities for specific domains
- Building portable skills that can be shared across teams
- When agent instructions contain detailed procedural knowledge that could be modularized
- Creating task-specific capabilities that agents should load on-demand

**Do NOT use this skill for**:
- Creating one-off instructions (use agent instructions instead)
- Building persona-based workflows (use agents instead)
- Always-applied guidelines (use instruction files instead)

## Skill Structure

Skills are self-contained directories containing:

```
.github/skills/
└── skill-name/              # Directory name matches skill name
    ├── SKILL.md             # Required: skill definition
    ├── scripts/             # Optional: automation scripts
    │   └── helper.sh
    ├── references/          # Optional: additional documentation
    │   └── guide.md
    └── assets/              # Optional: templates, data files, images
        └── template.md
```

### Progressive Disclosure

Skills use progressive disclosure for efficient context usage:

1. **Discovery** (metadata only): Agent reads skill names/descriptions from frontmatter
2. **Loading** (full instructions): When relevant, full SKILL.md instructions load
3. **Resources** (on-demand): Scripts, references, and assets load only when referenced

Keep SKILL.md under 500 lines. Move detailed reference material to `references/` directory.

## Creating a New Skill

### 1. Identify the Workflow

Before creating a skill:

1. **Verify it's reusable**: Will this workflow be needed repeatedly or across projects?
2. **Check existing skills**: Does a skill already exist that could be extended instead?
3. **Define scope**: What specific task or capability should this skill handle?
4. **Identify resources**: Will it need templates, scripts, or reference documentation?

### 2. Choose a Skill Name

**Naming rules** (per Agent Skills spec):
- Lowercase letters, numbers, and hyphens only
- Must not start or end with hyphen
- Must not contain consecutive hyphens (`--`)
- Maximum 64 characters
- Must match directory name exactly

**Examples**:
- ✅ `create-test-spec`, `log-work-session`, `test-api`
- ❌ `Create-Test-Spec` (uppercase), `-api` (starts with hyphen), `test--api` (consecutive hyphens)

**Naming conventions**:
- **Single-action skills**: Use noun-verb or verb-noun pairs (whichever order is more natural). Even if the action's inputs and outputs vary, if the skill performs one conceptual action, use this format. Examples:
  - `git-commit`
  - `process-pdf`
  - `code-review`
  - `create-skill`
- **Multi-action skills**: If a skill encompasses multiple closely related actions (like create, update, review), name it for the technology, product, or concept it pertains to. Examples:
  - `memory` (not `update-memory`)
  - `work-session` (not `create-work-session`)
  - `adr` (not `create-adr`)

### 3. Use the Skill Template

The template is located at [assets/skill.template.md](assets/skill.template.md).

**Required frontmatter fields**:

```yaml
---
name: skill-name                    # Must match directory name
description: Brief description...   # Max 1024 chars, describes what and when
---
```

**Optional frontmatter fields**:

```yaml
---
name: skill-name
description: Brief description...
python_dependencies:                # Python packages required by skill scripts
  - requests>=2.31.0
  - pyyaml>=6.0.0
---
```

**Python Dependencies**:
- List any Python packages that skill scripts need to import
- Use standard pip/uv version specifiers (e.g., `>=2.0.0`, `~=1.5`)
- Include only non-standard-library packages
- If skill has no Python dependencies, omit field or use empty list `[]`

**Key principle**: The description should help agents decide when to load the skill. Include specific keywords and scenarios.

**Good description**:
```yaml
description: Manage test specifications using Given/When/Then format. Create new specs, update with test results, and review for context. Use when defining acceptance criteria, updating test status, or researching expected behavior.
```

**Poor description**:
```yaml
description: Helps with testing.
```

### 4. Structure the Skill Content

Follow this recommended structure:

#### Overview
- Brief explanation of what the skill does
- Bulleted list of capabilities (Create, Update, Review)

#### When to Use This Skill
- Separate subsections for creating, updating, reviewing
- Clear do/don't guidance
- Specific scenarios and triggers

#### Main Content Sections
Organize by workflow:
- **Managing Existing [Items]** (update/review workflows)
- **Creating New [Items]** (creation workflow with numbered steps)

#### Best Practices
```markdown
## Best Practices

### DO

- ✅ Specific best practice
- ✅ Another best practice

### DON'T

- ❌ Common pitfall to avoid
- ❌ Another anti-pattern
```

#### Template Reference
If the skill includes a template in `assets/`:
```markdown
## Template Reference

The complete template with all sections and guidance is available at [assets/template-name.md](assets/template-name.md).
```

### 5. Create Directory Structure

1. **Create skill directory**: `.github/skills/[skill-name]/`
2. **Create SKILL.md** from template in that directory
3. **Add optional directories** only if needed:
   - `scripts/` - Executable automation scripts
   - `references/` - Additional documentation loaded on-demand
   - `assets/` - Templates, data files, images

### 6. Add Supporting Resources

**Templates** (`assets/`):
- Use for reusable file structures
- Include YAML frontmatter with placeholders to define template variables
- Reference in "Template Reference" section

**Scripts** (`scripts/`):
- Executable helpers for the skill
- Include helpful error messages
- Document dependencies clearly
- Make self-contained when possible

**References** (`references/`):
- Detailed technical documentation
- Examples and case studies
- Domain-specific guides
- Keep files focused and scannable

### 7. Write Clear Instructions

**Be specific**: Use concrete examples, not generic descriptions
- ❌ "Update the status when things change"
- ✅ "Update status from `planned` → `implemented` when tests are written"

**Be actionable**: Each section should have clear next steps
- Use numbered lists for sequences
- Use bullet points for guidelines
- Include example commands and outputs

**Consider the audience**: Agents will follow these instructions literally
- Avoid ambiguity
- Define terms when needed
- Explain non-obvious reasoning

**Keep it scannable**: Use headings, bullets, and formatting
- Break up long paragraphs
- Use code blocks for examples
- Highlight important warnings or notes

## Skill Naming Conventions

Skills follow consistent naming patterns based on their scope:

**Single-action skills** (one conceptual action, regardless of input/output variation):
- Use noun-verb or verb-noun format
- Examples: `git-commit`, `process-pdf`, `code-review`, `create-skill`

**Multi-action skills** (multiple closely related actions):
- Named for the technology, product, or concept they pertain to
- Examples: `memory` (not `update-memory`), `work-session` (not `create-work-session`), `adr` (not `create-adr`)

**Rationale**: Single-action skills describe what they do, while multi-action skills are named for what they manage to encompass their full lifecycle.

## Best Practices

### DO

- ✅ Keep SKILL.md under 500 lines; use `references/` for detailed content
- ✅ Write descriptions that help agents decide when to load the skill
- ✅ Include concrete examples with real-world data
- ✅ Use progressive disclosure: metadata → instructions → resources
- ✅ Follow the Agent Skills open standard for portability
- ✅ Test skills by actually using them before finalizing
- ✅ Include both best practices (DO) and anti-patterns (DON'T)
- ✅ Reference templates and resources with relative paths
- ✅ Check if a similar skill already exists before creating a new one
- ✅ Define clear scope and boundaries for the skill

### DON'T

- ❌ Create skills for one-off tasks (use agent instructions instead)
- ❌ Mix multiple unrelated workflows in a single skill
- ❌ Write vague descriptions like "Helps with documentation"
- ❌ Forget to match skill name with directory name exactly
- ❌ Use uppercase letters or special characters in skill names
- ❌ Create deeply nested resource references (keep one level deep)
- ❌ Skip the "When to Use" section (critical for agent discovery)

## Template Reference

The complete skill template with all sections and guidance is available at [assets/skill.template.md](assets/skill.template.md).
