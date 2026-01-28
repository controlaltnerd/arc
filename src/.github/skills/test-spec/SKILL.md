---
name: test-spec
description: Manage test specifications using Given/When/Then format with concrete scenarios. Create new specs, update existing ones with test results, and review specs for context. Use when defining acceptance criteria, updating test status, or researching expected behavior before implementation.
---

# Test Specification Management

## Overview

Manage test specifications that define expected behavior and acceptance criteria. Test specifications use Given/When/Then format to clearly communicate what should be tested and what outcomes are expected.

You can use this skill to:
- **Create** new test specifications for features
- **Update** existing specs with test results, coverage, or new scenarios
- **Review** test specifications to understand expected behavior

## When to Use This Skill

**Creating test specifications**:
- A feature has been approved for implementation and needs acceptance criteria defined
- You need to define expected behavior before coding begins
- The user has requested test specifications or architectural planning
- You are transitioning from design to implementation and need clear "done" criteria

**Updating test specifications**:
- Test implementations are complete and results need to be documented
- Coverage percentages are available and should be recorded
- Test status has changed (planned → implemented → passing/failing)
- New edge cases or scenarios are discovered during implementation
- Test files have been created and need to be linked

**Reviewing test specifications**:
- Understanding expected behavior before implementing a feature
- Checking what edge cases should be covered
- Verifying test coverage and status for a feature
- Researching acceptance criteria before starting work

