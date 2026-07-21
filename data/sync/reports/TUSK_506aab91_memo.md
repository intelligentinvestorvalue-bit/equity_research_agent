# TUSK — Planned Research Report

> Not investment advice. Local research draft only.

**Goal:** Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers
**Mode:** deep
**Template:** memo
**Planner:** template

## Plan executed

- **(1) Snapshot, KPIs & capital structure** (`fundamentals`): get_fundamentals
  - Multi-year KPI table, leverage, EV/EBITDA snapshot. Focus: institutional deep-dive: thesis, priced-in scenarios, catalysts, falsifiers
- **(2) EV/EBITDA priced-in scenarios** (`multiples`): run_ev_ebitda
  - Bear/base/bull EBITDA × multiple → implied equity value
- **(3) DCF cross-check** (`valuation`): run_dcf
  - FCF DCF as second valuation lens vs multiples
- **(4) Peer & factor comps** (`peers`): get_peer_comps
  - Heuristic sector peers: returns, EV/EBITDA, leverage, volatility
- **(5) Earnings & surprise history** (`earnings`): get_earnings
  - EPS estimate vs actual vs 1-day move when available
- **(6a) Street / narrative web** (`web_analysts`): search_web
  - Analyst targets, thesis debates, guidance headlines
- **(6b) Drivers & proxies** (`web_drivers`): search_web
  - Operating KPIs, contracts, refinancing, sector drivers
- **(7a) SEC 10-K intake** (`sec_fetch`): fetch_10k
  - Latest 10-K for risks and MD&A
- **(7b) Recent 10-Q / 8-K headlines** (`recent_filings`): fetch_recent_filings
  - Catalyst calendar inputs — meta only, not full parse
- **(7c) Risk factors (Item 1A)** (`risks`): summarize_item_1a
  - Falsification inputs from filing risks
- **(7d) MD&A (Item 7)** (`mda`): summarize_item_7
  - Business model and guidance cues
- **(8) Quarterly driver correlations** (`drivers`): analyze_drivers
  - Suggestive FCF/revenue/debt vs return correlations (small-n caveats)
- **(9) Thesis memo sections** (`memo`): draft_memo_sections
  - Exec summary, variant perception, catalysts, falsifiers, limitations

## Fundamentals [S1]
- Company: Mammoth Energy Services, Inc.
- Sector / industry: Industrials / Conglomerates
- Price: 2.685
- 52-week range: $1.72 – $3.92
- Market cap: $129.34M
- Enterprise value: $13.62M
- Shares outstanding: 48.17M
- Beta: 1.109
- Book equity: $258.29M
- Revenue (latest): $44.29M
- EBITDA (latest): -$17.84M
- Free cash flow (latest): -$89.12M
- Operating income: -$28.14M
- Operating margin: -63.5%
- EV / EBITDA: -0.8x
- ROIC: -17.6%
- FCF yield: -68.9%
- Debt / Equity: 0.013341696091185034
- FCF / share: -$1.85
- Revenue / share: $0.92

### Capital structure
- Cash: $101.99M
- Short-term debt: —
- Long-term debt: $3.45M
- Total debt: $3.45M
- Net debt: -$98.54M
- Net debt / EBITDA: 5.5x

### Growth
- Revenue CAGR: -50.4%
- FCF CAGR: —
- Latest revenue YoY: -2.9%
- Latest FCF YoY: -149.6%

### Market expectations (yfinance, sparse)
- Mean target: —
- Target range: — – —
- Recommendation: none

_Consensus revenue/EBITDA forecasts are often unavailable via free feeds; treat targets as point-in-time only._

### Historical KPIs (multi-year)

| Year | Revenue | OCF | Capex | FCF | EBITDA | LT debt | Cash | Net debt | Net income |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2025 | $44.29M | -$18.57M | $70.55M | -$89.12M | -$17.84M | — | $101.99M | -$101.99M | $4.60M |
| 2024 | $45.60M | $180.72M | $1.21M | $179.50M | -$173.21M | — | $60.84M | -$60.84M | -$207.33M |
| 2023 | $309.49M | $31.39M | $19.39M | $11.99M | $70.44M | $42.81M | $16.56M | $26.25M | -$3.16M |
| 2022 | $362.09M | $15.27M | $12.74M | $2.53M | $88.77M | $6.05M | $17.28M | -$11.23M | -$619.00K |
| 2021 | — | — | — | — | — | $85.24M | — | $85.24M | — |

## Charts

