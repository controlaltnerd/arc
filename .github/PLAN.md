# Plan: Read-Only Information-Gathering Agent Lineup

**Date**: 2026.02.11  
**Goal**: Replace current action-oriented agents with read-only information-gathering agents to reduce context rot in the main agent by providing focused, concise summaries of relevant information.

## Problem Statement

Current agents perform both read and write operations, which means:
- The main agent accumulates significant context from planning, implementation, and documentation activities, tool activation, etc.
- Context windows fill up with unnecessary details, reducing effectiveness over long sessions
- Using subagents turns the process into a black box for the user, as they lose visibility into agent communication and rationale

## Solution Approach

Shift to **read-only information-gathering agents** that:
- **Only read and analyze** - never write, commit, or modify files other than their output file
- **Return concise summaries** - distill large amounts of information into relevant insights
- **Serve the main agent** - act as specialized assistants that keep the main agent's context lean
- **Focus on specific domains** - each agent specializes in one type of information gathering

The main agent (or a single action-oriented agent) handles all write operations based on the concise summaries provided by information-gathering agents.

## Current Agent Analysis

### Existing Agents

1. **coordinator-agent** - Orchestrates work, manages sessions, reviews quality
2. **architect-agent** - System design, planning, collaborative requirements gathering
3. **coder-agent** - Code implementation, test writing, style/formatting
4. **maintainer-agent** - Git operations, commit messages, version control
5. **librarian-agent** - Documentation management, memory curation, ADR handling

### Key Observations

- **High context load**: Architect needs full codebase context for design; coder needs test specs + implementation context; librarian needs all docs
- **Write-heavy**: Three agents actively modify files (coder, maintainer, librarian)
- **Handoff complexity**: Work passes between multiple agents with state maintained by coordinator
- **Context duplication**: Multiple agents may load similar information (e.g., both architect and coder read test specs)

## Proposed Read-Only Agent Lineup

### 1. Context Builder (User-Suggested)
**Purpose**: Initialize each work session with relevant project/environment context

**Responsibilities**:
- Run once at session start after user describes their goal
- Analyze user's request to identify relevant areas of the codebase
- Read project structure, ROADMAP status, recent work sessions
- Check active branch, uncommitted changes, and environment state
- Generate concise summary (less than 500 words) covering:
  - Project overview relevant to user's request
  - Current branch and git status
  - Related ROADMAP items and their status
  - Recent related work from work session history
  - Key files/directories relevant to the request
  - Any blockers or dependencies to be aware of

**Returns**: Structured context summary for main agent

### 2. Code Analyst
**Purpose**: Search and analyze existing code to answer "how does X work?" questions and investigate errors

**Responsibilities**:
- Find implementation of specific features or functions
- Trace code paths and execution flows
- Identify where specific functionality lives
- Debug code at rest or in execution
- Parse error messages and stack traces
- Find relevant code sections related to errors
- Search for similar past issues in work sessions or memory
- Check recent changes that might have introduced issues
- Identify common error patterns
- Suggest likely root causes for failures
- Explain how existing code works without loading entire files into main agent's context
- Find usage examples of patterns, APIs, or libraries
- Map relationships between components

**Returns**: Concise explanation with file paths, line ranges, key insights, or root cause analysis with suspected issues and relevant context

### 3. Librarian
**Purpose**: Search all documentation to find relevant information without loading everything

**Responsibilities**:
- Search ADRs for relevant architectural decisions
- Review memory.instructions.md for applicable patterns/lessons
- Check work session summaries for related prior work
- Find relevant sections in README, SPEC, AGENTS, etc.
- Identify documentation gaps or conflicts
- Extract relevant test specifications
- Search online documentation when relevant to a request

**Returns**: Summary of relevant documentation with specific references

### 4. Test Analyst
**Purpose**: Analyze test coverage, status, and requirements without loading all test files

**Responsibilities**:
- Review test specifications for specific features
- Check test implementation status (⏳ Planned, 🔄 In Progress, ✅ Passing, ❌ Failing)
- Identify missing test coverage for proposed changes
- Summarize test requirements for new features
- Find existing test patterns to follow
- Analyze test failures and related code

**Returns**: Test status summary with coverage gaps and requirements

### 5. Impact Analyst
**Purpose**: Assess the potential impact of proposed changes across the codebase

