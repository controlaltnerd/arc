---
template:
  name: "Agent Skill"
  version: "1.0"
placeholders:
  SKILL_NAME:
    type: string
    description: "Unique identifier for the skill (lowercase, hyphens for spaces, max 64 chars)"
    required: true
  SKILL_DESCRIPTION:
    type: string
    description: "What the skill does and when to use it (max 1024 chars)"
    required: true
  SKILL_PURPOSE:
    type: string
    description: "Detailed explanation of what the skill helps accomplish"
    required: true
  WHEN_TO_USE:
    type: string
    description: "Conditions or scenarios when this skill should be activated"
    required: true
  PROCEDURES:
    type: string
    description: "Step-by-step instructions for the agent to follow"
    required: true
  EXAMPLES:
    type: string
    description: "Example inputs and expected outputs"
    required: false
    default: ""
  RESOURCES:
    type: array
    description: "List of included scripts, reference docs, or asset files"
    required: false
    default: []
  TEMPLATE_FILE_PATH:
    type: string
    description: "Relative path from skill root to template file (e.g., 'assets/template.md')"
    required: false
    default: ""
output:
  path: "/.github/skills/{{SKILL_NAME}}/"
  naming: "SKILL.md"
---

<!-- 
TEMPLATE USAGE NOTES (delete this block when creating skill):
- Skill names must be lowercase with hyphens (e.g., webapp-testing)
- Description should be specific enough for agents to decide when to load
- Include concrete examples to demonstrate expected behavior
- Reference any scripts or resources using relative paths: [script](./scripts/helper.sh)
- Template frontmatter: do not include the first frontmatter section in generated SKILL.md
- Output frontmatter: Required metadata for skill discovery
- Best Practices: Use ✅ for DO items and ❌ for DON'T items
- Template Reference: Set TEMPLATE_FILE_PATH if skill includes a template in assets/

SKILL DIRECTORY STRUCTURE:
Skills are self-contained directories with the following structure:
  .github/skills/
  └── skill-name/              # Directory name matches skill name
      ├── SKILL.md             # Required: generated from this template
      ├── scripts/             # Optional: automation scripts
      │   └── helper.sh
      ├── references/          # Optional: additional documentation
      │   └── guide.md
      └── assets/              # Optional: templates, data files, images
          └── template.md

When creating a skill:
1. Create directory: .github/skills/{SKILL_NAME}/
2. Generate SKILL.md in that directory (this file)
3. Add optional subdirectories (scripts/, references/, assets/) only if needed
4. Reference files within the skill using relative paths in SKILL.md
-->
---
name: {{SKILL_NAME}}
description: {{SKILL_DESCRIPTION}}
---

# {{SKILL_NAME}}

## Purpose

{{SKILL_PURPOSE}}

## When to Use

{{WHEN_TO_USE}}

## Procedures

{{PROCEDURES}}

## Examples

{{EXAMPLES}}

## Best Practices

### DO

- ✅ {{Best practice item}}
- ✅ {{Best practice item}}
- ✅ {{Best practice item}}

### DON'T

- ❌ {{Anti-pattern or common mistake}}
- ❌ {{Anti-pattern or common mistake}}
- ❌ {{Anti-pattern or common mistake}}

## Template Reference

{{#if TEMPLATE_FILE_PATH}}
The complete template with all sections and guidance is available at [{{TEMPLATE_FILE_PATH}}]({{TEMPLATE_FILE_PATH}}).
{{else}}
No template file is associated with this skill.
{{/if}}
