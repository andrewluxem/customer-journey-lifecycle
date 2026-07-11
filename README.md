# Customer Journey Lifecycle Skill

A vendor-neutral Agent Skill for designing, auditing, prioritizing, and measuring customer lifecycle systems.

It helps teams move from disconnected campaigns to a shared operating model:

**customer state → signal → eligibility → need → candidate action → priority → channel and timing → experience → outcome → next state**

## What the skill can produce

- lifecycle and commercial-funnel maps
- customer-state taxonomies
- transition-opportunity matrices
- current-state journey inventories and coverage audits
- onboarding, adoption, engagement, expansion, retention, and win-back designs
- channel and owned-surface registries
- contact-priority and suppression policies
- progressive-profiling and preference strategies
- measurement and experimentation plans
- implementation roadmaps

## Design principles

- State before campaign.
- Behavior and context before generic calendar sequences.
- One clear next customer outcome.
- Eligibility and suppression are first-class logic.
- Contextual expansion instead of indiscriminate upsell.
- Detect deterioration before full lapse.
- Coordinate channels and surfaces.
- Respect preferences, privacy, and attention.
- Measure incremental state movement.
- Validate attribution before optimizing.
- Automate validated logic, not untested assumptions.
- Treat no action as a legitimate decision.

## Repository layout

- `SKILL.md` — the canonical Agent Skill
- `references/` — detailed methods loaded only when relevant
- `assets/` — reusable templates
- `examples/` — fictional, non-benchmark examples
- `evals/` — activation and output-quality tests
- `scripts/` — validation, packaging, and public-safety checks
- `docs/` — architecture, compatibility, and contribution guidance

## Installation

### ChatGPT

Download the packaged `.skill` release and upload it from the Skills page.

### Claude Code

Clone or link this repository as:

```text
~/.claude/skills/customer-journey-lifecycle
```

For project-only use:

```text
.claude/skills/customer-journey-lifecycle
```

### Cursor

Clone or link this repository as:

```text
.cursor/skills/customer-journey-lifecycle
```

### Gemini CLI

```bash
gemini skills install https://github.com/andrewluxem/customer-journey-lifecycle
```

For local development:

```bash
gemini skills link .
```

### Other compatible agents

Use:

```text
.agents/skills/customer-journey-lifecycle
```

or the location documented by the client.

## Example requests

- “Define a customer-state model for a subscription service.”
- “Audit these journeys for overlap, missing suppressions, and measurement gaps.”
- “Design a first-value onboarding journey.”
- “Create a contact governance policy across email, push, paid media, and in-product messaging.”
- “Prioritize the highest-value lifecycle transitions without inventing benchmarks.”
- “Build a current-state journey inventory and coverage heatmap.”
- “Design a controlled win-back experiment with a sunset rule.”

## Publication standard

This repository contains no restricted metrics, internal source documents, company-specific examples, proprietary system names, or historical performance claims. Contributions must follow `docs/sanitization-policy.md`.
