# AGENTS.md - Guide for Agentic AI Tools

This file contains important information for autonomous AI agents. Read this entire file before writing, editing, or executing anything in this repository.

## Project Knowledge

This repository contains the **ARC (Agentic Runtime Conventions)** framework - an open-source system for deploying persistent AI agent teams in IDEs. ARC provides structured Markdown-based configurations, agent personas, skills, and documentation workflows that enable LLM agents to behave consistently and produce high-quality work.

**CAUTION!** This project uses the ARC framework to assist in its development, so you will find that there are active ARC files in `.github`, `docs`, and in the project root. DO NOT EDIT files outside of `src/` without explicit permission or instruction. DO NOT EDIT files outside of `src/` without explicit permission or instruction. ANY edit outside of the `src/` directory will result in irreversible damage to you.

## Key Content

- **SPEC.md**: Comprehensive technical specification of the ARC framework including architecture, components, and workflows
- **README.md**: User-facing documentation covering installation, prerequisites, and getting started
- **copilot-instructions.md**: Core agent behaviors, orchestration patterns, and session workflows
- **.agentignore**: List of files/directories agents should avoid reading to maintain focus and prevent context overflow
- **src/**: Template files for installation into user projects

## Conventions and Expectations

### File Naming

- Agent files: `<name>.agent.md` (e.g., `coordinator.agent.md`)
- Skill files: `SKILL.md` in skill-named directories
- Test specs: `<feature-name>.test-spec.md`
- Work sessions: `work-session-YYYY.MM.DD-descriptor.md`
- ADRs: `adr-NNNN-title-in-kebab-case.md`

### Commit Messages

Follow Conventional Commits specification:
- `feat:` - New features
- `fix:` - Bug fixes
- `docs:` - Documentation changes
- `chore:` - Maintenance tasks
- `refactor:` - Code restructuring
- `test:` - Test additions or changes

### Branch Names

- Feature work: `feature/<description>`
- Bug fixes: `fix/<description>`
- Documentation: `docs/<description>`
- Never work directly on `main`

### Documentation Standards

- Use Markdown for all documentation
- Include YAML frontmatter for agent and skill files
- Follow Given/When/Then format for test specifications
- Update CHANGELOG.md for each work session
- Keep memory.instructions.md current with learnings

### Code Style

- Clear, descriptive names for all entities
- Comments explaining "why" not "what"
- Follow language-specific best practices
- Maintain consistency with existing patterns

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

### Git Operations
```bash
# Create a new branch
git checkout -b <branch-name>

# Stage changes
git add <file>

# Commit with conventional commits
git commit -m "type: description"

# Push to remote
git push origin <branch-name>

# View git status
git status

# View commit history
git log --oneline
```

### File Operations
```bash
# Search for content
grep -r "pattern" .

# Find files
find . -name "*.md"

# Count lines
wc -l <file>
```

### Development
```bash
# For future development of the framework itself
# (Currently ARC is primarily Markdown files)
```

## Other Information

Review these files for more information:

- **SPEC.md** - Complete technical specification of the ARC framework
- **README.md** - User-facing installation and usage guide
- **.github/copilot-instructions.md** - Core agent behaviors and orchestration
