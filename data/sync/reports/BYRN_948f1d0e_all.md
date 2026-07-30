# BYRN — Full research pack

> Not investment advice. Local research draft only.

**Templates:** memo, valuation, deep, income, fast
**Generated:** 2026-07-24T16:28:54.103085+00:00



---

# Template: Institutional deep dive (memo) (`memo`)

# BYRN — Planned Research Report

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

**Fundamentals error:** Failed to perform, curl: (28) Connection timed out after 30008 milliseconds. See https://curl.se/libcurl/c/libcurl-errors.html first for more details.

## DCF valuation (base / bull / bear) [S3]

> Simplified revenue->FCF DCF. Not investment advice; assumptions are editable heuristics.

- **Error:** Cannot run DCF without positive base revenue.
- **Error:** Cannot run DCF without shares outstanding.

## Valuation — EV/EBITDA scenarios [S2]

> Priced-in model: implied price = (EBITDA × EV/EBITDA − net debt) ÷ shares. Not a forecast.

- Net debt used: $0

| Scenario | EBITDA | EV/EBITDA | Implied EV | Equity value | Implied price |
|---|---:|---:|---:|---:|---:|
| bear | $700.00M | 6.0x | $4.20B | $4.20B | — |
| base | $1.00B | 8.0x | $8.00B | $8.00B | — |
| bull | $1.20B | 10.0x | $12.00B | $12.00B | — |

- EBITDA missing or non-positive; scenarios use placeholder $1B EBITDA — edit before relying on prices.
- No current EV/EBITDA; defaulted base multiple to 8.0x.
- **Error:** Missing shares outstanding

## Scenario price ranges (headwinds & tailwinds) [S39]

> Medium-term (18–36 months (medium / medium-long term)) driver → EV/EBITDA bridge. Distinct from the FCF DCF path. Not investment advice.

- Anchor multiple: 8.0x (driver_ev_ebitda_bridge)
- Anchor EBITDA: $1.00B
- Driver extraction: `rules`

### Headwinds (bear-case fuel)

- **Balance-sheet / refinancing pressure** — sector=None industry=None revenue=None ebitda=None fcf=None net_debt=None nd_ebitda=None target=None rec=None _(source: fundamentals)_
- **Competitive / pricing pressure** — Byrna Technologies Inc. (BYRN) Interactive Stock Chart - Yahoo Finance Interactive Chart for Byrna Technologies Inc. (BYRN), analyze all the data with a huge range of indicators.Cr _(source: web)_
- **Regulatory / legal risk** — Market Demand: Definition, How to Calculate, Determinants What’s it: Market demand is the sum of individual demand in the market at a given price. Economists define demand as our w _(source: web)_

### Tailwinds (bull-case fuel)

- **Growth / execution upside** — Byrna Technologies (BYRN) Stock Forecast & Price TargetByrna Technologies Inc. (BYRN): A Bullish Thesis for Long ...BYRN | Byrna Technologies, Inc. Common Institutional ...BYRN - B _(source: web)_
- **Product / pricing power** — Byrna Technologies (BYRN) Stock Forecast & Analyst Price Targets Stock forecasts and analyst price target predictions for Byrna Technologies Inc. (BYRN) stock, with detailed revenu _(source: web)_
- **Capital returns / FCF inflection** — Byrna Technologies (Nasdaq:BYRN) - Stock Analysis - Simply Wall St Research Byrna Technologies' (Nasdaq:BYRN) fundamentals, past performance, valuation, dividends and more. _(source: web)_
- **Contract / backlog wins** — Byrna Technologies Has One Critical Flaw: Recurring Revenue May 11, 2026 ... Byrna Technologies (BYRN) has fallen 70% YTD and now ... contract revenue from law enforcement can make _(source: web)_

### Price ranges by case

| Case | Prob. | Metric vs TTM | Multiple | Price low | Mid | High | Upside vs spot |
|---|---:|---:|---:|---:|---:|---:|---:|
| bear | 0.24 | — | — | — | — | — | Missing shares outstanding |
| base | 0.46 | — | — | — | — | — | Missing shares outstanding |
| bull | 0.3 | — | — | — | — | — | Missing shares outstanding |

#### Bear — headwinds dominate

Headwinds bite: weaker operating trajectory and multiple compression. Equity duration shrinks if cash generation fails to offset leverage / competitive pressure.

- Driver: **Balance-sheet / refinancing pressure** — sector=None industry=None revenue=None ebitda=None fcf=None net_debt=None nd_ebitda=None target=None rec=None
- Driver: **Competitive / pricing pressure** — Byrna Technologies Inc. (BYRN) Interactive Stock Chart - Yahoo Finance Interactive Chart for Byrna Technologies Inc. (BYRN), analyze all the data with a huge ra
- Driver: **Regulatory / legal risk** — Market Demand: Definition, How to Calculate, Determinants What’s it: Market demand is the sum of individual demand in the market at a given price. Economists de

#### Base — mixed execution

Balanced path: some tailwinds offset headwinds. Operating scale roughly holds with modest repair/normalization; valuation stays near the current EV/EBITDA anchor.

- Driver: **Growth / execution upside** — Byrna Technologies (BYRN) Stock Forecast & Price TargetByrna Technologies Inc. (BYRN): A Bullish Thesis for Long ...BYRN | Byrna Technologies, Inc. Common Insti
- Driver: **Product / pricing power** — Byrna Technologies (BYRN) Stock Forecast & Analyst Price Targets Stock forecasts and analyst price target predictions for Byrna Technologies Inc. (BYRN) stock, 
- Driver: **Balance-sheet / refinancing pressure** — sector=None industry=None revenue=None ebitda=None fcf=None net_debt=None nd_ebitda=None target=None rec=None
- Driver: **Competitive / pricing pressure** — Byrna Technologies Inc. (BYRN) Interactive Stock Chart - Yahoo Finance Interactive Chart for Byrna Technologies Inc. (BYRN), analyze all the data with a huge ra

#### Bull — tailwinds dominate

Tailwinds compound: operating improvement plus a re-rating toward peer or recovery multiples as balance-sheet and growth narratives improve.

- Driver: **Growth / execution upside** — Byrna Technologies (BYRN) Stock Forecast & Price TargetByrna Technologies Inc. (BYRN): A Bullish Thesis for Long ...BYRN | Byrna Technologies, Inc. Common Insti
- Driver: **Product / pricing power** — Byrna Technologies (BYRN) Stock Forecast & Analyst Price Targets Stock forecasts and analyst price target predictions for Byrna Technologies Inc. (BYRN) stock, 
- Driver: **Capital returns / FCF inflection** — Byrna Technologies (Nasdaq:BYRN) - Stock Analysis - Simply Wall St Research Byrna Technologies' (Nasdaq:BYRN) fundamentals, past performance, valuation, dividen
- Driver: **Contract / backlog wins** — Byrna Technologies Has One Critical Flaw: Recurring Revenue May 11, 2026 ... Byrna Technologies (BYRN) has fallen 70% YTD and now ... contract revenue from law 

### Method notes

- Item 1A risks weighted toward headwinds.
- Current ev_ebitda multiple missing; anchored at 8.0x.
- Mapping follows Gemini/Perplexity-style scenario memos: qualitative drivers → operating metric & multiple paths → share-price ranges over a medium-term horizon.

### Errors

- Missing shares outstanding

## Peer & factor comps

- Sector / industry: — / —
- Peers: —

_No peer data available._

## Earnings, guidance & revision catalysts

_No earnings surprise history available from yfinance._

- Failed to perform, curl: (6) Could not resolve host: finance.yahoo.com. See https://curl.se/libcurl/c/libcurl-errors.html first for more details.

## Recent SEC filings (10-Q / 8-K)

