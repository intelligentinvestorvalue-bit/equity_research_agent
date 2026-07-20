"""CLI entrypoint: python main.py --ticker TSLA --mode deep"""

from __future__ import annotations

import argparse
import logging
import sys

from src.orchestrator import run_research
from tabulate import tabulate


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Local equity research agent")
    parser.add_argument("--ticker", required=True, help="Ticker symbol, e.g. AAPL")
    parser.add_argument(
        "--mode",
        default="fast",
        choices=["fast", "deep", "comprehensive"],
        help="fast=quant only; deep/comprehensive=plan+tools (SEC+LLM)",
    )
    parser.add_argument("--goal", default="", help="Optional research goal for the planner")
    parser.add_argument(
        "--template",
        default="auto",
        choices=["auto", "valuation", "deep", "income", "fast"],
        help="Plan template (auto infers from goal)",
    )
    parser.add_argument(
        "--legacy",
        action="store_true",
        help="Use linear pipeline instead of plan-driven tools",
    )
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args(argv)

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )

    def progress(stage: str, message: str) -> None:
        print(f"[{stage}] {message}", flush=True)

    def think(kind: str, message: str) -> None:
        print(f"[{kind}] {message}", flush=True)

    result = run_research(
        args.ticker,
        args.mode,
        progress=progress,
        goal=args.goal,
        template=args.template,
        use_plan=not args.legacy,
        think=think,
    )
    fund = (result.get("quant") or {}).get("fundamentals") or {}
    ratios = fund.get("ratios") or {}
    rows = [
        ["Company", fund.get("company_name")],
        ["Price", fund.get("price")],
        ["Revenue", fund.get("revenue")],
        ["FCF", fund.get("free_cash_flow")],
        ["Shares", fund.get("shares_outstanding")],
        ["Rev CAGR", (fund.get("growth") or {}).get("revenue_cagr")],
        ["ROIC", ratios.get("roic")],
        ["FCF yield", ratios.get("fcf_yield")],
        ["D/E", ratios.get("debt_to_equity")],
        ["Evidence", len(result.get("evidence") or [])],
        ["Report", result.get("report_path")],
        ["Financials JSON", result.get("financials_path")],
    ]
    print(tabulate(rows, headers=["Field", "Value"], tablefmt="github"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
