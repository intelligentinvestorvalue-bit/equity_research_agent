"""Altman Z-score — medium-term bankruptcy / distress screen."""

from __future__ import annotations

from typing import Any


def _f(val: Any) -> float | None:
    if val is None:
        return None
    try:
        x = float(val)
    except (TypeError, ValueError):
        return None
    if x != x:  # NaN
        return None
    return x


def _fmt(x: float | None, *, money: bool = False, ratio: bool = False) -> str:
    if x is None:
        return "—"
    if money:
        ax = abs(x)
        if ax >= 1e9:
            return f"${x/1e9:.2f}B"
        if ax >= 1e6:
            return f"${x/1e6:.1f}M"
        return f"${x:,.0f}"
    if ratio:
        return f"{x:.3f}"
    return f"{x:.2f}"


def _is_non_manufacturer(sector: str | None, industry: str | None) -> bool:
    blob = f"{sector or ''} {industry or ''}".lower()
    manufacturing_kw = (
        "manufactur",
        "industrial",
        "machinery",
        "auto",
        "aerospace",
        "chemical",
        "steel",
        "metal",
        "building product",
        "paper",
        "textile",
    )
    non_mfg_kw = (
        "bank",
        "financ",
        "insurance",
        "reit",
        "software",
        "internet",
        "service",
        "retail",
        "health care",
        "healthcare",
        "biotech",
        "pharma",
        "utility",
        "telecom",
        "media",
        "restaurant",
        "hotel",
        "consumer defensive",
        "consumer cyclical",
        "technology",
        "communication",
        "real estate",
    )
    if any(k in blob for k in manufacturing_kw):
        return False
    if any(k in blob for k in non_mfg_kw):
        return True
    # Default: use classic public Z when market cap exists; still show Z''.
    return False


def _zone_classic(z: float) -> tuple[str, str, str]:
    """Return (zone_id, label, medium_term_read)."""
    if z > 2.99:
        return (
            "safe",
            "Safe zone",
            "Classic Altman thresholds imply low near-term bankruptcy probability; "
            "still monitor leverage and cash burn over an 18–36 month horizon.",
        )
    if z >= 1.81:
        return (
            "grey",
            "Grey zone",
            "Elevated distress risk over a medium-term window — neither clearly safe nor "
            "clearly bankrupt. Stress cash, refinancing, and earnings durability.",
        )
    return (
        "distress",
        "Distress zone",
        "High bankruptcy / credit-stress risk on a medium-term horizon. Treat as a core "
        "falsifier for bullish theses until leverage and earnings repair.",
    )


def _zone_z_double_prime(z: float) -> tuple[str, str, str]:
    # Altman Z'' cutoffs commonly cited: >2.6 safe, <1.1 distress
    if z > 2.60:
        return (
            "safe",
            "Safe zone (Z'')",
            "Non-manufacturer model implies low medium-term insolvency risk; verify liquidity and covenants separately.",
        )
    if z >= 1.10:
        return (
            "grey",
            "Grey zone (Z'')",
            "Medium-term credit risk is ambiguous under the non-manufacturer model — watch WC, RE, and EBIT trends.",
        )
    return (
        "distress",
        "Distress zone (Z'')",
        "Elevated medium-term bankruptcy risk under the non-manufacturer Altman model.",
    )


def _extract_inputs(fund: dict[str, Any]) -> dict[str, Any]:
    cap = fund.get("capital_structure") or {}
    raw = fund.get("raw_inputs") or {}
    snap = fund.get("snapshot") or {}

    total_assets = _f(cap.get("total_assets") or raw.get("total_assets"))
    total_liabilities = _f(cap.get("total_liabilities") or raw.get("total_liabilities"))
    current_assets = _f(cap.get("current_assets") or raw.get("current_assets"))
    current_liabilities = _f(cap.get("current_liabilities") or raw.get("current_liabilities"))
    working_capital = _f(cap.get("working_capital") or raw.get("working_capital"))
    if working_capital is None and current_assets is not None and current_liabilities is not None:
        working_capital = current_assets - current_liabilities

    retained_earnings = _f(cap.get("retained_earnings") or raw.get("retained_earnings"))
    ebit = _f(raw.get("ebit") or fund.get("operating_income"))
    sales = _f(fund.get("revenue"))
    market_equity = _f(fund.get("market_cap") or snap.get("market_cap"))
    book_equity = _f(cap.get("book_equity") or raw.get("equity") or snap.get("book_equity"))

    # Fallback total liabilities ≈ total debt + (rough) if TA and equity known
    if total_liabilities is None and total_assets is not None and book_equity is not None:
        total_liabilities = total_assets - book_equity
    if total_assets is None and total_liabilities is not None and book_equity is not None:
        total_assets = total_liabilities + book_equity

    missing: list[str] = []
    for name, val in (
        ("total_assets", total_assets),
        ("total_liabilities", total_liabilities),
        ("working_capital", working_capital),
        ("retained_earnings", retained_earnings),
        ("ebit", ebit),
        ("sales", sales),
    ):
        if val is None:
            missing.append(name)

    return {
        "total_assets": total_assets,
        "total_liabilities": total_liabilities,
        "current_assets": current_assets,
        "current_liabilities": current_liabilities,
        "working_capital": working_capital,
        "retained_earnings": retained_earnings,
        "ebit": ebit,
        "sales": sales,
        "market_equity": market_equity,
        "book_equity": book_equity,
        "sector": snap.get("sector"),
        "industry": snap.get("industry"),
        "missing": missing,
    }


