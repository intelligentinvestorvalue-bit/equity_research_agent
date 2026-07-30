# SBSW — Full research pack

> Not investment advice. Local research draft only.

**Templates:** memo, valuation, deep, income, fast
**Generated:** 2026-07-28T08:08:34.763265+00:00



---

# Template: Institutional deep dive (memo) (`memo`)

# SBSW — Planned Research Report

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
  - Latest 10-K for business, risks, and MD&A
- **(7b) Recent 10-Q / 8-K headlines** (`recent_filings`): fetch_recent_filings
  - Catalyst calendar inputs — meta only, not full parse
- **(7c) Business overview (Item 1)** (`business`): summarize_item_1
  - Company setup & business model from 10-K Item 1
- **(7d) Risk factors (Item 1A)** (`risks`): summarize_item_1a
  - Falsification inputs from filing risks
- **(7e) MD&A (Item 7)** (`mda`): summarize_item_7
  - Guidance cues and operating commentary
- **(7f) Headwind / tailwind price ranges** (`scenario_ranges`): build_scenario_ranges
  - Medium-term (18–36m) bear/base/bull price bands from catalysts & risks — complements DCF, not a substitute
- **(8) Quarterly driver correlations** (`drivers`): analyze_drivers
  - Suggestive FCF/revenue/debt vs return correlations (small-n caveats)
- **(9) Thesis memo sections** (`memo`): draft_memo_sections
  - Exec summary, variant perception, catalysts, falsifiers, limitations

## Fundamentals [S1]
- Company: D/B/A Sibanye-Stillwater Limite
- Sector / industry: Basic Materials / Other Precious Metals & Mining
- Price: 8.55
- 52-week range: $7.10 – $21.29
- Market cap: $6.18B
- Enterprise value: $43.47B
- Shares outstanding: 707.64M
- Beta: 0.863
- Book equity: $39.53B
- Revenue (latest): $129.68B
- EBITDA (latest): $12.67B
- Free cash flow (latest): $1.10B
- Operating income: $25.06B
- Operating margin: 19.3%
- EV / EBITDA: 3.4x
- ROIC: 5.0%
- FCF yield: 17.8%
- Debt / Equity: 1.1107625360522189
- FCF / share: $1.55
- Revenue / share: $183.25

### Capital structure
- Cash: $17.18B
- Short-term debt: $11.40B
- Long-term debt: $31.86B
- Total debt: $43.90B
- Net debt: $26.73B
- Net debt / EBITDA: 2.1x

### Growth
- Revenue CAGR: -2.1%
- FCF CAGR: —
- Latest revenue YoY: 15.6%
- Latest FCF YoY: 109.6%

### Market expectations (yfinance, sparse)
- Mean target: $12.52
- Target range: $8.91 – $16.13
- Recommendation: buy

_Consensus revenue/EBITDA forecasts are often unavailable via free feeds; treat targets as point-in-time only._

### Historical KPIs (multi-year)

| Year | Revenue | OCF | Capex | FCF | EBITDA | LT debt | Cash | Net debt | Net income |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2025 | $129.68B | $21.41B | $20.31B | $1.10B | $12.67B | $31.86B | $17.18B | $14.68B | -$5.17B |
| 2024 | $112.13B | $10.11B | $21.57B | -$11.46B | $7.86B | $41.13B | $16.05B | $25.09B | -$7.30B |
| 2023 | $113.68B | $7.09B | $22.41B | -$15.32B | -$27.52B | $24.95B | $25.56B | -$614.00M | -$37.77B |
| 2022 | $138.29B | $15.54B | $15.90B | -$356.00M | $37.13B | $22.61B | $26.08B | -$3.47B | $18.40B |

## Charts

### Revenue & FCF history
![Revenue & FCF history](/charts/SBSW_memo_revenue_fcf.png)

### DCF scenario prices
![DCF scenario prices](/charts/SBSW_memo_dcf_scenarios.png)

### Base-case FCF path
![Base-case FCF path](/charts/SBSW_memo_base_fcf_path.png)

### EV/EBITDA scenario prices
![EV/EBITDA scenario prices](/charts/SBSW_memo_ev_ebitda_scenarios.png)

### Headwind/tailwind price ranges
![Headwind/tailwind price ranges](/charts/SBSW_memo_scenario_ranges.png)

### Normalized price vs peers
![Normalized price vs peers](/charts/SBSW_memo_peers_normalized.png)

## DCF valuation (base / bull / bear) [S3]

> Simplified revenue->FCF DCF. Not investment advice; assumptions are editable heuristics.

- Spot price: $8.55
- Base revenue: $129.68B
- Shares: 707,641,816
- Net debt (Debt−Cash): $26.73B

| Scenario | Growth | FCF margin | WACC | Term. g | Equity value | Share price | Upside |
|----------|--------|------------|------|---------|--------------|-------------|--------|
| bear | 8.6% | 0.5% | 12.0% | 1.5% | -$18.38B | $-25.97 | -403.8% |
| base | 15.6% | 1.0% | 10.0% | 2.5% | $3.59B | $5.08 | -40.6% |
| bull | 22.6% | 4.0% | 9.0% | 3.0% | $171.36B | $242.16 | 2732.3% |

### Assumption notes
- Base revenue growth seeded from historical rate (15.6%).

- _bear: model equity value is negative after net debt (-18,378,907,160); showing $-25.97/sh._

### Base-case projected FCF

- Year 1: revenue $149.97B, FCF $1.50B (PV $1.36B)
- Year 2: revenue $173.44B, FCF $1.73B (PV $1.43B)
- Year 3: revenue $200.58B, FCF $2.01B (PV $1.51B)
- Year 4: revenue $231.98B, FCF $2.32B (PV $1.58B)
- Year 5: revenue $268.28B, FCF $2.68B (PV $1.67B)
- Terminal value $36.66B (PV $22.77B)

## Valuation — EV/EBITDA scenarios [S2]

> Priced-in model: implied price = (EBITDA × EV/EBITDA − net debt) ÷ shares. Not a forecast.

- Spot: $8.55
- Net debt used: $26.73B

| Scenario | EBITDA | EV/EBITDA | Implied EV | Equity value | Implied price |
|---|---:|---:|---:|---:|---:|
| bear | $8.87B | 2.6x | $22.82B | -$3.91B | $-5.52 |
| base | $12.67B | 3.4x | $43.47B | $16.74B | $23.66 |
| bull | $15.20B | 4.3x | $65.20B | $38.48B | $54.37 |

- Base EBITDA seeded from latest reported/TTM figure (12,668,000,000).
- Base multiple seeded from current EV/EBITDA (3.4x).

## Scenario price ranges (headwinds & tailwinds) [S31]

> Medium-term (18–36 months (medium / medium-long term)) driver → EV/EBITDA bridge. Distinct from the FCF DCF path. Not investment advice.

- Spot: $8.55
- Sparse Street mean target: $12.52
- Anchor multiple: 3.4x (driver_ev_ebitda_bridge)
- Anchor EBITDA: $12.67B
- Probability-weighted midpoint: **$406.40** (heuristic weights, not a rating)
- Driver extraction: `rules`

### Headwinds (bear-case fuel)

- **Balance-sheet / refinancing pressure** — sector=Basic Materials industry=Other Precious Metals & Mining revenue=129677000000.0 ebitda=12668000000.0 fcf=1100000000.0 net_debt=26726000000.0 nd_ebitda=2.1097252920745184 targ _(source: fundamentals)_
- **Competitive / pricing pressure** — Sibanye Stillwater (SBSW) Stock Forecast: Analyst Ratings, Predictions & Price Target 2026 Sibanye Stillwater (SBSW) Stock Forecast: Analyst Ratings, Predictions & Price Target 202 _(source: web_page)_

### Tailwinds (bull-case fuel)

- **Positive free cash flow** — FCF $1.10B (yield 17.8%) _(source: fundamentals)_
- **Revenue growth momentum** — Latest revenue YoY ≈ 15.6% _(source: fundamentals)_
- **Street target implies upside** — Mean target $12.52 vs spot $8.55 _(source: fundamentals)_
- **Growth / execution upside** — Sibanye Gold (SBSW) Stock Forecast and Price Target 2026 $SBSW 1 week ago - SBSW's current price target is $17.93. Learn why top analysts are making this stock forecast for Sibanye _(source: web)_
- **Product / pricing power** — RBC Capital Issues a Buy Rating on Sibanye Stillwater (SBSW) Detailed price information for Sibanye Gold Ltd ADR (SBSW-N) from The Globe and Mail including charting and trades. _(source: web)_
- **Multiple re-rating / Street upgrades** — Sibanye Stillwater Limited (SBSW) Down 5.8% - Weiss Ratings Mar 2, 2026 ... Weiss Ratings assigns SBSW a D rating, with a current recommendation of Sell. The stock was upgraded on  _(source: web)_
- **Contract / backlog wins** — A Deep Dive into Sibanye ($SBSW): Unlocking a 5x Upside on ...Sibanye Stillwater Limited (SBSW) Stock Price, News, Quote ...Sibanye Stillwater Limited (SBSW) Stock Research ReportS _(source: web)_
- **Deleveraging / BS repair** — Sibanye Stillwater Limited (SBSW) Stock Research Report | Flash Sibanye Stillwater Limited (SBSW) Stock Research Report | Flash Sibanye Stillwater Limited (SBSW) Stock Research Rep _(source: web_page)_

### Price ranges by case

| Case | Prob. | Metric vs TTM | Multiple | Price low | Mid | High | Upside vs spot |
|---|---:|---:|---:|---:|---:|---:|---:|
| bear | 0.17 | 0.78x | 1.5x | $-18.92 | $-16.82 | $-14.73 | -297% |
| base | 0.38 | 1.08x | 3.4x | $23.93 | $28.57 | $33.22 | +234% |
| bull | 0.45 | 1.25x | 41.3x | $793.02 | $885.33 | $977.64 | +10255% |

#### Bear — headwinds dominate

Headwinds bite: weaker operating trajectory and multiple compression. Equity duration shrinks if cash generation fails to offset leverage / competitive pressure.

- **Range:** $-18.92 – $-14.73 (mid $-16.82) · EBITDA $9.88B · multiple 1.5x
- Driver: **Balance-sheet / refinancing pressure** — sector=Basic Materials industry=Other Precious Metals & Mining revenue=129677000000.0 ebitda=12668000000.0 fcf=1100000000.0 net_debt=26726000000.0 nd_ebitda=2.1
- Driver: **Competitive / pricing pressure** — Sibanye Stillwater (SBSW) Stock Forecast: Analyst Ratings, Predictions & Price Target 2026 Sibanye Stillwater (SBSW) Stock Forecast: Analyst Ratings, Prediction

#### Base — mixed execution

Balanced path: some tailwinds offset headwinds. Operating scale roughly holds with modest repair/normalization; valuation stays near the current EV/EBITDA anchor.

- **Range:** $23.93 – $33.22 (mid $28.57) · EBITDA $13.68B · multiple 3.4x
- Driver: **Positive free cash flow** — FCF $1.10B (yield 17.8%)
- Driver: **Revenue growth momentum** — Latest revenue YoY ≈ 15.6%
- Driver: **Balance-sheet / refinancing pressure** — sector=Basic Materials industry=Other Precious Metals & Mining revenue=129677000000.0 ebitda=12668000000.0 fcf=1100000000.0 net_debt=26726000000.0 nd_ebitda=2.1
- Driver: **Competitive / pricing pressure** — Sibanye Stillwater (SBSW) Stock Forecast: Analyst Ratings, Predictions & Price Target 2026 Sibanye Stillwater (SBSW) Stock Forecast: Analyst Ratings, Prediction

#### Bull — tailwinds dominate

Tailwinds compound: operating improvement plus a re-rating toward peer or recovery multiples as balance-sheet and growth narratives improve.

- **Range:** $793.02 – $977.64 (mid $885.33) · EBITDA $15.84B · multiple 41.3x
- Driver: **Positive free cash flow** — FCF $1.10B (yield 17.8%)
- Driver: **Revenue growth momentum** — Latest revenue YoY ≈ 15.6%
- Driver: **Street target implies upside** — Mean target $12.52 vs spot $8.55
- Driver: **Growth / execution upside** — Sibanye Gold (SBSW) Stock Forecast and Price Target 2026 $SBSW 1 week ago - SBSW's current price target is $17.93. Learn why top analysts are making this stock 
- Driver: **Product / pricing power** — RBC Capital Issues a Buy Rating on Sibanye Stillwater (SBSW) Detailed price information for Sibanye Gold Ltd ADR (SBSW-N) from The Globe and Mail including char

### Method notes

- Item 1A risks weighted toward headwinds.
- Peer EV/EBITDA band 1.3x–43.4x (median 11.1x) informs multiple ranges.
- Mapping follows Gemini/Perplexity-style scenario memos: qualitative drivers → operating metric & multiple paths → share-price ranges over a medium-term horizon.

## Peer & factor comps

- Sector / industry: Basic Materials / Other Precious Metals & Mining
- Peers: CCJ, UEC, NXE, UUUU, FCX

