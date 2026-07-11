#!/usr/bin/env python3
"""Package the Agent Skill into a distributable `.skill` (zip) archive.

Security model: EXPLICIT ALLOWLIST. Only the files that constitute the portable
skill are packaged. Repository-management files (README, CONTRIBUTING, SECURITY,
CHANGELOG, AGENTS, LICENSE, CI config, docs, evals, git metadata, build output,
caches, OS metadata, and any transferred planning or handoff artifacts) are
never included, even if new ones are added to the repository later.

The archive contains exactly one top-level directory named after the skill,
with `SKILL.md` at its root:

    customer-journey-lifecycle/
    customer-journey-lifecycle/SKILL.md
    customer-journey-lifecycle/references/...
    customer-journey-lifecycle/assets/...
    customer-journey-lifecycle/examples/...
    customer-journey-lifecycle/scripts/...
"""
from pathlib import Path
import zipfile
import sys

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
# Canonical skill name. validate_skill.py enforces frontmatter name == directory.
TOP = ROOT.name

# Explicit allowlist: the only content permitted in the packaged skill.
ALLOWED_TOP_FILES = {"SKILL.md"}
ALLOWED_TOP_DIRS = {"references", "assets", "examples", "scripts"}

# Defense in depth: never package these, even inside an allowed directory.
DENY_PATH_PARTS = {".git", ".github", "dist", "docs", "evals", "__pycache__"}
DENY_FILENAMES = {".DS_Store", ".gitignore"}
DENY_SUFFIXES = {".pyc", ".pyo", ".swp", ".swo", ".skill", ".zip"}


def is_allowed(rel: Path) -> bool:
    """Return True only for files explicitly permitted in the package."""
    parts = rel.parts
    if any(part in DENY_PATH_PARTS for part in parts):
        return False
    if rel.name in DENY_FILENAMES or rel.suffix.lower() in DENY_SUFFIXES:
        return False
    if len(parts) == 1:
        return rel.name in ALLOWED_TOP_FILES
    return parts[0] in ALLOWED_TOP_DIRS


def main() -> int:
    DIST.mkdir(exist_ok=True)
    out = DIST / f"{TOP}.skill"

    selected = sorted(
        path.relative_to(ROOT)
        for path in ROOT.rglob("*")
        if path.is_file() and is_allowed(path.relative_to(ROOT))
    )

    if Path("SKILL.md") not in selected:
        print("Refusing to package: SKILL.md is not in the allowlisted set.")
        return 1

    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as archive:
        for rel in selected:
            archive.write(ROOT / rel, f"{TOP}/{rel.as_posix()}")

    # Self-check the produced archive against the required layout.
    with zipfile.ZipFile(out) as archive:
        names = archive.namelist()
    top_levels = {name.split("/", 1)[0] for name in names}
    if top_levels != {TOP}:
        out.unlink(missing_ok=True)
        print(f"Refusing to package: unexpected top-level entries {sorted(top_levels)}.")
        return 1
    if f"{TOP}/SKILL.md" not in names:
        out.unlink(missing_ok=True)
        print(f"Refusing to package: {TOP}/SKILL.md missing from archive.")
        return 1

    print(f"Packaged {len(names)} files into {out}")
    for rel in selected:
        print(f"  {TOP}/{rel.as_posix()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
