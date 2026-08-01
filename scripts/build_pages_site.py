#!/usr/bin/env python3
"""Build a styled static GitHub Pages site from data/sync research packs.

Usage:
  python scripts/build_pages_site.py
  python scripts/build_pages_site.py --out docs

Output goes to docs/ (index + report pages + charts + CSS).
Enable GitHub Pages: Settings → Pages → Deploy from branch → main → /docs
"""

from __future__ import annotations

import argparse
import html
import json
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path

try:
    import markdown as md_lib
except ImportError as exc:  # pragma: no cover
    raise SystemExit(
        "Missing dependency: markdown\n  pip install markdown\n"
    ) from exc

ROOT = Path(__file__).resolve().parents[1]
SYNC_DIR = ROOT / "data" / "sync"
JOBS_DIR = SYNC_DIR / "jobs"
CHARTS_SRC = SYNC_DIR / "charts"

MD_EXTENSIONS = [
    "tables",
    "fenced_code",
    "sane_lists",
    "nl2br",
    "toc",
]


def _short_date(iso: str | None) -> str:
    if not iso:
        return "—"
    try:
        return iso[:16].replace("T", " ") + " UTC"
    except Exception:
        return iso


def _load_jobs() -> list[dict]:
    items: list[dict] = []
    if not JOBS_DIR.exists():
        return items
    for path in sorted(JOBS_DIR.glob("*.json")):
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        job = payload.get("job") if isinstance(payload.get("job"), dict) else payload
        if not isinstance(job, dict):
            continue
        result = job.get("result") if isinstance(job.get("result"), dict) else {}
        md = (result or {}).get("report_markdown") or ""
        if not md.strip():
            # Fall back to synced .md report file if present
            report_file = payload.get("report_file")
            if report_file:
                rp = SYNC_DIR / "reports" / report_file
                if rp.exists():
                    md = rp.read_text(encoding="utf-8")
        if not md.strip():
            continue
        if (job.get("status") or "").lower() not in {"completed", "failed"}:
            continue
        ticker = (job.get("ticker") or "UNK").upper()
        job_id = job.get("id") or path.stem
        items.append(
            {
                "id": job_id,
                "ticker": ticker,
                "mode": job.get("mode") or "",
                "template": job.get("template") or "",
                "goal": job.get("goal") or (job.get("plan") or {}).get("goal") or "",
                "status": job.get("status") or "",
                "created_at": job.get("created_at") or "",
                "finished_at": job.get("finished_at") or "",
                "exported_at": payload.get("exported_at") or "",
                "charts": payload.get("charts") or [],
                "markdown": md,
                "slug": f"{ticker}-{job_id[:8]}".lower(),
            }
        )
    # Newest finished first; prefer richer packs when timestamps tie
    items.sort(
        key=lambda x: (x.get("finished_at") or x.get("created_at") or "", len(x["markdown"])),
        reverse=True,
    )
    return items


def _rewrite_chart_urls(markdown_text: str) -> str:
    """Point /charts/foo.png at the Pages charts folder (relative from reports/)."""
    text = re.sub(r"\(/charts/", "(../charts/", markdown_text)
    text = re.sub(r'(src=["\'])/charts/', r"\1../charts/", text)
    return text


def _md_to_html(markdown_text: str) -> str:
    rewritten = _rewrite_chart_urls(markdown_text)
    body = md_lib.markdown(rewritten, extensions=MD_EXTENSIONS)
    # Wrap tables for horizontal scroll on phones
    body = re.sub(
        r"(<table>.*?</table>)",
        r'<div class="table-scroll">\1</div>',
        body,
        flags=re.DOTALL | re.IGNORECASE,
    )
    return body


def _page_shell(
    *,
    title: str,
    body: str,
    css_href: str,
    active: str = "reports",
) -> str:
    nav_reports = ' class="active"' if active == "reports" else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
  <meta name="color-scheme" content="dark" />
  <title>{html.escape(title)}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,600;0,9..40,700;1,9..40,400&family=Fraunces:opsz,wght@9..144,600;9..144,700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="{css_href}" />
</head>
<body>
  <header class="topnav">
    <a class="topnav-brand" href="INDEX_HREF">Equity Research</a>
    <nav class="topnav-links" aria-label="Site">
      <a href="INDEX_HREF"{nav_reports}>Reports</a>
    </nav>
  </header>
  {body}
  <footer class="site-foot">
    <p>Static viewer of synced research packs · Not investment advice</p>
  </footer>
