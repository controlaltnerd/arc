# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Example entry:

```
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
