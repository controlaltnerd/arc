---
name: work-session
description: Manage work session summaries to document discrete units of work. Create, update, and review session documentation to capture objectives, implementation details, decisions, and outcomes. Maps to commits and provides traceability for future reference.
---

# Work Session Management

## Overview

Manage work session summaries that document discrete units of work. Work sessions provide a narrative record of what was accomplished, why decisions were made, and what comes next. They serve as historical documentation and context for future work.

You can use this skill to:
- **Create** new work session summaries at the end of sessions
- **Update** existing work sessions with additional information
- **Review** past work sessions to understand project history

## When to Use

**Creating work sessions**:
- At the end of a work session when code has been committed
- After completing a discrete unit of work (feature, fix, refactoring)
- When the user indicates session completion ("done", "wrap up", "finish session")
- Before finalizing documentation commits
- When documenting significant implementation decisions or learnings

**Updating work sessions**:
- When additional commits are made to the same logical unit of work
- When test results become available after initial documentation
- When memory updates or next steps need refinement
- When compliance information needs to be added

**Reviewing work sessions**:
- When understanding the history of a feature or component
- When onboarding to a codebase or project area
- When investigating why certain decisions were made
- When preparing context for new related work

**Do NOT use for**:
- Work that hasn't been committed yet
- Minor documentation-only changes
- Sessions where no code was changed

## Work Session Structure

Work session documents capture:
- **Objective**: What the session aimed to accomplish
- **What Was Implemented**: Major changes and decisions
- **Technical Details**: Key commands, APIs, design notes
- **Benefits Achieved**: Measurable improvements
- **Compliance**: Alignment with project standards
- **Files Changed**: Created and modified files
- **Next Steps**: Follow-up actions
- **Tests**: Test specifications and results
- **Verification Log**: Commands run and outputs
- **Memory Updates**: Checklist for memory curation

## Managing Existing Work Sessions

### Updating a Work Session

When you need to update an existing work session:

1. **Locate the work session file** in the work sessions directory
2. **Identify what needs updating**:
   - Additional commits made to the same feature
   - Test results that came in after initial documentation
   - Updated next steps based on new information
   - Additional files created or modified
3. **Update relevant sections**:
   - Add new commits to a "Related Commits" section if tracking multiple
   - Update test results with new coverage or passing/failing status
   - Revise next steps if priorities changed
   - Add to verification log if new tests were run
4. **Update the Last Updated timestamp** if the template includes one
5. **Commit the update** with a message like "Update work session: [descriptor]"

### Reviewing Work Sessions

When researching past work:

1. **Search by date or descriptor** to find relevant sessions
2. **Check commit hashes** to see the actual code changes
3. **Review technical details** for implementation patterns and decisions
4. **Check next steps** to see if follow-up work was planned
5. **Look at verification logs** to understand what testing was done

## Creating New Work Sessions

### 1. Verify Prerequisites

Before creating a work session:

1. **Code has been committed**: Work session references the code commit (not the documentation commit)
2. **Work is complete or at a stopping point**: Session represents a discrete unit
3. **Changes are meaningful**: Not just trivial documentation updates

### 2. Gather Session Information

Collect the following information:

**Required**:
- Session descriptor (1-2 words describing the work, e.g., "user-auth", "api-refactor")
- Current date
- Git branch name
- Commit hash (of the code commit, not the documentation commit)
- Status (Complete/In Progress/Blocked)

**Auto-discoverable**:
- Human contributor name (from agent context, or else from `git config user.name`, falls back to "User")
- Files created (from git diff)
- Files modified (from git diff)
- Branch name (from agent context, or else from `git branch --show-current`)
- Commit hash (from `git rev-parse --short HEAD`)

**From work session**:
- Objective (what was the goal?)
- Implementation details (what changed?)
- Technical decisions (why these choices?)
- Benefits achieved (what improved?)
- Test results (what was tested?)
- Next steps (what comes next?)

### 3. Use the Work Session Template

