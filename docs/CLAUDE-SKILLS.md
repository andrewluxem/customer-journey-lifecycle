<!--
  Portable skills catalog — safe to copy into any Some Luck Productions project repo.
  Suggested placement: save as docs/CLAUDE-SKILLS.md, then add one line to the repo's
  AGENTS.md / CLAUDE.md:  "Available skills: see docs/CLAUDE-SKILLS.md"
  (Claude Code reads AGENTS.md/CLAUDE.md automatically; this file is the detail it points to.)
-->

# Claude Skills — Toolkit Catalog

First-party skills available to any Claude Code session on this machine. They are **user-global** (installed under `~/.claude/skills/`, promoted from the canonical `claude-skills-src` repo), so they work in **every** repo automatically — you do not install them per project. This file exists so you, collaborators, and Claude know the toolkit is here and how to use it.

## Are they available here?

They're global, so yes — in any repo. To confirm on this machine:

```bash
ls ~/.claude/skills/ | grep slp-        # expect: slp-infographic-prompts, slp-data-analysis,
                                        # slp-research-validators, slp-academic-search, slp-deck
```

On a **fresh machine or for a collaborator**, install once from the source of truth:

```bash
git clone https://github.com/andrewluxem/claude-skills-src.git
cd claude-skills-src && ./bin/promote.sh --apply     # copies skills into ~/.claude/skills/
# runtime deps for the two that need them:
python3 -m pip install --user --break-system-packages --require-hashes \
  -r skills/slp-academic-search/requirements.lock          # academic search
cd skills/slp-deck && npm ci && npx playwright install chromium   # deck export
```

## The five skills

| Skill | Reach for it when… | Runtime |
|---|---|---|
| `slp-infographic-prompts` | you want an infographic / dense visual explainer | none (feeds `deapi`) |
| `slp-data-analysis` | you're doing Excel/tabular work outside BigQuery | none (reference) |
| `slp-research-validators` | you want guardrails on a research/evidence flow | Python stdlib |
| `slp-academic-search` | you need a citable primary source | Python + deps |
| `slp-deck` | you need to generate a PPTX from HTML slides | Node + Playwright |

---

### `slp-infographic-prompts` — infographic generation
**What:** 87 layout patterns + 66 visual styles + a prompt-scoring rubric. Claude picks a layout that matches the *information shape*, a style that matches the brand, composes and scores a prompt, then renders through your existing `deapi` skill.
**Use for:** BeehiveFlippers BOLO visuals, Craps-AI / SlotsGPT myth-busting graphics, WisdomBranch framework diagrams, AndrewLuxem content.
**How to invoke:** just ask — *"make an infographic that shows X."* Claude reads `~/.claude/skills/slp-infographic-prompts/references/` (layouts, styles, `layout-style-selection.md`) and hands the composed prompt to `deapi` → `/generate-image`.
**Note:** image rendering is `deapi` only; it never calls a third-party image API.

### `slp-data-analysis` — Excel/tabular methodology (reference)
**What:** a decomposed pandas/openpyxl playbook — reading (multi-sheet, large-file), cleaning, filtering, statistics, group-by/pivot/trend, conditional formatting, export.
**Use for:** one-off spreadsheets, brand-export cleanup, quick local pivots — the cases that don't warrant a BigQuery/MicroStrategy round-trip.
**How to invoke:** ask for the spreadsheet task — *"clean and pivot this Excel."* Claude consults the relevant recipe under `~/.claude/skills/slp-data-analysis/capability/` and pairs with the `xlsx` skill for file mechanics.
**Note:** reference methodology, not an installed pipeline; no runtime adopted.

### `slp-research-validators` — research guardrails (stdlib)
**What:** four model-agnostic validators — `source_snapshot` (path-traversal-safe source capture), `validate_evidence`, `validate_outline`, `validate_plan`.
**Use for:** hardening any deep-research / evidence-gathering flow; the `source_snapshot` pattern is the reference for safely writing fetched content to disk.
**How to invoke:**
```bash
python3 ~/.claude/skills/slp-research-validators/scripts/validate_plan.py --help
```
**Note:** zero dependencies — pure Python stdlib.

### `slp-academic-search` — citable literature search
**What:** one dispatcher over arXiv, OpenAlex, Crossref, PubMed/PMC, Semantic Scholar, Google Scholar, and Wikipedia, with per-source fallback. Unified JSON output.
**Use for:** fact-checking gambling-math or health claims, WisdomBranch PKM pieces, anything that must cite research.
**How to invoke:**
```bash
python3 ~/.claude/skills/slp-academic-search/scripts/search.py "<query>" [--source arxiv] [--limit 5]
python3 ~/.claude/skills/slp-academic-search/scripts/paper.py --source arxiv --id <arxiv_id|doi>
```
**Note:** requires the deps in `requirements.lock` (installed via the fresh-machine step above). Semantic Scholar rate-limits anonymous requests and may time out — the other sources cover the gap; add a free S2 API key for reliability. Camoufox crawlers and deepxiv were removed at extraction; do not re-add them.

### `slp-deck` — HTML → PPTX export engine
**What:** converts per-slide HTML into a PPTX (pptxgenjs + echarts + headless Chromium). Complements `archforge-pptx-lint` (that lints; this generates).
**Use for:** WisdomBranch framework decks, AndrewLuxem lead magnets, brand pitch decks.
**How to invoke:**
```bash
node ~/.claude/skills/slp-deck/html_to_pptx.mjs --deck-dir <path-to-deck-with-pages/>
```
**Note:** deps are pre-provisioned (no runtime auto-install); the image fetcher has an SSRF guard + timeout + size cap. Run inside your egress-restricted sandbox for anything that fetches remote images. It's an engine other flows call, not a chat-triggered skill.

---

## Provenance & governance

All five were extracted from **OpenSenseNova/SenseNova-Skills @ `698dd0c`** (MIT), audited and independently verified at **CONDITIONAL / MEDIUM** under an *extract-don't-adopt* posture: retargeted off SenseNova, stripped of the crawler/deepxiv/CN-social pieces, hardened, and pinned. Full provenance is in each skill's `SOURCES.md` and the vault registry (`~/sandbox/audits/audit-registry.md`).

**Source of truth:** `andrewluxem/claude-skills-src`. Edit skills there, never in `~/.claude/skills/` (runtime is deploy output, overwritten on the next `promote.sh --apply`).

**Adding a new tool to the toolkit?** Run it through the 8-check audit first (`repo-audit-prompt` skill → audit in `~/sandbox/audits/` → registry entry). Never `npm install`/`pip install` a new third-party dependency into a skill without clearing it. This catalog documents only what's already cleared.
