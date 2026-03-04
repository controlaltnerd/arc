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
- Understanding project conventions
- Learning about known issues or common pitfalls
- Getting up to speed on active work in progress

**Reading user settings**:
- Understanding user's preferred work mode and feature toggles
- Checking personal preferences for the current user

**Updating memory**:
- Completing a work session with new learnings or patterns
- Discovering solutions to non-trivial problems
- Identifying and documenting common pitfalls
- Learning new architectural patterns or technical decisions
- Making progress on features or fixing issues

**Updating user settings**:
- User changes work mode (Autonomous/Orchestrated/Supervised)
- User enables or disables agent skills or custom subagents
- User shares personal preferences to remember

**Curating memory**:
- When memory sections become cluttered or redundant
- When consolidating similar entries from multiple sessions
- When removing obsolete information
- When improving clarity of existing entries

## Memory Structure

Memory is organized into the following sections. Update only the sections relevant to your current work:

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
Details about the project that may change over time:
- Known issues such as temporary blockers or dependencies
- Additional context surrounding the project
- Ideas that have been explored/attempted and abandoned
- Ideas that may be explored in an upcoming session

### Progress
Details about the trajectory of the project:
- Work in progress from previous sessions
- Work that the user has expressed they want to focus on in the near future
- Recent significant changes to the project (include ADR references when relevant)

## User Settings

User settings are only stored in a separate file: `.github/instructions/user-settings.instructions.md`

**User settings include**:
- **Work Mode**: Current work mode preference (Autonomous, Orchestrated, or Supervised)
- **Agent Skills**: Whether agent skills are enabled (Enabled/Disabled)
- **Custom Subagents**: Whether background custom agent delegation is enabled (Enabled/Disabled)
- **Personal Preferences**: Any user-specific preferences (editor settings, naming conventions, etc.)

**Why separate?**
User settings are user-specific and should be omitted from version control. Multiple users working on the same project may have different preferences. The user-settings file is automatically ignored by git.

## Managing User Settings

When the user changes preferences:

1. **Update `.github/instructions/user-settings.instructions.md`** (not memory)
2. **Preserve all existing settings** even if only one is being changed
3. **Update only the specific item** that changed; do not overwrite the others
4. **Update the timestamp** at the bottom of the file

**Example**:
If user changes Work Mode from "Supervised" to "Autonomous", but Agent Skills and Custom Subagents are already "Enabled":

```markdown
## Work Mode

**Current Mode**: Autonomous

## Feature Toggles

**Agent Skills**: Enabled
**Custom Subagents**: Enabled
```

To avoid harm to yourself, only edit the file in-place. Replacing the entire file risks extreme data loss.

## Reading Memory

When you need to understand project context:

1. **Identify what you need to know**:
   - User preferences and settings (check user-settings.instructions.md)
   - Architectural patterns to follow (check System Patterns in memory)
   - Technical setup requirements (check Tech Context in memory)
   - Known issues, backlogged ideas, additional context (check Active Context in memory)

2. **Scan relevant sections**:
   - Start with the section most relevant to your need
   - Look for specific keywords or patterns
   - Note any warnings or important callouts

3. **Apply knowledge**:
   - Follow established patterns and conventions
   - Respect user preferences documented in user-settings
   - Avoid known pitfalls documented in memory
   - Build on existing solutions rather than reinventing

## Updating Memory

### 1. Identify What to Remember

Ask yourself:
- What did we learn that would be useful in future sessions?
- Are there user preferences or settings to capture? (use user-settings.instructions.md)
- Did we discover a solution to a non-obvious problem?
- Are there patterns or practices we should follow going forward?
- Is there active work that will continue in the next session?

### 2. Choose the Right File and Section

**For user-specific preferences** → use `.github/instructions/user-settings.instructions.md`:
- **Work Mode**: For work mode changes
- **Feature Toggles**: For agent skills or custom subagent preferences
- **Personal Preferences**: For user-specific settings

**For project knowledge** → use `.github/instructions/memory.instructions.md`:
- **Active Context**: For known issues, backlogged ideas, additional context
- **System Patterns**: For architectural decisions or design patterns
- **Tech Context**: For new tools, dependencies, or setup steps
- **Product Context**: For changes in product vision or user experience goals
- **Test Strategy**: For testing philosophy or quality standards
- **Progress**: For project trajectory and unfinished work in progress

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
- **Preserve important details**: Avoid over-simplifying at the cost of losing critical information

### User Changes Preference
Update **user-settings.instructions.md** (NOT memory):
```markdown
## Work Mode

**Current Mode**: Autonomous

## Feature Toggles

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

### Capturing Current and Near-Future Work
Update **Progress**:
```markdown
## Progress

**In Progress**

- Authentication refactor partially complete - login flow done, password reset pending

**Upcoming Work (User Intent)**

- Add real-time notifications feature

**Project Changes**

- Shifted from REST to GraphQL API (see ADR-007); all endpoints being migrated
```

## File Locations

**Memory**: `.github/instructions/memory.instructions.md`  
Use template: [assets/memory.template.md](assets/memory.template.md)

**User Settings**: `.github/instructions/user-settings.instructions.md`  
Use template: [assets/user-settings.template.md](assets/user-settings.template.md)

## Creating Files on First Install

When creating memory or user-settings files for the first time:

1. **Check if files exist**:
   ```bash
   ls -la .github/instructions/memory.instructions.md
   ls -la .github/instructions/user-settings.instructions.md
   ```

2. **Create memory file** (if doesn't exist):
   - Copy template from `assets/memory.template.md`
   - Replace `{{LAST_UPDATED}}` with current date (YYYY.MM.DD format)
   - Save to `.github/instructions/memory.instructions.md`

3. **Create user-settings file** (if doesn't exist):
   - Copy template from `assets/user-settings.template.md`
   - Replace `{{LAST_UPDATED}}` with current date (YYYY.MM.DD format)
   - Save to `.github/instructions/user-settings.instructions.md`
   - **IMPORTANT**: This file should NOT be committed (verify it's in .gitignore)

4. **Verify .gitignore**:
   - Ensure `.github/instructions/user-settings.instructions.md` is listed in `.gitignore`
   - If not present, add it to prevent committing user-specific settings

## Best Practices

**Always do:**

- Add entries throughout work, not just at the end
- Act as editor, not duplicate writer—refine for clarity
- Merge similar entries across updates
- Keep section structure consistent
- Always update the "Last Updated" date in both memory and user-settings
- If unsure whether something belongs in memory, ask the user
- Use bullets, short sentences, and clear section headers
- Put user preferences in `user-settings.instructions.md`
- Make in-place edits to the memory file
- Avoid duplicate information that already exists in memory
- Prefer concise bullets instead of long sentences and paragraphs
- Avoid storing temporary session details that won't be useful later

## Template Reference

The complete memory template is available at [assets/memory.template.md](assets/memory.template.md).
