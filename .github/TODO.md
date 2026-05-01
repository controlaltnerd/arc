# TODO - Read-Only Information-Gathering Agent Lineup

**Plan Reference**: `.github/PLAN.md`  
**Last Updated**: 2026.02.25

## Phase 1: Add New Read-Only Agents

- [x] Create Context Builder agent file
  - Initializes sessions with relevant project context
  - Returns structured summary under 500 words
  
- [x] Create Code Analyst agent file
  - Searches and analyzes existing code
  - Traces code paths and execution flows
  - Debugs and explains functionality
  
- [x] Create Librarian agent file (enhanced)
  - Searches ADRs for architectural decisions
  - Reviews memory and work sessions
  - Extracts test specifications
  
- [x] Create Test Analyst agent file
  - Reviews test specifications and coverage
  - Tracks test implementation status
  - Summarizes test requirements
  
- [x] Create Impact Analyst agent file
  - Identifies dependent files and usages
  - Assesses change scope and breaking changes
  - Flags files requiring updates

## Phase 2: Simplify Coordinator

- [x] Reduce orchestration complexity in coordinator-agent
- [x] Define coordinator role as main action-oriented agent
- [x] Implement read-only agent invocation pattern
- [x] Establish output format standards for read-only agents
- [x] Support parallel invocation of multiple agents

## Phase 3: Remove Old Agents

- [x] Delete old agents files
- [x] Update documentation (AGENTS.md, copilot-instructions.md)
- [x] Remove redundant agent responsibilities
- [x] Verify no broken references

## Phase 4: Optimize

- [ ] Refine agent outputs based on real usage
- [ ] Add additional specialized agents as needed
- [ ] Profile context window usage
- [ ] Document best practices for agent invocation

## Preparation Tasks (Pre-Implementation)

- [x] User review of this plan and approval
- [x] Prioritize which 2-3 agents to implement first
- [x] Develop agent file templates
- [ ] Plan prototype testing scenarios
- [x] Document agent output parsing requirements

## Known Challenges to Address

- [x] Design summary quality standards
- [ ] Prevent information loss in summarization
- [ ] Manage single main agent complexity
- [x] Ensure parallel invocation support
- [x] Establish output parsing protocols

---

**Status**: Phase 1 & 2 Complete  
**Next Action**: Phase 3 - Remove old agents and update documentation
