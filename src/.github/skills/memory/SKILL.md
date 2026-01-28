---
name: memory
description: Manage project memory to capture and retrieve reusable knowledge, lessons learned, user preferences, and common pitfalls. Use when completing work sessions, learning new patterns, researching past decisions, or when users share preferences that should be remembered across sessions.
---

# Memory Management

## Purpose

This skill guides you through managing project memory—a living knowledge base that captures reusable knowledge persisting across work sessions. Memory accumulates solutions to problems, lessons learned, user and team preferences, architectural patterns, and common pitfalls.

You can use this skill to:
- **Read** memory to understand project context, patterns, and preferences
- **Update** memory to capture new learnings and knowledge
- **Curate** memory to eliminate redundancy and maintain clarity

## When to Use

**Reading memory**:
- Starting a new work session to understand project context
- Researching past decisions or patterns before implementing
- Understanding user preferences or project conventions
- Learning about known issues or common pitfalls
- Getting up to speed on active work in progress

**Updating memory**:
- Completing a work session with new learnings or patterns
- User shares preferences or settings that should be remembered
- Discovering solutions to non-trivial problems
- Identifying and documenting common pitfalls
- Learning new architectural patterns or technical decisions
- User changes work mode or other configurable preferences
- Making progress on features or fixing issues

**Curating memory**:
- When memory sections become cluttered or redundant
- When consolidating similar entries from multiple sessions
- When removing obsolete information
- When improving clarity of existing entries

## Memory Structure

Memory is organized into the following sections. Update only the sections relevant to your current work:

### Project Brief
Foundational knowledge of the project:
- Core requirements and goals
- Project scope and boundaries
- Key objectives

### Product Context
High-level product information:
- Why the project exists
- Problems it solves
- How it should work
- User experience goals

### System Patterns
Technical architecture and design:
- System architecture overview
- Key technical decisions
- Design patterns in use
- Component relationships

### Tech Context
Technology stack and setup:
- Technologies used
- Development setup
- Technical constraints
- Dependencies and tooling

### Test Strategy
Testing approach and practices:
- Testing philosophy
- Test types and coverage goals
- Testing tools and frameworks
- Quality standards

### Active Context
Current work in progress:
- Features, fixes, or tasks in progress
- Temporary blockers or dependencies
- Recent decisions and their implications
- Work that will continue in next session

### Progress
Project status and trajectory:
- What works well
- What's left to build
- Current status
- Known issues

### User Settings
User-configurable preferences that affect behavior:

- **Work Mode**: Current work mode preference (Autonomous, Orchestrated, or Supervised)
- **Agent Skills**: Whether agent skills are enabled (Enabled/Disabled)
- **Custom Subagents**: Whether background custom agent delegation is enabled (Enabled/Disabled)

## Updating User Settings

When the user changes preferences:

1. **Preserve all three items** even if only one is being changed
2. **Update only the specific item** that changed; do not overwrite the others
3. **Preserve previous values** if a setting cannot be inferred from context
4. **Mark as "Unknown"** only if this is the first session and a value cannot be inferred

**Example**:
If user changes Work Mode from "Supervised" to "Autonomous", but Agent Skills and Custom Subagents are already "Enabled":

```markdown
**Work Mode**: Autonomous
**Agent Skills**: Enabled
**Custom Subagents**: Enabled
```

Do NOT replace the entire section and lose the other two values.

## Reading Memory

When you need to understand project context:

1. **Identify what you need to know**:
   - User preferences and settings (check User Settings)
   - Current work in progress (check Active Context)
   - Architectural patterns to follow (check System Patterns)
   - Technical setup requirements (check Tech Context)
   - Known issues or pitfalls (check Progress)
   - Project goals and scope (check Project Brief)

2. **Scan relevant sections**:
   - Start with the section most relevant to your need
   - Look for specific keywords or patterns
   - Note any warnings or important callouts

3. **Apply knowledge**:
   - Follow established patterns and conventions
   - Respect user preferences documented in User Settings
   - Avoid known pitfalls documented in memory
   - Build on existing solutions rather than reinventing

## Updating Memory

### 1. Identify What to Remember

Ask yourself:
- What did we learn that would be useful in future sessions?
- Are there user preferences or settings to capture?
- Did we discover a solution to a non-obvious problem?
- Are there patterns or practices we should follow going forward?
- Is there active work that will continue in the next session?

### 2. Choose the Right Section

- **User Settings**: For work mode, feature toggles, or user preferences
- **Active Context**: For work in progress or temporary blockers
- **Progress**: For completed work, current status, or known issues
- **System Patterns**: For architectural decisions or design patterns
- **Tech Context**: For new tools, dependencies, or setup steps
- **Project Brief**: Rarely updated; only for fundamental changes to project scope
- **Product Context**: For changes in product vision or user experience goals
- **Test Strategy**: For testing philosophy or quality standards

### 3. Write Clear, Concise Entries

- **Be specific**: Include enough detail to be actionable
- **Be concise**: One or two sentences per point
- **Use bullets**: For easy scanning
- **Add context**: Explain *why* when not obvious
- **Update timestamps**: Change the "Last Updated" date at the bottom

### 4. Curate as You Update

As you add new entries:
- **Merge redundant information**: Combine similar points
- **Remove obsolete entries**: Delete outdated or no-longer-relevant items
- **Maintain consistency**: Use similar phrasing and structure across sections
- **Preserve important details**: Don't over-simplify at the cost of losing critical information

## Common Memory Management Patterns

### After Completing Work
Update **Progress** and **Active Context**:
```markdown
## Progress
- ✅ User authentication with JWT working
- 🚧 Password reset flow in progress
- ⏳ Email verification not started

## Active Context
- Password reset email template created, needs user review before implementation
```

### User Changes Preference
Update **User Settings**:
```markdown
## User Settings
**Work Mode**: Autonomous
**Agent Skills**: Enabled
**Custom Subagents**: Enabled
```

### Discovering a Pattern
Update **System Patterns**:
```markdown
## System Patterns
- All API routes use middleware chain: auth → validation → handler → error handling
- Database connections use connection pooling with max 10 connections
```

### Learning a Solution
Update **Tech Context** or **System Patterns**:
```markdown
## Tech Context
- Running tests requires `npm run test:setup` first to initialize test database
- Hot reload breaks on port 3000; use port 3001 for development
```

### Documenting a Pitfall
Add to the relevant section with clear warning:
```markdown
## Tech Context
- ⚠️ Do not use `Promise.all()` for database writes; can cause race conditions
- Use sequential writes with `for...of` loop instead
```

## Memory Location

Memory is stored at: `.github/instructions/memory.instructions.md`

Use the template at [assets/memory.template.md](assets/memory.template.md) if creating memory for the first time.

## Best Practices

### DO

- ✅ Add entries throughout work, not just at the end
- ✅ Act as editor, not duplicate writer—refine for clarity
- ✅ Merge similar entries across updates
- ✅ Keep section structure consistent
- ✅ Always update the "Last Updated" date
- ✅ If unsure whether something belongs in memory, ask the user
- ✅ Use bullets, short sentences, and clear section headers

### DON'T

- ❌ Overwriting User Settings when updating only one preference
- ❌ Adding duplicate information that already exists in memory
- ❌ Writing long paragraphs instead of concise bullets
- ❌ Forgetting to update the timestamp
- ❌ Removing Active Context when work completes (move to Progress instead)
- ❌ Adding temporary session details that won't be useful later
- ❌ Losing important context when consolidating entries

## Template Reference

The complete memory template is available at [assets/memory.template.md](assets/memory.template.md).