</body>
</html>
"""


def _index_html(jobs: list[dict], built_at: str) -> str:
    cards = []
    for j in jobs:
        goal = html.escape((j["goal"] or "")[:160])
        cards.append(
            f"""
      <a class="report-card" href="reports/{html.escape(j['slug'])}.html">
        <div class="report-card-top">
          <span class="ticker">{html.escape(j['ticker'])}</span>
          <span class="pill">{html.escape(j['status'])}</span>
        </div>
        <p class="meta">{html.escape(j['mode'] or '—')} · {html.escape(j['template'] or 'job')}</p>
        <p class="when">{html.escape(_short_date(j['finished_at'] or j['created_at']))}</p>
        {"<p class='goal'>" + goal + "</p>" if goal else ""}
      </a>"""
        )

    tickers = sorted({j["ticker"] for j in jobs})
    ticker_opts = "".join(f'<option value="{html.escape(t)}">{html.escape(t)}</option>' for t in tickers)

    body = f"""
  <main class="wrap wide">
    <header class="hero">
      <p class="eyebrow">GitHub Pages</p>
      <h1 class="brand">Research reports</h1>
      <p class="sub">Lightweight read-only viewer of completed packs from <code>data/sync/</code>. Built {html.escape(built_at)}.</p>
    </header>

    <div class="toolbar">
      <label class="sr-only" for="q">Filter</label>
      <input id="q" type="search" placeholder="Filter by ticker, mode, goal…" autocomplete="off" />
      <label class="sr-only" for="ticker">Ticker</label>
      <select id="ticker">
        <option value="">All tickers</option>
        {ticker_opts}
      </select>
      <p class="count" id="count">{len(jobs)} report{"s" if len(jobs) != 1 else ""}</p>
    </div>

    <section class="card-grid" id="grid" aria-label="Reports">
      {"".join(cards) if cards else "<p class='empty'>No completed sync reports yet. Run research locally, sync, then rebuild.</p>"}
    </section>
  </main>
  <script>
    (function () {{
      const q = document.getElementById("q");
      const ticker = document.getElementById("ticker");
      const grid = document.getElementById("grid");
      const count = document.getElementById("count");
      const cards = [...grid.querySelectorAll(".report-card")];
      function apply() {{
        const needle = (q.value || "").trim().toLowerCase();
        const t = ticker.value;
        let n = 0;
        for (const c of cards) {{
          const text = c.textContent.toLowerCase();
          const okT = !t || c.querySelector(".ticker")?.textContent === t;
          const okQ = !needle || text.includes(needle);
          const show = okT && okQ;
          c.hidden = !show;
          if (show) n += 1;
        }}
        count.textContent = n + " report" + (n === 1 ? "" : "s");
      }}
      q.addEventListener("input", apply);
      ticker.addEventListener("change", apply);
    }})();
  </script>
"""
    shell = _page_shell(title="Equity Research Reports", body=body, css_href="assets/site.css", active="reports")
    return shell.replace("INDEX_HREF", "./index.html")


def _report_html(job: dict) -> str:
    body_md = _md_to_html(job["markdown"])
    charts = job.get("charts") or []
    gallery = ""
    if charts:
        figs = []
        for name in charts:
            figs.append(
                f"""
        <figure class="chart-card">
          <figcaption>{html.escape(Path(name).stem.replace("_", " "))}</figcaption>
          <img src="../charts/{html.escape(name)}" alt="{html.escape(name)}" loading="lazy" />
        </figure>"""
            )
        gallery = f'<section class="chart-gallery" aria-label="Charts">{"".join(figs)}</section>'

    goal = html.escape(job["goal"]) if job.get("goal") else ""
    body = f"""
  <main class="wrap wide">
    <header class="row">
      <div>
        <p class="brand">{html.escape(job["ticker"])} report</p>
        <p class="sub">{html.escape(job["mode"] or "—")} · {html.escape(job["template"] or "job")} · {_short_date(job["finished_at"] or job["created_at"])}</p>
        {"<p class='fine'>Goal: " + goal + "</p>" if goal else ""}
      </div>
      <div class="actions">
        <a class="btn secondary" href="../index.html">All reports</a>
      </div>
    </header>
    {gallery}
    <article class="report">
      {body_md}
    </article>
  </main>
"""
    shell = _page_shell(
        title=f"{job['ticker']} report",
        body=body,
        css_href="../assets/site.css",
        active="reports",
    )
    return shell.replace("INDEX_HREF", "../index.html")


def _copy_charts(jobs: list[dict], out_charts: Path) -> int:
    out_charts.mkdir(parents=True, exist_ok=True)
    names: set[str] = set()
    for j in jobs:
        for name in j.get("charts") or []:
            names.add(name)
        for m in re.finditer(r"/charts/([A-Za-z0-9._\-]+)", j["markdown"]):
            names.add(m.group(1))
    n = 0
    for name in sorted(names):
        src = CHARTS_SRC / name
        if not src.exists():
            continue
        shutil.copy2(src, out_charts / name)
        n += 1
    return n


def build(out_dir: Path) -> dict:
    jobs = _load_jobs()
    if out_dir.exists():
        # Keep only generated site files; wipe previous build artifacts we own
        for child in list(out_dir.iterdir()):
            if child.name in {".git"}:
                continue
            if child.is_dir():
                shutil.rmtree(child)
            else:
                child.unlink()
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "reports").mkdir(parents=True, exist_ok=True)
    assets = Path(__file__).resolve().parent / "pages_assets"
    css_src = assets / "site.css"
    css_dest = out_dir / "assets"
    css_dest.mkdir(parents=True, exist_ok=True)
    shutil.copy2(css_src, css_dest / "site.css")
    (out_dir / ".nojekyll").write_text("", encoding="utf-8")

    built_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    (out_dir / "index.html").write_text(_index_html(jobs, built_at), encoding="utf-8")
    for j in jobs:
        (out_dir / "reports" / f"{j['slug']}.html").write_text(_report_html(j), encoding="utf-8")
    charts_n = _copy_charts(jobs, out_dir / "charts")

    manifest = {
        "built_at": built_at,
        "reports": len(jobs),
        "charts": charts_n,
        "tickers": sorted({j["ticker"] for j in jobs}),
    }
    (out_dir / "build.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description="Build GitHub Pages report site from data/sync")
    parser.add_argument("--out", type=Path, default=ROOT / "docs", help="Output directory (default: docs/)")
    args = parser.parse_args()
    manifest = build(args.out.resolve())
    print(
        f"Built {manifest['reports']} reports, {manifest['charts']} charts → {args.out}"
        f"\nTickers: {', '.join(manifest['tickers']) or '(none)'}"
    )


if __name__ == "__main__":
    main()
