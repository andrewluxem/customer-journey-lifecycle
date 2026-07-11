---
name: customer-journey-lifecycle
description: Designs, audits, and prioritizes customer journey lifecycle operating systems. Use for lifecycle strategy, customer-state models, journey inventories, onboarding and adoption, engagement, expansion, retention, win-back, channel and surface planning, contact governance, preference strategy, measurement, experimentation, and implementation roadmaps.
license: Apache-2.0
compatibility: Works with Agent Skills-compatible clients. No external network access is required.
metadata:
  version: "0.1.0"
  category: customer-experience
---

# Customer Journey Lifecycle

Use this skill to turn disconnected campaigns and channels into a customer-state transition system.

## Core operating model

Frame every recommendation as:

**current state → signal → eligibility → customer need → candidate action → priority → channel and timing → experience → outcome → next state**

Always preserve **no action** as a valid candidate.

## Public-safety rules

- Use only information supplied by the user or clearly labeled assumptions.
- Do not invent performance benchmarks, thresholds, conversion rates, financial values, or causal claims.
- Do not reproduce restricted source material, company-specific terminology, internal codenames, or identifying examples.
- Replace proprietary examples with neutral business archetypes.
- Separate observed facts, assumptions, recommendations, and decisions still required.
- Minimize personal data. Do not recommend collecting an attribute unless it has a defined customer benefit or operational purpose.
- Treat legal, privacy, accessibility, consent, security, and data-quality requirements as implementation gates requiring qualified review.

## Intake

Determine the requested outcome and the minimum available context:

- business model and customer relationship
- target population
- customer and business objective
- known lifecycle stages or behaviors
- available data and update cadence
- existing journeys, channels, and surfaces
- constraints, risks, and required output

Do not block progress when context is incomplete. State assumptions and create a discovery list.

## Workflow router

Choose the smallest workflow that satisfies the request.

### Define a lifecycle operating model

Read `references/operating-model.md`.
Produce a lifecycle map, definitions, entry and exit criteria, and unresolved business decisions.

### Build a customer-state model

Read `references/customer-states.md`.
Use `assets/state-taxonomy.yaml`.
Produce orthogonal state dimensions, derivation logic, exclusions, rollups, and candidate transitions.

### Inventory or audit journeys

Read `references/journey-design.md` and `references/orchestration-governance.md`.
Use `assets/current-state-journey-inventory.csv`.
Identify gaps, overlaps, conflicting ownership, missing suppressions, weak exit rules, and measurement risk.

### Design a journey

Read `references/journey-design.md`.
Use `assets/journey-brief.md`.
Define the current state, desired next state, signal, eligibility, need, intervention, channel, timing, behavior check, escalation, exit, re-entry, and control design.

### Prioritize opportunities

Read `references/operating-model.md` and `references/measurement-experimentation.md`.
Rank transitions using evidence strength, reachable population, customer value, business value, feasibility, risk, and learning value. Do not fabricate inputs.

### Plan channels and owned surfaces

Read `references/channels-surfaces.md`.
Use `assets/surface-registry.csv`.
Classify each surface by suitability, targeting, effort, proven opportunity, intrusiveness, measurement, owner, and lead time.

### Create contact governance

Read `references/orchestration-governance.md`.
Use `assets/contact-governance-policy.md`.
Define priority rules, mandatory overrides, frequency limits, cool-downs, mutual exclusions, escalation limits, rejection handling, sunset rules, and a no-action outcome.

### Design data and preference strategy

Read `references/data-preferences-privacy.md`.
Specify the minimum useful data, value exchange, progressive profiling, inferred versus explicit attributes, preference controls, and privacy gates.

### Build a measurement or experimentation plan

Read `references/measurement-experimentation.md`.
Use `assets/measurement-plan.md`.
Define the state transition, primary outcome, guardrails, control or holdout, attribution window, data-quality checks, and decision rule.

### Build an implementation roadmap

Read `references/implementation-playbook.md`.
Use `assets/roadmap.md`.
Sequence discovery, diagnosis, design, pilot, validation, automation, and scale.

## Universal design procedure

For any lifecycle task:

1. Define the customer outcome before the business treatment.
2. Name the current state and desired next state.
3. Identify the observable signal and its freshness.
4. Define eligibility, exclusions, and suppressions.
5. Diagnose the customer barrier or need.
6. Generate candidate interventions, including support, recognition, protection, and no action.
7. Prioritize candidates using comparable criteria.
8. Choose the least intrusive channel or surface that can solve the need.
9. Define timing, cadence, behavior checks, escalation limits, and exit.
10. Define how the outcome updates customer state.
11. Specify measurement, guardrails, data-quality checks, and ownership.
12. Label assumptions and decisions still required.

## Output standard

Unless the user requests another format, include:

- objective
- scope
- facts and evidence
- assumptions
- current state
- desired transition
- recommended design
- suppressions and no-action rule
- measurement approach
- risks and dependencies
- decisions required
- next artifact or implementation step

## Final quality check

Before finishing, verify that:

- the recommendation is state-based rather than campaign-calendar based
- one primary customer outcome is clear
- completed behaviors are suppressed
- competing journeys are resolved
- escalation ends
- no action is possible
- customer preferences and privacy are respected
- channels act as one system
- attribution and event quality are questioned before optimization
- incremental behavior is measured where feasible
- facts, assumptions, proposals, and open decisions are clearly separated
