---
template:
  name: "Test Specification"
  version: "1.0"
placeholders:
  FEATURE_NAME:
    type: string
    description: "Name of feature being tested"
    required: true
  STATUS:
    type: enum
    options: ["planned", "implemented", "passing", "failing"]
    description: "Current overall status of test suite for this feature"
    required: true
    default: "planned"
  COVERAGE:
    type: string
    description: "Test coverage percentage for this feature (e.g., '85%')"
    required: false
    default: "N/A"
  RELATED_ROADMAP:
    type: string
    description: "Related roadmap item ID"
    required: false
    default: ""
  RELATED_SPEC:
    type: string
    description: "Link to relevant section in SPEC.md"
    required: false
    default: ""
  TEST_FILES:
    type: array
    description: "List of actual test implementation files"
    required: false
    default: []
  DATE:
    type: date
    description: "Last updated date in YYYY.MM.DD format"
    required: true
    auto: "current_date"
  BLOCKING:
    type: boolean
    description: "Whether this test specification blocks implementation; if true, requires user approval before proceeding"
    required: false
    default: false
  DEPENDENCIES:
    type: array
    description: "List of features this test suite depends on (e.g., ['authentication', 'database-connection']); leave empty if none"
    required: false
    default: []
---

<!-- 
TEMPLATE USAGE NOTES (delete this block when creating test spec):
- Use Given/When/Then format for all test scenarios
- Be specific with concrete examples rather than generic descriptions
- Include edge cases and error conditions for each scenario
- Update test status (⏳ ✅ ❌ 🔄) after implementation and test runs
- Link test files with line numbers after implementation (e.g., src/auth/auth.test.js:15-32)
- Template frontmatter: do not include the first frontmatter section in a generated test spec
- Output frontmatter: Machine-readable metadata for agent scanning and test dependency tracking
-->
---
feature: {{FEATURE_NAME}}
status: {{STATUS}}
coverage: {{COVERAGE}}
related_roadmap: {{RELATED_ROADMAP}}
related_spec: {{RELATED_SPEC}}
test_files: {{TEST_FILES}}
blocking: {{BLOCKING}}
dependencies: {{DEPENDENCIES}}
last_updated: {{DATE}}
---

# Test Specification: {{FEATURE_NAME}}

**Status**: {{STATUS}}  
**Coverage**: {{COVERAGE}}  
**Related Roadmap**: {{RELATED_ROADMAP}}  
**Related Spec**: {{RELATED_SPEC}}  
**Blocking**: {{BLOCKING}}  
**Last Updated**: {{DATE}}

## Overview

{{Brief description of what this feature does and why it needs testing}}

## Test Files

<!-- List actual test implementation files once created -->

{{#each TEST_FILES}}
- {{this}}
{{/each}}

## Test Scenarios

<!-- Add as many scenarios as needed to cover all aspects of the feature -->
<!-- Use Given/When/Then format for clarity and consistency -->
<!-- Status icons: ⏳ Planned | ✅ Passing | ❌ Failing | 🔄 In Progress -->

### Scenario 1: Happy Path - {{SCENARIO_NAME}}

**Given**: {{Initial conditions or context - be specific}}  
**When**: {{Action or event that triggers the test - use concrete examples}}  
**Then**: {{Expected outcome or behavior - measurable result}}

**Test Status**: ⏳ Planned  
**Test File**: {{path/to/test.file:line-range (update after implementation)}}

**Edge Cases**:
- {{Edge case 1 - be specific (e.g., "Empty password field")}}
- {{Edge case 2 - be specific (e.g., "Password exceeds 128 characters")}}
- {{Edge case 3 - include security concerns (e.g., "SQL injection in username")}}

**Notes**: {{Any additional context, known issues, or dependencies}}

---

### Scenario 2: Error Handling - {{SCENARIO_NAME}}

**Given**: {{Initial conditions including what makes this an error case}}  
**When**: {{Invalid action or malformed input}}  
**Then**: {{Expected error handling behavior - should be graceful and informative}}

**Test Status**: ⏳ Planned  
**Test File**: {{path/to/test.file:line-range}}

**Edge Cases**:
- {{Null/undefined values}}
- {{Wrong data types}}
- {{Out of range values}}

**Notes**: {{Error messages should be user-friendly and not expose sensitive system information}}

---

### Scenario 3: Boundary Conditions - {{SCENARIO_NAME}}

**Given**: {{System state at resource limits or boundaries}}  
**When**: {{Action that tests system boundaries}}  
**Then**: {{Expected handling of boundary condition without crashing}}

**Test Status**: ⏳ Planned  
**Test File**: {{path/to/test.file:line-range}}

**Edge Cases**:
- {{Minimum allowed values}}
- {{Maximum allowed values}}
- {{Empty collections}}
- {{Very large datasets}}

**Notes**: {{These tests ensure the system degrades gracefully under stress}}

---

### Scenario 4: Concurrent Operations - {{SCENARIO_NAME}}

<!-- Include this section only if feature involves shared state or multi-user scenarios -->

**Given**: {{Multiple users/processes accessing the system simultaneously}}  
**When**: {{Operations that might conflict or create race conditions}}  
**Then**: {{Expected data consistency and concurrency handling}}

**Test Status**: ⏳ Planned  
**Test File**: {{path/to/test.file:line-range}}

**Edge Cases**:
- {{Race conditions}}
- {{Deadlock scenarios}}
- {{Resource contention}}

**Notes**: {{Critical for multi-user systems and systems with shared state}}

---

## Performance Considerations

<!-- Only include this section after asking the user if they need to test performance -->
<!-- Include specific, measurable performance requirements -->

- Response time: {{Target latency with percentile}}
- Throughput: {{Target requests/operations per second}}
- Resource usage: {{Maximum memory/CPU usage under normal load}}
- Scalability: {{How performance should scale with load}}

## Security Considerations

<!-- List security requirements and attack vectors to test -->

- Input validation: {{How inputs are validated and sanitized}}
- Authentication: {{Authentication requirements for operations}}
- Authorization: {{Authorization checks to prevent unauthorized access}}
- Data protection: {{How sensitive data is protected in logs, errors, storage}}
- Attack vectors: {{Specific security tests like SQL injection, XSS, CSRF}}

## Dependencies

<!-- List features or systems that must be working for these tests to pass -->

{{List any other features or systems this test suite depends on}}

## Compliance

<!-- Document alignment with AGENTS.md, SPEC.md, ROADMAP.md, and security practices -->

- Adherence to coding standards and testing conventions in AGENTS.md
- Alignment with feature specifications in SPEC.md
- Coverage of acceptance criteria from related ROADMAP item

---

## Revision History

- {{DATE}}: Initial test specification created
- {{DATE}}: {{Description of changes to test specification}}
