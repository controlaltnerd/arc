# AGENTS.md - Guide for Agentic AI Tools

This file contains important information for autonomous AI agents. Read this entire file before writing, editing, or executing anything in this repository.

## Project Knowledge

- One or two sentences describing the purpose and context of this repository and (as relevant) the project it supports.

## Key Content

- Comprehensive but concise listing and descriptions of key content (only used for highlighting certain files)

## Conventions and Expectations

- Comprehensive but concise listing of conventions, naming rules, and expectations of contributors (both human and agent)

## Agents Roster

These agents are enabled by default:

- **@coordinator-agent**
    - **Description**: Central orchestrator responsible for directing work between specialized agents and managing work sessions. Start here for general work.
    - **Location**: `/.github/agents/coordinator.agent.md`
- **@architect-agent**
    - **Description**: An expert in software design and engineering, @architect-agent is responsible for designing and planning implementation of desired software features.
    - **Location**: `/.github/agents/architect.agent.md`
- **@coder-agent**
    - **Description**: A general-purpose programmer, @coder-agent is good at handling most common coding tasks.
    - **Location**: `/.github/agents/coder.agent.md`
- **@maintainer-agent**
    - **Description**: An expert in version control, @maintainer-agent is useful whenever git operations are needed.
    - **Location**: `/.github/agents/maintainer.agent.md`
- **@librarian-agent**
    - **Description**: A master of information management, @librarian-agent ensures repository documentation is always up-to-date.
    - **Location**: `/.github/agents/librarian.agent.md`

The following agents are also available in this repository:

- List of additional enabled agents, their purpose, and when they should be used, following the format of the defaults above

## Skills

Skills are portable, task-specific capabilities that can be loaded on-demand. Unlike instructions (always applied) or agents (persona-based), skills provide specialized workflows with supporting scripts and resources.

Skills are located in `/.github/skills/` and follow the [Agent Skills open standard](https://agentskills.io/), making them portable across GitHub Copilot in VS Code, Copilot CLI, and Copilot coding agent.

Available skills in this repository:

- **adr** - Manage Architecture Decision Records (ADRs) for technical decisions. Create new ADRs with auto-populated content, review existing decisions for context, and update ADR status.
- **create-skill** - Create new agent skills with proper structure, naming, and organization, following the Agent Skills open standard.
- **git-branch** - Create and manage git branches using consistent naming conventions. Create feature branches, bugfix branches, and other work branches following the repository's naming standards.
- **git-commit** - Create standardized git commits using Conventional Commits specification. Analyzes diffs to determine appropriate type, scope, and message.
- **git-push** - Workflow for requesting and executing git push operations with user approval. Handles single and multiple commits with transparent information presentation.
- **memory** - Manage project memory to capture and retrieve reusable knowledge, lessons learned, user preferences, and common pitfalls.
- **test-spec** - Manage test specifications using Given/When/Then format with concrete scenarios. Create new specs, update existing ones with test results, and review specs for context.
- **work-session** - Manage work session summaries to document discrete units of work. Create, update, and review session documentation to capture objectives, implementation details, decisions, and outcomes.

## Terminal Commands You Can Use

There are no specific commands commonly used in the development of this repository yet, so use your best judgment and the awareness of your environment to recommend practical commandments for linting, formatting, testing, etc.

## Other Information

Review these SPEC files for more information:

- /SPEC.md
