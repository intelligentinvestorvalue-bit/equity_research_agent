"""Self-critique pass over draft research reports."""

from __future__ import annotations

import logging
import re
from typing import Any

from src.nlp_engine import ollama_available
from src.plan_schema import ResearchPlan
from src.tools import ToolContext

logger = logging.getLogger(__name__)

CRITIQUE_PROMPT = """You are reviewing a local equity research draft. Be skeptical and precise.

Do NOT invent financial figures or price targets that are not already in the draft.
Do NOT change the investment-advice disclaimer.

Return Markdown with exactly these headings:
### Strengths
(2-4 short bullets of what is well supported)

### Issues & gaps
(bullets on unsupported claims, missing sources, fragile assumptions, contradictions)

### Caution for readers
(1-3 bullets on how to interpret this draft)

Draft report:
{chunk}
"""


def _heuristic_issues(plan: ResearchPlan, ctx: ToolContext, draft_md: str) -> list[str]:
    issues: list[str] = []
    draft_l = (draft_md or "").lower()
    fund = ctx.fundamentals or {}
    val = ctx.valuation or {}
    web = ctx.web or {}
    evidence_n = len(ctx.evidence.items())

    if plan.template in {"valuation", "deep"} and evidence_n < 2:
        issues.append("Very few cited sources; conclusions may be under-supported.")

    wants_web = any("search_web" in s.tools for s in plan.enabled_sections())
    if wants_web and (web.get("hit_count") or 0) < 2:
        issues.append("Web research was planned but returned sparse hits; Street/driver context may be incomplete.")

    if any("run_dcf" in s.tools for s in plan.enabled_sections()):
        if not val.get("ok"):
            issues.append("DCF section was planned but valuation did not complete successfully.")
        else:
            base = (val.get("scenarios") or {}).get("base") or {}
            upside = base.get("upside_vs_price")
            share = base.get("share_price")
            if share is not None and share < 0:
                issues.append("Base-case model equity value is negative - treat intrinsic-value output as stress/distress, not a buy signal.")
            if upside is not None and upside > 1.5:
                issues.append("Base-case upside vs spot is extreme (>150%); check growth/margin/WACC assumptions for optimism bias.")
            if upside is not None and upside < -0.7:
                issues.append("Base-case implies deep downside vs spot (<-70%); confirm whether near-term FCF normalization is appropriate for this business.")

    if fund.get("free_cash_flow") is not None and float(fund["free_cash_flow"] or 0) < 0:
        if "normalized" not in draft_l and "negative" not in draft_l:
            issues.append("Company FCF is negative; ensure the report clearly flags normalized-margin DCF assumptions.")

    # Soft ban on strong recommendations without framing
    if re.search(r"\b(strong buy|strong sell|must buy|guaranteed)\b", draft_l):
        issues.append("Draft uses strong recommendation language; this local agent should stay descriptive, not advisory.")

    if "not investment advice" not in draft_l:
        issues.append("Missing investment-advice disclaimer.")

    if ctx.errors:
        issues.append(f"Run recorded {len(ctx.errors)} tool warning(s); see Run warnings before relying on the draft.")

    # Valuation vs spot without noting uncertainty
    if val.get("ok") and "assumption" not in draft_l and "heuristic" not in draft_l:
        issues.append("Valuation results appear without enough emphasis that inputs are editable heuristics.")

    return issues


def _format_heuristic_critique(issues: list[str]) -> str:
    lines = [
        "## Self-critique",
        "",
        "_Automated review (heuristic)._",
        "",
        "### Strengths",
        "- Combines local fundamentals, optional DCF scenarios, and cited sources where available.",
        "- Keeps a non-advisory framing for local research drafts.",
        "",
        "### Issues & gaps",
    ]
    if issues:
        for iss in issues:
            lines.append(f"- {iss}")
    else:
        lines.append("- No major structural issues flagged by heuristics.")
    lines += [
        "",
        "### Caution for readers",
        "- Treat scenario prices as sensitivity output, not a forecast.",
        "- Re-check primary filings and fresh market data before any decision.",
        "",
    ]
    return "\n".join(lines)


def _ollama_critique(draft_md: str) -> str | None:
    if not ollama_available():
        return None
    try:
        import httpx

        from src.config import settings
        from src.nlp_engine import chunk_text

        chunks = chunk_text(draft_md, max_chars=7000, overlap=200)
        material = chunks[0] if chunks else draft_md[:7000]
        if len(chunks) > 1:
            material = material + "\n\n...\n\n" + chunks[-1]
        prompt = CRITIQUE_PROMPT.format(chunk=material[:9000])
        url = f"{settings.ollama_base_url}/api/generate"
        with httpx.Client(timeout=45.0) as client:
            r = client.post(
                url,
                json={
                    "model": settings.ollama_model,
                    "prompt": prompt,
                    "stream": False,
                    "options": {"temperature": 0.2},
                },
            )
            r.raise_for_status()
            body = ((r.json() or {}).get("response") or "").strip()
        if not body:
            return None
        return "## Self-critique\n\n_Automated review (Ollama)._\n\n" + body + "\n"
    except Exception as exc:  # noqa: BLE001
        logger.warning("Ollama critique failed: %s", exc)
        return None


def critique_report(
    draft_md: str,
    plan: ResearchPlan,
    ctx: ToolContext,
    *,
    use_llm: bool = True,
) -> dict[str, Any]:
    """
    Review the draft report and append a self-critique section.
    Does not invent new financial figures into the body.
    """
    issues = _heuristic_issues(plan, ctx, draft_md)
    ollama_md = _ollama_critique(draft_md) if use_llm else None
    if ollama_md:
        critique_md = ollama_md
        if issues:
            critique_md = (
                critique_md.rstrip()
                + "\n\n### Automated checks\n"
                + "\n".join(f"- {i}" for i in issues)
                + "\n"
            )
        mode = "ollama"
    else:
        critique_md = _format_heuristic_critique(issues)
        mode = "heuristic"

    # Ensure single trailing critique; strip a prior Self-critique if re-run
    body = re.sub(r"\n## Self-critique[\s\S]*$", "\n", draft_md).rstrip() + "\n\n" + critique_md
    if not body.endswith("\n"):
        body += "\n"

    return {
        "mode": mode,
        "issues": issues,
        "issue_count": len(issues),
        "critique_markdown": critique_md,
        "final_markdown": body,
    }
