"""EV/EBITDA priced-in scenario valuation (parallel to DCF)."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


def _f(val: Any) -> float | None:
    if val is None:
        return None
    try:
        return float(val)
    except (TypeError, ValueError):
        return None


def _clamp(x: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, x))


class MultiplesScenario(BaseModel):
    label: str
    ebitda: float | None = None
    multiple: float = 8.0


class MultiplesAssumptions(BaseModel):
    """Editable EV/EBITDA scenario pack for memo / valuation plans."""

    method: str = "ev_ebitda"
    base: MultiplesScenario = Field(default_factory=lambda: MultiplesScenario(label="base", multiple=8.0))
    bull: MultiplesScenario = Field(default_factory=lambda: MultiplesScenario(label="bull", multiple=10.0))
    bear: MultiplesScenario = Field(default_factory=lambda: MultiplesScenario(label="bear", multiple=5.0))
    notes: list[str] = Field(default_factory=list)
    seed_ebitda: float | None = None
    seed_multiple: float | None = None
    seed_net_debt: float | None = None
    seed_shares: float | None = None
    user_edited: bool = False


def default_multiples() -> MultiplesAssumptions:
    return MultiplesAssumptions()


def multiples_from_fundamentals(fund: dict[str, Any]) -> MultiplesAssumptions:
    notes: list[str] = []
    ebitda = _f(fund.get("ebitda")) or _f((fund.get("snapshot") or {}).get("ebitda"))
    raw = fund.get("raw_inputs") or {}
    net_debt = _f(raw.get("net_debt"))
    if net_debt is None:
        debt = _f(raw.get("total_debt")) or 0.0
        cash = _f(raw.get("cash")) or 0.0
        net_debt = debt - cash
    shares = _f(fund.get("shares_outstanding"))
    cur_mult = _f((fund.get("ratios") or {}).get("ev_to_ebitda")) or _f(
        (fund.get("snapshot") or {}).get("ev_to_ebitda")
    )

    if ebitda is None or ebitda <= 0:
        notes.append("EBITDA missing or non-positive; scenarios use placeholder $1B EBITDA — edit before relying on prices.")
        ebitda = 1_000_000_000.0
    else:
        notes.append(f"Base EBITDA seeded from latest reported/TTM figure ({ebitda:,.0f}).")

    if cur_mult is None or cur_mult <= 0:
        cur_mult = 8.0
        notes.append("No current EV/EBITDA; defaulted base multiple to 8.0x.")
    else:
        notes.append(f"Base multiple seeded from current EV/EBITDA ({cur_mult:.1f}x).")
        cur_mult = _clamp(cur_mult, 2.0, 40.0)

    base_m = cur_mult
    bull_m = _clamp(base_m * 1.25, base_m + 0.5, 45.0)
    bear_m = _clamp(base_m * 0.75, 1.5, base_m - 0.25 if base_m > 2 else 2.0)

    return MultiplesAssumptions(
        base=MultiplesScenario(label="base", ebitda=ebitda, multiple=base_m),
        bull=MultiplesScenario(label="bull", ebitda=ebitda * 1.2, multiple=bull_m),
        bear=MultiplesScenario(label="bear", ebitda=ebitda * 0.7, multiple=bear_m),
        notes=notes,
        seed_ebitda=ebitda,
        seed_multiple=base_m,
        seed_net_debt=net_debt,
        seed_shares=shares,
        user_edited=False,
    )


def merge_multiples(
    fund: dict[str, Any],
    plan_multiples: dict[str, Any] | MultiplesAssumptions | None,
) -> MultiplesAssumptions:
    seeded = multiples_from_fundamentals(fund)
    if plan_multiples is None:
        return seeded
    if isinstance(plan_multiples, MultiplesAssumptions):
        raw = plan_multiples.model_dump()
    else:
        raw = dict(plan_multiples)
    if not raw.get("user_edited"):
        # Keep seeds unless user edited; still allow partial overrides of multiples
        return seeded
    patched = seeded.model_dump()
    for scen in ("base", "bull", "bear"):
        if isinstance(raw.get(scen), dict):
            patched[scen] = {**patched.get(scen, {}), **raw[scen], "label": scen}
    patched["user_edited"] = True
    patched["notes"] = list(dict.fromkeys([*(seeded.notes), *((raw.get("notes") or []))]))
    return MultiplesAssumptions.model_validate(patched)


def run_ev_ebitda(
    fund: dict[str, Any],
    assumptions: MultiplesAssumptions | None = None,
) -> dict[str, Any]:
    """Priced-in share prices = (EBITDA × multiple − net debt) / shares."""
    assumptions = assumptions or multiples_from_fundamentals(fund)
    raw = fund.get("raw_inputs") or {}
    net_debt = _f(assumptions.seed_net_debt)
    if net_debt is None:
        net_debt = _f(raw.get("net_debt"))
    if net_debt is None:
        net_debt = (_f(raw.get("total_debt")) or 0.0) - (_f(raw.get("cash")) or 0.0)
    shares = _f(assumptions.seed_shares) or _f(fund.get("shares_outstanding"))
    spot = _f(fund.get("price"))
    errors: list[str] = []
    if shares in (None, 0):
        errors.append("Missing shares outstanding")
    scenarios: dict[str, Any] = {}
    for key in ("bear", "base", "bull"):
        sc: MultiplesScenario = getattr(assumptions, key)
        ebitda = _f(sc.ebitda)
        multiple = _f(sc.multiple) or 0.0
        if ebitda is None:
            scenarios[key] = {"label": key, "ok": False, "error": "missing EBITDA"}
            continue
        ev = ebitda * multiple
        equity = ev - (net_debt or 0.0)
        share_price = (equity / shares) if shares not in (None, 0) else None
        scenarios[key] = {
            "label": key,
            "ok": share_price is not None,
            "ebitda": ebitda,
            "multiple": multiple,
            "enterprise_value": ev,
            "net_debt": net_debt,
            "equity_value": equity,
            "share_price": share_price,
        }
    ok = any(s.get("ok") for s in scenarios.values()) and not errors
    return {
        "ok": ok,
        "method": "ev_ebitda",
        "assumptions": assumptions.model_dump(),
        "spot_price": spot,
        "net_debt": net_debt,
        "shares": shares,
        "scenarios": scenarios,
        "errors": errors,
        "notes": list(assumptions.notes),
    }


def format_multiples_markdown(result: dict[str, Any]) -> str:
    lines = [
        "## Valuation — EV/EBITDA scenarios",
        "",
        "> Priced-in model: implied price = (EBITDA × EV/EBITDA − net debt) ÷ shares. Not a forecast.",
        "",
    ]
    if result.get("spot_price") is not None:
        lines.append(f"- Spot: ${float(result['spot_price']):.2f}")
    if result.get("net_debt") is not None:
        nd = float(result["net_debt"])
        sign = "-" if nd < 0 else ""
        abs_v = abs(nd)
        if abs_v >= 1e9:
            nd_s = f"{sign}${abs_v / 1e9:.2f}B"
        elif abs_v >= 1e6:
            nd_s = f"{sign}${abs_v / 1e6:.2f}M"
        else:
            nd_s = f"{sign}${abs_v:,.0f}"
        lines.append(f"- Net debt used: {nd_s}")
    lines.append("")
    lines.append(
        '<div class="table-scroll"><table class="fin-table">'
        "<thead><tr>"
        "<th>Scenario</th>"
        '<th class="num">EBITDA</th>'
        '<th class="num">EV/EBITDA</th>'
        '<th class="num">Implied EV</th>'
        '<th class="num">Equity value</th>'
        '<th class="num">Implied price</th>'
        "</tr></thead><tbody>"
    )
    for key in ("bear", "base", "bull"):
        sc = (result.get("scenarios") or {}).get(key) or {}
        if not sc:
            continue
        ebitda = sc.get("ebitda")
        mult = sc.get("multiple")
        ev = sc.get("enterprise_value")
        eq = sc.get("equity_value")
        px = sc.get("share_price")

        def _m(v: Any) -> str:
            if v is None:
                return "—"
            v = float(v)
            sign = "-" if v < 0 else ""
            a = abs(v)
            if a >= 1e9:
                return f"{sign}${a / 1e9:.2f}B"
            if a >= 1e6:
                return f"{sign}${a / 1e6:.2f}M"
            return f"{sign}${a:,.0f}"

        lines.append(
            "<tr>"
            f"<td>{key}</td>"
            f'<td class="num">{_m(ebitda)}</td>'
            f'<td class="num">{f"{float(mult):.1f}x" if mult is not None else "—"}</td>'
            f'<td class="num">{_m(ev)}</td>'
            f'<td class="num">{_m(eq)}</td>'
            f'<td class="num">{f"${float(px):.2f}" if px is not None else "—"}</td>'
            "</tr>"
        )
    lines.append("</tbody></table></div>")
    lines.append("")
    for n in result.get("notes") or []:
        lines.append(f"- {n}")
    for e in result.get("errors") or []:
        lines.append(f"- **Error:** {e}")
    lines.append("")
    return "\n".join(lines) + "\n"