| Ticker | Mkt cap | EV/EBITDA | ND/EBITDA | Beta | 1y | 5y | Vol |
|---|---:|---:|---:|---:|---:|---:|---:|
| SBSW | $6.2B | 1.3x | 0.8x | 0.86 | -4.8% | -39.0% | 60.1% |
| CCJ | — | 43.4x | -0.1x | 1.00 | 12.5% | 411.6% | 49.9% |
| UEC | — | -36.6x | 4.0x | 1.19 | 11.2% | 325.3% | 74.4% |
| NXE | $6.2B | -61.1x | 3.1x | 1.65 | 27.7% | 124.0% | 58.1% |
| UUUU | $2.9B | -33.2x | 2.9x | 1.58 | 17.0% | 114.5% | 73.1% |
| FCX | — | 11.1x | 0.7x | 1.36 | 41.2% | 83.2% | 45.2% |

- Peer set (heuristic by sector/industry): CCJ, UEC, NXE, UUUU, FCX
- Beta vs CCJ (daily, ~5y overlap): 0.43

_Price returns are price-only (dividends ignored). Peer set is heuristic, not a formal comps universe._

## Earnings, guidance & revision catalysts

_No earnings surprise history available from yfinance._

- Insufficient paired earnings/move observations for correlation.

## Recent SEC filings (10-Q / 8-K)

_No recent filings found._

## Key driver analysis (quarterly)

Pearson / Spearman correlations of quarterly stock returns with fundamentals.

| Driver | Pearson r | p | n | Spearman ρ | p |
|---|---:|---:|---:|---:|---:|
| Revenue growth (YoY) | — | — | — | — | — |
| Free cash flow | — | — | — | — | — |
| FCF margin | — | — | — | — | — |
| Operating cash flow | — | — | — | — | — |
| Long-term debt level | — | — | 3 | — | — |
| EBITDA | — | — | — | — | — |
| Capex (abs) | — | — | — | — | — |

- Correlations describe association, not causation.
- Small samples (especially regime splits) are directional only.
- Insufficient quarterly overlap for driver correlations.

## Executive summary

D/B/A Sibanye-Stillwater Limite (SBSW) trades near 8.55 with market cap $6.18B and EV $43.47B. Net debt is $26.73B (ND/EBITDA 2.1097252920745184). Latest revenue $129.68B, EBITDA $12.67B, FCF $1.10B.

**Goal focus:** Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers.

What matters most (framework): balance-sheet trajectory, cash generation vs leverage, and whether market expectations (sparse free-data targets) already price execution risk.

EV/EBITDA implied prices — bear $-5.52 / base $23.66 / bull $54.37.

## Company setup & business model

No Item 1 Business text extracted.

_Source: latest 10-K Item 1 (Business), summarized locally._

## Variant perception

- **Consensus frame (sparse):** recommendation=buy, mean target=12.516296.
- **Bear:** leverage and execution risk dominate; cash generation fails to cover refinancing / reinvestment needs; equity remains constrained by net debt.
- **Bull:** cash-flow and strategic optionality re-rate the equity as leverage falls and growth/mix improves.
- **Middle:** returns may track free-cash-flow more than headline revenue — verify with driver analysis tab.

## Catalysts & monitoring

- Next earnings window (calendar): unconfirmed
- Peer tape to watch: CCJ, UEC, NXE, UUUU, FCX
- Monitor: FCF vs net debt, leverage (ND/EBITDA), refinancing headlines, and material 8-K strategy updates.

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
| Guidance / outlook | Forward cash/earnings path | Sibanye Stillwater (SBSW) Stock Forecast: Analyst Ratings, Predictions & Price Target 2026 This rating is provided by third-party analysts and is not investment advice from Public. | Sibanye Stillwater (SBSW) Stock Forecast: Analyst Ratings, Predictions & Price Target 2026 |
| Leverage / refinancing | Balance-sheet repair | Sibanye Stillwater (SBSW) Builds Momentum as Debt Declines and Palladium Outlook... Sibanye Stillwater Limited (NYSE:SBSW) is one of the 12 cheap gold stocks to buy now. On Novembe | Sibanye Stillwater (SBSW) Builds Momentum as Debt Declines and Palladium Outlook... |
| Contract / backlog | Demand durability | A Deep Dive into Sibanye ($SBSW): Unlocking a 5x Upside on ...Sibanye Stillwater Limited (SBSW) Stock Price, News, Quote ...Sibanye Stillwater Limited (SBSW) Stock Research ReportS | A Deep Dive into Sibanye ($SBSW): Unlocking a 5x Upside on ...Sibanye Stillwater Limited (SBSW) Stock Price, News, Quote ...Sibanye Stillwater Limited (SBSW) Stock Research ReportSibanye Stillwater Limited (SBSW): A Bull Case TheorySibanye Stillwater Limited (SBSW) Bullish Thesis: PGM Price ...Sibanye Stillwater Limited (SBSW): A Bull Case Theory |
| Margin / EBITDA | Mix and operating leverage | Sibanye Stillwater: More Gains To Come (NYSE:SBSW) Jan 29, 2026 ... Trading at 7x forward EV/EBITDA versus sector median of 10x, SBSW offers 42% upside from multiple expansion alon | Sibanye Stillwater: More Gains To Come (NYSE:SBSW) |

_Proxies are heuristic extractions from public web/SEC context; verify against primary filings._

## Catalyst calendar

| Window | Catalyst | Notes |
|---|---|---|
| Mar 2, 2026 | Web event | Sibanye Stillwater Limited (SBSW) Down 5.8% - Weiss Ratings |
| May 21, 2026 | Web event | Stellantis Investor Day 2026 |
| February 25, 2025 | Web event | Home - Investor Day |
| Feb 17, 2025 | Web event | A Deep Dive into Sibanye ($SBSW): Unlocking a 5x Upside on ...Sibanye Stillwater Limited (SBSW) Stock Price, News, Quote ...Sibanye Stillwat |
| Aug 4, 2025 | Web event | Sibanye Stillwater Limited (SBSW): A Bull Case Theory |
| Mar 10, 2025 | Web event | Is Sibanye Stillwater Limited (SBSW) the Best Mining Penny Stock to ... |
| Jan 29, 2026 | Web event | Sibanye Stillwater: More Gains To Come (NYSE:SBSW) |

## Web research — web_analysts

- Queries: SBSW analyst price target, D/B/A Sibanye-Stillwater Limite stock rating OR consensus OR upgrade OR downgrade, SBSW Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers analyst, SBSW guidance OR investor day OR catalyst
- Unique hits: 20
- Pages fetched: 2/3

### Web synthesis — web_analysts (rule-based fallback — Ollama unavailable)
**Keyword hits:** customer, product, service, market, operations

- [HIT] Sibanye Gold (SBSW) Stock Forecast and Price Target 2026 $SBSW | www.marketbeat.com | https://www.marketbeat.com/stocks/NYSE/SBSW/forecast/ 1 week ago - SBSW's current price target is $17.93.
- Learn why top analysts are making this stock forecast for Sibanye Gold at MarketBeat.
- [HIT] RBC Capital Issues a Buy Rating on Sibanye Stillwater (SBSW) | The Globe and Mail | https://www.theglobeandmail.com/investing/markets/stocks/SBSW-N/pressreleases/3046805/rbc-capital-issues-a-buy-rating-on-sibanye-stillwater-sbsw/ Detailed price information for Sibanye Gold Ltd ADR (SBSW-N) from The Globe and Mail including charting and trades.
- View live SBSW depositary receipt chart, financials, and market news.
- [HIT] Sibanye Stillwater Ltd ADR (SBSW) - Morningstar | www.morningstar.com | https://www.morningstar.com/stocks/xnys/sbsw/quote Sibanye Stillwater Ltd is a South African mining and metals processing group with a diverse portfolio of operations, projects, and investments across five ...
- [HIT] Sibanye Stillwater (SBSW) Institutional Ownership 2025 | www.marketbeat.com | https://www.marketbeat.com/stocks/NYSE/SBSW/institutional-ownership/ View SBSW institutional ownership (13F) transactions at MarketBeat.Institutional investors have sold a total of 25,129,105 shares in the last 24 months.
- | Seeking Alpha | seekingalpha.com | https://seekingalpha.com/symbol/SBSW/cash-flow-statement Get the cash flow statement for Sibanye Stillwater Limited (SBSW).Invest smarter in volatile markets Make informed decisions with the data, context, and analysis behind today’s market moves, with unlimited access to breaking stock news and free investing newsletters.
- The program included a review of financial targets and key regions, plus sessions on technology, product and financial framework supporting the plan ...

