"""Iterative think → act → gap-fill loop after the planned tool pass."""

from __future__ import annotations

import json
import logging
import re
from typing import Any, Callable

from src.nlp_engine import ollama_available
from src.plan_schema import ResearchPlan
from src.thinking import ThinkCb, _noop_think
from src.tools import TOOL_REGISTRY, ToolContext

logger = logging.getLogger(__name__)

ProgressCb = Callable[[str, str], None]

LOOP_PROMPT = """You are controlling a local equity research agent.
Given the research state JSON, decide if more work is needed.

Return ONLY JSON:
{{
  "thought": "what you learned and what is still missing",
  "done": true/false,
  "actions": [
    {{"tool": "search_web", "queries": ["query1", "query2"], "reason": "why"}}
  ]
}}

Allowed tools: search_web, get_fundamentals, run_dcf, fetch_10k, screen_puts
Max 2 actions. Prefer search_web for missing analyst targets or drivers.
If coverage is adequate, set done=true and actions=[].

State:
{state}
"""


def _state_snapshot(plan: ResearchPlan, ctx: ToolContext) -> dict[str, Any]:
    fund = ctx.fundamentals or {}
    val = ctx.valuation or {}
    web = ctx.web or {}
    base = ((val.get("scenarios") or {}).get("base") or {}) if val else {}
    return {
        "ticker": plan.ticker,
        "template": plan.template,
        "goal": plan.goal,
        "has_fundamentals": bool(fund) and not fund.get("error"),
        "revenue": fund.get("revenue"),
        "fcf": fund.get("free_cash_flow"),
        "valuation_ok": bool(val.get("ok")),
        "base_share_price": base.get("share_price"),
        "web_hits": web.get("hit_count") or 0,
        "web_fetched": web.get("fetched_ok") or 0,
        "web_queries": (web.get("queries") or [])[:6],
        "sec_ok": bool((ctx.sections or {}).get("extraction_ok")) if ctx.sections else None,
        "evidence_count": len(ctx.evidence.items()),
        "errors": (ctx.errors or [])[:5],
    }


def _heuristic_decision(plan: ResearchPlan, ctx: ToolContext, step: int) -> dict[str, Any]:
    """Rule-based gap fill when Ollama is unavailable."""
    snap = _state_snapshot(plan, ctx)
    actions: list[dict[str, Any]] = []
    thoughts: list[str] = []

    wants_web = any("search_web" in s.tools for s in plan.enabled_sections())
    hits = int(snap.get("web_hits") or 0)

    if wants_web and hits < 2 and step == 0:
        thoughts.append(f"Only {hits} web hits so far; broadening news/analyst search.")
        actions.append(
            {
                "tool": "search_web",
                "queries": [
                    f"{plan.ticker} analyst price target",
                    f"{plan.ticker} stock news",
                ],
                "reason": "sparse web coverage",
            }
        )

    if plan.template == "valuation" and hits >= 1 and step == 0:
        # Check whether analyst-ish language appeared
        blob = " ".join(
            f"{h.get('title','')} {h.get('snippet','')}" for h in (ctx.web or {}).get("hits") or []
        ).lower()
        if "target" not in blob and "analyst" not in blob and "rating" not in blob:
            thoughts.append("Web hits lack clear analyst target language; searching specifically.")
            actions.append(
                {
                    "tool": "search_web",
                    "queries": [
                        f"{plan.ticker} consensus price target",
                        f"{plan.ticker} buy sell hold rating",
                    ],
                    "reason": "missing Street targets",
                }
            )

    if plan.template == "valuation" and step <= 1:
        blob = " ".join(
            f"{h.get('title','')} {h.get('snippet','')}" for h in (ctx.web or {}).get("hits") or []
        ).lower()
        driver_kw = ("uranium", "rare earth", "vanadium", "commodity", "lithium", "copper")
        goal_l = (plan.goal or "").lower()
        if any(k in goal_l for k in driver_kw) and not any(k in blob for k in driver_kw):
            thoughts.append("Goal mentions commodity drivers but web hits do not; searching drivers.")
            actions.append(
                {
                    "tool": "search_web",
                    "queries": [f"{plan.ticker} {plan.goal}", f"{plan.ticker} market drivers"],
                    "reason": "missing drivers from goal",
                }
            )

    if snap.get("has_fundamentals") and not snap.get("valuation_ok"):
        if any("run_dcf" in s.tools for s in plan.enabled_sections()):
            thoughts.append("Fundamentals present but DCF missing/failed; retrying valuation.")
            actions.append({"tool": "run_dcf", "queries": [], "reason": "DCF incomplete"})

    # de-dupe tools (keep first)
    seen: set[str] = set()
    uniq: list[dict[str, Any]] = []
    for a in actions:
        key = a.get("tool", "") + "|" + "|".join(a.get("queries") or [])
        if key in seen:
            continue
        seen.add(key)
        uniq.append(a)
    actions = uniq[:2]

    if not actions:
        thoughts.append("Coverage looks adequate for this pass; stopping iterative loop.")
        return {"thought": " ".join(thoughts), "done": True, "actions": [], "mode": "heuristic"}

    return {
        "thought": " ".join(thoughts) or "Identified follow-up research gaps.",
        "done": False,
        "actions": actions,
        "mode": "heuristic",
    }


