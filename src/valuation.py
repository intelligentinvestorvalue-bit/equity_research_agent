"""Valuation assumptions + simple 3-scenario FCF DCF."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


def _clamp(x: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, x))


def _f(val: Any) -> float | None:
    if val is None:
        return None
    try:
        return float(val)
    except (TypeError, ValueError):
        return None


class ScenarioParams(BaseModel):
    """Per-scenario forecast inputs (rates as decimals, e.g. 0.08 = 8%)."""

    label: str
    revenue_growth: float = 0.08
    fcf_margin: float = 0.05
    wacc: float = 0.10
    terminal_growth: float = 0.025
    explicit_years: int = Field(default=5, ge=1, le=15)


class ValuationAssumptions(BaseModel):
    """Editable assumption pack for collaborative planning + DCF."""

    method: str = "revenue_fcf_dcf"
    explicit_years: int = Field(default=5, ge=1, le=15)
    base: ScenarioParams = Field(
        default_factory=lambda: ScenarioParams(label="base", revenue_growth=0.08, fcf_margin=0.05, wacc=0.10, terminal_growth=0.025)
    )
    bull: ScenarioParams = Field(
        default_factory=lambda: ScenarioParams(label="bull", revenue_growth=0.15, fcf_margin=0.08, wacc=0.09, terminal_growth=0.03)
    )
    bear: ScenarioParams = Field(
        default_factory=lambda: ScenarioParams(label="bear", revenue_growth=0.02, fcf_margin=0.02, wacc=0.12, terminal_growth=0.015)
    )
    notes: list[str] = Field(default_factory=list)
    # Optional anchors filled from fundamentals at run time (or left for UI display)
    seed_revenue: float | None = None
    seed_fcf: float | None = None
    seed_shares: float | None = None
    seed_net_debt: float | None = None
    user_edited: bool = False


def default_assumptions() -> ValuationAssumptions:
    return ValuationAssumptions()


def assumptions_from_fundamentals(fund: dict[str, Any]) -> ValuationAssumptions:
    """Derive base/bull/bear heuristics from richer fundamentals."""
    notes: list[str] = []
    revenue = _f(fund.get("revenue"))
    fcf = _f(fund.get("free_cash_flow"))
    shares = _f(fund.get("shares_outstanding"))
    raw = fund.get("raw_inputs") or {}
    debt = _f(raw.get("total_debt")) or 0.0
    cash = _f(raw.get("cash")) or 0.0
    net_debt = debt - cash

    growth = fund.get("growth") or {}
    hist_g = _f(growth.get("latest_revenue_yoy"))
    if hist_g is None:
        hist_g = _f(growth.get("revenue_cagr"))
    if hist_g is None:
        hist_g = 0.08
        notes.append("No revenue growth history; defaulted base growth to 8%.")
    else:
        notes.append(f"Base revenue growth seeded from historical rate ({hist_g * 100:.1f}%).")

    if hist_g < 0:
        notes.append(
            f"Recent revenue declined ({hist_g * 100:.1f}% YoY); "
            "base/bull use normalized mid-cycle growth instead of extrapolating the decline."
        )
        base_g = 0.06
        bull_g = 0.15
        bear_g = _clamp(hist_g, -0.25, 0.0)
    else:
        base_g = _clamp(hist_g, -0.15, 0.35)
        bull_g = _clamp(base_g + 0.07, -0.05, 0.45)
        bear_g = _clamp(base_g - 0.07, -0.25, 0.25)

    op_margin = _f(fund.get("operating_margin"))
    if revenue and revenue != 0 and fcf is not None:
        fcf_m = fcf / revenue
    elif op_margin is not None:
        fcf_m = op_margin * 0.6
        notes.append("FCF margin approximated from operating margin.")
    else:
        fcf_m = 0.05
        notes.append("No FCF/revenue; defaulted FCF margin to 5%.")

    # Negative FCF margins are common for developers/miners — normalize for going-concern DCF
    if fcf_m < 0:
        notes.append(
            f"Latest FCF margin was {fcf_m * 100:.1f}%; "
            "scenarios use normalized positive margins for a going-concern DCF."
        )
        base_m, bull_m, bear_m = 0.03, 0.08, 0.01
    else:
        base_m = _clamp(fcf_m, 0.01, 0.25)
        bull_m = _clamp(base_m + 0.03, 0.02, 0.30)
        bear_m = _clamp(base_m - 0.02, 0.005, 0.20)

    if not revenue or revenue <= 0:
        notes.append("Missing/invalid revenue — DCF may be unreliable.")
    if not shares or shares <= 0:
        notes.append("Missing shares outstanding — cannot compute per-share value.")

    return ValuationAssumptions(
        seed_revenue=revenue,
        seed_fcf=fcf,
        seed_shares=shares,
        seed_net_debt=net_debt,
        base=ScenarioParams(label="base", revenue_growth=base_g, fcf_margin=base_m, wacc=0.10, terminal_growth=0.025),
        bull=ScenarioParams(label="bull", revenue_growth=bull_g, fcf_margin=bull_m, wacc=0.09, terminal_growth=0.03),
        bear=ScenarioParams(label="bear", revenue_growth=bear_g, fcf_margin=bear_m, wacc=0.12, terminal_growth=0.015),
        notes=notes,
        user_edited=False,
    )


def merge_assumptions(
    fund: dict[str, Any],
    overrides: ValuationAssumptions | dict[str, Any] | None,
) -> ValuationAssumptions:
    """Auto-seed from fundamentals; keep user-edited scenario rates when provided."""
    auto = assumptions_from_fundamentals(fund)
    if not overrides:
        return auto
    if isinstance(overrides, dict):
        overrides = ValuationAssumptions.model_validate(overrides)

    # Always refresh seed anchors from live fundamentals
    merged = overrides.model_copy(deep=True)
    merged.seed_revenue = auto.seed_revenue
    merged.seed_fcf = auto.seed_fcf
    merged.seed_shares = auto.seed_shares
    merged.seed_net_debt = auto.seed_net_debt

    if not overrides.user_edited:
        # Plan still has generic defaults — prefer auto-seeded scenarios
        merged.base = auto.base
        merged.bull = auto.bull
        merged.bear = auto.bear
        merged.notes = auto.notes
    else:
        merged.notes = list(dict.fromkeys([*(auto.notes or []), *(overrides.notes or [])]))

    years = overrides.explicit_years or auto.explicit_years
    merged.explicit_years = years
    for sc in (merged.base, merged.bull, merged.bear):
        sc.explicit_years = years
    return merged


def _project_scenario(
    revenue0: float,
    net_debt: float,
    shares: float,
    params: ScenarioParams,
    price: float | None,
) -> dict[str, Any]:
    wacc = params.wacc
    g_t = params.terminal_growth
    warnings: list[str] = []
    if wacc <= g_t:
        warnings.append(f"{params.label}: WACC ({wacc:.1%}) <= terminal growth ({g_t:.1%}); capped terminal growth.")
        g_t = wacc - 0.005

    years = params.explicit_years
    cashflows: list[dict[str, Any]] = []
    rev = revenue0
    pv_fcf = 0.0
    fcf_n = 0.0
    for t in range(1, years + 1):
        rev = rev * (1.0 + params.revenue_growth)
        fcf = rev * params.fcf_margin
        disc = (1.0 + wacc) ** t
        pv = fcf / disc
        pv_fcf += pv
        fcf_n = fcf
        cashflows.append({"year": t, "revenue": rev, "fcf": fcf, "pv_fcf": pv})

    tv = fcf_n * (1.0 + g_t) / (wacc - g_t) if (wacc - g_t) else 0.0
    pv_tv = tv / ((1.0 + wacc) ** years)
    enterprise_value = pv_fcf + pv_tv
    equity_value = enterprise_value - net_debt
    share_price = None
    if shares:
        share_price = equity_value / shares
        if share_price < 0:
            warnings.append(
                f"{params.label}: model equity value is negative after net debt "
                f"({equity_value:,.0f}); showing ${share_price:.2f}/sh."
            )
    upside = None
    if share_price is not None and price not in (None, 0):
        upside = (share_price / float(price)) - 1.0

    return {
        "label": params.label,
        "params": params.model_dump(),
        "cashflows": cashflows,
        "terminal_value": tv,
        "pv_terminal_value": pv_tv,
        "enterprise_value": enterprise_value,
        "equity_value": equity_value,
        "share_price": share_price,
        "upside_vs_price": upside,
        "warnings": warnings,
    }


def run_dcf(
    fund: dict[str, Any],
    assumptions: ValuationAssumptions,
) -> dict[str, Any]:
    """
    Revenue → FCF margin bridge DCF for base / bull / bear.
    Equity value ≈ PV(FCFs) + PV(terminal) − net debt.
    """
    revenue0 = _f(assumptions.seed_revenue) or _f(fund.get("revenue"))
    shares = _f(assumptions.seed_shares) or _f(fund.get("shares_outstanding"))
    net_debt = _f(assumptions.seed_net_debt)
    if net_debt is None:
        raw = fund.get("raw_inputs") or {}
        net_debt = (_f(raw.get("total_debt")) or 0.0) - (_f(raw.get("cash")) or 0.0)
    price = _f(fund.get("price"))

    errors: list[str] = []
    if not revenue0 or revenue0 <= 0:
        errors.append("Cannot run DCF without positive base revenue.")
    if not shares or shares <= 0:
        errors.append("Cannot run DCF without shares outstanding.")

    if errors:
        return {
            "ok": False,
            "errors": errors,
            "assumptions": assumptions.model_dump(),
            "scenarios": {},
            "spot_price": price,
        }

    scenarios = {
        "base": _project_scenario(revenue0, net_debt, shares, assumptions.base, price),
        "bull": _project_scenario(revenue0, net_debt, shares, assumptions.bull, price),
        "bear": _project_scenario(revenue0, net_debt, shares, assumptions.bear, price),
    }

    return {
        "ok": True,
        "method": assumptions.method,
        "spot_price": price,
        "base_revenue": revenue0,
        "shares": shares,
        "net_debt": net_debt,
        "assumptions": assumptions.model_dump(),
        "scenarios": scenarios,
        "notes": assumptions.notes,
    }


def _fmt_money(val: float | None) -> str:
    if val is None:
        return "—"
    abs_v = abs(val)
    sign = "-" if val < 0 else ""
    if abs_v >= 1e9:
        return f"{sign}${abs_v / 1e9:.2f}B"
    if abs_v >= 1e6:
        return f"{sign}${abs_v / 1e6:.2f}M"
    return f"{sign}${abs_v:,.0f}"


def _fmt_pct(val: float | None) -> str:
    if val is None:
        return "—"
    return f"{val * 100:.1f}%"


def _fmt_price(val: float | None) -> str:
    if val is None:
        return "—"
    return f"${val:.2f}"


def _fmt_shares(val: float | None) -> str:
    if val is None:
        return "—"
    if val >= 1e9:
        return f"{val / 1e9:.2f}B"
    if val >= 1e6:
        return f"{val / 1e6:.2f}M"
    return f"{val:,.0f}"


def format_valuation_markdown(valuation: dict[str, Any]) -> str:
    lines = [
        "## DCF valuation (base / bull / bear)",
        "",
        "> Simplified revenue->FCF DCF. Not investment advice; assumptions are editable heuristics.",
        "",
    ]
    if not valuation.get("ok"):
        for err in valuation.get("errors") or []:
            lines.append(f"- **Error:** {err}")
        return "\n".join(lines) + "\n"

    lines += [
        f"- Spot price: {_fmt_price(_f(valuation.get('spot_price')))}",
        f"- Base revenue: {_fmt_money(_f(valuation.get('base_revenue')))}",
        f"- Shares: {_fmt_shares(_f(valuation.get('shares')))}",
        f"- Net debt (Debt−Cash): {_fmt_money(_f(valuation.get('net_debt')))}",
        "",
    ]

    # HTML table avoids markdown→CSS column crush on Equity value / Share price
    headers = ["Scenario", "Growth", "FCF margin", "WACC", "Term. g", "Equity value", "Share price", "Upside"]
    body_rows: list[str] = []
    for key in ("bear", "base", "bull"):
        sc = (valuation.get("scenarios") or {}).get(key) or {}
        p = sc.get("params") or {}
        cells = [
            key,
            _fmt_pct(p.get("revenue_growth")),
            _fmt_pct(p.get("fcf_margin")),
            _fmt_pct(p.get("wacc")),
            _fmt_pct(p.get("terminal_growth")),
            _fmt_money(_f(sc.get("equity_value"))),
            _fmt_price(_f(sc.get("share_price"))),
            _fmt_pct(_f(sc.get("upside_vs_price"))),
        ]
        tds = "".join(
            f'<td class="num">{c}</td>' if i else f"<td>{c}</td>" for i, c in enumerate(cells)
        )
        body_rows.append(f"<tr>{tds}</tr>")
    ths = "".join(
        f'<th class="num">{h}</th>' if i else f"<th>{h}</th>" for i, h in enumerate(headers)
    )
    lines.append(
        '<div class="table-scroll"><table class="fin-table">'
        f"<thead><tr>{ths}</tr></thead>"
        f"<tbody>{''.join(body_rows)}</tbody>"
        "</table></div>"
    )
    lines.append("")

    notes = valuation.get("notes") or []
    if notes:
        lines.append("### Assumption notes")
        for n in notes:
            lines.append(f"- {n}")
        lines.append("")

    for key in ("base", "bull", "bear"):
        sc = (valuation.get("scenarios") or {}).get(key) or {}
        for w in sc.get("warnings") or []:
            lines.append(f"- _{w}_")

    # Brief base-case path
    base = (valuation.get("scenarios") or {}).get("base") or {}
    cfs = base.get("cashflows") or []
    if cfs:
        lines += ["", "### Base-case projected FCF", ""]
        for row in cfs:
            lines.append(
                f"- Year {row['year']}: revenue {_fmt_money(row['revenue'])}, "
                f"FCF {_fmt_money(row['fcf'])} (PV {_fmt_money(row['pv_fcf'])})"
            )
        lines.append(
            f"- Terminal value {_fmt_money(_f(base.get('terminal_value')))} "
            f"(PV {_fmt_money(_f(base.get('pv_terminal_value')))})"
        )
        lines.append("")

    return "\n".join(lines) + "\n"
