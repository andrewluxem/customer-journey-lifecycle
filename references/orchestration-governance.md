# Orchestration and Contact Governance

## Candidate-action flow

1. Discover candidate actions from customer, product, transaction, service, preference, and contextual signals.
2. Apply eligibility, consent, content-quality, inventory, availability, and completion checks.
3. Score or rank candidates using customer value, customer benefit, expected behavior, business value, risk, cost, urgency, and confidence.
4. Select the best action, channel, timing, and cadence.
5. Construct the experience.
6. Deliver and capture response.
7. Update customer state and future eligibility.

## Priority policy

Consider:

- mandatory versus discretionary
- customer need and urgency
- expected incremental behavior
- customer and business value
- retention or service risk
- confidence
- offer or treatment cost
- recent contact pressure
- customer preference
- negative feedback
- expiration

## Required controls

- global contact limits
- channel-specific limits
- cool-down periods
- journey mutual exclusions
- mandatory overrides
- onboarding protection
- post-conversion suppression
- completed-action suppression
- escalation limits
- explicit-rejection handling
- re-entry rules
- sunset rules
- no-action outcome

## Ownership

When objectives conflict, one program should own the customer decision for that moment. Protective and service-critical treatments generally outrank promotional activity.

## Confidence

A ranking based on weak evidence should be marked low confidence and treated as a test rather than a permanent policy.

## Governance artifacts

Maintain:

- decision policy
- journey registry
- contact history
- suppression registry
- exception log
- experiment registry
- model or rule version
- owner and approval history
