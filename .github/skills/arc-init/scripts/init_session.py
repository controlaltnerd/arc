#!/usr/bin/env python3
"""
ARC Session Initialization Script

Gathers git configuration and repository information for session context.
Outputs JSON with gathered information and any warnings.
"""

import json
import subprocess
import sys
from pathlib import Path


def run_git_command(args):
    """Run a git command and return the output, or None if it fails."""
    try:
        result = subprocess.run(
            ["git"] + args,
            capture_output=True,
            text=True,
            check=True,
            timeout=5
        )
        return result.stdout.strip()
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, FileNotFoundError):
        return None


def gather_session_context():
    """Gather git and repository information for session initialization."""
    context = {
        "git_username": "User",
        "git_email": "",
        "current_branch": "unknown",
        "repo_root": "",
        "warnings": []
    }
    
    # Get git username
    username = run_git_command(["config", "user.name"])
    if username:
        context["git_username"] = username
    else:
        context["warnings"].append("Git user.name not configured")
    
    # Get git email
    email = run_git_command(["config", "user.email"])
    if email:
        context["git_email"] = email
    else:
        context["warnings"].append("Git user.email not configured")
    
    # Get current branch
    branch = run_git_command(["branch", "--show-current"])
    if branch:
        context["current_branch"] = branch
    else:
        # Try to get detached HEAD info
        ref = run_git_command(["rev-parse", "--short", "HEAD"])
        if ref:
            context["current_branch"] = f"detached@{ref}"
            context["warnings"].append("Not on a branch (detached HEAD)")
        else:
            context["warnings"].append("Unable to determine current branch")
    
    # Get repository root
    repo_root = run_git_command(["rev-parse", "--show-toplevel"])
    if repo_root:
        context["repo_root"] = repo_root
    else:
        context["warnings"].append("Not in a git repository")
    
    return context


def main():
    """Main entry point for session initialization."""
    try:
        context = gather_session_context()
        print(json.dumps(context, indent=2))
        
        # Exit with status 0 even if there are warnings
        # Exit with status 1 only on critical failures
        return 0
    except Exception as e:
        # Critical failure - output error as JSON
        error_context = {
            "git_username": "User",
            "git_email": "",
            "current_branch": "unknown",
            "repo_root": "",
            "warnings": [f"Critical error during initialization: {str(e)}"]
        }
        print(json.dumps(error_context, indent=2))
        return 1


if __name__ == "__main__":
    sys.exit(main())
