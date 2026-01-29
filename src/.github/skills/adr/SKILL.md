---
name: adr
description: Manage Architecture Decision Records (ADRs) for technical decisions. Create new ADRs with auto-populated content, review existing decisions for context, and update ADR status. Use when documenting, researching, or updating important technical choices that affect system architecture or design.
---

# ADR (Architecture Decision Record) Management

## Overview

Manage architectural decision records for technical decisions using the ADR template. Handle information gathering, template instantiation, decision workflow guidance, and ADR review to capture and track technical decisions efficiently.

You can use this skill to:
- **Create** new ADRs for technical decisions
- **Review** existing ADRs to understand past decisions
- **Update** ADR status (Proposed → Accepted/Rejected) or content

## When to Use

**Create ADRs for technical decisions that**:
- Affect system architecture, data structures, or project direction
- Have multiple viable alternatives with tradeoffs
- Need to be justified or communicated to stakeholders
- Will impact future development work
- Should be preserved for historical context

**Review existing ADRs when**:
- Starting work that may be affected by past architectural decisions
- Understanding why certain patterns or technologies are used
- Evaluating whether a past decision should be reconsidered
- Onboarding to a codebase or project area
- Researching alternatives that were previously considered and rejected

**Update existing ADRs to**:
- Change status from "Proposed" to "Accepted" after user approval
- Mark as "Rejected" if the decision is not pursued
- Mark as "Superseded" when a newer ADR replaces an old decision
- Add implementation details or consequences discovered after the decision
- Link to related work items or dependent ADRs discovered later

## Creating ADRs

### Step 1: Gather Information from Context

Before creating an ADR, extract as much information as possible from:
- **Current conversation**: Decision context, rationale, alternatives discussed
- **Git history and recent code changes**: Implementation details, affected files
- **Available documentation**: Any agent-specific files in Markdown or other format (do not read README files unless no other documentation is available)

#### Frontmatter Fields

**Required fields** (must be inferrable or explicitly provided):
- **Decision Title**: Clear, concise name for the decision
- **Context**: Problem statement—infer from conversation or project documentation
- **Decision**: The chosen solution—infer from the conversation
- **Rationale**: Key reasons for the choice—infer from discussion

**Machine-Readable Frontmatter** (helps agents scan ADRs efficiently):
- **related_item** (optional): Link to triggering issue, epic, or work item ID if available (e.g., "ITEM-003")
- **blocking** (optional): Set to `true` if this decision must be user-approved before implementation can proceed
- **affected_components** (optional): List of impacted systems (e.g., ["backend", "database"])
- **dependencies** (optional): List of prerequisite ADRs (e.g., ["ADR-001"])

**Optional narrative fields** (auto-populate if available, otherwise use `[TODO]` placeholder):
- **Author**: Retrieved from agent context (or else from `git config user.name`), falls back to "User"
- **Implementation**: Plan of action, deployment requirements
- **Alternatives**: Other options considered and why rejected
- **Stakeholders**: People involved (infer from git history or project communication)
- **Consequences**: Good, bad, and neutral impacts

**Workflow Principle**: Generate the ADR immediately with inferred content. Do NOT block on missing optional fields. Use `[TODO: description]` placeholders for any information that cannot be inferred. The goal is to capture the decision now; refinement can happen later.

### Step 2: Generate ADR Document

Create the ADR using template instantiation. The process will automatically:
- Determine the next ADR number from existing ADR files in the project
- Auto-populate date, author, and other fields marked with `auto` in the template schema
- Prompt for required fields that cannot be inferred

Additional requirements:
- Generate the complete document in Markdown format
- Use precise, unambiguous language
- Document all alternatives with clear rejection rationale (use `[TODO]` if not discussed)
- Structure content for both machine parsing and human reference
- Mark any inferred content with `[Inferred]` tag so reviewers know what to verify

#### ADR Naming Convention

Format: `adr-NNN-[title-slug].md`

For example: `adr-001-database-selection.md`

**Rules**:
- All lowercase
- Convert spaces to single hyphens
- Remove special characters
- Keep the title slug concise (3-4 words max)

### Step 3: Present ADR to User with Decision Guidance

After generating the ADR, present it to the user with a summary that highlights the decision's impact:

