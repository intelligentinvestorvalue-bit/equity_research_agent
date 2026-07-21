"""Collaborative research planner: Ollama when available, else templates."""

from __future__ import annotations

import json
import logging
import re
from typing import Any

import httpx

from src.config import settings
from src.nlp_engine import ollama_available
from src.plan_schema import (
    PlanConstraints,
    PlanSection,
    ResearchPlan,
    plan_summary_markdown,
)
from src.valuation import default_assumptions

logger = logging.getLogger(__name__)

PLANNER_PROMPT = """You are an equity research planner. Return ONLY valid JSON (no markdown fences).

Ticker: {ticker}
Mode: {mode}
User goal: {goal}

Produce a research plan with this shape:
{{
  "goal": "refined goal string",
  "sections": [
    {{
      "id": "snake_case_id",
      "title": "Short title",
      "enabled": true,
      "tools": ["tool_name", ...],
      "notes": "what this section should cover",
      "queries": ["optional search-style query"]
    }}
  ]
}}

Allowed tools ONLY:
- get_fundamentals
- screen_puts
- fetch_10k
- summarize_item_1a
- summarize_item_7
- run_dcf
- search_web

Rules:
- For mode "fast": get_fundamentals, run_dcf, and optionally screen_puts.
- For mode "deep": include search_web; include fetch_10k before summarize_item_1a / summarize_item_7; include run_dcf after get_fundamentals.
- Keep 2–8 sections. Prefer concrete notes tied to the user goal.
"""


def build_template_plan(
    ticker: str,
    mode: str = "deep",
    goal: str = "",
    template: str = "auto",
) -> ResearchPlan:
    from src.plan_templates import (
        default_goal_for_template,
        resolve_template_id,
        sections_for_template,
    )

    ticker = ticker.upper().strip()
    mode = "fast" if mode == "fast" else "deep"
    tid = resolve_template_id(template, goal=goal, mode=mode)
    if tid == "all":
        raise ValueError("template=all is a pack run; use run_research_pack / UI All templates")
    # Fast mode forces fast template unless valuation/income explicitly chosen
    if mode == "fast" and (template or "auto") == "auto":
        tid = "fast"

    company = None
    assumptions = default_assumptions()
    multiples = None
    try:
        from src.multiples import multiples_from_fundamentals
        from src.quant_engine import fetch_fundamentals
        from src.valuation import assumptions_from_fundamentals

        fund = fetch_fundamentals(ticker)
        if not fund.get("error"):
            assumptions = assumptions_from_fundamentals(fund)
            multiples = multiples_from_fundamentals(fund)
            company = fund.get("company_name")
    except Exception as exc:  # noqa: BLE001
        logger.warning("Could not seed valuation assumptions for %s: %s", ticker, exc)

    sections = sections_for_template(tid, ticker, company=company, goal=goal)
    # Income/valuation/memo collaborative plans should use deep execution mode for web/SEC tools
    exec_mode = "fast" if tid == "fast" and mode == "fast" else ("deep" if tid in {"valuation", "deep", "income", "memo"} else mode)
    if tid == "fast":
        exec_mode = "fast"
    elif tid in {"valuation", "deep", "income", "memo"}:
        exec_mode = "deep"

    from src.multiples import default_multiples

    plan = ResearchPlan(
        ticker=ticker,
        goal=default_goal_for_template(tid, goal),
        mode=exec_mode,
        template=tid,
        sections=sections,
        constraints=PlanConstraints(mode=exec_mode),
        planner_mode="template",
        assumptions=assumptions,
        multiples=multiples or default_multiples(),
    )
    plan.summary_markdown = plan_summary_markdown(plan)
    return plan


def _extract_json(text: str) -> dict[str, Any] | None:
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        m = re.search(r"\{[\s\S]*\}", text)
        if not m:
            return None
        try:
            return json.loads(m.group(0))
        except json.JSONDecodeError:
            return None


def _ollama_plan_json(ticker: str, mode: str, goal: str) -> dict[str, Any] | None:
    prompt = PLANNER_PROMPT.format(
        ticker=ticker.upper(),
        mode=mode,
        goal=goal.strip() or "(none — use a solid default equity plan)",
    )
    url = f"{settings.ollama_base_url}/api/generate"
    payload = {
        "model": settings.ollama_model,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": 0.2},
    }
    with httpx.Client(timeout=12.0) as client:
        r = client.post(url, json=payload)
        r.raise_for_status()
        raw = (r.json() or {}).get("response", "")
    return _extract_json(raw)


_ALLOWED = {
    "get_fundamentals",
    "screen_puts",
    "fetch_10k",
    "summarize_item_1a",
    "summarize_item_7",
    "run_dcf",
    "run_ev_ebitda",
    "get_peer_comps",
    "get_earnings",
    "fetch_recent_filings",
    "analyze_drivers",
    "draft_memo_sections",
    "search_web",
}


