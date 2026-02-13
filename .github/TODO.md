# TODO - Read-Only Information-Gathering Agent Lineup

**Plan Reference**: `.github/PLAN.md`  
**Last Updated**: 2026.02.12

## Phase 1: Add New Read-Only Agents

- [ ] Create Context Builder agent file
  - Initializes sessions with relevant project context
  - Returns structured summary under 500 words
  
- [ ] Create Code Analyst agent file
  - Searches and analyzes existing code
  - Traces code paths and execution flows
  - Debugs and explains functionality
  
- [ ] Create Librarian agent file (enhanced)
  - Searches ADRs for architectural decisions
  - Reviews memory and work sessions
  - Extracts test specifications
  
- [ ] Create Test Analyst agent file
  - Reviews test specifications and coverage
  - Tracks test implementation status
  - Summarizes test requirements
  
- [ ] Create Impact Analyst agent file
  - Identifies dependent files and usages
  - Assesses change scope and breaking changes
  - Flags files requiring updates

## Phase 2: Simplify Coordinator

- [ ] Reduce orchestration complexity in coordinator-agent
- [ ] Define coordinator role as main action-oriented agent
- [ ] Implement read-only agent invocation pattern
- [ ] Establish output format standards for read-only agents
- [ ] Support parallel invocation of multiple agents

## Phase 3: Remove Old Agents

- [ ] Delete old agents files
- [ ] Update documentation (AGENTS.md, copilot-instructions.md)
- [ ] Remove redundant agent responsibilities
- [ ] Verify no broken references

## Phase 4: Optimize

- [ ] Refine agent outputs based on real usage
- [ ] Add additional specialized agents as needed
- [ ] Profile context window usage
- [ ] Document best practices for agent invocation

## Preparation Tasks (Pre-Implementation)

- [ ] User review of this plan and approval
- [ ] Prioritize which 2-3 agents to implement first
- [ ] Develop agent file templates
- [ ] Plan prototype testing scenarios
- [ ] Document agent output parsing requirements

## Known Challenges to Address

- [ ] Design summary quality standards
- [ ] Prevent information loss in summarization
- [ ] Manage single main agent complexity
- [ ] Ensure parallel invocation support
- [ ] Establish output parsing protocols

---

**Status**: Ready for User Review  
**Next Action**: Await user feedback on plan and agent prioritization
