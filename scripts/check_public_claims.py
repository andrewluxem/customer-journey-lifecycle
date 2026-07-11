#!/usr/bin/env python3
"""Scan repository text for leaked private-source labels, unsupported claims,
and identifying company/employer names.

Attribution allowlist (narrow, path- and value-specific): the repository carries
one intentional creator attribution in `README.md`. Exactly two values are
excepted, and only in the exact location described below. Every other email
address, every other use of the approved address, and every use of the approved
employer names outside the README attribution section still fails validation.
No general email, company-name, or identifying-content protection is disabled.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
TEXT_EXTENSIONS = {".md", ".txt", ".yaml", ".yml", ".json", ".csv", ".py"}

# --- Attribution allowlist -------------------------------------------------
# The single approved contact address. Permitted ONLY in README.md; the same
# address anywhere else fails, and any other address (including elsewhere in
# README.md) fails.
APPROVED_EMAIL = "andrew@andrewluxem.com"

# The repository-facing document that may carry creator attribution.
README = Path("README.md")

# Heading that opens the approved creator-attribution section in README.md.
ATTRIBUTION_HEADING = re.compile(r"^## Built by Andrew Luxem\s*$", re.M)

# Employer names that appear in the approved README creator biography. They are
# treated as identifying content everywhere else: permitted ONLY inside the
# README "Built by Andrew Luxem" section, and flagged in SKILL.md, references/,
# assets/, examples/, other scripts, and any packaged artifact.
BIOGRAPHY_COMPANY_NAMES = [
    "Amazon",
    "Ancestry",
    "Stanley Black & Decker",
    "Overstock.com",
    "Bed Bath & Beyond",
    "Big Dill Pickleball Co.",
]


def _company_pattern(names):
    """Build a case-insensitive alternation that matches each employer name,
    anchored on word boundaries wherever the edge character is alphanumeric."""
    parts = []
    for name in names:
        prefix = r"\b" if name[:1].isalnum() else ""
        suffix = r"\b" if name[-1:].isalnum() else ""
        parts.append(prefix + re.escape(name) + suffix)
    return re.compile("|".join(parts), re.I)


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
    "company or employer name": _company_pattern(BIOGRAPHY_COMPANY_NAMES),
}

# Files whose entire contents are exempt because they legitimately enumerate the
# prohibited patterns themselves. This is not the attribution exception.
EXCLUDED = {
    Path("docs/sanitization-policy.md"),
    Path("scripts/check_public_claims.py"),
    Path("LICENSE"),
}


def attribution_section_span(text):
    """Return the (start, end) character offsets of the README creator
    attribution section, or None if the heading is absent. The section runs
    from the "Built by Andrew Luxem" heading to the next Markdown heading or
    end of file."""
    heading = ATTRIBUTION_HEADING.search(text)
    if not heading:
        return None
    start = heading.start()
    following = re.search(r"^#{1,6} ", text[heading.end():], re.M)
    end = heading.end() + following.start() if following else len(text)
    return (start, end)


def is_allowed(rel, label, value, pos, attr_span):
    """Return True only for the narrow, path- and value-specific attribution
    exceptions. Everything else is a finding."""
    if label == "email address":
        # The approved contact address, and only in README.md.
        return rel == README and value.lower() == APPROVED_EMAIL
    if label == "company or employer name":
        # Approved employer names, and only inside the README attribution
        # section — nowhere else, not even elsewhere in README.md.
        return (
            rel == README
            and attr_span is not None
            and attr_span[0] <= pos < attr_span[1]
        )
    return False


def evaluate_file(rel, text):
    """Return a list of (line, label, value) findings for one file's text,
    applying the attribution allowlist. `rel` is the repository-relative path."""
    if rel in EXCLUDED:
        return []
    attr_span = attribution_section_span(text) if rel == README else None
    findings = []
    for label, pattern in patterns.items():
        for match in pattern.finditer(text):
            if is_allowed(rel, label, match.group(0), match.start(), attr_span):
                continue
            line = text.count("\n", 0, match.start()) + 1
            findings.append((line, label, match.group(0)))
    return findings


def scan_repo(root=ROOT):
    """Scan every text file under `root` and return (rel, line, label, value)."""
    findings = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        rel = path.relative_to(root)
        text = path.read_text(encoding="utf-8", errors="ignore")
        for line, label, value in evaluate_file(rel, text):
            findings.append((str(rel), line, label, value))
    return findings


def main():
    findings = scan_repo()
    if findings:
        print("Public-claim review required:")
        for rel, line, label, value in findings:
            print(f"- {rel}:{line}: {label}: {value!r}")
        return 1
    print("No high-risk public claims detected.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