def compute_altman_z(fund: dict[str, Any] | None) -> dict[str, Any]:
    """
    Compute Altman Z (classic public) and Z'' (non-manufacturer / emerging).

    Classic (1968 public manufacturing):
      X1 = WC/TA, X2 = RE/TA, X3 = EBIT/TA, X4 = MVE/TL, X5 = Sales/TA
      Z  = 1.2 X1 + 1.4 X2 + 3.3 X3 + 0.6 X4 + 1.0 X5
      Zones: Z > 2.99 safe; 1.81–2.99 grey; Z < 1.81 distress

    Z'' (non-manufacturers):
      Z'' = 6.56 X1 + 3.26 X2 + 6.72 X3 + 1.05 X4b  (X4b = book equity / TL)
    """
    ticker = ((fund or {}).get("ticker") or "").upper()
    if not fund or fund.get("error"):
        return {
            "ok": False,
            "ticker": ticker,
            "errors": [fund.get("error") if fund else "No fundamentals"],
            "report_markdown": "",
        }

    inp = _extract_inputs(fund)
    errors: list[str] = []
    notes: list[str] = [
        "Altman Z is a statistical screen from historical samples — not a forecast or credit rating.",
        "Use alongside liquidity, covenants, and refinancing calendar over an 18–36 month horizon.",
    ]

    ta = inp["total_assets"]
    tl = inp["total_liabilities"]
    if ta in (None, 0):
        errors.append("total_assets missing or zero — cannot compute Z ratios")
    if tl in (None, 0):
        errors.append("total_liabilities missing or zero — cannot compute X4")

    components: dict[str, float | None] = {
        "x1_wc_ta": None,
        "x2_re_ta": None,
        "x3_ebit_ta": None,
        "x4_mve_tl": None,
        "x4b_be_tl": None,
        "x5_sales_ta": None,
    }
    if ta not in (None, 0):
        if inp["working_capital"] is not None:
            components["x1_wc_ta"] = inp["working_capital"] / ta
        if inp["retained_earnings"] is not None:
            components["x2_re_ta"] = inp["retained_earnings"] / ta
        if inp["ebit"] is not None:
            components["x3_ebit_ta"] = inp["ebit"] / ta
        if inp["sales"] is not None:
            components["x5_sales_ta"] = inp["sales"] / ta
    if tl not in (None, 0):
        if inp["market_equity"] is not None:
            components["x4_mve_tl"] = inp["market_equity"] / tl
        if inp["book_equity"] is not None:
            components["x4b_be_tl"] = inp["book_equity"] / tl

    z_classic: float | None = None
    classic_ok = all(
        components[k] is not None
        for k in ("x1_wc_ta", "x2_re_ta", "x3_ebit_ta", "x4_mve_tl", "x5_sales_ta")
    )
    if classic_ok:
        z_classic = (
            1.2 * float(components["x1_wc_ta"])
            + 1.4 * float(components["x2_re_ta"])
            + 3.3 * float(components["x3_ebit_ta"])
            + 0.6 * float(components["x4_mve_tl"])
            + 1.0 * float(components["x5_sales_ta"])
        )
    else:
        need = [
            k
            for k in ("x1_wc_ta", "x2_re_ta", "x3_ebit_ta", "x4_mve_tl", "x5_sales_ta")
            if components[k] is None
        ]
        errors.append("Classic Z incomplete — missing " + ", ".join(need))

    z_pp: float | None = None
    zpp_ok = all(
        components[k] is not None for k in ("x1_wc_ta", "x2_re_ta", "x3_ebit_ta", "x4b_be_tl")
    )
    if zpp_ok:
        z_pp = (
            6.56 * float(components["x1_wc_ta"])
            + 3.26 * float(components["x2_re_ta"])
            + 6.72 * float(components["x3_ebit_ta"])
            + 1.05 * float(components["x4b_be_tl"])
        )

    non_mfg = _is_non_manufacturer(inp.get("sector"), inp.get("industry"))
    primary_model = "z_double_prime" if non_mfg and z_pp is not None else "classic"
    if primary_model == "classic" and z_classic is None and z_pp is not None:
        primary_model = "z_double_prime"
        notes.append("Fell back to Z'' because classic public Z inputs were incomplete.")

    primary_z: float | None = z_pp if primary_model == "z_double_prime" else z_classic
    if primary_z is None:
        zone_id, zone_label, medium_term = "n/a", "Insufficient data", (
            "Could not score medium-term bankruptcy risk — missing balance-sheet inputs."
        )
    elif primary_model == "z_double_prime":
        zone_id, zone_label, medium_term = _zone_z_double_prime(primary_z)
    else:
        zone_id, zone_label, medium_term = _zone_classic(primary_z)

    if non_mfg:
        notes.append(
            f"Sector/industry ({inp.get('sector') or '—'} / {inp.get('industry') or '—'}) "
            "leans non-manufacturing; primary screen uses Z'' when available."
        )
    else:
        notes.append("Primary screen uses classic public Altman Z (manufacturing-oriented sample).")

    result: dict[str, Any] = {
        "ok": primary_z is not None,
        "ticker": ticker,
        "inputs": {k: v for k, v in inp.items() if k != "missing"},
        "missing_inputs": inp["missing"],
        "components": components,
        "z_classic": z_classic,
        "z_double_prime": z_pp,
        "primary_model": primary_model,
        "z": primary_z,
        "zone": zone_id,
        "zone_label": zone_label,
        "medium_term_read": medium_term,
        "non_manufacturer": non_mfg,
        "notes": notes,
        "errors": errors,
    }
    result["report_markdown"] = format_altman_markdown(result)
    return result


