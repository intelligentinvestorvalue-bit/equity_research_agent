"""SEC EDGAR filing parser (Module B)."""

from __future__ import annotations

import logging
import re
from pathlib import Path
from typing import Any

from src.config import FILINGS_DIR, settings

logger = logging.getLogger(__name__)


SECTION_PATTERNS = {
    # Item 1 Business — must not match Item 1A; allow spaced letters (HTML artifacts)
    "item_1": [
        re.compile(r"(?m)^\s*item\s*1(?![a-z])\.?\s+b\s*u\s*s\s*i\s*n\s*e\s*s\s*s\b", re.I),
        re.compile(r"(?m)^\s*item\s*1(?![a-z])\.?\s+description\s+of\s+business\b", re.I),
        re.compile(r"(?m)^\s*item\s*1\s*[–\-—]\s*b\s*u\s*s\s*i\s*n\s*e\s*s\s*s\b", re.I),
        # Fallback without line anchor (some filings wrap oddly)
        re.compile(r"item\s*1(?![a-z])\.?\s+b\s*u\s*s\s*i\s*n\s*e\s*s\s*s\b", re.I),
        re.compile(r"item\s*1(?![a-z])\.?\s+description\s+of\s+business\b", re.I),
    ],
    "item_1a": [
        re.compile(r"(?m)^\s*item\s*1a\.?\s*r\s*i\s*s\s*k\s*f\s*a\s*c\s*t\s*o\s*r\s*s", re.I),
        re.compile(r"item\s*1a\.?\s*r\s*i\s*s\s*k\s*f\s*a\s*c\s*t\s*o\s*r\s*s", re.I),
    ],
    "item_7": [
        re.compile(r"(?m)^\s*item\s*7\.?\s*management.?s\s*discussion", re.I),
        re.compile(r"item\s*7\.?\s*management.?s\s*discussion", re.I),
        re.compile(r"item\s*7\s*[–\-—]?\s*management", re.I),
    ],
}

NEXT_ITEM = re.compile(r"(?m)^\s*item\s*\d{1,2}[a-z]?\.?\s", re.I)
ITEM_1A_BOUNDARY = re.compile(r"(?m)^\s*item\s*1a\.?\s", re.I)


