# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## 2026.02.05

**Contributor: GitHub Copilot (Claude Haiku 4.5)**

### Changed
- **Streamlined copilot-instructions.md**: Reduced verbosity by ~30% while maintaining critical agent guidance; improved scannability and directiveness [feature/streamline-framework | 07f0918]
- **Optimized coordinator-agent configuration**: Updated default model reference for improved performance and reduced token overhead [feature/streamline-framework | 07f0918]

### Added
- **Structured framework roadmap**: Created 5-phase roadmap for systematic streamlining (core files, agents, instructions, skills, documentation) [feature/streamline-framework | 07f0918]
- **YAML format guidelines for ROADMAP.md**: Established machine-readable format with metadata for LLM agent parsing [feature/streamline-framework | 07f0918]

---

## 2026.01.28

**Contributor: Claude Sonnet 4.5**

### Changed
- **Updated README**: Added instructions for new users to start contributing [#PR | commit-abc123]

### Added
- **Created new docs directory**: Added docs directory to support standardized documentation efforts.

---

## 2026.01.29

**Contributor: User + GitHub Copilot**

### Added
- **arc-init skill**: Automatic session initialization gathering git username, email, branch, and repo root for consistent user attribution
- **Python dependency management**: Skills can declare dependencies in frontmatter; auto-aggregated and installed at session start
- **Branch sync detection**: Git fetch and sync state detection (behind/ahead/diverged/synced) in arc-init with timeout protection [feat/user-enhancements | b933f87]
- **User settings separation**: Dedicated user-settings.instructions.md file for user-specific preferences, gitignored to prevent conflicts [feat/user-enhancements | b933f87]
- **User settings template**: Template file for initializing user settings in new projects [feat/user-enhancements | b933f87]

### Changed
- **Memory skill**: Updated to clarify user settings belong in separate file, not memory [feat/user-enhancements | b933f87]
- **Memory template**: Removed User Settings section to prevent duplication [feat/user-enhancements | b933f87]
- **Dual file structure pattern**: Memory documents critical workflow for syncing changes between .github/ and src/

### Changed
- **Coordinator agent**: Now automatically runs arc-init at session start
- **adr skill**: Uses git config directly for author attribution (portable)
- **work-session skill**: Uses git config directly for contributor names (portable)
- **create-skill**: Documents python_dependencies frontmatter field
- **Memory structure**: Removed Active Context and Progress sections (duplicated other tracking)

[Work Session](docs/work-sessions/002-INIT-UPDATES.md) | [Commit 6d92498]

### Removed
- Deleted test files from various directories
```
