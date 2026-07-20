"""Research plan schema for collaborative deep research (Phase 1)."""

from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field


ToolName = Literal[
    "get_fundamentals",
    "screen_puts",
    "fetch_10k",
    "summarize_item_1a",
    "summarize_item_7",
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
    sections: list[PlanSection]
    constraints: PlanConstraints = Field(default_factory=PlanConstraints)
    planner_mode: str = "template"  # template | ollama
    summary_markdown: str = ""

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
            id="sec_fetch",
            title="SEC 10-K intake",
            tools=["fetch_10k"],
            notes="Latest 10-K; extract Item 1A and Item 7",
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
    ]


def plan_summary_markdown(plan: ResearchPlan) -> str:
    lines = [
        f"# Research plan — {plan.ticker}",
        "",
        f"**Goal:** {plan.goal or 'Standard equity research draft'}",
        f"**Mode:** {plan.mode}",
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
    lines += [
        "## Constraints",
        f"- Max steps: {plan.constraints.max_steps}",
        f"- Max sources: {plan.constraints.max_sources}",
        "",
        "_Edit or disable sections, then approve to run._",
        "",
    ]
    return "\n".join(lines)
