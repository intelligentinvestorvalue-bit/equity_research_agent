"""Goal-based research plan templates (valuation, deep, income, fast)."""

from __future__ import annotations

from typing import Any

from src.plan_schema import PlanSection


TEMPLATES: dict[str, dict[str, Any]] = {
    "auto": {
        "id": "auto",
        "label": "Auto (from goal)",
        "description": "Pick valuation / income / deep / memo / fast from your goal text",
    },
    "all": {
        "id": "all",
        "label": "All templates (full pack)",
        "description": "Run memo + valuation + deep + income + fast for one equity; view each in its own tab",
    },
    "memo": {
        "id": "memo",
        "label": "Institutional deep dive (memo)",
        "description": "Thesis memo: KPIs, EV/EBITDA + DCF, peers, catalysts, falsifiers, earnings, drivers",
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

# Templates included in a full-pack run (order = UI tab order)
PACK_TEMPLATE_IDS: list[str] = ["memo", "valuation", "deep", "income", "fast"]


def list_templates() -> list[dict[str, Any]]:
    order = ["all", "auto", "memo", "valuation", "deep", "income", "fast"]
    return [TEMPLATES[k] for k in order if k in TEMPLATES]


def infer_template_from_goal(goal: str, mode: str = "deep") -> str:
    """Map free-text goal (and mode) to a template id."""
    g = (goal or "").lower()
    mode = "fast" if mode == "fast" else "deep"

    if mode == "fast" and not g:
        return "fast"

    all_kw = ("all templates", "full pack", "every template", "run all", "complete pack")
    memo_kw = (
        "memo",
        "thesis",
        "deep dive",
        "deep-dive",
        "variant",
        "falsif",
        "catalyst calendar",
        "institutional",
    )
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

    if any(k in g for k in all_kw):
        return "all"
    if any(k in g for k in memo_kw):
        return "memo"
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
    if tid == "all":
        return "all"
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
            id="multiples",
            title="(2b) EV/EBITDA priced-in scenarios",
            tools=["run_ev_ebitda"],
            notes="Cross-check DCF with EBITDA × multiple scenarios",
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
            notes="Latest 10-K for business, risk, and MD&A context behind the valuation",
            enabled=True,
        ),
        PlanSection(
            id="business",
            title="(5b) Business overview (Item 1)",
            tools=["summarize_item_1"],
            notes="What the company does — products, segments, customers, competitive position",
        ),
        PlanSection(
            id="risks",
            title="(5c) Risk factors (Item 1A)",
            tools=["summarize_item_1a"],
            notes="Key risks that should stress the bear case",
        ),
        PlanSection(
            id="mda",
            title="(5d) MD&A (Item 7)",
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


def memo_sections(ticker: str, company: str | None = None, goal: str = "") -> list[PlanSection]:
    """Institutional deep-dive memo (Perplexity-style spine)."""
    name = company or ticker
    focus = goal.strip() or "institutional deep-dive: thesis, priced-in scenarios, catalysts, falsifiers"
    analyst_q, driver_q = _company_queries(ticker, company, goal)
    return [
        PlanSection(
            id="fundamentals",
            title="(1) Snapshot, KPIs & capital structure",
            tools=["get_fundamentals"],
            notes=f"Multi-year KPI table, leverage, EV/EBITDA snapshot. Focus: {focus}",
        ),
        PlanSection(
            id="multiples",
            title="(2) EV/EBITDA priced-in scenarios",
            tools=["run_ev_ebitda"],
            notes="Bear/base/bull EBITDA × multiple → implied equity value",
        ),
        PlanSection(
            id="valuation",
            title="(3) DCF cross-check",
            tools=["run_dcf"],
            notes="FCF DCF as second valuation lens vs multiples",
        ),
        PlanSection(
            id="peers",
            title="(4) Peer & factor comps",
            tools=["get_peer_comps"],
            notes="Heuristic sector peers: returns, EV/EBITDA, leverage, volatility",
        ),
        PlanSection(
            id="earnings",
            title="(5) Earnings & surprise history",
            tools=["get_earnings"],
            notes="EPS estimate vs actual vs 1-day move when available",
        ),
        PlanSection(
            id="web_analysts",
            title="(6a) Street / narrative web",
            tools=["search_web"],
            notes="Analyst targets, thesis debates, guidance headlines",
            queries=analyst_q + [f"{ticker} guidance OR investor day OR catalyst"],
        ),
        PlanSection(
            id="web_drivers",
            title="(6b) Drivers & proxies",
            tools=["search_web"],
            notes="Operating KPIs, contracts, refinancing, sector drivers",
            queries=driver_q + [f"{name} {ticker} backlog OR contract OR refinancing OR leverage"],
        ),
        PlanSection(
            id="sec_fetch",
            title="(7a) SEC 10-K intake",
            tools=["fetch_10k"],
            notes="Latest 10-K for business, risks, and MD&A",
        ),
        PlanSection(
            id="recent_filings",
            title="(7b) Recent 10-Q / 8-K headlines",
            tools=["fetch_recent_filings"],
            notes="Catalyst calendar inputs — meta only, not full parse",
        ),
        PlanSection(
            id="business",
            title="(7c) Business overview (Item 1)",
            tools=["summarize_item_1"],
            notes="Company setup & business model from 10-K Item 1",
        ),
        PlanSection(
            id="risks",
            title="(7d) Risk factors (Item 1A)",
            tools=["summarize_item_1a"],
            notes="Falsification inputs from filing risks",
        ),
        PlanSection(
            id="mda",
            title="(7e) MD&A (Item 7)",
            tools=["summarize_item_7"],
            notes="Guidance cues and operating commentary",
        ),
        PlanSection(
            id="drivers",
            title="(8) Quarterly driver correlations",
            tools=["analyze_drivers"],
            notes="Suggestive FCF/revenue/debt vs return correlations (small-n caveats)",
        ),
        PlanSection(
            id="memo",
            title="(9) Thesis memo sections",
            tools=["draft_memo_sections"],
            notes="Exec summary, variant perception, catalysts, falsifiers, limitations",
        ),
    ]


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
    tid = template_id if template_id in {"valuation", "deep", "income", "fast", "memo"} else "deep"
    builders = {
        "valuation": valuation_sections,
        "deep": deep_sections,
        "income": income_sections,
        "fast": fast_sections,
        "memo": memo_sections,
    }
    return builders[tid](ticker, company, goal)


def default_goal_for_template(template_id: str, goal: str = "") -> str:
    if goal.strip():
        return goal.strip()
    defaults = {
        "all": "Full research pack across all templates",
        "memo": "Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers",
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
