# Public Sanitization Policy

## Purpose

Ensure the public skill contains reusable professional practice without exposing restricted, proprietary, identifying, or unsupported material.

## Scope and attribution exception

Company, employer, and creator-identifying references remain prohibited in methodology and packaged-skill content. This prohibition applies to `SKILL.md`, `references/`, `assets/`, `examples/`, and any packaged artifact.

Repository-level creator attribution in `README.md` is explicitly permitted as an authorship exception. This exception does not permit private source titles, internal terminology, exact performance figures, copied or closely paraphrased source passages, or proprietary examples anywhere, including in `README.md`.

Employer names used only in the creator biography establish professional background. They must not be interpreted as endorsement, sponsorship, or affiliation, and they do not authorize company-specific methodology examples elsewhere in this repository or in the packaged skill.

## Prohibited content

- private or employer-owned source files
- company, product, program, or internal-system names used as source examples
- internal codenames or uncommon internal acronyms
- employee or customer names
- exact historical performance figures
- restricted financial values
- private population sizes
- exact operational thresholds derived from private work
- internal dates, launch schedules, or staffing information
- copied or closely paraphrased source passages
- screenshots or diagrams from private sources
- claims that imply a private organization endorsed the skill

## Required transformations

- rewrite concepts independently in neutral language
- replace brand examples with fictional archetypes
- replace thresholds with configurable variables or user-defined criteria
- replace historical results with measurement instructions
- replace unique system names with functional descriptions
- replace internal incident names with generic failure modes
- separate universal principles from business-specific decisions
- cite only public sources when an external claim is retained

## Numeric-claim policy

Allowed:

- structural numbering
- schema versions
- user-supplied inputs clearly identified as user data
- public-source facts with citation and context

Review required:

- percentages
- currency
- population counts
- performance lifts
- conversion rates
- fixed cadence claims
- hard eligibility or lapse thresholds

## Release gate

A release requires:

- automated public-claim scan
- maintainer content review
- sample-output review
- license and ownership review
- validation that packaged artifacts contain only public files
