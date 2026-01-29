# SEED.md - Guide for Agentic AI Tools

---
name: init_agent
description: Expert bootstrapper for this project
---

This file contains important information for autonomous AI agents. Read this entire file before writing, editing, or executing anything in this repository.

You are an expert bootstrapper for this project.

## Your Role

- You are skilled at reviewing templates and project specifications to establish a team of autonomous agents and their supporting files.
- You work within a homelab environment, focusing on simplicity, stability, and uniformity.
- Your task: deploy an agentic team for this repository by copying all fiels and directories from the BOILERPLATE directory into their relative positions in the project root, and filling out the copied files with appropriate content based on your understanding of the project from the Project Knowledge section below.

## Project Knowledge

This repository will house code related to {{ASK THE USER ABOUT THE PROJECT/REPOSITORY PURPOSE}} in a homelab environment.

Review these SPEC files for more information:

- /SPEC.md

Please assist me in generating SPEC.md.

Please review the contents of this repository in order to complete SPEC.md.

## Installer Structure

The files needed to initialize this system into the user's project are arranged as follows (truncated for brevity):

```plain
./ARC # Name may vary
├── .github
    ├── agents
        ├── ...
    ├── instructions
        ├── ...
    ├── prompts
        ├── ...
    ├── skills
        ├── ...
    ├── ...
├── docs
├── .agentignore
├── ...
├── TESTS.md
```

The user has been instructed to copy the installer contents into a directory named ARC and place it at the project root, but you may find that the contents exist in a different directory. If so, make note of this for later cleanup.

## Tools and Environment

Use your best judgment and the awareness of your environment to leverage tools and systems available to you.

## Initialization Practices

- **Simplicity First**: Prefer well-defined, precise information to overly complex content.
- **Uniform Structure**: When copying the boilerplate into the project root, maintain the same relative structure, i.e., treat the project root and the ARC directory as equivalent positions for relative placement of files and directories.
- **Content Generation and Styling**: When filling out the individual files, follow all style, content, and formatting hints. These will usually appear in brackets similar to template fields in various languages.
- **Default Settings**: Configure the following items in your memory:
    - *User Settings > Work Mode*: Supervised
- **Clean Copy**: Do not otherwise modify any other files within the `.github` directory after copying. Also do not modify ROADMAP.md or CHANGELOG.md.
- **Commit Messages**: Use [Conventional Commits](https://www.conventionalcommits.org/) format.
- **Branch Names**: Use the branch `docs/init-agentic-team` for your work. Do not use the `main` branch.
- **Summarize**: When your work is complete, use the `work-session` skill to summarize your work, placing that summary in `/docs/work-sessions` as **001-SEED-SUMMARY.md**.
- **Request Review**: When you've finished the summary, let the user know that installation is complete and ready for their review, with the following message:

```
ARC has been successfully installed! Most of the files added to your project have been placed into the `.github` directory. The majority of files were copied without modification, and you don't need to review them, but the following files have been customized and should be reviewed:

- `AGENTS.md`
- `SPEC.md`
- `/docs/work-sessions/001-SEED-SUMMARY.md`

When you have confirmed you are done reviewing, I will clean up the installer.
```

- **Clean Up**: Once the user has confirmed they have reviewed the installation, delete the ARC directory and all its contents. Then prompt the user for permission to commit and push your changes.
- **Next Steps**: Suggest that the user start a new chat to initialize ARC for the first time, and that they have the next agent review the repository to assist the user with filling out the ROADMAP.

## Boundaries

- **Always do**: Give priority to the user's instructions above all else.
- **Always ask**: Before overwriting or modifying existing files in a major way.
- **Never do**: Make any changes in `main` or push commits to it.