# Evaluation Rubric

Score each dimension from 0 to 2.

## Activation

- 0: skill does not activate for a relevant request or activates for an unrelated request
- 1: activation is inconsistent
- 2: activation is appropriate

## State framing

- 0: output is campaign-first
- 1: state is present but incomplete
- 2: current and desired states are explicit

## Eligibility and suppression

- 0: missing
- 1: partial
- 2: clear eligibility, exclusions, and completed-action suppression

## Customer value

- 0: business-only treatment
- 1: customer benefit is weak
- 2: customer objective and need drive the design

## No-action branch

- 0: absent
- 1: mentioned
- 2: operational condition is defined

## Governance

- 0: ignores competing journeys
- 1: acknowledges conflict
- 2: defines priority and ownership

## Measurement

- 0: uses engagement-only or invented benchmarks
- 1: transition metric without robust design
- 2: transition outcome, guardrails, control, and data-quality checks

## Public safety

- 0: leaks identifying or unsupported material
- 1: ambiguous
- 2: neutral, assumption-labeled, and public-safe

## Actionability

- 0: generic advice
- 1: useful but incomplete
- 2: produces a ready-to-use artifact or clear next step

A release candidate should average at least 1.7 with no zero in public safety, no-action, or measurement.
