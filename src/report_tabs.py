"""Split research report markdown into named tabs for the UI."""

from __future__ import annotations

import re
from typing import Any


# Map heading substrings (lowercase) → stable tab id + display label
_TAB_RULES: list[tuple[str, str, str]] = [
    ("plan executed", "plan", "Plan"),
    ("executive summary", "exec", "Exec summary"),
    ("company setup", "business", "Business"),
    ("fundamentals", "fundamentals", "Fundamentals"),
    ("capital structure", "fundamentals", "Fundamentals"),
    ("historical kpis", "fundamentals", "Fundamentals"),
    ("valuation — ev/ebitda", "multiples", "EV/EBITDA"),
    ("ev/ebitda", "multiples", "EV/EBITDA"),
    ("dcf valuation", "valuation", "DCF"),
    ("peer & factor", "peers", "Peers"),
    ("peer comps", "peers", "Peers"),
    ("earnings, guidance", "earnings", "Earnings"),
    ("earnings", "earnings", "Earnings"),
    ("key driver", "drivers", "Drivers"),
    ("driver analysis", "drivers", "Drivers"),
    ("variant perception", "thesis", "Thesis"),
    ("catalysts & monitoring", "catalysts", "Catalysts"),
    ("catalyst calendar", "catalysts", "Catalysts"),
    ("early proxy", "proxies", "Proxies"),
    ("falsification", "falsifiers", "Falsifiers"),
    ("source quality", "limitations", "Limitations"),
    ("web research", "web", "Web & news"),
    ("web / news", "web", "Web & news"),
    ("put opportunities", "options", "Options"),
    ("sec filing", "sec", "SEC"),
    ("recent sec filings", "sec", "SEC"),
    ("qualitative analysis", "qualitative", "Qualitative"),
    ("charts", "charts-md", "Chart notes"),
    ("research loop", "loop", "Research loop"),
    ("self-critique", "critique", "Critique"),
    ("sources", "sources", "Sources"),
    ("run warnings", "warnings", "Warnings"),
]


def _match_tab(heading: str) -> tuple[str, str]:
    h = heading.strip().lower()
    for needle, tab_id, label in _TAB_RULES:
        if needle in h:
            return tab_id, label
    # Fallback: slug from heading
    slug = re.sub(r"[^a-z0-9]+", "-", h).strip("-")[:40] or "section"
    label = heading.strip()[:48] or "Section"
    return slug, label


def split_report_sections(markdown: str) -> list[dict[str, str]]:
    """Split on top-level ## headings into ordered sections."""
    text = (markdown or "").strip()
    if not text:
        return []

    parts = re.split(r"(?m)^(## .+)$", text)
    sections: list[dict[str, str]] = []

    # Preamble before first ##
    preamble = (parts[0] or "").strip()
    if preamble:
        sections.append(
            {
                "id": "overview",
                "label": "Overview",
                "heading": "Overview",
                "markdown": preamble,
            }
        )

    i = 1
    while i + 1 < len(parts):
        heading_line = parts[i].strip()
        body = (parts[i + 1] or "").strip()
        heading = re.sub(r"^##\s+", "", heading_line).strip()
        # Drop citation markers like [1] from tab labels
        heading_clean = re.sub(r"\s*\[[^\]]+\]\s*$", "", heading).strip()
        tab_id, label = _match_tab(heading_clean)
        md = f"## {heading_clean}\n\n{body}".strip() if body else f"## {heading_clean}"
        # Merge duplicate tab ids (e.g. multiple web sections)
        existing = next((s for s in sections if s["id"] == tab_id), None)
        if existing:
            existing["markdown"] = (existing["markdown"] + "\n\n" + md).strip()
            if tab_id == "web" and "—" in heading_clean:
                # Keep label generic for merged web tabs
                existing["label"] = "Web & news"
        else:
            sections.append(
                {
                    "id": tab_id,
                    "label": label,
                    "heading": heading_clean,
                    "markdown": md,
                }
            )
        i += 2

    return sections


def build_report_tabs(
    markdown: str,
    charts: list[dict[str, Any]] | None = None,
) -> list[dict[str, Any]]:
    """Build UI tabs: Charts (if any) + markdown sections + Full report."""
    tabs: list[dict[str, Any]] = []
    chart_list = list(charts or [])

    if chart_list:
        tabs.append(
            {
                "id": "charts",
                "label": "Charts",
                "kind": "charts",
                "charts": chart_list,
                "markdown": "",
            }
        )

    for sec in split_report_sections(markdown):
        # Skip empty chart-notes tab if we already have a Charts gallery
        if sec["id"] == "charts-md" and chart_list:
            continue
        tabs.append(
            {
                "id": sec["id"],
                "label": sec["label"],
                "kind": "markdown",
                "charts": [],
                "markdown": sec["markdown"],
            }
        )

    if markdown and (len(tabs) > 1 or (tabs and tabs[0].get("kind") == "charts")):
        tabs.append(
            {
                "id": "full",
                "label": "Full report",
                "kind": "markdown",
                "charts": [],
                "markdown": markdown,
            }
        )

    if not tabs and markdown:
        tabs.append(
            {
                "id": "full",
                "label": "Report",
                "kind": "markdown",
                "charts": [],
                "markdown": markdown,
            }
        )

    return tabs


def job_href(job: Any) -> str:
    status = getattr(job, "status", "") or ""
    jid = getattr(job, "id", "")
    if status == "completed":
        return f"/jobs/{jid}/report"
    if status in {"planning", "awaiting_approval"}:
        return f"/jobs/{jid}/plan"
    return f"/jobs/{jid}"
