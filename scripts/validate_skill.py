#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"

errors = []

if not SKILL.exists():
    errors.append("SKILL.md is missing.")
else:
    text = SKILL.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        errors.append("SKILL.md must begin with YAML frontmatter.")
    else:
        frontmatter = match.group(1)
        name_match = re.search(r"^name:\s*(.+)$", frontmatter, re.M)
        desc_match = re.search(r"^description:\s*(.+)$", frontmatter, re.M)
        if not name_match:
            errors.append("Frontmatter requires name.")
        else:
            name = name_match.group(1).strip().strip('"')
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
                errors.append("Name must use lowercase letters, numbers, and single hyphens.")
            if name != ROOT.name:
                errors.append(f"Name '{name}' must match directory '{ROOT.name}'.")
        if not desc_match or not desc_match.group(1).strip():
            errors.append("Frontmatter requires a non-empty description.")
        elif len(desc_match.group(1).strip()) > 1024:
            errors.append("Description exceeds 1024 characters.")
    if len(text.splitlines()) > 500:
        errors.append("SKILL.md exceeds 500 lines.")

required = [
    "references/operating-model.md",
    "references/customer-states.md",
    "references/journey-design.md",
    "references/orchestration-governance.md",
    "references/channels-surfaces.md",
    "references/data-preferences-privacy.md",
    "references/measurement-experimentation.md",
    "references/implementation-playbook.md",
]
for rel in required:
    if not (ROOT / rel).exists():
        errors.append(f"Missing required reference: {rel}")

if errors:
    print("Validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("Skill structure is valid.")
