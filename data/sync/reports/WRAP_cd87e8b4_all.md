# WRAP — Full research pack

> Not investment advice. Local research draft only.

**Templates:** memo, valuation, deep, income, fast
**Generated:** 2026-07-21T02:37:03.403845+00:00



---

# Template: Institutional deep dive (memo) (`memo`)

# WRAP — Planned Research Report

> Not investment advice. Local research draft only.

**Goal:** Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers
**Mode:** deep
**Template:** memo
**Planner:** template

## Plan executed

- **(1) Snapshot, KPIs & capital structure** (`fundamentals`): get_fundamentals
  - Multi-year KPI table, leverage, EV/EBITDA snapshot. Focus: Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers
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
- Company: Wrap Technologies, Inc.
- Sector / industry: Technology / Scientific & Technical Instruments
- Price: 1.87
- 52-week range: $1.04 – $3.23
- Market cap: $104.23M
- Enterprise value: $97.43M
- Shares outstanding: 55.74M
- Beta: 1.368
- Book equity: $11.49M
- Revenue (latest): $4.67M
- EBITDA (latest): -$12.89M
- Free cash flow (latest): -$10.68M
- Operating income: -$13.48M
- Operating margin: -288.6%
- EV / EBITDA: -7.6x
- ROIC: -129.2%
- FCF yield: -10.2%
- Debt / Equity: 0.2103568320278503
- FCF / share: -$0.19
- Revenue / share: $0.08

### Capital structure
- Cash: $3.47M
- Short-term debt: $320.00K
- Long-term debt: $2.10M
- Total debt: $2.42M
- Net debt: -$1.05M
- Net debt / EBITDA: 0.1x

### Growth
- Revenue CAGR: -16.6%
- FCF CAGR: —
- Latest revenue YoY: 3.7%
- Latest FCF YoY: -28.7%

### Market expectations (yfinance, sparse)
- Mean target: —
- Target range: — – —
- Recommendation: none

_Consensus revenue/EBITDA forecasts are often unavailable via free feeds; treat targets as point-in-time only._

### Historical KPIs (multi-year)

| Year | Revenue | OCF | Capex | FCF | EBITDA | LT debt | Cash | Net debt | Net income |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2025 | $4.67M | -$10.29M | $387.00K | -$10.68M | -$12.89M | $2.42M | $3.47M | -$1.05M | -$10.34M |
| 2024 | $4.51M | -$8.12M | $168.00K | -$8.29M | -$14.74M | $2.20M | $3.61M | -$1.41M | -$5.88M |
| 2023 | $6.13M | -$16.70M | $623.00K | -$17.33M | -$17.90M | $2.29M | $3.96M | -$1.67M | -$30.22M |
| 2022 | $8.05M | -$14.60M | $1.13M | -$15.73M | -$16.97M | $301.00K | $5.33M | -$5.03M | -$17.62M |

## Charts

### Revenue & FCF history
![Revenue & FCF history](/charts/WRAP_memo_revenue_fcf.png)

### DCF scenario prices
![DCF scenario prices](/charts/WRAP_memo_dcf_scenarios.png)

### Base-case FCF path
![Base-case FCF path](/charts/WRAP_memo_base_fcf_path.png)

### EV/EBITDA scenario prices
![EV/EBITDA scenario prices](/charts/WRAP_memo_ev_ebitda_scenarios.png)

### Normalized price vs peers
![Normalized price vs peers](/charts/WRAP_memo_peers_normalized.png)

## DCF valuation (base / bull / bear) [S3]

> Simplified revenue->FCF DCF. Not investment advice; assumptions are editable heuristics.

- Spot price: $1.87
- Base revenue: $4.67M
- Shares: 55,738,250
- Net debt (Debt−Cash): -$1.05M

| Scenario | Growth | FCF margin | WACC | Term. g | Equity value | Share price | Upside |
|----------|--------|------------|------|---------|--------------|-------------|--------|
| bear | -3.3% | 1.0% | 12.0% | 1.5% | $1.42M | $0.03 | -98.6% |
| base | 3.7% | 3.0% | 10.0% | 2.5% | $3.06M | $0.05 | -97.1% |
| bull | 10.7% | 8.0% | 9.0% | 3.0% | $9.93M | $0.18 | -90.5% |

### Assumption notes
- Base revenue growth seeded from historical rate (3.7%).
- Latest FCF margin was -228.5%; scenarios use normalized positive margins for a going-concern DCF.


### Base-case projected FCF

- Year 1: revenue $4.84M, FCF $145,291 (PV $132,083)
- Year 2: revenue $5.02M, FCF $150,610 (PV $124,471)
- Year 3: revenue $5.20M, FCF $156,124 (PV $117,298)
- Year 4: revenue $5.39M, FCF $161,840 (PV $110,539)
- Year 5: revenue $5.59M, FCF $167,765 (PV $104,169)
- Terminal value $2.29M (PV $1.42M)

## Valuation — EV/EBITDA scenarios [S2]

> Priced-in model: implied price = (EBITDA × EV/EBITDA − net debt) ÷ shares. Not a forecast.

- Spot: $1.87
- Net debt used: -$1.05M

| Scenario | EBITDA | EV/EBITDA | Implied EV | Equity value | Implied price |
|---|---:|---:|---:|---:|---:|
| bear | $700.00M | 6.0x | $4.20B | $4.20B | $75.37 |
| base | $1.00B | 8.0x | $8.00B | $8.00B | $143.55 |
| bull | $1.20B | 10.0x | $12.00B | $12.00B | $215.31 |

- EBITDA missing or non-positive; scenarios use placeholder $1B EBITDA — edit before relying on prices.
- No current EV/EBITDA; defaulted base multiple to 8.0x.

## Peer & factor comps

- Sector / industry: Technology / Scientific & Technical Instruments
- Peers: —

| Ticker | Mkt cap | EV/EBITDA | ND/EBITDA | Beta | 1y | 5y | Vol |
|---|---:|---:|---:|---:|---:|---:|---:|
| WRAP | $104.2M | -7.4x | 0.5x | 1.37 | 37.0% | -73.2% | 91.7% |

- No industry peer map match; comps limited to the subject ticker.

_Price returns are price-only (dividends ignored). Peer set is heuristic, not a formal comps universe._

## Earnings, guidance & revision catalysts

- Next earnings (calendar): 2026-08-13

| Date | EPS est | EPS actual | Surprise | 1-day move |
|---|---:|---:|---:|---:|
| 2023-03-01 | -0.08 | -0.09 | -0.01 | -11.0% |
| 2022-11-09 | -0.08 | -0.07 | 0.01 | 11.9% |
| 2022-08-10 | -0.10 | -0.10 | 0.00 | 10.3% |
| 2022-05-03 | -0.11 | -0.11 | 0.00 | 2.7% |
| 2022-03-10 | -0.14 | -0.10 | 0.04 | -7.5% |
| 2021-10-28 | -0.15 | -0.15 | 0.00 | 1.2% |
| 2021-07-29 | -0.12 | -0.18 | -0.06 | 2.7% |
| 2021-04-29 | -0.09 | -0.14 | -0.05 | -2.0% |
| 2021-03-04 | -0.10 | -0.09 | 0.01 | -2.0% |
| 2020-10-29 | -0.08 | -0.11 | -0.03 | -2.0% |
| 2020-07-31 | -0.07 | -0.09 | -0.02 | -2.0% |
| 2020-04-29 | -0.09 | -0.08 | 0.01 | -2.0% |

_EPS surprise vs 1-day move Pearson r=-0.035 (n=12, p≈0.911); treat as suggestive only._

_Guidance vs Street and adjusted EBITDA are often missing from free feeds; use web/SEC sections for narrative guidance._

## Recent SEC filings (10-Q / 8-K)

