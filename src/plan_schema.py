"""Research plan schema for collaborative deep research (Phase 1)."""

from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field

from src.multiples import MultiplesAssumptions, default_multiples
from src.valuation import ValuationAssumptions, default_assumptions


ToolName = Literal[
    "get_fundamentals",
    "screen_puts",
    "fetch_10k",
    "summarize_item_1",
    "summarize_item_1a",
    "summarize_item_7",
    "run_dcf",
    "run_ev_ebitda",
    "build_scenario_ranges",
    "run_altman_z",
    "get_peer_comps",
    "get_earnings",
    "fetch_recent_filings",
    "analyze_drivers",
    "draft_memo_sections",
    "search_web",
]


class PlanSection(BaseModel):
    id: str
    title: str
    enabled: bool = True
    tools: list[str] = Field(default_factory=list)
    notes: str = ""
    queries: list[str] = Field(default_factory=list)


class PlanConstraints(BaseModel):
    max_steps: int = 12
    max_sources: int = 40
    mode: str = "deep"


class ResearchPlan(BaseModel):
    ticker: str
    goal: str = ""
    mode: str = "deep"
    template: str = "deep"
    sections: list[PlanSection]
    constraints: PlanConstraints = Field(default_factory=PlanConstraints)
    planner_mode: str = "template"  # template | ollama
    summary_markdown: str = ""
    assumptions: ValuationAssumptions = Field(default_factory=default_assumptions)
    multiples: MultiplesAssumptions = Field(default_factory=default_multiples)

    def enabled_sections(self) -> list[PlanSection]:
        return [s for s in self.sections if s.enabled]

    def to_public_dict(self) -> dict[str, Any]:
        return self.model_dump()


def default_fast_sections() -> list[PlanSection]:
    return [
        PlanSection(
            id="fundamentals",
            title="Fundamentals & ratios",
            tools=["get_fundamentals"],
            notes="Revenue, FCF, shares, growth rates, ROIC, FCF yield, debt/equity",
        ),
        PlanSection(
            id="valuation",
            title="DCF valuation (base / bull / bear)",
            tools=["run_dcf"],
            notes="Intrinsic value from growth, FCF margin, and WACC assumptions",
        ),
        PlanSection(
            id="options",
            title="Put income screen",
            tools=["screen_puts"],
            notes="~30–60 DTE OTM puts targeting ~10–15% annualized premium",
        ),
    ]


def default_deep_sections() -> list[PlanSection]:
    return [
        *default_fast_sections(),
        PlanSection(
            id="web_research",
            title="News, analysts & market drivers",
            tools=["search_web"],
            notes="Street targets, recent news, sector/commodity drivers via web search + page fetch",
            queries=[],
        ),
        PlanSection(
            id="sec_fetch",
            title="SEC 10-K intake",
            tools=["fetch_10k"],
            notes="Latest 10-K; extract Item 1 (Business), Item 1A, and Item 7",
        ),
        PlanSection(
            id="business",
            title="Business overview (Item 1)",
            tools=["summarize_item_1"],
            notes="Company setup from 10-K Item 1 Business",
        ),
        PlanSection(
            id="risks",
            title="Risk factors (Item 1A)",
            tools=["summarize_item_1a"],
            notes="Qualitative risks from the filing",
        ),
        PlanSection(
            id="mda",
            title="MD&A (Item 7)",
            tools=["summarize_item_7"],
            notes="Management discussion, tone, guidance cues",
        ),
        PlanSection(
            id="altman",
            title="Altman Z — medium-term bankruptcy risk",
            tools=["run_altman_z"],
            notes="Distress screen (classic Z / Z'') for medium-term solvency risk",
        ),
    ]


def plan_summary_markdown(plan: ResearchPlan) -> str:
    lines = [
        f"# Research plan — {plan.ticker}",
        "",
        f"**Goal:** {plan.goal or 'Standard equity research draft'}",
        f"**Mode:** {plan.mode}",
        f"**Template:** {plan.template}",
        f"**Planner:** {plan.planner_mode}",
        "",
        "## Sections",
        "",
    ]
    for i, sec in enumerate(plan.sections, start=1):
        mark = "✓" if sec.enabled else "○"
        tools = ", ".join(sec.tools) if sec.tools else "—"
        lines.append(f"{i}. **{mark} {sec.title}** (`{sec.id}`)")
        lines.append(f"   - Tools: {tools}")
        if sec.notes:
            lines.append(f"   - Notes: {sec.notes}")
        if sec.queries:
            lines.append(f"   - Queries: {'; '.join(sec.queries)}")
        lines.append("")

    a = plan.assumptions
    m = plan.multiples
    lines += [
        "## Valuation assumptions (DCF)",
        f"- Explicit years: {a.explicit_years}",
        f"- Base: growth {a.base.revenue_growth:.1%}, FCF margin {a.base.fcf_margin:.1%}, WACC {a.base.wacc:.1%}",
        f"- Bull: growth {a.bull.revenue_growth:.1%}, FCF margin {a.bull.fcf_margin:.1%}, WACC {a.bull.wacc:.1%}",
        f"- Bear: growth {a.bear.revenue_growth:.1%}, FCF margin {a.bear.fcf_margin:.1%}, WACC {a.bear.wacc:.1%}",
        "",
        "## EV/EBITDA assumptions",
        f"- Base: EBITDA {m.base.ebitda}, multiple {m.base.multiple:.1f}x",
        f"- Bull: EBITDA {m.bull.ebitda}, multiple {m.bull.multiple:.1f}x",
        f"- Bear: EBITDA {m.bear.ebitda}, multiple {m.bear.multiple:.1f}x",
        "",
        "## Constraints",
        f"- Max steps: {plan.constraints.max_steps}",
        f"- Max sources: {plan.constraints.max_sources}",
        "",
        "_Edit or disable sections / assumptions, then approve to run._",
        "",
    ]
    return "\n".join(lines)
