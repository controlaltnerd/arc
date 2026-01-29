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
