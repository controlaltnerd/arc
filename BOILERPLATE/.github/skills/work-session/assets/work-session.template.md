---
template:
  name: "Work Session Summary"
  version: "1.0"
placeholders:
  SESSION_DESCRIPTOR:
    type: string
    description: "Brief description of session focus (e.g., 'JWT Authentication', 'UI Refactor')"
    required: true
  DATE:
    type: date
    description: "Session date in YYYY.MM.DD format"
    required: true
    auto: "current_date"
  BRANCH_NAME:
    type: string
    description: "Git branch name"
    required: true
    auto: "git_branch"
  COMMIT_HASH:
    type: string
    description: "Git commit hash of the last CODE commit (short or full). This is the code work commit, not the documentation commit."
    required: false
    auto: "git_commit"
    default: "[pending]"
  STATUS:
    type: enum
    options: ["In Progress", "Complete", "Blocked"]
    description: "Current session status"
    required: true
    default: "In Progress"
  FILES_CREATED_COUNT:
    type: integer
    description: "Number of files created in this session"
    required: true
    auto: "git_diff_created"
    default: 0
  FILES_MODIFIED_COUNT:
    type: integer
    description: "Number of files modified in this session"
    required: true
    auto: "git_diff_modified"
    default: 0
  HUMAN_CONTRIBUTOR:
    type: string
    description: "Name of human contributor"
    required: false
    auto: "git_user"
  AGENT_NAME:
    type: string
    description: "Name of AI agent used"
    required: false
    default: "GitHub Copilot"
---

# Session Summary - {{SESSION_DESCRIPTOR}}

**Date**: {{DATE}}
**Branch**: {{BRANCH_NAME}}
**Commit**: {{COMMIT_HASH}}
**Status**: {{STATUS}}

## Objective

- One or two sentences capturing the human + agent pairing goal

## What Was Implemented

1. Concise bullet per major change or decision
2. Note which collaborator (agent vs human) drove each item when helpful

## Technical Details

- Key commands, APIs, or design notes required for future readers

## Benefits Achieved

1. Highlight measurable improvements or reduced risk
2. Tie benefits to ROADMAP priorities when possible

## Compliance

- Document alignment with AGENTS.md, SPEC.md, ROADMAP.md, and security practices

## Files Created ({{FILES_CREATED_COUNT}})

1. path/to/file

## Files Modified ({{FILES_MODIFIED_COUNT}})

1. path/to/file

## Next Steps

- Brief follow-up actions for either collaborator

## Tests

**Test Specifications**: {{List test specs created or updated}}
**Test Files**: {{List actual test files created or modified}}
**Test Results**: {{Summary of test execution results}}
**Coverage**: {{Coverage percentage if available}}

## Verification Log

- Commands/tests run with notable output summaries

## Memory Updates
- [ ] Coder: Document key points in memory.instructions.md
- [ ] Librarian: Review and clean up memory entries as needed

---

## Template Population Guide

This guide clarifies **when** each field should be populated and **who** is responsible:

| Field | When | Who | How/Source |
|-------|------|-----|------------|
| **Descriptor** | Session start | User | User provides brief description (e.g., "user-auth", "api-refactor") |
| **Date** | Session start | Agent | Auto-populated with current date (YYYY.MM.DD) |
| **Branch** | Session start | Agent | Retrieved from `git branch --show-current` |
| **Commit** | Session end | Agent | Retrieved from `git rev-parse --short HEAD` after final CODE commit (before documentation is created). This references the code work, not the documentation commit. |
| **Status** | Session end | Agent | Reflects actual outcome: Complete / Blocked / In Progress |
| **Objective** | Session start | User + Agent | User states goal; Agent refines to 1-2 sentences |
| **What Was Implemented** | During work | Agent | Running notes of major changes; finalized at session end |
| **Technical Details** | During work | Agent | Key commands, APIs, design notes captured during implementation |
| **Benefits Achieved** | Session end | Agent drafts, User approves | Agent proposes benefits; user confirms or refines |
| **Compliance** | Session end | Agent | Agent verifies alignment with AGENTS.md, SPEC.md, ROADMAP.md |
| **Files Created** | Session end | Agent | Auto-populated from `git diff --name-status` |
| **Files Modified** | Session end | Agent | Auto-populated from `git diff --name-status` |
| **Next Steps** | Session end | User approves | Agent suggests; user confirms, refines, or replaces |
| **Verification Log** | During + session end | Agent | Commands run and their output summaries |
| **Memory Updates** | Session end | librarian | librarian completes after user approves summary |

**Key Principle**: Agent DRAFTS all technical sections; User APPROVES all strategic sections (Objective, Benefits, Next Steps, Status).

**Important**: The work session document itself is committed as a separate, untracked housekeeping step after being approved. The "Commit" field in this document refers only to the code work commits, not to the commit of the documentation file itself. This avoids self-referential commit tracking.

---

Session completed on {{DATE}} by {{HUMAN_CONTRIBUTOR}} + {{AGENT_NAME}}