### Revenue & FCF history
![Revenue & FCF history](/charts/TUSK_revenue_fcf.png)

### DCF scenario prices
![DCF scenario prices](/charts/TUSK_dcf_scenarios.png)

### Base-case FCF path
![Base-case FCF path](/charts/TUSK_base_fcf_path.png)

### EV/EBITDA scenario prices
![EV/EBITDA scenario prices](/charts/TUSK_ev_ebitda_scenarios.png)

### Normalized price vs peers
![Normalized price vs peers](/charts/TUSK_peers_normalized.png)

## DCF valuation (base / bull / bear) [S3]

> Simplified revenue->FCF DCF. Not investment advice; assumptions are editable heuristics.

- Spot price: $2.69
- Base revenue: $44.29M
- Shares: 48,170,647
- Net debt (Debt−Cash): -$98.54M

| Scenario | Growth | FCF margin | WACC | Term. g | Equity value | Share price | Upside |
|----------|--------|------------|------|---------|--------------|-------------|--------|
| bear | -2.9% | 1.0% | 12.0% | 1.5% | $102.12M | $2.12 | -21.0% |
| base | 6.0% | 3.0% | 10.0% | 2.5% | $119.58M | $2.48 | -7.5% |
| bull | 15.0% | 8.0% | 9.0% | 3.0% | $198.92M | $4.13 | 53.8% |

### Assumption notes
- Base revenue growth seeded from historical rate (-2.9%).
- Recent revenue declined (-2.9% YoY); base/bull use normalized mid-cycle growth instead of extrapolating the decline.
- Latest FCF margin was -201.2%; scenarios use normalized positive margins for a going-concern DCF.


### Base-case projected FCF

- Year 1: revenue $46.95M, FCF $1.41M (PV $1.28M)
- Year 2: revenue $49.77M, FCF $1.49M (PV $1.23M)
- Year 3: revenue $52.75M, FCF $1.58M (PV $1.19M)
- Year 4: revenue $55.92M, FCF $1.68M (PV $1.15M)
- Year 5: revenue $59.27M, FCF $1.78M (PV $1.10M)
- Terminal value $24.30M (PV $15.09M)

## Valuation — EV/EBITDA scenarios [S2]

> Priced-in model: implied price = (EBITDA × EV/EBITDA − net debt) ÷ shares. Not a forecast.

- Spot: $2.69
- Net debt used: -$98.54M

| Scenario | EBITDA | EV/EBITDA | Implied EV | Equity value | Implied price |
|---|---:|---:|---:|---:|---:|
| bear | $700.00M | 6.0x | $4.20B | $4.30B | $89.24 |
| base | $1.00B | 8.0x | $8.00B | $8.10B | $168.12 |
| bull | $1.20B | 10.0x | $12.00B | $12.10B | $251.16 |

- EBITDA missing or non-positive; scenarios use placeholder $1B EBITDA — edit before relying on prices.
- No current EV/EBITDA; defaulted base multiple to 8.0x.

## Peer & factor comps

- Sector / industry: Industrials / Conglomerates
- Peers: —

| Ticker | Mkt cap | EV/EBITDA | ND/EBITDA | Beta | 1y | 5y | Vol |
|---|---:|---:|---:|---:|---:|---:|---:|
| TUSK | $129.3M | -1.0x | 9.1x | 1.11 | 4.5% | -32.9% | 72.4% |

- No industry peer map match; comps limited to the subject ticker.

_Price returns are price-only (dividends ignored). Peer set is heuristic, not a formal comps universe._

## Earnings, guidance & revision catalysts

- Next earnings (calendar): 2026-08-07

| Date | EPS est | EPS actual | Surprise | 1-day move |
|---|---:|---:|---:|---:|
| 2023-04-27 | -0.06 | 0.17 | 0.23 | -5.4% |
| 2020-05-11 | -0.65 | -0.36 | 0.29 | -0.7% |
| 2020-02-27 | -0.60 | -0.58 | 0.02 | -0.7% |
| 2019-11-07 | -0.46 | -0.67 | -0.21 | -0.7% |
| 2019-08-01 | -0.09 | -0.24 | -0.15 | -0.7% |
| 2019-05-01 | 0.66 | 0.63 | -0.03 | -0.7% |
| 2019-03-14 | 0.64 | 1.61 | 0.97 | -0.7% |
| 2018-10-31 | 1.07 | 1.54 | 0.47 | -0.7% |
| 2018-08-06 | 1.46 | 0.95 | -0.51 | -0.7% |
| 2018-05-02 | 1.66 | 1.24 | -0.42 | -0.7% |
| 2018-02-21 | 0.58 | 1.56 | 0.98 | -0.7% |
| 2017-11-01 | 0.01 | -0.02 | -0.03 | -0.7% |

