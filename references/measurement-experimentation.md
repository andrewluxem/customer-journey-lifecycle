# Measurement and Experimentation

## Measure state movement

Primary measurement should reflect the desired customer transition, not only message engagement.

## Measurement layers

### Delivery

- eligible population
- delivery or exposure
- interaction
- conversion
- opt-out or complaint
- failure rate
- cost

### Behavior

- first value
- activation
- repeat use
- repeat purchase
- adoption
- breadth
- renewal
- recovery
- reactivation

### Business and customer

- incremental margin or value
- churn reduction
- satisfaction
- service impact
- contact fatigue
- long-term engagement
- negative experience

## Experiment design

Define:

- hypothesis
- target state and desired next state
- eligibility
- treatment
- control or holdout
- randomization unit
- primary outcome
- guardrails
- attribution window
- sample and duration assumptions
- stopping rule
- decision rule
- follow-up window

Do not invent effect-size assumptions. Use user-supplied planning inputs or clearly marked sensitivity scenarios.

## Data-quality gate

Before optimization:

- verify event definitions
- check duplicate events
- check missing events
- confirm identity resolution
- validate exposure logging
- validate conversion deduplication
- isolate concurrent experiments
- inspect suspiciously large downstream impact
- version metrics and attribution logic

## Useful test classes

- customer-segment treatment bundles
- product-oriented versus use-case creative
- message structure
- reminder presence and delay
- educational utility content
- milestone recognition
- cadence shape
- channel substitution
- escalation ladder
- surface portfolio tests

## Decision discipline

Do not scale a treatment because an engagement proxy improved while the target customer or business outcome remained unchanged.
