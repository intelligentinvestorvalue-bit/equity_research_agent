"""Web / news search and URL text extraction for research grounding."""

from __future__ import annotations

import logging
import re
from typing import Any
from urllib.parse import urlparse

import httpx

logger = logging.getLogger(__name__)

USER_AGENT = (
    "EquityResearchAgent/0.2 (+local research; respectful fetch; "
    "contact via SEC_USER_AGENT in .env)"
)

SKIP_HOST_FRAGMENTS = (
    "facebook.com",
    "twitter.com",
    "x.com",
    "instagram.com",
    "tiktok.com",
    "youtube.com",
    "linkedin.com",
)


def _safe_host(url: str) -> str:
    try:
        return (urlparse(url).hostname or "").lower()
    except Exception:  # noqa: BLE001
        return ""


def _should_skip_url(url: str) -> bool:
    host = _safe_host(url)
    if not host:
        return True
    return any(frag in host for frag in SKIP_HOST_FRAGMENTS)


def search_duckduckgo(query: str, max_results: int = 8, kind: str = "text") -> list[dict[str, Any]]:
    """
    Search via ddgs (DuckDuckGo).
    kind: "text" | "news"
    """
    try:
        try:
            from ddgs import DDGS
        except ImportError:  # pragma: no cover
            from duckduckgo_search import DDGS  # type: ignore
    except ImportError as exc:  # pragma: no cover
        raise RuntimeError("ddgs is not installed. Run: pip install ddgs") from exc

    results: list[dict[str, Any]] = []
    with DDGS() as ddgs:
        if kind == "news":
            raw = ddgs.news(query, max_results=max_results)
        else:
            raw = ddgs.text(query, max_results=max_results)
        for item in raw or []:
            url = item.get("url") or item.get("href") or ""
            if not url or _should_skip_url(url):
                continue
            results.append(
                {
                    "title": item.get("title") or "",
                    "url": url,
                    "snippet": item.get("body") or item.get("excerpt") or item.get("description") or "",
                    "source": item.get("source") or _safe_host(url),
                    "date": item.get("date") or item.get("published") or "",
                    "kind": kind,
                    "query": query,
                }
            )
    return results


def build_research_queries(
    ticker: str,
    company_name: str | None = None,
    goal: str = "",
    extra_queries: list[str] | None = None,
) -> list[str]:
    """Default query set for analyst / news / sector drivers."""
    name = (company_name or ticker).strip()
    queries = [
        f"{ticker} stock analyst price target",
        f"{name} ({ticker}) earnings OR outlook OR guidance",
        f"{ticker} news",
    ]
    goal = (goal or "").strip()
    if goal:
        queries.append(f"{ticker} {goal}")
    for q in extra_queries or []:
        q = (q or "").strip()
        if q and q not in queries:
            queries.append(q)
    # de-dupe preserve order
    seen: set[str] = set()
    out: list[str] = []
    for q in queries:
        key = q.lower()
        if key in seen:
            continue
        seen.add(key)
        out.append(q)
    return out[:6]


def fetch_url_text(url: str, max_chars: int = 12000, timeout: float = 20.0) -> dict[str, Any]:
    """Fetch a URL and extract readable text (HTML stripped)."""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
    }
    try:
        with httpx.Client(timeout=timeout, follow_redirects=True, headers=headers) as client:
            r = client.get(url)
            r.raise_for_status()
            ctype = (r.headers.get("content-type") or "").lower()
            if "pdf" in ctype:
                return {"url": url, "ok": False, "error": "PDF not supported", "text": "", "title": ""}
            html = r.text
    except Exception as exc:  # noqa: BLE001
        logger.info("fetch failed %s: %s", url, exc)
        return {"url": url, "ok": False, "error": str(exc), "text": "", "title": ""}

    title = ""
    text = html
    try:
        from bs4 import BeautifulSoup

        soup = BeautifulSoup(html, "html.parser")
        for tag in soup(["script", "style", "noscript", "nav", "footer", "header", "aside"]):
            tag.decompose()
        if soup.title and soup.title.string:
            title = soup.title.string.strip()
        text = soup.get_text("\n", strip=True)
    except Exception:  # noqa: BLE001
        text = re.sub(r"<script[\s\S]*?</script>", " ", html, flags=re.I)
        text = re.sub(r"<style[\s\S]*?</style>", " ", text, flags=re.I)
        text = re.sub(r"<[^>]+>", " ", text)
        text = re.sub(r"\s+", " ", text).strip()
        m = re.search(r"<title[^>]*>(.*?)</title>", html, flags=re.I | re.S)
        if m:
            title = re.sub(r"\s+", " ", m.group(1)).strip()

    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    if len(text) > max_chars:
        text = text[:max_chars] + "\n…"
    return {"url": url, "ok": bool(text), "error": None, "text": text, "title": title}


