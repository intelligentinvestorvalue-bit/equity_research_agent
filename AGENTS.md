# AGENTS.md

## Cursor Cloud specific instructions

Local equity research app: Python FastAPI web UI + CLI. Data comes from live network sources (Yahoo Finance via `yfinance`, SEC EDGAR via `edgartools`); egress is open in this environment.

### Environment
- Python deps live in a repo-local venv at `.venv` (created by the startup update script). Activate with `source .venv/bin/activate` or call `./.venv/bin/python` directly.
- `pytest` is installed into the venv by the update script (it is not in `requirements.txt`) so the `tests/` suite can run.
- No Ollama server runs in this environment. `--mode fast` (fundamentals + put screen) works fully; `--mode deep`/`comprehensive` still run but the LLM steps use the built-in rule-based fallback instead of Llama.

### Run
- CLI: `./.venv/bin/python main.py --ticker AAPL --mode fast`. Outputs land in `output/` (`{TICKER}_analysis_report.md`, `{TICKER}_financials.json`).
- Web UI (dev): `./.venv/bin/python -m uvicorn app.api:app --host 0.0.0.0 --port 8000` then open `http://localhost:8000`. The PowerShell `scripts/*.ps1` helpers are Windows-only; use the uvicorn command directly here.
- Tests: `./.venv/bin/python -m pytest -q`.

`.env` is optional (all keys are commented defaults); the app runs without it.
