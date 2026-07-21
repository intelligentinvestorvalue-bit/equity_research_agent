"""Generate research charts (matplotlib) for reports."""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Any

from src.config import OUTPUT_DIR

logger = logging.getLogger(__name__)

CHARTS_DIR = OUTPUT_DIR / "charts"


def _setup_mpl():
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    plt.rcParams.update(
        {
            "figure.facecolor": "#0f1714",
            "axes.facecolor": "#1a2621",
            "axes.edgecolor": "#3a4f45",
            "axes.labelcolor": "#e8f0eb",
            "xtick.color": "#9bb0a4",
            "ytick.color": "#9bb0a4",
            "text.color": "#e8f0eb",
            "axes.titlecolor": "#e8f0eb",
            "grid.color": "#2a3a32",
            "font.size": 10,
        }
    )
    return plt


def _fmt_year(period: str) -> str:
    return (period or "")[:4] or period


def _chart_path(out_dir: Path, ticker: str, key: str, name_tag: str = "") -> Path:
    tag = f"_{name_tag}" if name_tag else ""
    return out_dir / f"{ticker.upper()}{tag}_{key}.png"


def chart_revenue_fcf(
    ticker: str, fund: dict[str, Any], out_dir: Path | None = None, name_tag: str = ""
) -> Path | None:
    """Bar chart of revenue and FCF history."""
    history = (fund or {}).get("history") or {}
    rev = list(reversed(history.get("revenue") or []))
    fcf = list(reversed(history.get("free_cash_flow") or []))
    if not rev and not fcf:
        return None

    plt = _setup_mpl()
    out_dir = out_dir or CHARTS_DIR
    out_dir.mkdir(parents=True, exist_ok=True)
    path = _chart_path(out_dir, ticker, "revenue_fcf", name_tag)

    # Align on periods
    periods = []
    rev_map = {r["period"]: r["value"] for r in rev}
    fcf_map = {r["period"]: r["value"] for r in fcf}
    periods = sorted(set(rev_map) | set(fcf_map))
    if not periods:
        return None

    labels = [_fmt_year(p) for p in periods]
    rev_vals = [(rev_map.get(p) or 0) / 1e6 for p in periods]
    fcf_vals = [(fcf_map.get(p) or 0) / 1e6 for p in periods]

    fig, ax = plt.subplots(figsize=(8.2, 4.2))
    x = range(len(labels))
    width = 0.38
    ax.bar([i - width / 2 for i in x], rev_vals, width=width, label="Revenue", color="#3d9b6e")
    ax.bar([i + width / 2 for i in x], fcf_vals, width=width, label="FCF", color="#c9853a")
    ax.axhline(0, color="#5a6e64", linewidth=0.8)
    ax.set_xticks(list(x))
    ax.set_xticklabels(labels)
    ax.set_ylabel("USD millions")
    ax.set_title(f"{ticker.upper()} — Revenue & free cash flow")
    ax.legend(frameon=False, labelcolor="#e8f0eb")
    ax.grid(True, axis="y", alpha=0.35)
    fig.tight_layout()
    fig.savefig(path, dpi=140, bbox_inches="tight")
    plt.close(fig)
    return path


def chart_dcf_scenarios(
    ticker: str, valuation: dict[str, Any], out_dir: Path | None = None, name_tag: str = ""
) -> Path | None:
    """Bar chart of bear/base/bull share prices vs spot."""
    if not valuation or not valuation.get("ok"):
        return None
    scenarios = valuation.get("scenarios") or {}
    order = ("bear", "base", "bull")
    labels = []
    prices = []
    for key in order:
        sc = scenarios.get(key) or {}
        sp = sc.get("share_price")
        if sp is None:
            continue
        labels.append(key)
        prices.append(float(sp))
    if not labels:
        return None

    plt = _setup_mpl()
    out_dir = out_dir or CHARTS_DIR
    out_dir.mkdir(parents=True, exist_ok=True)
    path = _chart_path(out_dir, ticker, "dcf_scenarios", name_tag)

    spot = valuation.get("spot_price")
    colors = {"bear": "#c45c5c", "base": "#3d9b6e", "bull": "#5b8def"}

    fig, ax = plt.subplots(figsize=(7.2, 4.0))
    bars = ax.bar(labels, prices, color=[colors.get(l, "#3d9b6e") for l in labels])
    if spot is not None:
        ax.axhline(float(spot), color="#e8f0eb", linestyle="--", linewidth=1.2, label=f"Spot ${float(spot):.2f}")
        ax.legend(frameon=False, labelcolor="#e8f0eb")
    ax.set_ylabel("Share price (USD)")
    ax.set_title(f"{ticker.upper()} — DCF scenario prices")
    ax.grid(True, axis="y", alpha=0.35)
    for bar, val in zip(bars, prices):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            f"${val:.2f}",
            ha="center",
            va="bottom" if val >= 0 else "top",
            fontsize=9,
            color="#e8f0eb",
        )
    fig.tight_layout()
    fig.savefig(path, dpi=140, bbox_inches="tight")
    plt.close(fig)
    return path


