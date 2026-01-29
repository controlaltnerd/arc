---
name: git-commit
description: Create standardized git commits using Conventional Commits specification. Analyzes diffs to determine appropriate type, scope, and message. Use when creating commits or user asks to "commit changes".
---

# Git Commit

## Overview

Create standardized, semantic git commits using the Conventional Commits specification. Analyze the actual diff to determine appropriate type, scope, and message.

## Conventional Commit Format

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

## Commit Types

| Type | Purpose |
|------|---------|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation only |
| `style` | Formatting/style changes (no logic change) |
| `refactor` | Code refactor without feature/fix |
| `perf` | Performance improvement |
| `test` | Add or update tests |
| `build` | Build system or dependency changes |
| `ci` | CI/CD or configuration changes |
| `chore` | Maintenance tasks or miscellaneous |
| `revert` | Revert a previous commit |

## Breaking Changes

Indicate breaking changes with an exclamation mark and appropriate footer:

```
# Using exclamation mark
feat!: remove deprecated API endpoint

# Using BREAKING CHANGE footer
feat: restructure authentication module

BREAKING CHANGE: session tokens now expire after 1 hour
```

## Workflow

### Step 1: Analyze Diff

Check what changes exist:

```bash
# If files are staged
git diff --staged

# If nothing staged, check working tree
git diff

# Also check overall status
git status --porcelain
```

Based on the diff, determine:
- **Type**: What kind of change is this? (feat, fix, docs, etc.)
- **Scope**: What area/component is affected? (optional but recommended)
- **Description**: One-line summary of what changed

### Step 2: Stage Files (if needed)

If nothing is staged or you want to group changes differently:

```bash
# Stage specific files
git add path/to/file1 path/to/file2

# Stage by pattern
git add *.test.*
git add src/components/*

# Interactive staging (choose hunks to stage)
git add -p
```

**Security**: Never commit secrets (.env files, credentials, private keys, API tokens).

### Step 3: Generate Commit Message

Craft the commit message following Conventional Commits:

**Subject line** (first line):
- Format: `<type>[optional scope]: <description>`
- Length: Keep under 72 characters (imperative mood, present tense, lowercase)
- No period at end

**Body** (if needed):
- Explain *what* changed and *why*, not *how*
- Wrap at 72 characters
- Separate from subject with blank line
- Use bullet points for multiple related changes

**Footer** (if needed):
- Reference issues if accessible: `Closes #123`, `Relates to #456`, `Fixes #789`
- Document breaking changes: `BREAKING CHANGE: description`
- Separate from body with blank line

**Examples**:

```
feat(auth): add OAuth token refresh mechanism

Implements automatic token refresh for long-lived sessions to improve UX.
Tokens now refresh transparently before expiry when within 15-minute window.

- Added RefreshStrategy interface
- Implemented DefaultRefreshStrategy with configurable windows
- Updated AuthClient to use new strategy

Closes #234
```

```
fix(parser): handle null values in JSON arrays

Previously threw NullPointerException when encountering null elements.
Now safely skips nulls and continues parsing.

Closes #156
```

```
docs: update installation instructions for macOS
```

### Step 4: Execute Commit

Create the commit:

```bash
# Single-line commit
git commit -m "feat(auth): add OAuth token refresh"

# Multi-line commit with body and footer
git commit -m "feat(auth): add OAuth token refresh

Implements automatic token refresh for sessions.
- Configurable refresh windows
- Transparent to calling code

Closes #234"
```

## Best Practices

- One logical change per commit
- Present tense: use "add" not "added"
- Imperative mood: "add feature" not "adds feature"
- Atomic commits: should be small enough to understand quickly but large enough to be meaningful
- Reference related work: Link to issues, tickets, related PRs, or Jira items in commit footers
- Include scope when possible to indicate affected area: `feat(api)`, `fix(ui)`, `docs(readme)`
- Write for developers new to the codebase who need context
- Include rationale for significant changes in the commit body

## Git Safety Protocol

- NEVER update git config as part of a commit workflow without explicit request
- NEVER run destructive commands (`--force`, hard reset, etc.) without explicit request
- NEVER skip hooks (`--no-verify`) without explicit request
- NEVER force push to main/master
- On hook failures, fix issues and create a NEW commit rather than amending (unless explicitly requested)
- On merge conflicts, resolve carefully and preserve both authors' intent where possible
