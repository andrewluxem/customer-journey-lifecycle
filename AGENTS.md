# AGENTS.md

## Repository purpose

Maintain one portable Agent Skill for customer journey lifecycle strategy and operating-model design.

## Required checks

Before submitting changes:

```bash
python scripts/validate_skill.py
python scripts/check_public_claims.py
python scripts/run_evals.py
```

## Content rules

- Keep `SKILL.md` focused and under the Agent Skills recommended limits.
- Put detailed methods in `references/`.
- Use only fictional or neutral examples.
- Do not add company names, internal codenames, private source titles, restricted metrics, or unverified benchmarks.
- Do not state causal impact without evidence and an explicit measurement design.
- Preserve no action, suppression, privacy, accessibility, and data-quality checks.
- Keep facts, assumptions, proposals, and decisions required distinct.

## Contribution style

- Use plain language.
- Prefer reusable frameworks over vendor-specific instructions.
- Add or update eval cases for material behavior changes.
- Update `CHANGELOG.md` for user-visible changes.
