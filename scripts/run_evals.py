#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
prompt_file = ROOT / "evals/prompts.yaml"
rubric_file = ROOT / "evals/rubric.md"

errors = []
if not prompt_file.exists():
    errors.append("Missing evals/prompts.yaml")
if not rubric_file.exists():
    errors.append("Missing evals/rubric.md")

if errors:
    for error in errors:
        print(error)
    sys.exit(1)

text = prompt_file.read_text(encoding="utf-8")
case_count = text.count("\n  - id:")
if case_count < 6:
    print("Add at least six eval cases.")
    sys.exit(1)

print(f"Eval scaffolding valid with {case_count} cases.")
print("Model-execution evals are intentionally not run by this local structural check.")
