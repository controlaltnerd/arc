---
name: remember
agent: agent
tools: ['edit', 'read/readFile']
---

The user is asking you to remember something. Ask the user what they want you to remember if it is not provided.

Your memory is a special instruction file located in the project root, at `.github/instructions/memory.instructions.md`.

Each saved memory should be on its own line under the appropriate header, in unordered list format, and should be written concisely for optimal token usage. Keep it simple; additional documentation is often available when needed for a particular task.