def chart_base_fcf_path(
    ticker: str, valuation: dict[str, Any], out_dir: Path | None = None, name_tag: str = ""
) -> Path | None:
    """Line/bar of base-case projected FCF path."""
    if not valuation or not valuation.get("ok"):
        return None
    base = (valuation.get("scenarios") or {}).get("base") or {}
    cfs = base.get("cashflows") or []
    if not cfs:
        return None

    plt = _setup_mpl()
    out_dir = out_dir or CHARTS_DIR
    out_dir.mkdir(parents=True, exist_ok=True)
    path = _chart_path(out_dir, ticker, "base_fcf_path", name_tag)

    years = [c["year"] for c in cfs]
    fcf = [float(c["fcf"]) / 1e6 for c in cfs]

    fig, ax = plt.subplots(figsize=(7.2, 4.0))
    ax.plot(years, fcf, marker="o", color="#3d9b6e", linewidth=2)
    ax.fill_between(years, fcf, alpha=0.2, color="#3d9b6e")
    ax.set_xlabel("Year")
    ax.set_ylabel("Projected FCF (USD millions)")
    ax.set_title(f"{ticker.upper()} — Base-case projected FCF")
    ax.grid(True, alpha=0.35)
    fig.tight_layout()
    fig.savefig(path, dpi=140, bbox_inches="tight")
    plt.close(fig)
    return path


def chart_ev_ebitda_scenarios(
    ticker: str, multiples: dict[str, Any], out_dir: Path | None = None, name_tag: str = ""
) -> Path | None:
    if not multiples or not multiples.get("ok"):
        return None
    scenarios = multiples.get("scenarios") or {}
    labels, prices = [], []
    for key in ("bear", "base", "bull"):
        sc = scenarios.get(key) or {}
        sp = sc.get("share_price")
        if sp is None:
            continue
        labels.append(key)
        prices.append(float(sp))
    if not labels:
        return None

    plt = _setup_mpl()
    out_dir = out_dir or CHARTS_DIR
    out_dir.mkdir(parents=True, exist_ok=True)
    path = _chart_path(out_dir, ticker, "ev_ebitda_scenarios", name_tag)
    spot = multiples.get("spot_price")
    colors = {"bear": "#c45c5c", "base": "#3d9b6e", "bull": "#5b8def"}

    fig, ax = plt.subplots(figsize=(7.2, 4.0))
    bars = ax.bar(labels, prices, color=[colors.get(l, "#3d9b6e") for l in labels])
    if spot is not None:
        ax.axhline(float(spot), color="#e8f0eb", linestyle="--", linewidth=1.2, label=f"Spot ${float(spot):.2f}")
        ax.legend(frameon=False, labelcolor="#e8f0eb")
    ax.set_ylabel("Implied share price (USD)")
    ax.set_title(f"{ticker.upper()} — EV/EBITDA scenario prices")
    ax.grid(True, axis="y", alpha=0.35)
    for bar, val in zip(bars, prices):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            f"${val:.2f}",
            ha="center",
            va="bottom" if val >= 0 else "top",
            fontsize=9,
            color="#e8f0eb",
        )
    fig.tight_layout()
    fig.savefig(path, dpi=140, bbox_inches="tight")
    plt.close(fig)
    return path


def chart_scenario_ranges(
    ticker: str, scenarios: dict[str, Any], out_dir: Path | None = None, name_tag: str = ""
) -> Path | None:
    """Error-bar chart of medium-term bear/base/bull price ranges."""
    if not scenarios or not scenarios.get("ok"):
        return None
    scens = scenarios.get("scenarios") or {}
    labels, mids, lows, highs = [], [], [], []
    for key in ("bear", "base", "bull"):
        sc = scens.get(key) or {}
        if not sc.get("ok"):
            continue
        labels.append(key)
        mids.append(float(sc["price_mid"]))
        lows.append(float(sc["price_low"]))
        highs.append(float(sc["price_high"]))
    if not labels:
        return None

    plt = _setup_mpl()
    out_dir = out_dir or CHARTS_DIR
    out_dir.mkdir(parents=True, exist_ok=True)
    path = _chart_path(out_dir, ticker, "scenario_ranges", name_tag)
    spot = scenarios.get("spot_price")
    colors = {"bear": "#c45c5c", "base": "#3d9b6e", "bull": "#5b8def"}
    yerr = [[m - lo for m, lo in zip(mids, lows)], [hi - m for m, hi in zip(mids, highs)]]

    fig, ax = plt.subplots(figsize=(7.4, 4.2))
    bars = ax.bar(
        labels,
        mids,
        yerr=yerr,
        color=[colors.get(l, "#3d9b6e") for l in labels],
        capsize=5,
        error_kw={"ecolor": "#9bb0a4", "linewidth": 1.2},
    )
    if spot is not None:
        ax.axhline(float(spot), color="#e8f0eb", linestyle="--", linewidth=1.2, label=f"Spot ${float(spot):.2f}")
        ax.legend(frameon=False, labelcolor="#e8f0eb")
    ax.set_ylabel("Share price range (USD)")
    ax.set_title(f"{ticker.upper()} — Headwind/tailwind scenario ranges")
    ax.grid(True, axis="y", alpha=0.35)
    for bar, mid, lo, hi in zip(bars, mids, lows, highs):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            mid,
            f"${mid:.2f}\n[{lo:.0f}–{hi:.0f}]",
            ha="center",
            va="bottom",
            fontsize=8,
            color="#e8f0eb",
        )
    fig.tight_layout()
    fig.savefig(path, dpi=140, bbox_inches="tight")
    plt.close(fig)
    return path


