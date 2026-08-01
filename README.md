# Equity Research Agent

Local equity research app: fundamentals + options (yfinance), SEC 10-K parsing, and Llama via Ollama. Use the CLI on your PC, or open the web UI from an iPhone/iPad on the same Wi‑Fi.

## Prerequisites

- Python 3.11+
- [Ollama](https://ollama.com) with `llama3` (or set `OLLAMA_MODEL` in `.env`)
- Network access to Yahoo Finance and SEC EDGAR

## Setup

```powershell
cd c:\DevWork\equity_research_agent
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
# Edit .env: set SEC_USER_AGENT to your name + email (SEC requirement)
```

Pull the model (once):

```powershell
ollama pull llama3
```

## Run web UI (PC + phone)

```powershell
.\scripts\start_local.ps1
```

- PC: http://127.0.0.1:8000  
- iPhone/iPad: http://YOUR_LAN_IP:8000 (script prints the IP)

If the phone cannot connect: same Wi‑Fi (not Guest), Windows Firewall allow TCP 8000, servers bind `0.0.0.0`.

Optional LAN PIN: set `ACCESS_PIN` in `.env`.

### Keep-alive (auto-start on login)

Starts the web app at Windows logon and re-checks every 15 minutes. Cursor does **not** need to stay open.

```powershell
.\scripts\install_ensure_online.ps1
.\scripts\ensure_online.ps1 -SkipTunnel   # test now (local only)
```

- Local UI: http://127.0.0.1:8000  
- Log: `data/ensure_online.log`  
- Optional remote tunnel + ntfy: see [CLOUDFLARE_TUNNEL.md](./CLOUDFLARE_TUNNEL.md) (set `ENSURE_SKIP_TUNNEL=1` in `.env` while the tunnel is flaky).

## CLI

```powershell
python main.py --ticker AAPL --mode fast
python main.py --ticker AAPL --mode deep
```

Outputs:

- `output/{TICKER}_financials.json`
- `output/{TICKER}_analysis_report.md`

## Modes

| Mode | What runs |
|------|-----------|
| `fast` | Fundamentals + put screen |
| `deep` | Above + 10-K Item 1A/7 + Ollama (or rule-based fallback) |

## Cloud ↔ local sync

Research jobs are stored in local SQLite (`data/research.db`, gitignored). To keep **Cursor Cloud** and **local** in sync:

1. After a research run finishes, the app writes packs to `data/sync/` (JSON + report markdown + charts).
2. Commit and push `data/sync/` from that environment.
3. On the other environment: `git pull`, then start the app (startup auto-imports) or run:

```powershell
python -m src.sync_cli import
python -m src.sync_cli export   # push existing local DB jobs into data/sync/
python -m src.sync_cli status
```

API helpers: `POST /api/sync/import`, `POST /api/sync/export`.

## GitHub Pages (read-only reports)

Styled static viewer of completed `data/sync/` packs — open from any browser, no laptop tunnel.

```powershell
pip install markdown
python scripts/build_pages_site.py          # writes docs/
.\scripts\install_publish_sync.ps1          # auto push after research (Task Scheduler)
.\scripts\publish_sync.ps1 -Force           # test publish now
```

Enable once: GitHub **Settings → Pages → Deploy from branch → `main` / `/docs`**.

URL: `https://intelligentinvestorvalue-bit.github.io/equity_research_agent/`

Privacy and auto-publish details: [GITHUB_PAGES.md](./GITHUB_PAGES.md).

## Fallbacks (built in)

- Ollama down → keyword/rule-based text summary
- edgartools fails → direct SEC HTTP + cached filing under `data/filings/`
- Options deltas missing → % OTM put filter
- IV rank → deferred (needs historical cache)

Not investment advice.
