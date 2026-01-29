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


def check_branch_sync(current_branch):
    """
    Check sync status between local and remote branches.
    
    Returns dict with branch sync information including:
    - current_branch_status: sync status of the current branch
    - out_of_sync_branches: list of branches that are out of sync
    - fetch_failed: whether git fetch failed
    - fetch_error: error message if fetch failed
    """
    sync_info = {
        "current_branch_status": "unknown",
        "out_of_sync_branches": [],
        "fetch_failed": False,
        "fetch_error": None
    }
    
    # Check if remote exists
    try:
        result = subprocess.run(
            ["git", "remote", "-v"],
            capture_output=True,
            text=True,
            timeout=5
        )
        if not result.stdout.strip():
            sync_info["fetch_error"] = "No remote configured"
            return sync_info
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
        sync_info["fetch_error"] = "Unable to check remote configuration"
        return sync_info
    
    # Perform git fetch
    try:
        subprocess.run(
            ["git", "fetch", "--all", "--quiet"],
            capture_output=True,
            text=True,
            check=True,
            timeout=30
        )
    except subprocess.TimeoutExpired:
        sync_info["fetch_failed"] = True
        sync_info["fetch_error"] = "Git fetch timed out (30s limit)"
        return sync_info
    except subprocess.CalledProcessError as e:
        sync_info["fetch_failed"] = True
        error_msg = e.stderr.strip() if e.stderr else "Unknown error"
        if "authentication" in error_msg.lower() or "permission" in error_msg.lower():
            sync_info["fetch_error"] = "Authentication required - check credentials"
        else:
            sync_info["fetch_error"] = f"Fetch failed: {error_msg}"
        return sync_info
    except FileNotFoundError:
        sync_info["fetch_failed"] = True
        sync_info["fetch_error"] = "Git command not found"
        return sync_info
    
    # Get branch tracking information
    try:
        result = subprocess.run(
            ["git", "for-each-ref", "--format=%(refname:short)|%(upstream:short)|%(upstream:track)", "refs/heads/"],
            capture_output=True,
            text=True,
            check=True,
            timeout=5
        )
        
        branches = result.stdout.strip().split('\n')
        if not branches or branches == ['']:
            return sync_info
        
        for branch_line in branches:
            parts = branch_line.split('|')
            if len(parts) < 2:
                continue
                
            branch_name = parts[0]
            tracking_branch = parts[1] if len(parts) > 1 else ""
            track_status = parts[2] if len(parts) > 2 else ""
            
            # Skip if no tracking branch
            if not tracking_branch:
                if branch_name == current_branch:
                    sync_info["current_branch_status"] = "no_tracking"
                continue
            
            # Parse tracking status
            ahead = 0
            behind = 0
            status = "synced"
            
            if track_status:
                # Parse "[ahead N, behind M]" or "[ahead N]" or "[behind M]"
                if "ahead" in track_status:
                    try:
                        ahead = int(track_status.split("ahead ")[1].split("]")[0].split(",")[0])
                    except (IndexError, ValueError):
                        pass
                if "behind" in track_status:
                    try:
                        behind = int(track_status.split("behind ")[1].split("]")[0])
                    except (IndexError, ValueError):
                        pass
                
                # Determine status
                if ahead > 0 and behind > 0:
                    status = "diverged"
                elif ahead > 0:
                    status = "ahead"
                elif behind > 0:
                    status = "behind"
                else:
                    status = "synced"
            
            # Store current branch status
            if branch_name == current_branch:
                sync_info["current_branch_status"] = status
            
            # Track out of sync branches
            if status != "synced":
                sync_info["out_of_sync_branches"].append({
                    "branch": branch_name,
                    "status": status,
                    "ahead": ahead,
                    "behind": behind,
                    "tracking": tracking_branch
                })
        
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        sync_info["fetch_error"] = "Unable to check branch tracking status"
    
    return sync_info


def gather_session_context():
    """Gather git and repository information for session initialization."""
    context = {
        "git_username": "User",
        "git_email": "",
        "current_branch": "unknown",
        "repo_root": "",
        "branch_sync": None,
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
    
    # Check branch sync status (only if in a git repo)
    if context["repo_root"]:
        sync_status = check_branch_sync(context["current_branch"])
        context["branch_sync"] = sync_status
        
        # Add warnings for sync issues
        if sync_status.get("fetch_failed"):
            context["warnings"].append(f"Branch sync check failed: {sync_status.get('fetch_error', 'Unknown error')}")
        elif sync_status.get("fetch_error"):
            context["warnings"].append(sync_status["fetch_error"])
    
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