The template is located at [assets/work-session.template.md](assets/work-session.template.md). The copy you create should be named with a sequential prefix according to existing files in its destination folder, for example:

```
001-SEED-SUMMARY.md
002-PLAN-PROJECT.md
003-BEGIN-UX.md
```

**Template Frontmatter** (do not include in output):
The template's first frontmatter section defines placeholders; do not include it in generated work session documents.

**Critical Fields**:

```yaml
SESSION_DESCRIPTOR: Brief description (e.g., "JWT Authentication", "UI Refactor")
DATE: Session date in YYYY.MM.DD format (use current date)
BRANCH_NAME: Git branch name
COMMIT_HASH: Short commit hash of the CODE work (not documentation commit)
STATUS: "Complete" | "In Progress" | "Blocked"
FILES_CREATED_COUNT: Number of files created
FILES_MODIFIED_COUNT: Number of files modified
HUMAN_CONTRIBUTOR: From `git config user.name`, defaults to "User"
AGENT_NAME: AI agent name (e.g., "GitHub Copilot")
```

**Important Note on Commit Hash**:
The commit hash should reference the **code work commit**, not the documentation commit that includes the work session file itself. Get the commit hash before creating the work session document.

### 4. Populate Template Sections

#### Objective (1-2 sentences)
- Start with user's stated goal
- Refine to be clear and concise
- **User approves** this section

**Example**:
```markdown
## Objective

Implement JWT-based authentication for API endpoints with refresh token rotation.
```

#### What Was Implemented
- Concise bullet per major change or decision
- Note which collaborator (agent vs human) drove each item when helpful
- Focus on **what**, not **how**

**Example**:
```markdown
## What Was Implemented

1. JWT authentication middleware with token validation
2. Refresh token rotation mechanism
3. Login/logout endpoints with secure cookie handling
4. User session management in Redis
```

#### Technical Details
- Key commands, APIs, or design notes
- Information needed for future developers
- Non-obvious implementation choices

**Example**:
```markdown
## Technical Details

- JWT tokens expire after 15 minutes, refresh tokens after 7 days
- Used `jsonwebtoken` library for token generation/validation
- Redis stores refresh tokens with automatic expiration
- Secure cookies with `httpOnly`, `sameSite: strict`, and `secure` flags
```

#### Benefits Achieved
- Measurable improvements or reduced risk
- Tie to project goals or roadmap priorities when possible
- **Agent drafts, user approves**

**Example**:
```markdown
## Benefits Achieved

1. Secure, stateless authentication that scales horizontally
2. Reduced session storage requirements by 80%
3. Improved security with automatic token rotation
4. Compliance with OAuth 2.0 best practices
```

#### Compliance
Document alignment with project standards:

```markdown
## Compliance

- Follows authentication patterns defined in System Patterns
- Aligns with security requirements in SPEC.md
- Addresses security concern R-012 from ROADMAP.md
- Uses consistent error handling per AGENTS.md guidelines
```

#### Files Created/Modified
Auto-populate from git diff:

```bash
git diff --name-status <previous-commit> HEAD
```

List files with paths:
```markdown
## Files Created (3)

1. src/auth/jwt.middleware.ts
2. src/auth/refresh.service.ts
3. tests/auth/jwt.test.ts

## Files Modified (5)

1. src/routes/auth.routes.ts
2. src/config/redis.config.ts
3. package.json
4. README.md
5. .env.example
```

#### Next Steps
- Brief follow-up actions
- Items for next session
- **Agent suggests, user approves**

```markdown
## Next Steps

- Add password reset flow with email verification
- Implement rate limiting on login endpoint
- Add OAuth social login (Google, GitHub)
```

#### Tests
Document test specifications and results:

```markdown
## Tests

**Test Specifications**: docs/tests/jwt-authentication.md
**Test Files**: tests/auth/jwt.test.ts, tests/auth/refresh.test.ts
**Test Results**: 24 tests passing, 0 failing
**Coverage**: 87% for auth module
```

