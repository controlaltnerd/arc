---
name: git-push
description: Workflow for requesting and executing git push operations with user approval. Handles single and multiple commits with transparent information presentation.
---

# Git Push

## Overview

Present pending commits to the user for approval before pushing to remote repositories. Ensure transparency, gather all necessary information about what's being pushed, and handle user responses appropriately.

## When to Use

- After creating commits that need review before pushing
- When multiple commits need to be presented together for approval
- Any time commits exist locally that haven't been pushed to remote yet
- When you need explicit user approval before modifying remote state

## Workflow

### Step 1: Determine Scope

Before starting, identify what you're about to push:

```bash
git status  # Check current state
```

Determine if you have:
- **Single commit**: Standard push operation
- **Multiple commits**: Batch push operation (e.g., related changes or final sync)

### Step 2: Gather Information

For each unpushed commit, collect the following data:

**Get current branch name:**
```bash
git rev-parse --abbrev-ref HEAD
```

**Get all unpushed commits:**
```bash
git log origin/[branch]..HEAD --oneline
```
This shows commit hashes and subjects for commits that exist locally but not on remote.

**For each commit, get detailed information:**
```bash
git show --stat [commit-hash]
```
This provides:
- Full commit message
- List of changed files and modification counts

### Step 3: Format the Approval Request

Present the user with a clear, structured request. Use this template:

```
## Ready to Push

**Branch**: [branch name]
**Commits to push**: [n] commit(s)

[For each commit:]

### Commit [n]
**Hash**: [short hash, e.g., abc1234]
**Message**: [full commit message from git show]

**Files Changed**:
[one of the following:]
- If 15 or fewer files/directories: List all files with modification counts
- If more than 15 files/directories: Provide discovery command instead
```

Example with ≤ 15 files:
```
- src/auth.js (+50, -30)
- tests/auth.test.js (+120, -0)
- docs/AUTH.md (+20, -5)
```

Example with > 15 files:
``````
To see all changed files and counts, run:
```
git show --stat [commit-hash]
```
``````

### Step 4: Request Explicit Approval

Ask the user directly for approval using clear language:

```
Ready to push these changes to remote [branch]? 

Please respond with one of:
- ✅ "yes" or "approve" to proceed
- ❌ "no" or "cancel" to keep commits local
- "?" for more information about specific commits
```

### Step 5: Handle User Response

**If approved** ("yes", "approve", "proceed"):
```bash
git push origin [branch-name]
```

Then confirm success:
```
✅ [n] commit(s) pushed to remote [branch].
```

**If rejected** ("no", "cancel", "stop"):
```
❌ Push cancelled. [n] commit(s) remain local and unpushed.

Would you like to:
- Make changes and retry
- Rollback these commits
- Proceed differently
```

**If more information requested** ("?"):
- Provide the specific details requested
- Re-ask for approval after providing details

**If feedback provided** (specific concerns):
```
Understood. Before pushing, would you like to:
1. Make changes to these commits
2. Rollback and start over
3. Push with modifications (I can help amend commits)
```

Wait for user guidance before proceeding.

### Step 6: Confirm Push Status

After the user response, always provide clear status confirmation:

**On successful push:**
```
✅ Push successful!
- [n] commit(s) pushed to [branch]
- Commits are now on remote
```

**On user rejection:**
```
❌ Push declined
- [n] commit(s) remain local (not pushed)
- Changes are safe but not yet on remote
```

**On error:**
```
⚠️ Push failed
Error: [git error message]

Would you like to:
- Retry the push
- Troubleshoot the issue
- Defer pushing for now
```

## Key Principles

- **Always Ask**: Never push without explicit user approval
- **Be Transparent**: Show all relevant information (commits, files, branches) so users can make informed decisions
- **Respect User Choice**: If the user declines to push, do not push anyway
- **Show Work**: Present commit messages in full, not abbreviated
- **Manage Information**: For large numbers of files, provide discovery commands rather than cluttering the view
- **Handle Errors Gracefully**: Report git errors clearly and offer next steps

## Information Limits

To keep information digestible:

- **Commit Messages**: Always show in full
- **File Lists**: 
  - ≤ 15 files: List all with modification counts
  - \> 15 files: Provide git command to discover, don't list inline
- **Commit Count**: Show number prominently (e.g., "2 commits")
- **Branch Name**: Always display clearly

## Examples

### Example 1: Single Commit, Few Files

```
## Ready to Push

**Branch**: feat/oauth-refresh
**Commits to push**: 1 commit

### Commit 1
**Hash**: a1b2c3d
**Message**: feat(auth): add OAuth token refresh mechanism

Implements automatic token refresh for long-lived sessions with:
- Refresh token rotation
- Configurable expiry windows
- Redis-backed token storage

Closes #123

**Files Changed**:
- src/auth/oauth.js (+85, -10)
- tests/auth/oauth.test.js (+120, -0)
- docs/OAUTH.md (+35, -0)

Ready to push to remote feat/oauth-refresh? (yes/no)
```

### Example 2: Multiple Commits (Batch Push)

```
## Ready to Push

**Branch**: feat/rate-limiting
**Commits to push**: 2 commits

### Commit 1
**Hash**: abc1234
**Message**: feat(api): implement rate limiting

Adds per-IP rate limiting to API endpoints:
- 100 requests per minute baseline
- Configurable per-endpoint
- Redis-backed counters

**Files Changed**:
- src/api/middleware.js (+45, -5)
- src/api/rate-limiter.js (+120, -0)
- tests/api/rate-limiter.test.js (+95, -0)

### Commit 2
**Hash**: def5678
**Message**: docs: update API documentation for rate limiting

Updates API documentation and usage examples.

**Files Changed**:
- docs/API.md (+20, -5)
- docs/RATE_LIMITING.md (+40, -0)

Ready to push 2 commits to remote feat/rate-limiting? (yes/no)
```

### Example 3: Large Change Set

``````
## Ready to Push

**Branch**: feat/auth-overhaul
**Commits to push**: 1 commit

### Commit 1
**Hash**: xyz9999
**Message**: refactor(auth): overhaul authentication system

Comprehensive refactoring of auth system including new OAuth providers,
improved token management, and enhanced security practices.

**Files Changed**:
To see all changed files and modification counts, run:
```bash
git show --stat xyz9999
```

Ready to push to remote feat/auth-overhaul? (yes/no)
``````
