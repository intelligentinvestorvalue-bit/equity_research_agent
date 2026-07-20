"""SEC EDGAR filing parser (Module B)."""

from __future__ import annotations

import logging
import re
from pathlib import Path
from typing import Any

from src.config import FILINGS_DIR, settings

logger = logging.getLogger(__name__)


SECTION_PATTERNS = {
    "item_1a": [
        re.compile(r"item\s*1a\.?\s*risk\s*factors", re.I),
        re.compile(r"item\s*1a\s*[–\-—]?\s*risk\s*factors", re.I),
    ],
    "item_7": [
        re.compile(r"item\s*7\.?\s*management.?s\s*discussion", re.I),
        re.compile(r"item\s*7\s*[–\-—]?\s*management", re.I),
    ],
}

NEXT_ITEM = re.compile(r"item\s*\d{1,2}[a-z]?\.?\s", re.I)


def _extract_section(text: str, patterns: list[re.Pattern[str]]) -> str | None:
    start = None
    for pat in patterns:
        m = pat.search(text)
        if m:
            start = m.start()
            break
    if start is None:
        return None
    rest = text[start:]
    # skip the header line, find next Item
    after_header = rest.split("\n", 1)[-1]
    nxt = NEXT_ITEM.search(after_header[200:] if len(after_header) > 200 else after_header)
    # search from a small offset to avoid matching the same item header
    search_from = 100
    nxt = NEXT_ITEM.search(after_header[search_from:])
    if nxt:
        return after_header[search_from : search_from + nxt.start()].strip()
    return after_header[:50_000].strip()


def _fetch_via_edgartools(ticker: str) -> tuple[str, dict[str, Any]]:
    from edgar import Company, set_identity

    set_identity(settings.sec_user_agent)
    company = Company(ticker)
    filings = company.get_filings(form="10-K")
    latest = filings.latest()
    meta = {
        "accession_number": getattr(latest, "accession_number", None),
        "filing_date": str(getattr(latest, "filing_date", "")),
        "source": "edgartools",
    }
    text = latest.text() if hasattr(latest, "text") else str(latest)
    return text, meta


def _fetch_via_sec_http(ticker: str) -> tuple[str, dict[str, Any]]:
    """Fallback: SEC company tickers + submissions JSON."""
    import requests

    headers = {"User-Agent": settings.sec_user_agent, "Accept-Encoding": "gzip, deflate"}
    tickers = requests.get("https://www.sec.gov/files/company_tickers.json", headers=headers, timeout=60)
    tickers.raise_for_status()
    data = tickers.json()
    cik = None
    for row in data.values():
        if str(row.get("ticker", "")).upper() == ticker.upper():
            cik = int(row["cik_str"])
            break
    if cik is None:
        raise ValueError(f"CIK not found for ticker {ticker}")

    cik_str = f"{cik:010d}"
    sub = requests.get(f"https://data.sec.gov/submissions/CIK{cik_str}.json", headers=headers, timeout=60)
    sub.raise_for_status()
    recent = sub.json().get("filings", {}).get("recent", {})
    forms = recent.get("form", [])
    accession = None
    primary = None
    filing_date = None
    for i, form in enumerate(forms):
        if form == "10-K":
            accession = recent["accessionNumber"][i]
            primary = recent["primaryDocument"][i]
            filing_date = recent["filingDate"][i]
            break
    if not accession or not primary:
        raise ValueError(f"No 10-K found for {ticker}")

    acc_nodash = accession.replace("-", "")
    url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc_nodash}/{primary}"
    doc = requests.get(url, headers=headers, timeout=120)
    doc.raise_for_status()
    # crude HTML strip
    text = re.sub(r"<script[\s\S]*?</script>", " ", doc.text, flags=re.I)
    text = re.sub(r"<style[\s\S]*?</style>", " ", text, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text)
    meta = {"accession_number": accession, "filing_date": filing_date, "source": "sec_http", "url": url}
    return text, meta


def fetch_10k_sections(ticker: str) -> dict[str, Any]:
    """Fetch latest 10-K and extract Item 1A / Item 7."""
    cache_path = FILINGS_DIR / f"{ticker.upper()}_10k.txt"
    meta: dict[str, Any] = {}
    text: str

    if cache_path.exists():
        text = cache_path.read_text(encoding="utf-8", errors="replace")
        meta = {"source": "cache", "path": str(cache_path)}
    else:
        try:
            text, meta = _fetch_via_edgartools(ticker)
        except Exception as exc:  # noqa: BLE001
            logger.warning("edgartools failed (%s); trying SEC HTTP", exc)
            text, meta = _fetch_via_sec_http(ticker)
        cache_path.write_text(text, encoding="utf-8", errors="replace")
        meta["path"] = str(cache_path)

    item_1a = _extract_section(text, SECTION_PATTERNS["item_1a"])
    item_7 = _extract_section(text, SECTION_PATTERNS["item_7"])

    return {
        "ticker": ticker.upper(),
        "meta": meta,
        "item_1a": item_1a,
        "item_7": item_7,
        "item_1a_chars": len(item_1a or ""),
        "item_7_chars": len(item_7 or ""),
        "extraction_ok": bool(item_1a or item_7),
    }


def save_section_blocks(sections: dict[str, Any], out_dir: Path | None = None) -> dict[str, str]:
    out_dir = out_dir or FILINGS_DIR
    paths: dict[str, str] = {}
    ticker = sections["ticker"]
    for key in ("item_1a", "item_7"):
        body = sections.get(key)
        if not body:
            continue
        path = out_dir / f"{ticker}_{key}.txt"
        path.write_text(body, encoding="utf-8")
        paths[key] = str(path)
    return paths