def _ollama_decision(plan: ResearchPlan, ctx: ToolContext) -> dict[str, Any] | None:
    if not ollama_available():
        return None
    try:
        import httpx

        from src.config import settings

        state = json.dumps(_state_snapshot(plan, ctx), default=str)
        prompt = LOOP_PROMPT.format(state=state)
        url = f"{settings.ollama_base_url}/api/generate"
        with httpx.Client(timeout=20.0) as client:
            r = client.post(
                url,
                json={
                    "model": settings.ollama_model,
                    "prompt": prompt,
                    "stream": False,
                    "options": {"temperature": 0.1},
                },
            )
            r.raise_for_status()
            raw = (r.json() or {}).get("response", "")
        text = raw.strip()
        if text.startswith("```"):
            text = re.sub(r"^```(?:json)?\s*", "", text)
            text = re.sub(r"\s*```$", "", text)
        data = json.loads(text) if text.startswith("{") else None
        if not data:
            m = re.search(r"\{[\s\S]*\}", text)
            data = json.loads(m.group(0)) if m else None
        if not isinstance(data, dict):
            return None
        actions = []
        for a in (data.get("actions") or [])[:2]:
            if not isinstance(a, dict):
                continue
            tool = a.get("tool")
            if tool not in TOOL_REGISTRY:
                continue
            actions.append(
                {
                    "tool": tool,
                    "queries": [str(q)[:120] for q in (a.get("queries") or [])[:4]],
                    "reason": str(a.get("reason") or "")[:200],
                }
            )
        return {
            "thought": str(data.get("thought") or "Model suggested follow-ups.")[:500],
            "done": bool(data.get("done")) and not actions,
            "actions": actions,
            "mode": "ollama",
        }
    except Exception as exc:  # noqa: BLE001
        logger.warning("Ollama loop decision failed: %s", exc)
        return None


def _execute_action(ctx: ToolContext, action: dict[str, Any], think: ThinkCb) -> None:
    tool = action.get("tool")
    fn = TOOL_REGISTRY.get(tool or "")
    if not fn:
        ctx.errors.append(f"loop unknown tool: {tool}")
        return
    reason = action.get("reason") or ""
    think("act", f"Follow-up `{tool}` — {reason or 'gap fill'}")
    if tool == "search_web":
        ctx.active_section_id = "loop_followup"
        ctx.active_section_queries = list(action.get("queries") or [])
    try:
        fn(ctx)
    except Exception as exc:  # noqa: BLE001
        logger.exception("Loop action %s failed", tool)
        ctx.errors.append(f"loop:{tool}: {exc}")
        think("gap", f"Follow-up `{tool}` failed: {exc}")
    finally:
        ctx.active_section_id = None
        ctx.active_section_queries = []


def run_research_loop(
    plan: ResearchPlan,
    ctx: ToolContext,
    *,
    progress: ProgressCb | None = None,
    think: ThinkCb | None = None,
    max_steps: int | None = None,
) -> dict[str, Any]:
    """
    After the planned sections run, iteratively assess gaps and take follow-up actions.
    """
    progress = progress or (lambda s, m: None)
    think = think or _noop_think
    # More room for valuation/deep; fast stays lean
    if max_steps is None:
        max_steps = 3 if plan.template in {"valuation", "deep"} else (2 if plan.template == "income" else 1)

    steps_log: list[dict[str, Any]] = []
    think("think", f"Starting iterative review for template `{plan.template}` (max {max_steps} follow-ups).")
    progress("think", "Assessing research gaps")

    for step in range(max_steps):
        decision = _ollama_decision(plan, ctx) or _heuristic_decision(plan, ctx, step)
        think("think", decision.get("thought") or f"Loop step {step + 1}")
        steps_log.append(decision)

        if decision.get("done") or not decision.get("actions"):
            think("done", "No further follow-ups required.")
            break

        progress("think", f"Follow-up step {step + 1}/{max_steps}")
        for action in decision.get("actions") or []:
            _execute_action(ctx, action, think)

    else:
        think("done", "Reached max iterative steps.")

    return {"steps": steps_log, "max_steps": max_steps}
