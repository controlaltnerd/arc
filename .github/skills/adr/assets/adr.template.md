---
template:
  name: "Architecture Decision Record"
  version: "1.0"
placeholders:
  ADR_NUMBER:
    type: integer
    description: "Sequential ADR number (e.g., 001, 002)"
    required: true
    auto: "next_adr_number"
  ADR_TITLE:
    type: string
    description: "Concise title for the decision (e.g., 'Use PostgreSQL for Data Storage')"
    required: true
  DATE:
    type: date
    description: "Date of decision in YYYY.MM.DD format"
    required: true
    auto: "current_date"
  STATUS:
    type: enum
    options: ["Proposed", "Accepted", "Rejected", "Deprecated"]
    description: "Current status of the decision"
    required: true
    default: "Proposed"
  CONTEXT_SUMMARY:
    type: string
    description: "One-sentence summary linking to ROADMAP item or goal"
    required: true
  TOP_BENEFITS:
    type: string
    description: "Key benefits of chosen approach"
    required: false
    default: "[TODO]"
  TOP_DRAWBACKS:
    type: string
    description: "Key drawbacks of chosen approach"
    required: false
    default: "[TODO]"
  ALTERNATIVE_A_BENEFITS:
    type: string
    description: "Benefits of alternative A"
    required: false
    default: "[TODO]"
  ALTERNATIVE_A_DRAWBACKS:
    type: string
    description: "Drawbacks of alternative A"
    required: false
    default: "[TODO]"
  POSITIVE_CONSEQUENCES:
    type: string
    description: "Expected positive outcomes"
    required: false
    default: "[Inferred] from discussion"
  NEGATIVE_CONSEQUENCES:
    type: string
    description: "New risks, costs, or maintenance burden"
    required: false
    default: "[TODO]"
  NEUTRAL_CONSEQUENCES:
    type: string
    description: "Impacts that shift work without clear benefit/cost"
    required: false
    default: "[TODO]"
  AUTHOR:
    type: string
    description: "Author of the ADR"
    required: false
    auto: "git_user"
  ROADMAP_ITEM:
    type: string
    description: "Related roadmap item ID (e.g., R-003); leave empty if not linked"
    required: false
    default: ""
  BLOCKING:
    type: boolean
    description: "Whether this decision blocks implementation; if true, requires user approval before proceeding"
    required: false
    default: false
  AFFECTED_COMPONENTS:
    type: array
    description: "List of components/systems affected by this decision (e.g., ['backend', 'database']); leave empty if not applicable"
    required: false
    default: []
  DEPENDENCIES:
    type: array
    description: "List of ADR numbers this decision depends on (e.g., ['ADR-001', 'ADR-005']); leave empty if none"
    required: false
    default: []
---

<!-- 
TEMPLATE USAGE NOTES (delete this block when creating ADR):
- [Inferred] tag: Content auto-populated from context; verify accuracy
- [TODO: description]: Placeholder for missing info; fill in later or leave as-is
- Required sections: Context, Decision, Rationale (must have content)
- Optional sections: Can remain [TODO] without blocking ADR creation
- Template frontmatter: do not include the first frontmatter section in a generated ADR
- Output frontmatter: Machine-readable metadata (status, blocking, dependencies) for agent scanning and decision dependency tracking
-->
---
adr_number: {{ADR_NUMBER}}
title: {{ADR_TITLE}}
date: {{DATE}}
status: {{STATUS}}
roadmap_item: {{ROADMAP_ITEM}}
blocking: {{BLOCKING}}
affected_components: {{AFFECTED_COMPONENTS}}
dependencies: {{DEPENDENCIES}}
author: {{AUTHOR}}
---

# ADR {{ADR_NUMBER}}: {{ADR_TITLE}}

**Date**: {{DATE}}
**Status**: {{STATUS}}
**Blocking**: {{BLOCKING}}
**Context**: {{CONTEXT_SUMMARY}}

## Context

- Summarize the household, lab, or technical problem
- Reference triggering docs (ROADMAP, SPEC, incidents)

## Decision

- State the chosen approach in 1-2 sentences
- Mention scope boundaries or exclusions

## Rationale

- Key reasons this option wins (cost, risk, maintainability, speed)
- Note critical assumptions or supporting data

## Alternatives Considered

<!-- If alternatives were not explicitly discussed, use [TODO] or [Inferred] -->

| Option | Pros | Cons | Outcome |
| --- | --- | --- | --- |
| Chosen approach | {{TOP_BENEFITS}} | {{TOP_DRAWBACKS}} | Accepted |
| Alternative A | {{ALTERNATIVE_A_BENEFITS}} | {{ALTERNATIVE_A_DRAWBACKS}} | Rejected |
| Alternative B | [TODO] | [TODO] | [TODO] |

## Implementation Plan

1. Outline major steps or phases
2. Call out owners, dependencies, or sequencing
3. Note testing, documentation, or rollout requirements

## Consequences

<!-- Mark with [Inferred] if derived from context; use [TODO] if unknown -->

- **Positive**: {{POSITIVE_CONSEQUENCES}}
- **Negative**: {{NEGATIVE_CONSEQUENCES}}
- **Neutral**: {{NEUTRAL_CONSEQUENCES}}

## Compliance

- Adherence to AGENTS.md, SPEC.md, ROADMAP.md, security, etc.

## Future Considerations

- Follow-up work, metrics to watch, or triggers for revisitng the ADR

## References

- List relevant files, tickets, specs, or prior ADRs

-- 

**Last Updated**: {{DATE}} by {{AUTHOR}}