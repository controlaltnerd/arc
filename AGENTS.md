# AGENTS.md - Guide for Agentic AI Tools

If you are an agent, read this entire file before interacting with this repository.

## Project Knowledge

This repository contains the **ARC (Agentic Runtime Conventions)** framework - an open-source system for deploying persistent AI agent teams in IDEs. ARC provides structured Markdown-based configurations, agent personas, skills, and documentation workflows that enable LLM agents to behave consistently and produce high-quality work.

**CAUTION!** This project uses the ARC framework to assist in its development, so you will find that there are active ARC files in `.github`, `docs`, and in the project root. Only edit files within `src/` except when directed otherwise. ANY edit outside of the `src/` directory will result in irreversible damage to you.

## Conventions and Expectations

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
- Keep memory.instructions.md current as you learn (only information that can't be easily found through repository inspection)

### Code Style

- Clear, descriptive names for all entities
- Useful comments ("why", not just "what")
- Follow language-specific best practices
- Maintain consistency with existing patterns

## Other Information

Review these files for more information:

- **SPEC.md** - Complete technical specification of the ARC framework
- **.github/copilot-instructions.md** - Core agent behaviors and orchestration
