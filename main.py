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
        help="fast=quant only; deep/comprehensive=quant+SEC+LLM",
    )
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args(argv)

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )

    def progress(stage: str, message: str) -> None:
        print(f"[{stage}] {message}", flush=True)

    result = run_research(args.ticker, args.mode, progress=progress)
    fund = (result.get("quant") or {}).get("fundamentals") or {}
    ratios = fund.get("ratios") or {}
    rows = [
        ["Company", fund.get("company_name")],
        ["Price", fund.get("price")],
        ["ROIC", ratios.get("roic")],
        ["FCF yield", ratios.get("fcf_yield")],
        ["D/E", ratios.get("debt_to_equity")],
        ["Report", result.get("report_path")],
        ["Financials JSON", result.get("financials_path")],
    ]
    print(tabulate(rows, headers=["Field", "Value"], tablefmt="github"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
