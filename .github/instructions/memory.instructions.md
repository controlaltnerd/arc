---
applyTo: '**'
---

## Product Context

## System Patterns

**Dual File Structure**:
- ARC repository contains TWO sets of files: active development files and distribution templates
- `.github/`, `docs/`, root `*.md` files: Active ARC files used to develop ARC itself
- `src/`: Template/source files distributed to users when they install ARC in their projects
- **CRITICAL**: When updating ARC features (agents, skills, instructions), ALWAYS follow these steps:
  - First, update and test in `src/`
  - Then, ask the user if they would like to COPY the working files to `.github/` so the updates are available for immediate use
  - Use `cp` command to ensure exact copies, preserving any user-made changes

## Tech Context

## Test Strategy

## User Settings

**Work Mode**: Supervised

---

**Last Updated**: 2026.01.29