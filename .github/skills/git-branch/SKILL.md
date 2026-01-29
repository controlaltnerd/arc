---
name: git-branch
description: Create and manage git branches using consistent naming conventions. Create feature branches, bugfix branches, and other work branches following the repository's naming standards.
---

# Git Branch

## Overview

Create and manage git branches using consistent, descriptive naming conventions. Branch names should communicate the type of work and the specific change at a glance.

## Branch Naming Format

**Format**: `<type>/<short-description>` (kebab-case)

**Types**: 
- `feat` - New feature
- `bugfix` - Bug fix
- `docs` - Documentation update
- `test` - Test additions or updates
- `chore` - Maintenance, dependencies, tooling
- `perf` - Performance improvement
- `refactor` - Code refactoring
- `ci` - CI/CD or configuration changes

**Examples**:
- `feat/oauth-token-refresh`
- `bugfix/null-pointer-exception`
- `docs/update-readme-macos`
- `test/add-parser-coverage`
- `refactor/simplify-auth-flow`
- `perf/optimize-query-performance`
- `chore/upgrade-dependencies`
- `ci/add-github-workflows`

## Naming Rules

- **Keep total length under 50 characters**: Concise but descriptive
- **Use hyphens to separate words**: No underscores or spaces
- **Use lowercase**: Consistency across all branches
- **Be descriptive but concise**: Someone reading the branch name should understand the purpose
- **Match the commit type when possible**: Align branch type with the commit type that will be created

## Creating Branches

### From Current Branch

```bash
# Create and checkout a new branch
git checkout -b feat/oauth-token-refresh

# Or using the newer git switch syntax
git switch -c feat/oauth-token-refresh
```

### From Specific Branch or Commit

```bash
# Create from main
git checkout -b bugfix/parser-issue origin/main

# Create from a specific commit
git checkout -b hotfix/urgent-fix abc123def
```

### Listing Branches

```bash
# List local branches
git branch

# List remote branches
git branch -r

# List all branches (local and remote)
git branch -a

# List with last commit info
git branch -v
```

## Branch Management

### Rename a Branch

```bash
# Rename current branch
git branch -m new-name

# Rename another branch
git branch -m old-name new-name

# Rename and push (after renaming locally)
git push origin -u new-name
git push origin --delete old-name
```

### Delete a Branch

```bash
# Delete local branch (safe - won't delete unmerged work)
git branch -d branch-name

# Force delete local branch (dangerous - deletes unmerged work)
git branch -D branch-name

# Delete remote branch
git push origin --delete branch-name
```

### Switch Between Branches

```bash
# Checkout (older syntax)
git checkout branch-name

# Switch (newer syntax, recommended)
git switch branch-name

# Switch to previous branch
git switch -

# Create and switch in one command
git switch -c feat/new-feature
```

## Branch Tracking

### Set Upstream

```bash
# Push new branch and set upstream
git push -u origin feat/my-feature

# Or set upstream after pushing
git push origin feat/my-feature
git branch -u origin/feat/my-feature

# Check tracking status
git branch -vv
```

### Pull Updates from Main

```bash
# Rebase your branch on latest main
git fetch origin
git rebase origin/main

# Or merge main into your branch
git merge origin/main
```

## Best Practices

- **One purpose per branch**: Each branch should contain work for a single feature, fix, or improvement
- **Keep branches short-lived**: Merge or delete completed branches promptly (typically within days, not weeks)
- **Name before creating**: Think through the branch name first - it's a communication tool for the team
- **Push early**: Push your branch early so others know you're working on it (even if incomplete)
- **Keep synchronized**: Regularly pull latest main to reduce merge conflicts
- **Descriptive is better than clever**: `feat/user-authentication-oauth` is better than `feat/auth-2`
- **Reference issues when relevant**: If the branch is for a specific issue, consider including the issue number in commit messages rather than branch names

## Git Safety Protocol

- **NEVER delete main/master branch**
- **NEVER force delete a branch** that might contain important work (`-D` instead of `-d`) without confirming
- **NEVER rename branches** on main or master without team coordination
- **NEVER rebase public branches** that others depend on (use merge instead)
- **Test locally first**: Verify branch content before pushing to remote