**Do NOT use this skill for**:
- Features that are still exploratory or speculative (wait until they're committed)
- Creating specs for completed work without a clear need for documentation
- Features without clear user requirements (gather requirements first)

## Managing Existing Test Specifications

### Updating a Test Specification

When test results become available or status changes:

1. **Locate the test spec file** in the test specifications directory
2. **Update relevant sections**:
   - **Status**: Change from `planned` → `implemented` → `passing` or `failing`
   - **Coverage**: Add coverage percentage when available (e.g., "85%")
   - **Test Files**: Link to actual test implementation files with line numbers
   - **Test Status icons**: Update scenario status (⏳ → ✅ or ❌)
   - **New scenarios**: Add newly discovered edge cases or test scenarios
3. **Update frontmatter**:
   ```yaml
   status: passing
   coverage: 85%
   test_files:
     - tests/feature/feature.test.ts:15-42
     - tests/feature/edge-cases.test.ts:10-28
   ```
4. **Update last_updated date** in frontmatter
5. **Commit the update** with a message like "Update test spec: feature-name status"

### Reviewing Test Specifications

When researching expected behavior:

1. **Locate test spec files** in the test specifications directory
2. **Read key sections**:
   - **Overview**: What the feature does and why it needs testing
   - **Test Scenarios**: Given/When/Then scenarios with concrete examples
   - **Edge Cases**: Unusual conditions that should be handled
   - **Performance/Security Considerations**: Non-functional requirements
3. **Check status and coverage**: Understand current test implementation state
4. **Review dependencies**: Understand what other features must work first
5. **Note blocking status**: Whether implementation requires approval

## Creating New Test Specifications

### 1. Verify Feature Readiness

Before creating a test specification:

1. **Confirm feature approval**: Ensure the feature has been approved for implementation
2. **Check implementation status (verbiage may vary)**: 
   - ✅ **Not yet started**: Proceed with test spec creation
   - ✅ **Planning phase**: Proceed with test spec creation or refinement
   - ❌ **Still exploratory**: Stop. Ask user to finalize requirements first
   - ⚠️ **Already in progress or completed**: Confirm with user if this is refinement or new work

3. **Verify you have sufficient context**: Ensure you understand the feature's purpose, scope, and constraints before proceeding

### 2. Gather Requirements from User

Before writing test scenarios, collaborate with the user to understand:

- **Feature purpose**: What problem does this solve?
- **Success criteria**: What does "done" look like?
- **Edge cases**: What unusual conditions should be handled?
- **Performance expectations**: Are there speed/scale requirements?
- **Security concerns**: Are there authentication, authorization, or data protection requirements?
- **Dependencies**: What other features or systems does this rely on?
- **Blocking status**: Does implementation need to wait for user approval of this spec?

### 3. Use the Test Spec Template

The template is located at [assets/test-spec.template.md](assets/test-spec.template.md).

**Key Points**:
- **Do NOT include** the template's first frontmatter section (the one defining placeholders)
- **DO include** the output frontmatter (feature, status, coverage, etc.)
- Set `blocking: true` if user approval is required before implementation begins
- Set `status: "planned"` initially
- Use current date in YYYY.MM.DD format for `last_updated`

### 4. Write Test Scenarios in Given/When/Then Format

Each scenario should follow this structure:

```markdown
### Scenario N: [Category] - [Specific Scenario Name]

**Given**: [Initial conditions or context - be specific with concrete examples]  
**When**: [Action or event that triggers the test - use concrete examples]  
**Then**: [Expected outcome or behavior - measurable result]

**Test Status**: ⏳ Planned  
**Test File**: [path/to/test.file:line-range (update after implementation)]

**Edge Cases**:
- [Specific edge case with concrete example]
- [Another edge case with concrete example]
- [Security or boundary condition]

**Notes**: [Any additional context, known issues, or dependencies]
```

**Status Icons**:
- ⏳ Planned - Not yet implemented
- 🔄 In Progress - Implementation started
- ✅ Passing - Tests passing
- ❌ Failing - Tests failing

**Scenario Categories** (use as appropriate):
1. **Happy Path** - Normal, expected usage
2. **Error Handling** - Invalid inputs, malformed data
3. **Boundary Conditions** - Limits, empty collections, large datasets
4. **Concurrent Operations** - Multi-user, race conditions (if applicable)

**Writing Guidelines**:
- **Be specific**: Use concrete examples, not generic descriptions
  - ❌ "When user enters invalid data"
  - ✅ "When user enters email 'notanemail' without @ symbol"
- **Be measurable**: Expected outcomes should be verifiable
  - ❌ "Then system handles it appropriately"
  - ✅ "Then system returns 400 error with message 'Invalid email format'"
- **Include edge cases**: Think about null values, empty strings, very large inputs, special characters
- **Consider security**: Include SQL injection, XSS, authentication bypass scenarios where relevant

### 5. Add Optional Sections (Ask User First)

**Performance Considerations**: Only include if user has stated performance requirements
```markdown
## Performance Considerations

- Response time: 95th percentile under 200ms
- Throughput: 1000 requests/second
- Resource usage: Max 512MB memory under normal load
- Scalability: Linear scaling up to 10,000 concurrent users
```

**Security Considerations**: Include if feature handles sensitive data or user input
```markdown
## Security Considerations

- Input validation: All user inputs sanitized before database queries
- Authentication: JWT required for all API endpoints
- Authorization: Role-based access control enforced
- Data protection: Passwords hashed with bcrypt, sensitive data encrypted at rest
- Attack vectors: SQL injection, XSS, CSRF protection validated
```

### 6. File Naming and Placement

**Location**: If unclear, ask the user where test specifications should be stored (common locations: `docs/tests/`, `specs/`, `test-specs/`, or alongside source code)

**Naming Convention**: 
- Use kebab-case (lowercase with hyphens)
- Be descriptive and match the feature name
- Examples:
  - `user-authentication.md`
  - `api-rate-limiting.md`
  - `database-backup-restore.md`

**File Creation**:
```markdown
[test-specs-location]/[feature-name].md
```

### 7. User Approval Process

Before finalizing the test specification:

1. **Share draft with user**: Present the test specification in full
2. **Walk through scenarios**: Explain the Given/When/Then scenarios and ask for feedback
3. **Confirm completeness**: Ask "Have I captured all the edge cases and requirements you have in mind?"
4. **Discuss blocking status**: If `blocking: true`, explicitly state "Implementation will wait for your approval of this spec"
5. **Iterate if needed**: Revise based on user feedback
6. **Get explicit approval**: Ask "Does this test specification accurately capture the acceptance criteria for [feature]?"

### 8. Link to Project Documentation

After creating the test specification:

1. If unclear, ask the user if there are related planning documents, feature specs, or issues that should be cross-referenced
2. Add relevant links to the test specification's overview or frontmatter
3. Update those documents to reference the test spec if appropriate for traceability

## Best Practices

- **Start with happy path**: Cover the primary use case first, then edge cases
- **One concept per scenario**: Don't combine multiple behaviors in a single Given/When/Then
- **Realistic test data**: Use concrete examples that reflect real-world usage
- **Testable outcomes**: Every "Then" should be verifiable by an automated test
- **Consider maintenance**: Tests should be clear enough that future developers understand intent
- **Document assumptions**: Note any assumptions about system state or dependencies
- **Update after implementation**: As tests are implemented, update `test_files`, `coverage`, and `status` fields

## Common Pitfalls to Avoid

- ❌ Creating specs for exploratory or unapproved features
- ❌ Generic scenarios like "User does something invalid"
- ❌ Missing edge cases (nulls, empty strings, very large values)
- ❌ Forgetting to link to related project documentation
- ❌ Not getting user approval before implementation
- ❌ Writing implementation details instead of behavior expectations
- ❌ Skipping the `blocking` field when user approval is required

## Template Reference

The complete template with all sections and examples is available at [assets/test-spec.template.md](assets/test-spec.template.md).
