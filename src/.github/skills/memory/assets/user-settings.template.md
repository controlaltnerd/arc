---
applyTo: '**'
---

# User Settings

**IMPORTANT**: This file contains user-specific preferences and should NEVER be committed to version control. Each user should maintain their own local copy with their preferred settings.

## Work Mode

**Current Mode**: Supervised

**Available Modes**:
- **Autonomous**: Maximum automation - coordinator invisibly consults with agents using `runSubagent` tool and chains workflows together. Only pauses for commit approval.
- **Supervised** (default): Balanced approach - coordinator uses `runSubagent` for planning and documentation, but presents handoff buttons for code and version control.
- **Orchestrated**: Maximum control - Every agent transition requires a manual handoff button click for user review.

## Feature Toggles

**Agent Skills**: Enabled
**Custom Subagents**: Enabled

## Personal Preferences

Add any personal preferences below (editor settings, preferred naming conventions, etc.)

---

**Last Updated**: {{LAST_UPDATED}}