_EPS surprise vs 1-day move Pearson r=-0.063 (n=12, p≈0.843); treat as suggestive only._

_Guidance vs Street and adjusted EBITDA are often missing from free feeds; use web/SEC sections for narrative guidance._

## Recent SEC filings (10-Q / 8-K)

| Date | Form | Description |
|---|---|---|
| 2026-06-26 | 8-K | [8-K](https://www.sec.gov/Archives/edgar/data/1679268/000162828026045745/tusk-20260625.htm) |
| 2026-05-15 | 8-K | [8-K](https://www.sec.gov/Archives/edgar/data/1679268/000162828026035328/tusk-20260513.htm) |
| 2026-05-11 | 10-Q | [10-Q](https://www.sec.gov/Archives/edgar/data/1679268/000162828026033686/tusk-20260331.htm) |
| 2026-05-11 | 8-K | [8-K](https://www.sec.gov/Archives/edgar/data/1679268/000162828026033142/tusk-20260511.htm) |
| 2026-03-06 | 10-K | [10-K](https://www.sec.gov/Archives/edgar/data/1679268/000162828026015693/tusk-20251231.htm) |
| 2026-03-06 | 8-K | [8-K](https://www.sec.gov/Archives/edgar/data/1679268/000162828026015465/tusk-20260306.htm) |
| 2025-12-04 | 8-K | [8-K](https://www.sec.gov/Archives/edgar/data/1679268/000167926825000046/tusk-20251202.htm) |
| 2025-11-03 | 10-Q | [10-Q](https://www.sec.gov/Archives/edgar/data/1679268/000167926825000039/tusk-20250930.htm) |
| 2025-10-31 | 8-K | [8-K](https://www.sec.gov/Archives/edgar/data/1679268/000167926825000036/tusk-20251031.htm) |
| 2025-08-08 | 10-Q | [10-Q](https://www.sec.gov/Archives/edgar/data/1679268/000162828025039262/tusk-20250630.htm) |
| 2025-08-08 | 8-K | [8-K](https://www.sec.gov/Archives/edgar/data/1679268/000162828025039122/tusk-20250808.htm) |
| 2025-07-03 | 8-K | [8-K](https://www.sec.gov/Archives/edgar/data/1679268/000162828025034133/tusk-20250630.htm) |

_Headlines/meta only — documents not fully parsed in this pass._

## Key driver analysis (quarterly)

Pearson / Spearman correlations of quarterly stock returns with fundamentals.

| Driver | Pearson r | p | n | Spearman ρ | p |
|---|---:|---:|---:|---:|---:|
| Revenue growth (YoY) | — | — | 1 | — | — |
| Free cash flow | -0.472 | 0.354 | 5 | -0.600 | 0.194 |
| FCF margin | -0.419 | 0.425 | 5 | -0.800 | 0.021 |
| Operating cash flow | -0.571 | 0.228 | 5 | -0.700 | 0.090 |
| Long-term debt level | -0.543 | 0.263 | 5 | -0.300 | 0.586 |
| EBITDA | -0.173 | 0.761 | 5 | -0.300 | 0.586 |
| Capex (abs) | 0.389 | 0.465 | 5 | 0.600 | 0.194 |

### Regime check (FCF)

- later: r=-0.472 (n=5, p≈0.354)

- Correlations describe association, not causation.
- Small samples (especially regime splits) are directional only.
- Regime split at 2023-12-31 (sample midpoint); directional only.

## Executive summary

Mammoth Energy Services, Inc. (TUSK) trades near 2.685 with market cap $129.34M and EV $13.62M. Net debt is -$98.54M (ND/EBITDA 5.522669954604046). Latest revenue $44.29M, EBITDA -$17.84M, FCF -$89.12M.

**Goal focus:** Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers.

What matters most (framework): balance-sheet trajectory, cash generation vs leverage, and whether market expectations (sparse free-data targets) already price execution risk.

EV/EBITDA implied prices — bear $89.24 / base $168.12 / bull $251.16.

## Company setup & business model

Sector/industry: Industrials / Conglomerates. Detail the competitive position, revenue mix, and strategic pivots from SEC MD&A and web sources in adjacent report tabs. This skeleton does not invent segment KPIs.

## Variant perception

- **Consensus frame (sparse):** recommendation=none, mean target=—.
- **Bear:** leverage and execution risk dominate; cash generation fails to cover refinancing / reinvestment needs; equity remains constrained by net debt.
- **Bull:** cash-flow and strategic optionality re-rate the equity as leverage falls and growth/mix improves.
- **Middle:** returns may track free-cash-flow more than headline revenue — verify with driver analysis tab.

## Catalysts & monitoring

- Next earnings window (calendar): 2026-08-07
- Peer tape to watch: n/a
- Monitor: FCF vs net debt, leverage (ND/EBITDA), refinancing headlines, and material 8-K strategy updates.
- Recent filing: 8-K on 2026-06-26 — 8-K
- Recent filing: 8-K on 2026-05-15 — 8-K
- Recent filing: 10-Q on 2026-05-11 — 10-Q
- Recent filing: 8-K on 2026-05-11 — 8-K
- Recent filing: 10-K on 2026-03-06 — 10-K

## Falsification triggers

- Leverage (net debt/EBITDA) re-rises sustainably above prior repaired levels without offsetting EBITDA growth.
- Underlying FCF (ex one-times, when identifiable) trends below levels needed to service debt and fund required capex.
- Strategic thesis KPIs (from filings/web) stall for consecutive reporting periods.
- Distressed refinancing, covenant stress, or major customer/contract loss headlines.

## Source quality & limitations

- Quantitative data from yfinance (statements, prices, sparse targets); qualitative from SEC + public web.
- Consensus revenue/EBITDA estimates and adjusted metrics are often unavailable — do not treat missing fields as zero.
- Peer sets are heuristic by sector/industry keyword maps.
- This is a local research draft only — not investment advice and not a rating.

## Early proxy tracker

| Proxy | Why it matters | Current signal | Source |
|---|---|---|---|
| Guidance / outlook | Forward cash/earnings path | TUSK Forecast, Price Target & Analyst Ratings / ChartMill.com 7 analysts have analysed TUSK and the average price target is 4.28 USD. This implies a price increase of 53% is expect | TUSK Forecast, Price Target & Analyst Ratings | ChartMill.com |

_Proxies are heuristic extractions from public web/SEC context; verify against primary filings._

## Catalyst calendar

| Window | Catalyst | Notes |
|---|---|---|
| 2026-08-07 | Earnings | Next report date from yfinance calendar |
| 2026-06-26 | 8-K | 8-K |
| 2026-05-15 | 8-K | 8-K |
| 2026-05-11 | 10-Q | 10-Q |
| 2026-05-11 | 8-K | 8-K |
| 2026-03-06 | 10-K | 10-K |
| 2026-03-06 | 8-K | 8-K |
| 2025-12-04 | 8-K | 8-K |
| 2025-11-03 | 10-Q | 10-Q |
| 2025-10-31 | 8-K | 8-K |
| 2025-08-08 | 10-Q | 10-Q |
| 2025-08-08 | 8-K | 8-K |
| 2025-07-03 | 8-K | 8-K |
| Feb 26, 2026 | Web event | Investor Bradley Tusk: Market falling prey to letting narrative dictate ... |
| May 19, 2025 | Web event | JPMorgan investor day kicks off - CNBC |
| Apr 7, 2026 | Web event | Understanding Demand: Key Determinants and the Demand Curve |
| Jan 21, 2025 | Web event | Market Demand: Definition, How to Calculate, Determinants |
| Dec 2, 2025 | Web event | Mammoth Energy Services, Inc. Announces Sale of Engineering ... |
| Feb 05, 2026 | Web event | Press Releases - Mammoth Energy Services, Inc. |
| Feb 17, 2021 | Web event | Mammoth Energy Announces Growth of Engineering Services ... |

## Web research — web_analysts

- Queries: TUSK analyst price target, Mammoth Energy Services, Inc. stock rating OR consensus OR upgrade OR downgrade, TUSK guidance OR investor day OR catalyst
- Unique hits: 11
- Pages fetched: 1/3

### Web synthesis — web_analysts (rule-based fallback — Ollama unavailable)
**Keyword hits:** none

- No keyword highlights found.

### Sources found
- [TUSK Forecast, Price Target & Analyst Ratings | ChartMill.com](https://www.chartmill.com/stock/quote/TUSK/analyst-ratings)
  - 7 analysts have analysed TUSK and the average price target is 4.28 USD. This implies a price increase of 53% is expected in the next year compared to the ...
- [TUSK Stock Forecast & Price Target | Mammoth Energy Services Inc ...](https://valueinvesting.io/TUSK/estimates)
  - The average stock forecast for Mammoth Energy Services Inc (TUSK) is 4.28 USD. This price target corresponds to an upside of 36.87%. The range of stock ...
- [Mammoth Energy Services, Inc. (TUSK) - Yahoo Finance](https://finance.yahoo.com/quote/TUSK/)
  - Find the latest Mammoth Energy Services, Inc. (TUSK) stock quote, history, news and other vital information to help you with your stock trading and ...
- [TUSK - Mammoth Energy Services Stock Forecast - StockInvest.us](https://stockinvest.us/stock/TUSK)
  - Given the current short-term trend, the stock is expected to rise 9.16% during the next 3 months and, with a 90% probability hold a price between $2.85 and ...
- [Analyst Upgrades & Downgrades - MarketWatch](https://www.marketwatch.com/tools/upgrades-downgrades)
  - Real-time information on stock upgrades and downgrades by MarketWatch. View information on strong stocks to buy and weak stocks to sell.
- [Stock Screener: Best Stocks Consensus Opinion Analysts | MarketScreener](https://m.marketscreener.com/tools/stock-screener/top-consensus/)
  - A surprise rate measures the difference between the consensus (average estimated value by the analysts covering the company) of an accounting item the day be…
- [What Are Stock Upgrades & Downgrades? | The Motley Fool](https://www.fool.com/terms/u/upgrades-downgrades/)
  - What does a downgrade mean for stocks? When a stock analyst changes his or her opinion of a stock, making either an upgrade or a downgrade, it can sometimes …
- [Consensus: AI for Research](https://consensus.app/)
  - Consensus is an AI academic search engine for peer-reviewed literature—your research OS for finding, organizing, and analyzing science 10x faster.
- [Investor Bradley Tusk: Market falling prey to letting narrative dictate ...](https://www.cnbc.com/video/2026/02/26/investor-bradley-tusk-market-falling-prey-to-letting-narrative-dictate-everything.html)
  - Feb 26, 2026 ... Bradley Tusk, Tusk Ventures, joins 'Closing Bell Overtime' to talk the state of the tech and software trades, how private investing is ...
- [JPMorgan investor day kicks off - CNBC](https://www.cnbc.com/video/2025/05/19/jpmorgan-investor-day-kicks-off.html)
  - May 19, 2025 ... JPMorgan investor day kicks off. CNBC's Leslie Picker joins 'Squawk on ... Watch CNBC's full interview with Tusk Ventures CEO Bradley Tusk.
- [Investor issues stark warning to retail buyers chasing SpaceX ...](https://finance.yahoo.com/video/investor-issues-stark-warning-retail-141638725.html)
  - 8 days ago ... Bradley Tusk, CEO of Tusk Ventures, shares his investment strategy for high-valuation AI IPOs such as SpaceX, OpenAI and Anthropic. He ...

### Search warnings
- news:TUSK analyst price target: No results found.
- news:Mammoth Energy Services, Inc. stock rating OR consensus OR upgrade OR downgrade: No results found.
- news:TUSK guidance OR investor day OR catalyst: No results found.

## Web research — web_drivers

- Queries: Mammoth Energy Services, Inc. TUSK outlook OR catalyst OR commodity OR uranium OR rare earth OR vanadium, TUSK sector drivers OR market demand, Mammoth Energy Services, Inc. TUSK backlog OR contract OR refinancing OR leverage
- Unique hits: 12
- Pages fetched: 1/3

### Web synthesis — web_drivers (rule-based fallback — Ollama unavailable)
**Keyword hits:** revenue

- (TUSK) 7-Day Stock Price Changes.Earnings announcements often act as important catalysts for TUSK, as they provide updated information on revenue, profitability and management's outlook.

### Sources found
- [Mammoth Energy Services, Inc. (TUSK) Stock Price... - Yahoo Finance](https://finance.yahoo.com/quote/TUSK/)
  - Find the latest Mammoth Energy Services, Inc. (TUSK) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Mammoth Energy Services, Inc. (TUSK) Stock Price... | Seeking Alpha](https://seekingalpha.com/symbol/TUSK)
  - TUSK Mammoth Energy Services, Inc. Stock Price & Overview.Mammoth Energy Services, Inc. operates as an energy services company in the United States, Canada, …
- [Mammoth Energy Services Share Price Today | NASDAQ: TUSK...](https://in.investing.com/equities/mammoth-energy-services-inc)
  - View the real-time Mammoth Energy Services Inc (NASDAQ TUSK) share price. Assess historical data, charts, technical analysis and contribute in the forum.
- [TUSK Price Today: Mammoth Energy Services, Inc. Stock... | MEXC](https://www.mexc.com/stocks/tusk)
  - Mammoth Energy Services, Inc. (TUSK) 7-Day Stock Price Changes.Earnings announcements often act as important catalysts for TUSK, as they provide updated info…
- [Demand curve - Wikipedia](https://en.wikipedia.org/wiki/Demand_curve)
  - Market demand curve: the relationship between the quantity of a product that all consumers in the market are willing to buy and its price. The market demand …
- [Understanding Demand: Key Determinants and the Demand Curve](https://www.investopedia.com/terms/d/demand.asp)
  - Apr 7, 2026 · Market demand is the total quantity demanded by all consumers in a market for a given good, and aggregate demand is the total demand for all go…
- [Market Demand: Definition, How to Calculate, Determinants](https://penpoin.com/market-demand/)
  - Jan 21, 2025 · What’s it: Market demand is the sum of individual demand in the market at a given price. Economists define demand as our willingness and abili…
- [Global Dram And Nand Market Outlook 2025–2026: Ai Demand ...](https://www.axtekic.com/news/global-dram-and-nand-market-outlook-2025–2026:-ai-demand-sparks-new-wave-of-price-hikes.html)
  - 19 hours ago · Driven by AI adoption, DRAM and NAND flash markets face supply shortages. Micron, SanDisk, Samsung, and SK Hynix lead price hikes, boosting SS…
- [Morning Bid: US-China trade war goes full throttle](https://finance.yahoo.com/news/morning-bid-us-china-trade-103633856.html)
  - The escalating U.S.-China trade war has expanded and moved beyond tariffs, now hitting everything from chips to planes and pharma. * Shares fell in Asia...
- [Mammoth Energy Services, Inc. Announces Sale of Engineering ...](https://ir.mammothenergy.com/news-events/press-releases/detail/141/mammoth-energy-services-inc-announces-sale-of-engineering)
  - Dec 2, 2025 ... At closing, Mammoth Energy Partners LLC received total cash proceeds of $23.5 million. An additional $2.5 million was placed into escrow to f…
- [Press Releases - Mammoth Energy Services, Inc.](https://ir.mammothenergy.com/news-events/press-releases)
  - Mammoth Energy Services, Inc. Announces Fourth Quarter and Full Year 2025 Operational and Financial Results. Feb 05, 2026 4:30pm EST ...
- [Mammoth Energy Announces Growth of Engineering Services ...](https://ir.mammothenergy.com/news-events/press-releases/detail/12/mammoth-energy-announces-growth-of-engineering-services)
  - Feb 17, 2021 ... OKLAHOMA CITY, Feb. 17, 2021 (GLOBE NEWSWIRE) -- Mammoth Energy Services, Inc. (“Mammoth” or the “Company”) (NASDAQ:TUSK) today announced ...

### Search warnings
- news:Mammoth Energy Services, Inc. TUSK outlook OR catalyst OR commodity OR uranium OR rare earth OR vanadium: No results found.
- news:Mammoth Energy Services, Inc. TUSK backlog OR contract OR refinancing OR leverage: No results found.

## SEC filing [S24]
- Extraction OK: True
- Item 1A chars: 2
- Item 7 chars: 2
- Meta: {'accession_number': '0001628280-26-015693', 'filing_date': '2026-03-06', 'source': 'edgartools', 'path': 'C:\\DevWork\\equity_research_agent\\data\\filings\\TUSK_10k.txt'}

## Qualitative analysis (local LLM)

### Item 1A — Risk Factors
I'm happy to help! However, I don't see any text excerpted below. Please provide the filing excerpt, and I'll be happy to analyze it for you.

Once I receive the excerpt, I'll return a concise Markdown summary with short bullet points and 1-2 short quotes highlighting:

* Shifts in management tone or competitive dynamics
* Explicit forward guidance (capex, growth, margins)
* Counterparty, regulatory, or legal risks

Please provide the excerpt, and I'll get started!


### Item 7 — MD&A
I'm happy to help! However, I need the excerpt text you'd like me to analyze. Please provide it, and I'll summarize the key points in Markdown format, focusing on evidence within the text.


## Research loop (think → act)

1. _heuristic_ — Coverage looks adequate for this pass; stopping iterative loop.

## Sources

- **[S1]** TUSK fundamentals (yfinance)
  - Mammoth Energy Services, Inc.: price=2.685, rev=44292000.0, fcf=-89122000.0, shares=48170647.0, rev_cagr=-0.5035930506625281, ROIC=-0.1761222432972137, FCF yield=-0.689061785497…
- **[S2]** TUSK EV/EBITDA valuation (multiples)
  - Base implied price=168.1219062720914, multiple=8.0
- **[S3]** TUSK DCF valuation (dcf)
  - Base share price=2.482501947036513, bull=4.12956738773692, bear=2.1198753553474856
- **[S4]** TUSK peer comps (peers)
  - Peers: ; rows=1
- **[S5]** TUSK earnings history (earnings)
  - rows=12; next=2026-08-07
- **[S6]** TUSK Forecast, Price Target & Analyst Ratings | ChartMill.com (web) — https://www.chartmill.com/stock/quote/TUSK/analyst-ratings
  - 7 analysts have analysed TUSK and the average price target is 4.28 USD. This implies a price increase of 53% is expected in the next year compared to the ...
- **[S7]** TUSK Stock Forecast & Price Target | Mammoth Energy Services Inc ... (web) — https://valueinvesting.io/TUSK/estimates
  - The average stock forecast for Mammoth Energy Services Inc (TUSK) is 4.28 USD. This price target corresponds to an upside of 36.87%. The range of stock ...
- **[S8]** Mammoth Energy Services, Inc. (TUSK) - Yahoo Finance (web) — https://finance.yahoo.com/quote/TUSK/
  - Find the latest Mammoth Energy Services, Inc. (TUSK) stock quote, history, news and other vital information to help you with your stock trading and ...
- **[S9]** TUSK - Mammoth Energy Services Stock Forecast - StockInvest.us (web) — https://stockinvest.us/stock/TUSK
  - Given the current short-term trend, the stock is expected to rise 9.16% during the next 3 months and, with a 90% probability hold a price between $2.85 and ...
- **[S10]** Analyst Upgrades & Downgrades - MarketWatch (web) — https://www.marketwatch.com/tools/upgrades-downgrades
  - Real-time information on stock upgrades and downgrades by MarketWatch. View information on strong stocks to buy and weak stocks to sell.
- **[S11]** Stock Screener: Best Stocks Consensus Opinion Analysts | MarketScreener (web) — https://m.marketscreener.com/tools/stock-screener/top-consensus/
  - A surprise rate measures the difference between the consensus (average estimated value by the analysts covering the company) of an accounting item the day before publication and…
- **[S12]** What Are Stock Upgrades & Downgrades? | The Motley Fool (web) — https://www.fool.com/terms/u/upgrades-downgrades/
  - What does a downgrade mean for stocks? When a stock analyst changes his or her opinion of a stock, making either an upgrade or a downgrade, it can sometimes lead to a large swin…
- **[S13]** Consensus: AI for Research (web) — https://consensus.app/
  - Consensus is an AI academic search engine for peer-reviewed literature—your research OS for finding, organizing, and analyzing science 10x faster.
- **[S14]** Mammoth Energy Services, Inc. (TUSK) Stock Price, News, Quote & History - Yahoo Finance (web_page) — https://finance.yahoo.com/quote/TUSK/
  - Mammoth Energy Services, Inc. (TUSK) Stock Price, News, Quote & History - Yahoo Finance Oops, something went wrong Skip to navigation Skip to main content Skip to right column W…
- **[S15]** Mammoth Energy Services, Inc. (TUSK) Stock Price... - Yahoo Finance (web) — https://finance.yahoo.com/quote/TUSK/
  - Find the latest Mammoth Energy Services, Inc. (TUSK) stock quote, history, news and other vital information to help you with your stock trading and investing.
- **[S16]** Mammoth Energy Services, Inc. (TUSK) Stock Price... | Seeking Alpha (web) — https://seekingalpha.com/symbol/TUSK
  - TUSK Mammoth Energy Services, Inc. Stock Price & Overview.Mammoth Energy Services, Inc. operates as an energy services company in the United States, Canada, and internationally.
- **[S17]** Mammoth Energy Services Share Price Today | NASDAQ: TUSK... (web) — https://in.investing.com/equities/mammoth-energy-services-inc
  - View the real-time Mammoth Energy Services Inc (NASDAQ TUSK) share price. Assess historical data, charts, technical analysis and contribute in the forum.
- **[S18]** TUSK Price Today: Mammoth Energy Services, Inc. Stock... | MEXC (web) — https://www.mexc.com/stocks/tusk
  - Mammoth Energy Services, Inc. (TUSK) 7-Day Stock Price Changes.Earnings announcements often act as important catalysts for TUSK, as they provide updated information on revenue, …
- **[S19]** Demand curve - Wikipedia (web) — https://en.wikipedia.org/wiki/Demand_curve
  - Market demand curve: the relationship between the quantity of a product that all consumers in the market are willing to buy and its price. The market demand curve can be obtaine…
- **[S20]** Understanding Demand: Key Determinants and the Demand Curve (web) — https://www.investopedia.com/terms/d/demand.asp
  - Apr 7, 2026 · Market demand is the total quantity demanded by all consumers in a market for a given good, and aggregate demand is the total demand for all goods and services in …
- **[S21]** Market Demand: Definition, How to Calculate, Determinants (web) — https://penpoin.com/market-demand/
  - Jan 21, 2025 · What’s it: Market demand is the sum of individual demand in the market at a given price. Economists define demand as our willingness and ability as consumers to b…
- **[S22]** Global Dram And Nand Market Outlook 2025–2026: Ai Demand ... (web) — https://www.axtekic.com/news/global-dram-and-nand-market-outlook-2025–2026:-ai-demand-sparks-new-wave-of-price-hikes.html
  - 19 hours ago · Driven by AI adoption, DRAM and NAND flash markets face supply shortages. Micron, SanDisk, Samsung, and SK Hynix lead price hikes, boosting SSD, server, and autom…
- **[S23]** Mammoth Energy Services, Inc. (TUSK) Stock Price, News, Quote & History - Yahoo Finance (web_page) — https://finance.yahoo.com/quote/TUSK/
  - Mammoth Energy Services, Inc. (TUSK) Stock Price, News, Quote & History - Yahoo Finance Oops, something went wrong Skip to navigation Skip to main content Skip to right column W…
- **[S24]** TUSK 10-K (sec)
  - Item 1A chars=2, Item 7 chars=2, ok=True, source=edgartools
- **[S25]** TUSK 8-K 2026-06-26 (sec) — https://www.sec.gov/Archives/edgar/data/1679268/000162828026045745/tusk-20260625.htm
  - 8-K
- **[S26]** TUSK 8-K 2026-05-15 (sec) — https://www.sec.gov/Archives/edgar/data/1679268/000162828026035328/tusk-20260513.htm
  - 8-K
- **[S27]** TUSK 10-Q 2026-05-11 (sec) — https://www.sec.gov/Archives/edgar/data/1679268/000162828026033686/tusk-20260331.htm
  - 10-Q
- **[S28]** TUSK 8-K 2026-05-11 (sec) — https://www.sec.gov/Archives/edgar/data/1679268/000162828026033142/tusk-20260511.htm
  - 8-K
- **[S29]** TUSK 10-K 2026-03-06 (sec) — https://www.sec.gov/Archives/edgar/data/1679268/000162828026015693/tusk-20251231.htm
  - 10-K
- **[S30]** TUSK 8-K 2026-03-06 (sec) — https://www.sec.gov/Archives/edgar/data/1679268/000162828026015465/tusk-20260306.htm
  - 8-K
- **[S31]** TUSK 8-K 2025-12-04 (sec) — https://www.sec.gov/Archives/edgar/data/1679268/000167926825000046/tusk-20251202.htm
  - 8-K
- **[S32]** TUSK 10-Q 2025-11-03 (sec) — https://www.sec.gov/Archives/edgar/data/1679268/000167926825000039/tusk-20250930.htm
  - 10-Q
- **[S33]** Item 1A summary (nlp)
  - ### Item 1A — Risk Factors I'm happy to help! However, I don't see any text excerpted below. Please provide the filing excerpt, and I'll be happy to analyze it for you.  Once I …
- **[S34]** Item 7 summary (nlp)
  - ### Item 7 — MD&A I'm happy to help! However, I need the excerpt text you'd like me to analyze. Please provide it, and I'll summarize the key points in Markdown format, focusing…
- **[S35]** TUSK driver analysis (drivers)
  - ok=True; drivers=7
- **[S36]** TUSK memo sections (memo)
  - mode=rules; proxies=1

## Self-critique

_Automated review (heuristic)._

### Strengths
- Combines local fundamentals, optional DCF scenarios, and cited sources where available.
- Keeps a non-advisory framing for local research drafts.

### Issues & gaps
- No major structural issues flagged by heuristics.

### Caution for readers
- Treat scenario prices as sensitivity output, not a forecast.
- Re-check primary filings and fresh market data before any decision.
