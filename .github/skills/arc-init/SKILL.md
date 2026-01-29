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
5. **Branch Sync Status**: Remote tracking status for all branches
   - Current branch sync state (ahead/behind/diverged/synced)
   - List of out-of-sync branches
   - Suggested commands to resolve sync issues

This information is presented to the user as session context and kept available for other agents throughout the conversation.

NOTE: When instructed to display a message to the user, DO NOT deviate from the provided message.

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
python3 .github/skills/arc-init/scripts/init_session.py
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

**Display Branch Sync Status (if out of sync):**

If `branch_sync.current_branch_status` is NOT "synced" or "unknown", display sync information for the current branch:

**For "behind" status:**
```
🔄 **Branch Sync Status**

Current Branch: `[current_branch]` is **behind** `[tracking]` by [behind] commit(s)
├─ Impact: Your local branch is missing [behind] commit(s) from the remote
├─ Fix: `git pull --ff-only`
└─ Result: Fast-forward your branch to include the [behind] new commit(s) from remote
```

**For "ahead" status:**
```
🔄 **Branch Sync Status**

Current Branch: `[current_branch]` is **ahead of** `[tracking]` by [ahead] commit(s)
├─ Impact: You have [ahead] local commit(s) not yet pushed to the remote
├─ Fix: `git push`
└─ Result: Push your [ahead] local commit(s) to the remote
```

**For "diverged" status:**
```
🔄 **Branch Sync Status**

Current Branch: `[current_branch]` has **diverged** from `[tracking]`
├─ Local: [ahead] commit(s) ahead
├─ Remote: [behind] commit(s) behind
├─ Impact: Your branch and the remote have different commits
├─ Fix: `git pull --rebase` or `git pull --merge`
└─ Result: Integrate remote changes with your local commits (may require conflict resolution)
```

**For "no_tracking" status:**
```
🔄 **Branch Sync Status**

Current Branch: `[current_branch]` has **no remote tracking** configured
├─ Impact: Cannot sync with remote - no upstream branch set
├─ Fix: `git push -u origin [current_branch]`
└─ Result: Push your branch to remote and set up tracking
```

**Display other out-of-sync branches (if any):**

If there are branches in `branch_sync.out_of_sync_branches` besides the current branch:

```
Other branches out of sync:
- `[branch_name]`: [status] [tracking] by [ahead/behind] commit(s)
```

**Add helpful tip:**
```
💡 Tip: Run the suggested command to sync your current branch before making new changes
```

**Handle fetch failures gracefully:**

If `branch_sync.fetch_failed` is true or `branch_sync.fetch_error` is set:
- Display the error in warnings
- Do NOT display sync status (data may be stale)
- Continue with session normally

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

### Step 6: Load User Settings

Read user settings from `.github/instructions/user-settings.instructions.md` to load user preferences:
- Work Mode: [Autonomous/Orchestrated/Supervised]
- Agent Skills: [Enabled/Disabled]
- Custom Subagents: [Enabled/Disabled]

### Step 7: Inform and Offer Mode Options

Proactively inform the user of the current work mode and offer to continue or learn more:
```
Current work mode: [Autonomous/Orchestrated/Supervised]

Let me know at any time if you'd like to switch to a different mode, or learn more about the available work modes.
```

### Step 8: VS Code Experimental Features Notice

After communicating about work modes, check the User Settings from memory:

- **If both "Agent Skills" and "Custom Subagents" are Enabled**: Skip this section entirely
- **If both are Disabled**: Inform the user about required experimental settings:
  ```
  Note: ARC uses agent skills for on-demand extensible capabilities and delegates work to specialized custom agents in the background. Both features rely on experimental settings in VS Code that must be enabled for them to work properly. If these settings are not enabled, your experience with ARC may be degraded:

  - Chat: Use Agent Skills
  - Chat > Custom Agent in Subagent
  
  Would you like instructions on how to enable them, or have they already been enabled?
  ```
- **If only "Agent Skills" is Disabled**: 
  ```
  Note: ARC uses agent skills for on-demand extensible capabilities. This feature relies on an experimental setting in VS Code that must be enabled. If the setting "Chat: Use Agent Skills" is not enabled, your experience with ARC may be degraded.
  
  Would you like instructions on how to enable it, or has it already been enabled?
  ```
- **If only "Custom Subagents" is Disabled**: 
  ```
  Note: ARC delegates work to specialized agents in the background. This feature relies on an experimental setting in VS Code that must be enabled. If the setting "Chat > Custom Agent in Subagent" is not enabled, your experience with ARC may be degraded.
  
  Would you like instructions on how to enable it, or has it already been enabled?
  ```

**DO NOT proceed past this point until the user has responded.**

**If user requests instructions**, provide the appropriate subset:
- **For both settings**:
  ```
  To enable the required experimental features:
  1. Open User Settings: `Cmd+,` (macOS) or `Ctrl+,` (Windows/Linux)
  2. In the search box, type: "chat.useAgentSkills"
  3. Look for "Chat: Use Agent Skills (Experimental)" and check the box to enable it
  4. In the search box, type: "chat.customAgentInSubagent"
  5. Look for "Chat: Custom Agent In Subagent" and check the box to enable it
  ```
- **For Agent Skills only**:
  ```
  To enable Agent Skills:
  1. Open User Settings: `Cmd+,` (macOS) or `Ctrl+,` (Windows/Linux)
  2. In the search box, type: "chat.useAgentSkills"
  3. Look for "Chat: Use Agent Skills (Experimental)" and check the box to enable it
  ```
- **For Custom Subagents only**:
  ```
  To enable Custom Subagents:
  1. Open User Settings: `Cmd+,` (macOS) or `Ctrl+,` (Windows/Linux)
  2. In the search box, type: "chat.customAgentInSubagent"
  3. Look for "Chat: Custom Agent In Subagent" and check the box to enable it
  ```

### Step 9: Explain Modes (if requested)

If the user wants to learn more about work modes, provide concise descriptions:
- **Autonomous**: Coordinator handles everything until commit time
- **Orchestrated**: User approves each step manually
- **Supervised**: Coordinator handles planning, user approves code changes

### Step 10: Update User Settings

If the user changes mode, update `.github/instructions/user-settings.instructions.md`.

### Step 11: Assess Work

Determine whether this is a continuation of previous work or a fresh start.

### Step 12: Review Context

Help the user understand the project state by referencing ROADMAP and recent CHANGELOG entries.

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
  "branch_sync": {
    "current_branch_status": "synced",
    "out_of_sync_branches": [],
    "fetch_failed": false,
    "fetch_error": null
  },
  "warnings": []
}
```

Or with branch sync issues:

```json
{
  "git_username": "Jane Developer",
  "git_email": "jane@example.com",
  "current_branch": "feature/new-feature",
  "repo_root": "/Users/jane/git/project",
  "branch_sync": {
    "current_branch_status": "behind",
    "out_of_sync_branches": [
      {
        "branch": "feature/new-feature",
        "status": "behind",
        "ahead": 0,
        "behind": 3,
        "tracking": "origin/feature/new-feature"
      },
      {
        "branch": "main",
        "status": "ahead",
        "ahead": 2,
        "behind": 0,
        "tracking": "origin/main"
      }
    ],
    "fetch_failed": false,
    "fetch_error": null
  },
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
  "branch_sync": null,
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
