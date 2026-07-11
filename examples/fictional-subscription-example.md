# Fictional Subscription Example

## Context

A fictional digital subscription service wants to improve first value and reduce early disengagement. No performance benchmarks are assumed.

## Current state

New subscriber who has created an account but has not completed the core value action.

## Desired transition

Account created → first meaningful value achieved.

## Signal

Account created, core value action incomplete, contact permission available.

## Candidate actions

- in-product guided setup when the customer returns
- one concise email that explains the value and links to the next action
- support route if setup failure is detected
- no action when the customer has already completed the behavior or lacks permission

## Suppressions

- core action completed
- active service issue requiring a different owner
- channel permission unavailable
- recent equivalent contact
- explicit rejection

## Measurement

Use a customer-level control or holdout where feasible. Measure incremental completion of the core action and monitor opt-out, support contacts, and early cancellation.
