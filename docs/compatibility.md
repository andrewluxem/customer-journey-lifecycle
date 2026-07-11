# Compatibility

## Canonical standard

The repository follows the Agent Skills directory format with a required `SKILL.md` and optional references, scripts, and assets.

## Client mapping

| Client | Typical location or method |
|---|---|
| ChatGPT | Upload the packaged skill from the Skills page |
| Claude Code | `~/.claude/skills/customer-journey-lifecycle` or `.claude/skills/customer-journey-lifecycle` |
| Cursor | `.cursor/skills/customer-journey-lifecycle` |
| Gemini CLI | Install from Git or use `.gemini/skills/`, `~/.gemini/skills/`, or the `.agents/skills/` alias |
| Other compatible clients | `.agents/skills/customer-journey-lifecycle` or the client-defined location |

## Compatibility policy

- Keep the canonical `SKILL.md` within the open standard.
- Do not rely on vendor-only frontmatter in the canonical file.
- Put vendor-specific helpers in optional adapter documentation.
- Test automatic activation and explicit invocation in each supported client before release.
- Re-check client documentation at each minor release because installation surfaces can change.