### Sources found
- [Sibanye Stillwater (SBSW) Stock Forecast: Analyst Ratings, Predictions & Price Target 2026](https://public.com/stocks/sbsw/forecast-price-target)
  - This rating is provided by third-party analysts and is not investment advice from Public.com. Wall Street analysts have set a price target of $19.93, reflect…
- [Sibanye Stillwater (SBSW) Stock Forecast, Price Targets and Analysts Predictions - TipRanks.com](https://www.tipranks.com/stocks/sbsw/forecast)
  - SBSW average Analyst price target in the past 3 months is 19.93.
- [Sibanye Gold (SBSW) Stock Forecast and Price Target 2026 $SBSW](https://www.marketbeat.com/stocks/NYSE/SBSW/forecast/)
  - 1 week ago - SBSW's current price target is $17.93. Learn why top analysts are making this stock forecast for Sibanye Gold at MarketBeat.
- [SBSW Forecast, Price Target & Analyst Ratings | ChartMill.com](https://www.chartmill.com/stock/quote/SBSW/analyst-ratings)
  - 11 analysts have analysed SBSW and the average price target is 15.59 USD.
- [Sibanye Stillwater (SBSW): Price Targets Rise, But Mixed Outlook Persists](https://finance.yahoo.com/news/sibanye-stillwater-sbsw-price-targets-054158613.html)
  - Sibanye Stillwater Ltd. (NYSE:SBSW) is one of the best precious metals stocks to buy now. On...
- [Sibanye Stillwater (SBSW) Builds Momentum as Debt Declines and Palladium Outlook...](https://finance.yahoo.com/news/sibanye-stillwater-sbsw-builds-momentum-065551456.html)
  - Sibanye Stillwater Limited (NYSE:SBSW) is one of the 12 cheap gold stocks to buy now. On November 17...
- [Is Sibanye Stillwater Limited (SBSW) the Best Nickel Stock to Invest in?](https://finance.yahoo.com/news/sibanye-stillwater-limited-sbsw-best-150313634.html)
  - We recently published a list of 10 Best Nickel Stocks to Invest in According to Analysts. In this...
- [RBC Capital Issues a Buy Rating on Sibanye Stillwater (SBSW)](https://www.theglobeandmail.com/investing/markets/stocks/SBSW-N/pressreleases/3046805/rbc-capital-issues-a-buy-rating-on-sibanye-stillwater-sbsw/)
  - Detailed price information for Sibanye Gold Ltd ADR (SBSW-N) from The Globe and Mail including charting and trades.
- [Sibanye Stillwater Limited (SBSW) Down 5.8% - Weiss Ratings](https://weissratings.com/en/instant-news-alerts/sibanye-stillwater-limited-sbsw-down-5-8-is-it-time-to-reallocate-funds)
  - Mar 2, 2026 ... Weiss Ratings assigns SBSW a D rating, with a current recommendation of Sell. The stock was upgraded on 6/5/2025, but the overall assessment ...
- [SBSW Stock Price and Chart — NYSE:SBSW - TradingView](https://www.tradingview.com/symbols/NYSE-SBSW/)
  - An easy way to get D/B/A Sibanye-Stillwater Limited real-time prices. View live SBSW depositary receipt chart, financials, and market news.
- [Is Sibanye Stillwater Stock a Buy? - Danelfin](https://danelfin.com/is-sibanye-stillwater-stock-a-buy-now)
  - According to Danelfin's proprietary AI model, Sibanye Stillwater Ltd today receives an AI Score of 6/10, which translates to a Hold rating. The stock has a ...
- [Sibanye Stillwater Ltd ADR (SBSW) - Morningstar](https://www.morningstar.com/stocks/xnys/sbsw/quote)
  - Sibanye Stillwater Ltd is a South African mining and metals processing group with a diverse portfolio of operations, projects, and investments across five ...

### Search warnings
- news:D/B/A Sibanye-Stillwater Limite stock rating OR consensus OR upgrade OR downgrade: No results found.
- news:SBSW Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers analyst: No results found.
- news:SBSW guidance OR investor day OR catalyst: No results found.

## Web research — web_drivers

- Queries: SBSW Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers, D/B/A Sibanye-Stillwater Limite SBSW outlook OR catalyst OR commodity OR uranium OR rare earth OR vanadium, SBSW sector drivers OR market demand, D/B/A Sibanye-Stillwater Limite SBSW backlog OR contract OR refinancing OR leverage
- Unique hits: 13
- Pages fetched: 3/3

### Web synthesis — web_drivers (rule-based fallback — Ollama unavailable)
**Keyword hits:** revenue, segment, product, market, operations, subsidiary

- [HIT] Sibanye-Stillwater - Wikipedia | en.wikipedia.org | https://en.wikipedia.org/wiki/Sibanye-Stillwater Sibanye-Stillwater is a multinational mining and metals processing Group with a diverse portfolio of mining and processing operations and projects and investments across five continents.
- Return vs Market: SBSW underperformed the US ...
- View live SBSW depositary receipt chart, financials, and market news.
- [PAGE] A Deep Dive into Sibanye ($SBSW): Unlocking a 5x Upside on PGM Prices | https://smallcaptreasures.substack.com/p/a-deep-dive-into-sibanye-sbsw-unlocking A Deep Dive into Sibanye ($SBSW): Unlocking a 5x Upside on PGM Prices Undervalued and undercovered Subscribe Sign in A Deep Dive into Sibanye ($SBSW): Unlocking a 5x Upside on PGM Prices High-Cost Assets, High Reward: Why a Price Spike Magnifies Sibanye’s Gains Hugo Navarro Feb 17, 2025 ∙ Paid 14 4 Share Investment Report Key points: High Leverage to PGM Prices: With around 70% of revenue from PGMs, Sibanye-Stillwater’s legacy high-cost operations offer substantial upside if prices rebound.
- mines and recycling operations are particularly valuable, given geopolitical uncertainties around palladium supply and potential trade issues with Russia.
- Sum-of-the-Parts Approach: From gold and PGMs to uranium and other minerals, various segments contribute to Sibanye’s valuation, offering both downside protection and significant upside.
- It is one of those “hated” markets that inevitably draws contrarian investors like myself—rare metals with constrained supply, mostly sourced from just two countries, Russia and South Africa.
- Factors such as substantial short interest in palladium, the potential hydrogen applications for platinum, and increased demand for these minerals in hybrid vehicles (whose production appears to be growing faster than that of BEVs) all point to a significant rise in PGM prices.

### Sources found
- [A Deep Dive into Sibanye ($SBSW): Unlocking a 5x Upside on ...Sibanye Stillwater Limited (SBSW) Stock Price, News, Quote ...Sibanye Stillwater Limited (SBSW) Stock Research ReportSibanye Stillwater Limited (SBSW): A Bull Case TheorySibanye Stillwater Limited (SBSW) Bullish Thesis: PGM Price ...Sibanye Stillwater Limited (SBSW): A Bull Case Theory](https://smallcaptreasures.substack.com/p/a-deep-dive-into-sibanye-sbsw-unlocking)
  - Feb 17, 2025 · In response, Sibanye has placed the Stillwater West Mine on care and maintenance and reduced its workforce to lower costs until prices recover…
- [Sibanye Stillwater Limited (SBSW) Stock Price, News, Quote ...](https://finance.yahoo.com/quote/SBSW/?fr=sycsrp_catchall)
  - Sibanye Stillwater (SBSW) is gaining attention for its strategic financial maneuvers and growth potential. Recent partnerships and earnings reports indicate …
- [Sibanye Stillwater Limited (SBSW) Stock Research Report](https://flash.stocksentinel.ai/research/SBSW)
  - Sibanye Stillwater (SBSW) is a large multinational miner and metals processor that evolved rapidly from a 2013 unbundling of South African gold assets into o…
- [Sibanye Stillwater Limited (SBSW): A Bull Case Theory](https://finance.yahoo.com/news/sibanye-stillwater-limited-sbsw-bull-173240031.html?fr=sycsrp_catchall)
  - Aug 4, 2025 · Sibanye-Stillwater (SBSW), a major producer of platinum group metals (PGMs)—platinum, palladium, and rhodium—offers a leveraged play on a secto…
- [Sibanye-Stillwater - Wikipedia](https://en.wikipedia.org/wiki/Sibanye-Stillwater)
  - Sibanye-Stillwater is a multinational mining and metals processing Group with a diverse portfolio of mining and processing operations and projects and invest…
- [Sibanye Stillwater Limited (SBSW) Stock Price... - Yahoo Finance](https://finance.yahoo.com/quote/SBSW/)
  - Find the latest Sibanye Stillwater Limited (SBSW) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Sibanye Stillwater Limited (SBSW) Stock Price... | Seeking Alpha](https://seekingalpha.com/symbol/SBSW)
  - A high-level overview of Sibanye Stillwater Limited (SBSW) stock. View (SBSW) real-time stock price, chart, news, analysis, analyst reviews and more.
- [SBSW Forecast — Price Target — Prediction for 2027 — TradingView](https://www.tradingview.com/symbols/NYSE-SBSW/forecast/)
  - See Sibanye Stillwater Limited Sponsored ADR stock price prediction for 1 year made by analysts and compare it to price changes over time to develop a better…
- [Is Sibanye Stillwater Limited (SBSW) the Best Mining Penny Stock to ...](https://finance.yahoo.com/news/sibanye-stillwater-limited-sbsw-best-040227899.html)
  - Mar 10, 2025 ... The global demand for essential metals and materials has been on the rise, helping the mining industry expand. The global mineral market is ...
- [Sibanye Stillwater: More Gains To Come (NYSE:SBSW)](https://seekingalpha.com/article/4863946-sibanye-stillwater-more-gains-to-come)
  - Jan 29, 2026 ... Trading at 7x forward EV/EBITDA versus sector median of 10x, SBSW offers 42% upside from multiple expansion alone as 2027 consensus improves.
- [Sibanye Stillwater (NYSE:SBSW) - Stock Analysis - Simply Wall St](https://simplywall.st/stocks/us/materials/nyse-sbsw/sibanye-stillwater)
  - Return vs Industry: SBSW underperformed the US Metals and Mining industry which returned 47.1% over the past year. Return vs Market: SBSW underperformed the …
- [SBSW Stock Price and Chart — NYSE:SBSW — TradingView](https://www.tradingview.com/symbols/NYSE-SBSW/)
  - An easy way to get D/B/A Sibanye-Stillwater Limited real-time prices. View live SBSW depositary receipt chart, financials, and market news.

### Search warnings
- news:SBSW Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers: No results found.
- news:D/B/A Sibanye-Stillwater Limite SBSW outlook OR catalyst OR commodity OR uranium OR rare earth OR vanadium: No results found.
- news:SBSW sector drivers OR market demand: No results found.
- news:D/B/A Sibanye-Stillwater Limite SBSW backlog OR contract OR refinancing OR leverage: No results found.

## SEC filing [S27]
- Extraction OK: False
- Item 1 chars: 0
- Item 1A chars: 0
- Item 7 chars: 0
- Meta: {'accession_number': None, 'filing_date': '', 'source': 'edgartools', 'path': 'C:\\DevWork\\equity_research_agent\\data\\filings\\SBSW_10k.txt'}

## Qualitative analysis (local LLM)

_Item 1 Business summary mode: empty (see Company setup & business model)._

### Item 1A — Risk Factors
No text extracted.


### Item 7 — MD&A
No text extracted.


## Research loop (think → act)

1. _heuristic_ — Coverage looks adequate for this pass; stopping iterative loop.

## Sources

- **[S1]** SBSW fundamentals (yfinance)
  - D/B/A Sibanye-Stillwater Limite: price=8.55, rev=129677000000.0, fcf=1100000000.0, shares=707641816.0, rev_cagr=-0.02120257146003901, ROIC=0.04982491094608465, FCF yield=0.17785…
- **[S2]** SBSW EV/EBITDA valuation (multiples)
  - Base implied price=23.658400650534762, multiple=3.431297252920745
- **[S3]** SBSW DCF valuation (dcf)
  - Base share price=5.0789177948722735, bull=242.1630162522678, bear=-25.972047927162336
- **[S4]** SBSW peer comps (peers)
  - Peers: CCJ, UEC, NXE, UUUU, FCX; rows=6
- **[S5]** SBSW earnings history (earnings)
  - rows=0; next=None
- **[S6]** Sibanye Stillwater (SBSW) Stock Forecast: Analyst Ratings, Predictions & Price Target 2026 (web) — https://public.com/stocks/sbsw/forecast-price-target
  - This rating is provided by third-party analysts and is not investment advice from Public.com. Wall Street analysts have set a price target of $19.93, reflecting a 0.00% increase…
- **[S7]** Sibanye Stillwater (SBSW) Stock Forecast, Price Targets and Analysts Predictions - TipRanks.com (web) — https://www.tipranks.com/stocks/sbsw/forecast
  - SBSW average Analyst price target in the past 3 months is 19.93.
- **[S8]** Sibanye Gold (SBSW) Stock Forecast and Price Target 2026 $SBSW (web) — https://www.marketbeat.com/stocks/NYSE/SBSW/forecast/
  - 1 week ago - SBSW's current price target is $17.93. Learn why top analysts are making this stock forecast for Sibanye Gold at MarketBeat.
- **[S9]** SBSW Forecast, Price Target & Analyst Ratings | ChartMill.com (web) — https://www.chartmill.com/stock/quote/SBSW/analyst-ratings
  - 11 analysts have analysed SBSW and the average price target is 15.59 USD.
- **[S10]** Sibanye Stillwater (SBSW): Price Targets Rise, But Mixed Outlook Persists (web) — https://finance.yahoo.com/news/sibanye-stillwater-sbsw-price-targets-054158613.html
  - Sibanye Stillwater Ltd. (NYSE:SBSW) is one of the best precious metals stocks to buy now. On...
- **[S11]** Sibanye Stillwater (SBSW) Builds Momentum as Debt Declines and Palladium Outlook... (web) — https://finance.yahoo.com/news/sibanye-stillwater-sbsw-builds-momentum-065551456.html
  - Sibanye Stillwater Limited (NYSE:SBSW) is one of the 12 cheap gold stocks to buy now. On November 17...
- **[S12]** Is Sibanye Stillwater Limited (SBSW) the Best Nickel Stock to Invest in? (web) — https://finance.yahoo.com/news/sibanye-stillwater-limited-sbsw-best-150313634.html
  - We recently published a list of 10 Best Nickel Stocks to Invest in According to Analysts. In this...
- **[S13]** RBC Capital Issues a Buy Rating on Sibanye Stillwater (SBSW) (web) — https://www.theglobeandmail.com/investing/markets/stocks/SBSW-N/pressreleases/3046805/rbc-capital-issues-a-buy-rating-on-sibanye-stillwater-sbsw/
  - Detailed price information for Sibanye Gold Ltd ADR (SBSW-N) from The Globe and Mail including charting and trades.
- **[S14]** Sibanye Stillwater (SBSW) Stock Forecast: Analyst Ratings, Predictions & Price Target 2026 (web_page) — https://public.com/stocks/sbsw/forecast-price-target
  - Sibanye Stillwater (SBSW) Stock Forecast: Analyst Ratings, Predictions & Price Target 2026 Skip to main About SBSW Options chain Market cap P/E ratio Forecast News Pre-market Af…
- **[S15]** Sibanye Gold (SBSW) Stock Forecast and Price Target 2026 (web_page) — https://www.marketbeat.com/stocks/NYSE/SBSW/forecast/
  - Sibanye Gold (SBSW) Stock Forecast and Price Target 2026 Skip to main content → Your book attached (From Profits Run) (Ad) Free SBSW Stock Alerts Sibanye Gold (SBSW)  Stock Fore…
- **[S16]** A Deep Dive into Sibanye ($SBSW): Unlocking a 5x Upside on ...Sibanye Stillwater Limited (SBSW) Stock Price, News, Quote ...Sibanye Stillwater Limited (SBSW) Stock Research ReportSibanye Stillwater Limited (SBSW): A Bull Case TheorySibanye Stillwater Limited (SBSW) Bullish Thesis: PGM Price ...Sibanye Stillwater Limited (SBSW): A Bull Case Theory (web) — https://smallcaptreasures.substack.com/p/a-deep-dive-into-sibanye-sbsw-unlocking
  - Feb 17, 2025 · In response, Sibanye has placed the Stillwater West Mine on care and maintenance and reduced its workforce to lower costs until prices recover. Overall, the compa…
- **[S17]** Sibanye Stillwater Limited (SBSW) Stock Price, News, Quote ... (web) — https://finance.yahoo.com/quote/SBSW/?fr=sycsrp_catchall
  - Sibanye Stillwater (SBSW) is gaining attention for its strategic financial maneuvers and growth potential. Recent partnerships and earnings reports indicate strong performance, …
- **[S18]** Sibanye Stillwater Limited (SBSW) Stock Research Report (web) — https://flash.stocksentinel.ai/research/SBSW
  - Sibanye Stillwater (SBSW) is a large multinational miner and metals processor that evolved rapidly from a 2013 unbundling of South African gold assets into one of the world’s le…
- **[S19]** Sibanye Stillwater Limited (SBSW): A Bull Case Theory (web) — https://finance.yahoo.com/news/sibanye-stillwater-limited-sbsw-bull-173240031.html?fr=sycsrp_catchall
  - Aug 4, 2025 · Sibanye-Stillwater (SBSW), a major producer of platinum group metals (PGMs)—platinum, palladium, and rhodium—offers a leveraged play on a sector where years of und…
- **[S20]** Sibanye-Stillwater - Wikipedia (web) — https://en.wikipedia.org/wiki/Sibanye-Stillwater
  - Sibanye-Stillwater is a multinational mining and metals processing Group with a diverse portfolio of mining and processing operations and projects and investments across five co…
- **[S21]** Sibanye Stillwater Limited (SBSW) Stock Price... - Yahoo Finance (web) — https://finance.yahoo.com/quote/SBSW/
  - Find the latest Sibanye Stillwater Limited (SBSW) stock quote, history, news and other vital information to help you with your stock trading and investing.
- **[S22]** Sibanye Stillwater Limited (SBSW) Stock Price... | Seeking Alpha (web) — https://seekingalpha.com/symbol/SBSW
  - A high-level overview of Sibanye Stillwater Limited (SBSW) stock. View (SBSW) real-time stock price, chart, news, analysis, analyst reviews and more.
- **[S23]** SBSW Forecast — Price Target — Prediction for 2027 — TradingView (web) — https://www.tradingview.com/symbols/NYSE-SBSW/forecast/
  - See Sibanye Stillwater Limited Sponsored ADR stock price prediction for 1 year made by analysts and compare it to price changes over time to develop a better trading strategy.D/…
- **[S24]** A Deep Dive into Sibanye ($SBSW): Unlocking a 5x Upside on PGM Prices (web_page) — https://smallcaptreasures.substack.com/p/a-deep-dive-into-sibanye-sbsw-unlocking
  - A Deep Dive into Sibanye ($SBSW): Unlocking a 5x Upside on PGM Prices Undervalued and undercovered Subscribe Sign in A Deep Dive into Sibanye ($SBSW): Unlocking a 5x Upside on P…
- **[S25]** Sibanye Stillwater Limited (SBSW) Stock Price, News, Quote & History - Yahoo Finance (web_page) — https://finance.yahoo.com/quote/SBSW/?fr=sycsrp_catchall
  - Sibanye Stillwater Limited (SBSW) Stock Price, News, Quote & History - Yahoo Finance Oops, something went wrong Skip to navigation Skip to main content Skip to right column We a…
- **[S26]** Sibanye Stillwater Limited (SBSW) Stock Research Report | Flash (web_page) — https://flash.stocksentinel.ai/research/SBSW
  - Sibanye Stillwater Limited (SBSW) Stock Research Report | Flash Sibanye Stillwater Limited (SBSW) Stock Research Report An undervalued, highly cyclical PGM-and-gold miner attemp…
- **[S27]** SBSW 10-K (sec)
  - Item 1 chars=0, Item 1A chars=0, Item 7 chars=0, ok=False, source=edgartools
- **[S28]** Item 1 Business summary (nlp)
  - ### Item 1 — Business No Item 1 Business text extracted. 
- **[S29]** Item 1A summary (nlp)
  - ### Item 1A — Risk Factors No text extracted. 
- **[S30]** Item 7 summary (nlp)
  - ### Item 7 — MD&A No text extracted. 
- **[S31]** SBSW scenario price ranges (scenarios)
  - ok=True; base mid=28.572488271382763; headwinds=2; tailwinds=8
- **[S32]** SBSW driver analysis (drivers)
  - ok=False; drivers=7
- **[S33]** SBSW memo sections (memo)
  - mode=rules; proxies=4

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



---

# Template: Valuation (DCF + Street + drivers) (`valuation`)

# SBSW — Planned Research Report

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
  - Latest 10-K for business, risk, and MD&A context behind the valuation
- **(5b) Business overview (Item 1)** (`business`): summarize_item_1
  - What the company does — products, segments, customers, competitive position
- **(5c) Risk factors (Item 1A)** (`risks`): summarize_item_1a
  - Key risks that should stress the bear case
- **(5d) MD&A (Item 7)** (`mda`): summarize_item_7
  - Management tone, guidance, and operational cues for scenarios
- **(6) Headwind / tailwind price ranges** (`scenario_ranges`): build_scenario_ranges
  - Gemini/Perplexity-style medium-term bear/base/bull ranges: map catalysts & risks → EBITDA/multiple paths → price bands

## Fundamentals [S1]
- Company: D/B/A Sibanye-Stillwater Limite
- Sector / industry: Basic Materials / Other Precious Metals & Mining
- Price: 8.55
- 52-week range: $7.10 – $21.29
- Market cap: $6.18B
- Enterprise value: $43.47B
- Shares outstanding: 707.64M
- Beta: 0.863
- Book equity: $39.53B
- Revenue (latest): $129.68B
- EBITDA (latest): $12.67B
- Free cash flow (latest): $1.10B
- Operating income: $25.06B
- Operating margin: 19.3%
- EV / EBITDA: 3.4x
- ROIC: 5.0%
- FCF yield: 17.8%
- Debt / Equity: 1.1107625360522189
- FCF / share: $1.55
- Revenue / share: $183.25

### Capital structure
- Cash: $17.18B
- Short-term debt: $11.40B
- Long-term debt: $31.86B
- Total debt: $43.90B
- Net debt: $26.73B
- Net debt / EBITDA: 2.1x

### Growth
- Revenue CAGR: -2.1%
- FCF CAGR: —
- Latest revenue YoY: 15.6%
- Latest FCF YoY: 109.6%

### Market expectations (yfinance, sparse)
- Mean target: $12.51
- Target range: $8.91 – $16.12
- Recommendation: buy

_Consensus revenue/EBITDA forecasts are often unavailable via free feeds; treat targets as point-in-time only._

### Historical KPIs (multi-year)

| Year | Revenue | OCF | Capex | FCF | EBITDA | LT debt | Cash | Net debt | Net income |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2025 | $129.68B | $21.41B | $20.31B | $1.10B | $12.67B | $31.86B | $17.18B | $14.68B | -$5.17B |
| 2024 | $112.13B | $10.11B | $21.57B | -$11.46B | $7.86B | $41.13B | $16.05B | $25.09B | -$7.30B |
| 2023 | $113.68B | $7.09B | $22.41B | -$15.32B | -$27.52B | $24.95B | $25.56B | -$614.00M | -$37.77B |
| 2022 | $138.29B | $15.54B | $15.90B | -$356.00M | $37.13B | $22.61B | $26.08B | -$3.47B | $18.40B |

## Charts

### Revenue & FCF history
![Revenue & FCF history](/charts/SBSW_valuation_revenue_fcf.png)

### DCF scenario prices
![DCF scenario prices](/charts/SBSW_valuation_dcf_scenarios.png)

### Base-case FCF path
![Base-case FCF path](/charts/SBSW_valuation_base_fcf_path.png)

### EV/EBITDA scenario prices
![EV/EBITDA scenario prices](/charts/SBSW_valuation_ev_ebitda_scenarios.png)

### Headwind/tailwind price ranges
![Headwind/tailwind price ranges](/charts/SBSW_valuation_scenario_ranges.png)

## DCF valuation (base / bull / bear) [S2]

> Simplified revenue->FCF DCF. Not investment advice; assumptions are editable heuristics.

- Spot price: $8.55
- Base revenue: $129.68B
- Shares: 707,641,816
- Net debt (Debt−Cash): $26.73B

| Scenario | Growth | FCF margin | WACC | Term. g | Equity value | Share price | Upside |
|----------|--------|------------|------|---------|--------------|-------------|--------|
| bear | 8.6% | 0.5% | 12.0% | 1.5% | -$18.38B | $-25.97 | -403.8% |
| base | 15.6% | 1.0% | 10.0% | 2.5% | $3.59B | $5.08 | -40.6% |
| bull | 22.6% | 4.0% | 9.0% | 3.0% | $171.36B | $242.16 | 2732.3% |

### Assumption notes
- Base revenue growth seeded from historical rate (15.6%).

- _bear: model equity value is negative after net debt (-18,378,907,160); showing $-25.97/sh._

### Base-case projected FCF

- Year 1: revenue $149.97B, FCF $1.50B (PV $1.36B)
- Year 2: revenue $173.44B, FCF $1.73B (PV $1.43B)
- Year 3: revenue $200.58B, FCF $2.01B (PV $1.51B)
- Year 4: revenue $231.98B, FCF $2.32B (PV $1.58B)
- Year 5: revenue $268.28B, FCF $2.68B (PV $1.67B)
- Terminal value $36.66B (PV $22.77B)

## Valuation — EV/EBITDA scenarios [S3]

> Priced-in model: implied price = (EBITDA × EV/EBITDA − net debt) ÷ shares. Not a forecast.

- Spot: $8.55
- Net debt used: $26.73B

| Scenario | EBITDA | EV/EBITDA | Implied EV | Equity value | Implied price |
|---|---:|---:|---:|---:|---:|
| bear | $8.87B | 2.6x | $22.82B | -$3.91B | $-5.52 |
| base | $12.67B | 3.4x | $43.47B | $16.74B | $23.66 |
| bull | $15.20B | 4.3x | $65.20B | $38.48B | $54.37 |

- Base EBITDA seeded from latest reported/TTM figure (12,668,000,000).
- Base multiple seeded from current EV/EBITDA (3.4x).

## Scenario price ranges (headwinds & tailwinds) [S26]

> Medium-term (18–36 months (medium / medium-long term)) driver → EV/EBITDA bridge. Distinct from the FCF DCF path. Not investment advice.

- Spot: $8.55
- Sparse Street mean target: $12.51
- Anchor multiple: 3.4x (driver_ev_ebitda_bridge)
- Anchor EBITDA: $12.67B
- Probability-weighted midpoint: **$38.73** (heuristic weights, not a rating)
- Driver extraction: `rules`

### Headwinds (bear-case fuel)

- **Balance-sheet / refinancing pressure** — sector=Basic Materials industry=Other Precious Metals & Mining revenue=129677000000.0 ebitda=12668000000.0 fcf=1100000000.0 net_debt=26726000000.0 nd_ebitda=2.1097252920745184 targ _(source: fundamentals)_

### Tailwinds (bull-case fuel)

- **Positive free cash flow** — FCF $1.10B (yield 17.8%) _(source: fundamentals)_
- **Revenue growth momentum** — Latest revenue YoY ≈ 15.6% _(source: fundamentals)_
- **Street target implies upside** — Mean target $12.51 vs spot $8.55 _(source: fundamentals)_
- **Growth / execution upside** — Sibanye Gold (SBSW) Stock Forecast and Price Target 2026 SBSW's current price target is $19.93. Learn why top analysts are making this stock forecast for Sibanye Gold at MarketBeat _(source: web)_
- **Product / pricing power** — RBC Capital Issues a Buy Rating on Sibanye Stillwater (SBSW) Detailed price information for Sibanye Gold Ltd ADR (SBSW-N) from The Globe and Mail including charting and trades. _(source: web)_
- **Multiple re-rating / Street upgrades** — SBSW Forecast, Price Target & Analyst Ratings | ChartMill.com View the latest analyst price targets, stock forecast, EPS estimates, revenue projections, revisions, full estimates,  _(source: web)_
- **Contract / backlog wins** — What value stocks have you bought recently and why? What ... - Reddit Oct 31, 2024 ... In what world is this possibly a value stock? It's trading at a 3.5% earnings yield and plowi _(source: web)_
- **Capital returns / FCF inflection** — What value stocks have you bought recently and why? What ... - Reddit Oct 31, 2024 ... In what world is this possibly a value stock? It's trading at a 3.5% earnings yield and plowi _(source: web)_

### Price ranges by case

| Case | Prob. | Metric vs TTM | Multiple | Price low | Mid | High | Upside vs spot |
|---|---:|---:|---:|---:|---:|---:|---:|
| bear | 0.17 | 0.78x | 2.4x | $-7.58 | $-4.23 | $-0.88 | -149% |
| base | 0.36 | 1.08x | 3.4x | $23.93 | $28.57 | $33.22 | +234% |
| bull | 0.47 | 1.25x | 4.5x | $52.07 | $62.05 | $72.03 | +626% |

#### Bear — headwinds dominate

Headwinds bite: weaker operating trajectory and multiple compression. Equity duration shrinks if cash generation fails to offset leverage / competitive pressure.

- **Range:** $-7.58 – $-0.88 (mid $-4.23) · EBITDA $9.88B · multiple 2.4x
- Driver: **Balance-sheet / refinancing pressure** — sector=Basic Materials industry=Other Precious Metals & Mining revenue=129677000000.0 ebitda=12668000000.0 fcf=1100000000.0 net_debt=26726000000.0 nd_ebitda=2.1

#### Base — mixed execution

Balanced path: some tailwinds offset headwinds. Operating scale roughly holds with modest repair/normalization; valuation stays near the current EV/EBITDA anchor.

- **Range:** $23.93 – $33.22 (mid $28.57) · EBITDA $13.68B · multiple 3.4x
- Driver: **Positive free cash flow** — FCF $1.10B (yield 17.8%)
- Driver: **Revenue growth momentum** — Latest revenue YoY ≈ 15.6%
- Driver: **Balance-sheet / refinancing pressure** — sector=Basic Materials industry=Other Precious Metals & Mining revenue=129677000000.0 ebitda=12668000000.0 fcf=1100000000.0 net_debt=26726000000.0 nd_ebitda=2.1

#### Bull — tailwinds dominate

Tailwinds compound: operating improvement plus a re-rating toward peer or recovery multiples as balance-sheet and growth narratives improve.

- **Range:** $52.07 – $72.03 (mid $62.05) · EBITDA $15.84B · multiple 4.5x
- Driver: **Positive free cash flow** — FCF $1.10B (yield 17.8%)
- Driver: **Revenue growth momentum** — Latest revenue YoY ≈ 15.6%
- Driver: **Street target implies upside** — Mean target $12.51 vs spot $8.55
- Driver: **Growth / execution upside** — Sibanye Gold (SBSW) Stock Forecast and Price Target 2026 SBSW's current price target is $19.93. Learn why top analysts are making this stock forecast for Sibany
- Driver: **Product / pricing power** — RBC Capital Issues a Buy Rating on Sibanye Stillwater (SBSW) Detailed price information for Sibanye Gold Ltd ADR (SBSW-N) from The Globe and Mail including char

### Method notes

- Item 1A risks weighted toward headwinds.
- Mapping follows Gemini/Perplexity-style scenario memos: qualitative drivers → operating metric & multiple paths → share-price ranges over a medium-term horizon.

## Web research — web_analysts

- Queries: SBSW analyst price target, D/B/A Sibanye-Stillwater Limite stock rating OR consensus OR upgrade OR downgrade, SBSW Estimate intrinsic value under base / bull / bear scenarios analyst
- Unique hits: 14
- Pages fetched: 2/3

### Web synthesis — web_analysts (rule-based fallback — Ollama unavailable)
**Keyword hits:** guidance, revenue, margin, customer, service, market

- [HIT] Sibanye Gold (SBSW) Stock Forecast and Price Target 2026 | www.marketbeat.com | https://www.marketbeat.com/stocks/NYSE/SBSW/forecast/ SBSW's current price target is $19.93.
- Learn why top analysts are making this stock forecast for Sibanye Gold at MarketBeat.According to the 5 analysts' twelve-month price targets for Sibanye Gold, the average price target is $19.93.
- [HIT] RBC Capital Issues a Buy Rating on Sibanye Stillwater (SBSW) | The Globe and Mail | https://www.theglobeandmail.com/investing/markets/stocks/SBSW-N/pressreleases/3046805/rbc-capital-issues-a-buy-rating-on-sibanye-stillwater-sbsw/ Detailed price information for Sibanye Gold Ltd ADR (SBSW-N) from The Globe and Mail including charting and trades.
- [HIT] Sibanye Stillwater Ltd, SBSW:NYQ summary - FT.com | markets.ft.com | https://markets.ft.com/data/equities/tearsheet/summary?s=SBSW:NYQ Latest Sibanye Stillwater Ltd (SBSW:NYQ) share price with interactive charts, historical prices, comparative analysis, forecasts, business profile and more.
- [HIT] SBSW Forecast, Price Target & Analyst Ratings | ChartMill.com | www.chartmill.com | https://www.chartmill.com/stock/quote/SBSW/analyst-ratings View the latest analyst price targets, stock forecast, EPS estimates, revenue projections, revisions, full estimates, rating distribution and upgrades/downgrades for SIBANYE-STILLWATER LTD-ADR (SBSW).
- ADR Analyst Estimates - MarketWatch | www.marketwatch.com | https://www.marketwatch.com/investing/stock/sbsw/analystestimates Sibanye-Stillwater Ltd.
- [PAGE] Sibanye Gold (SBSW) Stock Forecast and Price Target 2026 | https://www.marketbeat.com/stocks/NYSE/SBSW/forecast/ Sibanye Gold (SBSW) Stock Forecast and Price Target 2026 Skip to main content → Here’s the stock symbol I’ve promised (From Stansberry Research) (Ad) Free SBSW Stock Alerts Sibanye Gold (SBSW)  Stock Forecast & Price Target $8.54 +0.18 (+2.09%) Closing price 07/27/2026 03:59 PM Eastern Extended Trading $8.48 -0.06 (-0.70%) As of 04:15 AM Eastern Extended trading is trading that happens on electronic markets outside of regular trading hours.
- This is a fair market value extended hours price provided by Massive.

### Sources found
- [Sibanye Stillwater Limited (SBSW) Stock Forecast, Price Targets and...](https://www.tipranks.com/stocks/sbsw/forecast)
  - Analyze Forecast. Average Price Target.The average price target for Sibanye Stillwater Limited is 14.25. This is based on 2 Wall Streets Analysts 12-month pr…
- [Sibanye Gold (SBSW) Stock Forecast and Price Target 2026](https://www.marketbeat.com/stocks/NYSE/SBSW/forecast/)
  - SBSW's current price target is $19.93. Learn why top analysts are making this stock forecast for Sibanye Gold at MarketBeat.According to the 5 analysts' twel…
- [Sibanye Stillwater Analyst Ratings and Price Targets | NYSE:SBSW](https://www.benzinga.com/quote/SBSW/analyst-ratings)
  - The latest price target for Sibanye Stillwater (NYSE:SBSW) was reported by RBC Capital on June 29, 2026. The analyst firm set a price target for $16.50 expec…
- [Sibanye Stillwater Limited (SBSW) Analyst Insights, Price Targets...](https://finance.yahoo.com/quote/SBSW/analyst-insights/)
  - Price Action Lowers. Price Target 14 -> 12. Top Analysts. Yahoo Finance’s Top Analysts section provides an objective scorecard to evaluate the accuracy of Wa…
- [RBC Capital Issues a Buy Rating on Sibanye Stillwater (SBSW)](https://www.theglobeandmail.com/investing/markets/stocks/SBSW-N/pressreleases/3046805/rbc-capital-issues-a-buy-rating-on-sibanye-stillwater-sbsw/)
  - Detailed price information for Sibanye Gold Ltd ADR (SBSW-N) from The Globe and Mail including charting and trades.
- [Sibanye Stillwater (SBSW): Price Targets Rise, But Mixed Outlook Persists](https://finance.yahoo.com/news/sibanye-stillwater-sbsw-price-targets-054158613.html)
  - Sibanye Stillwater Ltd. (NYSE:SBSW) is one of the best precious metals stocks to buy now. On...
- [Sibanye Stillwater (SBSW) Builds Momentum as Debt Declines and Palladium Outlook...](https://finance.yahoo.com/news/sibanye-stillwater-sbsw-builds-momentum-065551456.html)
  - Sibanye Stillwater Limited (NYSE:SBSW) is one of the 12 cheap gold stocks to buy now. On November 17...
- [Is Sibanye Stillwater Limited (SBSW) the Best Nickel Stock to Invest in?](https://finance.yahoo.com/news/sibanye-stillwater-limited-sbsw-best-150313634.html)
  - We recently published a list of 10 Best Nickel Stocks to Invest in According to Analysts. In this...
- [Sibanye Stillwater Ltd, SBSW:NYQ summary - FT.com](https://markets.ft.com/data/equities/tearsheet/summary?s=SBSW:NYQ)
  - Latest Sibanye Stillwater Ltd (SBSW:NYQ) share price with interactive charts, historical prices, comparative analysis, forecasts, business profile and more.
- [SBSW Forecast, Price Target & Analyst Ratings | ChartMill.com](https://www.chartmill.com/stock/quote/SBSW/analyst-ratings)
  - View the latest analyst price targets, stock forecast, EPS estimates, revenue projections, revisions, full estimates, rating distribution and upgrades/downgr…
- [Sibanye-Stillwater Ltd. ADR Analyst Estimates - MarketWatch](https://www.marketwatch.com/investing/stock/sbsw/analystestimates)
  - Sibanye-Stillwater Ltd. ADR analyst estimates, including SBSW earnings per share estimates and analyst recommendations.
- [Sibanye Stillwater (NYSE:SBSW) - Stock Analysis - Simply Wall St](https://simplywall.st/stocks/us/materials/nyse-sbsw/sibanye-stillwater)
  - Sibanye Stillwater: Time To Test The Waters (Rating Upgrade) Summary We have decided to upgrade Sibanye Stillwater Limited's stock on the basis of an enhance…

### Search warnings
- news:D/B/A Sibanye-Stillwater Limite stock rating OR consensus OR upgrade OR downgrade: No results found.
- news:SBSW Estimate intrinsic value under base / bull / bear scenarios analyst: No results found.

## Web research — web_drivers

- Queries: SBSW Estimate intrinsic value under base / bull / bear scenarios, D/B/A Sibanye-Stillwater Limite SBSW outlook OR catalyst OR commodity OR uranium OR rare earth OR vanadium, SBSW sector drivers OR market demand
- Unique hits: 11
- Pages fetched: 0/3

### Web synthesis — web_drivers (rule-based fallback — Ollama unavailable)
**Keyword hits:** revenue, market, operations

- ADR Analyst Estimates | MarketWatch | www.marketwatch.com | https://www.marketwatch.com/investing/stock/sbsw/analystestimates?mod=mw_quote_tab SBSW Analyst Estimates.
- [HIT] Sibanye Stillwater Limited (SBSW) Earnings Estimates, Revenue...
- Example: Bulls Say  [HIT] News & investors - Sibanye-Stillwater | www.sibanyestillwater.com | https://www.sibanyestillwater.com/news-investors/ News & investors Sibanye-Stillwater (JSE:SSW, NYSE:SBSW) is a multinational mining and metals processing group with a diverse portfolio of operations, projects and investments across five continents.
- [HIT] Sibanye Stillwater Ltd, SBSW:NYQ summary - FT.com | markets.ft.com | https://markets.ft.com/data/equities/tearsheet/summary?s=SBSW:NYQ Latest Sibanye Stillwater Ltd (SBSW:NYQ) share price with interactive charts, historical prices, comparative analysis, forecasts, business profile and more.
- Return vs Market: SBSW underperformed the US ...

### Sources found
- [SBSW Intrinsic Valuation and Fundamental Analysis... - Alpha Spread](https://www.alphaspread.com/security/NYSE/SBSW/summary)
  - Sibanye Stillwater Ltd (NYSE:SBSW) Intrinsic Valuation. Check if SBSW is overvalued or undervalued under the bear, base, and bull scenarios of the company's …
- [SBSW | Sibanye-Stillwater Ltd. ADR Analyst Estimates | MarketWatch](https://www.marketwatch.com/investing/stock/sbsw/analystestimates?mod=mw_quote_tab)
  - SBSW Analyst Estimates. Snapshot. Average Recommendation.Current Year's Estimate. 2.99. Median PE on CY Estimate.
- [Sibanye Stillwater Limited (SBSW) Earnings Estimates, Revenue...](https://seekingalpha.com/symbol/SBSW/earnings/estimates)
  - SBSW Sibanye Stillwater Limited. Earnings Estimates. sbsw Summary. Follow. 30.35K followers.
- [SBSW | Sibanye-Stillwater American Depositary Shares, Stock Data...](https://www.quiverquant.com/stock/SBSW/)
  - What funds own $SBSW stock? * These are estimates based on data taken from SEC filings.Score Breakdown. Bull Case vs Bear Case. See concise summaries of anal…
- [News & investors - Sibanye-Stillwater](https://www.sibanyestillwater.com/news-investors/)
  - News & investors Sibanye-Stillwater (JSE:SSW, NYSE:SBSW) is a multinational mining and metals processing group with a diverse portfolio of operations, projec…
- [Sibanye Stillwater Keliber & Uranium: 2026 Gold Mining](https://farmonaut.com/mining/sibanye-stillwater-keliber-uranium-2026-gold-mining)
  - In this extensive 2026-focused analysis, we explore how sibanye stillwater keliber, sibanye gold stillwater, and sibanye stillwater uranium are rewriting the…
- [Sibanye Stillwater Ltd, SBSW:NYQ summary - FT.com](https://markets.ft.com/data/equities/tearsheet/summary?s=SBSW:NYQ)
  - Latest Sibanye Stillwater Ltd (SBSW:NYQ) share price with interactive charts, historical prices, comparative analysis, forecasts, business profile and more.
- [SBSW Sibanye Stillwater Limited - Seeking Alpha](https://seekingalpha.com/symbol/SBSW)
  - A high-level overview of Sibanye Stillwater Limited (SBSW) stock. View (SBSW) real-time stock price, chart, news, analysis, analyst reviews and more.
- [Is Sibanye Stillwater Limited (SBSW) the Best Mining Penny Stock to ...](https://finance.yahoo.com/news/sibanye-stillwater-limited-sbsw-best-040227899.html)
  - Mar 10, 2025 ... The global demand for essential metals and materials has been on the rise, helping the mining industry expand. The global mineral market is ...
- [Sibanye Stillwater: More Gains To Come (NYSE:SBSW)](https://seekingalpha.com/article/4863946-sibanye-stillwater-more-gains-to-come)
  - Jan 29, 2026 ... Trading at 7x forward EV/EBITDA versus sector median of 10x, SBSW offers 42% upside from multiple expansion alone as 2027 consensus improves.
- [Sibanye Stillwater (NYSE:SBSW) - Stock Analysis - Simply Wall St](https://simplywall.st/stocks/us/materials/nyse-sbsw/sibanye-stillwater)
  - Return vs Industry: SBSW underperformed the US Metals and Mining industry which returned 47.1% over the past year. Return vs Market: SBSW underperformed the …

### Search warnings
- news:SBSW Estimate intrinsic value under base / bull / bear scenarios: No results found.
- news:D/B/A Sibanye-Stillwater Limite SBSW outlook OR catalyst OR commodity OR uranium OR rare earth OR vanadium: No results found.
- news:SBSW sector drivers OR market demand: No results found.

## SEC filing [S22]
- Extraction OK: False
- Item 1 chars: 0
- Item 1A chars: 0
- Item 7 chars: 0
- Meta: {'source': 'cache', 'path': 'C:\\DevWork\\equity_research_agent\\data\\filings\\SBSW_10k.txt'}

## Company setup & business model

No Item 1 Business text extracted.

_Source: latest 10-K Item 1 (Business), summarized locally._

## Qualitative analysis (local LLM)

### Item 1 — Business
No Item 1 Business text extracted.


### Item 1A — Risk Factors
No text extracted.


### Item 7 — MD&A
No text extracted.


## Research loop (think → act)

1. _heuristic_ — Coverage looks adequate for this pass; stopping iterative loop.

## Sources

- **[S1]** SBSW fundamentals (yfinance)
  - D/B/A Sibanye-Stillwater Limite: price=8.55, rev=129677000000.0, fcf=1100000000.0, shares=707641816.0, rev_cagr=-0.02120257146003901, ROIC=0.04982491094608465, FCF yield=0.17785…
- **[S2]** SBSW DCF valuation (dcf)
  - Base share price=5.0789177948722735, bull=242.1630162522678, bear=-25.972047927162336
- **[S3]** SBSW EV/EBITDA valuation (multiples)
  - Base implied price=23.658400650534762, multiple=3.431297252920745
- **[S4]** Sibanye Stillwater Limited (SBSW) Stock Forecast, Price Targets and... (web) — https://www.tipranks.com/stocks/sbsw/forecast
  - Analyze Forecast. Average Price Target.The average price target for Sibanye Stillwater Limited is 14.25. This is based on 2 Wall Streets Analysts 12-month price targets, issued …
- **[S5]** Sibanye Gold (SBSW) Stock Forecast and Price Target 2026 (web) — https://www.marketbeat.com/stocks/NYSE/SBSW/forecast/
  - SBSW's current price target is $19.93. Learn why top analysts are making this stock forecast for Sibanye Gold at MarketBeat.According to the 5 analysts' twelve-month price targe…
- **[S6]** Sibanye Stillwater Analyst Ratings and Price Targets | NYSE:SBSW (web) — https://www.benzinga.com/quote/SBSW/analyst-ratings
  - The latest price target for Sibanye Stillwater (NYSE:SBSW) was reported by RBC Capital on June 29, 2026. The analyst firm set a price target for $16.50 expecting SBSW to rise to…
- **[S7]** Sibanye Stillwater Limited (SBSW) Analyst Insights, Price Targets... (web) — https://finance.yahoo.com/quote/SBSW/analyst-insights/
  - Price Action Lowers. Price Target 14 -> 12. Top Analysts. Yahoo Finance’s Top Analysts section provides an objective scorecard to evaluate the accuracy of Wall Street analyst ra…
- **[S8]** RBC Capital Issues a Buy Rating on Sibanye Stillwater (SBSW) (web) — https://www.theglobeandmail.com/investing/markets/stocks/SBSW-N/pressreleases/3046805/rbc-capital-issues-a-buy-rating-on-sibanye-stillwater-sbsw/
  - Detailed price information for Sibanye Gold Ltd ADR (SBSW-N) from The Globe and Mail including charting and trades.
- **[S9]** Sibanye Stillwater (SBSW): Price Targets Rise, But Mixed Outlook Persists (web) — https://finance.yahoo.com/news/sibanye-stillwater-sbsw-price-targets-054158613.html
  - Sibanye Stillwater Ltd. (NYSE:SBSW) is one of the best precious metals stocks to buy now. On...
- **[S10]** Sibanye Stillwater (SBSW) Builds Momentum as Debt Declines and Palladium Outlook... (web) — https://finance.yahoo.com/news/sibanye-stillwater-sbsw-builds-momentum-065551456.html
  - Sibanye Stillwater Limited (NYSE:SBSW) is one of the 12 cheap gold stocks to buy now. On November 17...
- **[S11]** Is Sibanye Stillwater Limited (SBSW) the Best Nickel Stock to Invest in? (web) — https://finance.yahoo.com/news/sibanye-stillwater-limited-sbsw-best-150313634.html
  - We recently published a list of 10 Best Nickel Stocks to Invest in According to Analysts. In this...
- **[S12]** Sibanye Gold (SBSW) Stock Forecast and Price Target 2026 (web_page) — https://www.marketbeat.com/stocks/NYSE/SBSW/forecast/
  - Sibanye Gold (SBSW) Stock Forecast and Price Target 2026 Skip to main content → Here’s the stock symbol I’ve promised (From Stansberry Research) (Ad) Free SBSW Stock Alerts Siba…
- **[S13]** Sibanye Stillwater Analyst Ratings and Price Targets | NYSE:SBSW | Benzinga (web_page) — https://www.benzinga.com/quote/SBSW/analyst-ratings
  - Sibanye Stillwater Analyst Ratings and Price Targets | NYSE:SBSW | Benzinga Benzinga España Italia 대한민국 日本 Français My Account Login SPY 737.72 - QQQ 675.86 0.92% BTC/USD 63415.…
- **[S14]** SBSW Intrinsic Valuation and Fundamental Analysis... - Alpha Spread (web) — https://www.alphaspread.com/security/NYSE/SBSW/summary
  - Sibanye Stillwater Ltd (NYSE:SBSW) Intrinsic Valuation. Check if SBSW is overvalued or undervalued under the bear, base, and bull scenarios of the company's future.
- **[S15]** SBSW | Sibanye-Stillwater Ltd. ADR Analyst Estimates | MarketWatch (web) — https://www.marketwatch.com/investing/stock/sbsw/analystestimates?mod=mw_quote_tab
  - SBSW Analyst Estimates. Snapshot. Average Recommendation.Current Year's Estimate. 2.99. Median PE on CY Estimate.
- **[S16]** Sibanye Stillwater Limited (SBSW) Earnings Estimates, Revenue... (web) — https://seekingalpha.com/symbol/SBSW/earnings/estimates
  - SBSW Sibanye Stillwater Limited. Earnings Estimates. sbsw Summary. Follow. 30.35K followers.
- **[S17]** SBSW | Sibanye-Stillwater American Depositary Shares, Stock Data... (web) — https://www.quiverquant.com/stock/SBSW/
  - What funds own $SBSW stock? * These are estimates based on data taken from SEC filings.Score Breakdown. Bull Case vs Bear Case. See concise summaries of analyst reports, present…
- **[S18]** News & investors - Sibanye-Stillwater (web) — https://www.sibanyestillwater.com/news-investors/
  - News & investors Sibanye-Stillwater (JSE:SSW, NYSE:SBSW) is a multinational mining and metals processing group with a diverse portfolio of operations, projects and investments a…
- **[S19]** Sibanye Stillwater Keliber & Uranium: 2026 Gold Mining (web) — https://farmonaut.com/mining/sibanye-stillwater-keliber-uranium-2026-gold-mining
  - In this extensive 2026-focused analysis, we explore how sibanye stillwater keliber, sibanye gold stillwater, and sibanye stillwater uranium are rewriting the rules of resource e…
- **[S20]** Sibanye Stillwater Ltd, SBSW:NYQ summary - FT.com (web) — https://markets.ft.com/data/equities/tearsheet/summary?s=SBSW:NYQ
  - Latest Sibanye Stillwater Ltd (SBSW:NYQ) share price with interactive charts, historical prices, comparative analysis, forecasts, business profile and more.
- **[S21]** SBSW Sibanye Stillwater Limited - Seeking Alpha (web) — https://seekingalpha.com/symbol/SBSW
  - A high-level overview of Sibanye Stillwater Limited (SBSW) stock. View (SBSW) real-time stock price, chart, news, analysis, analyst reviews and more.
- **[S22]** SBSW 10-K (sec)
  - Item 1 chars=0, Item 1A chars=0, Item 7 chars=0, ok=False, source=cache
- **[S23]** Item 1 Business summary (nlp)
  - ### Item 1 — Business No Item 1 Business text extracted. 
- **[S24]** Item 1A summary (nlp)
  - ### Item 1A — Risk Factors No text extracted. 
- **[S25]** Item 7 summary (nlp)
  - ### Item 7 — MD&A No text extracted. 
- **[S26]** SBSW scenario price ranges (scenarios)
  - ok=True; base mid=28.572488271382763; headwinds=1; tailwinds=8

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



---

# Template: Full diligence (`deep`)

# SBSW — Planned Research Report

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
  - Latest 10-K; extract Item 1 (Business), Item 1A, and Item 7
- **Business overview (Item 1)** (`business`): summarize_item_1
  - Company setup from 10-K Item 1 Business
- **Risk factors (Item 1A)** (`risks`): summarize_item_1a
  - Qualitative risks from the filing
- **MD&A (Item 7)** (`mda`): summarize_item_7
  - Management discussion, tone, guidance cues

## Fundamentals [S1]
- Company: D/B/A Sibanye-Stillwater Limite
- Sector / industry: Basic Materials / Other Precious Metals & Mining
- Price: 8.55
- 52-week range: $7.10 – $21.29
- Market cap: $6.18B
- Enterprise value: $43.47B
- Shares outstanding: 707.64M
- Beta: 0.863
- Book equity: $39.53B
- Revenue (latest): $129.68B
- EBITDA (latest): $12.67B
- Free cash flow (latest): $1.10B
- Operating income: $25.06B
- Operating margin: 19.3%
- EV / EBITDA: 3.4x
- ROIC: 5.0%
- FCF yield: 17.8%
- Debt / Equity: 1.1107625360522189
- FCF / share: $1.55
- Revenue / share: $183.25

### Capital structure
- Cash: $17.18B
- Short-term debt: $11.40B
- Long-term debt: $31.86B
- Total debt: $43.90B
- Net debt: $26.73B
- Net debt / EBITDA: 2.1x

### Growth
- Revenue CAGR: -2.1%
- FCF CAGR: —
- Latest revenue YoY: 15.6%
- Latest FCF YoY: 109.6%

### Market expectations (yfinance, sparse)
- Mean target: $12.52
- Target range: $8.91 – $16.13
- Recommendation: buy

_Consensus revenue/EBITDA forecasts are often unavailable via free feeds; treat targets as point-in-time only._

### Historical KPIs (multi-year)

| Year | Revenue | OCF | Capex | FCF | EBITDA | LT debt | Cash | Net debt | Net income |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2025 | $129.68B | $21.41B | $20.31B | $1.10B | $12.67B | $31.86B | $17.18B | $14.68B | -$5.17B |
| 2024 | $112.13B | $10.11B | $21.57B | -$11.46B | $7.86B | $41.13B | $16.05B | $25.09B | -$7.30B |
| 2023 | $113.68B | $7.09B | $22.41B | -$15.32B | -$27.52B | $24.95B | $25.56B | -$614.00M | -$37.77B |
| 2022 | $138.29B | $15.54B | $15.90B | -$356.00M | $37.13B | $22.61B | $26.08B | -$3.47B | $18.40B |

## Charts

### Revenue & FCF history
![Revenue & FCF history](/charts/SBSW_deep_revenue_fcf.png)

### DCF scenario prices
![DCF scenario prices](/charts/SBSW_deep_dcf_scenarios.png)

### Base-case FCF path
![Base-case FCF path](/charts/SBSW_deep_base_fcf_path.png)

## DCF valuation (base / bull / bear) [S2]

> Simplified revenue->FCF DCF. Not investment advice; assumptions are editable heuristics.

- Spot price: $8.55
- Base revenue: $129.68B
- Shares: 707,641,816
- Net debt (Debt−Cash): $26.73B

| Scenario | Growth | FCF margin | WACC | Term. g | Equity value | Share price | Upside |
|----------|--------|------------|------|---------|--------------|-------------|--------|
| bear | 8.6% | 0.5% | 12.0% | 1.5% | -$18.38B | $-25.97 | -403.8% |
| base | 15.6% | 1.0% | 10.0% | 2.5% | $3.59B | $5.08 | -40.6% |
| bull | 22.6% | 4.0% | 9.0% | 3.0% | $171.36B | $242.16 | 2732.3% |

### Assumption notes
- Base revenue growth seeded from historical rate (15.6%).

- _bear: model equity value is negative after net debt (-18,378,907,160); showing $-25.97/sh._

### Base-case projected FCF

- Year 1: revenue $149.97B, FCF $1.50B (PV $1.36B)
- Year 2: revenue $173.44B, FCF $1.73B (PV $1.43B)
- Year 3: revenue $200.58B, FCF $2.01B (PV $1.51B)
- Year 4: revenue $231.98B, FCF $2.32B (PV $1.58B)
- Year 5: revenue $268.28B, FCF $2.68B (PV $1.67B)
- Terminal value $36.66B (PV $22.77B)

## Web research — web_research

- Queries: Deep diligence: fundamentals, DCF, web, 10-K risks & MD&A
- Unique hits: 4
- Pages fetched: 2/3

### Web synthesis — web_research (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, litigation, revenue, margin, customer, product, market

- Connects to live market data via MCP servers to deliver company deep dives, due diligence reports, competitive landscape analysis, market sentiment, and DCF-based intrinsic value estimates — all from natural language prompts.
- [HIT] Deep Due Diligence Investors | | duediligenceclub.com | https://duediligenceclub.com/ A comprehensive online course offering due diligence training, equipping investors with essential skills to evaluate deals, mitigate risks, and make informed investment decisions.
- You've been through preliminary Q&A sessions, shared high-level metrics, and convinced them on market and team.
- But now they want to see everything: your code architecture, financial models, legal structure, intellectual property, customer contracts, and every assumption that powers your business.
- Three diligence domains and their focus areas Technical diligence examines your product's foundation, scalability, and development practices.
- Financial diligence goes beyond basic metrics to examine unit economics modeling, cash flow forecasting, customer cohort analysis  [PAGE] GitHub - Lunatic16/deep-financial-research: A Claude/Qwen/Gemini skill for institutional-grade investment research.
- Connects to live market data via MCP servers to deliver company deep dives, due diligence reports, competitive landscape analysis, market sentiment, and DCF-based intrinsic value estimates — all from natural language prompts.
- Connects to live market data via MCP servers to deliver company deep dives, due diligence reports, competitive landscape analysis, market sentiment, and DCF-based intrinsic value estimates — all from natural language prompts.

### Sources found
- [Deep Diligence Checklist for Startup Founders | Flux Capital Academy ...](https://www.fluxcapital.com/academy/boards-and-diligence/boards-and-diligence-deep-diligence-technical-financial-and-legal)
  - Deep diligence checklist for technical, financial, and legal review: prepare data rooms, models, IP, contracts, and investor Q&A for Series A.
- [PDF Checklist for DCF Valuation](https://pages.stern.nyu.edu/~adamodar/pdfiles/eqnotes/DCFtodolist.pdf)
  - Checklist for DCF Valuation Checklist for DCF Valuation
- [GitHub - Lunatic16/deep-financial-research: A Claude/Qwen/Gemini skill ...](https://github.com/Lunatic16/deep-financial-research)
  - A Claude/Qwen/Gemini skill for institutional-grade investment research. Connects to live market data via MCP servers to deliver company deep dives, due dilig…
- [Deep Due Diligence Investors |](https://duediligenceclub.com/)
  - A comprehensive online course offering due diligence training, equipping investors with essential skills to evaluate deals, mitigate risks, and make informed…

### Search warnings
- news:Deep diligence: fundamentals, DCF, web, 10-K risks & MD&A: No results found.

## Put opportunities (heuristic) [S3]
- Expiration: 2026-09-18 (DTE 52)
- Candidates: 0
- ATM IV (est.): 6.3%
- IV rank: — (1 local samples)
- HV rank (20d realized): 17.0%


_Note: Delta band approximated via % OTM when greeks are unavailable; IV rank needs ~20+ local daily IV samples (have 1); run the options screen over time to build history.; HV rank is realized-vol rank (20d HV vs ~1y); useful when IV history is thin._

## SEC filing [S10]
- Extraction OK: False
- Item 1 chars: 0
- Item 1A chars: 0
- Item 7 chars: 0
- Meta: {'source': 'cache', 'path': 'C:\\DevWork\\equity_research_agent\\data\\filings\\SBSW_10k.txt'}

## Company setup & business model

No Item 1 Business text extracted.

_Source: latest 10-K Item 1 (Business), summarized locally._

## Qualitative analysis (local LLM)

### Item 1 — Business
No Item 1 Business text extracted.


### Item 1A — Risk Factors
No text extracted.


### Item 7 — MD&A
No text extracted.


## Research loop (think → act)

1. _heuristic_ — Coverage looks adequate for this pass; stopping iterative loop.

## Sources

- **[S1]** SBSW fundamentals (yfinance)
  - D/B/A Sibanye-Stillwater Limite: price=8.55, rev=129677000000.0, fcf=1100000000.0, shares=707641816.0, rev_cagr=-0.02120257146003901, ROIC=0.04982491094608465, FCF yield=0.17785…
- **[S2]** SBSW DCF valuation (dcf)
  - Base share price=5.0789177948722735, bull=242.1630162522678, bear=-25.972047927162336
- **[S3]** SBSW put screen (yfinance_options)
  - Expiration 2026-09-18 (DTE 52): 0 candidates; IV=0.062509375, IV rank=None, HV rank=0.17036629274351578. Delta band approximated via % OTM when greeks are unavailable; IV rank n…
- **[S4]** Deep Diligence Checklist for Startup Founders | Flux Capital Academy ... (web) — https://www.fluxcapital.com/academy/boards-and-diligence/boards-and-diligence-deep-diligence-technical-financial-and-legal
  - Deep diligence checklist for technical, financial, and legal review: prepare data rooms, models, IP, contracts, and investor Q&A for Series A.
- **[S5]** PDF Checklist for DCF Valuation (web) — https://pages.stern.nyu.edu/~adamodar/pdfiles/eqnotes/DCFtodolist.pdf
  - Checklist for DCF Valuation Checklist for DCF Valuation
- **[S6]** GitHub - Lunatic16/deep-financial-research: A Claude/Qwen/Gemini skill ... (web) — https://github.com/Lunatic16/deep-financial-research
  - A Claude/Qwen/Gemini skill for institutional-grade investment research. Connects to live market data via MCP servers to deliver company deep dives, due diligence reports, compet…
- **[S7]** Deep Due Diligence Investors | (web) — https://duediligenceclub.com/
  - A comprehensive online course offering due diligence training, equipping investors with essential skills to evaluate deals, mitigate risks, and make informed investment decisions.
- **[S8]** Deep Diligence Checklist for Startup Founders | Flux Capital Academy | Flux Capital (web_page) — https://www.fluxcapital.com/academy/boards-and-diligence/boards-and-diligence-deep-diligence-technical-financial-and-legal
  - Deep Diligence Checklist for Startup Founders | Flux Capital Academy | Flux Capital Deep diligence: technical, financial, and legal Author Ari Stiegler Managing Partner, Flux Ca…
- **[S9]** GitHub - Lunatic16/deep-financial-research: A Claude/Qwen/Gemini skill for institutional-grade investment research. Connects to live market data via MCP servers to deliver company deep dives, due diligence reports, competitive landscape analysis, market sentiment, and DCF-based intrinsic value estimates — all from natural language prompts. · GitHub (web_page) — https://github.com/Lunatic16/deep-financial-research
  - GitHub - Lunatic16/deep-financial-research: A Claude/Qwen/Gemini skill for institutional-grade investment research. Connects to live market data via MCP servers to deliver compa…
- **[S10]** SBSW 10-K (sec)
  - Item 1 chars=0, Item 1A chars=0, Item 7 chars=0, ok=False, source=cache
- **[S11]** Item 1 Business summary (nlp)
  - ### Item 1 — Business No Item 1 Business text extracted. 
- **[S12]** Item 1A summary (nlp)
  - ### Item 1A — Risk Factors No text extracted. 
- **[S13]** Item 7 summary (nlp)
  - ### Item 7 — MD&A No text extracted.

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



---

# Template: Options income (`income`)

# SBSW — Planned Research Report

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
- Company: D/B/A Sibanye-Stillwater Limite
- Sector / industry: Basic Materials / Other Precious Metals & Mining
- Price: 8.55
- 52-week range: $7.10 – $21.29
- Market cap: $6.18B
- Enterprise value: $43.47B
- Shares outstanding: 707.64M
- Beta: 0.863
- Book equity: $39.53B
- Revenue (latest): $129.68B
- EBITDA (latest): $12.67B
- Free cash flow (latest): $1.10B
- Operating income: $25.06B
- Operating margin: 19.3%
- EV / EBITDA: 3.4x
- ROIC: 5.0%
- FCF yield: 17.8%
- Debt / Equity: 1.1107625360522189
- FCF / share: $1.55
- Revenue / share: $183.25

### Capital structure
- Cash: $17.18B
- Short-term debt: $11.40B
- Long-term debt: $31.86B
- Total debt: $43.90B
- Net debt: $26.73B
- Net debt / EBITDA: 2.1x

### Growth
- Revenue CAGR: -2.1%
- FCF CAGR: —
- Latest revenue YoY: 15.6%
- Latest FCF YoY: 109.6%

### Market expectations (yfinance, sparse)
- Mean target: $12.52
- Target range: $8.92 – $16.14
- Recommendation: buy

_Consensus revenue/EBITDA forecasts are often unavailable via free feeds; treat targets as point-in-time only._

### Historical KPIs (multi-year)

| Year | Revenue | OCF | Capex | FCF | EBITDA | LT debt | Cash | Net debt | Net income |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2025 | $129.68B | $21.41B | $20.31B | $1.10B | $12.67B | $31.86B | $17.18B | $14.68B | -$5.17B |
| 2024 | $112.13B | $10.11B | $21.57B | -$11.46B | $7.86B | $41.13B | $16.05B | $25.09B | -$7.30B |
| 2023 | $113.68B | $7.09B | $22.41B | -$15.32B | -$27.52B | $24.95B | $25.56B | -$614.00M | -$37.77B |
| 2022 | $138.29B | $15.54B | $15.90B | -$356.00M | $37.13B | $22.61B | $26.08B | -$3.47B | $18.40B |

## Charts

### Revenue & FCF history
![Revenue & FCF history](/charts/SBSW_income_revenue_fcf.png)

## Web research — web_research

- Queries: SBSW news, D/B/A Sibanye-Stillwater Limite earnings OR catalyst
- Unique hits: 12
- Pages fetched: 1/3

### Web synthesis — web_research (rule-based fallback — Ollama unavailable)
**Keyword hits:** revenue, product, service, market, operations, network, subsidiary

- It operates its flagship television channel which has a nationwide network of 10 regional stations, and three radio networks.
- SBS has provided digital terrestrial television service in the ATSC format since 2001, and T-DMB (Digital Multimedia Broadcasting) service since 2005.
- [HIT] News & investors - Sibanye-Stillwater | www.sibanyestillwater.com | https://www.sibanyestillwater.com/news-investors/ Sibanye-Stillwater (JSE:SSW, NYSE:SBSW) is a multinational mining and metals processing group with a diverse portfolio of operations, projects and investments ...
- [HIT] SBSW Stock Quote Price and Forecast - CNN | www.cnn.com | https://www.cnn.com/markets/stocks/SBSW View Sibanye Stillwater Limited Sponsored ADR SBSW stock quote prices, financial information, real-time forecasts, and company news from CNN.
- | Kalkine Media | https://kalkinemedia.com/us/stocks/metal-and-mining/why-is-sibanye-gold-nysesbsw-watching-precious-metals-trends Explore Sibanye Gold (NYSE:SBSW), precious metals mining, recycling operations, global assets, production portfolio, and its ...
- [HIT] Sibanye Stillwater appeals US trade ruling over Russian palladium import dumping | Seeking Alpha on MSN | https://www.msn.com/en-us/money/markets/sibanye-stillwater-appeals-us-trade-ruling-over-russian-palladium-import-dumping/ar-AA28nWX2?ocid=BingNewsVerp Sibanye Stillwater (SBSW) said Tuesday it is appealing a recent U.S.
- [HIT] Sibanye Stillwater Files Form 6-K Notice of Market Release with U.S.
- SEC | The Globe and Mail | https://www.theglobeandmail.com/investing/markets/stocks/SBSW/pressreleases/2627120/sibanye-stillwater-files-form-6-k-notice-of-market-release-with-us-sec/ Detailed price information for Sibanye Gold Ltd ADR (SBSW-N) from The Globe and Mail including charting and trades.

### Sources found
- [SBS Newstech](https://en.wikipedia.org/wiki/SBS_Newstech)
  - Seoul Broadcasting System (SBS; Korean: 에스비에스) is one of the leading South Korean television and radio broadcasters. The broadcaster legally became known as …
- [Sibanye Stillwater Limited (SBSW) Stock Price, News, Quote & History](https://finance.yahoo.com/quote/SBSW/)
  - Sibanye-Stillwater (SBSW) is actively managing its debt through significant tender offers while exploring growth opportunities in precious metals and healthc…
- [News & investors - Sibanye-Stillwater](https://www.sibanyestillwater.com/news-investors/)
  - Sibanye-Stillwater (JSE:SSW, NYSE:SBSW) is a multinational mining and metals processing group with a diverse portfolio of operations, projects and investment…
- [SBSW Stock Quote Price and Forecast - CNN](https://www.cnn.com/markets/stocks/SBSW)
  - View Sibanye Stillwater Limited Sponsored ADR SBSW stock quote prices, financial information, real-time forecasts, and company news from CNN.
- [Why Is Sibanye Gold (NYSE:SBSW) Watching Precious Metals Trends?](https://kalkinemedia.com/us/stocks/metal-and-mining/why-is-sibanye-gold-nysesbsw-watching-precious-metals-trends)
  - Explore Sibanye Gold (NYSE:SBSW), precious metals mining, recycling operations, global assets, production portfolio, and its ...
- [Sibanye Stillwater appeals US trade ruling over Russian palladium import dumping](https://www.msn.com/en-us/money/markets/sibanye-stillwater-appeals-us-trade-ruling-over-russian-palladium-import-dumping/ar-AA28nWX2?ocid=BingNewsVerp)
  - Sibanye Stillwater (SBSW) said Tuesday it is appealing a recent U.S. International Trade Commission ruling that imports of Russian palladium do not pose an i…
- [Sibanye Stillwater Files Form 6-K Notice of Market Release with U.S. SEC](https://www.theglobeandmail.com/investing/markets/stocks/SBSW/pressreleases/2627120/sibanye-stillwater-files-form-6-k-notice-of-market-release-with-us-sec/)
  - Detailed price information for Sibanye Gold Ltd ADR (SBSW-N) from The Globe and Mail including charting and trades.
- [Sibanye Stillwater Files July 2026 Form 6-K with U.S. Regulators](https://www.theglobeandmail.com/investing/markets/stocks/SBSW-N/pressreleases/3098322/sibanye-stillwater-files-july-2026-form-6-k-with-u-s-regulators/)
  - Detailed price information for Sibanye Gold Ltd ADR (SBSW-N) from The Globe and Mail including charting and trades.
- [D/B/A Sibanye-Stillwater Limited Earnings and Revenue – NYSE...](https://www.tradingview.com/symbols/NYSE-SBSW/financials-earnings/?earnings-period=FQ&revenues-period=FQ)
  - Watch D/B/A Sibanye-Stillwater Limited key financial stats — earnings and revenue. Keep track of their change over time and use estimation numbers to develop…
- [D/B/A Sibanye-Stillwater Limite (SBSW) H1 FY2025 earnings call...](https://finance.yahoo.com/quote/SBSW/earnings/SBSW-H1-2025-earnings_call-340096.html)
  - Earnings call Sibanye-Stillwater delivered a strong H1 2025, with adjusted EBITDA up 120% YoY (or 51% excluding Section 45X credits), and net debt/EBITDA red…
- [D/B/A Sibanye-Stillwater Limited ADS (SBSW) Earnings... | Nasdaq](https://www.nasdaq.com/market-activity/stocks/sbsw/earnings)
  - Find annual and quearterly earnings data for D/B/A Sibanye-Stillwater Limited ADS (SBSW) including earnings per share, earnings forecasts at Nasdaq.com.
- [SBSW: D/B/A Sibanye-Stillwater Limite Option... | OptionCharts](https://optioncharts.io/options/SBSW?tvwidgetsymbol=NYSE:SBSW)
  - D/B/A Sibanye-Stillwater Limited New York Stock Exchange.Upcoming Earnings. EPS. Market Cap.

### Search warnings
- news:D/B/A Sibanye-Stillwater Limite earnings OR catalyst: No results found.

## Put opportunities (heuristic) [S2]
- Expiration: 2026-09-18 (DTE 52)
- Candidates: 0
- ATM IV (est.): 6.3%
- IV rank: — (1 local samples)
- HV rank (20d realized): 17.0%


_Note: Delta band approximated via % OTM when greeks are unavailable; IV rank needs ~20+ local daily IV samples (have 1); run the options screen over time to build history.; HV rank is realized-vol rank (20d HV vs ~1y); useful when IV history is thin._

## Research loop (think → act)

1. _heuristic_ — Coverage looks adequate for this pass; stopping iterative loop.

## Sources

- **[S1]** SBSW fundamentals (yfinance)
  - D/B/A Sibanye-Stillwater Limite: price=8.55, rev=129677000000.0, fcf=1100000000.0, shares=707641816.0, rev_cagr=-0.02120257146003901, ROIC=0.04982491094608465, FCF yield=0.17785…
- **[S2]** SBSW put screen (yfinance_options)
  - Expiration 2026-09-18 (DTE 52): 0 candidates; IV=0.062509375, IV rank=None, HV rank=0.17036629274351578. Delta band approximated via % OTM when greeks are unavailable; IV rank n…
- **[S3]** SBS Newstech (web) — https://en.wikipedia.org/wiki/SBS_Newstech
  - Seoul Broadcasting System (SBS; Korean: 에스비에스) is one of the leading South Korean television and radio broadcasters. The broadcaster legally became known as SBS in March 2000, c…
- **[S4]** Sibanye Stillwater Limited (SBSW) Stock Price, News, Quote & History (web) — https://finance.yahoo.com/quote/SBSW/
  - Sibanye-Stillwater (SBSW) is actively managing its debt through significant tender offers while exploring growth opportunities in precious metals and healthcare ...
- **[S5]** News & investors - Sibanye-Stillwater (web) — https://www.sibanyestillwater.com/news-investors/
  - Sibanye-Stillwater (JSE:SSW, NYSE:SBSW) is a multinational mining and metals processing group with a diverse portfolio of operations, projects and investments ...
- **[S6]** SBSW Stock Quote Price and Forecast - CNN (web) — https://www.cnn.com/markets/stocks/SBSW
  - View Sibanye Stillwater Limited Sponsored ADR SBSW stock quote prices, financial information, real-time forecasts, and company news from CNN.
- **[S7]** Why Is Sibanye Gold (NYSE:SBSW) Watching Precious Metals Trends? (web) — https://kalkinemedia.com/us/stocks/metal-and-mining/why-is-sibanye-gold-nysesbsw-watching-precious-metals-trends
  - Explore Sibanye Gold (NYSE:SBSW), precious metals mining, recycling operations, global assets, production portfolio, and its ...
- **[S8]** Sibanye Stillwater appeals US trade ruling over Russian palladium import dumping (web) — https://www.msn.com/en-us/money/markets/sibanye-stillwater-appeals-us-trade-ruling-over-russian-palladium-import-dumping/ar-AA28nWX2?ocid=BingNewsVerp
  - Sibanye Stillwater (SBSW) said Tuesday it is appealing a recent U.S. International Trade Commission ruling that imports of Russian palladium do not pose an imminent threat to U.…
- **[S9]** Sibanye Stillwater Files Form 6-K Notice of Market Release with U.S. SEC (web) — https://www.theglobeandmail.com/investing/markets/stocks/SBSW/pressreleases/2627120/sibanye-stillwater-files-form-6-k-notice-of-market-release-with-us-sec/
  - Detailed price information for Sibanye Gold Ltd ADR (SBSW-N) from The Globe and Mail including charting and trades.
- **[S10]** Sibanye Stillwater Files July 2026 Form 6-K with U.S. Regulators (web) — https://www.theglobeandmail.com/investing/markets/stocks/SBSW-N/pressreleases/3098322/sibanye-stillwater-files-july-2026-form-6-k-with-u-s-regulators/
  - Detailed price information for Sibanye Gold Ltd ADR (SBSW-N) from The Globe and Mail including charting and trades.
- **[S11]** Sibanye Stillwater Limited (SBSW) Stock Price, News, Quote & History - Yahoo Finance (web_page) — https://finance.yahoo.com/quote/SBSW/
  - Sibanye Stillwater Limited (SBSW) Stock Price, News, Quote & History - Yahoo Finance Oops, something went wrong Skip to navigation Skip to main content Skip to right column We a…

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



---

# Template: Fast quant (`fast`)

# SBSW — Planned Research Report

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
- Company: D/B/A Sibanye-Stillwater Limite
- Sector / industry: Basic Materials / Other Precious Metals & Mining
- Price: 8.55
- 52-week range: $7.10 – $21.29
- Market cap: $6.18B
- Enterprise value: $43.47B
- Shares outstanding: 707.64M
- Beta: 0.863
- Book equity: $39.53B
- Revenue (latest): $129.68B
- EBITDA (latest): $12.67B
- Free cash flow (latest): $1.10B
- Operating income: $25.06B
- Operating margin: 19.3%
- EV / EBITDA: 3.4x
- ROIC: 5.0%
- FCF yield: 17.8%
- Debt / Equity: 1.1107625360522189
- FCF / share: $1.55
- Revenue / share: $183.25

### Capital structure
- Cash: $17.18B
- Short-term debt: $11.40B
- Long-term debt: $31.86B
- Total debt: $43.90B
- Net debt: $26.73B
- Net debt / EBITDA: 2.1x

### Growth
- Revenue CAGR: -2.1%
- FCF CAGR: —
- Latest revenue YoY: 15.6%
- Latest FCF YoY: 109.6%

### Market expectations (yfinance, sparse)
- Mean target: $12.53
- Target range: $8.92 – $16.14
- Recommendation: buy

_Consensus revenue/EBITDA forecasts are often unavailable via free feeds; treat targets as point-in-time only._

### Historical KPIs (multi-year)

| Year | Revenue | OCF | Capex | FCF | EBITDA | LT debt | Cash | Net debt | Net income |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2025 | $129.68B | $21.41B | $20.31B | $1.10B | $12.67B | $31.86B | $17.18B | $14.68B | -$5.17B |
| 2024 | $112.13B | $10.11B | $21.57B | -$11.46B | $7.86B | $41.13B | $16.05B | $25.09B | -$7.30B |
| 2023 | $113.68B | $7.09B | $22.41B | -$15.32B | -$27.52B | $24.95B | $25.56B | -$614.00M | -$37.77B |
| 2022 | $138.29B | $15.54B | $15.90B | -$356.00M | $37.13B | $22.61B | $26.08B | -$3.47B | $18.40B |

## Charts

### Revenue & FCF history
![Revenue & FCF history](/charts/SBSW_fast_revenue_fcf.png)

### DCF scenario prices
![DCF scenario prices](/charts/SBSW_fast_dcf_scenarios.png)

### Base-case FCF path
![Base-case FCF path](/charts/SBSW_fast_base_fcf_path.png)

## DCF valuation (base / bull / bear) [S2]

> Simplified revenue->FCF DCF. Not investment advice; assumptions are editable heuristics.

- Spot price: $8.55
- Base revenue: $129.68B
- Shares: 707,641,816
- Net debt (Debt−Cash): $26.73B

| Scenario | Growth | FCF margin | WACC | Term. g | Equity value | Share price | Upside |
|----------|--------|------------|------|---------|--------------|-------------|--------|
| bear | 8.6% | 0.5% | 12.0% | 1.5% | -$18.38B | $-25.97 | -403.8% |
| base | 15.6% | 1.0% | 10.0% | 2.5% | $3.59B | $5.08 | -40.6% |
| bull | 22.6% | 4.0% | 9.0% | 3.0% | $171.36B | $242.16 | 2732.3% |

### Assumption notes
- Base revenue growth seeded from historical rate (15.6%).

- _bear: model equity value is negative after net debt (-18,378,907,160); showing $-25.97/sh._

### Base-case projected FCF

- Year 1: revenue $149.97B, FCF $1.50B (PV $1.36B)
- Year 2: revenue $173.44B, FCF $1.73B (PV $1.43B)
- Year 3: revenue $200.58B, FCF $2.01B (PV $1.51B)
- Year 4: revenue $231.98B, FCF $2.32B (PV $1.58B)
- Year 5: revenue $268.28B, FCF $2.68B (PV $1.67B)
- Terminal value $36.66B (PV $22.77B)

## Put opportunities (heuristic) [S3]
- Expiration: 2026-09-18 (DTE 52)
- Candidates: 0
- ATM IV (est.): 6.3%
- IV rank: — (1 local samples)
- HV rank (20d realized): 17.0%


_Note: Delta band approximated via % OTM when greeks are unavailable; IV rank needs ~20+ local daily IV samples (have 1); run the options screen over time to build history.; HV rank is realized-vol rank (20d HV vs ~1y); useful when IV history is thin._

## Research loop (think → act)

1. _heuristic_ — Coverage looks adequate for this pass; stopping iterative loop.

## Sources

- **[S1]** SBSW fundamentals (yfinance)
  - D/B/A Sibanye-Stillwater Limite: price=8.55, rev=129677000000.0, fcf=1100000000.0, shares=707641816.0, rev_cagr=-0.02120257146003901, ROIC=0.04982491094608465, FCF yield=0.17785…
- **[S2]** SBSW DCF valuation (dcf)
  - Base share price=5.0789177948722735, bull=242.1630162522678, bear=-25.972047927162336
- **[S3]** SBSW put screen (yfinance_options)
  - Expiration 2026-09-18 (DTE 52): 0 candidates; IV=0.062509375, IV rank=None, HV rank=0.17036629274351578. Delta band approximated via % OTM when greeks are unavailable; IV rank n…

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
