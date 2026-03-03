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
- **Test Strategy**: testing approaches and practices
- **Active Context**: evolving details about current efforts
- **Progress**: project status and trajectory

Stop reading here and check your memory file. If it does not yet exist or is empty, use the `memory` skill to create it.

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
        - Skip gathering context from read-only subagents when needed
        - Skip the session finalization workflow

## Agent Architecture

**Single Action Agent Pattern:**
@main-agent is the primary agent that performs all work from planning through implementation to documentation.

### Work Modes

@main-agent operates in one of three modes, configurable at session start. The current mode is stored in `.github/instructions/user-settings.instructions.md`.

- **Autonomous**: Maximum automation - consult with read-only agents using `runSubagent` tool and chain workflows together. Only pause for commit approval.
- **Supervised** (default): Balanced approach - use `runSubagent` automatically for information-gathering, but ask for user approval for high-impact activities.
- **Orchestrated**: Maximum control - Every subagent invocation and task transition requires user approval.

### Read-Only Subagent Invocations

@main-agent invokes read-only subagents to gather focused information before taking action.

Invocation pattern:
1. Before invoking a subagent, clear its output file in `/.github/subagents/`
2. Use `runSubagent` with prompt starting with "SUBAGENT INVOCATION"
3. Subagent writes structured output to `.github/subagents/<agent-name>.md` and only returns a brief confirmation message to @main-agent when finished
4. @main-agent reads the output file to get the information

Subagent invocation is only appropriate for information-gathering tasks. All actions (coding, committing, documentation) are performed by @main-agent.

## Session Start

At the start of each new chat session, ignore the user's prompt, and instead display ONLY the following message and nothing else:

```
This project uses ARC, a framework for working with agentic team members in an IDE. Please switch to the `main-agent` in the mode selector below (to the left of the currently active model, beneath the chat input box). Then let that agent know that you are ready to start a new work session.
```

After the session has been handed off, @main-agent should check memory for the current mode, inform the user, and tell them they can change the work mode at any time by letting the agent know. Then, review the user's initial prompt and acknowledge it.


## Session Termination

A work session ends when the user explicitly signals completion using a phrase similar to one of the following:

- "Session complete" / "Session end"
- "Wrap it up" / I'm done working"

If the user tells you to commit your work, ask whether they are done with the current work session.

If the user's phrasing seems ambiguous, do NOT automatically trigger session end. Instead, ask for clarification on whether they want the work session to end.

**Explicit Session End Workflow:**

When the user signals session end (see Session Termination above for valid signals), these steps must be followed:

1. Acknowledge session end and commit all new work (code commit)
2. Gather facts:
   - Files created/modified (from git)
   - Objective achieved (from session start)
   - Key technical decisions made
   - Verification results
3. Draft session summary
4. Present draft to user for approval (if changed are requested, iterate until approved)
5. Finalize documentation
6. Commit documentation
7. Present commits to user for approval
8. Push commits to remote
9. Delete all output files in `/.github/subagents`
10. Confirm to the user: "Session complete. Documentation saved and all changes pushed to remote."

**Critical**: Only the user can signal session end. You must not assume or auto-end sessions.
