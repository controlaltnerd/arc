# Repository/Project Specification

## Overview

This repository contains the **ARC (Agentic Runtime Conventions)** framework - an open-source system for deploying persistent AI agent teams in IDEs with a focus on restraint, quality, and consistent behavior. ARC provides agents with the context, standards, and tools they need to perform as effective virtual team members, enforcing compliance to expectations and ensuring thorough documentation.

## Technologies and Dependencies

- **Primary Technology**: Markdown-based configuration and documentation
- **IDE**: Visual Studio Code (v1.108.0 or greater)
- **Extension**: GitHub Copilot Chat extension (latest version)
- **LLM Requirements**: Tool-calling capable models (Claude, GPT-4, Gemini, etc.)
- **Version Control**: Git
- **Standards**: Agent Skills open standard (agentskills.io), Conventional Commits

## Project Structure

```sh
/                       # Project root
├── .agentignore        # Files for agents to avoid reading
├── .github/            # ARC system configuration
│   ├── agents/         # Specialized AI agent personas
│   ├── instructions/   # Coding standards and persistent memory
│   ├── prompts/        # Reusable user-invoked commands
│   └── skills/         # Portable task-specific capabilities
├── ARC/                # Installation directory (removed after setup)
├── docs/               # Project documentation
│   └── adrs/           # Architecture Decision Records
│   ├── tests/          # Human-readable test specifications
│   ├── work-sessions/  # Session summaries
├── AGENTS.md           # Agent roster and project knowledge
├── CHANGELOG.md        # Work session summaries
├── README.md           # User-facing documentation
├── ROADMAP.md          # Planned work tracking
├── SPEC.md             # Project specification (this file)
└── TESTS.md            # Test catalog and status
```

## Data Structures

### Agent Configuration
- **Format**: Markdown files with YAML frontmatter
- **Location**: `.github/agents/*.agent.md`
- **Structure**: Name, description, expertise, responsibilities, boundaries

### Skills
- **Format**: SKILL.md files following Agent Skills standard
- **Location**: `.github/skills/<skill-name>/`
- **Components**: SKILL.md definition, optional assets/ directory with templates

### Memory
- **Format**: Structured Markdown with specific sections
- **Location**: `.github/instructions/memory.instructions.md`
- **Sections**: Project Brief, Product Context, System Patterns, Tech Context, Progress

### Test Specifications
- **Format**: Given/When/Then scenario format in Markdown
- **Location**: `docs/tests/<feature-name>.test-spec.md`
- **Status Icons**: ⏳ Planned, 🔄 In Progress, ✅ Passing, ❌ Failing

### Work Session Summaries
- **Format**: Structured Markdown with standardized fields
- **Location**: `docs/work-sessions/work-session-YYYY.MM.DD-descriptor.md`
- **Content**: Objective, files changed, decisions, verification, next steps

## Core Functionality

### 1. Agent Orchestration

The framework provides five built-in agents that collaborate through a central coordinator. See AGENTS.md for complete agent roster and descriptions.

### 2. Persistent Memory

Agents maintain context across sessions through structured memory storage covering project knowledge, patterns, technical details, and progress.

### 3. Test-Driven Development

Two-layer TDD approach:
- **Layer 1**: Human-readable test specifications in Markdown
- **Layer 2**: Language-specific test implementations

### 4. Skills System

Portable, on-demand capabilities following Agent Skills open standard. See AGENTS.md for complete skills listing.

### 5. Session Documentation

Every work session produces structured documentation including technical details, compliance analysis, and verification logs. Two-phase commit strategy separates code commits from documentation commits.

## Configuration

### Initial Setup

1. Clone ARC repository to project root in directory named `ARC`
2. Review and customize `SEED.md` with project purpose
3. Run seed agent with: `Review SEED.md and carefully follow the instructions within it`
4. Review `.agentignore` and add files agents should avoid

### Skills Activation

Enable skills with VS Code setting: `chat.useAgentSkills: true`

## Installation and Usage

### Prerequisites

- Visual Studio Code v1.108.0+
- GitHub Copilot Chat extension (latest)
- Tool-calling capable LLM

### Installation

Run the installation prompt with Copilot while viewing SEED.md. The seed agent will:
1. Review project content
2. Customize all template files
3. Deploy files to appropriate locations
4. Generate installation summary
5. Clean up installation directory

### Usage

1. Start conversations with `@coordinator-agent` for general work
2. Coordinator orchestrates specialized agents as needed
3. Skills activate automatically based on context
4. Use `/` commands to invoke reusable prompts
5. End sessions with explicit termination phrases

## Logging and Error Handling

### Work Tracking

- **CHANGELOG.md**: Completed work with semantic versioning
- **ROADMAP.md**: Planned work organized by priority
- **TESTS.md**: Test status and coverage metrics

### Session Logs

Each work session creates a detailed log in `docs/work-sessions/` including:
- Objective and outcomes
- Files modified
- Technical decisions
- Verification results
- Next steps

### Error Documentation

When debugging occurs, lessons learned are documented in:
- Work session summaries
- Memory file under appropriate section
- ADRs for architectural decisions

## Possible Future Enhancements

- Support for additional IDEs beyond VS Code
- Enhanced skill library
- Automated quality metrics

## Testing Strategy

### Test-Driven Development

All features follow TDD workflow:
1. Create human-readable test specification
2. Get user approval
3. Implement language-specific tests
4. Write code to pass tests
5. Update test catalog

### Test Catalog

TESTS.md provides real-time quality dashboard:
- Overall coverage metrics
- Feature-by-feature test status
- Critical failing tests
- Recently updated tests

### Test Specifications

Located in `docs/tests/` using Given/When/Then format. Language-agnostic and reviewable by all stakeholders.

## Dependencies and Requirements

### Runtime Requirements

- VS Code editor with Copilot support
- Git version control
- Markdown rendering capability

### Development Requirements

- Understanding of Markdown syntax
- Familiarity with Git workflows
- Knowledge of Conventional Commits format
- Understanding of Agent Skills standard

## Security Considerations

### File Access Control

`.agentignore` prevents agents from reading user-defined files:
- Credentials and secrets
- Build artifacts
- Dependencies (node_modules, etc.)
- Large data files that could overflow context

### Boundary Enforcement

Agents are configured to:
- Never commit secrets
- Never edit config files without approval
- Always ask before major changes
- Follow principle of least privilege

### Memory Safety

Memory file should not contain:
- Passwords or API keys
- Personal identifiable information
- Proprietary business logic
- Confidential data

## Support and Contribution

### Documentation

See AGENTS.md for documentation references.

### Contact

Project repository: https://github.com/controlaltnerd/arc
