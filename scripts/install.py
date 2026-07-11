#!/usr/bin/env python3
from pathlib import Path
import argparse
import shutil
import os
import sys

ROOT = Path(__file__).resolve().parents[1]

def target_path(client: str, scope: str, project: Path) -> Path:
    name = ROOT.name
    home = Path.home()
    if client == "claude":
        return (home / ".claude/skills" / name) if scope == "user" else (project / ".claude/skills" / name)
    if client == "cursor":
        if scope == "user":
            raise ValueError("This installer supports project scope for Cursor. Use the client UI for user-level setup.")
        return project / ".cursor/skills" / name
    if client == "gemini":
        return (home / ".gemini/skills" / name) if scope == "user" else (project / ".gemini/skills" / name)
    if client == "agents":
        return (home / ".agents/skills" / name) if scope == "user" else (project / ".agents/skills" / name)
    raise ValueError(f"Unsupported client: {client}")

parser = argparse.ArgumentParser()
parser.add_argument("client", choices=["claude", "cursor", "gemini", "agents"])
parser.add_argument("--scope", choices=["user", "project"], default="project")
parser.add_argument("--project", default=".")
parser.add_argument("--copy", action="store_true", help="Copy instead of symlink.")
args = parser.parse_args()

project = Path(args.project).resolve()
target = target_path(args.client, args.scope, project)
target.parent.mkdir(parents=True, exist_ok=True)

if target.exists() or target.is_symlink():
    print(f"Target already exists: {target}")
    sys.exit(1)

if args.copy:
    shutil.copytree(ROOT, target, ignore=shutil.ignore_patterns(".git", ".github", "dist", "__pycache__"))
else:
    target.symlink_to(ROOT, target_is_directory=True)

print(target)
