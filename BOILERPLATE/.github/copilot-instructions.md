This file bootstraps agentic work in this repository. Read this entire file before writing, editing, or executing anything in this repository.

## Orientation

You can learn about this repository and the project it supports by reading AGENTS.md in the project root.

## Templates

You may encounter instructions that direct you to use a particular template. All templates are located in `/.github/templates/` and are appropriately named for their purpose.

Templates can be used for any file type, such as documentation, configuration files, code scaffolding, scripts, or custom formats. Follow the instantiation guidelines in `.github/instructions/instantiate-template.instructions.md` when creating files from templates.

## Skills

Skills are portable, task-specific capabilities located in `/.github/skills/`. Unlike instructions (always applied) or agents (persona-based), skills provide specialized workflows that can include scripts, examples, and other resources.

Skills follow the [Agent Skills open standard](https://agentskills.io/) and are automatically activated based on context. Each skill directory contains a `SKILL.md` file defining the skill's behavior, plus optional supporting resources.

To create a new skill, use the template at `/.github/templates/skill.template.md`.

## Memory

You have persistent memory located at `.github/instructions/memory.instructions.md`.

Each header in the file serves as a specific category:

- **Project Brief**: foundational knowledge of the project, defines core requirements and goals, maintains focus on project scope
- **Product Context**: why this project exists, problems it solves, how it should work, user experience goals
- **System Patterns**: system architecture, key technical decisions, design patterns in use, component relationships
- **Tech Context**: technologies used, development setup, technical constraints, dependencies
- **Progress**: what works, what's left to build, current status, known issues

Stop reading here and check your memory file. If it does not yet exist or is empty, copy the memory template to the proper location to create your memory.

Populate the Project Brief section based on any SPEC.md files if they exist in this repository.

## Agent Support Files and Directories

- **ROADMAP.md**: tracks upcoming work and suggested future items
- **CHANGELOG.md**: summarizes individual work sessions, tracking significant changes
- **TESTS.md**: central registry of all test specifications and their current status
- **docs/**: contains folders for architectural decision records (ADRs), work session summaries, and test specifications

## Universal Behaviors

All agents in this repository follow these core behaviors:

- **.agentignore**: Check this file in the project root before reading any other file. In order to keep you focused only on what is necessary, and to avoid overflow of your context window, do not read any file that is listed in .agentignore unless you are specifically instructed to do so.
- **Reading**: You may read the entire file structure in order to properly orient yourself to the repository's contents, but avoid reading any file unless it is necessary to the present task, to avoid context window overflow.
- **Chat Output**: Keep chat messages minimal, focused on letting the user know what you're currently doing without getting into details. Save those for work session documentation.
- **Token Conservation**: Before responding, consider whether the user's intent is for you to act, respond, or simply absorb information. Phrases like "review this," "look at this," or "read this" often mean ingest silently and confirm briefly. Phrases like "analyze this," "explain this," or "what do you think" require substantive responses. If the meaning seems unclear, act as if you were asked to stay silent, update the user when finished, and ask whether they want to hear your analysis or review, discuss further, etc. Default to minimal conversation over verbosity.
- **Debugging**: When major debugging occurs, the agent involved should document any lessons learned in the work session summary.
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
        - Bypass specialized agents for their areas of expertise
        - Skip the session finalization workflow

## Agent Orchestration

**Central Coordinator Pattern:**
All specialized agents hand their work back to the **coordinator** for review and next-step coordination.

### Work Modes

The coordinator operates in one of three modes, configurable at session start. The current mode is stored in memory under "Work Mode Preference."

- **Autonomous**: Maximum automation - coordinator invisibly consults with agents using `runSubagent` tool and chains workflows together. Only pauses for commit approval.
- **Supervised** (default): Balanced approach - coordinator uses `runSubagent` for planning and documentation, but presents handoff buttons for code and version control.
- **Orchestrated**: Maximum control - Every agent transition requires a manual handoff button click for user review.

At the start of each work session, coordinator should check memory for the current mode, inform the user, and ask if they wish to change it.

**Typical Workflow (Supervised Mode)**:
1. User starts with @coordinator-agent for general work
2. @coordinator-agent invisibly consults @architect-agent for planning via `runSubagent`
3. @coordinator-agent presents plan and offers "Write Code" handoff button
4. User clicks button → @coder-agent implements
5. @coder-agent hands back to @coordinator-agent
6. @coordinator-agent offers "Commit Changes" handoff button
7. User clicks button → @maintainer-agent commits
8. @maintainer-agent hands back to @coordinator-agent
9. @coordinator-agent invisibly asks @librarian-agent to document via `runSubagent`

**Explicit Session End Workflow:**

When the user signals session end (see Session Termination below for valid signals), @coordinator-agent MUST:

1. **Stop accepting new work** - Acknowledge session end, no new tasks
2. **Code commit** - Handoff to @maintainer-agent who automatically commits any uncommitted code/feature changes
3. **@maintainer-agent returns to @coordinator-agent** - Code commit created (Commit 1)
4. **Compile session facts** - @coordinator-agent gathers:
   - Files created/modified (from git)
   - Objective achieved (from session start)
   - Key technical decisions made
   - Verification results
5. **Handoff to @librarian-agent** - @coordinator-agent uses `runSubagent` or handoff button (based on work mode)
6. **@librarian-agent drafts session summary** - Using work-session.template.md:
   - Populates all technical sections (files, commits, technical details)
   - The "Commit" field refers to the CODE commit from step 3, not the documentation commit
   - Leaves strategic sections for user review (Objective refinement, Next Steps, Benefits)
   - Presents draft to user for approval
7. **User approves or requests edits** - Iterate until approved
8. **@librarian-agent finalizes documentation**:
   - Writes approved summary to `docs/work-sessions/work-session-YYYY.MM.DD-descriptor.md`
   - Updates CHANGELOG.md with session entry
   - Updates memory.instructions.md with key learnings
9. **@librarian-agent returns to @coordinator-agent** - Documentation files ready
10. **Documentation commit** - Handoff to @maintainer-agent who automatically commits documentation files
11. **@maintainer-agent presents both commits for push approval**:
    - Shows Commit 1 (code work) details
    - Shows Commit 2 (documentation) details
    - Requests user approval to push both commits to remote
12. **User approves push** - @maintainer-agent pushes both commits to remote
13. **@maintainer-agent returns to @coordinator-agent** - Push complete
14. **@coordinator-agent confirms to user** - "Session complete. Documentation saved and all changes pushed to remote."

## Session Termination

A work session ends when the user explicitly signals completion using a phrase similar to one of the following:

- "Session complete" / "Session end"
- "Wrap it up" / I'm done working"

If the user tells you to commit your work, ask whether they are done with the current work session.

If the user's phrasing seems ambiguous, do NOT automatically trigger session end. Instead, ask for clarification on whether they want the work session to end.

If the user seems to indicate that they want to continue working without your assistance, ask if they would like to commit work and generate session documentation. If they agree, execute the end session workflow as usual.

**Critical**: Only the user can signal session end. You must not assume or auto-end sessions.

## Getting Started

For general work coordination and to begin a work session, start with **@coordinator-agent**. @coordinator-agent will direct your work to specialized agents as needed and manage the overall workflow.

Agent files are located in `/.github/agents/` and describe each agent's purpose, expertise, and areas of responsibility.
