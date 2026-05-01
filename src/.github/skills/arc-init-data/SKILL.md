---
name: arc-init-data
description: Gather git and repository information without user interaction. Returns JSON data for programmatic use by agents.
python_dependencies: []
---

# ARC Session Data Gathering

## Overview

Pure data-gathering skill that collects git and repository information without any user interaction. Designed for use by read-only agents that need session context.

## When to Use

- When a read-only agent needs git/repo information
- When you need raw session data without display formatting
- As a prerequisite for other operations that need context

## What Gets Gathered

1. **Git Username**: From `git config user.name` (falls back to "User")
2. **Git Email**: From `git config user.email`
3. **Current Branch**: From `git branch --show-current`
4. **Repository Root**: From `git rev-parse --show-toplevel`
5. **Uncommitted Changes**: Working directory and staged changes status
6. **Branch Sync Status**: Remote tracking status for all branches

## Usage

### Step 1: Run Data Gathering Script

Execute the Python script and capture its JSON output:

```bash
python3 .github/skills/arc-init/scripts/init_session.py
```

### Step 2: Output Structure

The script outputs JSON to stdout with this structure:

```json
{
  "git_username": "string",
  "git_email": "string",
  "current_branch": "string",
  "repo_root": "string",
  "uncommitted_changes": {
    "has_changes": bool,
    "staged_count": int,
    "unstaged_count": int,
    "summary": "string"
  },
  "branch_sync": {
    "current_branch_status": "synced|ahead|behind|diverged|no_tracking|unknown",
    "out_of_sync_branches": [...],
    "fetch_failed": bool,
    "fetch_error": "string or null"
  },
  "warnings": [...]
}
```

### Step 3: Return or Store Output

The skill execution is complete. The invoking agent decides what to do with the JSON output (display it, write to file, parse and use directly, etc.).

## Example Use Cases

- **context-builder**: Get git status for session context summary
- **Planning agents**: Check branch state before proposing changes
- **Documentation agents**: Include repo/branch info in generated docs

## Notes

- This skill is READ-ONLY - no user interaction, no display formatting
- For interactive session initialization, use `arc-init-session` skill instead
- Both skills use the same underlying Python script
