"""Medium-term bull/base/bear price ranges from headwinds & tailwinds.

Inspired by how Gemini / Perplexity-style research memos frame scenarios:
1) Collect qualitative drivers (risks = headwinds, catalysts = tailwinds)
2) Map each case to growth / EBITDA / multiple assumptions
3) Translate into a share-price *range* (not a single DCF path)

This is deliberately separate from the FCF DCF engine — it is a
driver → multiple bridge over an ~18–36 month horizon.
"""

from __future__ import annotations

import re
from typing import Any

HORIZON_LABEL = "18–36 months (medium / medium-long term)"

HEADWIND_PATTERNS: list[tuple[str, str]] = [
    (r"debt|leverage|refinanc|covenant|maturity|interest.?rate|downgrade", "Balance-sheet / refinancing pressure"),
    (r"regulation|litigation|lawsuit|antitrust|compliance|fine|penalty", "Regulatory / legal risk"),
    (r"competition|market.?share|pricing.?pressure|commodit", "Competitive / pricing pressure"),
    (r"customer.?concentrat|contract.?loss|churn|cancellation|backlog.?declin", "Demand / customer risk"),
    (r"margin.?compress|cost.?inflation|opex|labor.?cost|supply.?chain", "Margin / cost headwind"),
    (r"cyber|security.?breach|outage|operational.?disrupt", "Operational / cyber risk"),
    (r"recession|macro|demand.?slow|volume.?declin|weak.?guid", "Macro / demand slowdown"),
    (r"dilution|equity.?raise|going.?concern|liquidity.?crunch", "Dilution / liquidity stress"),
]

TAILWIND_PATTERNS: list[tuple[str, str]] = [
    (r"growth|expansion|ramp|accelerate|beat|outperform", "Growth / execution upside"),
    (r"margin.?expand|operating.?leverage|cost.?cut|efficien|synerg", "Margin expansion / cost takeout"),
    (r"delever|debt.?reduc|refinanc.*success|balance.?sheet.?repair|net.?debt.?declin", "Deleveraging / BS repair"),
    (r"contract|backlog|win|award|partnership|hyperscaler|customer.?win", "Contract / backlog wins"),
    (r"new.?product|innovation|AI|platform|pricing.?power", "Product / pricing power"),
    (r"buyback|dividend|capital.?return|FCF.?inflect", "Capital returns / FCF inflection"),
    (r"multiple.?re.?rate|re.?rating|upgrade|target.?rais", "Multiple re-rating / Street upgrades"),
    (r"commodity.?tailwind|price.?strength|volume.?recover", "Commodity / volume recovery"),
]


def _f(val: Any) -> float | None:
    if val is None:
        return None
    try:
        return float(val)
    except (TypeError, ValueError):
        return None


def _clamp(x: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, x))


def _money(v: Any) -> str:
    if v is None:
        return "—"
    try:
        v = float(v)
    except (TypeError, ValueError):
        return "—"
    sign = "-" if v < 0 else ""
    a = abs(v)
    if a >= 1e9:
        return f"{sign}${a / 1e9:.2f}B"
    if a >= 1e6:
        return f"{sign}${a / 1e6:.2f}M"
    return f"{sign}${a:,.0f}"


