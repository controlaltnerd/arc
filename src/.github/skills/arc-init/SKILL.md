---
name: arc-init
description: Initialize session context by gathering git configuration and repository information. DO NOT use this skill unless your instructions explicitly require it.
python_dependencies: []
---

# ARC Session Initialization

## Overview

Initialize session context automatically at the start of each conversation. This skill gathers essential information that will be available throughout the session, reducing redundant queries and providing consistent context to all agents.

## When to Use

**Automatic invocation:**
- At the start of every new conversation session
- Before processing the user's first prompt
- Invoked by the coordinator agent - DO NOT use without explicit instructions

## What Gets Initialized

The initialization script gathers:

1. **Git Username**: From `git config user.name` (falls back to "User")
2. **Git Email**: From `git config user.email` (for verification context)
3. **Current Branch**: From `git branch --show-current`
4. **Repository Root**: From `git rev-parse --show-toplevel`

This information is presented to the user as session context and kept available for other agents throughout the conversation.

## Initialization Process

### Step 0: Check and Install Python Dependencies

Ensure all Python dependencies are available:

1. **Check for package manager**:
   ```bash
   which uv || which pip
   ```

2. **If neither available**, inform user:
   ```
   Python package manager not found. ARC requires 'uv' (recommended) or 'pip' to manage dependencies.
   Would you like me to install 'uv'?
   ```

3. **If user agrees**, install uv:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

4. **Scan all skills** for dependencies:
   - Read frontmatter from all `.github/skills/*/SKILL.md` files
   - Extract `python_dependencies` lists
   - Aggregate and deduplicate dependencies

5. **Update arc-requirements.txt**:
   - Write all dependencies to `.github/arc-requirements.txt`
   - Include header comment: `# ARC Framework Infrastructure Dependencies`
   - Add comment: `# Auto-generated from skill frontmatter - do not edit manually`

6. **Install dependencies**:
   ```bash
   # Prefer uv if available
   uv pip install -r .github/arc-requirements.txt
   
   # Fallback to pip
   pip install -r .github/arc-requirements.txt
   ```

7. **Handle errors gracefully**:
   - If install fails, warn user but continue with session
   - Skills requiring missing packages will fail when invoked
   - User can manually install dependencies later

### Step 1: Run Initialization Script

Execute the Python script that gathers git and repository information:

```bash
python .github/skills/arc-init/scripts/init_session.py
```

The script outputs JSON with the gathered information.

### Step 2: Parse and Store Context

Extract the following from the script output:
- `git_username`: User's git configured name
- `git_email`: User's git configured email
- `current_branch`: Active git branch
- `repo_root`: Repository root directory
- `warnings`: Any configuration issues detected

### Step 3: Present Context to User

Show the user what context was initialized:

```
Session initialized:
- User: [git_username]
- Branch: [current_branch]
- Repository: [repo_root]
```

### Step 4: Handle Missing Configuration

If `git_username` is not configured:
1. Fall back to "User" for the session
2. Warn the user with: "Git username not configured. Currently using 'User' for attribution. How would you like me to refer to you?"
3. If user provides a name, use it for the session. Ask the user if they would like the git global config to be updated with that name.
4. If user agrees, run the following command, substituting `[NAME]` for the user-provided name:

```bash
git config --global user.name "[NAME]"
```

5. Verify the name is correctly set:

```bash
git config --global user.name
```

### Step 5: Make Context Available

Keep the initialized context available throughout the session. Other agents and skills can reference:
- **Git Username**: For author attribution in documentation
- **Current Branch**: For work session and commit tracking
- **Repository Root**: For file path resolution

## Integration with Other Skills

Other skills that need user attribution should reference the session context:

**work-session skill:**
```markdown
**Getting Author Name:**
Use the git username from arc-init session context. If arc-init has not run or returned "User", use "User" as fallback.
```

**adr skill:**
```markdown
**Author Field:**
Populate with git username from arc-init session context. Default to "User" if not available.
```

## Script Output Format

The initialization script outputs JSON:

```json
{
  "git_username": "Jane Developer",
  "git_email": "jane@example.com",
  "current_branch": "feature/new-feature",
  "repo_root": "/Users/jane/git/project",
  "warnings": []
}
```

Or with warnings if configuration is missing:

```json
{
  "git_username": "User",
  "git_email": "",
  "current_branch": "main",
  "repo_root": "/Users/jane/git/project",
  "warnings": ["Git user.name not configured"]
}
```

## Error Handling

If the script fails to run:
1. Continue with session using "User" as fallback
2. Warn coordinator that initialization failed and provide details
3. Do not block user's work

If git commands fail:
1. Use sensible defaults (e.g., "User", "Unknown branch")
2. Include warnings in output
3. Continue with session

## Implementation Notes

- **Non-blocking**: Initialization failure should never prevent work
- **Silent success**: Only show output if there are warnings or errors
- **One-time per session**: Run once at session start, not repeatedly
- **No git modifications**: Never modify git config, only read it

## Best Practices

### DO

- ✅ Run initialization automatically at the start of every new conversation
- ✅ Present session context clearly to the user if any warnings exist
- ✅ Fall back gracefully to "User" if git username is not configured
- ✅ Ask the user how they'd like to be referred to if git config is missing
- ✅ Offer to update git global config if user provides a preferred name
- ✅ Keep initialized context available throughout the entire session
- ✅ Use session context in other skills (work-session, adr) for attribution
- ✅ Continue with the session even if initialization fails

### DON'T

- ❌ Block the user's work if initialization fails or git config is missing
- ❌ Modify git configuration without explicit user permission
- ❌ Re-run initialization multiple times during the same session
- ❌ Show initialization output if everything succeeded without warnings
- ❌ Fail silently - always inform user of missing configuration
- ❌ Use this skill manually - it's invoked automatically by coordinator
- ❌ Assume git is configured - always handle missing values gracefully
