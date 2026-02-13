---
applyTo: '**'
---

# User Settings

**IMPORTANT**: This file contains user-specific preferences and should NEVER be committed to version control. Each user should maintain their own local copy with their preferred settings.

## Work Mode

**Current Mode**: Supervised

**Available Modes**:
- **Autonomous**: Maximum automation - coordinator invisibly consults with agents using `runSubagent` tool and executes work automatically. Only pauses for commit approval.
- **Supervised** (default): Balanced approach - coordinator handles low-risk activities automatically, but pauses for user approval before high-impact actions (code implementation, commits).
- **Orchestrated**: Maximum control - coordinator asks permission before every task.

## Feature Toggles

**Agent Skills**: Enabled
**Custom Subagents**: Enabled

## Personal Preferences

Add any personal preferences below (editor settings, preferred naming conventions, etc.)

---

**Last Updated**: {{LAST_UPDATED}}
