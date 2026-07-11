# Architecture

## Canonical package

The repository itself is the canonical Agent Skill directory. `SKILL.md` contains the router and universal procedure. Detailed knowledge is stored in one-level-deep references and loaded only when the task requires it.

## Why one skill

The domain has a shared decision chain and common quality gates. Splitting it into many independently triggered skills would create overlapping activation, duplicated doctrine, and inconsistent output. One skill with workflow routing preserves a single operating model while keeping detailed references modular.

## Progressive disclosure

- discovery: name and description
- activation: `SKILL.md`
- task-specific detail: selected files from `references/`
- output construction: selected template from `assets/`

## Portability

The canonical package follows the Agent Skills format. Platform-specific installation paths and release packaging are documented separately; the content remains identical.

## No required tools

Version zero is knowledge- and workflow-focused. Scripts validate and package the repository, but the skill does not require network access or production system access.

## Future optional extensions

- schema validation for state and journey artifacts
- synthetic opportunity scoring
- diagram generation
- spreadsheet export
- optional MCP integrations
- vendor-specific implementation companions maintained outside the canonical skill