**Responsibilities**:
- Identify files that import/depend on code to be changed
- Find usages of functions, classes, or variables being modified
- Check for test files that might need updates
- Identify documentation that might need updates
- Flag potential breaking changes
- Estimate scope of work (small/medium/large change)

**Returns**: Impact assessment with list of affected files and recommendations

## Revised Workflow

### Traditional Workflow (Current)
```
User Request → Coordinator → Architect (plan) → Coordinator → 
Coder (implement) → Coordinator → Maintainer (commit) → 
Coordinator → Librarian (document) → Coordinator → Done
```

**Issues**: Each agent loads significant context; coordinator must track all state

### New Workflow (Proposed)
```
User Request → Main Agent:
  1. Invokes Context Builder → receives session context summary
  2. Invokes Librarian → receives relevant docs/decisions
  3. Invokes Code Analyst → receives relevant code insights
  4. Plans approach based on summaries (no heavyweight architect needed)
  5. [If needed] Invokes Test Analyst → receives test requirements
  6. [If needed] Invokes Impact Analyzst → receives change impact
  7. Implements changes directly
  8. Commits directly
  9. Documents directly
```

**Benefits**: 
- Main agent's context contains only concise summaries, not full file contents
- No state management across multiple agents
- Faster workflow with fewer handoffs
- Information-gathering agents can be invoked in parallel
- Main agent maintains full context of user's intent throughout

## Agent Model Assignment

**Information-Gathering Agents** (Read-Only):
- Use Claude Haiku 4.5 for most efforts
- Use Claude Sonnet 4.5 for code analysis
- These agents do pure research/analysis with no decision-making
- Usually fast and cost-effective, sufficient for information extraction

**Main/Action Agent**:
- Use Claude Sonnet 4.5 for most efforts
- Use Claude Haiku 4.5 for documentation
- Use Claude Opus 4.6 for code generation
- Needs decision-making, code generation, and quality judgment
- Handles all write operations based on gathered information

## Implementation Considerations

### Subagent Behavior
All read-only agents should:
- Follow the existing subagent invocation pattern (respond with "Analysis complete. Output written to...")
- Write their output to `/.github/subagents/<agent-name>.md`
- Include structured sections in their output for easy parsing
- Never wait for user input
- Never create/modify files

### Output Format
Each agent should return very concise, structured Markdown with:
- 2-3 sentence overview of what was explored
- Structured information (files, line numbers, explanations) on what was found
- How complete/certain the analysis is

### Parallel Invocation
The main agent should be able to invoke multiple information-gathering agents simultaneously:
```
# Start of session
→ Invoke Context Builder, Librarian, and Code Analyst in parallel
→ Wait for all three to complete
→ Review summaries
→ Proceed with planning and implementation
```

### Context Management
- Each read-only agent gets a clean context (only what it needs to investigate)
- Main agent accumulates only the concise summaries (not the raw data)
- Maximum summary length should be enforced (e.g., 500 words per agent)

## Migration Path

### Phase 1: Add New Read-Only Agents

Create the five new agent files with read-only focus.

### Phase 2: Simplify Coordinator

- Remove orchestration complexity
- Coordinator becomes the main action-oriented agent, renamed ARC
- ARC uses read-only agents for information gathering
- ARC handles all write operations directly

### Phase 3: Remove Old Agents

- Delete old agents files
- Update documentation to reflect new workflow
- Update AGENTS.md with new agent lineup

### Phase 4: Optimize

- Refine agent outputs based on real usage
- Add additional specialized agents as needed

## Potential Challenges

1. **Quality of Summaries**: Read-only agents must be well-prompted to return concise, relevant information
2. **Information Loss**: Risk of missing important details in summarization
3. **Main Agent Complexity**: Single agent must handle planning, coding, committing, documenting
4. **Parallel Invocation**: Need to ensure framework supports calling multiple agents simultaneously
5. **Output Parsing**: Main agent needs to efficiently parse and integrate multiple summaries

## Next Steps

1. **User Review**: Review this plan with the user for feedback and approval
2. **Prioritize Agents**: Decide which 2-3 agents to implement first for testing
3. **Create Templates**: Develop the agent file templates with proper structure
4. **Build Prototype**: Implement first agent and test with real scenarios
5. **Iterate**: Refine based on actual usage and performance
6. **Scale**: Roll out remaining agents once pattern is validated

---

**Status**: Draft - Awaiting User Review  
**Next**: User feedback → Agent prioritization → Prototype development
