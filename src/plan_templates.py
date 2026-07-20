"""Goal-based research plan templates (valuation, deep, income, fast)."""

from __future__ import annotations

from typing import Any

from src.plan_schema import PlanSection


TEMPLATES: dict[str, dict[str, Any]] = {
    "auto": {
        "id": "auto",
        "label": "Auto (from goal)",
        "description": "Pick valuation / income / deep / fast from your goal text",
    },
    "valuation": {
        "id": "valuation",
        "label": "Valuation (DCF + Street + drivers)",
        "description": "Financials → assumptions/DCF → analyst targets → market drivers → scenarios",
    },
    "deep": {
        "id": "deep",
        "label": "Full diligence",
        "description": "Fundamentals, DCF, options, web, 10-K risks & MD&A",
    },
    "income": {
        "id": "income",
        "label": "Options income",
        "description": "Fundamentals + put screen (+ light web); skip heavy SEC by default",
    },
    "fast": {
        "id": "fast",
        "label": "Fast quant",
        "description": "Fundamentals + DCF + puts; runs quickly",
    },
}


def list_templates() -> list[dict[str, Any]]:
    order = ["auto", "valuation", "deep", "income", "fast"]
    return [TEMPLATES[k] for k in order if k in TEMPLATES]


def infer_template_from_goal(goal: str, mode: str = "deep") -> str:
    """Map free-text goal (and mode) to a template id."""
    g = (goal or "").lower()
    mode = "fast" if mode == "fast" else "deep"

    if mode == "fast" and not g:
        return "fast"

    valuation_kw = (
        "valuat",
        "dcf",
        "intrinsic",
        "fair value",
        "price target",
        "bull",
        "bear",
        "wacc",
        "upside",
        "downside",
        "scenario",
    )
    income_kw = ("covered call", "put income", "wheel", "options income", "premium", "csp", "put screen")
    deep_kw = ("10-k", "10k", "diligence", "risk factor", "md&a", "mda", "filing")

    if any(k in g for k in valuation_kw):
        return "valuation"
    if any(k in g for k in income_kw):
        return "income"
    if any(k in g for k in deep_kw):
        return "deep"
    if mode == "fast":
        return "fast"
    return "deep"


def resolve_template_id(template: str | None, goal: str = "", mode: str = "deep") -> str:
    tid = (template or "auto").strip().lower() or "auto"
    if tid == "auto":
        return infer_template_from_goal(goal, mode)
    if tid in TEMPLATES and tid != "auto":
        return tid
    return infer_template_from_goal(goal, mode)


def _company_queries(ticker: str, company: str | None, goal: str) -> tuple[list[str], list[str]]:
    """Analyst-focused and driver-focused query packs."""
    name = company or ticker
    goal = (goal or "").strip()
    analyst = [
        f"{ticker} analyst price target",
        f"{name} stock rating OR consensus OR upgrade OR downgrade",
    ]
    drivers = [
        f"{name} {ticker} outlook OR catalyst OR commodity OR uranium OR rare earth OR vanadium",
        f"{ticker} sector drivers OR market demand",
    ]
    if goal:
        # Peel commodity-ish tokens from goal into driver queries
        drivers.insert(0, f"{ticker} {goal}")
        analyst.append(f"{ticker} {goal} analyst")
    return analyst[:3], drivers[:3]


