---
template:
  name: "Memory Instructions"
  version: "1.0"
applyTo: '**'
placeholders:
  WORK_MODE:
    type: string
    description: "Current work mode (e.g., 'Planning', 'Implementation', 'Review')"
    required: false
  LAST_UPDATED:
    type: date
    description: "Date of last update in YYYY.MM.DD format"
    required: false
    auto: "current_date"
---

## Product Context

## System Patterns

## Tech Context

## Test Strategy

## Active Context

## Progress

## User Settings

**Work Mode**:  {{WORK_MODE}}
**Agent Skills**: {{STATUS}}
**Custom Subagents**: {{STATUS}}

---

**Last Updated**: {{LAST_UPDATED}}
