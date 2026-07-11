# Customer-State Model

## Core premise

Every known customer should resolve to one operational state at a given decision moment. The state model should drive eligibility and message routing rather than forcing each channel to re-derive logic independently.

## Choose orthogonal dimensions

Use a small set of dimensions that are:

- mutually exclusive within each dimension
- collectively exhaustive
- queryable from available data
- stable enough to act on
- meaningful for eligibility or treatment

Common dimensions:

- relationship status
- lifecycle status
- engagement recency
- engagement frequency
- product or feature adoption
- plan or tier
- commercial status
- value tier
- risk status
- channel permission
- explicit preferences

Do not multiply the state count with every possible modifier. Keep a compact operational state model and use selected modifiers for treatment variants.

## State definition template

For each state define:

- state ID and plain-language name
- derivation rule
- data sources
- refresh cadence
- eligible offers or actions
- ineligible actions
- primary desired transition
- alternate transitions
- guardrails
- population and value fields, when available
- success and exit conditions

## Rollups

Maintain:

- full-grain states for eligibility and analytics
- messaging groups for shared treatment
- executive rollups for reporting

## One source of truth

State assignment should be computed once in a governed data product and consumed by channels and surfaces. Avoid independent channel logic that produces contradictory states.

## State quality checks

- no customer is assigned to multiple mutually exclusive states
- unknown or stale data has an explicit fallback state
- state changes are logged
- derivation logic is versioned
- trial, eligibility, and permission logic are separated
- completed outcomes trigger immediate suppression
- thresholds are configurable and evidence-based
