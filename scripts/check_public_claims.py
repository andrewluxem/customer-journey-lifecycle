#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
TEXT_EXTENSIONS = {".md", ".txt", ".yaml", ".yml", ".json", ".csv", ".py"}

# Generic patterns that usually indicate leaked private-source labels or
# unsupported quantitative claims. Findings require deliberate review.
patterns = {
    "private distribution marker": re.compile(
        r"\b(internal only|do not distribute|not for distribution|private source title)\b",
        re.I,
    ),
    "email address": re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I),
    "currency claim": re.compile(r"[$€£]\s?\d"),
    "percentage claim": re.compile(r"\b\d+(?:\.\d+)?\s?%"),
    "performance lift": re.compile(r"\b\d+(?:\.\d+)?\s?[x×]\b|\blift(?:ed)?\s+(?:by\s+)?\d", re.I),
    "large population shorthand": re.compile(r"\b\d+(?:\.\d+)?\s?(?:k|m|mm|b)\b", re.I),
}

excluded = {
    Path("docs/sanitization-policy.md"),
    Path("scripts/check_public_claims.py"),
    Path("LICENSE"),
}

findings = []
for path in ROOT.rglob("*"):
    if not path.is_file() or path.suffix.lower() not in TEXT_EXTENSIONS:
        continue
    rel = path.relative_to(ROOT)
    if rel in excluded:
        continue
    text = path.read_text(encoding="utf-8", errors="ignore")
    for label, pattern in patterns.items():
        for match in pattern.finditer(text):
            line = text.count("\n", 0, match.start()) + 1
            findings.append((str(rel), line, label, match.group(0)))

if findings:
    print("Public-claim review required:")
    for rel, line, label, value in findings:
        print(f"- {rel}:{line}: {label}: {value!r}")
    sys.exit(1)

print("No high-risk public claims detected.")
