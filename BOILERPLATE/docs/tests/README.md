# Test Specifications

This directory contains human-readable test specifications for all features in this project.

## Purpose

Test specifications serve as:
- **Planning Documents**: Define expected behavior before implementation
- **Acceptance Criteria**: Clear definition of "done" for features
- **Living Documentation**: Always up-to-date description of system behavior
- **Language-Agnostic Layer**: Readable by all stakeholders, independent of implementation

## Structure

Each test specification file follows the format: `<feature-name>.test-spec.md`

Example: `authentication.test-spec.md`, `rate-limiting.test-spec.md`

## Workflow

1. **Planning**: When a feature is planned, @architect-agent creates a test specification
2. **Review**: User reviews and approves test scenarios before implementation
3. **Implementation**: @coder-agent uses test spec as guide to write actual tests and code
4. **Maintenance**: Test specs are updated when requirements change or bugs are found
5. **Tracking**: TESTS.md at project root tracks status of all test specifications

## Test Scenario Format

Each scenario uses Given/When/Then structure:
- **Given**: Initial state or preconditions
- **When**: Action or event that occurs
- **Then**: Expected result or outcome

## Test Status Icons

- ⏳ **Planned**: Test scenario defined but not yet implemented
- 🔄 **In Progress**: Test is being written or code is being developed
- ✅ **Passing**: Test implemented and passing
- ❌ **Failing**: Test exists but currently failing

## Creating Test Specifications

Use the template at `.github/templates/test-spec.template.md` to create new test specifications.

Follow the instantiation guidelines in `.github/instructions/instantiate-template.instructions.md`.
