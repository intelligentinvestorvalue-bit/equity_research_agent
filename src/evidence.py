"""Evidence store with citation IDs for planned research reports."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class EvidenceItem:
    id: str  # S1, S2, ...
    source: str
    title: str
    summary: str
    url: str | None = None
    meta: dict[str, Any] = field(default_factory=dict)


class EvidenceStore:
    def __init__(self) -> None:
        self._items: list[EvidenceItem] = []

    def add(
        self,
        source: str,
        title: str,
        summary: str,
        url: str | None = None,
        meta: dict[str, Any] | None = None,
    ) -> EvidenceItem:
        eid = f"S{len(self._items) + 1}"
        item = EvidenceItem(
            id=eid,
            source=source,
            title=title,
            summary=(summary or "")[:2000],
            url=url,
            meta=meta or {},
        )
        self._items.append(item)
        return item

    def items(self) -> list[EvidenceItem]:
        return list(self._items)

    def citations_markdown(self) -> str:
        if not self._items:
            return "_No sources recorded._\n"
        lines = ["## Sources", ""]
        for it in self._items:
            loc = f" — {it.url}" if it.url else ""
            lines.append(f"- **[{it.id}]** {it.title} ({it.source}){loc}")
            if it.summary:
                preview = it.summary.replace("\n", " ")
                if len(preview) > 180:
                    preview = preview[:177] + "…"
                lines.append(f"  - {preview}")
        return "\n".join(lines) + "\n"

    def to_list(self) -> list[dict[str, Any]]:
        return [
            {
                "id": it.id,
                "source": it.source,
                "title": it.title,
                "summary": it.summary,
                "url": it.url,
                "meta": it.meta,
            }
            for it in self._items
        ]