def chart_peer_normalized(
    ticker: str, peers: dict[str, Any], out_dir: Path | None = None, name_tag: str = ""
) -> Path | None:
    """Normalized 5y price index for subject + peers."""
    histories = (peers or {}).get("_histories") or (peers or {}).get("histories") or {}
    if not histories:
        return None
    plt = _setup_mpl()
    out_dir = out_dir or CHARTS_DIR
    out_dir.mkdir(parents=True, exist_ok=True)
    path = _chart_path(out_dir, ticker, "peers_normalized", name_tag)

    fig, ax = plt.subplots(figsize=(8.4, 4.4))
    plotted = 0
    for sym, hist in histories.items():
        try:
            if hist is None or hist.empty or "Close" not in hist.columns:
                continue
            closes = hist["Close"].dropna()
            if len(closes) < 20:
                continue
            indexed = closes / float(closes.iloc[0]) * 100.0
            lw = 2.4 if sym.upper() == ticker.upper() else 1.2
            ax.plot(indexed.index, indexed.values, label=sym.upper(), linewidth=lw)
            plotted += 1
        except Exception as exc:  # noqa: BLE001
            logger.debug("peer chart skip %s: %s", sym, exc)
    if plotted < 1:
        plt.close(fig)
        return None
    ax.axhline(100, color="#5a6e64", linewidth=0.8, linestyle=":")
    ax.set_ylabel("Indexed price (start=100)")
    ax.set_title(f"{ticker.upper()} — Normalized price vs peers")
    ax.legend(frameon=False, labelcolor="#e8f0eb", fontsize=8, ncol=2)
    ax.grid(True, alpha=0.35)
    fig.tight_layout()
    fig.savefig(path, dpi=140, bbox_inches="tight")
    plt.close(fig)
    return path


def generate_research_charts(
    ticker: str,
    fund: dict[str, Any] | None,
    valuation: dict[str, Any] | None,
    out_dir: Path | None = None,
    *,
    multiples: dict[str, Any] | None = None,
    peers: dict[str, Any] | None = None,
    scenario_ranges: dict[str, Any] | None = None,
    name_tag: str = "",
) -> dict[str, Any]:
    """
    Build available charts; returns metadata with paths and public URLs.
    name_tag namespaces filenames (e.g. template id) so pack runs don't overwrite.
    """
    out_dir = out_dir or CHARTS_DIR
    out_dir.mkdir(parents=True, exist_ok=True)
    ticker = ticker.upper()
    tag = name_tag or ""
    charts: list[dict[str, str]] = []

    builders = [
        ("revenue_fcf", "Revenue & FCF history", lambda: chart_revenue_fcf(ticker, fund or {}, out_dir, tag)),
        ("dcf_scenarios", "DCF scenario prices", lambda: chart_dcf_scenarios(ticker, valuation or {}, out_dir, tag)),
        ("base_fcf_path", "Base-case FCF path", lambda: chart_base_fcf_path(ticker, valuation or {}, out_dir, tag)),
        (
            "ev_ebitda_scenarios",
            "EV/EBITDA scenario prices",
            lambda: chart_ev_ebitda_scenarios(ticker, multiples or {}, out_dir, tag),
        ),
        (
            "scenario_ranges",
            "Headwind/tailwind price ranges",
            lambda: chart_scenario_ranges(ticker, scenario_ranges or {}, out_dir, tag),
        ),
        (
            "peers_normalized",
            "Normalized price vs peers",
            lambda: chart_peer_normalized(ticker, peers or {}, out_dir, tag),
        ),
    ]
    for key, title, fn in builders:
        try:
            path = fn()
        except Exception as exc:  # noqa: BLE001
            logger.warning("Chart %s failed: %s", key, exc)
            continue
        if not path:
            continue
        rel = path.name
        charts.append(
            {
                "id": key,
                "title": title,
                "path": str(path),
                "filename": rel,
                "url": f"/charts/{rel}",
            }
        )

    return {"ticker": ticker, "charts": charts, "name_tag": tag}


def charts_markdown(charts_meta: dict[str, Any]) -> str:
    charts = (charts_meta or {}).get("charts") or []
    if not charts:
        return ""
    lines = ["## Charts", ""]
    for c in charts:
        lines.append(f"### {c['title']}")
        lines.append(f"![{c['title']}]({c['url']})")
        lines.append("")
    return "\n".join(lines) + "\n"