def _coerce_plan(ticker: str, mode: str, goal: str, data: dict[str, Any]) -> ResearchPlan:
    sections_in = data.get("sections") or []
    sections: list[PlanSection] = []
    for i, raw in enumerate(sections_in):
        if not isinstance(raw, dict):
            continue
        tools = [t for t in (raw.get("tools") or []) if t in _ALLOWED]
        if not tools:
            continue
        sid = str(raw.get("id") or f"section_{i+1}").strip().replace(" ", "_")[:40]
        sections.append(
            PlanSection(
                id=sid,
                title=str(raw.get("title") or sid)[:80],
                enabled=bool(raw.get("enabled", True)),
                tools=tools,
                notes=str(raw.get("notes") or "")[:400],
                queries=[str(q)[:120] for q in (raw.get("queries") or [])[:5]],
            )
        )
    if not sections:
        raise ValueError("empty sections from planner")

    # Deep mode: ensure fetch_10k before summarize tools if those are present
    tool_set = {t for s in sections for t in s.tools}
    if mode != "fast" and ({"summarize_item_1a", "summarize_item_7"} & tool_set) and "fetch_10k" not in tool_set:
        sections.insert(
            0,
            PlanSection(
                id="sec_fetch",
                title="SEC 10-K intake",
                tools=["fetch_10k"],
                notes="Required before filing summaries",
            ),
        )

    plan = ResearchPlan(
        ticker=ticker.upper(),
        goal=str(data.get("goal") or goal or "").strip()
        or "Deep diligence: fundamentals, options, 10-K risks & MD&A",
        mode=mode,
        sections=sections,
        constraints=PlanConstraints(mode=mode),
        planner_mode="ollama",
    )
    plan.summary_markdown = plan_summary_markdown(plan)
    return plan


def generate_plan(
    ticker: str,
    mode: str = "deep",
    goal: str = "",
    template: str = "auto",
) -> ResearchPlan:
    """Build a research plan from a goal-based template (Ollama optional refine)."""
    import os

    mode = "fast" if (mode or "").lower() in {"fast"} else "deep"
    ticker = ticker.upper().strip()
    goal = (goal or "").strip()
    template = (template or "auto").strip().lower() or "auto"

    built = build_template_plan(ticker, mode=mode, goal=goal, template=template)

    # Optional Ollama refine only for generic deep/auto paths
    if os.getenv("OLLAMA_PLANNER", "").strip() not in {"1", "true", "yes"}:
        return built
    if built.template in {"valuation", "income", "memo"}:
        return built
    if not ollama_available():
        return built

    try:
        data = _ollama_plan_json(ticker, built.mode, goal or built.goal)
        if data:
            coerced = _coerce_plan(ticker, built.mode, goal or built.goal, data)
            coerced.template = built.template
            coerced.assumptions = built.assumptions
            return coerced
    except Exception as exc:  # noqa: BLE001
        logger.warning("Ollama planner failed (%s); using template", exc)

    return built

def apply_plan_edits(plan: ResearchPlan, edits: dict[str, Any] | None) -> ResearchPlan:
    """Apply UI edits: goal, enabled flags, notes, valuation assumptions."""
    if not edits:
        return plan
    data = plan.model_dump()
    if "goal" in edits and edits["goal"] is not None:
        data["goal"] = str(edits["goal"]).strip()
    section_edits = edits.get("sections")
    if isinstance(section_edits, list):
        by_id = {s["id"]: s for s in data["sections"]}
        for se in section_edits:
            if not isinstance(se, dict) or "id" not in se:
                continue
            sid = se["id"]
            if sid not in by_id:
                continue
            if "enabled" in se:
                by_id[sid]["enabled"] = bool(se["enabled"])
            if "notes" in se and se["notes"] is not None:
                by_id[sid]["notes"] = str(se["notes"])[:400]
            if "title" in se and se["title"]:
                by_id[sid]["title"] = str(se["title"])[:80]
        data["sections"] = list(by_id.values())

    raw_assump = edits.get("assumptions")
    if isinstance(raw_assump, dict):
        from src.valuation import ValuationAssumptions

        current = data.get("assumptions") or {}
        # Patch nested scenario fields from flat or nested payload
        patched = {**current, **{k: v for k, v in raw_assump.items() if k not in {"base", "bull", "bear"}}}
        for scen in ("base", "bull", "bear"):
            if scen in raw_assump and isinstance(raw_assump[scen], dict):
                patched[scen] = {**(current.get(scen) or {}), **raw_assump[scen]}
        patched["user_edited"] = True
        data["assumptions"] = ValuationAssumptions.model_validate(patched).model_dump()

    raw_mult = edits.get("multiples")
    if isinstance(raw_mult, dict):
        from src.multiples import MultiplesAssumptions

        current_m = data.get("multiples") or {}
        patched_m = {
            **current_m,
            **{k: v for k, v in raw_mult.items() if k not in {"base", "bull", "bear"}},
        }
        for scen in ("base", "bull", "bear"):
            if scen in raw_mult and isinstance(raw_mult[scen], dict):
                patched_m[scen] = {**(current_m.get(scen) or {}), **raw_mult[scen], "label": scen}
        patched_m["user_edited"] = True
        data["multiples"] = MultiplesAssumptions.model_validate(patched_m).model_dump()

    updated = ResearchPlan.model_validate(data)
    updated.summary_markdown = plan_summary_markdown(updated)
    return updated
