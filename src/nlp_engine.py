"""Local NLP engine via Ollama (Module C), with rule-based fallback."""

from __future__ import annotations

import logging
import re
from typing import Any

import httpx

from src.config import settings

logger = logging.getLogger(__name__)

ANALYSIS_PROMPT = """You are an equity research assistant. Analyze the filing excerpt below.
Focus only on evidence in the text. Do not invent financial figures.

Look for:
1) Shifts in management tone or competitive dynamics
2) Explicit forward guidance (capex, growth, margins)
3) Counterparty, regulatory, or legal risks

Return a concise Markdown summary with short bullet points and 1-2 short quotes.

Excerpt:
{chunk}
"""

BUSINESS_PROMPT = """You are an equity research assistant summarizing 10-K Item 1 (Business).
Use ONLY the excerpt. Do not invent products, segments, or figures not in the text.

Write a thorough Markdown business overview with these ### headings:
### What the company does
### Products, services & segments
### Customers & go-to-market
### Competitive position & industry
### Geography & operations
### Recent strategic focus (if stated)

Aim for 400–800 words total. Prefer concrete details from the filing over generic language.
If a subsection has no evidence, write one short sentence saying it is not covered in the excerpt.

Excerpt:
{chunk}
"""


def chunk_text(text: str, max_chars: int = 6000, overlap: int = 400) -> list[str]:
    if not text:
        return []
    if len(text) <= max_chars:
        return [text]
    chunks: list[str] = []
    start = 0
    while start < len(text):
        end = min(len(text), start + max_chars)
        chunks.append(text[start:end])
        if end >= len(text):
            break
        start = max(0, end - overlap)
    return chunks


def rule_based_summary(text: str, label: str, *, max_sentences: int = 8) -> str:
    """Fallback when Ollama is unreachable: keyword hits + truncated excerpt."""
    if not text:
        return f"### {label}\nNo text available.\n"
    keywords = [
        "risk",
        "uncertainty",
        "litigation",
        "regulation",
        "competition",
        "guidance",
        "capex",
        "revenue",
        "margin",
        "supply chain",
        "cyber",
        "interest rate",
        "customer",
        "segment",
        "product",
        "service",
        "market",
        "operations",
        "network",
        "subsidiary",
    ]
    lower = text.lower()
    hits = [kw for kw in keywords if kw in lower]
    sentences = re.split(r"(?<=[.!?])\s+", text.replace("\n", " "))
    sentences = [s.strip() for s in sentences if len(s.strip()) > 40]
    interesting = [s for s in sentences if any(kw in s.lower() for kw in hits)]
    picked = interesting[:max_sentences] or sentences[:max_sentences]
    bullets = "\n".join(f"- {s}" for s in picked) or "- No keyword highlights found."
    return (
        f"### {label} (rule-based fallback — Ollama unavailable)\n"
        f"**Keyword hits:** {', '.join(hits) if hits else 'none'}\n\n"
        f"{bullets}\n"
    )