def search_and_read(
    queries: list[str],
    *,
    max_results_per_query: int = 5,
    max_pages_to_fetch: int = 4,
) -> dict[str, Any]:
    """Run text+news search across queries, then fetch a few top pages."""
    import time

    hits: list[dict[str, Any]] = []
    errors: list[str] = []
    for i, q in enumerate(queries):
        if i:
            time.sleep(1.0)  # gentle pacing vs DDG rate limits
        try:
            hits.extend(search_duckduckgo(q, max_results=max_results_per_query, kind="text"))
        except Exception as exc:  # noqa: BLE001
            errors.append(f"text:{q}: {exc}")
            logger.warning("text search failed for %s: %s", q, exc)
        try:
            time.sleep(0.6)
            hits.extend(search_duckduckgo(q, max_results=max_results_per_query, kind="news"))
        except Exception as exc:  # noqa: BLE001
            errors.append(f"news:{q}: {exc}")
            logger.warning("news search failed for %s: %s", q, exc)

    # Dedupe by URL
    by_url: dict[str, dict[str, Any]] = {}
    for h in hits:
        url = h.get("url") or ""
        if not url:
            continue
        if url not in by_url:
            by_url[url] = h
    unique = list(by_url.values())

    pages: list[dict[str, Any]] = []
    for h in unique[:max_pages_to_fetch]:
        page = fetch_url_text(h["url"])
        page["search_title"] = h.get("title")
        page["snippet"] = h.get("snippet")
        pages.append(page)

    return {
        "queries": queries,
        "hits": unique[:20],
        "pages": pages,
        "errors": errors,
        "hit_count": len(unique),
        "fetched_ok": sum(1 for p in pages if p.get("ok")),
    }


WEB_SUMMARY_PROMPT = """You are an equity research assistant. Using ONLY the web snippets and page extracts below, summarize:
1) Analyst views / price targets / ratings (if present)
2) Recent company news and catalysts
3) Sector or commodity drivers mentioned (e.g. uranium, rare earths, pricing)

Do not invent numbers. If targets are missing, say so. Use short Markdown bullets and cite source titles.

Material:
{chunk}
"""


def corpus_from_web(web: dict[str, Any], max_chars: int = 14000) -> str:
    parts: list[str] = []
    for h in web.get("hits") or []:
        parts.append(
            f"[HIT] {h.get('title')} | {h.get('source')} | {h.get('url')}\n{h.get('snippet')}"
        )
    for p in web.get("pages") or []:
        if not p.get("ok"):
            continue
        parts.append(
            f"[PAGE] {p.get('title') or p.get('search_title')} | {p.get('url')}\n{(p.get('text') or '')[:3500]}"
        )
    blob = "\n\n".join(parts)
    return blob[:max_chars]


def format_web_markdown(web: dict[str, Any], summary_md: str = "") -> str:
    lines = [
        "## Web / news research",
        "",
        f"- Queries: {', '.join(web.get('queries') or []) or '—'}",
        f"- Unique hits: {web.get('hit_count', 0)}",
        f"- Pages fetched: {web.get('fetched_ok', 0)}/{len(web.get('pages') or [])}",
        "",
    ]
    if summary_md:
        lines += [summary_md.strip(), ""]
    hits = web.get("hits") or []
    if hits:
        lines.append("### Sources found")
        for h in hits[:12]:
            title = h.get("title") or h.get("url")
            url = h.get("url") or ""
            snippet = (h.get("snippet") or "").replace("\n", " ")
            if len(snippet) > 160:
                snippet = snippet[:157] + "…"
            lines.append(f"- [{title}]({url})")
            if snippet:
                lines.append(f"  - {snippet}")
        lines.append("")
    errs = web.get("errors") or []
    if errs:
        lines.append("### Search warnings")
        for e in errs[:8]:
            lines.append(f"- {e}")
        lines.append("")
    return "\n".join(lines) + "\n"