def _collect_text_blobs(
    fund: dict[str, Any] | None,
    web: dict[str, Any] | None,
    nlp_1a: dict[str, Any] | None,
    nlp_7: dict[str, Any] | None,
    nlp_business: dict[str, Any] | None,
    earnings: dict[str, Any] | None,
    filings_extra: dict[str, Any] | None,
    goal: str = "",
) -> list[tuple[str, str]]:
    """Return (source_label, text) pairs for driver extraction."""
    blobs: list[tuple[str, str]] = []
    if goal.strip():
        blobs.append(("goal", goal.strip()))
    fund = fund or {}
    snap = fund.get("snapshot") or {}
    cap = fund.get("capital_structure") or {}
    fund_bits = [
        f"sector={snap.get('sector')} industry={snap.get('industry')}",
        f"revenue={fund.get('revenue')} ebitda={fund.get('ebitda')} fcf={fund.get('free_cash_flow')}",
        f"net_debt={cap.get('net_debt')} nd_ebitda={cap.get('net_debt_to_ebitda')}",
        f"target={snap.get('target_mean_price')} rec={snap.get('recommendation')}",
    ]
    blobs.append(("fundamentals", " ".join(fund_bits)))

    for label, nlp in (
        ("item_1a", nlp_1a),
        ("item_7", nlp_7),
        ("item_1", nlp_business),
    ):
        md = ((nlp or {}).get("markdown") or "").strip()
        if md:
            blobs.append((label, md[:5000]))

    for h in (web or {}).get("hits") or []:
        blobs.append(("web", f"{h.get('title') or ''} {h.get('snippet') or ''}"))
    for p in (web or {}).get("pages") or []:
        if p.get("ok"):
            blobs.append(("web_page", f"{p.get('title') or ''} {(p.get('text') or '')[:600]}"))

    if earnings:
        blobs.append(("earnings", f"next={earnings.get('next_earnings')}"))
        for r in (earnings.get("rows") or [])[:4]:
            blobs.append(
                (
                    "earnings",
                    f"{r.get('date')} est={r.get('eps_estimate')} act={r.get('eps_actual')} move={r.get('one_day_move')}",
                )
            )

    for f in (filings_extra or {}).get("recent") or []:
        blobs.append(
            ("filing", f"{f.get('form')} {f.get('filing_date')} {f.get('description') or ''}")
        )
    return blobs


def _match_drivers(
    blobs: list[tuple[str, str]],
    patterns: list[tuple[str, str]],
    *,
    kind: str,
    limit: int = 8,
) -> list[dict[str, str]]:
    seen: set[str] = set()
    out: list[dict[str, str]] = []
    for source, text in blobs:
        low = (text or "").lower()
        if not low.strip():
            continue
        for pat, theme in patterns:
            if theme in seen:
                continue
            if re.search(pat, low, re.I):
                snippet = re.sub(r"\s+", " ", text).strip()[:180]
                seen.add(theme)
                out.append(
                    {
                        "kind": kind,
                        "theme": theme,
                        "signal": snippet or theme,
                        "source": source,
                    }
                )
                if len(out) >= limit:
                    return out
    return out


def _fundamental_drivers(fund: dict[str, Any] | None) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    """Hard financial flags that always count as headwinds or tailwinds."""
    fund = fund or {}
    snap = fund.get("snapshot") or {}
    cap = fund.get("capital_structure") or {}
    ratios = fund.get("ratios") or {}
    growth = fund.get("growth") or {}
    head: list[dict[str, str]] = []
    tail: list[dict[str, str]] = []

    nd_eb = _f(cap.get("net_debt_to_ebitda"))
    if nd_eb is not None and nd_eb > 4.0:
        head.append(
            {
                "kind": "headwind",
                "theme": "Elevated leverage (ND/EBITDA)",
                "signal": f"Net debt / EBITDA ≈ {nd_eb:.1f}x — refinancing and equity duration risk",
                "source": "fundamentals",
            }
        )
    elif nd_eb is not None and nd_eb < 2.0:
        tail.append(
            {
                "kind": "tailwind",
                "theme": "Manageable leverage",
                "signal": f"Net debt / EBITDA ≈ {nd_eb:.1f}x — room for reinvestment or returns",
                "source": "fundamentals",
            }
        )

    fcf = _f(fund.get("free_cash_flow"))
    if fcf is not None and fcf < 0:
        head.append(
            {
                "kind": "headwind",
                "theme": "Negative free cash flow",
                "signal": f"Latest FCF {_money(fcf)} — cash burn raises financing risk",
                "source": "fundamentals",
            }
        )
    elif fcf is not None and fcf > 0:
        fy = _f(ratios.get("fcf_yield"))
        tail.append(
            {
                "kind": "tailwind",
                "theme": "Positive free cash flow",
                "signal": f"FCF {_money(fcf)}" + (f" (yield {fy:.1%})" if fy is not None else ""),
                "source": "fundamentals",
            }
        )

    yoy = _f(growth.get("latest_revenue_yoy"))
    if yoy is not None and yoy < -0.05:
        head.append(
            {
                "kind": "headwind",
                "theme": "Revenue contraction",
                "signal": f"Latest revenue YoY ≈ {yoy:.1%}",
                "source": "fundamentals",
            }
        )
    elif yoy is not None and yoy > 0.08:
        tail.append(
            {
                "kind": "tailwind",
                "theme": "Revenue growth momentum",
                "signal": f"Latest revenue YoY ≈ {yoy:.1%}",
                "source": "fundamentals",
            }
        )

    tgt = _f(snap.get("target_mean_price"))
    px = _f(fund.get("price"))
    if tgt is not None and px is not None and px > 0 and tgt / px > 1.25:
        tail.append(
            {
                "kind": "tailwind",
                "theme": "Street target implies upside",
                "signal": f"Mean target ${tgt:.2f} vs spot ${px:.2f}",
                "source": "fundamentals",
            }
        )
    elif tgt is not None and px is not None and px > 0 and tgt / px < 0.9:
        head.append(
            {
                "kind": "headwind",
                "theme": "Street target below spot",
                "signal": f"Mean target ${tgt:.2f} vs spot ${px:.2f}",
                "source": "fundamentals",
            }
        )
    return head, tail