def format_altman_markdown(result: dict[str, Any]) -> str:
    ticker = result.get("ticker") or ""
    inp = result.get("inputs") or {}
    comp = result.get("components") or {}
    lines = [
        "## Altman Z-score (medium-term bankruptcy risk)",
        "",
        f"**Ticker:** {ticker}",
        f"**Primary model:** `{result.get('primary_model')}`",
        f"**Z-score:** **{_fmt(_f(result.get('z')))}** — {result.get('zone_label') or '—'}",
        "",
        "### Medium-term read (18–36 months)",
        "",
        result.get("medium_term_read") or "_No read available._",
        "",
        "### Model scores",
        "",
        "| Model | Score | Zone guide |",
        "| --- | ---: | --- |",
        (
            f"| Classic public Z | {_fmt(_f(result.get('z_classic')))} | "
            ">2.99 safe · 1.81–2.99 grey · <1.81 distress |"
        ),
        (
            f"| Non-manufacturer Z'' | {_fmt(_f(result.get('z_double_prime')))} | "
            ">2.60 safe · 1.10–2.60 grey · <1.10 distress |"
        ),
        "",
        "### Inputs (latest statements / market)",
        "",
        "| Item | Value |",
        "| --- | ---: |",
        f"| Total assets | {_fmt(_f(inp.get('total_assets')), money=True)} |",
        f"| Total liabilities | {_fmt(_f(inp.get('total_liabilities')), money=True)} |",
        f"| Working capital | {_fmt(_f(inp.get('working_capital')), money=True)} |",
        f"| Current assets | {_fmt(_f(inp.get('current_assets')), money=True)} |",
        f"| Current liabilities | {_fmt(_f(inp.get('current_liabilities')), money=True)} |",
        f"| Retained earnings | {_fmt(_f(inp.get('retained_earnings')), money=True)} |",
        f"| EBIT / operating income | {_fmt(_f(inp.get('ebit')), money=True)} |",
        f"| Sales / revenue | {_fmt(_f(inp.get('sales')), money=True)} |",
        f"| Market value of equity | {_fmt(_f(inp.get('market_equity')), money=True)} |",
        f"| Book equity | {_fmt(_f(inp.get('book_equity')), money=True)} |",
        "",
        "### Ratio components",
        "",
        "| Component | Definition | Value |",
        "| --- | --- | ---: |",
        f"| X1 | Working capital / Total assets | {_fmt(_f(comp.get('x1_wc_ta')), ratio=True)} |",
        f"| X2 | Retained earnings / Total assets | {_fmt(_f(comp.get('x2_re_ta')), ratio=True)} |",
        f"| X3 | EBIT / Total assets | {_fmt(_f(comp.get('x3_ebit_ta')), ratio=True)} |",
        f"| X4 | Market equity / Total liabilities | {_fmt(_f(comp.get('x4_mve_tl')), ratio=True)} |",
        f"| X4b | Book equity / Total liabilities (Z'') | {_fmt(_f(comp.get('x4b_be_tl')), ratio=True)} |",
        f"| X5 | Sales / Total assets | {_fmt(_f(comp.get('x5_sales_ta')), ratio=True)} |",
        "",
        "### Formulas",
        "",
        "- Classic Z = `1.2·X1 + 1.4·X2 + 3.3·X3 + 0.6·X4 + 1.0·X5`",
        "- Z'' = `6.56·X1 + 3.26·X2 + 6.72·X3 + 1.05·X4b`",
        "",
    ]
    if result.get("missing_inputs"):
        lines.append("**Missing inputs:** " + ", ".join(result["missing_inputs"]))
        lines.append("")
    if result.get("errors"):
        lines.append("**Data gaps / errors:**")
        for e in result["errors"]:
            lines.append(f"- {e}")
        lines.append("")
    for n in result.get("notes") or []:
        lines.append(f"- _{n}_")
    lines.append("")
    lines.append(
        "_Not investment advice. Altman thresholds are historical; banks/REITs/financials "
        "are poorly suited to these models._"
    )
    lines.append("")
    return "\n".join(lines)