#### Verification Log
Commands run during session with output summaries:

```markdown
## Verification Log

- `npm test -- auth`: All 24 tests passing
- `npm run lint`: No errors
- `curl -X POST /api/login`: 200 OK, returns valid JWT
- `curl -H "Authorization: Bearer <token>" /api/protected`: 200 OK
```

#### Memory Updates
Checklist for post-session memory curation:

```markdown
## Memory Updates
- [ ] Document JWT authentication pattern in System Patterns
- [ ] Add Redis session storage to Tech Context
- [ ] Update Progress: Authentication complete
- [ ] Remove authentication task from Active Context
```

### 5. File Naming and Placement

**Location**: Ask the user where work sessions should be stored (common: `docs/work-sessions/`, `.github/docs/work-sessions/`)

**Naming Convention**: 
```
YYYY.MM.DD-descriptor.md
```

Where:
- `YYYY.MM.DD`: Session date
- `descriptor`: 1-2 words similar to commit message (use kebab-case)

**Examples**:
- `2026.01.28-jwt-auth.md`
- `2026.01.28-ui-refactor.md`
- `2026.01.28-bug-fix.md`

### 6. Session-to-Commit Mapping

**General Rule**: One work session per code commit

**Multiple Commits in Session**:
- If multiple code commits are made (excluding documentation commits), create multiple session files
- Each session file references its specific code commit
- Sessions can reference each other for continuity

**Example**:
```
Code commits:
- abc1234: Implement authentication endpoints
- def5678: Add refresh token rotation

Work sessions:
- 2026.01.28-auth-endpoints.md (references abc1234)
- 2026.01.28-token-rotation.md (references def5678)
```

### 7. User Approval Process

Before finalizing the work session:

1. **Present draft**: Share the complete work session document
2. **Review strategic sections**: Ask user to approve Objective, Benefits, Next Steps
3. **Confirm completeness**: "Does this accurately capture the work completed?"
4. **Verify status**: Confirm whether status is Complete, In Progress, or Blocked
5. **Get explicit approval**: "Ready to commit this work session documentation?"

### 8. Commit Work Session Separately

**Important**: The work session document is committed separately from the code work:

1. Code work is committed first (this generates the commit hash referenced in the session)
2. Work session document is created with reference to that commit
3. Work session document is committed separately as housekeeping

This avoids self-referential commit tracking.

## Population Timing Guide

| Field | When | Who |
|-------|------|-----|
| Descriptor | Session start | User provides |
| Date | Session start | Agent (auto) |
| Branch | Session start | Agent (from git) |
| Commit | Session end | Agent (after code commit, before docs) |
| Status | Session end | Agent (reflects outcome) |
| Objective | Session start | User states, agent refines |
| What Was Implemented | During work | Agent (running notes) |
| Technical Details | During work | Agent (captures as work progresses) |
| Benefits | Session end | Agent drafts, user approves |
| Compliance | Session end | Agent verifies |
| Files | Session end | Agent (from git diff) |
| Next Steps | Session end | Agent suggests, user approves |
| Tests | Session end | Agent documents |
| Verification Log | During + end | Agent (as tests run) |

## Best Practices

### DO

- ✅ Add notes during work, not just at the end
- ✅ One or two sentences per point
- ✅ List specific commands that were run
- ✅ Reference test specifications and results
- ✅ Don't finalize without user review of strategic sections
- ✅ Use current date in YYYY.MM.DD format
- ✅ Commit hash is for code work, not documentation 

### DON'T

- ❌ Create work session before code is committed
- ❌ Include documentation commit hash instead of code commit hash
- ❌ Write long paragraphs instead of concise bullets
- ❌ Skip user approval for strategic sections
- ❌ Miss test results or verification commands
- ❌ Forget to link to related documentation
- ❌ Bypass memory update checklist

## Template Reference

The complete work session template with all sections and guidance is available at [assets/work-session.template.md](assets/work-session.template.md).
