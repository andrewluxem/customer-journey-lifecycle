#!/usr/bin/env python3
"""Tests for the attribution allowlist in check_public_claims.py.

Run with: python3 scripts/test_check_public_claims.py

This file is itself scanned by check_public_claims.py, so it must not contain
prohibited literals. It imports the approved values from the scanner module and
builds negative fixtures by concatenation so no email or employer-name literal
ever appears in this source.
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from check_public_claims import (  # noqa: E402
    evaluate_file,
    README,
    APPROVED_EMAIL,
    BIOGRAPHY_COMPANY_NAMES,
)

EMAIL_LABEL = "email address"
COMPANY_LABEL = "company or employer name"


def has(findings, label, value=None):
    return any(
        f[1] == label and (value is None or f[2].lower() == value.lower())
        for f in findings
    )


def test_approved_email_in_readme_passes():
    text = f"# Title\n\nContact: {APPROVED_EMAIL} today.\n"
    findings = evaluate_file(README, text)
    assert not has(findings, EMAIL_LABEL), (
        "approved email in README.md should be allowed"
    )


def test_other_email_in_readme_fails():
    other_email = "person" + "@" + "example.test"
    text = f"# Title\n\nContact: {other_email} today.\n"
    findings = evaluate_file(README, text)
    assert has(findings, EMAIL_LABEL, other_email), (
        "a different email in README.md should still fail"
    )


def test_approved_email_in_skill_fails():
    text = f"Reach me at {APPROVED_EMAIL} today.\n"
    findings = evaluate_file(Path("SKILL.md"), text)
    assert has(findings, EMAIL_LABEL, APPROVED_EMAIL), (
        "the approved email outside README.md should fail"
    )


def test_biography_company_in_readme_section_passes():
    company = BIOGRAPHY_COMPANY_NAMES[0]
    text = (
        "# Customer Journey Lifecycle Skill\n\n"
        "## Built by Andrew Luxem\n\n"
        f"Built retention systems at {company} and elsewhere.\n\n"
        "## Publication standard\n\n"
        "Methodology content is organization-neutral.\n"
    )
    findings = evaluate_file(README, text)
    assert not has(findings, COMPANY_LABEL), (
        "an approved employer name inside the README attribution section "
        "should be allowed"
    )


def test_biography_company_in_reference_fails():
    company = BIOGRAPHY_COMPANY_NAMES[0]
    text = f"This lifecycle pattern was applied at {company}.\n"
    findings = evaluate_file(Path("references/journey-design.md"), text)
    assert has(findings, COMPANY_LABEL, company), (
        "the same employer name in methodology content should fail"
    )


def test_biography_company_outside_readme_section_fails():
    # The employer name is allowed only inside the attribution section, not
    # merely anywhere in README.md.
    company = BIOGRAPHY_COMPANY_NAMES[0]
    text = (
        "# Customer Journey Lifecycle Skill\n\n"
        f"An unrelated mention of {company} in the intro.\n\n"
        "## Built by Andrew Luxem\n\n"
        "Independent personal project.\n"
    )
    findings = evaluate_file(README, text)
    assert has(findings, COMPANY_LABEL, company), (
        "an employer name outside the README attribution section should fail"
    )


TESTS = [
    test_approved_email_in_readme_passes,
    test_other_email_in_readme_fails,
    test_approved_email_in_skill_fails,
    test_biography_company_in_readme_section_passes,
    test_biography_company_in_reference_fails,
    test_biography_company_outside_readme_section_fails,
]


def main():
    failures = 0
    for test in TESTS:
        try:
            test()
            print(f"PASS: {test.__name__}")
        except AssertionError as exc:
            failures += 1
            print(f"FAIL: {test.__name__}: {exc}")
    if failures:
        print(f"{failures} scanner test(s) failed.")
        return 1
    print(f"All {len(TESTS)} scanner attribution tests passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