| Date | Form | Description |
|---|---|---|
| 2026-07-09 | 8-K | [FORM 8-K](https://www.sec.gov/Archives/edgar/data/1354866/000143774926023101/byrn20260708_8k.htm) |
| 2026-07-09 | 10-Q | [FORM 10-Q](https://www.sec.gov/Archives/edgar/data/1354866/000143774926023100/byrn20260531_10q.htm) |
| 2026-07-08 | 8-K | [FORM 8-K](https://www.sec.gov/Archives/edgar/data/1354866/000143774926023029/byrn20260707_8k.htm) |
| 2026-06-18 | 8-K | [FORM 8-K](https://www.sec.gov/Archives/edgar/data/1354866/000143774926021142/byrn20260618c_8k.htm) |
| 2026-06-15 | 8-K | [FORM 8-K](https://www.sec.gov/Archives/edgar/data/1354866/000143774926020580/byrn20260612_8k.htm) |
| 2026-04-09 | 8-K | [FORM 8-K](https://www.sec.gov/Archives/edgar/data/1354866/000143774926011821/byrn20260408c_8k.htm) |
| 2026-04-09 | 10-Q | [FORM 10-Q](https://www.sec.gov/Archives/edgar/data/1354866/000143774926011820/byrn20260228_10q.htm) |
| 2026-04-08 | 8-K | [FORM 8-K](https://www.sec.gov/Archives/edgar/data/1354866/000143774926011756/byrn20260408_8k.htm) |
| 2026-03-23 | 8-K | [FORM 8-K](https://www.sec.gov/Archives/edgar/data/1354866/000143774926009296/byrn20260320_8k.htm) |
| 2026-03-19 | 8-K | [FORM 8-K](https://www.sec.gov/Archives/edgar/data/1354866/000143774926008945/byrn20260318_8k.htm) |
| 2026-03-09 | 8-K | [FORM 8-K](https://www.sec.gov/Archives/edgar/data/1354866/000143774926007268/byrn20260306_8k.htm) |
| 2026-03-03 | 8-K | [FORM 8-K](https://www.sec.gov/Archives/edgar/data/1354866/000143774926006482/byrn20260302_8k.htm) |

_Headlines/meta only — documents not fully parsed in this pass._

## Key driver analysis (quarterly)

Pearson / Spearman correlations of quarterly stock returns with fundamentals.

| Driver | Pearson r | p | n | Spearman ρ | p |
|---|---:|---:|---:|---:|---:|
| Revenue growth (YoY) | — | — | — | — | — |
| Free cash flow | — | — | — | — | — |
| FCF margin | — | — | — | — | — |
| Operating cash flow | — | — | — | — | — |
| Long-term debt level | — | — | — | — | — |
| EBITDA | — | — | — | — | — |
| Capex (abs) | — | — | — | — | — |

- Correlations describe association, not causation.
- Small samples (especially regime splits) are directional only.
- Regime split at 2023-12-31 (sample midpoint); directional only.
- Insufficient quarterly overlap for driver correlations.

## Executive summary

BYRN (BYRN) trades near None with market cap — and EV —. Net debt is — (ND/EBITDA —). Latest revenue —, EBITDA —, FCF —.

**Goal focus:** Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers.

What matters most (framework): balance-sheet trajectory, cash generation vs leverage, and whether market expectations (sparse free-data targets) already price execution risk.

EV/EBITDA implied prices — bear — / base — / bull —.

## Company setup & business model

No Item 1 Business text extracted.

_Source: latest 10-K Item 1 (Business), summarized locally._

## Variant perception

- **Consensus frame (sparse):** recommendation=—, mean target=—.
- **Bear:** leverage and execution risk dominate; cash generation fails to cover refinancing / reinvestment needs; equity remains constrained by net debt.
- **Bull:** cash-flow and strategic optionality re-rate the equity as leverage falls and growth/mix improves.
- **Middle:** returns may track free-cash-flow more than headline revenue — verify with driver analysis tab.

## Catalysts & monitoring

- Next earnings window (calendar): unconfirmed
- Peer tape to watch: n/a
- Monitor: FCF vs net debt, leverage (ND/EBITDA), refinancing headlines, and material 8-K strategy updates.
- Recent filing: 8-K on 2026-07-09 — FORM 8-K
- Recent filing: 10-Q on 2026-07-09 — FORM 10-Q
- Recent filing: 8-K on 2026-07-08 — FORM 8-K
- Recent filing: 8-K on 2026-06-18 — FORM 8-K
- Recent filing: 8-K on 2026-06-15 — FORM 8-K

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
| Guidance / outlook | Forward cash/earnings path | Byrna Technologies (BYRN) Stock Forecast & Price TargetByrna Technologies Inc. (BYRN): A Bullish Thesis for Long ...BYRN / Byrna Technologies, Inc. Common Institutional ...BYRN - B | Byrna Technologies (BYRN) Stock Forecast & Price TargetByrna Technologies Inc. (BYRN): A Bullish Thesis for Long ...BYRN | Byrna Technologies, Inc. Common Institutional ...BYRN - Byrna Technologies Inc. Stock - Stock Price ... - FintelByrna Technologies (BYRN) Stock Price, News & AnalysisBYRN Institutional Ownership & Insider Trading - Filings ... |
| Contract / backlog | Demand durability | Byrna Technologies Inc Customers by Division and Industry - CSIMarket Byrna Technologies Inc customers and markets, results by customer and performance relative to BYRN, by company | Byrna Technologies Inc Customers by Division and Industry - CSIMarket |
| Leverage / refinancing | Balance-sheet repair | Byrna Technologies Reports Fiscal First Quarter 2026 Results Apr 9, 2026 ... (“Byrna” or the “Company”) (Nasdaq: BYRN), a personal defense ... leverage proprietary data and insight | Byrna Technologies Reports Fiscal First Quarter 2026 Results |

_Proxies are heuristic extractions from public web/SEC context; verify against primary filings._

## Catalyst calendar

| Window | Catalyst | Notes |
|---|---|---|
| 2026-07-09 | 8-K | FORM 8-K |
| 2026-07-09 | 10-Q | FORM 10-Q |
| 2026-07-08 | 8-K | FORM 8-K |
| 2026-06-18 | 8-K | FORM 8-K |
| 2026-06-15 | 8-K | FORM 8-K |
| 2026-04-09 | 8-K | FORM 8-K |
| 2026-04-09 | 10-Q | FORM 10-Q |
| 2026-04-08 | 8-K | FORM 8-K |
| 2026-03-23 | 8-K | FORM 8-K |
| 2026-03-19 | 8-K | FORM 8-K |
| 2026-03-09 | 8-K | FORM 8-K |
| 2026-03-03 | 8-K | FORM 8-K |
| Oct 22, 2025 | Web event | Byrna Technologies (BYRN) Stock Forecast & Price TargetByrna Technologies Inc. (BYRN): A Bullish Thesis for Long ...BYRN | Byrna Technologie |
| Jul 22, 2025 | Web event | Byrna Technologies' Recent Surge in Investor Interest: A Deep ... |
| Jul 11, 2025 | Web event | BYRN Q2 Deep Dive: Market Skepticism Amid Channel Expansion ... |
| Jul 11, 2025 | Web event | BYRN Q2 Deep Dive: Market Skepticism Amid Channel Expansion ... |
| March 9, 2026 | Web event | Byrna Technologies Stock Guidance | NASDAQ:BYRN | Benzinga |
| Jul 8, 2026 | Web event | Investor Relations :: Byrna Technologies Inc. (BYRN) |
| Oct 22, 2025 | Web event | Byrna Technologies Inc. (BYRN): A Bullish Thesis for Long ... |
| Jul 9, 2026 | Web event | Byrna (NASDAQ:BYRN) Misses Q2 CY2026 Sales Expectations ... |
| Apr 9, 2026 | Web event | Byrna Technologies Reports Fiscal First Quarter 2026 Results |
| May 11, 2026 | Web event | Byrna Technologies Has One Critical Flaw: Recurring Revenue |

## Web research — web_analysts

- Queries: BYRN analyst price target, BYRN stock rating OR consensus OR upgrade OR downgrade, BYRN Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers analyst, BYRN guidance OR investor day OR catalyst
- Unique hits: 22
- Pages fetched: 3/3

### Web synthesis — web_analysts (rule-based fallback — Ollama unavailable)
**Keyword hits:** uncertainty, guidance, revenue, margin, customer, product, service, market

- [HIT] Byrna Technologies (BYRN) Stock Forecast & Price Target | www.marketbeat.com | https://www.marketbeat.com/stocks/NASDAQ/BYRN/forecast/ BYRN's current price target is $7.88.
- Learn why top analysts are making this stock forecast for Byrna Technologies at MarketBeat.
- (BYRN) stock, with detailed revenue and earnings estimates.
- | Asianet Newsable on MSN | https://www.msn.com/en-in/money/markets/why-did-stla-mat-byrn-stocks-tumble-to-52-week-lows-today/ar-AA27BZfD?ocid=BingNewsVerp Stellantis, Mattel, and Byrna Technologies tumbled to fresh lows on Thursday amid regional weaknesses, poor outlook, and Wall Street caution.
- [HIT] Analysts Have Mixed Views on Glacier Bancorp (GBCI) | Insider Monkey · via Yahoo Finance | https://finance.yahoo.com/markets/stocks/articles/analysts-mixed-views-glacier-bancorp-201806470.html Glacier Bancorp, Inc.
- [HIT] What To Expect From Byrna Technologies Inc (BYRN) Q2 2026 Earnings | Yahoo Finance | https://finance.yahoo.com/markets/stocks/articles/expect-byrna-technologies-inc-byrn-131713208.html At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage rates that help you manage your financial life.
- [HIT] Byrna Technologies (BYRN) Stock Price, News & Analysis | www.marketbeat.com | https://www.marketbeat.com/stocks/NASDAQ/BYRN/ Should You Buy or Sell Byrna Technologies Stock?
- Get The Latest BYRN Stock Analysis, Price Target, Earnings Estimates, Headlines, and Short Interest at MarketBeat.

### Sources found
- [Byrna Technologies (BYRN) Stock Forecast & Price Target](https://www.marketbeat.com/stocks/NASDAQ/BYRN/forecast/)
  - BYRN's current price target is $7.88. Learn why top analysts are making this stock forecast for Byrna Technologies at MarketBeat.
- [What is the current Price Target and Forecast for Byrna Technologies (BYRN)](https://www.zacks.com/stock/research/byrn/price-target-stock-forecast)
  - Price Target Based on short-term price targets offered by four analysts, the average price target for Byrna Technologies Inc. comes to $7.63. The forecasts r…
- [Byrna Technologies (BYRN) Stock Forecast & Analyst Price Targets](https://stockanalysis.com/stocks/byrn/forecast/)
  - Stock forecasts and analyst price target predictions for Byrna Technologies Inc. (BYRN) stock, with detailed revenue and earnings estimates.
- [Byrna Technologies Inc. (BYRN) Analyst Insights, Price Targets ...](https://finance.yahoo.com/quote/BYRN/analyst-insights/)
  - Yahoo Finance provides the latest analyst insights, price targets, and recommendations on Byrna Technologies Inc. (BYRN) to help inform your investment strat…
- [Why did STLA, MAT, BYRN stocks tumble to 52-week lows today?](https://www.msn.com/en-in/money/markets/why-did-stla-mat-byrn-stocks-tumble-to-52-week-lows-today/ar-AA27BZfD?ocid=BingNewsVerp)
  - Stellantis, Mattel, and Byrna Technologies tumbled to fresh lows on Thursday amid regional weaknesses, poor outlook, and Wall Street caution.
- [Needham Reiterates Buy on monday.com (MNDY), Sets $250 Price Targe](https://finance.yahoo.com/news/needham-reiterates-buy-monday-com-225907775.html)
  - monday.com Ltd. (NASDAQ:MNDY) is one of the AI Stocks Analysts Are Watching Closely. On August 18,...
- [Analysts Have Mixed Views on Glacier Bancorp (GBCI)](https://finance.yahoo.com/markets/stocks/articles/analysts-mixed-views-glacier-bancorp-201806470.html)
  - Glacier Bancorp, Inc. (NYSE:GBCI) is one of the 11 Best American Bank Stocks to Buy According to Wall Street Analysts. On February 11, Piper Sandler...
- [What To Expect From Byrna Technologies Inc (BYRN) Q2 2026 Earnings](https://finance.yahoo.com/markets/stocks/articles/expect-byrna-technologies-inc-byrn-131713208.html)
  - At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage rate…
- [Byrna Technologies Inc. (BYRN) Stock Price, News, Quote & History ...](https://finance.yahoo.com/quote/BYRN/)
  - Find the latest Byrna Technologies Inc. (BYRN) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Byrna Technologies (BYRN) Stock Price, News & Analysis](https://www.marketbeat.com/stocks/NASDAQ/BYRN/)
  - Should You Buy or Sell Byrna Technologies Stock? Get The Latest BYRN Stock Analysis, Price Target, Earnings Estimates, Headlines, and Short Interest at Marke…
- [BYRN Stock Price | Byrna Technologies Inc. Stock Quote (U.S.: Nasdaq ...](https://www.marketwatch.com/investing/stock/byrn)
  - BYRN | Complete Byrna Technologies Inc. stock news by MarketWatch. View real-time stock prices and stock quotes for a full financial overview.
- [Stocks Under Some Pressure as Optimism Fades Over US-Iran Ceasefire](https://finance.yahoo.com/markets/stocks/articles/stocks-under-pressure-optimism-fades-140947179.html)
  - The S&P 500 Index ($SPX ) (SPY ) today is down -0.04%, the Dow Jones Industrial Average ($DOWI )...

### Search warnings
- news:BYRN Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers analyst: No results found.
- news:BYRN guidance OR investor day OR catalyst: No results found.

## Web research — web_drivers

- Queries: BYRN Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers, BYRN BYRN outlook OR catalyst OR commodity OR uranium OR rare earth OR vanadium, BYRN sector drivers OR market demand, BYRN BYRN backlog OR contract OR refinancing OR leverage
- Unique hits: 16
- Pages fetched: 2/3

### Web synthesis — web_drivers (rule-based fallback — Ollama unavailable)
**Keyword hits:** revenue, customer, product, service, market

- | www.marketbeat.com | https://www.marketbeat.com/stocks/NASDAQ/BYRN/forecast/ BYRN's current price target is $7.88.
- Learn why top analysts are making this stock forecast for Byrna Technologies at MarketBeat.
- (BYRN) is a leading provider of less-lethal self-defense technology with a diverse product portfolio spanning handheld devices, launchers, projectiles, and aerosols.
- (NASDAQ: BYRN) designs, develops and markets non-lethal personal security devices and accessories intended to provide an alternative to traditional firearms.
- (BYRN) is a leading provider of less-lethal self-defense technology with a diverse product portfolio spanning handheld devices, launchers, projectiles, and aerosols.
- The company reported a Q2 2026 loss of $0.44 per share, missing estimates, with revenue declining 42.5...
- [HIT] FinancialContent - Why Byrna (BYRN) Shares Are Sliding Today | markets.financialcontent.com | https://markets.financialcontent.com/stocks/article/stockstory-2026-7-20-why-byrna-byrn-shares-are-sliding-today Shares of non-lethal weapons company Byrna (NASDAQ: BYRN) fell 4.1% in the afternoon session after the company announced the appointment of James White as Senior Vice President of Retail and Channel Growth.
- - Webull | www.webull.com | https://www.webull.com/quote/nasdaq-byrn Webull offers BYRN Ent Holdg (BYRN) historical stock prices, in-depth market analysis, NASDAQ: BYRN real-time stock quote data, in-depth charts, free BYRN options chain data, and a fully built financial calendar to help you invest smart.

### Sources found
- [Investor Relations :: Byrna Technologies Inc. (BYRN)](https://ir.byrna.com/)
  - Jul 8, 2026 · Byrna Technologies Inc. (NASDAQ: BYRN) is a technology company specializing in the areas of Personal Security Devices, Military, Law Enforcemen…
- [Byrna Technologies (BYRN) Stock Forecast & Price TargetByrna Technologies Inc. (BYRN): A Bullish Thesis for Long ...BYRN | Byrna Technologies, Inc. Common Institutional ...BYRN - Byrna Technologies Inc. Stock - Stock Price ... - FintelByrna Technologies (BYRN) Stock Price, News & AnalysisBYRN Institutional Ownership & Insider Trading - Filings ...](https://www.marketbeat.com/stocks/NASDAQ/BYRN/forecast/)
  - BYRN's current price target is $7.88. Learn why top analysts are making this stock forecast for Byrna Technologies at MarketBeat. Oct 22, 2025 · Byrna Techno…
- [Byrna Technologies Inc. (BYRN): A Bullish Thesis for Long ...](https://www.ainvest.com/news/byrna-technologies-byrn-bullish-thesis-long-term-growth-2510/)
  - Oct 22, 2025 · Byrna Technologies Inc. (BYRN) is a leading provider of less-lethal self-defense technology with a diverse product portfolio spanning handheld…
- [BYRN | Byrna Technologies, Inc. Common Institutional ...](https://www.quiverquant.com/stock/BYRN/institutions/)
  - View the latest changes in ownership of Byrna Technologies, Inc. Common Stock (BYRN) by institutional investors. See the top funds and the values of their po…
- [Byrna Technologies Inc. (BYRN) Interactive Stock Chart - Yahoo Finance](https://ca.finance.yahoo.com/quote/BYRN/chart/?p=BYRN)
  - Interactive Chart for Byrna Technologies Inc. (BYRN), analyze all the data with a huge range of indicators.Cryptocurrencies. Rates. Commodities. Currencies. …
- [AstraZeneca plc (AZN) vs Byrna Technologies Inc (BYRN)... | Pluang](https://pluang.com/en/compare/azn-vs-byrn)
  - BYRN trades at $3.26, down 2.4% today, with bearish technical signals from moving averages despite oversold RSI readings. The company reported a Q2 2026 loss…
- [FinancialContent - Why Byrna (BYRN) Shares Are Sliding Today](https://markets.financialcontent.com/stocks/article/stockstory-2026-7-20-why-byrna-byrn-shares-are-sliding-today)
  - Shares of non-lethal weapons company Byrna (NASDAQ: BYRN) fell 4.1% in the afternoon session after the company announced the appointment of James White as Se…
- [BYRN - Stock Quotes for BYRN Ent Holdg, NASDAQ: BYRN... - Webull](https://www.webull.com/quote/nasdaq-byrn)
  - Webull offers BYRN Ent Holdg (BYRN) historical stock prices, in-depth market analysis, NASDAQ: BYRN real-time stock quote data, in-depth charts, free BYRN op…
- [Demand - Wikipedia](https://en.m.wikipedia.org/wiki/Demand)
  - Demand curve is a graphical presentation of the "law of demand". [8] The curve shows how the price of a commodity or service changes as the quantity demanded…
- [3.1 Demand, Supply, and Equilibrium in Markets for Goods and Services ...](https://openstax.org/books/principles-economics-3e/pages/3-1-demand-supply-and-equilibrium-in-markets-for-goods-and-services)
  - First let’s first focus on what economists mean by demand, what they mean by supply, and then how demand and supply interact in a market. Demand for Goods an…
- [Market Demand: Definition, How to Calculate, Determinants](https://penpoin.com/market-demand/)
  - What’s it: Market demand is the sum of individual demand in the market at a given price. Economists define demand as our willingness and ability as consumers…
- [Byrna Technologies Inc Customers by Division and Industry - CSIMarket](https://csimarket.com/stocks/BYRN-Customers)
  - Byrna Technologies Inc customers and markets, results by customer and performance relative to BYRN, by company and industry - CSIMarket

### Search warnings
- news:BYRN Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers: No results found.
- news:BYRN BYRN outlook OR catalyst OR commodity OR uranium OR rare earth OR vanadium: No results found.
- news:BYRN sector drivers OR market demand: No results found.
- news:BYRN BYRN backlog OR contract OR refinancing OR leverage: No results found.

## SEC filing [S27]
- Extraction OK: False
- Item 1 chars: 0
- Item 1A chars: 0
- Item 7 chars: 0
- Meta: {'accession_number': '0001437749-26-010311', 'filing_date': '2026-03-30', 'source': 'edgartools', 'path': 'C:\\DevWork\\equity_research_agent\\data\\filings\\BYRN_10k.txt'}

## Qualitative analysis (local LLM)

_Item 1 Business summary mode: empty (see Company setup & business model)._

### Item 1A — Risk Factors
No text extracted.


### Item 7 — MD&A
No text extracted.


## Run warnings

- fundamentals: Failed to perform, curl: (28) Connection timed out after 30008 milliseconds. See https://curl.se/libcurl/c/libcurl-errors.html first for more details.
- ev_ebitda: Missing shares outstanding
- dcf: Cannot run DCF without positive base revenue.; Cannot run DCF without shares outstanding.
- scenarios: Missing shares outstanding

## Research loop (think → act)

1. _heuristic_ — Coverage looks adequate for this pass; stopping iterative loop.

## Sources

- **[S1]** BYRN fundamentals (yfinance)
  - Error: Failed to perform, curl: (28) Connection timed out after 30008 milliseconds. See https://curl.se/libcurl/c/libcurl-errors.html first for more details.
- **[S2]** BYRN EV/EBITDA valuation (multiples)
  - Base implied price=None, multiple=8.0
- **[S3]** BYRN DCF valuation (dcf)
  - DCF failed: Cannot run DCF without positive base revenue.; Cannot run DCF without shares outstanding.
- **[S4]** BYRN peer comps (peers)
  - Peers: ; rows=0
- **[S5]** BYRN earnings history (earnings)
  - rows=0; next=None
- **[S6]** Byrna Technologies (BYRN) Stock Forecast & Price Target (web) — https://www.marketbeat.com/stocks/NASDAQ/BYRN/forecast/
  - BYRN's current price target is $7.88. Learn why top analysts are making this stock forecast for Byrna Technologies at MarketBeat.
- **[S7]** What is the current Price Target and Forecast for Byrna Technologies (BYRN) (web) — https://www.zacks.com/stock/research/byrn/price-target-stock-forecast
  - Price Target Based on short-term price targets offered by four analysts, the average price target for Byrna Technologies Inc. comes to $7.63. The forecasts range from a low of $…
- **[S8]** Byrna Technologies (BYRN) Stock Forecast & Analyst Price Targets (web) — https://stockanalysis.com/stocks/byrn/forecast/
  - Stock forecasts and analyst price target predictions for Byrna Technologies Inc. (BYRN) stock, with detailed revenue and earnings estimates.
- **[S9]** Byrna Technologies Inc. (BYRN) Analyst Insights, Price Targets ... (web) — https://finance.yahoo.com/quote/BYRN/analyst-insights/
  - Yahoo Finance provides the latest analyst insights, price targets, and recommendations on Byrna Technologies Inc. (BYRN) to help inform your investment strategy.
- **[S10]** Why did STLA, MAT, BYRN stocks tumble to 52-week lows today? (web) — https://www.msn.com/en-in/money/markets/why-did-stla-mat-byrn-stocks-tumble-to-52-week-lows-today/ar-AA27BZfD?ocid=BingNewsVerp
  - Stellantis, Mattel, and Byrna Technologies tumbled to fresh lows on Thursday amid regional weaknesses, poor outlook, and Wall Street caution.
- **[S11]** Needham Reiterates Buy on monday.com (MNDY), Sets $250 Price Targe (web) — https://finance.yahoo.com/news/needham-reiterates-buy-monday-com-225907775.html
  - monday.com Ltd. (NASDAQ:MNDY) is one of the AI Stocks Analysts Are Watching Closely. On August 18,...
- **[S12]** Analysts Have Mixed Views on Glacier Bancorp (GBCI) (web) — https://finance.yahoo.com/markets/stocks/articles/analysts-mixed-views-glacier-bancorp-201806470.html
  - Glacier Bancorp, Inc. (NYSE:GBCI) is one of the 11 Best American Bank Stocks to Buy According to Wall Street Analysts. On February 11, Piper Sandler...
- **[S13]** What To Expect From Byrna Technologies Inc (BYRN) Q2 2026 Earnings (web) — https://finance.yahoo.com/markets/stocks/articles/expect-byrna-technologies-inc-byrn-131713208.html
  - At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage rates that help you mana…
- **[S14]** Byrna Technologies (BYRN) Stock Forecast and Price Target 2026 (web_page) — https://www.marketbeat.com/stocks/NASDAQ/BYRN/forecast/
  - Byrna Technologies (BYRN) Stock Forecast and Price Target 2026 Skip to main content → Trump’s emergency dollar reset (From Porter & Company) (Ad) Free BYRN Stock Alerts Byrna Te…
- **[S15]** What is the current Price Target and Forecast for Byrna Technologies (BYRN) (web_page) — https://www.zacks.com/stock/research/byrn/price-target-stock-forecast
  - Pardon Our Interruption As you were browsing something about your browser made us think you were a bot. There are a few reasons this might happen: You're a power user moving thr…
- **[S16]** Byrna Technologies (BYRN) Stock Forecast & Analyst Price Targets (web_page) — https://stockanalysis.com/stocks/byrn/forecast/
  - Byrna Technologies (BYRN) Stock Forecast & Analyst Price Targets Collapse Byrna Technologies Inc. (BYRN) NASDAQ: BYRN · Real-Time Price · USD Full Chart Watchlist Alerts Compare…
- **[S17]** Investor Relations :: Byrna Technologies Inc. (BYRN) (web) — https://ir.byrna.com/
  - Jul 8, 2026 · Byrna Technologies Inc. (NASDAQ: BYRN) is a technology company specializing in the areas of Personal Security Devices, Military, Law Enforcement, Corrections, and …
- **[S18]** Byrna Technologies (BYRN) Stock Forecast & Price TargetByrna Technologies Inc. (BYRN): A Bullish Thesis for Long ...BYRN | Byrna Technologies, Inc. Common Institutional ...BYRN - Byrna Technologies Inc. Stock - Stock Price ... - FintelByrna Technologies (BYRN) Stock Price, News & AnalysisBYRN Institutional Ownership & Insider Trading - Filings ... (web) — https://www.marketbeat.com/stocks/NASDAQ/BYRN/forecast/
  - BYRN's current price target is $7.88. Learn why top analysts are making this stock forecast for Byrna Technologies at MarketBeat. Oct 22, 2025 · Byrna Technologies Inc. (BYRN) i…
- **[S19]** Byrna Technologies Inc. (BYRN): A Bullish Thesis for Long ... (web) — https://www.ainvest.com/news/byrna-technologies-byrn-bullish-thesis-long-term-growth-2510/
  - Oct 22, 2025 · Byrna Technologies Inc. (BYRN) is a leading provider of less-lethal self-defense technology with a diverse product portfolio spanning handheld devices, launchers,…
- **[S20]** BYRN | Byrna Technologies, Inc. Common Institutional ... (web) — https://www.quiverquant.com/stock/BYRN/institutions/
  - View the latest changes in ownership of Byrna Technologies, Inc. Common Stock (BYRN) by institutional investors. See the top funds and the values of their positions.
- **[S21]** Byrna Technologies Inc. (BYRN) Interactive Stock Chart - Yahoo Finance (web) — https://ca.finance.yahoo.com/quote/BYRN/chart/?p=BYRN
  - Interactive Chart for Byrna Technologies Inc. (BYRN), analyze all the data with a huge range of indicators.Cryptocurrencies. Rates. Commodities. Currencies. Canada markets close…
- **[S22]** AstraZeneca plc (AZN) vs Byrna Technologies Inc (BYRN)... | Pluang (web) — https://pluang.com/en/compare/azn-vs-byrn
  - BYRN trades at $3.26, down 2.4% today, with bearish technical signals from moving averages despite oversold RSI readings. The company reported a Q2 2026 loss of $0.44 per share,…
- **[S23]** FinancialContent - Why Byrna (BYRN) Shares Are Sliding Today (web) — https://markets.financialcontent.com/stocks/article/stockstory-2026-7-20-why-byrna-byrn-shares-are-sliding-today
  - Shares of non-lethal weapons company Byrna (NASDAQ: BYRN) fell 4.1% in the afternoon session after the company announced the appointment of James White as Senior Vice President …
- **[S24]** BYRN - Stock Quotes for BYRN Ent Holdg, NASDAQ: BYRN... - Webull (web) — https://www.webull.com/quote/nasdaq-byrn
  - Webull offers BYRN Ent Holdg (BYRN) historical stock prices, in-depth market analysis, NASDAQ: BYRN real-time stock quote data, in-depth charts, free BYRN options chain data, an…
- **[S25]** Investor Relations :: Byrna Technologies Inc. (BYRN) (web_page) — https://ir.byrna.com/
  - Investor Relations :: Byrna Technologies Inc. (BYRN) Skip to content Shop Less-Lethal                                 Pistols Byrna CL-XL New Byrna CL Byrna SD Best           …
- **[S26]** Byrna Technologies (BYRN) Stock Forecast and Price Target 2026 (web_page) — https://www.marketbeat.com/stocks/NASDAQ/BYRN/forecast/
  - Byrna Technologies (BYRN) Stock Forecast and Price Target 2026 Skip to main content → Trump’s emergency dollar reset (From Porter & Company) (Ad) Free BYRN Stock Alerts Byrna Te…
- **[S27]** BYRN 10-K (sec)
  - Item 1 chars=0, Item 1A chars=0, Item 7 chars=0, ok=False, source=edgartools
- **[S28]** BYRN 8-K 2026-07-09 (sec) — https://www.sec.gov/Archives/edgar/data/1354866/000143774926023101/byrn20260708_8k.htm
  - FORM 8-K
- **[S29]** BYRN 10-Q 2026-07-09 (sec) — https://www.sec.gov/Archives/edgar/data/1354866/000143774926023100/byrn20260531_10q.htm
  - FORM 10-Q
- **[S30]** BYRN 8-K 2026-07-08 (sec) — https://www.sec.gov/Archives/edgar/data/1354866/000143774926023029/byrn20260707_8k.htm
  - FORM 8-K
- **[S31]** BYRN 8-K 2026-06-18 (sec) — https://www.sec.gov/Archives/edgar/data/1354866/000143774926021142/byrn20260618c_8k.htm
  - FORM 8-K
- **[S32]** BYRN 8-K 2026-06-15 (sec) — https://www.sec.gov/Archives/edgar/data/1354866/000143774926020580/byrn20260612_8k.htm
  - FORM 8-K
- **[S33]** BYRN 8-K 2026-04-09 (sec) — https://www.sec.gov/Archives/edgar/data/1354866/000143774926011821/byrn20260408c_8k.htm
  - FORM 8-K
- **[S34]** BYRN 10-Q 2026-04-09 (sec) — https://www.sec.gov/Archives/edgar/data/1354866/000143774926011820/byrn20260228_10q.htm
  - FORM 10-Q
- **[S35]** BYRN 8-K 2026-04-08 (sec) — https://www.sec.gov/Archives/edgar/data/1354866/000143774926011756/byrn20260408_8k.htm
  - FORM 8-K
- **[S36]** Item 1 Business summary (nlp)
  - ### Item 1 — Business No Item 1 Business text extracted. 
- **[S37]** Item 1A summary (nlp)
  - ### Item 1A — Risk Factors No text extracted. 
- **[S38]** Item 7 summary (nlp)
  - ### Item 7 — MD&A No text extracted. 
- **[S39]** BYRN scenario price ranges (scenarios)
  - ok=False; base mid=None; headwinds=3; tailwinds=4
- **[S40]** BYRN driver analysis (drivers)
  - ok=False; drivers=7
- **[S41]** BYRN memo sections (memo)
  - mode=rules; proxies=3

## Self-critique

_Automated review (heuristic)._

### Strengths
- Combines local fundamentals, optional DCF scenarios, and cited sources where available.
- Keeps a non-advisory framing for local research drafts.

### Issues & gaps
- DCF section was planned but valuation did not complete successfully.
- EV/EBITDA section was planned but multiples valuation did not complete.
- Run recorded 4 tool warning(s); see Run warnings before relying on the draft.

### Caution for readers
- Treat scenario prices as sensitivity output, not a forecast.
- Re-check primary filings and fresh market data before any decision.



---

# Template: Valuation (DCF + Street + drivers) (`valuation`)

# BYRN — Planned Research Report

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

**Fundamentals error:** Failed to perform, curl: (6) Could not resolve host: query2.finance.yahoo.com. See https://curl.se/libcurl/c/libcurl-errors.html first for more details.

## DCF valuation (base / bull / bear) [S2]

> Simplified revenue->FCF DCF. Not investment advice; assumptions are editable heuristics.

- **Error:** Cannot run DCF without positive base revenue.
- **Error:** Cannot run DCF without shares outstanding.

## Valuation — EV/EBITDA scenarios [S3]

> Priced-in model: implied price = (EBITDA × EV/EBITDA − net debt) ÷ shares. Not a forecast.

- Net debt used: $0

| Scenario | EBITDA | EV/EBITDA | Implied EV | Equity value | Implied price |
|---|---:|---:|---:|---:|---:|
| bear | $700.00M | 6.0x | $4.20B | $4.20B | — |
| base | $1.00B | 8.0x | $8.00B | $8.00B | — |
| bull | $1.20B | 10.0x | $12.00B | $12.00B | — |

- EBITDA missing or non-positive; scenarios use placeholder $1B EBITDA — edit before relying on prices.
- No current EV/EBITDA; defaulted base multiple to 8.0x.
- **Error:** Missing shares outstanding

## Scenario price ranges (headwinds & tailwinds) [S29]

> Medium-term (18–36 months (medium / medium-long term)) driver → EV/EBITDA bridge. Distinct from the FCF DCF path. Not investment advice.

- Anchor multiple: 8.0x (driver_ev_ebitda_bridge)
- Anchor EBITDA: $1.00B
- Driver extraction: `rules`

### Headwinds (bear-case fuel)

- **Balance-sheet / refinancing pressure** — sector=None industry=None revenue=None ebitda=None fcf=None net_debt=None nd_ebitda=None target=None rec=None _(source: fundamentals)_
- **Competitive / pricing pressure** — Commodity Prices | Commodity Market | Markets Insider Get all information on the commodity market. Find the latest commodity prices including News, Charts, Realtime Quotes and even _(source: web)_

### Tailwinds (bull-case fuel)

- **Growth / execution upside** — Byrna Technologies (BYRN) Stock Forecast and Price Target 2026 MarketBeat calculates consensus analyst ratings for stocks using the most recent rating from each Wall Street analyst _(source: web)_
- **Product / pricing power** — Stocks See Support from Airline Stocks but Trade Uncertainty Persists The S&P 500 Index ($SPX ) (SPY ) today is up +0.10%, the Dow Jones Industrials Index ($DOWI ) (DIA )... _(source: web)_
- **Capital returns / FCF inflection** — BYRN Intrinsic Valuation and Fundamental Analysis - Byrna Technologies Inc - Alpha Spread BYRN Intrinsic Valuation and Fundamental Analysis - Byrna Technologies Inc - Alpha Spread  _(source: web_page)_

### Price ranges by case

| Case | Prob. | Metric vs TTM | Multiple | Price low | Mid | High | Upside vs spot |
|---|---:|---:|---:|---:|---:|---:|---:|
| bear | 0.24 | — | — | — | — | — | Missing shares outstanding |
| base | 0.46 | — | — | — | — | — | Missing shares outstanding |
| bull | 0.3 | — | — | — | — | — | Missing shares outstanding |

#### Bear — headwinds dominate

Headwinds bite: weaker operating trajectory and multiple compression. Equity duration shrinks if cash generation fails to offset leverage / competitive pressure.

- Driver: **Balance-sheet / refinancing pressure** — sector=None industry=None revenue=None ebitda=None fcf=None net_debt=None nd_ebitda=None target=None rec=None
- Driver: **Competitive / pricing pressure** — Commodity Prices | Commodity Market | Markets Insider Get all information on the commodity market. Find the latest commodity prices including News, Charts, Real

#### Base — mixed execution

Balanced path: some tailwinds offset headwinds. Operating scale roughly holds with modest repair/normalization; valuation stays near the current EV/EBITDA anchor.

- Driver: **Growth / execution upside** — Byrna Technologies (BYRN) Stock Forecast and Price Target 2026 MarketBeat calculates consensus analyst ratings for stocks using the most recent rating from each
- Driver: **Product / pricing power** — Stocks See Support from Airline Stocks but Trade Uncertainty Persists The S&P 500 Index ($SPX ) (SPY ) today is up +0.10%, the Dow Jones Industrials Index ($DOW
- Driver: **Balance-sheet / refinancing pressure** — sector=None industry=None revenue=None ebitda=None fcf=None net_debt=None nd_ebitda=None target=None rec=None
- Driver: **Competitive / pricing pressure** — Commodity Prices | Commodity Market | Markets Insider Get all information on the commodity market. Find the latest commodity prices including News, Charts, Real

#### Bull — tailwinds dominate

Tailwinds compound: operating improvement plus a re-rating toward peer or recovery multiples as balance-sheet and growth narratives improve.

- Driver: **Growth / execution upside** — Byrna Technologies (BYRN) Stock Forecast and Price Target 2026 MarketBeat calculates consensus analyst ratings for stocks using the most recent rating from each
- Driver: **Product / pricing power** — Stocks See Support from Airline Stocks but Trade Uncertainty Persists The S&P 500 Index ($SPX ) (SPY ) today is up +0.10%, the Dow Jones Industrials Index ($DOW
- Driver: **Capital returns / FCF inflection** — BYRN Intrinsic Valuation and Fundamental Analysis - Byrna Technologies Inc - Alpha Spread BYRN Intrinsic Valuation and Fundamental Analysis - Byrna Technologies

### Method notes

- Item 1A risks weighted toward headwinds.
- Current ev_ebitda multiple missing; anchored at 8.0x.
- Mapping follows Gemini/Perplexity-style scenario memos: qualitative drivers → operating metric & multiple paths → share-price ranges over a medium-term horizon.

### Errors

- Missing shares outstanding

## Web research — web_analysts

- Queries: BYRN analyst price target, BYRN stock rating OR consensus OR upgrade OR downgrade, BYRN Estimate intrinsic value under base / bull / bear scenarios analyst
- Unique hits: 12
- Pages fetched: 2/3

### Web synthesis — web_analysts (rule-based fallback — Ollama unavailable)
**Keyword hits:** uncertainty, customer, product, service, market, network

- [HIT] Byrna Technologies (BYRN) Stock Forecast and Price Target 2026 | www.marketbeat.com | https://www.marketbeat.com/stocks/NASDAQ/BYRN/forecast/ MarketBeat calculates consensus analyst ratings for stocks using the most recent rating from each Wall Street analyst that has rated a stock within the last twelve months.
- [HIT] Stocks Under Some Pressure as Optimism Fades Over US-Iran Ceasefire | Barchart · via Yahoo Finance | https://finance.yahoo.com/markets/stocks/articles/stocks-under-pressure-optimism-fades-140947179.html The S&P 500 Index ($SPX ) (SPY ) today is down -0.04%, the Dow Jones Industrial Average ($DOWI )...
- [HIT] Stocks See Support from Airline Stocks but Trade Uncertainty Persists | Barchart · via Yahoo Finance | https://finance.yahoo.com/news/stocks-see-support-airline-stocks-151824703.html The S&P 500 Index ($SPX ) (SPY ) today is up +0.10%, the Dow Jones Industrials Index ($DOWI ) (DIA )...
- [PAGE] Byrna Technologies (BYRN) Stock Forecast and Price Target 2026 | https://www.marketbeat.com/stocks/NASDAQ/BYRN/forecast/ Byrna Technologies (BYRN) Stock Forecast and Price Target 2026 Skip to main content → Universal basic income is not impossible.
- It exist (kind of) (From Freedom Financial) (Ad) Free BYRN Stock Alerts Byrna Technologies (BYRN)  Stock Forecast & Price Target $3.72 +0.35 (+10.39%) As of 12:50 PM Eastern This is a fair market value price provided by Massive.
- Add Compare Share Share Analyst Forecasts Stock Analysis Analyst Forecasts Chart Competitors Earnings Financials Headlines Insider Trades Options Chain Ownership SEC Filings Trends Buy This Stock Byrna Technologies - Analysts' Recommendations and Stock Price Forecast (2026) How MarketBeat Calculates Price Target and Consensus Rating Consensus Rating Moderate Buy Based on 6 Analyst Ratings Sell 1 Hold 2 Buy 3 Based on 6 Wall Street analysts who have issued ratings for Byrna Technologies in the last 12 months ,  the stock has a consensus rating of "Moderate Buy." Out of the 6 analysts, 1 has given a sell rating, 2 have given a hold rating, 1 has given a buy rating, and 2 have given a strong buy rating for  BYRN.
- MarketBeat calculates consensus analyst ratings for stocks using the most recent rating from each Wall Street analyst that has rated a stock within the last twelve months.
- MarketBeat's consensus price targets are a mean average of the most recent available price targets set by each analyst that has set a price target for the stock in the last twelve months.

### Sources found
- [Byrna Technologies (BYRN) Stock Forecast and Price Target 2026](https://www.marketbeat.com/stocks/NASDAQ/BYRN/forecast/)
  - MarketBeat calculates consensus analyst ratings for stocks using the most recent rating from each Wall Street analyst that has rated a stock within the last …
- [Byrna Technologies Inc. (BYRN) Stock Price, News... - Yahoo Finance](https://finance.yahoo.com/quote/BYRN/)
  - Find the latest Byrna Technologies Inc. (BYRN) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [BYRNA TECHNOLOGIES INC(NASDAQ:BYRN) stock Analyst Ratings](https://www.chartmill.com/stock/quote/BYRN/analyst-ratings)
  - The Buy consensus is the weighted average rating of the current analysts ratings. Analysts have set a mean price target forecast of 39.27. This target is 92.…
- [Byrna Technologies (BYRN) Stock Price & Overview](https://stockanalysis.com/stocks/byrn/)
  - According to 3 analysts, the average rating for BYRN stock is "Buy." The 12-month stock price target is $13.67, which is an increase of 216.44% from the late…
- [Stocks Under Some Pressure as Optimism Fades Over US-Iran Ceasefire](https://finance.yahoo.com/markets/stocks/articles/stocks-under-pressure-optimism-fades-140947179.html)
  - The S&P 500 Index ($SPX ) (SPY ) today is down -0.04%, the Dow Jones Industrial Average ($DOWI )...
- [Stocks See Support from Airline Stocks but Trade Uncertainty Persists](https://finance.yahoo.com/news/stocks-see-support-airline-stocks-151824703.html)
  - The S&P 500 Index ($SPX ) (SPY ) today is up +0.10%, the Dow Jones Industrials Index ($DOWI ) (DIA )...
- [Stocks Power Higher on AI Optimism](https://finance.yahoo.com/news/stocks-power-higher-ai-optimism-205037354.html)
  - The S&P 500 Index ($SPX ) (SPY ) on Wednesday closed up +0.58%, the Dow Jones Industrials Index ($DOWI ) (DIA ) closed unchanged, and the Nasdaq 100...
- [Stocks Settle Higher on Tech Stock Strength and Lower Bond Yields](https://finance.yahoo.com/news/stocks-settle-higher-tech-stock-204327941.html)
  - The S&P 500 Index ($SPX ) (SPY ) Wednesday closed up +0.61%, the Dow Jones Industrials Index ($DOWI...
- [BYRN Intrinsic Valuation and Fundamental Analysis - Byrna Technologies Inc - Alpha Spread](https://www.alphaspread.com/security/nasdaq/byrn/summary)
  - ... Income Statement, Balance Sheet, Cash Flow Statement. ... BYRN stock discount rate: cost of equity and WACC. ... The intrinsic value of one BYRN stock un…
- [3 Ways of Calculating a Stock's Intrinsic Value - HubPages](https://discover.hubpages.com/money/Stock-Valuation-Using-Bear-Bull-and-Base-Case-Scenarios)
  - September 12, 2024 - When calculating intrinsic value, it can be helpful to have 3 probability-weighted, projected scenarios mapped out in order to dial in a…
- [3 Ways of Calculating a Stock's Intrinsic Value - ToughNickel](https://toughnickel.com/personal-finance/Stock-Valuation-Using-Bear-Bull-and-Base-Case-Scenarios)
  - March 22, 2023 - When calculating intrinsic value, it can be helpful to have 3 probability-weighted, projected scenarios mapped out in order to dial in a spe…
- [Bull Base Bear Valuation for One Stock | Model Reef](https://modelreef.io/resources/articles/stock-valuation/how-to-create-a-bull-base-bear-valuation-for-one-stock-scenario-driven-intrinsic-value)
  - April 15, 2026 - The point of bull/base/bear is to show what must be true-not to pretend the world can be summarised in one number. If you want a quick quali…

### Search warnings
- text:BYRN analyst price target: ConnectError: ConnectError('error sending request for url (https://www.mojeek.com/search?q=BYRN+analyst+price+target) > client error (Connect) > dns error > no connections available')
- news:BYRN analyst price target: No results found.
- news:BYRN Estimate intrinsic value under base / bull / bear scenarios analyst: No results found.

## Web research — web_drivers

- Queries: BYRN Estimate intrinsic value under base / bull / bear scenarios, BYRN BYRN outlook OR catalyst OR commodity OR uranium OR rare earth OR vanadium, BYRN sector drivers OR market demand
- Unique hits: 13
- Pages fetched: 3/3

### Web synthesis — web_drivers (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, revenue, margin, customer, service, market

- Compared to the current market price of 24.17 USD, Byrna Technologies Inc is Overvalued by 69%.
- [HIT] Byrna Technologies (BYRN) Earnings Date and Reports 2026 | www.marketbeat.com | https://www.marketbeat.com/stocks/NASDAQ/BYRN/earnings/ BYRN Upcoming Earnings.
- [HIT] Commodity Prices | Commodity Market | Markets Insider | markets.businessinsider.com | https://markets.businessinsider.com/commodities?op=1 Get all information on the commodity market.
- | finance.yahoo.com | https://finance.yahoo.com/markets/stocks/articles/byrna-nasdaq-byrn-misses-q2-125638829.html Jul 9, 2026 ...
- Byrna's annualized revenue growth of 35.1% over the last two years is above its five-year trend ...
- stock analysis: Q2 revenue -42.5%, margin hit from write-downs and weak demand.
- | www.marketbeat.com | https://www.marketbeat.com/instant-alerts/byrna-technologies-nasdaqbyrn-downgraded-to-strong-sell-rating-by-wall-street-zen-2026-07-12/ Jul 12, 2026 ...
- Essential Insights: Almost Everything You Need to Know About the EV Market ...

### Sources found
- [BYRN Intrinsic Valuation and Fundamental Analysis... - Alpha Spread](https://www.alphaspread.com/security/nasdaq/byrn/summary)
  - The intrinsic value of one BYRN stock under the Base Case scenario is 7.5 USD. Compared to the current market price of 24.17 USD, Byrna Technologies Inc is O…
- [Byrna Technologies (BYRN) Earnings Date and Reports 2026](https://www.marketbeat.com/stocks/NASDAQ/BYRN/earnings/)
  - BYRN Upcoming Earnings. Byrna Technologies' Q2 2026 earnings is estimated for Thursday, July 9, 2026, based on past reporting schedules, with a conference ca…
- [BYRN | Byrna Technologies, Inc. Common Stock Data, Price & News](https://www.quiverquant.com/stock/BYRN/)
  - BYRN stock data, price, and news. View BYRN insider trading, corporate lobbying, Congressional trading, social media sentiment, and more.
- [Byrna Technologies Inc. (BYRN) Earnings Estimates... | Seeking Alpha](https://seekingalpha.com/symbol/BYRN/earnings/estimates)
  - Top Value Stocks.byrn Summary. Follow. 4.29K followers.
- [Rare earth elements 2025 - Analysis - IEA](https://www.iea.org/reports/rare-earth-elements-2025)
  - Rare earth elements 2025 - Analysis and key findings. A report by the International Energy Agency.
- [Commodity Prices | Commodity Market | Markets Insider](https://markets.businessinsider.com/commodities?op=1)
  - Get all information on the commodity market. Find the latest commodity prices including News, Charts, Realtime Quotes and even more about commodities.
- [Rare Earth Archives - MINING.COM](https://www.mining.com/commodity/rare-earth/)
  - Rare Earth July 24, 2026 Japan finds heavy rare earths dominate seabed deposit Deep-sea rare earth discovery could boost Japan's critical mineral supply and …
- [Top 5 Uranium News Stories of 2025 | INN](https://investingnews.com/top-uranium-news-stories-2025/)
  - Uranium was once again in the spotlight this year. Take a look back at 2025 with our top uranium news stories over the last 12 months.
- [Byrna (NASDAQ:BYRN) Misses Q2 CY2026 Sales Expectations ...](https://finance.yahoo.com/markets/stocks/articles/byrna-nasdaq-byrn-misses-q2-125638829.html)
  - Jul 9, 2026 ... ... industry trends or demand cycles. Byrna's annualized revenue growth of 35.1% over the last two years is above its five-year trend ...
- [Byrna Technologies: Selling The Solution Is The Real Challenge](https://seekingalpha.com/article/4921219-byrna-technologies-selling-the-solution-is-the-real-challenge)
  - Jul 10, 2026 ... Byrna Technologies Inc. stock analysis: Q2 revenue -42.5%, margin hit from write-downs and weak demand. Click for this BYRN update and see ...
- [Byrna Technologies (NASDAQ:BYRN) Downgraded to Strong Sell ...](https://www.marketbeat.com/instant-alerts/byrna-technologies-nasdaqbyrn-downgraded-to-strong-sell-rating-by-wall-street-zen-2026-07-12/)
  - Jul 12, 2026 ... Essential Insights: Almost Everything You Need to Know About the EV Market ... AST SpaceMobile Stock Sinks as SpaceX Fallout Rattles Space S…
- [Byrna Technologies Future Growth - Simply Wall St](https://simplywall.st/stocks/us/capital-goods/nasdaq-byrn/byrna-technologies/future)
  - Jul 10, 2026 ... Company -7.9% Industry 8.9% Market 12.8%. Forecast ... Earnings vs Market: BYRN is forecast to remain unprofitable over the next 3 years.

### Search warnings
- news:BYRN Estimate intrinsic value under base / bull / bear scenarios: No results found.
- news:BYRN BYRN outlook OR catalyst OR commodity OR uranium OR rare earth OR vanadium: No results found.

## SEC filing [S25]
- Extraction OK: False
- Item 1 chars: 0
- Item 1A chars: 0
- Item 7 chars: 0
- Meta: {'source': 'cache', 'path': 'C:\\DevWork\\equity_research_agent\\data\\filings\\BYRN_10k.txt'}

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


## Run warnings

- fundamentals: Failed to perform, curl: (6) Could not resolve host: query2.finance.yahoo.com. See https://curl.se/libcurl/c/libcurl-errors.html first for more details.
- dcf: Cannot run DCF without positive base revenue.; Cannot run DCF without shares outstanding.
- ev_ebitda: Missing shares outstanding
- scenarios: Missing shares outstanding

## Research loop (think → act)

1. _heuristic_ — Coverage looks adequate for this pass; stopping iterative loop.

## Sources

- **[S1]** BYRN fundamentals (yfinance)
  - Error: Failed to perform, curl: (6) Could not resolve host: query2.finance.yahoo.com. See https://curl.se/libcurl/c/libcurl-errors.html first for more details.
- **[S2]** BYRN DCF valuation (dcf)
  - DCF failed: Cannot run DCF without positive base revenue.; Cannot run DCF without shares outstanding.
- **[S3]** BYRN EV/EBITDA valuation (multiples)
  - Base implied price=None, multiple=8.0
- **[S4]** Byrna Technologies (BYRN) Stock Forecast and Price Target 2026 (web) — https://www.marketbeat.com/stocks/NASDAQ/BYRN/forecast/
  - MarketBeat calculates consensus analyst ratings for stocks using the most recent rating from each Wall Street analyst that has rated a stock within the last twelve months. Each …
- **[S5]** Byrna Technologies Inc. (BYRN) Stock Price, News... - Yahoo Finance (web) — https://finance.yahoo.com/quote/BYRN/
  - Find the latest Byrna Technologies Inc. (BYRN) stock quote, history, news and other vital information to help you with your stock trading and investing.
- **[S6]** BYRNA TECHNOLOGIES INC(NASDAQ:BYRN) stock Analyst Ratings (web) — https://www.chartmill.com/stock/quote/BYRN/analyst-ratings
  - The Buy consensus is the weighted average rating of the current analysts ratings. Analysts have set a mean price target forecast of 39.27. This target is 92.12% above the curren…
- **[S7]** Byrna Technologies (BYRN) Stock Price & Overview (web) — https://stockanalysis.com/stocks/byrn/
  - According to 3 analysts, the average rating for BYRN stock is "Buy." The 12-month stock price target is $13.67, which is an increase of 216.44% from the latest price.
- **[S8]** Stocks Under Some Pressure as Optimism Fades Over US-Iran Ceasefire (web) — https://finance.yahoo.com/markets/stocks/articles/stocks-under-pressure-optimism-fades-140947179.html
  - The S&P 500 Index ($SPX ) (SPY ) today is down -0.04%, the Dow Jones Industrial Average ($DOWI )...
- **[S9]** Stocks See Support from Airline Stocks but Trade Uncertainty Persists (web) — https://finance.yahoo.com/news/stocks-see-support-airline-stocks-151824703.html
  - The S&P 500 Index ($SPX ) (SPY ) today is up +0.10%, the Dow Jones Industrials Index ($DOWI ) (DIA )...
- **[S10]** Stocks Power Higher on AI Optimism (web) — https://finance.yahoo.com/news/stocks-power-higher-ai-optimism-205037354.html
  - The S&P 500 Index ($SPX ) (SPY ) on Wednesday closed up +0.58%, the Dow Jones Industrials Index ($DOWI ) (DIA ) closed unchanged, and the Nasdaq 100...
- **[S11]** Stocks Settle Higher on Tech Stock Strength and Lower Bond Yields (web) — https://finance.yahoo.com/news/stocks-settle-higher-tech-stock-204327941.html
  - The S&P 500 Index ($SPX ) (SPY ) Wednesday closed up +0.61%, the Dow Jones Industrials Index ($DOWI...
- **[S12]** Byrna Technologies (BYRN) Stock Forecast and Price Target 2026 (web_page) — https://www.marketbeat.com/stocks/NASDAQ/BYRN/forecast/
  - Byrna Technologies (BYRN) Stock Forecast and Price Target 2026 Skip to main content → Universal basic income is not impossible. It exist (kind of) (From Freedom Financial) (Ad) …
- **[S13]** Byrna Technologies Inc. (BYRN) Stock Price, News, Quote & History - Yahoo Finance (web_page) — https://finance.yahoo.com/quote/BYRN/
  - Byrna Technologies Inc. (BYRN) Stock Price, News, Quote & History - Yahoo Finance Oops, something went wrong Skip to navigation Skip to main content Skip to right column We are …
- **[S14]** BYRN Intrinsic Valuation and Fundamental Analysis... - Alpha Spread (web) — https://www.alphaspread.com/security/nasdaq/byrn/summary
  - The intrinsic value of one BYRN stock under the Base Case scenario is 7.5 USD. Compared to the current market price of 24.17 USD, Byrna Technologies Inc is Overvalued by 69%.
- **[S15]** Byrna Technologies (BYRN) Earnings Date and Reports 2026 (web) — https://www.marketbeat.com/stocks/NASDAQ/BYRN/earnings/
  - BYRN Upcoming Earnings. Byrna Technologies' Q2 2026 earnings is estimated for Thursday, July 9, 2026, based on past reporting schedules, with a conference call scheduled on Tues…
- **[S16]** BYRN | Byrna Technologies, Inc. Common Stock Data, Price & News (web) — https://www.quiverquant.com/stock/BYRN/
  - BYRN stock data, price, and news. View BYRN insider trading, corporate lobbying, Congressional trading, social media sentiment, and more.
- **[S17]** Byrna Technologies Inc. (BYRN) Earnings Estimates... | Seeking Alpha (web) — https://seekingalpha.com/symbol/BYRN/earnings/estimates
  - Top Value Stocks.byrn Summary. Follow. 4.29K followers.
- **[S18]** Rare earth elements 2025 - Analysis - IEA (web) — https://www.iea.org/reports/rare-earth-elements-2025
  - Rare earth elements 2025 - Analysis and key findings. A report by the International Energy Agency.
- **[S19]** Commodity Prices | Commodity Market | Markets Insider (web) — https://markets.businessinsider.com/commodities?op=1
  - Get all information on the commodity market. Find the latest commodity prices including News, Charts, Realtime Quotes and even more about commodities.
- **[S20]** Rare Earth Archives - MINING.COM (web) — https://www.mining.com/commodity/rare-earth/
  - Rare Earth July 24, 2026 Japan finds heavy rare earths dominate seabed deposit Deep-sea rare earth discovery could boost Japan's critical mineral supply and reduce reliance on C…
- **[S21]** Top 5 Uranium News Stories of 2025 | INN (web) — https://investingnews.com/top-uranium-news-stories-2025/
  - Uranium was once again in the spotlight this year. Take a look back at 2025 with our top uranium news stories over the last 12 months.
- **[S22]** BYRN Intrinsic Valuation and Fundamental Analysis - Byrna Technologies Inc - Alpha Spread (web_page) — https://www.alphaspread.com/security/nasdaq/byrn/summary
  - BYRN Intrinsic Valuation and Fundamental Analysis - Byrna Technologies Inc - Alpha Spread Alpha Spread Dashboard Tools Market News Investing Ideas Pricing Search 100,000+ stocks…
- **[S23]** Byrna Technologies (BYRN) Earnings Date and Reports 2026 (web_page) — https://www.marketbeat.com/stocks/NASDAQ/BYRN/earnings/
  - Byrna Technologies (BYRN) Earnings Date and Reports 2026 Skip to main content → Trump’s emergency dollar reset (From Porter & Company) (Ad) Free BYRN Stock Alerts Byrna Technolo…
- **[S24]** BYRN | Byrna Technologies, Inc. Common Stock Data, Price & News (web_page) — https://www.quiverquant.com/stock/BYRN/
  - BYRN | Byrna Technologies, Inc. Common Stock Data, Price & News Skip to Main Content Byrna Technologies, Inc. Common Stock BYRN Real Time Price USD N/A N/A N/A ... Trade BYRN ..…
- **[S25]** BYRN 10-K (sec)
  - Item 1 chars=0, Item 1A chars=0, Item 7 chars=0, ok=False, source=cache
- **[S26]** Item 1 Business summary (nlp)
  - ### Item 1 — Business No Item 1 Business text extracted. 
- **[S27]** Item 1A summary (nlp)
  - ### Item 1A — Risk Factors No text extracted. 
- **[S28]** Item 7 summary (nlp)
  - ### Item 7 — MD&A No text extracted. 
- **[S29]** BYRN scenario price ranges (scenarios)
  - ok=False; base mid=None; headwinds=2; tailwinds=3

## Self-critique

_Automated review (heuristic)._

### Strengths
- Combines local fundamentals, optional DCF scenarios, and cited sources where available.
- Keeps a non-advisory framing for local research drafts.

### Issues & gaps
- DCF section was planned but valuation did not complete successfully.
- EV/EBITDA section was planned but multiples valuation did not complete.
- Draft uses strong recommendation language; this local agent should stay descriptive, not advisory.
- Run recorded 4 tool warning(s); see Run warnings before relying on the draft.

### Caution for readers
- Treat scenario prices as sensitivity output, not a forecast.
- Re-check primary filings and fresh market data before any decision.



---

# Template: Full diligence (`deep`)

# BYRN — Planned Research Report

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
- Company: Byrna Technologies, Inc.
- Sector / industry: Industrials / Aerospace & Defense
- Price: 3.69
- 52-week range: $3.17 – $30.62
- Market cap: $83.74M
- Enterprise value: $68.09M
- Shares outstanding: 22.69M
- Beta: 1.786
- Book equity: $65.76M
- Revenue (latest): $118.12M
- EBITDA (latest): $13.95M
- Free cash flow (latest): -$9.20M
- Operating income: $11.84M
- Operating margin: 10.0%
- EV / EBITDA: 4.9x
- ROIC: 21.8%
- FCF yield: -11.0%
- Debt / Equity: 0.035676810073452254
- FCF / share: -$0.41
- Revenue / share: $5.21

### Capital structure
- Cash: $13.73M
- Short-term debt: $734.00K
- Long-term debt: $1.61M
- Total debt: $2.35M
- Net debt: -$11.38M
- Net debt / EBITDA: -0.8x

### Growth
- Revenue CAGR: 35.0%
- FCF CAGR: —
- Latest revenue YoY: 37.7%
- Latest FCF YoY: -198.2%

### Market expectations (yfinance, sparse)
- Mean target: $6.83
- Target range: $4.00 – $12.00
- Recommendation: buy

_Consensus revenue/EBITDA forecasts are often unavailable via free feeds; treat targets as point-in-time only._

### Historical KPIs (multi-year)

| Year | Revenue | OCF | Capex | FCF | EBITDA | LT debt | Cash | Net debt | Net income |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2025 | $118.12M | -$1.57M | $7.63M | -$9.20M | $13.95M | $2.35M | $13.73M | -$11.38M | $9.69M |
| 2024 | $85.76M | $11.74M | $2.37M | $9.37M | $8.16M | $2.64M | $16.83M | -$14.19M | $12.79M |
| 2023 | $42.64M | $3.89M | $903.00K | $2.99M | -$6.53M | $1.90M | $20.50M | -$18.60M | -$8.19M |
| 2022 | $48.04M | -$13.83M | $3.25M | -$17.08M | -$6.88M | $2.55M | $20.07M | -$17.52M | -$7.88M |

## Charts

### Revenue & FCF history
![Revenue & FCF history](/charts/BYRN_deep_revenue_fcf.png)

### DCF scenario prices
![DCF scenario prices](/charts/BYRN_deep_dcf_scenarios.png)

### Base-case FCF path
![Base-case FCF path](/charts/BYRN_deep_base_fcf_path.png)

## DCF valuation (base / bull / bear) [S2]

> Simplified revenue->FCF DCF. Not investment advice; assumptions are editable heuristics.

- Spot price: $3.69
- Base revenue: $118.12M
- Shares: 22,693,356
- Net debt (Debt−Cash): -$11.38M

| Scenario | Growth | FCF margin | WACC | Term. g | Equity value | Share price | Upside |
|----------|--------|------------|------|---------|--------------|-------------|--------|
| bear | 25.0% | 1.0% | 12.0% | 1.5% | $39.46M | $1.74 | -52.9% |
| base | 35.0% | 3.0% | 10.0% | 2.5% | $180.36M | $7.95 | 115.4% |
| bull | 42.0% | 8.0% | 9.0% | 3.0% | $732.01M | $32.26 | 774.2% |

### Assumption notes
- Base revenue growth seeded from historical rate (37.7%).
- Latest FCF margin was -7.8%; scenarios use normalized positive margins for a going-concern DCF.


### Base-case projected FCF

- Year 1: revenue $159.46M, FCF $4.78M (PV $4.35M)
- Year 2: revenue $215.27M, FCF $6.46M (PV $5.34M)
- Year 3: revenue $290.62M, FCF $8.72M (PV $6.55M)
- Year 4: revenue $392.34M, FCF $11.77M (PV $8.04M)
- Year 5: revenue $529.65M, FCF $15.89M (PV $9.87M)
- Terminal value $217.16M (PV $134.84M)

## Web research — web_research

- Queries: Deep diligence: fundamentals, DCF, web, 10-K risks & MD&A
- Unique hits: 3
- Pages fetched: 3/3

### Web synthesis — web_research (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, interest rate, service, market

- [PAGE] SAFER Web - Company Snapshot | https://safer.fmcsa.dot.gov/CompanySnapshot.aspx SAFER Web - Company Snapshot SAFER Table Layout SAFER Table Layout Company Snapshot The Company Snapshot is a concise electronic record of a companyï¿½s  	identification, size, commodity information, and safety record, including the safety  	rating (if any), a roadside out-of-service inspection summary, and crash information.
- For example, assuming a 5% annual interest rate, $1 in a savings account will be worth $1.05 in a year.
- Factors such as the company or investor's risk profile and the conditions of the capital markets can affect the discount rate chosen.

### Sources found
- [SAFER Web - Company Snapshot](https://safer.fmcsa.dot.gov/CompanySnapshot.aspx)
  - SAFER Home | Feedback | Privacy Policy | USA.gov | Freedom of Information Act (FOIA) | Accessibility | OIG Hotline | Web Policies and Important Links | Plug-…
- [investopedia.com/terms/d/dcf.asp](https://www.investopedia.com/terms/d/dcf.asp)
  - Referensi DCF dapat dilihat pada web investopedia.
- [Login - Webflow](https://webflow.com/login?r=https://webflow.com/dashboard&m=WW91IGhhdmUgYmVlbiBsb2dnZWQgb3V0LiBQbGVhc2Ugc2lnbiBiYWNrIGluIHRvIGNvbnRpbnVlLg==)
  - You have been logged out. Please sign back in to continue.

### Search warnings
- news:Deep diligence: fundamentals, DCF, web, 10-K risks & MD&A: No results found.

## Put opportunities (heuristic) [S3]
- Expiration: 2026-09-18 (DTE 56)
- Candidates: 0
- ATM IV (est.): 135.9%
- IV rank: — (1 local samples)
- HV rank (20d realized): 100.0%


_Note: Delta band approximated via % OTM when greeks are unavailable; IV rank needs ~20+ local daily IV samples (have 1); run the options screen over time to build history.; HV rank is realized-vol rank (20d HV vs ~1y); useful when IV history is thin._

## SEC filing [S10]
- Extraction OK: False
- Item 1 chars: 0
- Item 1A chars: 0
- Item 7 chars: 0
- Meta: {'source': 'cache', 'path': 'C:\\DevWork\\equity_research_agent\\data\\filings\\BYRN_10k.txt'}

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

- **[S1]** BYRN fundamentals (yfinance)
  - Byrna Technologies, Inc.: price=3.69, rev=118120000.0, fcf=-9201000.0, shares=22693356.0, rev_cagr=0.3497464711860472, ROIC=0.2177063410328086, FCF yield=-0.10987779000738584
- **[S2]** BYRN DCF valuation (dcf)
  - Base share price=7.947753124041503, bull=32.256417371811665, bear=1.7389795505454393
- **[S3]** BYRN put screen (yfinance_options)
  - Expiration 2026-09-18 (DTE 56): 0 candidates; IV=1.359378203125, IV rank=None, HV rank=1.0. Delta band approximated via % OTM when greeks are unavailable; IV rank needs ~20+ loc…
- **[S4]** SAFER Web - Company Snapshot (web) — https://safer.fmcsa.dot.gov/CompanySnapshot.aspx
  - SAFER Home | Feedback | Privacy Policy | USA.gov | Freedom of Information Act (FOIA) | Accessibility | OIG Hotline | Web Policies and Important Links | Plug-ins.
- **[S5]** investopedia.com/terms/d/dcf.asp (web) — https://www.investopedia.com/terms/d/dcf.asp
  - Referensi DCF dapat dilihat pada web investopedia.
- **[S6]** Login - Webflow (web) — https://webflow.com/login?r=https://webflow.com/dashboard&m=WW91IGhhdmUgYmVlbiBsb2dnZWQgb3V0LiBQbGVhc2Ugc2lnbiBiYWNrIGluIHRvIGNvbnRpbnVlLg==
  - You have been logged out. Please sign back in to continue.
- **[S7]** SAFER Web - Company Snapshot (web_page) — https://safer.fmcsa.dot.gov/CompanySnapshot.aspx
  - SAFER Web - Company Snapshot SAFER Table Layout SAFER Table Layout Company Snapshot The Company Snapshot is a concise electronic record of a companyï¿½s  	identification, size,…
- **[S8]** Discounted Cash Flow (DCF) Explained With Formula and Examples (web_page) — https://www.investopedia.com/terms/d/dcf.asp
  - Discounted Cash Flow (DCF) Explained With Formula and Examples ​ Top Stories Making Sense of Modern Crypto How Much Couples With Annuity Income Need to Retire More Americans Bec…
- **[S9]** Login - Webflow (web_page) — https://webflow.com/login?r=https://webflow.com/dashboard&m=WW91IGhhdmUgYmVlbiBsb2dnZWQgb3V0LiBQbGVhc2Ugc2lnbiBiYWNrIGluIHRvIGNvbnRpbnVlLg==
  - Login - Webflow Log in to your account Continue with SSO You have been logged out. Please sign back in to continue. or Forgot your password? Continue Don't have an account? Sign up
- **[S10]** BYRN 10-K (sec)
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

# BYRN — Planned Research Report

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
- Company: Byrna Technologies, Inc.
- Sector / industry: Industrials / Aerospace & Defense
- Price: 3.7099
- 52-week range: $3.17 – $30.62
- Market cap: $84.19M
- Enterprise value: $68.09M
- Shares outstanding: 22.69M
- Beta: 1.786
- Book equity: $65.76M
- Revenue (latest): $118.12M
- EBITDA (latest): $13.95M
- Free cash flow (latest): -$9.20M
- Operating income: $11.84M
- Operating margin: 10.0%
- EV / EBITDA: 4.9x
- ROIC: 21.8%
- FCF yield: -10.9%
- Debt / Equity: 0.035676810073452254
- FCF / share: -$0.41
- Revenue / share: $5.21

### Capital structure
- Cash: $13.73M
- Short-term debt: $734.00K
- Long-term debt: $1.61M
- Total debt: $2.35M
- Net debt: -$11.38M
- Net debt / EBITDA: -0.8x

### Growth
- Revenue CAGR: 35.0%
- FCF CAGR: —
- Latest revenue YoY: 37.7%
- Latest FCF YoY: -198.2%

### Market expectations (yfinance, sparse)
- Mean target: $6.83
- Target range: $4.00 – $12.00
- Recommendation: buy

_Consensus revenue/EBITDA forecasts are often unavailable via free feeds; treat targets as point-in-time only._

### Historical KPIs (multi-year)

| Year | Revenue | OCF | Capex | FCF | EBITDA | LT debt | Cash | Net debt | Net income |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2025 | $118.12M | -$1.57M | $7.63M | -$9.20M | $13.95M | $2.35M | $13.73M | -$11.38M | $9.69M |
| 2024 | $85.76M | $11.74M | $2.37M | $9.37M | $8.16M | $2.64M | $16.83M | -$14.19M | $12.79M |
| 2023 | $42.64M | $3.89M | $903.00K | $2.99M | -$6.53M | $1.90M | $20.50M | -$18.60M | -$8.19M |
| 2022 | $48.04M | -$13.83M | $3.25M | -$17.08M | -$6.88M | $2.55M | $20.07M | -$17.52M | -$7.88M |

## Charts

### Revenue & FCF history
![Revenue & FCF history](/charts/BYRN_income_revenue_fcf.png)

## Web research — web_research

- Queries: BYRN news, Byrna Technologies, Inc. earnings OR catalyst
- Unique hits: 14
- Pages fetched: 1/3

### Web synthesis — web_research (rule-based fallback — Ollama unavailable)
**Keyword hits:** revenue, margin, market

- | www.marketbeat.com | https://www.marketbeat.com/stocks/NASDAQ/BYRN/news/ Read today's BYRN news from trusted media outlets at MarketBeat.
- (BYRN) | ir.byrna.com | https://ir.byrna.com/news-events/press-releases Jun 18, 2026 · Byrna Technologies Realigns Sales and Marketing Function to Strengthen Brand Messaging and Accelerate Retail Expansion; Appoints HLK as Agency of Record  [HIT] Byrna Technologies Inc.
- (BYRN) Reports Q2 Loss, Lags Revenue Estimates | Zacks.com on MSN | https://www.msn.com/en-us/money/topstocks/byrna-technologies-inc-byrn-reports-q2-loss-lags-revenue-estimates/ar-AA27zswG?ocid=BingNewsVerp Byrna Technologies Inc.
- | Asianet Newsable on MSN | https://www.msn.com/en-in/money/markets/why-did-stla-mat-byrn-stocks-tumble-to-52-week-lows-today/ar-AA27BZfD?ocid=BingNewsVerp Stellantis, Mattel, and Byrna Technologies tumbled to fresh lows on Thursday amid regional weaknesses, poor outlook, and Wall Street caution.
- | Zacks · via Yahoo Finance | https://finance.yahoo.com/markets/stocks/articles/analysts-estimate-byrna-technologies-inc-140001067.html Byrna Technologies (BYRN) doesn't possess the right combination of the two key ingredients for a...
- · via Yahoo Finance | https://finance.yahoo.com/markets/stocks/articles/byrna-technologies-byrn-rising-sales-211339237.html Byrna Technologies Inc.
- | https://www.marketbeat.com/stocks/NASDAQ/BYRN/news/ BYRN News Today | Why did Byrna Technologies stock go up today?
- (From Awesomely) (Ad) Free BYRN Stock Alerts Byrna Technologies (BYRN) News Today $3.70 +0.34 (+9.94%) As of 01:05 PM Eastern This is a fair market value price provided by Massive.

### Sources found
- [Byron Nelson](https://en.wikipedia.org/wiki/Byron_Nelson)
  - John Byron Nelson Jr. (February 4, 1912 – September 26, 2006) was an American professional golfer between 1935 and 1946, widely considered one of the greates…
- [BYRN News Today | Why did Byrna Technologies stock go up ...](https://www.marketbeat.com/stocks/NASDAQ/BYRN/news/)
  - Read today's BYRN news from trusted media outlets at MarketBeat.
- [Byrna Technologies Inc. (BYRN) Latest Stock News & Headlines ...](https://finance.yahoo.com/quote/BYRN/news/?fr=sycsrp_catchall)
  - Get the latest Byrna Technologies Inc. (BYRN) stock news and headlines to help you in your trading and investing decisions.
- [Press Releases :: Byrna Technologies Inc. (BYRN)](https://ir.byrna.com/news-events/press-releases)
  - Jun 18, 2026 · Byrna Technologies Realigns Sales and Marketing Function to Strengthen Brand Messaging and Accelerate Retail Expansion; Appoints HLK as Agency…
- [Byrna Technologies Inc. (BYRN) Reports Q2 Loss, Lags Revenue Estimates](https://www.msn.com/en-us/money/topstocks/byrna-technologies-inc-byrn-reports-q2-loss-lags-revenue-estimates/ar-AA27zswG?ocid=BingNewsVerp)
  - Byrna Technologies Inc. (BYRN) came out with a quarterly loss of $0.44 per share versus the Zacks Consensus Estimate of a ...
- [Noteworthy Friday Option Activity: BYRN, MARA, ASTS](https://www.nasdaq.com/articles/noteworthy-friday-option-activity-byrn-mara-asts)
  - Looking at options trading activity among components of the Russell 3000 index, there is noteworthy activity today in Byrna Technologies Inc (Symbol: BYRN), …
- [Why did STLA, MAT, BYRN stocks tumble to 52-week lows today?](https://www.msn.com/en-in/money/markets/why-did-stla-mat-byrn-stocks-tumble-to-52-week-lows-today/ar-AA27BZfD?ocid=BingNewsVerp)
  - Stellantis, Mattel, and Byrna Technologies tumbled to fresh lows on Thursday amid regional weaknesses, poor outlook, and Wall Street caution.
- [Byrna Technologies (BYRN) Is a Great Choice for 'Trend' Investors, Here's Why](https://www.nasdaq.com/articles/byrna-technologies-byrn-great-choice-trend-investors-heres-why-1)
  - When it comes to short-term investing or trading, they say "the trend is your friend." And there's no denying that this is the most profitable strategy. But …
- [Financial Results :: Byrna Technologies Inc. (BYRN)](https://ir.byrna.com/financial-information/financial-results)
  - Financial Info. Financial Results · Income Statement · Balance Sheet · Cash Flow. 2026. Q2 2026. Quarter Ended May 31, 2026. Earnings Release.
- [Investor Relations :: Byrna Technologies Inc. (BYRN)](https://ir.byrna.com/)
  - Byrna Technologies Inc. (NASDAQ: BYRN) is a technology company specializing in the areas of Personal Security Devices, Military, Law Enforcement, ...
- [Byrna Technologies Inc. (BYRN) - Yahoo Finance](https://finance.yahoo.com/quote/BYRN/)
  - 7 hours ago ... Byrna Technologies Inc., a less-lethal self-defense technology company, develops, manufactures, and sells less-lethal personal security ...
- [Byrna Technologies (BYRN) investor relations material - Quartr](https://quartr.com/companies/byrna-technologies-inc_10097)
  - Complete event summary combining all related documents: earnings call transcript, report, and slide presentation. Logotype for Byrna Technologies Inc. Q2 202…

## Put opportunities (heuristic) [S2]
- Expiration: 2026-09-18 (DTE 56)
- Candidates: 0
- ATM IV (est.): 146.1%
- IV rank: — (1 local samples)
- HV rank (20d realized): 100.0%


_Note: Delta band approximated via % OTM when greeks are unavailable; IV rank needs ~20+ local daily IV samples (have 1); run the options screen over time to build history.; HV rank is realized-vol rank (20d HV vs ~1y); useful when IV history is thin._

## Research loop (think → act)

1. _heuristic_ — Coverage looks adequate for this pass; stopping iterative loop.

## Sources

- **[S1]** BYRN fundamentals (yfinance)
  - Byrna Technologies, Inc.: price=3.7099, rev=118120000.0, fcf=-9201000.0, shares=22693356.0, rev_cagr=0.3497464711860472, ROIC=0.2177063410328086, FCF yield=-0.10928841022600287
- **[S2]** BYRN put screen (yfinance_options)
  - Expiration 2026-09-18 (DTE 56): 0 candidates; IV=1.4609401953124999, IV rank=None, HV rank=1.0. Delta band approximated via % OTM when greeks are unavailable; IV rank needs ~20+…
- **[S3]** Byron Nelson (web) — https://en.wikipedia.org/wiki/Byron_Nelson
  - John Byron Nelson Jr. (February 4, 1912 – September 26, 2006) was an American professional golfer between 1935 and 1946, widely considered one of the greatest golfers of all tim…
- **[S4]** BYRN News Today | Why did Byrna Technologies stock go up ... (web) — https://www.marketbeat.com/stocks/NASDAQ/BYRN/news/
  - Read today's BYRN news from trusted media outlets at MarketBeat.
- **[S5]** Byrna Technologies Inc. (BYRN) Latest Stock News & Headlines ... (web) — https://finance.yahoo.com/quote/BYRN/news/?fr=sycsrp_catchall
  - Get the latest Byrna Technologies Inc. (BYRN) stock news and headlines to help you in your trading and investing decisions.
- **[S6]** Press Releases :: Byrna Technologies Inc. (BYRN) (web) — https://ir.byrna.com/news-events/press-releases
  - Jun 18, 2026 · Byrna Technologies Realigns Sales and Marketing Function to Strengthen Brand Messaging and Accelerate Retail Expansion; Appoints HLK as Agency of Record
- **[S7]** Byrna Technologies Inc. (BYRN) Reports Q2 Loss, Lags Revenue Estimates (web) — https://www.msn.com/en-us/money/topstocks/byrna-technologies-inc-byrn-reports-q2-loss-lags-revenue-estimates/ar-AA27zswG?ocid=BingNewsVerp
  - Byrna Technologies Inc. (BYRN) came out with a quarterly loss of $0.44 per share versus the Zacks Consensus Estimate of a ...
- **[S8]** Noteworthy Friday Option Activity: BYRN, MARA, ASTS (web) — https://www.nasdaq.com/articles/noteworthy-friday-option-activity-byrn-mara-asts
  - Looking at options trading activity among components of the Russell 3000 index, there is noteworthy activity today in Byrna Technologies Inc (Symbol: BYRN), where a total volume…
- **[S9]** Why did STLA, MAT, BYRN stocks tumble to 52-week lows today? (web) — https://www.msn.com/en-in/money/markets/why-did-stla-mat-byrn-stocks-tumble-to-52-week-lows-today/ar-AA27BZfD?ocid=BingNewsVerp
  - Stellantis, Mattel, and Byrna Technologies tumbled to fresh lows on Thursday amid regional weaknesses, poor outlook, and Wall Street caution.
- **[S10]** Byrna Technologies (BYRN) Is a Great Choice for 'Trend' Investors, Here's Why (web) — https://www.nasdaq.com/articles/byrna-technologies-byrn-great-choice-trend-investors-heres-why-1
  - When it comes to short-term investing or trading, they say "the trend is your friend." And there's no denying that this is the most profitable strategy. But making sure of the s…
- **[S11]** BYRN News Today | Why did Byrna Technologies stock go up today? (web_page) — https://www.marketbeat.com/stocks/NASDAQ/BYRN/news/
  - BYRN News Today | Why did Byrna Technologies stock go up today? Skip to main content → BlackRock is hoarding it. JPMorgan is hoarding it. Do you own it? (From Awesomely) (Ad) Fr…

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

# BYRN — Planned Research Report

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
- Company: Byrna Technologies, Inc.
- Sector / industry: Industrials / Aerospace & Defense
- Price: 3.7
- 52-week range: $3.17 – $30.62
- Market cap: $83.97M
- Enterprise value: $68.09M
- Shares outstanding: 22.69M
- Beta: 1.786
- Book equity: $65.76M
- Revenue (latest): $118.12M
- EBITDA (latest): $13.95M
- Free cash flow (latest): -$9.20M
- Operating income: $11.84M
- Operating margin: 10.0%
- EV / EBITDA: 4.9x
- ROIC: 21.8%
- FCF yield: -11.0%
- Debt / Equity: 0.035676810073452254
- FCF / share: -$0.41
- Revenue / share: $5.21

### Capital structure
- Cash: $13.73M
- Short-term debt: $734.00K
- Long-term debt: $1.61M
- Total debt: $2.35M
- Net debt: -$11.38M
- Net debt / EBITDA: -0.8x

### Growth
- Revenue CAGR: 35.0%
- FCF CAGR: —
- Latest revenue YoY: 37.7%
- Latest FCF YoY: -198.2%

### Market expectations (yfinance, sparse)
- Mean target: $6.83
- Target range: $4.00 – $12.00
- Recommendation: buy

_Consensus revenue/EBITDA forecasts are often unavailable via free feeds; treat targets as point-in-time only._

### Historical KPIs (multi-year)

| Year | Revenue | OCF | Capex | FCF | EBITDA | LT debt | Cash | Net debt | Net income |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2025 | $118.12M | -$1.57M | $7.63M | -$9.20M | $13.95M | $2.35M | $13.73M | -$11.38M | $9.69M |
| 2024 | $85.76M | $11.74M | $2.37M | $9.37M | $8.16M | $2.64M | $16.83M | -$14.19M | $12.79M |
| 2023 | $42.64M | $3.89M | $903.00K | $2.99M | -$6.53M | $1.90M | $20.50M | -$18.60M | -$8.19M |
| 2022 | $48.04M | -$13.83M | $3.25M | -$17.08M | -$6.88M | $2.55M | $20.07M | -$17.52M | -$7.88M |

## Charts

### Revenue & FCF history
![Revenue & FCF history](/charts/BYRN_fast_revenue_fcf.png)

### DCF scenario prices
![DCF scenario prices](/charts/BYRN_fast_dcf_scenarios.png)

### Base-case FCF path
![Base-case FCF path](/charts/BYRN_fast_base_fcf_path.png)

## DCF valuation (base / bull / bear) [S2]

> Simplified revenue->FCF DCF. Not investment advice; assumptions are editable heuristics.

- Spot price: $3.70
- Base revenue: $118.12M
- Shares: 22,693,356
- Net debt (Debt−Cash): -$11.38M

| Scenario | Growth | FCF margin | WACC | Term. g | Equity value | Share price | Upside |
|----------|--------|------------|------|---------|--------------|-------------|--------|
| bear | 25.0% | 1.0% | 12.0% | 1.5% | $39.46M | $1.74 | -53.0% |
| base | 35.0% | 3.0% | 10.0% | 2.5% | $180.36M | $7.95 | 114.8% |
| bull | 42.0% | 8.0% | 9.0% | 3.0% | $732.01M | $32.26 | 771.8% |

### Assumption notes
- Base revenue growth seeded from historical rate (37.7%).
- Latest FCF margin was -7.8%; scenarios use normalized positive margins for a going-concern DCF.


### Base-case projected FCF

- Year 1: revenue $159.46M, FCF $4.78M (PV $4.35M)
- Year 2: revenue $215.27M, FCF $6.46M (PV $5.34M)
- Year 3: revenue $290.62M, FCF $8.72M (PV $6.55M)
- Year 4: revenue $392.34M, FCF $11.77M (PV $8.04M)
- Year 5: revenue $529.65M, FCF $15.89M (PV $9.87M)
- Terminal value $217.16M (PV $134.84M)

## Put opportunities (heuristic) [S3]
- Expiration: 2026-09-18 (DTE 56)
- Candidates: 0
- ATM IV (est.): 163.3%
- IV rank: — (1 local samples)
- HV rank (20d realized): 100.0%


_Note: Delta band approximated via % OTM when greeks are unavailable; IV rank needs ~20+ local daily IV samples (have 1); run the options screen over time to build history.; HV rank is realized-vol rank (20d HV vs ~1y); useful when IV history is thin._

## Research loop (think → act)

1. _heuristic_ — Coverage looks adequate for this pass; stopping iterative loop.

## Sources

- **[S1]** BYRN fundamentals (yfinance)
  - Byrna Technologies, Inc.: price=3.7, rev=118120000.0, fcf=-9201000.0, shares=22693356.0, rev_cagr=0.3497464711860472, ROIC=0.2177063410328086, FCF yield=-0.10958083027898058
- **[S2]** BYRN DCF valuation (dcf)
  - Base share price=7.947753124041503, bull=32.256417371811665, bear=1.7389795505454393
- **[S3]** BYRN put screen (yfinance_options)
  - Expiration 2026-09-18 (DTE 56): 0 candidates; IV=1.6328143359374998, IV rank=None, HV rank=1.0. Delta band approximated via % OTM when greeks are unavailable; IV rank needs ~20+…

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
