# GitHub Pages — static research reports

Read-only, styled HTML reports built from `data/sync/` packs. No Ollama, no API, no custom domain required.

## One-time: turn on Pages

1. Merge this branch to `main` (or use `main` after merge).
2. On GitHub: **Settings → Pages**
3. **Build and deployment**
   - Source: **Deploy from a branch**
   - Branch: `main`
   - Folder: `/docs`
4. Save. Wait 1–2 minutes.

## URL (open from anywhere)

```
https://intelligentinvestorvalue-bit.github.io/equity_research_agent/
```

Individual reports:

```
https://intelligentinvestorvalue-bit.github.io/equity_research_agent/reports/<ticker>-<jobid8>.html
```

Example: `.../reports/rblx-d6306a94.html`

If the site 404s: confirm Pages source is `main` + `/docs`, and that `docs/index.html` exists on `main`.

## Rebuild after new research

On the machine that has fresh `data/sync/` jobs:

```bash
pip install markdown
python scripts/build_pages_site.py
git add data/sync docs
git commit -m "Publish latest research reports to GitHub Pages"
git push
```

GitHub republishes `/docs` automatically after the push.

## What is published

| Included | Not included |
|---|---|
| Completed report HTML | Live research UI / queue |
| Charts referenced by packs | SQLite / filings cache |
| Index with filter | Ollama / deep-dive runs |

Keep packs lean: cleanup old local artifacts before syncing; only commit packs you want public (the Pages site is **public** on a public repo).
