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
    default_deep_sections,
    default_fast_sections,
    plan_summary_markdown,
)

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

Rules:
- For mode "fast": only get_fundamentals and screen_puts (2 sections).
- For mode "deep": include fetch_10k before summarize_item_1a / summarize_item_7.
- Keep 2–6 sections. Prefer concrete notes tied to the user goal.
"""


def build_template_plan(ticker: str, mode: str = "deep", goal: str = "") -> ResearchPlan:
    ticker = ticker.upper().strip()
    mode = "fast" if mode == "fast" else "deep"
    sections = default_fast_sections() if mode == "fast" else default_deep_sections()
    if goal.strip():
        # Attach goal hint to first qualitative-ish section
        for sec in sections:
            if sec.id in {"risks", "mda", "fundamentals"}:
                sec.notes = f"{sec.notes}. Focus: {goal.strip()}"
                break
    plan = ResearchPlan(
        ticker=ticker,
        goal=goal.strip() or ("Quick fundamentals + put screen" if mode == "fast" else "Deep diligence: fundamentals, options, 10-K risks & MD&A"),
        mode=mode,
        sections=sections,
        constraints=PlanConstraints(mode=mode),
        planner_mode="template",
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


def generate_plan(ticker: str, mode: str = "deep", goal: str = "") -> ResearchPlan:
    """Build a research plan.

    Uses a deterministic template by default so the approve UI is instant.
    Set OLLAMA_PLANNER=1 to let Llama refine the section list when responsive.
    """
    import os

    mode = "fast" if (mode or "").lower() in {"fast"} else "deep"
    ticker = ticker.upper().strip()
    goal = (goal or "").strip()

    if mode == "fast":
        return build_template_plan(ticker, mode="fast", goal=goal)

    template = build_template_plan(ticker, mode="deep", goal=goal)
    if os.getenv("OLLAMA_PLANNER", "").strip() not in {"1", "true", "yes"}:
        return template

    if not ollama_available():
        return template

    try:
        data = _ollama_plan_json(ticker, mode, goal)
        if data:
            return _coerce_plan(ticker, mode, goal, data)
    except Exception as exc:  # noqa: BLE001
        logger.warning("Ollama planner failed (%s); using template", exc)

    return template


def apply_plan_edits(plan: ResearchPlan, edits: dict[str, Any] | None) -> ResearchPlan:
    """Apply UI edits: goal, enabled flags, notes by section id."""
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
    updated = ResearchPlan.model_validate(data)
    updated.summary_markdown = plan_summary_markdown(updated)
    return updated
