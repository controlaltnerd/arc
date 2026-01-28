# ARC - Agentic Runtime Conventions

ARC is an open-source framework for deploying a team of persistent agents in IDEs with a focus on restraint and quality.

**Bottom line: ARC makes agents behave.**

LLMs were supposed to solve all problems everywhere. Instead, they are well-intentioned chaos monkeys that generally cause more headaches than they cure. ARC acts as a harness for LLM agents to rein them in, resulting in consistent behavior and higher-quality work in projects.

ARC provides agents with the context, standards, and tools they need to perform as an effective virtual member of your team, and it enforces greater compliance to expectations and ensures thorough documentation.

## Getting Started

### Compatibility

ARC is a structured set of Markdown files, and theoretically should be compatible with any IDE that supports LLM agents and Markdown. However, ARC currently makes use of some features in **Visual Studio Code** that may not be available in other environments.

The standards around agentic control are constantly evolving, and ARC will be frequently updated to follow the standards that appear to be gaining widespread adoption. Future updates may also include support for features specific to other environments where agents may be deployed.

### Prerequisites

- Visual Studio Code (v1.108.0 or greater is needed or some features may not be available or work properly)
- [GitHub Copilot Chat extension](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat) for VS Code (most recent version available, connected to an LLM provider)
- LLM capable of tool calling
    - If you have a GitHub Copilot subscription, it will provide access to a number of compatible models.
    - If you have an OpenAI (ChatGPT), Anthropic (Claude), or Gemini subscription, they [can all be directly used](https://code.visualstudio.com/docs/copilot/customization/language-models#_add-a-model-from-a-built-in-provider) with the Copilot Chat extension, and many of their models are tool-capable.
    - Local LLMs can be used, too!
    - Any model that you connect to the Copilot Chat extension that is not capable of tool calling will not be shown in the model picker when in agent mode.

### Basic Installation

1. Clone the ARC repository into a folder named **ARC** at the root of your project.
2. Update line 20 of `SEED.md` with the project/repository purpose.
3. Review lines 22-28 of `SEED.md` and do ONE of the following to provide Copilot with instructions on project knowledge:
   - **Keep lines 22-24** - Good for a new project that already has written documentation specifying its scope and constraints
   - **Keep line 26** - Good for a new project that does not yet have a defined specification
   - **Keep line 28** - Best for an established project, or when you don't want to write out your own `SPEC.md` file

4. Run the following prompt with Copilot:
   ```plain
   Review SEED.md and carefully follow the instructions within it. Please refer any questions you have to me.
   ```

   In existing projects, Copilot will review all files and customize ARC according to the seed instructions. In new projects, Copilot will work with you to customize ARC.

5. When ARC has finished installation, review `.agentignore` and add any files there that you want agents to avoid reading. The purpose of this is primarily to focus an agent's attention, but in very large repositories or repositories in which an agent has generated a large amount of documentation, the purpose of `.agentignore` can also be to avoid overflowing an LLM's context window, which causes hallucination.

#### Manual Review

Just as with any other output from an LLM, you should review the installation when it is complete. In VS Code, all files modified by Copilot are marked with a dot surrounded by a rounded square, and when you open one it will show diffs with red and green highlights, along with "Keep" and "Undo" buttons to the right of each diff. Review all customizations to make sure you're satisfied with the installation.

## Using ARC

After installation, ARC provides several components to structure agent behavior:

### Components

| Component | Location | Purpose |
|-----------|----------|---------|
| **Agents** | `.github/agents/` | Specialized AI personas (Coordinator, Architect, Coder, etc.) |
| **Rules** | `.github/instructions/` | Coding standards applied via glob patterns |
| **Commands** | `.github/prompts/` | Reusable user-invoked prompt files |
| **Templates** | `.github/templates/` | File scaffolding blueprints |
| **Skills** | `.github/skills/` | Portable, task-specific capabilities with scripts and resources |

### Getting Started

1. Start conversations with `@coordinator-agent` for general work
2. @coordinator-agent will orchestrate specialized agents as needed
3. Skills are automatically activated based on your prompts
4. Use `/` commands to invoke reusable prompts

### Skills

Skills follow the [Agent Skills open standard](https://agentskills.io/) and work across GitHub Copilot in VS Code, Copilot CLI, and Copilot coding agent. Unlike instructions that are always applied, skills load on-demand when relevant to your task.

To enable skills, set `chat.useAgentSkills: true` in VS Code settings. (ARC will prompt you to do this at the start of a work session)