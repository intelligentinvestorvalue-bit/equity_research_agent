# One-time owner actions (GitHub UI)

The cloud agent token cannot change default branch or visibility (HTTP 403). Do these once in the browser while logged into **intelligentinvestorvalue-bit**:

## 1) Default branch → `main`

1. Open https://github.com/intelligentinvestorvalue-bit/equity_research_agent/settings  
2. **General → Default branch** → switch to `main` → Update  
3. Then delete the old default:  
   https://github.com/intelligentinvestorvalue-bit/equity_research_agent/branches  
   Delete `cursor/scaffold-local-equity-research`

## 2) Make the repo private (recommended)

1. Same Settings page → **Danger Zone → Change repository visibility → Private**  
2. Confirm

**Pages privacy:**

| Your plan | After repo is private |
|---|---|
| GitHub Free | Pages is unavailable on private repos |
| GitHub Pro / Team | Settings → Pages → Visibility → **Private** |

If you stay on Free and need a private viewer, keep using Cloudflare Tunnel (already in this repo) instead of public Pages.

## 3) Enable Pages

**Settings → Pages → Deploy from a branch → `main` / `/docs`**

URL: `https://intelligentinvestorvalue-bit.github.io/equity_research_agent/`

## 4) Laptop auto-publish (no manual git)

```powershell
cd C:\DevWork\equity_research_agent
git checkout main
git pull
pip install markdown
.\scripts\install_publish_sync.ps1
.\scripts\publish_sync.ps1 -Force
```

Require: `git push` works without a password prompt (`gh auth login` or Git Credential Manager).
