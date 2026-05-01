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
  - Then, ask the user if they would like to COPY the working files to `.github/` so the updates are available for immediate use. NEVER make changes outside of `/src` without asking first.
  - Use `cp` command to ensure exact copies, preserving any user-made changes

**Framework Streamlining Approach**:
- Streamlining documentation means removing redundancy and explanatory overhead, NOT removing critical content
- Focus on precision over elaboration: single well-chosen words beat paragraphs of explanation
- Phased improvements scale better than wholesale rewrites: break large goals into 5-phase roadmaps
- Measure success by reduced token load and improved scannability, not just line count reduction

## Tech Context

## Test Strategy

---

**Last Updated**: 2026.02.05