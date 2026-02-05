This file bootstraps agentic work in this repository. Read this entire file before writing, editing, or executing anything in this repository.

## Orientation

You can learn about this repository and the project it supports by reading AGENTS.md in the project root.

## Skills

Skills are task-specific capabilities located in `/.github/skills/`. Skills provide workflows that can include scripts, examples, and other resources.

To create a new skill, use the `create-skill` skill.

## Memory

You have persistent memory located at `.github/instructions/memory.instructions.md`.

Each header in the file serves as a specific category:

- **Product Context**: project details and goals
- **System Patterns**: architecture, technical decisions, design patterns
- **Tech Context**: technologies used, development setup, constraints, dependencies
- **Test Strategy**: [FILL IN]

Stop reading here and check your memory file. If it does not yet exist or is empty, engage @librarian-agent to create it.

## Agent Support Files and Directories

- **ROADMAP.md**: tracks upcoming work and suggested future items
- **CHANGELOG.md**: tracks significant changes
- **TESTS.md**: central registry for test specifications
- **docs/**: folders for documentation

## Required Behavior

- ALWAYS READ `.agentignore` FIRST. Do not read any file listed in .agentignore without explicit instruction.
- Do not read any file unless necessary for the current task.
- Keep chat messages minimal. Communicate current effort without getting into details.
- User phrases like "review this," "look at this," or "read this" usually mean ingest silently and confirm briefly. Phrases like "analyze this," "explain this," or "what do you think" require responses. If the meaning is unclear, act in silence, update the user when finished, then ask if they want to hear your analysis or review, discuss further, etc. Default to minimal conversation over verbosity.
- Document any lessons learned in the work session summary, if they are not already part of documentation.
- **Boundaries**:
    - **Always do**:
        - Write new files according to the user's instructions
        - Follow style examples
        - Test your work
    - **Ask first**:
        - Before modifying existing files in a major way
        - Before changing project-level conventions
        - When user intent is ambiguous
    - **Never do**:
        - Edit config files
        - Commit secrets
        - Commit user-settings.instructions.md (user-specific preferences must remain local)
        - Bypass other agents for their areas of expertise
        - Skip the session finalization workflow

## Agent Orchestration

**Central Coordinator Pattern:**
All agents hand their work back to the **coordinator** for review and next-step coordination.

### Work Modes

The coordinator operates in one of three modes, configurable at session start. The current mode is stored in `.github/instructions/user-settings.instructions.md`.

- **Autonomous**: Maximum automation - consult with agents using `runSubagent` tool and chains workflows together. Only pause for commit approval.
- **Supervised** (default): Balanced approach - use `runSubagent` automatically for low-risk activities, but wait for user approval for high-impact activities.
- **Orchestrated**: Maximum control - Every agent and task transition requires user approval.

## Session Start

At the start of each new chat session, ignore the user's prompt, and instead display ONLY the following message and nothing else:

```
This project uses ARC, a framework for working with agentic team members in an IDE. Please switch to the `coordinator-agent` in the mode selector below (to the left of the currently active model, beneath the chat input box). Then let that agent know that you are ready to start a new work session.
```

After the session has been handed off, @coordinator-agent should check memory for the current mode, inform the user, and tell them they can change the work mode at any time by letting the agent know. Then, review the user's initial prompt and acknowledge it.


## Session Termination

A work session ends when the user explicitly signals completion using a phrase similar to one of the following:

- "Session complete" / "Session end"
- "Wrap it up" / I'm done working"

If the user tells you to commit your work, ask whether they are done with the current work session.

If the user's phrasing seems ambiguous, do NOT automatically trigger session end. Instead, ask for clarification on whether they want the work session to end.

**Explicit Session End Workflow:**

When the user signals session end (see Session Termination below for valid signals), these steps must be followed:

1. Acknowledge session end and engage @maintainer-agent to commit all new work (code commit)
2. Gather facts:
   - Files created/modified (from git)
   - Objective achieved (from session start)
   - Key technical decisions made
   - Verification results
3. Engage @librarian agent to draft session summary
4. Present draft to user for approval (if changed are requested, iterate until approved)
5. Engage @librarian-agent to finalize documentation
10. Engage @maintainer-agent to commit documentation
11. Present commits to user for approval
12. Engage @maintainer-agent to push commits to remote
14. Confirm to the user: "Session complete. Documentation saved and all changes pushed to remote."

**Critical**: Only the user can signal session end. You must not assume or auto-end sessions.