def _peer_multiple_band(peers: dict[str, Any] | None) -> tuple[float | None, float | None, float | None]:
    vals: list[float] = []
    for r in (peers or {}).get("rows") or []:
        m = _f(r.get("ev_to_ebitda"))
        if m is not None and 1.0 < m < 60.0:
            vals.append(m)
    if not vals:
        return None, None, None
    vals.sort()
    mid = vals[len(vals) // 2]
    return vals[0], mid, vals[-1]


def _merge_unique(*groups: list[dict[str, str]], limit: int = 8) -> list[dict[str, str]]:
    seen: set[str] = set()
    out: list[dict[str, str]] = []
    for group in groups:
        for item in group:
            key = (item.get("theme") or "").lower()
            if not key or key in seen:
                continue
            seen.add(key)
            out.append(item)
            if len(out) >= limit:
                return out
    return out


def _price_from_ebitda(ebitda: float, multiple: float, net_debt: float, shares: float) -> float:
    return (ebitda * multiple - net_debt) / shares


def build_scenario_ranges(
    ticker: str,
    *,
    fund: dict[str, Any] | None = None,
    peers: dict[str, Any] | None = None,
    web: dict[str, Any] | None = None,
    nlp_1a: dict[str, Any] | None = None,
    nlp_7: dict[str, Any] | None = None,
    nlp_business: dict[str, Any] | None = None,
    earnings: dict[str, Any] | None = None,
    filings_extra: dict[str, Any] | None = None,
    multiples: dict[str, Any] | None = None,
    goal: str = "",
) -> dict[str, Any]:
    """Build medium-term bear/base/bull price ranges from headwinds & tailwinds."""
    fund = fund or {}
    ticker = ticker.upper()
    notes: list[str] = []
    errors: list[str] = []

    blobs = _collect_text_blobs(
        fund, web, nlp_1a, nlp_7, nlp_business, earnings, filings_extra, goal=goal
    )
    rule_head = _match_drivers(blobs, HEADWIND_PATTERNS, kind="headwind")
    rule_tail = _match_drivers(blobs, TAILWIND_PATTERNS, kind="tailwind")
    fund_head, fund_tail = _fundamental_drivers(fund)
    # Item 1A text is preferentially headwind-weighted
    if nlp_1a and (nlp_1a.get("markdown") or "").strip():
        notes.append("Item 1A risks weighted toward headwinds.")

    # Rule-based driver extraction from filings/web/fundamentals (fast, deterministic).
    # Optional local-LLM polish is intentionally omitted here so scenario pricing stays quick;
    # memo drafting still uses Ollama separately when available.
    driver_mode = "rules"
    llm_head: list[dict[str, str]] = []
    llm_tail: list[dict[str, str]] = []

    headwinds = _merge_unique(fund_head, rule_head, llm_head)
    tailwinds = _merge_unique(fund_tail, rule_tail, llm_tail)

    if not headwinds:
        headwinds = [
            {
                "kind": "headwind",
                "theme": "Execution / macro uncertainty",
                "signal": "Sparse explicit risk language — default bear case still stresses leverage and multiple compression",
                "source": "default",
            }
        ]
        notes.append("Few explicit headwinds extracted; used a default stress narrative.")
    if not tailwinds:
        tailwinds = [
            {
                "kind": "tailwind",
                "theme": "Base-business continuity",
                "signal": "Sparse catalyst language — bull case relies on multiple normalization and EBITDA repair",
                "source": "default",
            }
        ]
        notes.append("Few explicit tailwinds extracted; used a default upside narrative.")

    # Anchors — prefer EV/EBITDA; fall back to EV/Sales when EBITDA ≤ 0 (common in turnarounds)
    ebitda = _f(fund.get("ebitda")) or _f((fund.get("snapshot") or {}).get("ebitda"))
    if ebitda is not None and ebitda <= 0:
        ebitda = None
    revenue = _f(fund.get("revenue")) or _f((fund.get("snapshot") or {}).get("total_revenue"))
    if ebitda is None and multiples:
        seed_eb = _f(((multiples or {}).get("assumptions") or {}).get("seed_ebitda"))
        if seed_eb is not None and seed_eb > 0:
            ebitda = seed_eb

    raw = fund.get("raw_inputs") or {}
    cap = fund.get("capital_structure") or {}
    net_debt = _f(cap.get("net_debt"))
    if net_debt is None:
        net_debt = _f(raw.get("net_debt"))
    if net_debt is None:
        net_debt = (_f(raw.get("total_debt")) or 0.0) - (_f(raw.get("cash")) or 0.0)
    shares = _f(fund.get("shares_outstanding"))
    spot = _f(fund.get("price"))
    mkt = _f(fund.get("market_cap"))
    ev = _f((fund.get("snapshot") or {}).get("enterprise_value"))
    if ev is None and mkt is not None:
        ev = mkt + (net_debt or 0.0)

    method = "ev_ebitda"
    metric = ebitda
    metric_label = "EBITDA"
    cur_mult = _f((fund.get("ratios") or {}).get("ev_to_ebitda")) or _f(
        (fund.get("snapshot") or {}).get("ev_to_ebitda")
    )
    if cur_mult is not None and cur_mult <= 0:
        cur_mult = None

    if metric is None or metric <= 0:
        if revenue is not None and revenue > 0:
            method = "ev_sales"
            metric = revenue
            metric_label = "Revenue"
            if ev is not None and revenue > 0:
                cur_mult = ev / revenue
            else:
                cur_mult = 1.0
            notes.append(
                "EBITDA missing/non-positive — using EV/Sales bridge (turnaround / stressed-earnings path)."
            )
        else:
            errors.append("Missing positive EBITDA and revenue — cannot price scenarios")

    if cur_mult is None or cur_mult <= 0:
        cur_mult = _f(((multiples or {}).get("assumptions") or {}).get("seed_multiple")) or (
            8.0 if method == "ev_ebitda" else 1.0
        )
        notes.append(f"Current {method} multiple missing; anchored at {cur_mult:.1f}x.")
    else:
        hi = 45.0 if method == "ev_ebitda" else 12.0
        cur_mult = _clamp(cur_mult, 0.2, hi)

    peer_lo, peer_mid, peer_hi = _peer_multiple_band(peers)
    if peer_mid is not None and method == "ev_ebitda":
        notes.append(
            f"Peer EV/EBITDA band {peer_lo:.1f}x–{peer_hi:.1f}x (median {peer_mid:.1f}x) informs multiple ranges."
        )

    if shares in (None, 0):
        errors.append("Missing shares outstanding")

    # Driver intensity scales scenario spread (more drivers → wider / more tilted cases)
    h_n = len(headwinds)
    t_n = len(tailwinds)
    if method == "ev_ebitda":
        bear_metric_mult = _clamp(0.78 - 0.02 * max(0, h_n - 3), 0.55, 0.85)
        bull_metric_mult = _clamp(1.15 + 0.02 * max(0, t_n - 3), 1.10, 1.45)
        base_metric_mult = _clamp(1.0 + 0.02 * (t_n - h_n), 0.92, 1.08)
        bear_mult = _clamp(cur_mult * (0.70 - 0.02 * max(0, h_n - 3)), 1.5, cur_mult - 0.3)
        bull_mult = _clamp(cur_mult * (1.20 + 0.02 * max(0, t_n - 3)), cur_mult + 0.3, 50.0)
    else:
        # Sales bridge: milder volume swings, wider multiple compression for stressed names
        bear_metric_mult = _clamp(0.88 - 0.015 * max(0, h_n - 3), 0.70, 0.95)
        bull_metric_mult = _clamp(1.08 + 0.02 * max(0, t_n - 3), 1.05, 1.30)
        base_metric_mult = _clamp(1.0 + 0.01 * (t_n - h_n), 0.95, 1.05)
        bear_mult = _clamp(cur_mult * (0.55 - 0.03 * max(0, h_n - 3)), 0.15, max(0.2, cur_mult - 0.05))
        bull_mult = _clamp(cur_mult * (1.35 + 0.03 * max(0, t_n - 3)), cur_mult + 0.05, 15.0)

    base_mult = cur_mult
    if peer_lo is not None and peer_hi is not None and method == "ev_ebitda":
        bear_mult = min(bear_mult, max(peer_lo * 0.95, 1.5))
        bull_mult = max(bull_mult, peer_hi * 0.95)
        if bear_mult >= base_mult:
            bear_mult = max(1.5, base_mult * 0.85)
        if bull_mult <= base_mult:
            bull_mult = base_mult * 1.1

    street_tgt = _f((fund.get("snapshot") or {}).get("target_mean_price"))

    scenario_specs = {
        "bear": {
            "label": "bear",
            "title": "Bear — headwinds dominate",
            "probability": _clamp(0.25 + 0.03 * (h_n - t_n), 0.15, 0.40),
            "metric_mult": bear_metric_mult,
            "multiple": bear_mult,
            "band": 0.10,
            "narrative": (
                "Headwinds bite: weaker operating trajectory and multiple compression. "
                "Equity duration shrinks if cash generation fails to offset leverage / competitive pressure."
            ),
            "key_drivers": headwinds[:5],
        },
        "base": {
            "label": "base",
            "title": "Base — mixed execution",
            "probability": _clamp(0.45 - 0.02 * abs(h_n - t_n), 0.30, 0.50),
            "metric_mult": base_metric_mult,
            "multiple": base_mult,
            "band": 0.07,
            "narrative": (
                "Balanced path: some tailwinds offset headwinds. Operating scale roughly holds with modest "
                f"repair/normalization; valuation stays near the current {method.replace('_', '/').upper()} anchor."
            ),
            "key_drivers": [*tailwinds[:2], *headwinds[:2]],
        },
        "bull": {
            "label": "bull",
            "title": "Bull — tailwinds dominate",
            "probability": _clamp(0.25 + 0.03 * (t_n - h_n), 0.15, 0.40),
            "metric_mult": bull_metric_mult,
            "multiple": bull_mult,
            "band": 0.10,
            "narrative": (
                "Tailwinds compound: operating improvement plus a re-rating toward peer "
                "or recovery multiples as balance-sheet and growth narratives improve."
            ),
            "key_drivers": tailwinds[:5],
        },
    }

    # Normalize probabilities to ~1.0
    psum = sum(float(s["probability"]) for s in scenario_specs.values())
    if psum > 0:
        for s in scenario_specs.values():
            s["probability"] = round(float(s["probability"]) / psum, 2)

    scenarios: dict[str, Any] = {}
    if not errors and metric is not None and shares not in (None, 0):
        assert shares is not None
        nd = net_debt or 0.0
        for key, spec in scenario_specs.items():
            metric_s = float(metric) * float(spec["metric_mult"])
            mult = float(spec["multiple"])
            band = float(spec["band"])
            mid = _price_from_ebitda(metric_s, mult, nd, float(shares))
            low = _price_from_ebitda(metric_s, mult * (1 - band), nd, float(shares))
            high = _price_from_ebitda(metric_s, mult * (1 + band), nd, float(shares))
            if low > high:
                low, high = high, low
            upside = ((mid / spot) - 1.0) if spot and spot > 0 else None
            scenarios[key] = {
                "label": key,
                "title": spec["title"],
                "ok": True,
                "probability": spec["probability"],
                "narrative": spec["narrative"],
                "key_drivers": spec["key_drivers"],
                "metric": metric_s,
                "metric_label": metric_label,
                "metric_vs_ttm": float(spec["metric_mult"]),
                "ebitda": metric_s if method == "ev_ebitda" else None,
                "ebitda_vs_ttm": float(spec["metric_mult"]) if method == "ev_ebitda" else None,
                "multiple": mult,
                "multiple_low": mult * (1 - band),
                "multiple_high": mult * (1 + band),
                "price_low": low,
                "price_mid": mid,
                "price_high": high,
                "upside_vs_spot": upside,
                "horizon": HORIZON_LABEL,
            }
    else:
        for key, spec in scenario_specs.items():
            scenarios[key] = {
                "label": key,
                "title": spec["title"],
                "ok": False,
                "probability": spec["probability"],
                "narrative": spec["narrative"],
                "key_drivers": spec["key_drivers"],
                "error": "; ".join(errors) or "pricing failed",
            }

    # Probability-weighted midpoint (analytical, not a target)
    expected = None
    if all((scenarios.get(k) or {}).get("ok") for k in ("bear", "base", "bull")):
        expected = sum(
            float(scenarios[k]["probability"]) * float(scenarios[k]["price_mid"])
            for k in ("bear", "base", "bull")
        )

    ok = any(s.get("ok") for s in scenarios.values()) and not errors
    result = {
        "ticker": ticker,
        "ok": ok,
        "method": f"driver_{method}_bridge",
        "horizon": HORIZON_LABEL,
        "driver_mode": driver_mode,
        "spot_price": spot,
        "street_target": street_tgt,
        "anchor_metric": metric,
        "anchor_metric_label": metric_label,
        "anchor_ebitda": ebitda,
        "anchor_multiple": cur_mult,
        "net_debt": net_debt,
        "shares": shares,
        "peer_multiple_band": {"low": peer_lo, "mid": peer_mid, "high": peer_hi},
        "headwinds": headwinds,
        "tailwinds": tailwinds,
        "scenarios": scenarios,
        "expected_mid": expected,
        "errors": errors,
        "notes": notes,
    }
    result["report_markdown"] = format_scenario_ranges_markdown(result)
    return result


def format_scenario_ranges_markdown(result: dict[str, Any]) -> str:
    lines = [
        "## Scenario price ranges (headwinds & tailwinds)",
        "",
        f"> Medium-term ({result.get('horizon') or HORIZON_LABEL}) driver → EV/EBITDA bridge. "
        "Distinct from the FCF DCF path. Not investment advice.",
        "",
    ]
    if result.get("spot_price") is not None:
        lines.append(f"- Spot: ${float(result['spot_price']):.2f}")
    if result.get("street_target") is not None:
        lines.append(f"- Sparse Street mean target: ${float(result['street_target']):.2f}")
    if result.get("anchor_multiple") is not None:
        lines.append(f"- Anchor multiple: {float(result['anchor_multiple']):.1f}x ({result.get('method')})")
    if result.get("anchor_metric") is not None:
        label = result.get("anchor_metric_label") or "Metric"
        lines.append(f"- Anchor {label}: {_money(result['anchor_metric'])}")
    elif result.get("anchor_ebitda") is not None:
        lines.append(f"- Anchor EBITDA (TTM/latest): {_money(result['anchor_ebitda'])}")
    if result.get("expected_mid") is not None:
        lines.append(
            f"- Probability-weighted midpoint: **${float(result['expected_mid']):.2f}** "
            f"(heuristic weights, not a rating)"
        )
    lines.append(f"- Driver extraction: `{result.get('driver_mode')}`")
    lines.append("")

    lines += ["### Headwinds (bear-case fuel)", ""]
    for h in result.get("headwinds") or []:
        lines.append(f"- **{h.get('theme')}** — {h.get('signal')} _(source: {h.get('source')})_")
    if not result.get("headwinds"):
        lines.append("- _None extracted._")
    lines.append("")

    lines += ["### Tailwinds (bull-case fuel)", ""]
    for t in result.get("tailwinds") or []:
        lines.append(f"- **{t.get('theme')}** — {t.get('signal')} _(source: {t.get('source')})_")
    if not result.get("tailwinds"):
        lines.append("- _None extracted._")
    lines.append("")

    metric_col = "Metric vs TTM"
    lines += [
        "### Price ranges by case",
        "",
        f"| Case | Prob. | {metric_col} | Multiple | Price low | Mid | High | Upside vs spot |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for key in ("bear", "base", "bull"):
        sc = (result.get("scenarios") or {}).get(key) or {}
        if not sc:
            continue
        if not sc.get("ok"):
            lines.append(f"| {key} | {sc.get('probability', '—')} | — | — | — | — | — | {sc.get('error', 'n/a')} |")
            continue
        ups = sc.get("upside_vs_spot")
        ups_s = f"{ups:+.0%}" if ups is not None else "—"
        vs = sc.get("metric_vs_ttm") if sc.get("metric_vs_ttm") is not None else sc.get("ebitda_vs_ttm")
        lines.append(
            f"| {key} | {sc.get('probability')} | {float(vs):.2f}x | "
            f"{float(sc['multiple']):.1f}x | "
            f"${float(sc['price_low']):.2f} | ${float(sc['price_mid']):.2f} | ${float(sc['price_high']):.2f} | "
            f"{ups_s} |"
        )
    lines.append("")

    for key in ("bear", "base", "bull"):
        sc = (result.get("scenarios") or {}).get(key) or {}
        if not sc:
            continue
        lines.append(f"#### {sc.get('title') or key.title()}")
        lines.append("")
        lines.append(sc.get("narrative") or "")
        lines.append("")
        if sc.get("ok"):
            mlabel = sc.get("metric_label") or "EBITDA"
            mval = sc.get("metric") if sc.get("metric") is not None else sc.get("ebitda")
            lines.append(
                f"- **Range:** ${float(sc['price_low']):.2f} – ${float(sc['price_high']):.2f} "
                f"(mid ${float(sc['price_mid']):.2f}) · {mlabel} {_money(mval)} · "
                f"multiple {float(sc['multiple']):.1f}x"
            )
        for d in sc.get("key_drivers") or []:
            lines.append(f"- Driver: **{d.get('theme')}** — {(d.get('signal') or '')[:160]}")
        lines.append("")

    if result.get("notes"):
        lines += ["### Method notes", ""]
        for n in result["notes"]:
            lines.append(f"- {n}")
        lines.append(
            "- Mapping follows Gemini/Perplexity-style scenario memos: qualitative drivers → "
            "operating metric & multiple paths → share-price ranges over a medium-term horizon."
        )
        lines.append("")

    if result.get("errors"):
        lines += ["### Errors", ""]
        for e in result["errors"]:
            lines.append(f"- {e}")
        lines.append("")

    return "\n".join(lines)