```
ADR-NNN created: [Title]
- Status: Proposed
- Blocking: [yes/no] — implementation [may/may not] proceed without approval
- Related work item: [ITEM-XXX or none]
- Dependencies: [ADR-XXX, ADR-YYY or none]
- Affected components: [list or none]

Auto-populated: Context, Decision, Rationale
Marked [TODO]: [list any placeholder sections]

Would you like to:
1. Accept this decision (→ marks status as "Accepted")
2. Reject this decision (→ marks status as "Rejected")
3. Keep as Proposed and review later
4. Request changes or more analysis
```

**Key guidance for blocking decisions**:
- If `blocking: true`, emphasize that implementation should wait for user approval before proceeding
- If `blocking: false`, clarify that implementation can proceed while the user reviews

## Reviewing Existing ADRs

When researching past decisions:

1. **Locate ADR files** in the project's ADR directory (commonly `docs/adr/`, `.github/docs/adr/`, or `adr/`)
2. **Scan ADR titles and numbers** to find relevant decisions
3. **Read key sections**:
   - **Context**: Why the decision was needed
   - **Decision**: What was chosen
   - **Rationale**: Why this choice was made
   - **Alternatives**: What else was considered and why rejected
   - **Consequences**: Expected impacts (good, bad, neutral)
4. **Check status**: Proposed, Accepted, Rejected, or Superseded
5. **Review metadata**: Related items, affected components, dependencies
6. **Check date**: Consider if the decision context is still valid

## Updating ADR Status

When a decision is finalized or changes:

1. **Locate the ADR file** to update
2. **Update the status field** in the frontmatter:
   - `Proposed` → `Accepted` (user approves and implementation proceeds)
   - `Proposed` → `Rejected` (user declines, alternative chosen)
   - `Accepted` → `Superseded` (newer ADR replaces this decision, reference the new ADR number)
3. **Add superseded reference** if applicable:
   ```yaml
   status: Superseded
   superseded_by: ADR-042
   ```
4. **Update date fields** if the template includes a "Last Updated" or "Decision Date" field
5. **Add notes** in the Consequences or Implementation section if new information emerged
6. **Commit the update** with a message like "Update ADR-003: mark as accepted"

## Field Inference Guidelines

When inferring values for frontmatter:
- **related_item**: Look for any reference to project work items, issues, or epics in conversation or documentation
- **blocking**: Assess whether user approval is needed before implementation. Set to `true` if the decision affects core architecture, data structures, or project direction
- **affected_components**: List all systems impacted by this choice (backend, frontend, database, deployment, etc.)
- **dependencies**: Check if this decision relies on prior ADRs or makes assumptions they validate

## Best Practices

- **Capture early**: Create ADRs when the decision is made, not later
- **Be pragmatic**: Use `[TODO]` for missing information rather than blocking ADR creation
- **Infer intelligently**: Extract as much as possible from context; tag inferred content for verification
- **Link decisions**: Reference related work items, dependencies, and affected components
- **Update status**: Move from "Proposed" to "Accepted" or "Rejected" based on user feedback
- **Maintain traceability**: Link back to issues, commits, or discussions that led to the decision

## Example ADR Creation

**Context**: User discussing whether to use SQLite or PostgreSQL for data storage.

**Actions**:
1. Review conversation for decision context, alternatives discussed, rationale
2. Check project backlog or documentation for related work items (e.g., ITEM-007: "Database setup")
3. Determine next ADR number (e.g., ADR-003)
4. Create ADR file using project conventions (e.g., `adr-003-use-sqlite-for-storage.md`)
5. Auto-populate:
   - Title: "Use SQLite for Data Storage"
   - Context: "[Inferred] Project needs persistent storage with minimal operational overhead"
   - Decision: "[Inferred] Use SQLite for initial implementation"
   - Rationale: "[Inferred] Simpler setup, embedded database, sufficient for current scale"
   - Alternatives: "PostgreSQL (more features but higher complexity), MariaDB (similar tradeoffs)"
6. Present to user with decision options

## Safety Guidelines

- Never overwrite existing ADRs without explicit user confirmation
- Always preserve the template frontmatter schema when creating new ADRs (the first YAML block in the template should NOT be included in the generated ADR)
- Verify ADR numbers or IDs follow the project's naming conventions sequentially
- Tag all inferred content appropriately so users can verify assumptions
- For blocking decisions, clearly communicate approval requirements before proceeding with implementation
- When project context is unavailable, ask the user for relevant information rather than making unsupported assumptions

## Template Reference

The complete template with all sections and examples is available at [assets/adr.template.md](assets/adr.template.md).