| Date | Form | Description |
|---|---|---|
| 2026-07-13 | 8-K | [8-K](https://www.sec.gov/Archives/edgar/data/1702924/000149315226033073/form8-k.htm) |
| 2026-05-13 | 10-Q | [QUARTERLY REPORT PURSUANT TO SECTION 13 OR 15(D)](https://www.sec.gov/Archives/edgar/data/1702924/000114036126021091/form10q.htm) |
| 2026-05-13 | 8-K | [8-K](https://www.sec.gov/Archives/edgar/data/1702924/000149315226022738/form8-k.htm) |
| 2026-03-26 | 10-K | [10-K](https://www.sec.gov/Archives/edgar/data/1702924/000114036126011401/form10k.htm) |
| 2026-03-26 | 8-K | [8-K](https://www.sec.gov/Archives/edgar/data/1702924/000149315226012909/form8-k.htm) |
| 2026-02-04 | 8-K | [8-K](https://www.sec.gov/Archives/edgar/data/1702924/000149315226005110/form8-k.htm) |
| 2025-12-17 | 8-K | [8-K](https://www.sec.gov/Archives/edgar/data/1702924/000149315225028133/form8-k.htm) |
| 2025-11-13 | 10-Q | [QUARTERLY REPORT PURSUANT TO SECTION 13 OR 15(D)](https://www.sec.gov/Archives/edgar/data/1702924/000114036125041816/form10q.htm) |
| 2025-11-12 | 8-K | [8-K](https://www.sec.gov/Archives/edgar/data/1702924/000149315225021986/form8-k.htm) |
| 2025-11-05 | 8-K | [8-K](https://www.sec.gov/Archives/edgar/data/1702924/000149315225020900/form8-k.htm) |
| 2025-10-27 | 8-K | [8-K](https://www.sec.gov/Archives/edgar/data/1702924/000149315225019686/form8-k.htm) |
| 2025-08-26 | 8-K | [8-K](https://www.sec.gov/Archives/edgar/data/1702924/000164117225025536/form8-k.htm) |

_Headlines/meta only — documents not fully parsed in this pass._

## Key driver analysis (quarterly)

Pearson / Spearman correlations of quarterly stock returns with fundamentals.

| Driver | Pearson r | p | n | Spearman ρ | p |
|---|---:|---:|---:|---:|---:|
| Revenue growth (YoY) | — | — | 1 | — | — |
| Free cash flow | -0.530 | 0.279 | 5 | -0.300 | 0.586 |
| FCF margin | 0.121 | 0.833 | 5 | 0.000 | 1.000 |
| Operating cash flow | -0.504 | 0.312 | 5 | -0.300 | 0.586 |
| Long-term debt level | 0.753 | 0.047 | 5 | 1.000 | 0.000 |
| EBITDA | 0.725 | 0.068 | 5 | 0.700 | 0.090 |
| Capex (abs) | 0.588 | 0.208 | 5 | 0.600 | 0.194 |

### Regime check (FCF)

- later: r=-0.53 (n=5, p≈0.279)

- Correlations describe association, not causation.
- Small samples (especially regime splits) are directional only.
- Regime split at 2023-12-31 (sample midpoint); directional only.

## Executive summary

Wrap Technologies, Inc. (WRAP) trades near 1.87 with market cap $104.23M and EV $97.43M. Net debt is -$1.05M (ND/EBITDA 0.08152974943759211). Latest revenue $4.67M, EBITDA -$12.89M, FCF -$10.68M.

**Goal focus:** Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers.

What matters most (framework): balance-sheet trajectory, cash generation vs leverage, and whether market expectations (sparse free-data targets) already price execution risk.

EV/EBITDA implied prices — bear $75.37 / base $143.55 / bull $215.31.

## Company setup & business model

Sector/industry: Technology / Scientific & Technical Instruments. Detail the competitive position, revenue mix, and strategic pivots from SEC MD&A and web sources in adjacent report tabs. This skeleton does not invent segment KPIs.

## Variant perception

- **Consensus frame (sparse):** recommendation=none, mean target=—.
- **Bear:** leverage and execution risk dominate; cash generation fails to cover refinancing / reinvestment needs; equity remains constrained by net debt.
- **Bull:** cash-flow and strategic optionality re-rate the equity as leverage falls and growth/mix improves.
- **Middle:** returns may track free-cash-flow more than headline revenue — verify with driver analysis tab.

## Catalysts & monitoring

- Next earnings window (calendar): 2026-08-13
- Peer tape to watch: n/a
- Monitor: FCF vs net debt, leverage (ND/EBITDA), refinancing headlines, and material 8-K strategy updates.
- Recent filing: 8-K on 2026-07-13 — 8-K
- Recent filing: 10-Q on 2026-05-13 — QUARTERLY REPORT PURSUANT TO SECTION 13 OR 15(D)
- Recent filing: 8-K on 2026-05-13 — 8-K
- Recent filing: 10-K on 2026-03-26 — 10-K
- Recent filing: 8-K on 2026-03-26 — 8-K

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
| Guidance / outlook | Forward cash/earnings path | WRAP - Wrap Technologies Inc Stock Price Forecast 2025, 2026, 2030 to 2050 - StockScan The Wrap Technologies Inc (WRAP) stock price forecast for the next 30 days is generally negat | WRAP - Wrap Technologies Inc Stock Price Forecast 2025, 2026, 2030 to 2050 - StockScan |
| Contract / backlog | Demand durability | Trump Just Gave a Shoutout to This Top Defense Contractor. Here’s What to Know. Out of the 24 analysts covering GD stock, 13 recommend “Strong Buy,” 10 recommend “Hold,” and one re | Trump Just Gave a Shoutout to This Top Defense Contractor. Here’s What to Know. |
| Margin / EBITDA | Mix and operating leverage | Building an Investment Thesis / Street Of Walls If so, what are the catalysts that will cause the Company to beat earnings (e.g., higher revenue, higher margins, lower interest exp | Building an Investment Thesis | Street Of Walls |
| Capex / capacity | Leading indicator of future revenue | 2 Under-the-Radar Energy Stocks to Watch for AI Demand in 2026 Key Points Data center expansion is outpacing grid capacity, creating demand for alternative power... | 2 Under-the-Radar Energy Stocks to Watch for AI Demand in 2026 |
| Leverage / refinancing | Balance-sheet repair | Leverage Public Page Leverage has a powerful, intelligent search, expanded document library, and a customizable calendar. We make it easy to find what you’re looking for with a soc | Leverage Public Page |

_Proxies are heuristic extractions from public web/SEC context; verify against primary filings._

## Catalyst calendar

| Window | Catalyst | Notes |
|---|---|---|
| 2026-08-13 | Earnings | Next report date from yfinance calendar |
| 2026-07-13 | 8-K | 8-K |
| 2026-05-13 | 10-Q | QUARTERLY REPORT PURSUANT TO SECTION 13 OR 15(D) |
| 2026-05-13 | 8-K | 8-K |
| 2026-03-26 | 10-K | 10-K |
| 2026-03-26 | 8-K | 8-K |
| 2026-02-04 | 8-K | 8-K |
| 2025-12-17 | 8-K | 8-K |
| 2025-11-13 | 10-Q | QUARTERLY REPORT PURSUANT TO SECTION 13 OR 15(D) |
| 2025-11-12 | 8-K | 8-K |
| 2025-11-05 | 8-K | 8-K |
| 2025-10-27 | 8-K | 8-K |
| 2025-08-26 | 8-K | 8-K |
| Jul 7, 2026 | Web event | Gallery | Built with Claude: Life Sciences - Cerebral Valley |
| May 14, 2024 | Web event | The Curious Case of Catalysts | Behavioural Investment |
| July 16, 2026 | Web event | Uranium - Price - Chart - Historical Data - News |
| September 30, 2025 | Web event | WRAP TECHNOLOGIES, INC. SEC 10-Q Report — TradingView News |
| April 30, 2026 | Web event | Wrap-Up From VettaFi’s Q2 Market Outlook Symposium |
| December 7, 2008 | Web event | Leverage - Reddit |

## Web research — web_analysts

- Queries: WRAP analyst price target, Wrap Technologies, Inc. stock rating OR consensus OR upgrade OR downgrade, WRAP Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers analyst, WRAP guidance OR investor day OR catalyst
- Unique hits: 22
- Pages fetched: 1/3

### Web synthesis — web_analysts (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk

- | www.benzinga.com | https://www.benzinga.com/analyst-ratings/analyst-color/21/07/22022104/5-chemical-stocks-get-mixed-reaction-which-ones-got-an-upgrade-or-downgrade
The risk-reward balance may be unfavorable for chemical stocks heading into second-quarter earnings season, and one analyst adjusted his chemical stock ratings accordingly on Friday.Dow Inc (NYSE:DOW) downgraded from Neutral to Underperform, price target cut from $71 to $68.
- The Score for WRAP is 31, which is 38% below its historic median score of 50, and infers higher risk than normal.

### Sources found
- [WRAP - Wrap Technologies Inc Stock Price Forecast 2025, 2026, 2030 to 2050 - StockScan](https://stockscan.io/stocks/WRAP/forecast)
  - The Wrap Technologies Inc (WRAP) stock price forecast for the next 30 days is generally negative, with an average analyst price target of $0.8586, representi…
- [Wrap Technologies (WRAP) Stock Forecast, Price Targets and Analysts Predictions - TipRanks.com](https://www.tipranks.com/stocks/wrap/forecast)
  - Based on 1 Wall Street analysts offering 12 month price targets for Wrap Technologies in the last 3 months. The average price target is $2.00 with a high for…
- [Wrap Technologies, Inc. Common Stock (WRAP) Analyst Reports & Ratings | Nasdaq](https://www.nasdaq.com/market-activity/stocks/wrap/analyst-research)
  - Based on analysts offering 12 month price targets for WRAP in the last 3 months. The average price target is $0.00 with a high estimate of $0.00 and a low es…
- [Wrap Technologies (WRAP) Stock Forecast: Analyst Ratings, Predictions & Price Target 2025](https://public.com/stocks/wrap/forecast-price-target)
  - This rating is provided by third-party analysts and is not investment advice from Public.com. Wall Street analysts have set a price target of $6.55, reflecti…
- [6 Wall Street analysts have issued price targets on SpaceX. Here's the one I agree with most.](https://www.msn.com/en-us/money/topstocks/6-wall-street-analysts-have-issued-price-targets-on-spacex-here-s-the-one-i-agree-with-most/ar-AA25Xqw8?ocid=BingNewsVerp)
  - Analyst price targets and earnings projections are important because they help set a baseline for a stock. Given SpaceX's valuations, some analysts believe t…
- [SpaceX Shares Fall Below $135 IPO Price For The First Time](https://finance.yahoo.com/markets/stocks/articles/spacex-shares-fall-below-135-170708190.html)
  - SpaceX bulls have reportedly noted SpaceX will need to...
- [Trump Just Gave a Shoutout to This Top Defense Contractor. Here’s What to Know.](https://finance.yahoo.com/markets/stocks/articles/trump-just-gave-shoutout-top-153405657.html)
  - Out of the 24 analysts covering GD stock, 13 recommend “Strong Buy,” 10 recommend “Hold,” and one re...
- [Stocks skid to losing week as Chinese AI fears fuel chipmaker rout](https://nypost.com/2026/07/17/business/stocks-skid-to-losing-week-as-chinese-ai-fears-fuel-chipmaker-rout/)
  - Iran also said Friday that it targeted US military forces in Syria and Bahrain. Analysts have warned...
- [Yahoo Finance - Stock Market Live, Quotes, Business & Finance News](https://finance.yahoo.com/)
  - At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage rate…
- [PLTR Stock Price | Palantir Technologies Inc. Stock... | MarketWatch](https://www.marketwatch.com/investing/stock/pltr)
  - PLTR | Complete Palantir Technologies Inc. stock news by MarketWatch. View real-time stock prices and stock quotes for a full financial overview.
- [5 Chemical Stocks Get Mixed Reaction: Which Ones Got An Upgrade...](https://www.benzinga.com/analyst-ratings/analyst-color/21/07/22022104/5-chemical-stocks-get-mixed-reaction-which-ones-got-an-upgrade-or-downgrade)
  - The risk-reward balance may be unfavorable for chemical stocks heading into second-quarter earnings season, and one analyst adjusted his chemical stock ratin…
- [Where will Wrap Technologies, Inc. Stock Be In 1 Year? – Financhill](https://financhill.com/stock-forecast/wrap-stock-prediction)
  - The current Wrap Technologies, Inc. [WRAP] share price is $1.52. The Score for WRAP is 31, which is 38% below its historic median score of 50, and infers hig…

### Search warnings
- news:Wrap Technologies, Inc. stock rating OR consensus OR upgrade OR downgrade: No results found.
- news:WRAP Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers analyst: No results found.

## Web research — web_drivers

- Queries: WRAP Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers, Wrap Technologies, Inc. WRAP outlook OR catalyst OR commodity OR uranium OR rare earth OR vanadium, WRAP sector drivers OR market demand, Wrap Technologies, Inc. WRAP backlog OR contract OR refinancing OR leverage
- Unique hits: 18
- Pages fetched: 3/3

### Web synthesis — web_drivers (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, guidance, capex, revenue, margin

- Thesis · FMP-verified financials · Catalysts · ClinicalTrials.gov-checked pipeline ·

[HIT] Building an Investment Thesis | Street Of Walls | www.streetofwalls.com | https://www.streetofwalls.com/finance-training-courses/hedge-fund-training/building-an-investment-thesis/
If so, what are the catalysts that will cause the Company to beat earnings (e.g., higher revenue, higher margins, lower interest expense, share buybacks, etc.)?
- Table of Contents
ACT I — IDENTITY & THESIS
- §1 — Company DNA & Business Model
- §2 — Sector & Structural Tailwinds
- §3 — Thesis Statement
ACT II — FORENSIC DEEP DIVE
- §4 — Audit Quality & Accounting Standards
- §5 — Earnings Quality (Accruals, CFO/PAT, Beneish)
- §6 — Balance Sheet Archaeology
- §7 — Related Party & Governance Forensics
- §8 — IPO Forensics & DRHP Intelligence
ACT III — OPERATING ENGINE
- §9 — Revenue Architecture & Segment Dynamics
- §10 — Cost Structure & Margin Drivers
- §11 — Capital Allocation Arc (5 Years)
- §12 — Working Capital & Cash Conversion
- §13 — Capacity, Capex, and the Infrastructure Bet
ACT IV — MANAGEMENT QUALITY
- §14 — Walk-the-Talk: Promises vs Delivery
- §15 — Guidance Discipline & Communication Quality
- §16 — Incentive Architecture & Skin-in-the-Game
- §17 — Capital Allocation Philosophy
ACT V — POSITIONING & PEERS
- §18 — Competitive Position & Moat Assessment
- §19 — Customer Concentration & Relationship Durability
- §20 — Regulatory & ESG Landscape
- §21 — Bear Case Stress Test
ACT VI — VALUATION & SCENARIOS
- §22 — Valuation Inheritance from PRISM
- §23 — Bear / Base / Bull Scenarios
- §24 — Catalysts & De-rating Risks
- §25 — Entry/Exit Framework
ACT VII — VERDICT
- §26 — The Three Questions
- §27 — Consensus vs.
- Payment Solutions
(₹769 Cr, FY26 actual; ~53% of revenue) is the heritage vertical: the design, manufacture, and personalisation of payment cards — debit, credit, prepaid, and co-branded plastic cards — for India's banking system.
- Bear Case
Critical risk analysis — the trade you should reconsider.

### Sources found
- [Seshaasai Technologies Limited — Institutional Deep Dive](https://seshaasai-technologies.netlify.app/)
  - The key industry shift that would change this thesis: a sustained RBI/government push to replace physical payment cards with purely digital (UPI-linked) inst…
- [Catalyst Ventures — Institutional-Grade Biotech Investment Intelligence](https://catalyst-ventures.eu/)
  - Our analysts author the institutional deep-dives by hand in a frontier-model workbench, grounded in verified FMP data and cross-checked against ClinicalTrial…
- [Building an Investment Thesis | Street Of Walls](https://www.streetofwalls.com/finance-training-courses/hedge-fund-training/building-an-investment-thesis/)
  - If so, what are the catalysts that will cause the Company to beat earnings (e.g., higher revenue, higher margins, lower interest expense, share buybacks, etc…
- [The Curious Case of Catalysts | Behavioural Investment](https://behaviouralinvestment.com/2024/05/01/the-curious-case-of-catalysts/)
  - May 14, 2024 - There are two types of investment thesis – one about something that is already performing well, here a catalyst is unnecessary because we just…
- [Uranium - Price - Chart - Historical Data - News](https://tradingeconomics.com/commodity/uranium)
  - Uranium rose to 85.45 USD/Lbs on July 16, 2026, up 0.23% from the previous day. Over the past month, Uranium's price has fallen 0.12%, but it is still 19.18%…
- [WRAP TECHNOLOGIES, INC. SEC 10-Q Report — TradingView News](https://www.tradingview.com/news/tradingview:ad8dc011d6c94:0-wrap-technologies-inc-sec-10-q-report/)
  - WRAP TECHNOLOGIES, INC., a leading provider of innovative public safety technologies and services, has released its Form 10-Q report for the third quarter en…
- [America's Leading Producer of Critical Minerals - Uranium Rare Earth...](https://www.readkong.com/page/america-s-leading-producer-of-critical-minerals-uranium-1653326)
  - Company inventory uranium rare earths vanadium recylcling. (us$MM) inventory (us$MM) isotopes.At today’s commodity prices, our inventory worth significantly …
- [Wrap sector drives net inflows as platform outflows persist...](https://www.rainmaker.com.au/media-release/wrap-sector-drives-net-inflows-as-platform-outflows-persist)
  - Growth was overwhelmingly led by the wrap sector, while platforms recorded net outflows for a fifth consecutive year, according to Rainmaker Information’s PF…
- [Markets Wrap – Sector movements today](https://www.varchev.com/en/markets-wrap-движенията-на-секторите-днес/)
  - The biggest gains for the day are the Real Estate sectors; Consumer Staples; Utilities; Information Technology. Similarly, the largest losses today are in th…
- [Worldwide Robot Stretch Wrapper Market 2026 - PW Consulting](https://pmarketresearch.com/worldwide-robot-stretch-wrapper-market-research/)
  - The Global Robot Stretch Wrapper Market was valued at USD 540.7 Million in 2025 and is projected to reach USD 892.9 Million by 2032, growing at a CAGR of 7.4%.
- [Wrap-Up From VettaFi’s Q2 Market Outlook Symposium](https://finance.yahoo.com/markets/options/articles/wrap-vettafi-q2-market-outlook-160951420.html)
  - The Q2 Market Outlook Symposium, Defining the Quarter Ahead, held on April 30, 2026, brought together industry leaders to dissect the evolving...
- [2 Under-the-Radar Energy Stocks to Watch for AI Demand in 2026](https://finance.yahoo.com/news/2-under-radar-energy-stocks-123600275.html)
  - Key Points Data center expansion is outpacing grid capacity, creating demand for alternative power...

### Search warnings
- news:WRAP Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers: No results found.
- news:Wrap Technologies, Inc. WRAP outlook OR catalyst OR commodity OR uranium OR rare earth OR vanadium: No results found.
- news:Wrap Technologies, Inc. WRAP backlog OR contract OR refinancing OR leverage: No results found.

## SEC filing [S26]
- Extraction OK: True
- Item 1A chars: 2
- Item 7 chars: 2
- Meta: {'accession_number': '0001140361-26-011401', 'filing_date': '2026-03-26', 'source': 'edgartools', 'path': 'C:\\DevWork\\equity_research_agent\\data\\filings\\WRAP_10k.txt'}

## Qualitative analysis (local LLM)

### Item 1A — Risk Factors
I'm happy to help! However, I don't see any filing excerpt provided. Could you please share the excerpt with me? Once I analyze it, I'll return a concise Markdown summary with short bullet points and 1-2 short quotes highlighting shifts in management tone or competitive dynamics, explicit forward guidance, and counterparty, regulatory, or legal risks.

Please paste the excerpt, and I'll get started!


### Item 7 — MD&A
I apologize, but it seems you didn't provide the filing excerpt. Please share the text, and I'll be happy to analyze it for you!


## Research loop (think → act)

1. _heuristic_ — Coverage looks adequate for this pass; stopping iterative loop.

## Sources

- **[S1]** WRAP fundamentals (yfinance)
  - Wrap Technologies, Inc.: price=1.87, rev=4672000.0, fcf=-10676000.0, shares=55738250.0, rev_cagr=-0.16583178878975358, ROIC=-1.2917904013794426, FCF yield=-0.1024268053213738
- **[S2]** WRAP EV/EBITDA valuation (multiples)
  - Base implied price=143.54686413728453, multiple=8.0
- **[S3]** WRAP DCF valuation (dcf)
  - Base share price=0.05495684193762078, bull=0.17810369957062142, bear=0.02548857573771363
- **[S4]** WRAP peer comps (peers)
  - Peers: ; rows=1
- **[S5]** WRAP earnings history (earnings)
  - rows=12; next=2026-08-13
- **[S6]** WRAP - Wrap Technologies Inc Stock Price Forecast 2025, 2026, 2030 to 2050 - StockScan (web) — https://stockscan.io/stocks/WRAP/forecast
  - The Wrap Technologies Inc (WRAP) stock price forecast for the next 30 days is generally negative, with an average analyst price target of $0.8586, representing a -59.69% decreas…
- **[S7]** Wrap Technologies (WRAP) Stock Forecast, Price Targets and Analysts Predictions - TipRanks.com (web) — https://www.tipranks.com/stocks/wrap/forecast
  - Based on 1 Wall Street analysts offering 12 month price targets for Wrap Technologies in the last 3 months. The average price target is $2.00 with a high forecast of $2.00 and a…
- **[S8]** Wrap Technologies, Inc. Common Stock (WRAP) Analyst Reports & Ratings | Nasdaq (web) — https://www.nasdaq.com/market-activity/stocks/wrap/analyst-research
  - Based on analysts offering 12 month price targets for WRAP in the last 3 months. The average price target is $0.00 with a high estimate of $0.00 and a low estimate of $0.00.
- **[S9]** Wrap Technologies (WRAP) Stock Forecast: Analyst Ratings, Predictions & Price Target 2025 (web) — https://public.com/stocks/wrap/forecast-price-target
  - This rating is provided by third-party analysts and is not investment advice from Public.com. Wall Street analysts have set a price target of $6.55, reflecting a 0.00% increase …
- **[S10]** 6 Wall Street analysts have issued price targets on SpaceX. Here's the one I agree with most. (web) — https://www.msn.com/en-us/money/topstocks/6-wall-street-analysts-have-issued-price-targets-on-spacex-here-s-the-one-i-agree-with-most/ar-AA25Xqw8?ocid=BingNewsVerp
  - Analyst price targets and earnings projections are important because they help set a baseline for a stock. Given SpaceX's valuations, some analysts believe the company is overva…
- **[S11]** SpaceX Shares Fall Below $135 IPO Price For The First Time (web) — https://finance.yahoo.com/markets/stocks/articles/spacex-shares-fall-below-135-170708190.html
  - SpaceX bulls have reportedly noted SpaceX will need to...
- **[S12]** Trump Just Gave a Shoutout to This Top Defense Contractor. Here’s What to Know. (web) — https://finance.yahoo.com/markets/stocks/articles/trump-just-gave-shoutout-top-153405657.html
  - Out of the 24 analysts covering GD stock, 13 recommend “Strong Buy,” 10 recommend “Hold,” and one re...
- **[S13]** Stocks skid to losing week as Chinese AI fears fuel chipmaker rout (web) — https://nypost.com/2026/07/17/business/stocks-skid-to-losing-week-as-chinese-ai-fears-fuel-chipmaker-rout/
  - Iran also said Friday that it targeted US military forces in Syria and Bahrain. Analysts have warned...
- **[S14]** WRAP - Wrap Technologies Inc Stock Price Forecast 2026, 2027, 2030 to 2050 - StockScan (web_page) — https://stockscan.io/stocks/WRAP/forecast
  - WRAP - Wrap Technologies Inc Stock Price Forecast 2026, 2027, 2030 to 2050 - StockScan Stock Screener App Free - Install All Stocks Watchlist NASDAQ NYSE Penny Stocks OTC Crypto…
- **[S15]** Seshaasai Technologies Limited — Institutional Deep Dive (web) — https://seshaasai-technologies.netlify.app/
  - The key industry shift that would change this thesis: a sustained RBI/government push to replace physical payment cards with purely digital (UPI-linked) instruments — not our ba…
- **[S16]** Catalyst Ventures — Institutional-Grade Biotech Investment Intelligence (web) — https://catalyst-ventures.eu/
  - Our analysts author the institutional deep-dives by hand in a frontier-model workbench, grounded in verified FMP data and cross-checked against ClinicalTrials.gov. ... Thesis · …
- **[S17]** Building an Investment Thesis | Street Of Walls (web) — https://www.streetofwalls.com/finance-training-courses/hedge-fund-training/building-an-investment-thesis/
  - If so, what are the catalysts that will cause the Company to beat earnings (e.g., higher revenue, higher margins, lower interest expense, share buybacks, etc.)? Paint the pictur…
- **[S18]** The Curious Case of Catalysts | Behavioural Investment (web) — https://behaviouralinvestment.com/2024/05/01/the-curious-case-of-catalysts/
  - May 14, 2024 - There are two types of investment thesis – one about something that is already performing well, here a catalyst is unnecessary because we just need to extrapolate…
- **[S19]** Uranium - Price - Chart - Historical Data - News (web) — https://tradingeconomics.com/commodity/uranium
  - Uranium rose to 85.45 USD/Lbs on July 16, 2026, up 0.23% from the previous day. Over the past month, Uranium's price has fallen 0.12%, but it is still 19.18% higher than a year …
- **[S20]** WRAP TECHNOLOGIES, INC. SEC 10-Q Report — TradingView News (web) — https://www.tradingview.com/news/tradingview:ad8dc011d6c94:0-wrap-technologies-inc-sec-10-q-report/
  - WRAP TECHNOLOGIES, INC., a leading provider of innovative public safety technologies and services, has released its Form 10-Q report for the third quarter ended September 30, 2025.
- **[S21]** America's Leading Producer of Critical Minerals - Uranium Rare Earth... (web) — https://www.readkong.com/page/america-s-leading-producer-of-critical-minerals-uranium-1653326
  - Company inventory uranium rare earths vanadium recylcling. (us$MM) inventory (us$MM) isotopes.At today’s commodity prices, our inventory worth significantly more. Value on Curre…
- **[S22]** Wrap sector drives net inflows as platform outflows persist... (web) — https://www.rainmaker.com.au/media-release/wrap-sector-drives-net-inflows-as-platform-outflows-persist
  - Growth was overwhelmingly led by the wrap sector, while platforms recorded net outflows for a fifth consecutive year, according to Rainmaker Information’s PFL Managed Funds Repo…
- **[S23]** Seshaasai Technologies Limited — Institutional Deep Dive (web_page) — https://seshaasai-technologies.netlify.app/
  - Seshaasai Technologies Limited — Institutional Deep Dive INSTITUTIONAL EQUITY RESEARCH  |  STYL  |  FY26  |  Generated 2026-05-22 Seshaasai Technologies Limited — Institutional …
- **[S24]** Catalyst Ventures — Institutional-Grade Biotech Investment Intelligence (web_page) — https://catalyst-ventures.eu/
  - Catalyst Ventures — Institutional-Grade Biotech Investment Intelligence Your plan's report limit was reached. Upgrade below to unlock unlimited institutional deep-dives. See pla…
- **[S25]** Building an Investment Thesis | Street Of Walls (web_page) — https://www.streetofwalls.com/finance-training-courses/hedge-fund-training/building-an-investment-thesis/
  - Building an Investment Thesis | Street Of Walls Now that you understand what characteristics make up attractive long and short ideas, it is time to explain how to formulate an i…
- **[S26]** WRAP 10-K (sec)
  - Item 1A chars=2, Item 7 chars=2, ok=True, source=edgartools
- **[S27]** WRAP 8-K 2026-07-13 (sec) — https://www.sec.gov/Archives/edgar/data/1702924/000149315226033073/form8-k.htm
  - 8-K
- **[S28]** WRAP 10-Q 2026-05-13 (sec) — https://www.sec.gov/Archives/edgar/data/1702924/000114036126021091/form10q.htm
  - QUARTERLY REPORT PURSUANT TO SECTION 13 OR 15(D)
- **[S29]** WRAP 8-K 2026-05-13 (sec) — https://www.sec.gov/Archives/edgar/data/1702924/000149315226022738/form8-k.htm
  - 8-K
- **[S30]** WRAP 10-K 2026-03-26 (sec) — https://www.sec.gov/Archives/edgar/data/1702924/000114036126011401/form10k.htm
  - 10-K
- **[S31]** WRAP 8-K 2026-03-26 (sec) — https://www.sec.gov/Archives/edgar/data/1702924/000149315226012909/form8-k.htm
  - 8-K
- **[S32]** WRAP 8-K 2026-02-04 (sec) — https://www.sec.gov/Archives/edgar/data/1702924/000149315226005110/form8-k.htm
  - 8-K
- **[S33]** WRAP 8-K 2025-12-17 (sec) — https://www.sec.gov/Archives/edgar/data/1702924/000149315225028133/form8-k.htm
  - 8-K
- **[S34]** WRAP 10-Q 2025-11-13 (sec) — https://www.sec.gov/Archives/edgar/data/1702924/000114036125041816/form10q.htm
  - QUARTERLY REPORT PURSUANT TO SECTION 13 OR 15(D)
- **[S35]** Item 1A summary (nlp)
  - ### Item 1A — Risk Factors I'm happy to help! However, I don't see any filing excerpt provided. Could you please share the excerpt with me? Once I analyze it, I'll return a conc…
- **[S36]** Item 7 summary (nlp)
  - ### Item 7 — MD&A I apologize, but it seems you didn't provide the filing excerpt. Please share the text, and I'll be happy to analyze it for you! 
- **[S37]** WRAP driver analysis (drivers)
  - ok=True; drivers=7
- **[S38]** WRAP memo sections (memo)
  - mode=rules; proxies=5

## Self-critique

_Automated review (heuristic)._

### Strengths
- Combines local fundamentals, optional DCF scenarios, and cited sources where available.
- Keeps a non-advisory framing for local research drafts.

### Issues & gaps
- Base-case implies deep downside vs spot (<-70%); confirm whether near-term FCF normalization is appropriate for this business.
- Draft uses strong recommendation language; this local agent should stay descriptive, not advisory.

### Caution for readers
- Treat scenario prices as sensitivity output, not a forecast.
- Re-check primary filings and fresh market data before any decision.



---

# Template: Valuation (DCF + Street + drivers) (`valuation`)

# WRAP — Planned Research Report

> Not investment advice. Local research draft only.

**Goal:** Estimate intrinsic value under base / bull / bear scenarios
**Mode:** deep
**Template:** valuation
**Planner:** template

## Plan executed

- **(1) Financial statements & key metrics** (`fundamentals`): get_fundamentals
  - Revenue, free cash flow, shares outstanding, historical growth rates, margins and leverage. Focus: Estimate intrinsic value under base / bull / bear scenarios
- **(2) DCF assumptions & intrinsic value** (`valuation`): run_dcf
  - Establish growth, operating/FCF margins, and WACC; run base / bull / bear share-price scenarios from the assumption pack
- **(2b) EV/EBITDA priced-in scenarios** (`multiples`): run_ev_ebitda
  - Cross-check DCF with EBITDA × multiple scenarios
- **(3) Analyst reports & Street targets** (`web_analysts`): search_web
  - Consensus targets, ratings, and investment theses from public web sources
- **(4) Market & commodity drivers** (`web_drivers`): search_web
  - Sector/commodity drivers that inform bull/bear assumptions (prices, demand, expansion)
- **(5a) SEC 10-K intake** (`sec_fetch`): fetch_10k
  - Latest 10-K for risk and MD&A context behind the valuation
- **(5b) Risk factors (Item 1A)** (`risks`): summarize_item_1a
  - Key risks that should stress the bear case
- **(5c) MD&A (Item 7)** (`mda`): summarize_item_7
  - Management tone, guidance, and operational cues for scenarios

## Fundamentals [S1]
- Company: Wrap Technologies, Inc.
- Sector / industry: Technology / Scientific & Technical Instruments
- Price: 1.87
- 52-week range: $1.04 – $3.23
- Market cap: $104.23M
- Enterprise value: $97.43M
- Shares outstanding: 55.74M
- Beta: 1.368
- Book equity: $11.49M
- Revenue (latest): $4.67M
- EBITDA (latest): -$12.89M
- Free cash flow (latest): -$10.68M
- Operating income: -$13.48M
- Operating margin: -288.6%
- EV / EBITDA: -7.6x
- ROIC: -129.2%
- FCF yield: -10.2%
- Debt / Equity: 0.2103568320278503
- FCF / share: -$0.19
- Revenue / share: $0.08

### Capital structure
- Cash: $3.47M
- Short-term debt: $320.00K
- Long-term debt: $2.10M
- Total debt: $2.42M
- Net debt: -$1.05M
- Net debt / EBITDA: 0.1x

### Growth
- Revenue CAGR: -16.6%
- FCF CAGR: —
- Latest revenue YoY: 3.7%
- Latest FCF YoY: -28.7%

### Market expectations (yfinance, sparse)
- Mean target: —
- Target range: — – —
- Recommendation: none

_Consensus revenue/EBITDA forecasts are often unavailable via free feeds; treat targets as point-in-time only._

### Historical KPIs (multi-year)

| Year | Revenue | OCF | Capex | FCF | EBITDA | LT debt | Cash | Net debt | Net income |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2025 | $4.67M | -$10.29M | $387.00K | -$10.68M | -$12.89M | $2.42M | $3.47M | -$1.05M | -$10.34M |
| 2024 | $4.51M | -$8.12M | $168.00K | -$8.29M | -$14.74M | $2.20M | $3.61M | -$1.41M | -$5.88M |
| 2023 | $6.13M | -$16.70M | $623.00K | -$17.33M | -$17.90M | $2.29M | $3.96M | -$1.67M | -$30.22M |
| 2022 | $8.05M | -$14.60M | $1.13M | -$15.73M | -$16.97M | $301.00K | $5.33M | -$5.03M | -$17.62M |

## Charts

### Revenue & FCF history
![Revenue & FCF history](/charts/WRAP_valuation_revenue_fcf.png)

### DCF scenario prices
![DCF scenario prices](/charts/WRAP_valuation_dcf_scenarios.png)

### Base-case FCF path
![Base-case FCF path](/charts/WRAP_valuation_base_fcf_path.png)

### EV/EBITDA scenario prices
![EV/EBITDA scenario prices](/charts/WRAP_valuation_ev_ebitda_scenarios.png)

## DCF valuation (base / bull / bear) [S2]

> Simplified revenue->FCF DCF. Not investment advice; assumptions are editable heuristics.

- Spot price: $1.87
- Base revenue: $4.67M
- Shares: 55,738,250
- Net debt (Debt−Cash): -$1.05M

| Scenario | Growth | FCF margin | WACC | Term. g | Equity value | Share price | Upside |
|----------|--------|------------|------|---------|--------------|-------------|--------|
| bear | -3.3% | 1.0% | 12.0% | 1.5% | $1.42M | $0.03 | -98.6% |
| base | 3.7% | 3.0% | 10.0% | 2.5% | $3.06M | $0.05 | -97.1% |
| bull | 10.7% | 8.0% | 9.0% | 3.0% | $9.93M | $0.18 | -90.5% |

### Assumption notes
- Base revenue growth seeded from historical rate (3.7%).
- Latest FCF margin was -228.5%; scenarios use normalized positive margins for a going-concern DCF.


### Base-case projected FCF

- Year 1: revenue $4.84M, FCF $145,291 (PV $132,083)
- Year 2: revenue $5.02M, FCF $150,610 (PV $124,471)
- Year 3: revenue $5.20M, FCF $156,124 (PV $117,298)
- Year 4: revenue $5.39M, FCF $161,840 (PV $110,539)
- Year 5: revenue $5.59M, FCF $167,765 (PV $104,169)
- Terminal value $2.29M (PV $1.42M)

## Valuation — EV/EBITDA scenarios [S3]

> Priced-in model: implied price = (EBITDA × EV/EBITDA − net debt) ÷ shares. Not a forecast.

- Spot: $1.87
- Net debt used: -$1.05M

| Scenario | EBITDA | EV/EBITDA | Implied EV | Equity value | Implied price |
|---|---:|---:|---:|---:|---:|
| bear | $700.00M | 6.0x | $4.20B | $4.20B | $75.37 |
| base | $1.00B | 8.0x | $8.00B | $8.00B | $143.55 |
| bull | $1.20B | 10.0x | $12.00B | $12.00B | $215.31 |

- EBITDA missing or non-positive; scenarios use placeholder $1B EBITDA — edit before relying on prices.
- No current EV/EBITDA; defaulted base multiple to 8.0x.

## Web research — web_analysts

- Queries: WRAP analyst price target, Wrap Technologies, Inc. stock rating OR consensus OR upgrade OR downgrade, WRAP Estimate intrinsic value under base / bull / bear scenarios analyst
- Unique hits: 13
- Pages fetched: 1/3

### Web synthesis — web_analysts (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, revenue, margin

- Analyst price targets are skyrocketing | MSN | https://www.msn.com/en-us/money/topstocks/amd-just-blew-out-earnings-and-wall-street-can-t-get-enough-analyst-price-targets-are-skyrocketing/ar-AA22wTc7?ocid=BingNewsVerp
AMD is continuing to see tremendous revenue growth in its data center division.
- The Score for WRAP is 31, which is 38% below its historic median score of 50, and infers higher risk than normal.
- | www.benzinga.com | https://www.benzinga.com/analyst-ratings/analyst-color/21/07/22022104/5-chemical-stocks-get-mixed-reaction-which-ones-got-an-upgrade-or-downgrade
The risk-reward balance may be unfavorable for chemical stocks heading into second-quarter earnings season, and one analyst adjusted his chemical stock ratings accordingly on Friday.Dow Inc (NYSE:DOW) downgraded from Neutral to Underperform, price target cut from $71 to $68.
- Here’s a step-by-step guide

[HIT] Intrinsic Value & Margin of Safety: Mr.
- | ValueMarkers | valuemarkers.com | https://valuemarkers.com/academy/intrinsic-value-margin-safety
(a) Estimate intrinsic value using a range (bull, base, bear).
- Margin of safety.
- Originally founded in 2018, Wrap Technologies has designed its product line to address de-escalation and risk mitigation in high-tension encounters.

### Sources found
- [Wrap Technologies WRAP - Analyst Price Targets... | AnaChart](https://anachart.com/ticker/wrap/)
  - Wrap Technologies(WRAP) on AnaChart.Avg target: $4.24. View analyst ratings, accuracy scores & price target history. Advanced plan from $45/mo.Previous price…
- [Wrap Technologies (WRTC) Stock Price, News & Analysis](https://www.marketbeat.com/stocks/OTCMKTS/WRTC/)
  - Should You Buy or Sell Wrap Technologies Stock? Get The Latest WRTC Stock Analysis, Price Target, Earnings Estimates, and Headlines at MarketBeat.
- [WRAP | Wrap Technologies Inc. Analyst Estimates | MarketWatch](https://www.marketwatch.com/investing/stock/wrap/analystestimates)
  - WRAP Analyst Estimates. Snapshot. Average Recommendation. Hold. Average Target Price. 2.50. Number Of Ratings.
- [Wrap Technologies, Inc. Common Stock (WRAP) Analyst... | Nasdaq](https://www.nasdaq.com/market-activity/stocks/wrap/analyst-research)
  - Based on analysts offering 12 month price targets for WRAP in the last 3 months. The average price target is $0.00 with a high estimate of $0.00 and a low es…
- [AMD just blew out earnings -- and Wall Street can't get enough. Analyst price targets are skyrocketing](https://www.msn.com/en-us/money/topstocks/amd-just-blew-out-earnings-and-wall-street-can-t-get-enough-analyst-price-targets-are-skyrocketing/ar-AA22wTc7?ocid=BingNewsVerp)
  - AMD is continuing to see tremendous revenue growth in its data center division. The growth in agentic artificial intelligence is driving increased demand for…
- [Yahoo Finance - Stock Market Live, Quotes, Business & Finance News](https://finance.yahoo.com/)
  - At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage rate…
- [PLTR Stock Price | Palantir Technologies Inc. Stock... | MarketWatch](https://www.marketwatch.com/investing/stock/pltr)
  - PLTR | Complete Palantir Technologies Inc. stock news by MarketWatch. View real-time stock prices and stock quotes for a full financial overview.
- [Where will Wrap Technologies, Inc. Stock Be In 1 Year? – Financhill](https://financhill.com/stock-forecast/wrap-stock-prediction)
  - The current Wrap Technologies, Inc. [WRAP] share price is $1.52. The Score for WRAP is 31, which is 38% below its historic median score of 50, and infers hig…
- [5 Chemical Stocks Get Mixed Reaction: Which Ones Got An Upgrade...](https://www.benzinga.com/analyst-ratings/analyst-color/21/07/22022104/5-chemical-stocks-get-mixed-reaction-which-ones-got-an-upgrade-or-downgrade)
  - The risk-reward balance may be unfavorable for chemical stocks heading into second-quarter earnings season, and one analyst adjusted his chemical stock ratin…
- [investopedia.com/insights/digging-deeper-bull-and-bear-markets](https://www.investopedia.com/insights/digging-deeper-bull-and-bear-markets/)
  - A bull market is favorable and rises in value, while a bear declines.
- [[FREE] How would I go about calculating intrinsic values... - brainly.com](https://brainly.com/question/32942382)
  - To calculate intrinsic values for the bullish and bearish scenarios, you need to apply discounted cash flow (DCF) analysis. This method estimates the intrins…
- [Intrinsic Value & Margin of Safety: Mr. | ValueMarkers](https://valuemarkers.com/academy/intrinsic-value-margin-safety)
  - (a) Estimate intrinsic value using a range (bull, base, bear). (b) Current market price.Self-Practice 1: Write down three stocks you own or track. For each, …

### Search warnings
- news:Wrap Technologies, Inc. stock rating OR consensus OR upgrade OR downgrade: No results found.
- news:WRAP Estimate intrinsic value under base / bull / bear scenarios analyst: No results found.

## Web research — web_drivers

- Queries: WRAP Estimate intrinsic value under base / bull / bear scenarios, Wrap Technologies, Inc. WRAP outlook OR catalyst OR commodity OR uranium OR rare earth OR vanadium, WRAP sector drivers OR market demand
- Unique hits: 15
- Pages fetched: 1/3

### Web synthesis — web_drivers (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, margin, interest rate

- [HIT] Intrinsic Value & Margin of Safety: Mr.
- | ValueMarkers | valuemarkers.com | https://valuemarkers.com/academy/intrinsic-value-margin-safety
Intrinsic value estimate (Bear): $700B (5% growth, 25% margins, 10% discount).
- Margin of safety.
- [HIT] Rare Earth Archives - MINING.COM | www.mining.com | https://www.mining.com/commodity/rare-earth/
AI emerges as new driver of rare earth demand, Sprott says AI is fueling new rare earth demand as data centers, defense and clean energy expose supply-chain risks amid China’s dominance.
- Bull and Bear Market Name Origin
How to Invest in Bear Markets
Where Bear Investors Put Their Money
Bear Markets and Your 401(k)
Protecting Retirement Money
Surviving A Market Downturn
Warren Buffett's Bear Market Maneuvers
Don't Sell After a Market Downturn
Adapt To A Bear Market
Profiting in Bull and Bear Markets
Bear Market Risks and Considerations
Bear Market Rally
4 Ways to Survive and Prosper in a Bear Market
Bear Trap Definition
Bloomberg / Getty Images
Close
Key Takeaways
A bull market occurs when stock prices rise continuously over time, typically alongside strong economic growth and high employment levels.
- Rising stock prices during bull markets are often driven by strong company earnings, low interest rates, and optimistic investor sentiment.

### Sources found
- [Intrinsic Value & Margin of Safety: Mr. | ValueMarkers](https://valuemarkers.com/academy/intrinsic-value-margin-safety)
  - Intrinsic value estimate (Bear): $700B (5% growth, 25% margins, 10% discount). Market was in Bull territory.Self-Practice 1: Write down three stocks you own …
- [investopedia.com/insights/digging-deeper-bull-and-bear-markets](https://www.investopedia.com/insights/digging-deeper-bull-and-bear-markets/)
  - A bull market is favorable and rises in value, while a bear declines.
- [[FREE] How would I go about calculating intrinsic values... - brainly.com](https://brainly.com/question/32942382)
  - To calculate intrinsic values for the bullish and bearish scenarios, you need to apply discounted cash flow (DCF) analysis. This method estimates the intrins…
- [Is Adobe's Share Price Slide Creating an Opportunity for Investors in 2025?](https://finance.yahoo.com/news/adobes-share-price-slide-creating-100826929.html)
  - Thinking about what to do with Adobe stock? You are not alone. Whether you are considering doubling ...
- [Rare Earth Archives - MINING.COM](https://www.mining.com/commodity/rare-earth/)
  - AI emerges as new driver of rare earth demand, Sprott says AI is fueling new rare earth demand as data centers, defense and clean energy expose supply-chain …
- [Energy Fuels - Uranium, Rare Earths & Critical Minerals](https://www.energyfuels.com/)
  - American producer of uranium for the nuclear fuel cycle, rare earth oxides and critical minerals, operating the only U.S. conventional uranium mill. The comp…
- [Rare earth elements 2025 – Analysis - IEA](https://www.iea.org/reports/rare-earth-elements-2025)
  - Rare earth elements 2025 - Analysis and key findings. A report by the International Energy Agency.
- [Mineral commodity summaries 2024 | U.S. Geological Survey](https://www.usgs.gov/publications/mineral-commodity-summaries-2024)
  - Each mineral commodity chapter of the 2024 edition of the U.S. Geological Survey (USGS) Mineral Commodity Summaries (MCS) includes information on events, tre…
- [Wrap sector drives net inflows as platform outflows persist...](https://www.rainmaker.com.au/media-release/wrap-sector-drives-net-inflows-as-platform-outflows-persist)
  - Growth was overwhelmingly led by the wrap sector, while platforms recorded net outflows for a fifth consecutive year, according to Rainmaker Information’s PF…
- [Markets Wrap – Sector movements today](https://www.varchev.com/en/markets-wrap-движенията-на-секторите-днес/)
  - The biggest gains for the day are the Real Estate sectors; Consumer Staples; Utilities; Information Technology. Similarly, the largest losses today are in th…
- [Latest Stock Market News & Analysis | INN](https://investingnews.com/)
  - Crypto Market Update: Over US$3.8 Billion Cumulative Loss For Trump Memecoin Investors. Meagen Seatter. Giann Liguid.
- [Wrap-Up From VettaFi’s Q2 Market Outlook Symposium](https://finance.yahoo.com/markets/options/articles/wrap-vettafi-q2-market-outlook-160951420.html)
  - The Q2 Market Outlook Symposium, Defining the Quarter Ahead, held on April 30, 2026, brought together industry leaders to dissect the evolving...

### Search warnings
- news:Wrap Technologies, Inc. WRAP outlook OR catalyst OR commodity OR uranium OR rare earth OR vanadium: No results found.

## SEC filing [S22]
- Extraction OK: True
- Item 1A chars: 2
- Item 7 chars: 2
- Meta: {'source': 'cache', 'path': 'C:\\DevWork\\equity_research_agent\\data\\filings\\WRAP_10k.txt'}

## Qualitative analysis (local LLM)

### Item 1A — Risk Factors
I'm happy to help! However, I don't see any text excerpted below. Please provide the filing excerpt, and I'll be happy to analyze it for you.

Once I receive the excerpt, I'll return a concise Markdown summary with short bullet points and 1-2 short quotes highlighting:

* Shifts in management tone or competitive dynamics
* Explicit forward guidance (capex, growth, margins)
* Counterparty, regulatory, or legal risks


### Item 7 — MD&A
I'm happy to help! However, I don't see any text excerpted. Please provide the filing excerpt you'd like me to analyze, and I'll do my best to summarize it for you in Markdown format with short bullet points and 1-2 short quotes.

Once I receive the excerpt, I'll focus on identifying shifts in management tone or competitive dynamics, explicit forward guidance (capex, growth, margins), and counterparty, regulatory, or legal risks.


## Research loop (think → act)

1. _heuristic_ — Coverage looks adequate for this pass; stopping iterative loop.

## Sources

- **[S1]** WRAP fundamentals (yfinance)
  - Wrap Technologies, Inc.: price=1.87, rev=4672000.0, fcf=-10676000.0, shares=55738250.0, rev_cagr=-0.16583178878975358, ROIC=-1.2917904013794426, FCF yield=-0.1024268053213738
- **[S2]** WRAP DCF valuation (dcf)
  - Base share price=0.05495684193762078, bull=0.17810369957062142, bear=0.02548857573771363
- **[S3]** WRAP EV/EBITDA valuation (multiples)
  - Base implied price=143.54686413728453, multiple=8.0
- **[S4]** Wrap Technologies WRAP - Analyst Price Targets... | AnaChart (web) — https://anachart.com/ticker/wrap/
  - Wrap Technologies(WRAP) on AnaChart.Avg target: $4.24. View analyst ratings, accuracy scores & price target history. Advanced plan from $45/mo.Previous price target. Date of las…
- **[S5]** Wrap Technologies (WRTC) Stock Price, News & Analysis (web) — https://www.marketbeat.com/stocks/OTCMKTS/WRTC/
  - Should You Buy or Sell Wrap Technologies Stock? Get The Latest WRTC Stock Analysis, Price Target, Earnings Estimates, and Headlines at MarketBeat.
- **[S6]** WRAP | Wrap Technologies Inc. Analyst Estimates | MarketWatch (web) — https://www.marketwatch.com/investing/stock/wrap/analystestimates
  - WRAP Analyst Estimates. Snapshot. Average Recommendation. Hold. Average Target Price. 2.50. Number Of Ratings.
- **[S7]** Wrap Technologies, Inc. Common Stock (WRAP) Analyst... | Nasdaq (web) — https://www.nasdaq.com/market-activity/stocks/wrap/analyst-research
  - Based on analysts offering 12 month price targets for WRAP in the last 3 months. The average price target is $0.00 with a high estimate of $0.00 and a low estimate of $0.00.
- **[S8]** AMD just blew out earnings -- and Wall Street can't get enough. Analyst price targets are skyrocketing (web) — https://www.msn.com/en-us/money/topstocks/amd-just-blew-out-earnings-and-wall-street-can-t-get-enough-analyst-price-targets-are-skyrocketing/ar-AA22wTc7?ocid=BingNewsVerp
  - AMD is continuing to see tremendous revenue growth in its data center division. The growth in agentic artificial intelligence is driving increased demand for central processing …
- **[S9]** Yahoo Finance - Stock Market Live, Quotes, Business & Finance News (web) — https://finance.yahoo.com/
  - At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage rates that help you mana…
- **[S10]** PLTR Stock Price | Palantir Technologies Inc. Stock... | MarketWatch (web) — https://www.marketwatch.com/investing/stock/pltr
  - PLTR | Complete Palantir Technologies Inc. stock news by MarketWatch. View real-time stock prices and stock quotes for a full financial overview.
- **[S11]** Where will Wrap Technologies, Inc. Stock Be In 1 Year? – Financhill (web) — https://financhill.com/stock-forecast/wrap-stock-prediction
  - The current Wrap Technologies, Inc. [WRAP] share price is $1.52. The Score for WRAP is 31, which is 38% below its historic median score of 50, and infers higher risk than normal…
- **[S12]** Wrap Technologies (WRTC) Stock Price, News & Analysis (web_page) — https://www.marketbeat.com/stocks/OTCMKTS/WRTC/
  - Wrap Technologies (WRTC) Stock Price, News & Analysis Skip to main content → Not oil. Not solar. Bigger. (From Behind the Markets) (Ad) Free WRTC Stock Alerts OTCMKTS:WRTC Wrap …
- **[S13]** Intrinsic Value & Margin of Safety: Mr. | ValueMarkers (web) — https://valuemarkers.com/academy/intrinsic-value-margin-safety
  - Intrinsic value estimate (Bear): $700B (5% growth, 25% margins, 10% discount). Market was in Bull territory.Self-Practice 1: Write down three stocks you own or track. For each, …
- **[S14]** investopedia.com/insights/digging-deeper-bull-and-bear-markets (web) — https://www.investopedia.com/insights/digging-deeper-bull-and-bear-markets/
  - A bull market is favorable and rises in value, while a bear declines.
- **[S15]** [FREE] How would I go about calculating intrinsic values... - brainly.com (web) — https://brainly.com/question/32942382
  - To calculate intrinsic values for the bullish and bearish scenarios, you need to apply discounted cash flow (DCF) analysis. This method estimates the intrinsic value of an inves…
- **[S16]** Is Adobe's Share Price Slide Creating an Opportunity for Investors in 2025? (web) — https://finance.yahoo.com/news/adobes-share-price-slide-creating-100826929.html
  - Thinking about what to do with Adobe stock? You are not alone. Whether you are considering doubling ...
- **[S17]** Rare Earth Archives - MINING.COM (web) — https://www.mining.com/commodity/rare-earth/
  - AI emerges as new driver of rare earth demand, Sprott says AI is fueling new rare earth demand as data centers, defense and clean energy expose supply-chain risks amid China’s d…
- **[S18]** Energy Fuels - Uranium, Rare Earths & Critical Minerals (web) — https://www.energyfuels.com/
  - American producer of uranium for the nuclear fuel cycle, rare earth oxides and critical minerals, operating the only U.S. conventional uranium mill. The company has begun commer…
- **[S19]** Rare earth elements 2025 – Analysis - IEA (web) — https://www.iea.org/reports/rare-earth-elements-2025
  - Rare earth elements 2025 - Analysis and key findings. A report by the International Energy Agency.
- **[S20]** Mineral commodity summaries 2024 | U.S. Geological Survey (web) — https://www.usgs.gov/publications/mineral-commodity-summaries-2024
  - Each mineral commodity chapter of the 2024 edition of the U.S. Geological Survey (USGS) Mineral Commodity Summaries (MCS) includes information on events, trends, and issues for …
- **[S21]** Bull vs. Bear Markets: What's the Difference? (web_page) — https://www.investopedia.com/insights/digging-deeper-bull-and-bear-markets/
  - Bull vs. Bear Markets: What's the Difference? ​ Table of Contents Expand Table of Contents Overview Bull Markets How to Invest in Bull Markets Bear Markets How to Invest During …
- **[S22]** WRAP 10-K (sec)
  - Item 1A chars=2, Item 7 chars=2, ok=True, source=cache
- **[S23]** Item 1A summary (nlp)
  - ### Item 1A — Risk Factors I'm happy to help! However, I don't see any text excerpted below. Please provide the filing excerpt, and I'll be happy to analyze it for you.  Once I …
- **[S24]** Item 7 summary (nlp)
  - ### Item 7 — MD&A I'm happy to help! However, I don't see any text excerpted. Please provide the filing excerpt you'd like me to analyze, and I'll do my best to summarize it for…

## Self-critique

_Automated review (heuristic)._

### Strengths
- Combines local fundamentals, optional DCF scenarios, and cited sources where available.
- Keeps a non-advisory framing for local research drafts.

### Issues & gaps
- Base-case implies deep downside vs spot (<-70%); confirm whether near-term FCF normalization is appropriate for this business.

### Caution for readers
- Treat scenario prices as sensitivity output, not a forecast.
- Re-check primary filings and fresh market data before any decision.



---

# Template: Full diligence (`deep`)

# WRAP — Planned Research Report

> Not investment advice. Local research draft only.

**Goal:** Deep diligence: fundamentals, DCF, web, 10-K risks & MD&A
**Mode:** deep
**Template:** deep
**Planner:** template

## Plan executed

- **Fundamentals & ratios** (`fundamentals`): get_fundamentals
  - Revenue, FCF, shares, growth rates, ROIC, FCF yield, debt/equity. Focus: Deep diligence: fundamentals, DCF, web, 10-K risks & MD&A
- **DCF valuation (base / bull / bear)** (`valuation`): run_dcf
  - Intrinsic value from growth, FCF margin, and WACC assumptions. Focus: Deep diligence: fundamentals, DCF, web, 10-K risks & MD&A
- **Put income screen** (`options`): screen_puts
  - ~30–60 DTE OTM puts targeting ~10–15% annualized premium
- **News, analysts & market drivers** (`web_research`): search_web
  - Street targets, recent news, sector/commodity drivers via web search + page fetch. Focus: Deep diligence: fundamentals, DCF, web, 10-K risks & MD&A
- **SEC 10-K intake** (`sec_fetch`): fetch_10k
  - Latest 10-K; extract Item 1A and Item 7
- **Risk factors (Item 1A)** (`risks`): summarize_item_1a
  - Qualitative risks from the filing
- **MD&A (Item 7)** (`mda`): summarize_item_7
  - Management discussion, tone, guidance cues

## Fundamentals [S1]
- Company: Wrap Technologies, Inc.
- Sector / industry: Technology / Scientific & Technical Instruments
- Price: 1.87
- 52-week range: $1.04 – $3.23
- Market cap: $104.23M
- Enterprise value: $97.43M
- Shares outstanding: 55.74M
- Beta: 1.368
- Book equity: $11.49M
- Revenue (latest): $4.67M
- EBITDA (latest): -$12.89M
- Free cash flow (latest): -$10.68M
- Operating income: -$13.48M
- Operating margin: -288.6%
- EV / EBITDA: -7.6x
- ROIC: -129.2%
- FCF yield: -10.2%
- Debt / Equity: 0.2103568320278503
- FCF / share: -$0.19
- Revenue / share: $0.08

### Capital structure
- Cash: $3.47M
- Short-term debt: $320.00K
- Long-term debt: $2.10M
- Total debt: $2.42M
- Net debt: -$1.05M
- Net debt / EBITDA: 0.1x

### Growth
- Revenue CAGR: -16.6%
- FCF CAGR: —
- Latest revenue YoY: 3.7%
- Latest FCF YoY: -28.7%

### Market expectations (yfinance, sparse)
- Mean target: —
- Target range: — – —
- Recommendation: none

_Consensus revenue/EBITDA forecasts are often unavailable via free feeds; treat targets as point-in-time only._

### Historical KPIs (multi-year)

| Year | Revenue | OCF | Capex | FCF | EBITDA | LT debt | Cash | Net debt | Net income |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2025 | $4.67M | -$10.29M | $387.00K | -$10.68M | -$12.89M | $2.42M | $3.47M | -$1.05M | -$10.34M |
| 2024 | $4.51M | -$8.12M | $168.00K | -$8.29M | -$14.74M | $2.20M | $3.61M | -$1.41M | -$5.88M |
| 2023 | $6.13M | -$16.70M | $623.00K | -$17.33M | -$17.90M | $2.29M | $3.96M | -$1.67M | -$30.22M |
| 2022 | $8.05M | -$14.60M | $1.13M | -$15.73M | -$16.97M | $301.00K | $5.33M | -$5.03M | -$17.62M |

## Charts

### Revenue & FCF history
![Revenue & FCF history](/charts/WRAP_deep_revenue_fcf.png)

### DCF scenario prices
![DCF scenario prices](/charts/WRAP_deep_dcf_scenarios.png)

### Base-case FCF path
![Base-case FCF path](/charts/WRAP_deep_base_fcf_path.png)

## DCF valuation (base / bull / bear) [S2]

> Simplified revenue->FCF DCF. Not investment advice; assumptions are editable heuristics.

- Spot price: $1.87
- Base revenue: $4.67M
- Shares: 55,738,250
- Net debt (Debt−Cash): -$1.05M

| Scenario | Growth | FCF margin | WACC | Term. g | Equity value | Share price | Upside |
|----------|--------|------------|------|---------|--------------|-------------|--------|
| bear | -3.3% | 1.0% | 12.0% | 1.5% | $1.42M | $0.03 | -98.6% |
| base | 3.7% | 3.0% | 10.0% | 2.5% | $3.06M | $0.05 | -97.1% |
| bull | 10.7% | 8.0% | 9.0% | 3.0% | $9.93M | $0.18 | -90.5% |

### Assumption notes
- Base revenue growth seeded from historical rate (3.7%).
- Latest FCF margin was -228.5%; scenarios use normalized positive margins for a going-concern DCF.


### Base-case projected FCF

- Year 1: revenue $4.84M, FCF $145,291 (PV $132,083)
- Year 2: revenue $5.02M, FCF $150,610 (PV $124,471)
- Year 3: revenue $5.20M, FCF $156,124 (PV $117,298)
- Year 4: revenue $5.39M, FCF $161,840 (PV $110,539)
- Year 5: revenue $5.59M, FCF $167,765 (PV $104,169)
- Terminal value $2.29M (PV $1.42M)

## Web research — web_research

- Queries: Deep diligence: fundamentals, DCF, web, 10-K risks & MD&A
- Unique hits: 3
- Pages fetched: 2/3

### Web synthesis — web_research (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, litigation, revenue, margin

- [HIT] The future of due diligence - kpmg.com | kpmg.com | https://kpmg.com/xx/en/our-insights/value-creation/the-future-of-due-diligence.html
It also explores the required capabilities and tools, including advanced data analytics and technologies, deep sector specialization and access to value driver trees, to deliver deeper, more expansive insights into a deal’s risks and opportunities.
- For investors, these documents provide a detailed account of financial data, risks, and management’s perspective, all essential for performing in-depth due diligence.
- Company Deep Dive
Trigger phrases:
"deep dive on [ticker]"
,
"research [company]"
,
"investment overview of..."
Pulls together a full investment-ready snapshot:
Real-time price and key market stats via Financial Datasets MCP
Recent news, press releases, and market narrative via Exa MCP
Core fundamentals — revenue, margins, P/E, EV/EBITDA, debt levels
Insider trading activity (net buys vs.
- sells, recent filings)
Analyst estimates, consensus ratings, and price targets
Synthesized bull case, bear case, and key risk summary
2.
- Due Diligence
Trigger phrases:
"due diligence on [company]"
,
"DD on [ticker]"
,
"red flags for..."
Everything in the Company Deep Dive, plus:
Litigation and regulatory search: SEC investigations, lawsuits, consent orders
Accounting integrity checks: restatements, auditor resignations, material weaknesses
Management background research: prior roles, track record, controversies
Short interest and institutional ownership trends
Structured risk and catalyst identifica

[PAGE] The future of due diligence | https://kpmg.com/xx/en/our-insights/value-creation/the-future-of-due-diligence.html
The future of due diligence
The future of due diligence
Sustainable deal value comes from a deeper, more expansive look at a deal’s risks and value opportunities
Share
Traditional due diligence likely isn’t enough for today’s deal.
- Restricting due diligence to a business’ financial matters, could expose dealmakers to unforeseen risks.
- In this point of view, KPMG professionals share a more complete view of due diligence that considers a wider aperture of risks and identifies performance improvements to help deliver a deal’s longer-term value potentials.
- It also explores the required capabilities and tools, including advanced data analytics and technologies, deep sector specialization and access to value driver trees, to deliver deeper, more expansive insights into a deal’s risks and opportunities.

### Sources found
- [GitHub - Lunatic16/deep-financial-research: A Claude/Qwen ...](https://github.com/Lunatic16/deep-financial-research)
  - This skill gives Claude access to real-time financial data and neural web search, enabling research workflows that typically require Bloomberg terminals, fin…
- [The future of due diligence - kpmg.com](https://kpmg.com/xx/en/our-insights/value-creation/the-future-of-due-diligence.html)
  - It also explores the required capabilities and tools, including advanced data analytics and technologies, deep sector specialization and access to value driv…
- [A Deep Dive Into Understanding 10K Reports - eFinancialModels](https://www.efinancialmodels.com/a-deep-dive-into-understanding-10k-reports/)
  - The importance of a 10K financial report cannot be overstated. For investors, these documents provide a detailed account of financial data, risks, and manage…

### Search warnings
- news:Deep diligence: fundamentals, DCF, web, 10-K risks & MD&A: No results found.

## Put opportunities (heuristic) [S3]
- Expiration: 2026-08-21 (DTE 32)
- Candidates: 0
- ATM IV (est.): 156.3%
- IV rank: — (1 local samples)
- HV rank (20d realized): 100.0%


_Note: Delta band approximated via % OTM when greeks are unavailable; IV rank needs ~20+ local daily IV samples (have 1); run the options screen over time to build history.; HV rank is realized-vol rank (20d HV vs ~1y); useful when IV history is thin._

## SEC filing [S9]
- Extraction OK: True
- Item 1A chars: 2
- Item 7 chars: 2
- Meta: {'source': 'cache', 'path': 'C:\\DevWork\\equity_research_agent\\data\\filings\\WRAP_10k.txt'}

## Qualitative analysis (local LLM)

### Item 1A — Risk Factors
I'm happy to help! However, I don't see any text excerpted below. Please provide the filing excerpt, and I'll be happy to analyze it for you.

Once I receive the excerpt, I'll return a concise Markdown summary with short bullet points and 1-2 short quotes highlighting:

* Shifts in management tone or competitive dynamics
* Explicit forward guidance (capex, growth, margins)
* Counterparty, regulatory, or legal risks

Please provide the excerpt, and I'll get started!


### Item 7 — MD&A
I apologize, but it seems you didn't provide the filing excerpt. Please share the text, and I'll be happy to analyze it for you!


## Research loop (think → act)

1. _heuristic_ — Coverage looks adequate for this pass; stopping iterative loop.

## Sources

- **[S1]** WRAP fundamentals (yfinance)
  - Wrap Technologies, Inc.: price=1.87, rev=4672000.0, fcf=-10676000.0, shares=55738250.0, rev_cagr=-0.16583178878975358, ROIC=-1.2917904013794426, FCF yield=-0.1024268053213738
- **[S2]** WRAP DCF valuation (dcf)
  - Base share price=0.05495684193762078, bull=0.17810369957062142, bear=0.02548857573771363
- **[S3]** WRAP put screen (yfinance_options)
  - Expiration 2026-08-21 (DTE 32): 0 candidates; IV=1.5625021874999998, IV rank=None, HV rank=1.0. Delta band approximated via % OTM when greeks are unavailable; IV rank needs ~20+…
- **[S4]** GitHub - Lunatic16/deep-financial-research: A Claude/Qwen ... (web) — https://github.com/Lunatic16/deep-financial-research
  - This skill gives Claude access to real-time financial data and neural web search, enabling research workflows that typically require Bloomberg terminals, financial databases, an…
- **[S5]** The future of due diligence - kpmg.com (web) — https://kpmg.com/xx/en/our-insights/value-creation/the-future-of-due-diligence.html
  - It also explores the required capabilities and tools, including advanced data analytics and technologies, deep sector specialization and access to value driver trees, to deliver…
- **[S6]** A Deep Dive Into Understanding 10K Reports - eFinancialModels (web) — https://www.efinancialmodels.com/a-deep-dive-into-understanding-10k-reports/
  - The importance of a 10K financial report cannot be overstated. For investors, these documents provide a detailed account of financial data, risks, and management’s perspective, …
- **[S7]** GitHub - Lunatic16/deep-financial-research: A Claude/Qwen/Gemini skill for institutional-grade investment research. Connects to live market data via MCP servers to deliver company deep dives, due diligence reports, competitive landscape analysis, market sentiment, and DCF-based intrinsic value estimates — all from natural language prompts. · GitHub (web_page) — https://github.com/Lunatic16/deep-financial-research
  - GitHub - Lunatic16/deep-financial-research: A Claude/Qwen/Gemini skill for institutional-grade investment research. Connects to live market data via MCP servers to deliver compa…
- **[S8]** The future of due diligence (web_page) — https://kpmg.com/xx/en/our-insights/value-creation/the-future-of-due-diligence.html
  - The future of due diligence The future of due diligence Sustainable deal value comes from a deeper, more expansive look at a deal’s risks and value opportunities Share Tradition…
- **[S9]** WRAP 10-K (sec)
  - Item 1A chars=2, Item 7 chars=2, ok=True, source=cache
- **[S10]** Item 1A summary (nlp)
  - ### Item 1A — Risk Factors I'm happy to help! However, I don't see any text excerpted below. Please provide the filing excerpt, and I'll be happy to analyze it for you.  Once I …
- **[S11]** Item 7 summary (nlp)
  - ### Item 7 — MD&A I apologize, but it seems you didn't provide the filing excerpt. Please share the text, and I'll be happy to analyze it for you!

## Self-critique

_Automated review (heuristic)._

### Strengths
- Combines local fundamentals, optional DCF scenarios, and cited sources where available.
- Keeps a non-advisory framing for local research drafts.

### Issues & gaps
- Base-case implies deep downside vs spot (<-70%); confirm whether near-term FCF normalization is appropriate for this business.

### Caution for readers
- Treat scenario prices as sensitivity output, not a forecast.
- Re-check primary filings and fresh market data before any decision.



---

# Template: Options income (`income`)

# WRAP — Planned Research Report

> Not investment advice. Local research draft only.

**Goal:** Screen put/call income opportunities with catalyst awareness
**Mode:** deep
**Template:** income
**Planner:** template

## Plan executed

- **Fundamentals check** (`fundamentals`): get_fundamentals
  - Liquidity, leverage, and volatility context for income overlays. Focus: Screen put/call income opportunities with catalyst awareness
- **Put income screen** (`options`): screen_puts
  - ~30–60 DTE OTM puts targeting ~10–15% annualized premium
- **Recent news & catalysts** (`web_research`): search_web
  - Near-term events that could spoil a short-premium thesis

## Fundamentals [S1]
- Company: Wrap Technologies, Inc.
- Sector / industry: Technology / Scientific & Technical Instruments
- Price: 1.87
- 52-week range: $1.04 – $3.23
- Market cap: $104.23M
- Enterprise value: $97.43M
- Shares outstanding: 55.74M
- Beta: 1.368
- Book equity: $11.49M
- Revenue (latest): $4.67M
- EBITDA (latest): -$12.89M
- Free cash flow (latest): -$10.68M
- Operating income: -$13.48M
- Operating margin: -288.6%
- EV / EBITDA: -7.6x
- ROIC: -129.2%
- FCF yield: -10.2%
- Debt / Equity: 0.2103568320278503
- FCF / share: -$0.19
- Revenue / share: $0.08

### Capital structure
- Cash: $3.47M
- Short-term debt: $320.00K
- Long-term debt: $2.10M
- Total debt: $2.42M
- Net debt: -$1.05M
- Net debt / EBITDA: 0.1x

### Growth
- Revenue CAGR: -16.6%
- FCF CAGR: —
- Latest revenue YoY: 3.7%
- Latest FCF YoY: -28.7%

### Market expectations (yfinance, sparse)
- Mean target: —
- Target range: — – —
- Recommendation: none

_Consensus revenue/EBITDA forecasts are often unavailable via free feeds; treat targets as point-in-time only._

### Historical KPIs (multi-year)

| Year | Revenue | OCF | Capex | FCF | EBITDA | LT debt | Cash | Net debt | Net income |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2025 | $4.67M | -$10.29M | $387.00K | -$10.68M | -$12.89M | $2.42M | $3.47M | -$1.05M | -$10.34M |
| 2024 | $4.51M | -$8.12M | $168.00K | -$8.29M | -$14.74M | $2.20M | $3.61M | -$1.41M | -$5.88M |
| 2023 | $6.13M | -$16.70M | $623.00K | -$17.33M | -$17.90M | $2.29M | $3.96M | -$1.67M | -$30.22M |
| 2022 | $8.05M | -$14.60M | $1.13M | -$15.73M | -$16.97M | $301.00K | $5.33M | -$5.03M | -$17.62M |

## Charts

### Revenue & FCF history
![Revenue & FCF history](/charts/WRAP_income_revenue_fcf.png)

## Web research — web_research

- Queries: WRAP news, Wrap Technologies, Inc. earnings OR catalyst
- Unique hits: 15
- Pages fetched: 1/3

### Web synthesis — web_research (rule-based fallback — Ollama unavailable)
**Keyword hits:** revenue

- [HIT] Wrap Technologies Earnings Estimates, EPS & Revenue | Benzinga | www.benzinga.com | https://www.benzinga.com/quote/WRAP/earnings
Wrap Technologies Inc Earnings Estimates.
- Over the last 4 quarters, Wrap Technologies has averaged an EPS surprise of 0.07% and a revenue surprise of 0.33%.

### Sources found
- [The Wrap News](https://en.wikipedia.org/wiki/The_Wrap_News)
  - TheWrap is an American online news organization that covers the business of entertainment and media. It was founded by journalist Sharon Waxman in 2009 and i…
- [TheWrap - Your trusted source for entertainment breaking news](https://www.thewrap.com/)
  - 1 day ago · Your trusted source for breaking entertainment news, film reviews, TV updates and Hollywood insights. Stay informed with the latest entertainment…
- [WRAL | News and Weather in Raleigh NC](https://www.wral.com/)
  - Raleigh breaking news and weather, Raleigh North Carolina news today, WRAL 7-day forecasts, NC lottery updates. WRAL news in Raleigh, NC.
- [Press Releases - Wrap Technologies, Inc.](https://ir.wrap.com/news-events/press-releases)
  - Jul 9, 2026 · WRAP Launches WrapShield: An Autonomous Defense & Public Safety Platform, Beginning with Advanced Thermal Polarimetric Sensing for Counter-UAS …
- [Wrap Launches Next-Generation Drone First Responder Interdiction Solution with a Focus on Non-Lethal Response](https://www.suasnews.com/2025/10/wrap-launches-next-generation-drone-first-responder-interdiction-solution-with-a-focus-on-non-lethal-response/)
  - Wrap Technologies, Inc. (NASDAQ: WRAP) ("Wrap" or the "Company"), a global leader in innovative public safety and unmanned aerial systems ("UAS") solutions, …
- [Wrap Technologies (NASDAQ: WRAP) Highlights Strategic Transformation in Letter to Stockholders](https://www.usatoday.com/press-release/story/37033/wrap-technologies-nasdaq-wrap-highlights-strategic-transformation-in-letter-to-stockholders/)
  - Wrap Technologies (NASDAQ: WRAP) issued a letter to stockholders outlining its strategy to evolve from a single-product
- [4 different ways to wrap presents: Video tutorials](https://www.usatoday.com/story/life/problem-solved/2025/12/16/4-ways-to-wrap-presents/87592459007/)
  - Finding the perfect gift within your budget is challenging enough — but then you've got to wrap it. You're wrangling boxes, searching for tape and scissors, …
- [Takeaways from the AP investigation into ICE’s use of a full-body restraint device known as the WRAP](https://www.nashuatelegraph.com/archive/2025/10/23/takeaways-from-the-ap-investigation-into-ices-use-of-a-full-body-restraint-device-known-as-the-wrap/)
  - This photo provided by Safe Restraints Inc., in October 2025, shows a custom version of the WRAP restraining equipment made for the U.S. Immigration and Cust…
- [Wrap Technologies Earnings Dates, Reports, Calls... | WallStreetZen](https://www.wallstreetzen.com/stocks/us/nasdaq/wrap/earnings)
  - Wrap Technologies Inc Earnings Dates, Reports, Calls.As of Wrap Technologies's earnings date in Q3 2025, Wrap Technologies's earnings has grown year over yea…
- [Wrap Technologies Earnings Estimates, EPS & Revenue | Benzinga](https://www.benzinga.com/quote/WRAP/earnings)
  - Wrap Technologies Inc Earnings Estimates. WRAPNASDAQ.Wrap Technologies (WRAP) is scheduled to report Q2 earnings on August 13, 2026. Over the last 4 quarters…
- [WRAP Stock Analysis & Price Target - In-Depth Research – Financhill](https://financhill.com/stocks/nasdaq/wrap)
  - Wrap Technologies, Inc. share price went down by -17.17% last month. The next quarterly earnings date for Wrap Technologies, Inc. is scheduled on August 13, …
- [Wrap Technologies, Inc. (WRAP) Company Profile... - Yahoo Finance](https://finance.yahoo.com/quote/WRAP/profile/)
  - See the company profile for Wrap Technologies, Inc. (WRAP) including business summary, industry/sector information, number of employees, business summary, co…

## Put opportunities (heuristic) [S2]
- Expiration: 2026-08-21 (DTE 32)
- Candidates: 0
- ATM IV (est.): 156.3%
- IV rank: — (1 local samples)
- HV rank (20d realized): 100.0%


_Note: Delta band approximated via % OTM when greeks are unavailable; IV rank needs ~20+ local daily IV samples (have 1); run the options screen over time to build history.; HV rank is realized-vol rank (20d HV vs ~1y); useful when IV history is thin._

## Research loop (think → act)

1. _heuristic_ — Coverage looks adequate for this pass; stopping iterative loop.

## Sources

- **[S1]** WRAP fundamentals (yfinance)
  - Wrap Technologies, Inc.: price=1.87, rev=4672000.0, fcf=-10676000.0, shares=55738250.0, rev_cagr=-0.16583178878975358, ROIC=-1.2917904013794426, FCF yield=-0.1024268053213738
- **[S2]** WRAP put screen (yfinance_options)
  - Expiration 2026-08-21 (DTE 32): 0 candidates; IV=1.5625021874999998, IV rank=None, HV rank=1.0. Delta band approximated via % OTM when greeks are unavailable; IV rank needs ~20+…
- **[S3]** The Wrap News (web) — https://en.wikipedia.org/wiki/The_Wrap_News
  - TheWrap is an American online news organization that covers the business of entertainment and media. It was founded by journalist Sharon Waxman in 2009 and is based in Los Angel…
- **[S4]** TheWrap - Your trusted source for entertainment breaking news (web) — https://www.thewrap.com/
  - 1 day ago · Your trusted source for breaking entertainment news, film reviews, TV updates and Hollywood insights. Stay informed with the latest entertainment news and analysis.
- **[S5]** WRAL | News and Weather in Raleigh NC (web) — https://www.wral.com/
  - Raleigh breaking news and weather, Raleigh North Carolina news today, WRAL 7-day forecasts, NC lottery updates. WRAL news in Raleigh, NC.
- **[S6]** Press Releases - Wrap Technologies, Inc. (web) — https://ir.wrap.com/news-events/press-releases
  - Jul 9, 2026 · WRAP Launches WrapShield: An Autonomous Defense & Public Safety Platform, Beginning with Advanced Thermal Polarimetric Sensing for Counter-UAS and Expanding Across…
- **[S7]** Wrap Launches Next-Generation Drone First Responder Interdiction Solution with a Focus on Non-Lethal Response (web) — https://www.suasnews.com/2025/10/wrap-launches-next-generation-drone-first-responder-interdiction-solution-with-a-focus-on-non-lethal-response/
  - Wrap Technologies, Inc. (NASDAQ: WRAP) ("Wrap" or the "Company"), a global leader in innovative public safety and unmanned aerial systems ("UAS") solutions, today unveiled the f…
- **[S8]** Wrap Technologies (NASDAQ: WRAP) Highlights Strategic Transformation in Letter to Stockholders (web) — https://www.usatoday.com/press-release/story/37033/wrap-technologies-nasdaq-wrap-highlights-strategic-transformation-in-letter-to-stockholders/
  - Wrap Technologies (NASDAQ: WRAP) issued a letter to stockholders outlining its strategy to evolve from a single-product
- **[S9]** 4 different ways to wrap presents: Video tutorials (web) — https://www.usatoday.com/story/life/problem-solved/2025/12/16/4-ways-to-wrap-presents/87592459007/
  - Finding the perfect gift within your budget is challenging enough — but then you've got to wrap it. You're wrangling boxes, searching for tape and scissors, and don't have the f…
- **[S10]** Takeaways from the AP investigation into ICE’s use of a full-body restraint device known as the WRAP (web) — https://www.nashuatelegraph.com/archive/2025/10/23/takeaways-from-the-ap-investigation-into-ices-use-of-a-full-body-restraint-device-known-as-the-wrap/
  - This photo provided by Safe Restraints Inc., in October 2025, shows a custom version of the WRAP restraining equipment made for the U.S. Immigration and Customs Enforcement agen…
- **[S11]** WRAL | News and Weather in Raleigh NC (web_page) — https://www.wral.com/
  - WRAL | News and Weather in Raleigh NC WRAL News – Raleigh, NC Breaking News and Weather Showers, storms push through central NC; more expected on Tuesday A few showers and storm…

## Self-critique

_Automated review (heuristic)._

### Strengths
- Combines local fundamentals, optional DCF scenarios, and cited sources where available.
- Keeps a non-advisory framing for local research drafts.

### Issues & gaps
- Company FCF is negative; ensure the report clearly flags normalized-margin DCF assumptions.

### Caution for readers
- Treat scenario prices as sensitivity output, not a forecast.
- Re-check primary filings and fresh market data before any decision.



---

# Template: Fast quant (`fast`)

# WRAP — Planned Research Report

> Not investment advice. Local research draft only.

**Goal:** Quick fundamentals + DCF + put screen
**Mode:** fast
**Template:** fast
**Planner:** template

## Plan executed

- **Fundamentals & ratios** (`fundamentals`): get_fundamentals
  - Revenue, FCF, shares, growth rates, ROIC, FCF yield, debt/equity. Focus: Quick fundamentals + DCF + put screen
- **DCF valuation (base / bull / bear)** (`valuation`): run_dcf
  - Intrinsic value from growth, FCF margin, and WACC assumptions
- **Put income screen** (`options`): screen_puts
  - ~30–60 DTE OTM puts targeting ~10–15% annualized premium

## Fundamentals [S1]
- Company: Wrap Technologies, Inc.
- Sector / industry: Technology / Scientific & Technical Instruments
- Price: 1.87
- 52-week range: $1.04 – $3.23
- Market cap: $104.23M
- Enterprise value: $97.43M
- Shares outstanding: 55.74M
- Beta: 1.368
- Book equity: $11.49M
- Revenue (latest): $4.67M
- EBITDA (latest): -$12.89M
- Free cash flow (latest): -$10.68M
- Operating income: -$13.48M
- Operating margin: -288.6%
- EV / EBITDA: -7.6x
- ROIC: -129.2%
- FCF yield: -10.2%
- Debt / Equity: 0.2103568320278503
- FCF / share: -$0.19
- Revenue / share: $0.08

### Capital structure
- Cash: $3.47M
- Short-term debt: $320.00K
- Long-term debt: $2.10M
- Total debt: $2.42M
- Net debt: -$1.05M
- Net debt / EBITDA: 0.1x

### Growth
- Revenue CAGR: -16.6%
- FCF CAGR: —
- Latest revenue YoY: 3.7%
- Latest FCF YoY: -28.7%

### Market expectations (yfinance, sparse)
- Mean target: —
- Target range: — – —
- Recommendation: none

_Consensus revenue/EBITDA forecasts are often unavailable via free feeds; treat targets as point-in-time only._

### Historical KPIs (multi-year)

| Year | Revenue | OCF | Capex | FCF | EBITDA | LT debt | Cash | Net debt | Net income |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2025 | $4.67M | -$10.29M | $387.00K | -$10.68M | -$12.89M | $2.42M | $3.47M | -$1.05M | -$10.34M |
| 2024 | $4.51M | -$8.12M | $168.00K | -$8.29M | -$14.74M | $2.20M | $3.61M | -$1.41M | -$5.88M |
| 2023 | $6.13M | -$16.70M | $623.00K | -$17.33M | -$17.90M | $2.29M | $3.96M | -$1.67M | -$30.22M |
| 2022 | $8.05M | -$14.60M | $1.13M | -$15.73M | -$16.97M | $301.00K | $5.33M | -$5.03M | -$17.62M |

## Charts

### Revenue & FCF history
![Revenue & FCF history](/charts/WRAP_fast_revenue_fcf.png)

### DCF scenario prices
![DCF scenario prices](/charts/WRAP_fast_dcf_scenarios.png)

### Base-case FCF path
![Base-case FCF path](/charts/WRAP_fast_base_fcf_path.png)

## DCF valuation (base / bull / bear) [S2]

> Simplified revenue->FCF DCF. Not investment advice; assumptions are editable heuristics.

- Spot price: $1.87
- Base revenue: $4.67M
- Shares: 55,738,250
- Net debt (Debt−Cash): -$1.05M

| Scenario | Growth | FCF margin | WACC | Term. g | Equity value | Share price | Upside |
|----------|--------|------------|------|---------|--------------|-------------|--------|
| bear | -3.3% | 1.0% | 12.0% | 1.5% | $1.42M | $0.03 | -98.6% |
| base | 3.7% | 3.0% | 10.0% | 2.5% | $3.06M | $0.05 | -97.1% |
| bull | 10.7% | 8.0% | 9.0% | 3.0% | $9.93M | $0.18 | -90.5% |

### Assumption notes
- Base revenue growth seeded from historical rate (3.7%).
- Latest FCF margin was -228.5%; scenarios use normalized positive margins for a going-concern DCF.


### Base-case projected FCF

- Year 1: revenue $4.84M, FCF $145,291 (PV $132,083)
- Year 2: revenue $5.02M, FCF $150,610 (PV $124,471)
- Year 3: revenue $5.20M, FCF $156,124 (PV $117,298)
- Year 4: revenue $5.39M, FCF $161,840 (PV $110,539)
- Year 5: revenue $5.59M, FCF $167,765 (PV $104,169)
- Terminal value $2.29M (PV $1.42M)

## Put opportunities (heuristic) [S3]
- Expiration: 2026-08-21 (DTE 32)
- Candidates: 0
- ATM IV (est.): 156.3%
- IV rank: — (1 local samples)
- HV rank (20d realized): 100.0%


_Note: Delta band approximated via % OTM when greeks are unavailable; IV rank needs ~20+ local daily IV samples (have 1); run the options screen over time to build history.; HV rank is realized-vol rank (20d HV vs ~1y); useful when IV history is thin._

## Research loop (think → act)

1. _heuristic_ — Coverage looks adequate for this pass; stopping iterative loop.

## Sources

- **[S1]** WRAP fundamentals (yfinance)
  - Wrap Technologies, Inc.: price=1.87, rev=4672000.0, fcf=-10676000.0, shares=55738250.0, rev_cagr=-0.16583178878975358, ROIC=-1.2917904013794426, FCF yield=-0.1024268053213738
- **[S2]** WRAP DCF valuation (dcf)
  - Base share price=0.05495684193762078, bull=0.17810369957062142, bear=0.02548857573771363
- **[S3]** WRAP put screen (yfinance_options)
  - Expiration 2026-08-21 (DTE 32): 0 candidates; IV=1.5625021874999998, IV rank=None, HV rank=1.0. Delta band approximated via % OTM when greeks are unavailable; IV rank needs ~20+…

## Self-critique

_Automated review (heuristic)._

### Strengths
- Combines local fundamentals, optional DCF scenarios, and cited sources where available.
- Keeps a non-advisory framing for local research drafts.

### Issues & gaps
- Base-case implies deep downside vs spot (<-70%); confirm whether near-term FCF normalization is appropriate for this business.

### Caution for readers
- Treat scenario prices as sensitivity output, not a forecast.
- Re-check primary filings and fresh market data before any decision.
