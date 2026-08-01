# GitHub Pages — static research reports

Read-only, styled HTML reports built from `data/sync/` packs. No Ollama, no API, no custom domain required.

## Privacy (important)

GitHub Pages cannot be “branch-private.” Visibility follows the **repo**:

| Repo | Pages |
|---|---|
| **Public** | Site is public (anyone with the URL) |
| **Private** + GitHub Free | Pages **not available** |
| **Private** + GitHub Pro / Team | Can enable **Private** Pages (signed-in viewers only) |

This repo is set **private** when possible so packs are not world-readable. If you are on Free and need a private viewer without Pro, keep using Cloudflare Tunnel + optional Cloudflare Access instead of Pages.

## One-time: turn on Pages

1. Use `main` (after merge).
2. On GitHub: **Settings → Pages**
3. **Build and deployment**
   - Source: **Deploy from a branch**
   - Branch: `main`
   - Folder: `/docs`
4. If the UI offers **Visibility**, choose **Private** (Pro/Team).
5. Save. Wait 1–2 minutes.

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

## Auto-publish from your laptop (no manual git)

After each completed/failed research job the app writes `data/sync/` **and** sets `data/publish_requested`. A Windows scheduled task rebuilds `docs/` and `git push`es.

**One-time on the research laptop:**

```powershell
# Need: git push works without typing a password (Git Credential Manager or: gh auth login)
pip install markdown
.\scripts\install_publish_sync.ps1          # logon + every 10 min
.\scripts\publish_sync.ps1 -Force           # test once
```

Flow:

1. Research finishes → export to `data/sync/` → flag file created  
2. Scheduled task runs `publish_sync.ps1` → rebuild Pages → commit → push  
3. GitHub updates the live site  

Log: `data/publish_sync.log`  
Remove: `.\scripts\install_publish_sync.ps1 -Uninstall`

Manual rebuild still works:

```powershell
python scripts/build_pages_site.py
.\scripts\publish_sync.ps1 -Force
```

## What is published

| Included | Not included |
|---|---|
| Completed report HTML | Live research UI / queue |
| Charts referenced by packs | SQLite / filings cache |
| Index with filter | Ollama / deep-dive runs |