def _extract_section(
    text: str,
    patterns: list[re.Pattern[str]],
    *,
    max_chars: int = 50_000,
    stop_at: re.Pattern[str] | None = None,
) -> str | None:
    """Extract a 10-K section, preferring real body headers over TOC / cross-refs."""
    matches: list[re.Match[str]] = []
    for pat in patterns:
        matches.extend(pat.finditer(text))
    if not matches:
        return None

    by_start = {m.start(): m for m in matches}
    candidates: list[tuple[int, str, bool]] = []

    for start, m in sorted(by_start.items()):
        body_region = text[m.end() :]
        search_from = min(80, max(0, len(body_region) // 20))
        end_rel: int | None = None
        if stop_at is not None:
            m_stop = stop_at.search(body_region[search_from:])
            if m_stop:
                end_rel = search_from + m_stop.start()
        if end_rel is None:
            nxt = NEXT_ITEM.search(body_region[search_from:])
            if nxt:
                end_rel = search_from + nxt.start()
        chunk = body_region[:end_rel] if end_rel is not None else body_region[:max_chars]
        body = chunk.strip()
        if not body:
            continue
        line_start = start == 0 or text[start - 1] in "\n\r"
        candidates.append((start, body, line_start))

    if not candidates:
        return None

    # Prefer earliest line-anchored body that is long enough to be the real section
    # (skips TOC stubs and late cross-references).
    substantial = [(s, b) for s, b, ls in candidates if ls and len(b) >= 2_000]
    if substantial:
        best = min(substantial, key=lambda x: x[0])[1]
    else:
        best = max(candidates, key=lambda x: len(x[1]))[1]
    return best[:max_chars]


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
    """Fetch latest 10-K and extract Item 1 (Business), Item 1A, Item 7."""
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

    item_1 = _extract_section(
        text,
        SECTION_PATTERNS["item_1"],
        max_chars=80_000,
        stop_at=ITEM_1A_BOUNDARY,
    )
    item_1a = _extract_section(text, SECTION_PATTERNS["item_1a"], max_chars=50_000)
    item_7 = _extract_section(text, SECTION_PATTERNS["item_7"], max_chars=50_000)

    return {
        "ticker": ticker.upper(),
        "meta": meta,
        "item_1": item_1,
        "item_1a": item_1a,
        "item_7": item_7,
        "item_1_chars": len(item_1 or ""),
        "item_1a_chars": len(item_1a or ""),
        "item_7_chars": len(item_7 or ""),
        "extraction_ok": bool(item_1 or item_1a or item_7),
    }


def _resolve_cik(ticker: str, headers: dict[str, str]) -> int:
    import requests

    tickers = requests.get("https://www.sec.gov/files/company_tickers.json", headers=headers, timeout=60)
    tickers.raise_for_status()
    data = tickers.json()
    for row in data.values():
        if str(row.get("ticker", "")).upper() == ticker.upper():
            return int(row["cik_str"])
    raise ValueError(f"CIK not found for ticker {ticker}")


def fetch_recent_filings(ticker: str, forms: list[str] | None = None, limit: int = 12) -> dict[str, Any]:
    """
    List recent 10-Q / 8-K (and optional other) filings from SEC submissions JSON.
    Does not fully parse documents — headlines/meta for catalysts.
    """
    import requests

    forms = forms or ["10-Q", "8-K", "10-K"]
    form_set = {f.upper() for f in forms}
    headers = {"User-Agent": settings.sec_user_agent, "Accept-Encoding": "gzip, deflate"}
    try:
        cik = _resolve_cik(ticker, headers)
    except Exception as exc:  # noqa: BLE001
        return {"ticker": ticker.upper(), "recent": [], "ok": False, "error": str(exc)}

    cik_str = f"{cik:010d}"
    try:
        sub = requests.get(
            f"https://data.sec.gov/submissions/CIK{cik_str}.json",
            headers=headers,
            timeout=60,
        )
        sub.raise_for_status()
        recent = sub.json().get("filings", {}).get("recent", {})
    except Exception as exc:  # noqa: BLE001
        return {"ticker": ticker.upper(), "recent": [], "ok": False, "error": str(exc)}

    out: list[dict[str, Any]] = []
    forms_list = recent.get("form", [])
    for i, form in enumerate(forms_list):
        if form not in form_set:
            continue
        accession = recent.get("accessionNumber", [None])[i]
        primary = recent.get("primaryDocument", [None])[i]
        filing_date = recent.get("filingDate", [None])[i]
        desc = None
        if recent.get("primaryDocDescription"):
            try:
                desc = recent["primaryDocDescription"][i]
            except Exception:  # noqa: BLE001
                desc = None
        url = None
        if accession and primary:
            acc_nodash = str(accession).replace("-", "")
            url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc_nodash}/{primary}"
        out.append(
            {
                "form": form,
                "filing_date": filing_date,
                "accession": accession,
                "description": desc or form,
                "url": url,
            }
        )
        if len(out) >= limit:
            break

    return {
        "ticker": ticker.upper(),
        "cik": cik,
        "recent": out,
        "ok": bool(out),
        "notes": ["Headlines/meta only — documents not fully parsed in this pass."],
    }


def format_recent_filings_markdown(filings: dict[str, Any]) -> str:
    lines = ["## Recent SEC filings (10-Q / 8-K)", ""]
    if filings.get("error"):
        lines.append(f"**Error:** {filings['error']}")
        lines.append("")
        return "\n".join(lines) + "\n"
    rows = filings.get("recent") or []
    if not rows:
        lines.append("_No recent filings found._")
        lines.append("")
        return "\n".join(lines) + "\n"
    lines.append("| Date | Form | Description |")
    lines.append("|---|---|---|")
    for r in rows:
        desc = (r.get("description") or "").replace("|", "/")
        link = r.get("url")
        if link:
            desc = f"[{desc}]({link})"
        lines.append(f"| {r.get('filing_date')} | {r.get('form')} | {desc} |")
    lines.append("")
    for n in filings.get("notes") or []:
        lines.append(f"_{n}_")
    lines.append("")
    return "\n".join(lines) + "\n"


def save_section_blocks(sections: dict[str, Any], out_dir: Path | None = None) -> dict[str, str]:
    out_dir = out_dir or FILINGS_DIR
    paths: dict[str, str] = {}
    ticker = sections["ticker"]
    for key in ("item_1", "item_1a", "item_7"):
        body = sections.get(key)
        if not body:
            continue
        path = out_dir / f"{ticker}_{key}.txt"
        path.write_text(body, encoding="utf-8")
        paths[key] = str(path)
    return paths