def summarize_business(text: str | None, use_llm: bool = True) -> dict[str, Any]:
    """Longer Item 1 Business overview for the memo Business tab."""
    label = "Item 1 — Business"
    if not text:
        return {
            "label": label,
            "mode": "empty",
            "markdown": f"### {label}\nNo Item 1 Business text extracted.\n",
        }

    if not use_llm or not ollama_available():
        return {
            "label": label,
            "mode": "rule_based",
            "markdown": rule_based_summary(text, label, max_sentences=28),
        }

    parts: list[str] = []
    try:
        chunks = chunk_text(text, max_chars=9000, overlap=500)
        for i, chunk in enumerate(chunks[:6], start=1):
            prompt = BUSINESS_PROMPT.format(chunk=chunk)
            parts.append(_generate(prompt) or f"(empty model response for chunk {i})")
        if len(parts) == 1:
            md = parts[0]
        else:
            combined = "\n\n".join(f"#### Part {i}\n{p}" for i, p in enumerate(parts, start=1))
            reduce_prompt = (
                "Merge these partial 10-K Item 1 Business summaries into one cohesive Markdown "
                "business overview for an equity research memo. Use these headings:\n"
                "### What the company does\n"
                "### Products, services & segments\n"
                "### Customers & go-to-market\n"
                "### Competitive position & industry\n"
                "### Geography & operations\n"
                "### Recent strategic focus (if stated)\n\n"
                "Deduplicate, keep concrete filing details, aim for 500–900 words.\n\n"
                + combined
            )
            md = _generate(reduce_prompt) or combined
        return {"label": label, "mode": "ollama", "markdown": md, "model": settings.ollama_model}
    except Exception as exc:  # noqa: BLE001
        logger.warning("Ollama business summarize failed: %s", exc)
        return {
            "label": label,
            "mode": "rule_based",
            "error": str(exc),
            "markdown": rule_based_summary(text, label, max_sentences=28),
        }


def ollama_available() -> bool:
    try:
        with httpx.Client(timeout=3.0) as client:
            r = client.get(f"{settings.ollama_base_url}/api/tags")
            return r.status_code == 200
    except Exception:  # noqa: BLE001
        return False


def _generate(prompt: str) -> str:
    url = f"{settings.ollama_base_url}/api/generate"
    payload = {
        "model": settings.ollama_model,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": 0.2},
    }
    with httpx.Client(timeout=180.0) as client:
        r = client.post(url, json=payload)
        r.raise_for_status()
        data = r.json()
        return data.get("response", "").strip()


def summarize_section(text: str | None, label: str, use_llm: bool = True) -> dict[str, Any]:
    return summarize_text(text, label, prompt_template=ANALYSIS_PROMPT, use_llm=use_llm)


def summarize_text(
    text: str | None,
    label: str,
    prompt_template: str = ANALYSIS_PROMPT,
    use_llm: bool = True,
) -> dict[str, Any]:
    if not text:
        return {"label": label, "mode": "empty", "markdown": f"### {label}\nNo text extracted.\n"}

    if not use_llm or not ollama_available():
        return {"label": label, "mode": "rule_based", "markdown": rule_based_summary(text, label)}

    parts: list[str] = []
    try:
        for i, chunk in enumerate(chunk_text(text), start=1):
            prompt = prompt_template.format(chunk=chunk)
            parts.append(_generate(prompt) or f"(empty model response for chunk {i})")
        if len(parts) == 1:
            md = f"### {label}\n{parts[0]}\n"
        else:
            combined = "\n\n".join(f"#### Chunk {i}\n{p}" for i, p in enumerate(parts, start=1))
            reduce_prompt = (
                "Combine these chunk summaries into one concise Markdown section. "
                "Deduplicate and keep only evidence-backed points.\n\n" + combined
            )
            md = f"### {label}\n{_generate(reduce_prompt)}\n"
        return {"label": label, "mode": "ollama", "markdown": md, "model": settings.ollama_model}
    except Exception as exc:  # noqa: BLE001
        logger.warning("Ollama summarize failed: %s", exc)
        return {
            "label": label,
            "mode": "rule_based",
            "error": str(exc),
            "markdown": rule_based_summary(text, label),
        }


def run_nlp(sections: dict[str, Any]) -> dict[str, Any]:
    business = summarize_business(sections.get("item_1"))
    item_1a = summarize_section(sections.get("item_1a"), "Item 1A — Risk Factors")
    item_7 = summarize_section(sections.get("item_7"), "Item 7 — MD&A")
    report = "\n".join([business["markdown"], item_1a["markdown"], item_7["markdown"]])
    return {
        "ticker": sections.get("ticker"),
        "ollama_up": ollama_available(),
        "business": business,
        "item_1a": item_1a,
        "item_7": item_7,
        "markdown": report,
    }