def valuation_sections(ticker: str, company: str | None = None, goal: str = "") -> list[PlanSection]:
    """UUUU-style 5-step valuation research plan."""
    analyst_q, driver_q = _company_queries(ticker, company, goal)
    focus = goal.strip() or "intrinsic value under base / bull / bear scenarios"
    return [
        PlanSection(
            id="fundamentals",
            title="(1) Financial statements & key metrics",
            tools=["get_fundamentals"],
            notes=(
                "Revenue, free cash flow, shares outstanding, historical growth rates, "
                f"margins and leverage. Focus: {focus}"
            ),
        ),
        PlanSection(
            id="valuation",
            title="(2) DCF assumptions & intrinsic value",
            tools=["run_dcf"],
            notes=(
                "Establish growth, operating/FCF margins, and WACC; run base / bull / bear "
                "share-price scenarios from the assumption pack"
            ),
        ),
        PlanSection(
            id="web_analysts",
            title="(3) Analyst reports & Street targets",
            tools=["search_web"],
            notes="Consensus targets, ratings, and investment theses from public web sources",
            queries=analyst_q,
        ),
        PlanSection(
            id="web_drivers",
            title="(4) Market & commodity drivers",
            tools=["search_web"],
            notes="Sector/commodity drivers that inform bull/bear assumptions (prices, demand, expansion)",
            queries=driver_q,
        ),
        PlanSection(
            id="sec_fetch",
            title="(5a) SEC 10-K intake",
            tools=["fetch_10k"],
            notes="Latest 10-K for risk and MD&A context behind the valuation",
            enabled=True,
        ),
        PlanSection(
            id="risks",
            title="(5b) Risk factors (Item 1A)",
            tools=["summarize_item_1a"],
            notes="Key risks that should stress the bear case",
        ),
        PlanSection(
            id="mda",
            title="(5c) MD&A (Item 7)",
            tools=["summarize_item_7"],
            notes="Management tone, guidance, and operational cues for scenarios",
        ),
    ]


def income_sections(ticker: str, company: str | None = None, goal: str = "") -> list[PlanSection]:
    focus = goal.strip() or "put/call premium income"
    name = company or ticker
    return [
        PlanSection(
            id="fundamentals",
            title="Fundamentals check",
            tools=["get_fundamentals"],
            notes=f"Liquidity, leverage, and volatility context for income overlays. Focus: {focus}",
        ),
        PlanSection(
            id="options",
            title="Put income screen",
            tools=["screen_puts"],
            notes="~30–60 DTE OTM puts targeting ~10–15% annualized premium",
        ),
        PlanSection(
            id="web_research",
            title="Recent news & catalysts",
            tools=["search_web"],
            notes="Near-term events that could spoil a short-premium thesis",
            queries=[f"{ticker} news", f"{name} earnings OR catalyst"],
            enabled=True,
        ),
        PlanSection(
            id="valuation",
            title="Quick DCF context",
            tools=["run_dcf"],
            notes="Optional valuation anchor vs spot for strike selection",
            enabled=False,
        ),
    ]


def deep_sections(ticker: str, company: str | None = None, goal: str = "") -> list[PlanSection]:
    from src.plan_schema import default_deep_sections

    sections = default_deep_sections()
    if goal.strip():
        for sec in sections:
            if sec.id in {"web_research", "fundamentals", "valuation", "risks"}:
                sec.notes = f"{sec.notes}. Focus: {goal.strip()}"
            if sec.id == "web_research":
                sec.queries = [goal.strip()]
                break
    return sections


def fast_sections(ticker: str, company: str | None = None, goal: str = "") -> list[PlanSection]:
    from src.plan_schema import default_fast_sections

    sections = default_fast_sections()
    if goal.strip():
        sections[0].notes = f"{sections[0].notes}. Focus: {goal.strip()}"
    return sections


def sections_for_template(
    template_id: str,
    ticker: str,
    *,
    company: str | None = None,
    goal: str = "",
) -> list[PlanSection]:
    tid = template_id if template_id in {"valuation", "deep", "income", "fast"} else "deep"
    builders = {
        "valuation": valuation_sections,
        "deep": deep_sections,
        "income": income_sections,
        "fast": fast_sections,
    }
    return builders[tid](ticker, company, goal)


def default_goal_for_template(template_id: str, goal: str = "") -> str:
    if goal.strip():
        return goal.strip()
    defaults = {
        "valuation": "Estimate intrinsic value under base / bull / bear scenarios",
        "deep": "Deep diligence: fundamentals, DCF, web, 10-K risks & MD&A",
        "income": "Screen put/call income opportunities with catalyst awareness",
        "fast": "Quick fundamentals + DCF + put screen",
    }
    return defaults.get(template_id, defaults["deep"])


def suggest_sector_queries_from_goal(goal: str) -> list[str]:
    """Optional helper: extract crude commodity tokens for driver queries."""
    g = (goal or "").lower()
    tokens = []
    for word in ("uranium", "rare earth", "vanadium", "lithium", "copper", "oil", "gas", "gold", "silver"):
        if word in g:
            tokens.append(word)
    return tokens
