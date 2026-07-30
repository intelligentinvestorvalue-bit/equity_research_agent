# BYRN — Full research pack

> Not investment advice. Local research draft only.

**Templates:** memo, valuation, deep, income, fast
**Generated:** 2026-07-24T20:30:21.613279+00:00



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
- Company: Byrna Technologies, Inc.
- Sector / industry: Industrials / Aerospace & Defense
- Price: 3.54
- 52-week range: $3.17 – $30.62
- Market cap: $80.33M
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
- FCF yield: -11.5%
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
![Revenue & FCF history](/charts/BYRN_memo_revenue_fcf.png)

### DCF scenario prices
![DCF scenario prices](/charts/BYRN_memo_dcf_scenarios.png)

### Base-case FCF path
![Base-case FCF path](/charts/BYRN_memo_base_fcf_path.png)

### EV/EBITDA scenario prices
![EV/EBITDA scenario prices](/charts/BYRN_memo_ev_ebitda_scenarios.png)

### Headwind/tailwind price ranges
![Headwind/tailwind price ranges](/charts/BYRN_memo_scenario_ranges.png)

### Normalized price vs peers
![Normalized price vs peers](/charts/BYRN_memo_peers_normalized.png)

## DCF valuation (base / bull / bear) [S3]

> Simplified revenue->FCF DCF. Not investment advice; assumptions are editable heuristics.

- Spot price: $3.54
- Base revenue: $118.12M
- Shares: 22,693,356
- Net debt (Debt−Cash): -$11.38M

| Scenario | Growth | FCF margin | WACC | Term. g | Equity value | Share price | Upside |
|----------|--------|------------|------|---------|--------------|-------------|--------|
| bear | 25.0% | 1.0% | 12.0% | 1.5% | $39.46M | $1.74 | -50.9% |
| base | 35.0% | 3.0% | 10.0% | 2.5% | $180.36M | $7.95 | 124.5% |
| bull | 42.0% | 8.0% | 9.0% | 3.0% | $732.01M | $32.26 | 811.2% |

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

## Valuation — EV/EBITDA scenarios [S2]

> Priced-in model: implied price = (EBITDA × EV/EBITDA − net debt) ÷ shares. Not a forecast.

- Spot: $3.54
- Net debt used: -$11.38M

| Scenario | EBITDA | EV/EBITDA | Implied EV | Equity value | Implied price |
|---|---:|---:|---:|---:|---:|
| bear | $9.77M | 3.7x | $35.74M | $47.13M | $2.08 |
| base | $13.95M | 4.9x | $68.09M | $79.47M | $3.50 |
| bull | $16.74M | 6.1x | $102.13M | $113.51M | $5.00 |

- Base EBITDA seeded from latest reported/TTM figure (13,953,000).
- Base multiple seeded from current EV/EBITDA (4.9x).

## Scenario price ranges (headwinds & tailwinds) [S38]

> Medium-term (18–36 months (medium / medium-long term)) driver → EV/EBITDA bridge. Distinct from the FCF DCF path. Not investment advice.

- Spot: $3.54
- Sparse Street mean target: $6.83
- Anchor multiple: 4.9x (driver_ev_ebitda_bridge)
- Anchor EBITDA: $13.95M
- Probability-weighted midpoint: **$4.18** (heuristic weights, not a rating)
- Driver extraction: `rules`

### Headwinds (bear-case fuel)

- **Negative free cash flow** — Latest FCF -$9.20M — cash burn raises financing risk _(source: fundamentals)_
- **Balance-sheet / refinancing pressure** — sector=Industrials industry=Aerospace & Defense revenue=118120000.0 ebitda=13953000.0 fcf=-9201000.0 net_debt=-11381000.0 nd_ebitda=-0.8156668816741919 target=6.83333 rec=buy _(source: fundamentals)_
- **Regulatory / legal risk** — Byrna Technologies (BYRN) Company Profile & DescriptionByrna Technologies Inc Customers by Division and Industry ...Market Demand: Definition, How to Calculate, DeterminantsPower D _(source: web)_
- **Competitive / pricing pressure** — Byrna Technologies Inc Stock Price Today | NASDAQ: BYRN Live - Byrna Technologies Inc. (NASDAQ:BYRN) announced today that it has selected Acceleration Partners as its...BYRN's last _(source: web)_

### Tailwinds (bull-case fuel)

- **Manageable leverage** — Net debt / EBITDA ≈ -0.8x — room for reinvestment or returns _(source: fundamentals)_
- **Revenue growth momentum** — Latest revenue YoY ≈ 37.7% _(source: fundamentals)_
- **Street target implies upside** — Mean target $6.83 vs spot $3.54 _(source: fundamentals)_
- **Product / pricing power** — Needham Reiterates Buy on monday.com (MNDY), Sets $250 Price Targe monday.com Ltd. (NASDAQ:MNDY) is one of the AI Stocks Analysts Are Watching Closely. On August 18,... _(source: web)_
- **Growth / execution upside** — Byrna Technologies (BYRN) Stock Price, News & Analysis Should You Buy or Sell Byrna Technologies Stock? Get The Latest BYRN Stock Analysis, Price Target, Earnings Estimates, Headli _(source: web)_
- **Multiple re-rating / Street upgrades** — BYRN | Byrna Technologies Inc. Analyst Estimates & Ratings – WSJBYRN Q2 Deep Dive: Market Skepticism Amid Channel Expansion ...BYRN Q2 Deep Dive: Market Skepticism Amid Channel Exp _(source: web)_
- **Contract / backlog wins** — Byrna Technologies Q2 2026 Deep Dive: Bottom Line Misses, Revenue Down 42% - Alphastreet 2 weeks ago - The aerospace and defense industry context makes this performance particularl _(source: web)_
- **Capital returns / FCF inflection** — Byrna Technologies Analyst Ratings and Price Targets | NASDAQ:BYRN | Benzinga Byrna Technologies Analyst Ratings and Price Targets | NASDAQ:BYRN | Benzinga Benzinga España Italia 대 _(source: web_page)_

### Price ranges by case

| Case | Prob. | Metric vs TTM | Multiple | Price low | Mid | High | Upside vs spot |
|---|---:|---:|---:|---:|---:|---:|---:|
| bear | 0.17 | 0.76x | 3.3x | $1.90 | $2.05 | $2.21 | -42% |
| base | 0.42 | 1.08x | 4.9x | $3.51 | $3.74 | $3.97 | +6% |
| bull | 0.42 | 1.25x | 6.3x | $4.89 | $5.38 | $5.86 | +52% |

#### Bear — headwinds dominate

Headwinds bite: weaker operating trajectory and multiple compression. Equity duration shrinks if cash generation fails to offset leverage / competitive pressure.

- **Range:** $1.90 – $2.21 (mid $2.05) · EBITDA $10.60M · multiple 3.3x
- Driver: **Negative free cash flow** — Latest FCF -$9.20M — cash burn raises financing risk
- Driver: **Balance-sheet / refinancing pressure** — sector=Industrials industry=Aerospace & Defense revenue=118120000.0 ebitda=13953000.0 fcf=-9201000.0 net_debt=-11381000.0 nd_ebitda=-0.8156668816741919 target=6
- Driver: **Regulatory / legal risk** — Byrna Technologies (BYRN) Company Profile & DescriptionByrna Technologies Inc Customers by Division and Industry ...Market Demand: Definition, How to Calculate,
- Driver: **Competitive / pricing pressure** — Byrna Technologies Inc Stock Price Today | NASDAQ: BYRN Live - Byrna Technologies Inc. (NASDAQ:BYRN) announced today that it has selected Acceleration Partners 

#### Base — mixed execution

Balanced path: some tailwinds offset headwinds. Operating scale roughly holds with modest repair/normalization; valuation stays near the current EV/EBITDA anchor.

- **Range:** $3.51 – $3.97 (mid $3.74) · EBITDA $15.07M · multiple 4.9x
- Driver: **Manageable leverage** — Net debt / EBITDA ≈ -0.8x — room for reinvestment or returns
- Driver: **Revenue growth momentum** — Latest revenue YoY ≈ 37.7%
- Driver: **Negative free cash flow** — Latest FCF -$9.20M — cash burn raises financing risk
- Driver: **Balance-sheet / refinancing pressure** — sector=Industrials industry=Aerospace & Defense revenue=118120000.0 ebitda=13953000.0 fcf=-9201000.0 net_debt=-11381000.0 nd_ebitda=-0.8156668816741919 target=6

#### Bull — tailwinds dominate

Tailwinds compound: operating improvement plus a re-rating toward peer or recovery multiples as balance-sheet and growth narratives improve.

- **Range:** $4.89 – $5.86 (mid $5.38) · EBITDA $17.44M · multiple 6.3x
- Driver: **Manageable leverage** — Net debt / EBITDA ≈ -0.8x — room for reinvestment or returns
- Driver: **Revenue growth momentum** — Latest revenue YoY ≈ 37.7%
- Driver: **Street target implies upside** — Mean target $6.83 vs spot $3.54
- Driver: **Product / pricing power** — Needham Reiterates Buy on monday.com (MNDY), Sets $250 Price Targe monday.com Ltd. (NASDAQ:MNDY) is one of the AI Stocks Analysts Are Watching Closely. On Augus
- Driver: **Growth / execution upside** — Byrna Technologies (BYRN) Stock Price, News & Analysis Should You Buy or Sell Byrna Technologies Stock? Get The Latest BYRN Stock Analysis, Price Target, Earnin

### Method notes

- Item 1A risks weighted toward headwinds.
- Mapping follows Gemini/Perplexity-style scenario memos: qualitative drivers → operating metric & multiple paths → share-price ranges over a medium-term horizon.

## Peer & factor comps

- Sector / industry: Industrials / Aerospace & Defense
- Peers: —

| Ticker | Mkt cap | EV/EBITDA | ND/EBITDA | Beta | 1y | 5y | Vol |
|---|---:|---:|---:|---:|---:|---:|---:|
| BYRN | $80.3M | -25.9x | 3.2x | 1.79 | -85.0% | -84.6% | 75.1% |

- No industry peer map match; comps limited to the subject ticker.

_Price returns are price-only (dividends ignored). Peer set is heuristic, not a formal comps universe._

## Earnings, guidance & revision catalysts

- Next earnings (calendar): 2026-10-08

| Date | EPS est | EPS actual | Surprise | 1-day move |
|---|---:|---:|---:|---:|
| 2026-10-08 | -0.11 | — | — | — |
| 2026-07-09 | -0.12 | -0.04 | 0.08 | -1.8% |
| 2026-04-09 | 0.05 | 0.07 | 0.02 | -10.6% |
| 2026-02-05 | 0.11 | 0.17 | 0.06 | 11.6% |
| 2025-10-09 | 0.05 | 0.12 | 0.07 | -4.6% |
| 2025-07-10 | 0.05 | 0.13 | 0.08 | -9.6% |
| 2025-04-10 | 0.02 | 0.11 | 0.09 | -0.8% |
| 2025-02-07 | 0.05 | 0.41 | 0.36 | 15.4% |
| 2024-10-09 | -0.01 | 0.04 | 0.05 | -2.8% |
| 2024-07-09 | -0.01 | 0.09 | 0.10 | -7.3% |
| 2024-04-05 | -0.08 | 0.05 | 0.13 | 13.3% |
| 2024-02-14 | -0.04 | -0.01 | 0.03 | 12.1% |

_EPS surprise vs 1-day move Pearson r=0.493 (n=11, p≈0.089); treat as suggestive only._

_Guidance vs Street and adjusted EBITDA are often missing from free feeds; use web/SEC sections for narrative guidance._

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

Byrna Technologies, Inc. (BYRN) trades near 3.54 with market cap $80.33M and EV $68.09M. Net debt is -$11.38M (ND/EBITDA -0.8156668816741919). Latest revenue $118.12M, EBITDA $13.95M, FCF -$9.20M.

**Goal focus:** Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers.

What matters most (framework): balance-sheet trajectory, cash generation vs leverage, and whether market expectations (sparse free-data targets) already price execution risk.

EV/EBITDA implied prices — bear $2.08 / base $3.50 / bull $5.00.

## Company setup & business model

No Item 1 Business text extracted.

_Source: latest 10-K Item 1 (Business), summarized locally._

## Variant perception

- **Consensus frame (sparse):** recommendation=buy, mean target=6.83333.
- **Bear:** leverage and execution risk dominate; cash generation fails to cover refinancing / reinvestment needs; equity remains constrained by net debt.
- **Bull:** cash-flow and strategic optionality re-rate the equity as leverage falls and growth/mix improves.
- **Middle:** returns may track free-cash-flow more than headline revenue — verify with driver analysis tab.

## Catalysts & monitoring

- Next earnings window (calendar): 2026-10-08
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
| Guidance / outlook | Forward cash/earnings path | Byrna Technologies Inc Us (BYRN) Stock Forecast, Price Targets and... Analyze Forecast. Average Price Target.The average price target for Byrna Technologies Inc Us is 8.25. This is | Byrna Technologies Inc Us (BYRN) Stock Forecast, Price Targets and... |
| Contract / backlog | Demand durability | Byrna (BYRN) Research Report - StockStory April 9, 2026 - Luckily, Byrna’s sales grew at an incredible 36.7% compounded annual growth rate over the last five years. Its growth beat | Byrna (BYRN) Research Report - StockStory |
| Margin / EBITDA | Mix and operating leverage | BYRN Q3 Deep Dive: Retail Expansion and AI-Driven Marketing Fuel Growth — TradingView News Search EN Get started BYRN Q3 Deep Dive: Retail Expansion and AI-Driven Marketing Fuel Gr | BYRN Q3 Deep Dive: Retail Expansion and AI-Driven Marketing Fuel Growth — TradingView News |

_Proxies are heuristic extractions from public web/SEC context; verify against primary filings._

## Catalyst calendar

| Window | Catalyst | Notes |
|---|---|---|
| 2026-10-08 | Earnings | Next report date from yfinance calendar |
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
| Jul 22, 2025 | Web event | Byrna Technologies' Recent Surge in Investor Interest: A Deep ... |
| Jul 11, 2025 | Web event | BYRN | Byrna Technologies Inc. Analyst Estimates & Ratings – WSJBYRN Q2 Deep Dive: Market Skepticism Amid Channel Expansion ...BYRN Q2 Deep  |
| Jul 11, 2025 | Web event | BYRN Q2 Deep Dive: Market Skepticism Amid Channel Expansion ... |
| Jul 11, 2025 | Web event | BYRN Q2 Deep Dive: Market Skepticism Amid Channel Expansion ... |
| Jun 25, 2026 | Web event | Byrna Technologies sets July 9 Q2 2026 call | BYRN Stock News |
| 2026/07/23 | Web event | Byrna Technologies (Nasdaq:BYRN) - Stock Analysis - Simply Wall St |
| October 10, 2025 | Web event | BYRN Q3 Deep Dive: Retail Expansion and AI-Driven Marketing Fuel Growth — TradingView News |
| April 10, 2026 | Web event | BYRN Q1 Deep Dive: Retail Expansion and E-Commerce Challenges Shape Near-Term Outlook |
| 2026-07-06 | Web event | BYRN Forecast, Price Target & Analyst Ratings | BYRNA TECHNOLOGIES INC (NASDAQ:BYRN) | ChartMill.com |
| April 9, 2026 | Web event | Byrna (BYRN) Research Report - StockStory |
| Jun 17, 2026 | Web event | Byrna Technologies (BYRN) Company Profile & DescriptionByrna Technologies Inc Customers by Division and Industry ...Market Demand: Definitio |
| Jun 17, 2026 | Web event | Byrna Technologies Inc Customers by Division and Industry ... |
| Jan 21, 2025 | Web event | Market Demand: Definition, How to Calculate, Determinants |
| Apr 7, 2026 | Web event | Understanding Demand: Key Determinants and the Demand Curve |

## Web research — web_analysts

- Queries: BYRN analyst price target, Byrna Technologies, Inc. stock rating OR consensus OR upgrade OR downgrade, BYRN Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers analyst, BYRN guidance OR investor day OR catalyst
- Unique hits: 19
- Pages fetched: 2/3

### Web synthesis — web_analysts (rule-based fallback — Ollama unavailable)
**Keyword hits:** guidance, revenue, margin, product, service, market

- | Asianet Newsable | https://www.msn.com/en-in/money/markets/why-did-stla-mat-byrn-stocks-tumble-to-52-week-lows-today/ar-AA27BZfD Stellantis, Mattel, and Byrna Technologies tumbled to fresh lows on Thursday amid regional weaknesses, poor outlook, and Wall Street caution.
- [HIT] Analysts Have Mixed Views on Glacier Bancorp (GBCI) | Insider Monkey · via Yahoo Finance | https://finance.yahoo.com/markets/stocks/articles/analysts-mixed-views-glacier-bancorp-201806470.html Glacier Bancorp, Inc.
- (BYRN) stock, with detailed revenue and earnings estimates.
- [HIT] Byrna Technologies (BYRN) Stock Price, News & Analysis | www.marketbeat.com | https://www.marketbeat.com/stocks/NASDAQ/BYRN/ Should You Buy or Sell Byrna Technologies Stock?
- Get The Latest BYRN Stock Analysis, Price Target, Earnings Estimates, Headlines, and Short Interest at MarketBeat.
- | www.ainvest.com | https://www.ainvest.com/news/byrna-technologies-surge-investor-interest-deep-dive-catalysts-market-positioning-2507/ Jul 22, 2025 · This article dissects the catalysts behind Byrna's resurgence, evaluates its competitive advantages, and assesses whether the stock's recent surge reflects a genuine inflection point IPCX -- or an overhyped rally.
- Analyst Estimates & Ratings – WSJBYRN Q2 Deep Dive: Market Skepticism Amid Channel Expansion ...BYRN Q2 Deep Dive: Market Skepticism Amid Channel Expansion ...Byrna BYRN plunges 50% to 16.1 P/E valuation analysis - LinkedInByrna Technologies Inc.
- | www.wsj.com | https://www.wsj.com/market-data/quotes/BYRN/research-ratings Byrna Technologies Inc.

### Sources found
- [Byrna Technologies Inc Us (BYRN) Stock Forecast, Price Targets and...](https://www.tipranks.com/stocks/byrn/forecast)
  - Analyze Forecast. Average Price Target.The average price target for Byrna Technologies Inc Us is 8.25. This is based on 2 Wall Streets Analysts 12-month pric…
- [Byrna Technologies Analyst Ratings and Price Targets | Benzinga](https://www.benzinga.com/quote/BYRN/analyst-ratings)
  - The analyst firm set a price target for $31.00 expecting BYRN to rise to within 12 months (a possible 233.33% upside). 6 analyst firms have reported ratings …
- [BYRN Forecast — Price Target — Prediction for 2027 — TradingView](https://www.tradingview.com/symbols/NASDAQ-BYRN/forecast/)
  - Price target. 29.000.000.00%. The 5 analysts offering 1-year price forecasts have a max estimate of — and a min estimate of —. Analyst rating. Based on 5 ana…
- [Byrna Technologies Inc. (BYRN) Analyst Insights, Price Targets...](https://finance.yahoo.com/quote/BYRN/analyst-insights/)
  - Analyst Price Targets. 7.50. 13.67 Average.Rating Buy. Price Action Lowers. Price Target 31 -> 21.
- [Why Byrna Technologies Inc.'s (BYRN) Stock Is Up 10.39%](https://www.aaii.com/investingideas/article/518457-why-byrna-technologies-inc8217s-byrn-stock-is-up-1039)
  - As of Friday, July 24, Byrna Technologies Inc.'s BYRN share price has surged by 10.39%, which has investors questioning if this is right time to sell.
- [Why did STLA, MAT, BYRN stocks tumble to 52-week lows today?](https://www.msn.com/en-in/money/markets/why-did-stla-mat-byrn-stocks-tumble-to-52-week-lows-today/ar-AA27BZfD)
  - Stellantis, Mattel, and Byrna Technologies tumbled to fresh lows on Thursday amid regional weaknesses, poor outlook, and Wall Street caution.
- [Needham Reiterates Buy on monday.com (MNDY), Sets $250 Price Targe](https://finance.yahoo.com/news/needham-reiterates-buy-monday-com-225907775.html)
  - monday.com Ltd. (NASDAQ:MNDY) is one of the AI Stocks Analysts Are Watching Closely. On August 18,...
- [Analysts Have Mixed Views on Glacier Bancorp (GBCI)](https://finance.yahoo.com/markets/stocks/articles/analysts-mixed-views-glacier-bancorp-201806470.html)
  - Glacier Bancorp, Inc. (NYSE:GBCI) is one of the 11 Best American Bank Stocks to Buy According to Wall Street Analysts. On February 11, Piper Sandler...
- [Byrna Technologies (BYRN) Stock Forecast & Analyst Price Targets](https://stockanalysis.com/stocks/byrn/forecast/)
  - Stock forecasts and analyst price target predictions for Byrna Technologies Inc. (BYRN) stock, with detailed revenue and earnings estimates.
- [Byrna Technologies (BYRN) Stock Price, News & Analysis](https://www.marketbeat.com/stocks/NASDAQ/BYRN/)
  - Should You Buy or Sell Byrna Technologies Stock? Get The Latest BYRN Stock Analysis, Price Target, Earnings Estimates, Headlines, and Short Interest at Marke…
- [Byrna Technologies Inc. (BYRN) Stock Price, Quote, News & Analysis ...](https://seekingalpha.com/symbol/BYRN)
  - A high-level overview of Byrna Technologies Inc. (BYRN) stock. View (BYRN) real-time stock price, chart, news, analysis, analyst reviews and more.
- [Byrna Technologies Inc. (BYRN) Stock Price, News, Quote & History ...](https://finance.yahoo.com/quote/BYRN/)
  - Find the latest Byrna Technologies Inc. (BYRN) stock quote, history, news and other vital information to help you with your stock trading and investing.

### Search warnings
- news:Byrna Technologies, Inc. stock rating OR consensus OR upgrade OR downgrade: No results found.
- news:BYRN Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers analyst: No results found.
- news:BYRN guidance OR investor day OR catalyst: No results found.

## Web research — web_drivers

- Queries: BYRN Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers, Byrna Technologies, Inc. BYRN outlook OR catalyst OR commodity OR uranium OR rare earth OR vanadium, BYRN sector drivers OR market demand, Byrna Technologies, Inc. BYRN backlog OR contract OR refinancing OR leverage
- Unique hits: 17
- Pages fetched: 2/3

### Web synthesis — web_drivers (rule-based fallback — Ollama unavailable)
**Keyword hits:** revenue, margin, customer, product, service, market, network

- [HIT] Byrna Technologies Q2 2026 Deep Dive: Bottom Line Misses, Revenue Down 42% - Alphastreet | news.alphastreet.com | https://news.alphastreet.com/byrna-technologies-q2-2026-deep-dive-bottom-line-misses-revenue-down-42/ 2 weeks ago - The aerospace and defense industry context makes this performance particularly concerning, as peer companies have generally benefited from elevated defense spending and geopolitical tensions driving demand.
- Byrna’s collapse during a period of sector tailwinds suggests company-specific execution failures or product-market fit issues rather than cyclical headwinds.
- [HIT] BYRN Q3 Deep Dive: Retail Expansion and AI-Driven Marketing Fuel Growth — TradingView News | www.tradingview.com | https://www.tradingview.com/news/stockstory:e728a26a7094b:0-byrn-q3-deep-dive-retail-expansion-and-ai-driven-marketing-fuel-growth/ October 10, 2025 - Byrna’s results for Q3 were met with a strongly positive market reaction, as the company’s operational momentum was underpinned by rapid growth in both retail channels and digital engagement.
- Management credited its robust 35% sales growth to the expansion of Byrna’s dealer network, successful mainstream advertising campaigns, and growing brand adoption.
- [HIT] BYRN Q1 Deep Dive: Retail Expansion and E-Commerce Challenges Shape Near-Term Outlook | finance.yahoo.com | https://finance.yahoo.com/markets/stocks/articles/byrn-q1-deep-dive-retail-072644011.html April 10, 2026 - Byrna’s first quarter saw sales climb year-over-year, but the company missed Wall Street’s revenue expectations and the market reacted sharply to the underperformance.
- Its growth beat the average industrials company and shows its offerings resonate with customers.
- [HIT] Byrna Technologies (BYRN) Company Profile & DescriptionByrna Technologies Inc Customers by Division and Industry ...Market Demand: Definition, How to Calculate, DeterminantsPower Data - IESOUnderstanding Demand: Key Determinants and the Demand CurveSector Byrn | Memory Beta, non-canon Star Trek Wiki | Fandom3.1 Demand, Supply, and Equilibrium in Markets for Goods and ...
- Jun 17, 2026 · Byrna Technologies Inc customers and markets, results by customer and performance relative to BYRN, by company and industry - CSIMarket Jan 21, 2025 · What’s it: Market demand is the sum of individual demand in the market at a given price.

### Sources found
- [Byrna Technologies Q2 2026 Deep Dive: Bottom Line Misses, Revenue Down 42% - Alphastreet](https://news.alphastreet.com/byrna-technologies-q2-2026-deep-dive-bottom-line-misses-revenue-down-42/)
  - 2 weeks ago - The aerospace and defense industry context makes this performance particularly concerning, as peer companies have generally benefited from elev…
- [BYRN Q3 Deep Dive: Retail Expansion and AI-Driven Marketing Fuel Growth — TradingView News](https://www.tradingview.com/news/stockstory:e728a26a7094b:0-byrn-q3-deep-dive-retail-expansion-and-ai-driven-marketing-fuel-growth/)
  - October 10, 2025 - Byrna’s results for Q3 were met with a strongly positive market reaction, as the company’s operational momentum was underpinned by rapid g…
- [BYRN Q1 Deep Dive: Retail Expansion and E-Commerce Challenges Shape Near-Term Outlook](https://finance.yahoo.com/markets/stocks/articles/byrn-q1-deep-dive-retail-072644011.html)
  - April 10, 2026 - Byrna’s first quarter saw sales climb year-over-year, but the company missed Wall Street’s revenue expectations and the market reacted sharp…
- [Byrna Tech | Quantum Capital](https://www.quantumcapitalresearch.com/byrn-call)
  - In this post, we break down our swing trade alert on BYRN — from the entry price to profit target — and how our members walked away with a +23% return.
- [Byrna Technologies, Inc. (BYRN) Stock Forecast: 1-Year Price Prediction & Outlook – Financhill](https://financhill.com/stock-forecast/byrn-stock-prediction)
  - 2 weeks ago - Byrna Technologies, Inc. (BYRN) stock is forecast up to $8.48 over the next 52 weeks. Financhill Stock Score: 10/100. Free AI-powered analysis …
- [BYRN Forecast, Price Target & Analyst Ratings | BYRNA TECHNOLOGIES INC (NASDAQ:BYRN) | ChartMill.com](https://www.chartmill.com/stock/quote/BYRN/analyst-ratings)
  - 11 analysts have analysed BYRN and the average price target is 14.23 USD. This implies a price increase of 184.58% is expected in the next year compared to t…
- [Byrna (BYRN) Research Report - StockStory](https://stockstory.org/us/stocks/nasdaq/byrn)
  - April 9, 2026 - Luckily, Byrna’s sales grew at an incredible 36.7% compounded annual growth rate over the last five years. Its growth beat the average indust…
- [BYRN - Byrna Technologies Stock Price - Barchart.com](https://www.barchart.com/stocks/quotes/BYRN)
  - Byrna Technologies Inc stocks price quote with latest real-time prices, charts, financials, latest news, technical analysis and opinions.
- [Byrna Technologies (BYRN) Company Profile & DescriptionByrna Technologies Inc Customers by Division and Industry ...Market Demand: Definition, How to Calculate, DeterminantsPower Data - IESOUnderstanding Demand: Key Determinants and the Demand CurveSector Byrn | Memory Beta, non-canon Star Trek Wiki | Fandom3.1 Demand, Supply, and Equilibrium in Markets for Goods and ...](https://stockanalysis.com/stocks/byrn/company/)
  - 1 day ago · Company profile for Byrna Technologies Inc. (BYRN) stock, with a description, list of executives, contact details and other key facts. Jun 17, 20…
- [Byrna Technologies Inc Customers by Division and Industry ...](https://csimarket.com/stocks/BYRN-Customers)
  - Jun 17, 2026 · Byrna Technologies Inc customers and markets, results by customer and performance relative to BYRN, by company and industry - CSIMarket
- [Market Demand: Definition, How to Calculate, Determinants](https://penpoin.com/market-demand/)
  - Jan 21, 2025 · What’s it: Market demand is the sum of individual demand in the market at a given price. Economists define demand as our willingness and abili…
- [Understanding Demand: Key Determinants and the Demand Curve](https://www.investopedia.com/terms/d/demand.asp)
  - Apr 7, 2026 · Market demand is the total quantity demanded by all consumers in a market for a given good, and aggregate demand is the total demand for all go…

### Search warnings
- news:BYRN Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers: No results found.
- news:Byrna Technologies, Inc. BYRN outlook OR catalyst OR commodity OR uranium OR rare earth OR vanadium: No results found.
- news:Byrna Technologies, Inc. BYRN backlog OR contract OR refinancing OR leverage: error sending request for url (https://duckduckgo.com/?q=Byrna+Technologies%2C+Inc.+BYRN+backlog+OR+contract+OR+refinancing+OR+leverage) > operation timed out

## SEC filing [S26]
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


## Research loop (think → act)

1. _heuristic_ — Coverage looks adequate for this pass; stopping iterative loop.

## Sources

- **[S1]** BYRN fundamentals (yfinance)
  - Byrna Technologies, Inc.: price=3.54, rev=118120000.0, fcf=-9201000.0, shares=22693356.0, rev_cagr=0.3497464711860472, ROIC=0.2177063410328086, FCF yield=-0.11453363487259767
- **[S2]** BYRN EV/EBITDA valuation (multiples)
  - Base implied price=3.5017565493618483, multiple=4.879639360710958
- **[S3]** BYRN DCF valuation (dcf)
  - Base share price=7.947753124041503, bull=32.256417371811665, bear=1.7389795505454393
- **[S4]** BYRN peer comps (peers)
  - Peers: ; rows=1
- **[S5]** BYRN earnings history (earnings)
  - rows=12; next=2026-10-08
- **[S6]** Byrna Technologies Inc Us (BYRN) Stock Forecast, Price Targets and... (web) — https://www.tipranks.com/stocks/byrn/forecast
  - Analyze Forecast. Average Price Target.The average price target for Byrna Technologies Inc Us is 8.25. This is based on 2 Wall Streets Analysts 12-month price targets, issued in…
- **[S7]** Byrna Technologies Analyst Ratings and Price Targets | Benzinga (web) — https://www.benzinga.com/quote/BYRN/analyst-ratings
  - The analyst firm set a price target for $31.00 expecting BYRN to rise to within 12 months (a possible 233.33% upside). 6 analyst firms have reported ratings in the last year.
- **[S8]** BYRN Forecast — Price Target — Prediction for 2027 — TradingView (web) — https://www.tradingview.com/symbols/NASDAQ-BYRN/forecast/
  - Price target. 29.000.000.00%. The 5 analysts offering 1-year price forecasts have a max estimate of — and a min estimate of —. Analyst rating. Based on 5 analysts giving stock r…
- **[S9]** Byrna Technologies Inc. (BYRN) Analyst Insights, Price Targets... (web) — https://finance.yahoo.com/quote/BYRN/analyst-insights/
  - Analyst Price Targets. 7.50. 13.67 Average.Rating Buy. Price Action Lowers. Price Target 31 -> 21.
- **[S10]** Why Byrna Technologies Inc.'s (BYRN) Stock Is Up 10.39% (web) — https://www.aaii.com/investingideas/article/518457-why-byrna-technologies-inc8217s-byrn-stock-is-up-1039
  - As of Friday, July 24, Byrna Technologies Inc.'s BYRN share price has surged by 10.39%, which has investors questioning if this is right time to sell.
- **[S11]** Why did STLA, MAT, BYRN stocks tumble to 52-week lows today? (web) — https://www.msn.com/en-in/money/markets/why-did-stla-mat-byrn-stocks-tumble-to-52-week-lows-today/ar-AA27BZfD
  - Stellantis, Mattel, and Byrna Technologies tumbled to fresh lows on Thursday amid regional weaknesses, poor outlook, and Wall Street caution.
- **[S12]** Needham Reiterates Buy on monday.com (MNDY), Sets $250 Price Targe (web) — https://finance.yahoo.com/news/needham-reiterates-buy-monday-com-225907775.html
  - monday.com Ltd. (NASDAQ:MNDY) is one of the AI Stocks Analysts Are Watching Closely. On August 18,...
- **[S13]** Analysts Have Mixed Views on Glacier Bancorp (GBCI) (web) — https://finance.yahoo.com/markets/stocks/articles/analysts-mixed-views-glacier-bancorp-201806470.html
  - Glacier Bancorp, Inc. (NYSE:GBCI) is one of the 11 Best American Bank Stocks to Buy According to Wall Street Analysts. On February 11, Piper Sandler...
- **[S14]** Byrna Technologies Analyst Ratings and Price Targets | NASDAQ:BYRN | Benzinga (web_page) — https://www.benzinga.com/quote/BYRN/analyst-ratings
  - Byrna Technologies Analyst Ratings and Price Targets | NASDAQ:BYRN | Benzinga Benzinga España Italia 대한민국 日本 Français My Account Login SPY 738.70 0.03% QQQ 684.59 0.05% BTC/USD …
- **[S15]** BYRN Forecast — Price Target — Prediction for 2027 — TradingView (web_page) — https://www.tradingview.com/symbols/NASDAQ-BYRN/forecast/
  - BYRN Forecast — Price Target — Prediction for 2027 — TradingView Search EN Get started Byrna Technologies, Inc. BYRN Nasdaq Stock Market BYRN Nasdaq Stock Market BYRN Nasdaq Sto…
- **[S16]** Byrna Technologies Q2 2026 Deep Dive: Bottom Line Misses, Revenue Down 42% - Alphastreet (web) — https://news.alphastreet.com/byrna-technologies-q2-2026-deep-dive-bottom-line-misses-revenue-down-42/
  - 2 weeks ago - The aerospace and defense industry context makes this performance particularly concerning, as peer companies have generally benefited from elevated defense spendin…
- **[S17]** BYRN Q3 Deep Dive: Retail Expansion and AI-Driven Marketing Fuel Growth — TradingView News (web) — https://www.tradingview.com/news/stockstory:e728a26a7094b:0-byrn-q3-deep-dive-retail-expansion-and-ai-driven-marketing-fuel-growth/
  - October 10, 2025 - Byrna’s results for Q3 were met with a strongly positive market reaction, as the company’s operational momentum was underpinned by rapid growth in both retail…
- **[S18]** BYRN Q1 Deep Dive: Retail Expansion and E-Commerce Challenges Shape Near-Term Outlook (web) — https://finance.yahoo.com/markets/stocks/articles/byrn-q1-deep-dive-retail-072644011.html
  - April 10, 2026 - Byrna’s first quarter saw sales climb year-over-year, but the company missed Wall Street’s revenue expectations and the market reacted sharply to the underperfo…
- **[S19]** Byrna Tech | Quantum Capital (web) — https://www.quantumcapitalresearch.com/byrn-call
  - In this post, we break down our swing trade alert on BYRN — from the entry price to profit target — and how our members walked away with a +23% return.
- **[S20]** Byrna Technologies, Inc. (BYRN) Stock Forecast: 1-Year Price Prediction & Outlook – Financhill (web) — https://financhill.com/stock-forecast/byrn-stock-prediction
  - 2 weeks ago - Byrna Technologies, Inc. (BYRN) stock is forecast up to $8.48 over the next 52 weeks. Financhill Stock Score: 10/100. Free AI-powered analysis and price prediction.
- **[S21]** BYRN Forecast, Price Target & Analyst Ratings | BYRNA TECHNOLOGIES INC (NASDAQ:BYRN) | ChartMill.com (web) — https://www.chartmill.com/stock/quote/BYRN/analyst-ratings
  - 11 analysts have analysed BYRN and the average price target is 14.23 USD. This implies a price increase of 184.58% is expected in the next year compared to the current price of …
- **[S22]** Byrna (BYRN) Research Report - StockStory (web) — https://stockstory.org/us/stocks/nasdaq/byrn
  - April 9, 2026 - Luckily, Byrna’s sales grew at an incredible 36.7% compounded annual growth rate over the last five years. Its growth beat the average industrials company and sh…
- **[S23]** BYRN - Byrna Technologies Stock Price - Barchart.com (web) — https://www.barchart.com/stocks/quotes/BYRN
  - Byrna Technologies Inc stocks price quote with latest real-time prices, charts, financials, latest news, technical analysis and opinions.
- **[S24]** BYRN Q3 Deep Dive: Retail Expansion and AI-Driven Marketing Fuel Growth — TradingView News (web_page) — https://www.tradingview.com/news/stockstory:e728a26a7094b:0-byrn-q3-deep-dive-retail-expansion-and-ai-driven-marketing-fuel-growth/
  - BYRN Q3 Deep Dive: Retail Expansion and AI-Driven Marketing Fuel Growth — TradingView News Search EN Get started BYRN Q3 Deep Dive: Retail Expansion and AI-Driven Marketing Fuel…
- **[S25]** BYRN Q1 Deep Dive: Retail Expansion and E-Commerce Challenges Shape Near-Term Outlook (web_page) — https://finance.yahoo.com/markets/stocks/articles/byrn-q1-deep-dive-retail-072644011.html
  - BYRN Q1 Deep Dive: Retail Expansion and E-Commerce Challenges Shape Near-Term Outlook Oops, something went wrong Skip to navigation Skip to main content Skip to right column Bre…
- **[S26]** BYRN 10-K (sec)
  - Item 1 chars=0, Item 1A chars=0, Item 7 chars=0, ok=False, source=edgartools
- **[S27]** BYRN 8-K 2026-07-09 (sec) — https://www.sec.gov/Archives/edgar/data/1354866/000143774926023101/byrn20260708_8k.htm
  - FORM 8-K
- **[S28]** BYRN 10-Q 2026-07-09 (sec) — https://www.sec.gov/Archives/edgar/data/1354866/000143774926023100/byrn20260531_10q.htm
  - FORM 10-Q
- **[S29]** BYRN 8-K 2026-07-08 (sec) — https://www.sec.gov/Archives/edgar/data/1354866/000143774926023029/byrn20260707_8k.htm
  - FORM 8-K
- **[S30]** BYRN 8-K 2026-06-18 (sec) — https://www.sec.gov/Archives/edgar/data/1354866/000143774926021142/byrn20260618c_8k.htm
  - FORM 8-K
- **[S31]** BYRN 8-K 2026-06-15 (sec) — https://www.sec.gov/Archives/edgar/data/1354866/000143774926020580/byrn20260612_8k.htm
  - FORM 8-K
- **[S32]** BYRN 8-K 2026-04-09 (sec) — https://www.sec.gov/Archives/edgar/data/1354866/000143774926011821/byrn20260408c_8k.htm
  - FORM 8-K
- **[S33]** BYRN 10-Q 2026-04-09 (sec) — https://www.sec.gov/Archives/edgar/data/1354866/000143774926011820/byrn20260228_10q.htm
  - FORM 10-Q
- **[S34]** BYRN 8-K 2026-04-08 (sec) — https://www.sec.gov/Archives/edgar/data/1354866/000143774926011756/byrn20260408_8k.htm
  - FORM 8-K
- **[S35]** Item 1 Business summary (nlp)
  - ### Item 1 — Business No Item 1 Business text extracted. 
- **[S36]** Item 1A summary (nlp)
  - ### Item 1A — Risk Factors No text extracted. 
- **[S37]** Item 7 summary (nlp)
  - ### Item 7 — MD&A No text extracted. 
- **[S38]** BYRN scenario price ranges (scenarios)
  - ok=True; base mid=3.7417760793070887; headwinds=4; tailwinds=8
- **[S39]** BYRN driver analysis (drivers)
  - ok=False; drivers=7
- **[S40]** BYRN memo sections (memo)
  - mode=rules; proxies=3

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
- Company: Byrna Technologies, Inc.
- Sector / industry: Industrials / Aerospace & Defense
- Price: 3.54
- 52-week range: $3.17 – $30.62
- Market cap: $80.33M
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
- FCF yield: -11.5%
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
![Revenue & FCF history](/charts/BYRN_valuation_revenue_fcf.png)

### DCF scenario prices
![DCF scenario prices](/charts/BYRN_valuation_dcf_scenarios.png)

### Base-case FCF path
![Base-case FCF path](/charts/BYRN_valuation_base_fcf_path.png)

### EV/EBITDA scenario prices
![EV/EBITDA scenario prices](/charts/BYRN_valuation_ev_ebitda_scenarios.png)

### Headwind/tailwind price ranges
![Headwind/tailwind price ranges](/charts/BYRN_valuation_scenario_ranges.png)

## DCF valuation (base / bull / bear) [S2]

> Simplified revenue->FCF DCF. Not investment advice; assumptions are editable heuristics.

- Spot price: $3.54
- Base revenue: $118.12M
- Shares: 22,693,356
- Net debt (Debt−Cash): -$11.38M

| Scenario | Growth | FCF margin | WACC | Term. g | Equity value | Share price | Upside |
|----------|--------|------------|------|---------|--------------|-------------|--------|
| bear | 25.0% | 1.0% | 12.0% | 1.5% | $39.46M | $1.74 | -50.9% |
| base | 35.0% | 3.0% | 10.0% | 2.5% | $180.36M | $7.95 | 124.5% |
| bull | 42.0% | 8.0% | 9.0% | 3.0% | $732.01M | $32.26 | 811.2% |

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

## Valuation — EV/EBITDA scenarios [S3]

> Priced-in model: implied price = (EBITDA × EV/EBITDA − net debt) ÷ shares. Not a forecast.

- Spot: $3.54
- Net debt used: -$11.38M

| Scenario | EBITDA | EV/EBITDA | Implied EV | Equity value | Implied price |
|---|---:|---:|---:|---:|---:|
| bear | $9.77M | 3.7x | $35.74M | $47.13M | $2.08 |
| base | $13.95M | 4.9x | $68.09M | $79.47M | $3.50 |
| bull | $16.74M | 6.1x | $102.13M | $113.51M | $5.00 |

- Base EBITDA seeded from latest reported/TTM figure (13,953,000).
- Base multiple seeded from current EV/EBITDA (4.9x).

## Scenario price ranges (headwinds & tailwinds) [S29]

> Medium-term (18–36 months (medium / medium-long term)) driver → EV/EBITDA bridge. Distinct from the FCF DCF path. Not investment advice.

- Spot: $3.54
- Sparse Street mean target: $6.83
- Anchor multiple: 4.9x (driver_ev_ebitda_bridge)
- Anchor EBITDA: $13.95M
- Probability-weighted midpoint: **$4.21** (heuristic weights, not a rating)
- Driver extraction: `rules`

### Headwinds (bear-case fuel)

- **Negative free cash flow** — Latest FCF -$9.20M — cash burn raises financing risk _(source: fundamentals)_
- **Balance-sheet / refinancing pressure** — sector=Industrials industry=Aerospace & Defense revenue=118120000.0 ebitda=13953000.0 fcf=-9201000.0 net_debt=-11381000.0 nd_ebitda=-0.8156668816741919 target=6.83333 rec=buy _(source: fundamentals)_

### Tailwinds (bull-case fuel)

- **Manageable leverage** — Net debt / EBITDA ≈ -0.8x — room for reinvestment or returns _(source: fundamentals)_
- **Revenue growth momentum** — Latest revenue YoY ≈ 37.7% _(source: fundamentals)_
- **Street target implies upside** — Mean target $6.83 vs spot $3.54 _(source: fundamentals)_
- **Multiple re-rating / Street upgrades** — BYRNA TECHNOLOGIES INC(NASDAQ:BYRN) stock Analyst Ratings Analyst ratings, forecast, price target, upgrades and downgrades.The consensus rating for BYRNA TECHNOLOGIES INC (BYRN) is _(source: web)_
- **Growth / execution upside** — Byrna Technologies (BYRN) Stock Price & OverviewByrna Technologies (BYRN) Stock Forecast & Analyst Price TargetsByrna Technologies (BYRN) Stock Price, News & AnalysisDoes Byrna Tec _(source: web)_
- **Contract / backlog wins** — Byrna Technologies (BYRN) Stock Price & OverviewByrna Technologies (BYRN) Stock Forecast & Analyst Price TargetsByrna Technologies (BYRN) Stock Price, News & AnalysisDoes Byrna Tec _(source: web)_
- **Product / pricing power** — Byrna Technologies (BYRN) Stock Price & OverviewByrna Technologies (BYRN) Stock Forecast & Analyst Price TargetsByrna Technologies (BYRN) Stock Price, News & AnalysisDoes Byrna Tec _(source: web)_
- **Capital returns / FCF inflection** — Boeing Co (BA) vs Byrna Technologies Inc (BYRN): Price... | Pluang BA. BYRN. Market Cap.Invest & Trade with #1 Award-Winning Investment Super App. Compare Boeing Co vs Byrna Techno _(source: web)_

### Price ranges by case

| Case | Prob. | Metric vs TTM | Multiple | Price low | Mid | High | Upside vs spot |
|---|---:|---:|---:|---:|---:|---:|---:|
| bear | 0.17 | 0.78x | 3.4x | $1.98 | $2.14 | $2.30 | -40% |
| base | 0.38 | 1.08x | 4.9x | $3.51 | $3.74 | $3.97 | +6% |
| bull | 0.45 | 1.25x | 6.3x | $4.89 | $5.38 | $5.86 | +52% |

#### Bear — headwinds dominate

Headwinds bite: weaker operating trajectory and multiple compression. Equity duration shrinks if cash generation fails to offset leverage / competitive pressure.

- **Range:** $1.98 – $2.30 (mid $2.14) · EBITDA $10.88M · multiple 3.4x
- Driver: **Negative free cash flow** — Latest FCF -$9.20M — cash burn raises financing risk
- Driver: **Balance-sheet / refinancing pressure** — sector=Industrials industry=Aerospace & Defense revenue=118120000.0 ebitda=13953000.0 fcf=-9201000.0 net_debt=-11381000.0 nd_ebitda=-0.8156668816741919 target=6

#### Base — mixed execution

Balanced path: some tailwinds offset headwinds. Operating scale roughly holds with modest repair/normalization; valuation stays near the current EV/EBITDA anchor.

- **Range:** $3.51 – $3.97 (mid $3.74) · EBITDA $15.07M · multiple 4.9x
- Driver: **Manageable leverage** — Net debt / EBITDA ≈ -0.8x — room for reinvestment or returns
- Driver: **Revenue growth momentum** — Latest revenue YoY ≈ 37.7%
- Driver: **Negative free cash flow** — Latest FCF -$9.20M — cash burn raises financing risk
- Driver: **Balance-sheet / refinancing pressure** — sector=Industrials industry=Aerospace & Defense revenue=118120000.0 ebitda=13953000.0 fcf=-9201000.0 net_debt=-11381000.0 nd_ebitda=-0.8156668816741919 target=6

#### Bull — tailwinds dominate

Tailwinds compound: operating improvement plus a re-rating toward peer or recovery multiples as balance-sheet and growth narratives improve.

- **Range:** $4.89 – $5.86 (mid $5.38) · EBITDA $17.44M · multiple 6.3x
- Driver: **Manageable leverage** — Net debt / EBITDA ≈ -0.8x — room for reinvestment or returns
- Driver: **Revenue growth momentum** — Latest revenue YoY ≈ 37.7%
- Driver: **Street target implies upside** — Mean target $6.83 vs spot $3.54
- Driver: **Multiple re-rating / Street upgrades** — BYRNA TECHNOLOGIES INC(NASDAQ:BYRN) stock Analyst Ratings Analyst ratings, forecast, price target, upgrades and downgrades.The consensus rating for BYRNA TECHNO
- Driver: **Growth / execution upside** — Byrna Technologies (BYRN) Stock Price & OverviewByrna Technologies (BYRN) Stock Forecast & Analyst Price TargetsByrna Technologies (BYRN) Stock Price, News & An

### Method notes

- Item 1A risks weighted toward headwinds.
- Mapping follows Gemini/Perplexity-style scenario memos: qualitative drivers → operating metric & multiple paths → share-price ranges over a medium-term horizon.

## Web research — web_analysts

- Queries: BYRN analyst price target, Byrna Technologies, Inc. stock rating OR consensus OR upgrade OR downgrade, BYRN Estimate intrinsic value under base / bull / bear scenarios analyst
- Unique hits: 15
- Pages fetched: 2/3

### Web synthesis — web_analysts (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, guidance, revenue, margin, service, market

- | Asianet Newsable on MSN | https://www.msn.com/en-in/money/markets/why-did-stla-mat-byrn-stocks-tumble-to-52-week-lows-today/ar-AA27BZfD?ocid=BingNewsVerp Stellantis, Mattel, and Byrna Technologies tumbled to fresh lows on Thursday amid regional weaknesses, poor outlook, and Wall Street caution.
- [HIT] What To Expect From Byrna Technologies Inc (BYRN) Q2 2026 Earnings | Yahoo Finance | https://finance.yahoo.com/markets/stocks/articles/expect-byrna-technologies-inc-byrn-131713208.html At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage rates that help you manage your financial life.
- [HIT] Byrna Technologies (BYRN) Stock Forecast and Price Target 2026 | www.marketbeat.com | https://www.marketbeat.com/stocks/NASDAQ/BYRN/forecast/ Byrna Technologies - Analysts' Recommendations and Stock Price Forecast (2026).
- How MarketBeat Calculates Price Target and Consensus Rating.Has Byrna Technologies been upgraded or downgraded by Wall Street analysts recently?
- Compared to the current market price of 3.54 USD, the stock is Undervalued by 79%.
- [HIT] QS: Valuation Exercise - Bear Case - Risk Premium: Research | riskpremiumresearch.substack.com | https://riskpremiumresearch.substack.com/p/qs-valuation-exercise-bear-case Feb 26, 2025 ...
- where V0 is the investor's current estimate of intrinsic value and P0 is the current observable market price.
- [PAGE] Byrna Technologies Analyst Ratings and Price Targets | NASDAQ:BYRN | Benzinga | https://www.benzinga.com/quote/BYRN/analyst-ratings Byrna Technologies Analyst Ratings and Price Targets | NASDAQ:BYRN | Benzinga Benzinga España Italia 대한민국 日本 Français My Account Login SPY 738.31 0.08% QQQ 684.64 0.06% BTC/USD 64088.48 1.48% DIA 518.36 0.08% GLD 371.73 0.05% TLT 83.30 0.06% Get Benzinga Pro Data & APIs Events Premarket Advertise Contribute España Italia 대한민국 日本 Français Login Register Benzinga Premium Services Benzinga Edge Benzinga Pro Benzinga Research Benzinga APIs Financial News Financial News Large Cap Stocks Small-Cap Stocks Insider Trades Earnings Technology AI News Personal Finance ETF News Crypto News Dividend News Latest Rumors Latest Offerings News Investment Ideas Investment Ideas Stock of the Day Stock Whisper Index Analyst Ratings Analyst Color Financial Advisors Government Trades Trading Ideas Stock Screener Markets Markets Premarket Movers After Hours Options ETFs Commodities Prediction Markets Private Markets Bonds Futures Forex Top Stocks Top Stocks Apple (AAPL) Tesla (TSLA) Amazon (AMZN) Nvidia (NVDA) Alphabet (GOOGL) Meta Platforms (META) Microsoft (MSFT) StreetTracks Gold Shares (GLD) IBIT Bitcoin Trust (IBIT) Top Value Stocks Top Momentum Stocks Top Growth Stocks Top Quality Stocks Learn Learn Investing Guides Personal Finance Mortgages Best Credit Cards Best Dividend Stocks Best Swing Trade Stocks Investment Ideas Investment Ideas Stock of the Day Stock Whisper Index Analyst Ratings Analyst Color Financial Advisors Government Trades Trading Ideas Stock Screener Markets Markets Premarket Movers After Hours Options ETFs Commodities Prediction Markets Private Markets Bonds Futures Forex Top Stocks Top Stocks Apple (AAPL) Tesla (TSLA) Amazon (AMZN) Nvidia (NVDA) Alphabet (GOOGL) Meta Platforms (META) Microsoft (MSFT) StreetTracks Gold Shares (GLD) IBIT Bitcoin Trust (IBIT) Top Value Stocks Top Momentum Stocks Top Growth Stocks Top Quality Stocks Learn Learn Investing Guides Personal Finance Mortgages Best Credit Cards Best Dividend Stocks Best Swing Trade Stocks Research My Stocks Tools Free Benzinga Pro Trial Calendars Analyst Ratings Calendar Conference Call Calendar Dividend Calendar Earnings Calendar Economic Calendar Events Calendar FDA Calendar Guidance Calendar IPO Calendar M&A Calendar Unusual Options Activity Calendar SPAC Calendar Stock Split Calendar Trade Ideas Stock Reports Insider Trades Trade Idea Feed Analyst Ratings Unusual Options Activity Heatmaps Free Newsletter Government Trades Perfect Stock Portfolio Easy Income Portfolio Short Interest Most Shorted Largest Increase Largest Decrease Calculators Options Profit Calculator Margin Calculator Forex Profit Calculator 100x Options Profit Calculator Covered Call Calculator Cash-Secured Put Calculator Long Call Calculator Long Put Calculator Screeners Stock Screener Top Momentum Stocks Top Quality Stocks Top Value Stocks Top Growth Stocks Compare Best Stocks Best Momentum Stocks Best Quality Stocks Best Value Stocks Best Growth Stocks Markets SPY 738.31 0.08% QQQ 684.64 0.06% BTC/USD 64088.48 1.48% DIA 518.36 0.08% GLD 371.73 0.05% TLT 83.30 0.06% Byrna Technologies Inc Analyst Ratings BYRN NASDAQ Watchlist Get Report Trade with Public Get Report Trade with Public $3.54 0.17 5.04% At close: Jul 24, 5:00 PM EST $3.63 0.09 2.54% After Hours: 4:00 PM EST Get Report Overview News Earnings Events Options Guidance Analyst Ratings Insider Trades Short Interest Stock Report Consensus Rating 1 Buy Highest Price Target 1 $36.00 Lowest Price Target 1 $12.00 Consensus Price Target 1 $21.95 Byrna Te  [PAGE] BYRN Forecast — Price Target — Prediction for 2027 — TradingView | https://www.tradingview.com/symbols/NASDAQ-BYRN/forecast/ BYRN Forecast — Price Target — Prediction for 2027 — TradingView Search EN Get started Byrna Technologies, Inc.

### Sources found
- [Byrna Technologies Inc Us (BYRN) Stock Forecast, Price Targets and...](https://www.tipranks.com/stocks/byrn/forecast)
  - Analyze Forecast. Average Price Target.The average price target for Byrna Technologies Inc Us is 8.25. This is based on 2 Wall Streets Analysts 12-month pric…
- [Byrna Technologies Analyst Ratings and Price Targets | Benzinga](https://www.benzinga.com/quote/BYRN/analyst-ratings)
  - The analyst firm set a price target for $31.00 expecting BYRN to rise to within 12 months (a possible 233.33% upside). 6 analyst firms have reported ratings …
- [BYRN Forecast — Price Target — Prediction for 2027 — TradingView](https://www.tradingview.com/symbols/NASDAQ-BYRN/forecast/)
  - Price target. 29.000.000.00%. The 5 analysts offering 1-year price forecasts have a max estimate of — and a min estimate of —. Analyst rating. Based on 5 ana…
- [Byrna Technologies Inc. (BYRN) Analyst Insights, Price Targets...](https://finance.yahoo.com/quote/BYRN/analyst-insights/)
  - Analyst Price Targets. 7.50. 13.67 Average.Rating Buy. Price Action Lowers. Price Target 31 -> 21.
- [Why Byrna Technologies Inc.’s (BYRN) Stock Is Up 10.39%](https://www.aaii.com/investingideas/article/518457-why-byrna-technologies-inc8217s-byrn-stock-is-up-1039)
  - As of Friday, July 24, Byrna Technologies Inc.’s BYRN share price has surged by 10.39%, which has investors questioning if ...
- [Why did STLA, MAT, BYRN stocks tumble to 52-week lows today?](https://www.msn.com/en-in/money/markets/why-did-stla-mat-byrn-stocks-tumble-to-52-week-lows-today/ar-AA27BZfD?ocid=BingNewsVerp)
  - Stellantis, Mattel, and Byrna Technologies tumbled to fresh lows on Thursday amid regional weaknesses, poor outlook, and Wall Street caution.
- [What To Expect From Byrna Technologies Inc (BYRN) Q2 2026 Earnings](https://finance.yahoo.com/markets/stocks/articles/expect-byrna-technologies-inc-byrn-131713208.html)
  - At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage rate…
- [BYRNA TECHNOLOGIES INC(NASDAQ:BYRN) stock Analyst Ratings](https://www.chartmill.com/stock/quote/BYRN/analyst-ratings)
  - Analyst ratings, forecast, price target, upgrades and downgrades.The consensus rating for BYRNA TECHNOLOGIES INC (BYRN) is 83.6364 / 100 .
- [Byrna Technologies (BYRN) Stock Price & Overview](https://stockanalysis.com/stocks/byrn/)
  - A detailed overview of Byrna Technologies Inc. (BYRN) stock, including real-time price, chart, key statistics, news, and more.
- [Byrna Technologies (BYRN) Stock Forecast and Price Target 2026](https://www.marketbeat.com/stocks/NASDAQ/BYRN/forecast/)
  - Byrna Technologies - Analysts' Recommendations and Stock Price Forecast (2026). How MarketBeat Calculates Price Target and Consensus Rating.Has Byrna Technol…
- [BYRN Stock Price - Byrna Technologies Inc Stock... - StockScan](https://stockscan.io/stocks/BYRN)
  - Byrna Technologies Inc Stock (BYRN) Upgrades & Downgrades. Date. Action. Analyst. Rating Change. Apr-10-26. Downgrade. Craig Hallum. Buy → Hold.
- [BYRN DCF Valuation - Byrna Technologies Inc - Alpha Spread](https://www.alphaspread.com/security/nasdaq/byrn/dcf-valuation)
  - Estimated DCF Value of one BYRN stock is 16.6 USD. Compared to the current market price of 3.54 USD, the stock is Undervalued by 79%. DCF Valuation FAQ:.

### Search warnings
- news:Byrna Technologies, Inc. stock rating OR consensus OR upgrade OR downgrade: No results found.
- news:BYRN Estimate intrinsic value under base / bull / bear scenarios analyst: No results found.

## Web research — web_drivers

- Queries: BYRN Estimate intrinsic value under base / bull / bear scenarios, Byrna Technologies, Inc. BYRN outlook OR catalyst OR commodity OR uranium OR rare earth OR vanadium, BYRN sector drivers OR market demand
- Unique hits: 12
- Pages fetched: 3/3

### Web synthesis — web_drivers (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, uncertainty, revenue, margin, product, market

- | www.edwyn.app | https://www.edwyn.app/intrinsic-value-calculator Estimate intrinsic value for public companies with filing-backed inputs, bear/base/bull valuation ranges, and margin-of-safety context.
- Stock Quote (U.S ...Byrna Technologies Reports Record Results for Fiscal Fourth ...Byrna Technologies (BYRN) Stock Price & OverviewByrna Technologies (BYRN) Stock Forecast & Analyst Price TargetsByrna Technologies (BYRN) Stock Price, News & AnalysisDoes Byrna Technologies' (BYRN) New CEO and Revenue Outlook ...
- | www.marketwatch.com | https://www.marketwatch.com/investing/stock/byrn 20 hours ago · BYRN | Complete Byrna Technologies Inc.
- Feb 7, 2025 · Full-Year 2024 Revenues Reach $85.8 Million, Up More Than 100% From 2023, Net Income for the Year of $12.8 million is Up $21.0 Million from Prior Year ANDOVER, Mass., Feb.
- (BYRN) stock, with detailed revenue and earnings estimates.
- Get The Latest BYRN Stock Analysis, Price Target, Earnings Estimates, Headlines, and Short Interest at MarketBeat.
- Byrna CEO Conn Davis stated: “Byrna has important strengths already in place, including a differentiated product offering, a strong balance sheet, a domest...
- Fundamental and historical data is provided by S&P Global Market Intelligence.

### Sources found
- [BYRN Fair Value 2026 — 13 Valuation Models | CirclFi](https://circlfi.com/stock/BYRN/)
  - Based on CirclFi's 13-model analysis, Byrna Technologies, Inc. (BYRN) has multiple fair value estimates. The Bayesian DCF model runs 10,000 Monte Carlo simul…
- [Intrinsik — Stock Valuation Tool | Fair Value in 60 Seconds](https://intrinsik.io/)
  - Fair value. Any stock. 60 seconds. Enter a ticker. Intrinsik reads the SEC filings, builds a full DCF model with bear, base & bull scenarios, and delivers in…
- [Intrinsic Value Calculator - Basis Report](https://www.basisreport.com/tools/intrinsic-value-calculator)
  - Calculate intrinsic value for any stock using Graham Number, DCF, and P/E methods. Now with Bull/Base/Bear scenario panel to stress-test your assumptions. Fr…
- [Intrinsic Value Calculator | Filing-Backed DCF Tool For Public Stocks ...](https://www.edwyn.app/intrinsic-value-calculator)
  - Estimate intrinsic value for public companies with filing-backed inputs, bear/base/bull valuation ranges, and margin-of-safety context.
- [Byrna Technologies Inc. (BYRN) Stock Price, News, Quote ...](https://finance.yahoo.com/quote/BYRN/?fr=sycsrp_catchall)
  - Find the latest Byrna Technologies Inc. (BYRN) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [BYRN Stock Price | Byrna Technologies Inc. Stock Quote (U.S ...Byrna Technologies Reports Record Results for Fiscal Fourth ...Byrna Technologies (BYRN) Stock Price & OverviewByrna Technologies (BYRN) Stock Forecast & Analyst Price TargetsByrna Technologies (BYRN) Stock Price, News & AnalysisDoes Byrna Technologies' (BYRN) New CEO and Revenue Outlook ...](https://www.marketwatch.com/investing/stock/byrn)
  - 20 hours ago · BYRN | Complete Byrna Technologies Inc. stock news by MarketWatch. View real-time stock prices and stock quotes for a full financial overview.…
- [Byrna Technologies Reports Record Results for Fiscal Fourth ...](https://ir.byrna.com/news-events/press-releases/detail/215/byrna-technologies-reports-record-results-for-fiscal-fourth)
  - Feb 7, 2025 · Full-Year 2024 Revenues Reach $85.8 Million, Up More Than 100% From 2023, Net Income for the Year of $12.8 million is Up $21.0 Million from Pri…
- [Byrna Technologies (BYRN) Stock Price & OverviewByrna Technologies (BYRN) Stock Forecast & Analyst Price TargetsByrna Technologies (BYRN) Stock Price, News & AnalysisDoes Byrna Technologies' (BYRN) New CEO and Revenue Outlook ...](https://stockanalysis.com/stocks/byrn/)
  - 2 hours ago · A detailed overview of Byrna Technologies Inc. (BYRN) stock, including real-time price, chart, key statistics, news, and more. Stock forecasts …
- [Boeing Co (BA) vs Byrna Technologies Inc (BYRN): Price... | Pluang](https://pluang.com/en/compare/ba-vs-byrn)
  - BA. BYRN. Market Cap.Invest & Trade with #1 Award-Winning Investment Super App. Compare Boeing Co vs Byrna Technologies Inc stock side by side — market cap, …
- [Byrna Technologies Inc Free Cash Flow Growth Rates (BYRN)...](https://csimarket.com/stocks/single_growth_rates.php?code=BYRN&cfw)
  - BYRN's Free Cash Flow Growth by Quarter and Year.CSIMarket Company, Sector, Industry, Market Analysis, Stock Quotes, Earnings, Economy, News and Research.
- [Byrna Technologies (BYRN) | Trefis](https://www.trefis.com/data/companies/BYRN)
  - Byrna Technologies (BYRN). Market Price (11/15/2025): $17.29 Market Cap: $392.3 Mil Sector: Industrials Industry: Aerospace & Defense.
- [BYRN Stock Risk & Deep Value Analysis | DVR Score](https://deepvaluereports.com/stock/BYRN/)
  - Get BYRN stock risk analysis, financial health assessment, and deep value score. Independent research for informed decisions.

### Search warnings
- news:BYRN Estimate intrinsic value under base / bull / bear scenarios: No results found.
- news:Byrna Technologies, Inc. BYRN outlook OR catalyst OR commodity OR uranium OR rare earth OR vanadium: No results found.
- news:BYRN sector drivers OR market demand: No results found.

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


## Research loop (think → act)

1. _heuristic_ — Coverage looks adequate for this pass; stopping iterative loop.

## Sources

- **[S1]** BYRN fundamentals (yfinance)
  - Byrna Technologies, Inc.: price=3.54, rev=118120000.0, fcf=-9201000.0, shares=22693356.0, rev_cagr=0.3497464711860472, ROIC=0.2177063410328086, FCF yield=-0.11453363487259767
- **[S2]** BYRN DCF valuation (dcf)
  - Base share price=7.947753124041503, bull=32.256417371811665, bear=1.7389795505454393
- **[S3]** BYRN EV/EBITDA valuation (multiples)
  - Base implied price=3.5017565493618483, multiple=4.879639360710958
- **[S4]** Byrna Technologies Inc Us (BYRN) Stock Forecast, Price Targets and... (web) — https://www.tipranks.com/stocks/byrn/forecast
  - Analyze Forecast. Average Price Target.The average price target for Byrna Technologies Inc Us is 8.25. This is based on 2 Wall Streets Analysts 12-month price targets, issued in…
- **[S5]** Byrna Technologies Analyst Ratings and Price Targets | Benzinga (web) — https://www.benzinga.com/quote/BYRN/analyst-ratings
  - The analyst firm set a price target for $31.00 expecting BYRN to rise to within 12 months (a possible 233.33% upside). 6 analyst firms have reported ratings in the last year.
- **[S6]** BYRN Forecast — Price Target — Prediction for 2027 — TradingView (web) — https://www.tradingview.com/symbols/NASDAQ-BYRN/forecast/
  - Price target. 29.000.000.00%. The 5 analysts offering 1-year price forecasts have a max estimate of — and a min estimate of —. Analyst rating. Based on 5 analysts giving stock r…
- **[S7]** Byrna Technologies Inc. (BYRN) Analyst Insights, Price Targets... (web) — https://finance.yahoo.com/quote/BYRN/analyst-insights/
  - Analyst Price Targets. 7.50. 13.67 Average.Rating Buy. Price Action Lowers. Price Target 31 -> 21.
- **[S8]** Why Byrna Technologies Inc.’s (BYRN) Stock Is Up 10.39% (web) — https://www.aaii.com/investingideas/article/518457-why-byrna-technologies-inc8217s-byrn-stock-is-up-1039
  - As of Friday, July 24, Byrna Technologies Inc.’s BYRN share price has surged by 10.39%, which has investors questioning if ...
- **[S9]** Why did STLA, MAT, BYRN stocks tumble to 52-week lows today? (web) — https://www.msn.com/en-in/money/markets/why-did-stla-mat-byrn-stocks-tumble-to-52-week-lows-today/ar-AA27BZfD?ocid=BingNewsVerp
  - Stellantis, Mattel, and Byrna Technologies tumbled to fresh lows on Thursday amid regional weaknesses, poor outlook, and Wall Street caution.
- **[S10]** What To Expect From Byrna Technologies Inc (BYRN) Q2 2026 Earnings (web) — https://finance.yahoo.com/markets/stocks/articles/expect-byrna-technologies-inc-byrn-131713208.html
  - At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage rates that help you mana…
- **[S11]** BYRNA TECHNOLOGIES INC(NASDAQ:BYRN) stock Analyst Ratings (web) — https://www.chartmill.com/stock/quote/BYRN/analyst-ratings
  - Analyst ratings, forecast, price target, upgrades and downgrades.The consensus rating for BYRNA TECHNOLOGIES INC (BYRN) is 83.6364 / 100 .
- **[S12]** Byrna Technologies Analyst Ratings and Price Targets | NASDAQ:BYRN | Benzinga (web_page) — https://www.benzinga.com/quote/BYRN/analyst-ratings
  - Byrna Technologies Analyst Ratings and Price Targets | NASDAQ:BYRN | Benzinga Benzinga España Italia 대한민국 日本 Français My Account Login SPY 738.31 0.08% QQQ 684.64 0.06% BTC/USD …
- **[S13]** BYRN Forecast — Price Target — Prediction for 2027 — TradingView (web_page) — https://www.tradingview.com/symbols/NASDAQ-BYRN/forecast/
  - BYRN Forecast — Price Target — Prediction for 2027 — TradingView Search EN Get started Byrna Technologies, Inc. BYRN Nasdaq Stock Market BYRN Nasdaq Stock Market BYRN Nasdaq Sto…
- **[S14]** BYRN Fair Value 2026 — 13 Valuation Models | CirclFi (web) — https://circlfi.com/stock/BYRN/
  - Based on CirclFi's 13-model analysis, Byrna Technologies, Inc. (BYRN) has multiple fair value estimates. The Bayesian DCF model runs 10,000 Monte Carlo simulations with jump-dif…
- **[S15]** Intrinsik — Stock Valuation Tool | Fair Value in 60 Seconds (web) — https://intrinsik.io/
  - Fair value. Any stock. 60 seconds. Enter a ticker. Intrinsik reads the SEC filings, builds a full DCF model with bear, base & bull scenarios, and delivers intrinsic value — auto…
- **[S16]** Intrinsic Value Calculator - Basis Report (web) — https://www.basisreport.com/tools/intrinsic-value-calculator
  - Calculate intrinsic value for any stock using Graham Number, DCF, and P/E methods. Now with Bull/Base/Bear scenario panel to stress-test your assumptions. Free, no signup.
- **[S17]** Intrinsic Value Calculator | Filing-Backed DCF Tool For Public Stocks ... (web) — https://www.edwyn.app/intrinsic-value-calculator
  - Estimate intrinsic value for public companies with filing-backed inputs, bear/base/bull valuation ranges, and margin-of-safety context.
- **[S18]** Byrna Technologies Inc. (BYRN) Stock Price, News, Quote ... (web) — https://finance.yahoo.com/quote/BYRN/?fr=sycsrp_catchall
  - Find the latest Byrna Technologies Inc. (BYRN) stock quote, history, news and other vital information to help you with your stock trading and investing.
- **[S19]** BYRN Stock Price | Byrna Technologies Inc. Stock Quote (U.S ...Byrna Technologies Reports Record Results for Fiscal Fourth ...Byrna Technologies (BYRN) Stock Price & OverviewByrna Technologies (BYRN) Stock Forecast & Analyst Price TargetsByrna Technologies (BYRN) Stock Price, News & AnalysisDoes Byrna Technologies' (BYRN) New CEO and Revenue Outlook ... (web) — https://www.marketwatch.com/investing/stock/byrn
  - 20 hours ago · BYRN | Complete Byrna Technologies Inc. stock news by MarketWatch. View real-time stock prices and stock quotes for a full financial overview. Feb 7, 2025 · Full-…
- **[S20]** Byrna Technologies Reports Record Results for Fiscal Fourth ... (web) — https://ir.byrna.com/news-events/press-releases/detail/215/byrna-technologies-reports-record-results-for-fiscal-fourth
  - Feb 7, 2025 · Full-Year 2024 Revenues Reach $85.8 Million, Up More Than 100% From 2023, Net Income for the Year of $12.8 million is Up $21.0 Million from Prior Year ANDOVER, Mas…
- **[S21]** Byrna Technologies (BYRN) Stock Price & OverviewByrna Technologies (BYRN) Stock Forecast & Analyst Price TargetsByrna Technologies (BYRN) Stock Price, News & AnalysisDoes Byrna Technologies' (BYRN) New CEO and Revenue Outlook ... (web) — https://stockanalysis.com/stocks/byrn/
  - 2 hours ago · A detailed overview of Byrna Technologies Inc. (BYRN) stock, including real-time price, chart, key statistics, news, and more. Stock forecasts and analyst price ta…
- **[S22]** BYRN Fair Value 2026 — 13 Valuation Models | CirclFi (web_page) — https://circlfi.com/stock/BYRN/
  - BYRN Fair Value 2026 — 13 Valuation Models | CirclFi Skip to main content Byrna Technologies, Inc. (BYRN) Fair Value 2026 BYRN · Aerospace & Defense · 2026-07-23 By CirclFi Rese…
- **[S23]** Intrinsik — Free Stock Valuation Tool | DCF Analysis & Fair Value Calculator (web_page) — https://intrinsik.io/
  - Intrinsik — Free Stock Valuation Tool | DCF Analysis & Fair Value Calculator
- **[S24]** Intrinsic Value Calculator | Basis Report (web_page) — https://www.basisreport.com/tools/intrinsic-value-calculator
  - Intrinsic Value Calculator | Basis Report Tools › Intrinsic Value Calculator Free tool · No signup · 3 valuation methods Intrinsic Value Calculator Calculate any stock's intrins…
- **[S25]** BYRN 10-K (sec)
  - Item 1 chars=0, Item 1A chars=0, Item 7 chars=0, ok=False, source=cache
- **[S26]** Item 1 Business summary (nlp)
  - ### Item 1 — Business No Item 1 Business text extracted. 
- **[S27]** Item 1A summary (nlp)
  - ### Item 1A — Risk Factors No text extracted. 
- **[S28]** Item 7 summary (nlp)
  - ### Item 7 — MD&A No text extracted. 
- **[S29]** BYRN scenario price ranges (scenarios)
  - ok=True; base mid=3.7417760793070887; headwinds=2; tailwinds=8

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
- Price: 3.54
- 52-week range: $3.17 – $30.62
- Market cap: $80.33M
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
- FCF yield: -11.5%
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

- Spot price: $3.54
- Base revenue: $118.12M
- Shares: 22,693,356
- Net debt (Debt−Cash): -$11.38M

| Scenario | Growth | FCF margin | WACC | Term. g | Equity value | Share price | Upside |
|----------|--------|------------|------|---------|--------------|-------------|--------|
| bear | 25.0% | 1.0% | 12.0% | 1.5% | $39.46M | $1.74 | -50.9% |
| base | 35.0% | 3.0% | 10.0% | 2.5% | $180.36M | $7.95 | 124.5% |
| bull | 42.0% | 8.0% | 9.0% | 3.0% | $732.01M | $32.26 | 811.2% |

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
- Unique hits: 4
- Pages fetched: 2/3

### Web synthesis — web_research (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, litigation, revenue, margin, customer, product, market

- Connects to live market data via MCP servers to deliver company deep dives, due diligence reports, competitive landscape analysis, market sentiment, and DCF-based intrinsic value estimates — all from natural language prompts.
- For investors, these documents provide a detailed account of financial data, risks, and management's perspective, all essential for performing in-depth due diligence.
- You've been through preliminary Q&A sessions, shared high-level metrics, and convinced them on market and team.
- But now they want to see everything: your code architecture, financial models, legal structure, intellectual property, customer contracts, and every assumption that powers your business.
- Three diligence domains and their focus areas Technical diligence examines your product's foundation, scalability, and development practices.
- Financial diligence goes beyond basic metrics to examine unit economics modeling, cash flow forecasting, customer cohort analysis  [PAGE] GitHub - Lunatic16/deep-financial-research: A Claude/Qwen/Gemini skill for institutional-grade investment research.
- Connects to live market data via MCP servers to deliver company deep dives, due diligence reports, competitive landscape analysis, market sentiment, and DCF-based intrinsic value estimates — all from natural language prompts.
- Connects to live market data via MCP servers to deliver company deep dives, due diligence reports, competitive landscape analysis, market sentiment, and DCF-based intrinsic value estimates — all from natural language prompts.

### Sources found
- [PDF Checklist for DCF Valuation](https://pages.stern.nyu.edu/~adamodar/pdfiles/eqnotes/DCFtodolist.pdf)
  - Checklist for DCF Valuation Checklist for DCF Valuation
- [Deep Diligence Checklist for Startup Founders | Flux Capital Academy ...](https://www.fluxcapital.com/academy/boards-and-diligence/boards-and-diligence-deep-diligence-technical-financial-and-legal)
  - Deep diligence checklist for technical, financial, and legal review: prepare data rooms, models, IP, contracts, and investor Q&A for Series A.
- [GitHub - Lunatic16/deep-financial-research: A Claude/Qwen/Gemini skill ...](https://github.com/Lunatic16/deep-financial-research)
  - A Claude/Qwen/Gemini skill for institutional-grade investment research. Connects to live market data via MCP servers to deliver company deep dives, due dilig…
- [A Deep Dive Into Understanding 10K Reports - eFinancialModels](https://www.efinancialmodels.com/a-deep-dive-into-understanding-10k-reports/)
  - The importance of a 10K financial report cannot be overstated. For investors, these documents provide a detailed account of financial data, risks, and manage…

### Search warnings
- news:Deep diligence: fundamentals, DCF, web, 10-K risks & MD&A: No results found.

## Put opportunities (heuristic) [S3]
- Expiration: 2026-09-18 (DTE 56)
- Candidates: 0
- ATM IV (est.): 183.6%
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
  - Byrna Technologies, Inc.: price=3.54, rev=118120000.0, fcf=-9201000.0, shares=22693356.0, rev_cagr=0.3497464711860472, ROIC=0.2177063410328086, FCF yield=-0.11453363487259767
- **[S2]** BYRN DCF valuation (dcf)
  - Base share price=7.947753124041503, bull=32.256417371811665, bear=1.7389795505454393
- **[S3]** BYRN put screen (yfinance_options)
  - Expiration 2026-09-18 (DTE 56): 0 candidates; IV=1.8359383203124997, IV rank=None, HV rank=1.0. Delta band approximated via % OTM when greeks are unavailable; IV rank needs ~20+…
- **[S4]** PDF Checklist for DCF Valuation (web) — https://pages.stern.nyu.edu/~adamodar/pdfiles/eqnotes/DCFtodolist.pdf
  - Checklist for DCF Valuation Checklist for DCF Valuation
- **[S5]** Deep Diligence Checklist for Startup Founders | Flux Capital Academy ... (web) — https://www.fluxcapital.com/academy/boards-and-diligence/boards-and-diligence-deep-diligence-technical-financial-and-legal
  - Deep diligence checklist for technical, financial, and legal review: prepare data rooms, models, IP, contracts, and investor Q&A for Series A.
- **[S6]** GitHub - Lunatic16/deep-financial-research: A Claude/Qwen/Gemini skill ... (web) — https://github.com/Lunatic16/deep-financial-research
  - A Claude/Qwen/Gemini skill for institutional-grade investment research. Connects to live market data via MCP servers to deliver company deep dives, due diligence reports, compet…
- **[S7]** A Deep Dive Into Understanding 10K Reports - eFinancialModels (web) — https://www.efinancialmodels.com/a-deep-dive-into-understanding-10k-reports/
  - The importance of a 10K financial report cannot be overstated. For investors, these documents provide a detailed account of financial data, risks, and management's perspective, …
- **[S8]** Deep Diligence Checklist for Startup Founders | Flux Capital Academy | Flux Capital (web_page) — https://www.fluxcapital.com/academy/boards-and-diligence/boards-and-diligence-deep-diligence-technical-financial-and-legal
  - Deep Diligence Checklist for Startup Founders | Flux Capital Academy | Flux Capital Deep diligence: technical, financial, and legal Author Ari Stiegler Managing Partner, Flux Ca…
- **[S9]** GitHub - Lunatic16/deep-financial-research: A Claude/Qwen/Gemini skill for institutional-grade investment research. Connects to live market data via MCP servers to deliver company deep dives, due diligence reports, competitive landscape analysis, market sentiment, and DCF-based intrinsic value estimates — all from natural language prompts. · GitHub (web_page) — https://github.com/Lunatic16/deep-financial-research
  - GitHub - Lunatic16/deep-financial-research: A Claude/Qwen/Gemini skill for institutional-grade investment research. Connects to live market data via MCP servers to deliver compa…
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
- Price: 3.54
- 52-week range: $3.17 – $30.62
- Market cap: $80.33M
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
- FCF yield: -11.5%
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
- Unique hits: 16
- Pages fetched: 1/3

### Web synthesis — web_research (rule-based fallback — Ollama unavailable)
**Keyword hits:** revenue, margin, product, market

- | www.marketbeat.com | https://www.marketbeat.com/stocks/NASDAQ/BYRN/news/ What's going on at Byrna Technologies (NASDAQ:BYRN)?
- Read today's BYRN news from trusted media outlets at MarketBeat.
- (BYRN) | ir.byrna.com | https://ir.byrna.com/news-events/press-releases Byrna Technologies Realigns Sales and Marketing Function to Strengthen Brand Messaging and Accelerate Retail Expansion; Appoints HLK as Agency of Record  [HIT] Pre-Q4 Earnings: Should Byrna Stock be in Your Portfolio?
- [HIT] BYRN Q2 Deep Dive: Market Skepticism Amid Channel Expansion and Product Launches | StockStory · via Yahoo Finance | https://finance.yahoo.com/news/byrn-q2-deep-dive-market-054117905.html Non-lethal weapons company Byrna (NASDAQ:BYRN) met Wall Street’s revenue expectations in Q2 CY2025, ...
- [HIT] Why Byrna (BYRN) Shares Are Sliding Today | StockStory · via Yahoo Finance | https://finance.yahoo.com/markets/stocks/articles/why-byrna-byrn-shares-sliding-201134994.html Shares of non-lethal weapons company Byrna (NASDAQ:BYRN) fell 4.1% in the afternoon session after the company announced the appointment of James White as...
- (BYRN) | ir.byrna.com | https://ir.byrna.com/financial-information/financial-results May 31, 2026 · Fiscal Year Ended Nov 30, 2024 Earnings Release  [HIT] BYRN Q2 2025 Earnings Report on 7/10/2025 - MarketBeat | www.marketbeat.com | https://www.marketbeat.com/earnings/reports/2025-7-10-byrna-technologies-inc-stock/ Jul 10, 2025 · Byrna Technologies announced their Q2 2025 earnings on 7/10/2025.
- View BYRN's earnings results, press release, and conference call transcript at MarketBeat.
- [HIT] Byrna Technologies (BYRN) Earnings Date and Reports 2026 | www.marketbeat.com | https://www.marketbeat.com/stocks/NASDAQ/BYRN/earnings/ Jul 17, 2026 · When is Byrna Technologies' next earnings announcement?

### Sources found
- [Byron Nelson](https://en.wikipedia.org/wiki/Byron_Nelson)
  - John Byron Nelson Jr. (February 4, 1912 – September 26, 2006) was an American professional golfer between 1935 and 1946, widely considered one of the greates…
- [BYRN News Today | Why did Byrna Technologies stock go up today?](https://www.marketbeat.com/stocks/NASDAQ/BYRN/news/)
  - What's going on at Byrna Technologies (NASDAQ:BYRN)? Read today's BYRN news from trusted media outlets at MarketBeat.
- [Byrna Technologies Inc. (BYRN) Latest Stock News & Headlines - Yahoo ...](https://finance.yahoo.com/quote/BYRN/news/)
  - Get the latest Byrna Technologies Inc. (BYRN) stock news and headlines to help you in your trading and investing decisions.
- [Press Releases :: Byrna Technologies Inc. (BYRN)](https://ir.byrna.com/news-events/press-releases)
  - Byrna Technologies Realigns Sales and Marketing Function to Strengthen Brand Messaging and Accelerate Retail Expansion; Appoints HLK as Agency of Record
- [Pre-Q4 Earnings: Should Byrna Stock be in Your Portfolio?](https://finance.yahoo.com/news/pre-q4-earnings-byrna-stock-170700220.html)
  - Byrna Technologies Inc. BYRN is set to report its fourth-quarter fiscal 2024 results on Feb. 7,...
- [BYRN Q2 Deep Dive: Market Skepticism Amid Channel Expansion and Product Launches](https://finance.yahoo.com/news/byrn-q2-deep-dive-market-054117905.html)
  - Non-lethal weapons company Byrna (NASDAQ:BYRN) met Wall Street’s revenue expectations in Q2 CY2025, ...
- [Here Is What You Need To Know Before Investing In Byrna Technologies Inc. (BYRN)](https://finance.yahoo.com/news/know-investing-byrna-technologies-inc-115559141.html)
  - Byrna Technologies Inc. (NASDAQ:BYRN) is among the 10 Best Small Cap Defense Stocks to Buy According...
- [Why Byrna (BYRN) Shares Are Sliding Today](https://finance.yahoo.com/markets/stocks/articles/why-byrna-byrn-shares-sliding-201134994.html)
  - Shares of non-lethal weapons company Byrna (NASDAQ:BYRN) fell 4.1% in the afternoon session after the company announced the appointment of James White as...
- [Investor Relations :: Byrna Technologies Inc. (BYRN)](https://ir.byrna.com/)
  - Jul 8, 2026 · Byrna Technologies Inc. (NASDAQ: BYRN) is a technology company specializing in the areas of Personal Security Devices, Military, Law Enforcemen…
- [Financial Results :: Byrna Technologies Inc. (BYRN)](https://ir.byrna.com/financial-information/financial-results)
  - May 31, 2026 · Fiscal Year Ended Nov 30, 2024 Earnings Release
- [BYRN Q2 2025 Earnings Report on 7/10/2025 - MarketBeat](https://www.marketbeat.com/earnings/reports/2025-7-10-byrna-technologies-inc-stock/)
  - Jul 10, 2025 · Byrna Technologies announced their Q2 2025 earnings on 7/10/2025. View BYRN's earnings results, press release, and conference call transcript …
- [Byrna Technologies (BYRN) Earnings Date and Reports 2026](https://www.marketbeat.com/stocks/NASDAQ/BYRN/earnings/)
  - Jul 17, 2026 · When is Byrna Technologies' next earnings announcement? View the latest BYRN earnings date, analysts forecasts, earnings history, and conferen…

## Put opportunities (heuristic) [S2]
- Expiration: 2026-09-18 (DTE 56)
- Candidates: 0
- ATM IV (est.): 183.6%
- IV rank: — (1 local samples)
- HV rank (20d realized): 100.0%


_Note: Delta band approximated via % OTM when greeks are unavailable; IV rank needs ~20+ local daily IV samples (have 1); run the options screen over time to build history.; HV rank is realized-vol rank (20d HV vs ~1y); useful when IV history is thin._

## Research loop (think → act)

1. _heuristic_ — Coverage looks adequate for this pass; stopping iterative loop.

## Sources

- **[S1]** BYRN fundamentals (yfinance)
  - Byrna Technologies, Inc.: price=3.54, rev=118120000.0, fcf=-9201000.0, shares=22693356.0, rev_cagr=0.3497464711860472, ROIC=0.2177063410328086, FCF yield=-0.11453363487259767
- **[S2]** BYRN put screen (yfinance_options)
  - Expiration 2026-09-18 (DTE 56): 0 candidates; IV=1.8359383203124997, IV rank=None, HV rank=1.0. Delta band approximated via % OTM when greeks are unavailable; IV rank needs ~20+…
- **[S3]** Byron Nelson (web) — https://en.wikipedia.org/wiki/Byron_Nelson
  - John Byron Nelson Jr. (February 4, 1912 – September 26, 2006) was an American professional golfer between 1935 and 1946, widely considered one of the greatest golfers of all tim…
- **[S4]** BYRN News Today | Why did Byrna Technologies stock go up today? (web) — https://www.marketbeat.com/stocks/NASDAQ/BYRN/news/
  - What's going on at Byrna Technologies (NASDAQ:BYRN)? Read today's BYRN news from trusted media outlets at MarketBeat.
- **[S5]** Byrna Technologies Inc. (BYRN) Latest Stock News & Headlines - Yahoo ... (web) — https://finance.yahoo.com/quote/BYRN/news/
  - Get the latest Byrna Technologies Inc. (BYRN) stock news and headlines to help you in your trading and investing decisions.
- **[S6]** Press Releases :: Byrna Technologies Inc. (BYRN) (web) — https://ir.byrna.com/news-events/press-releases
  - Byrna Technologies Realigns Sales and Marketing Function to Strengthen Brand Messaging and Accelerate Retail Expansion; Appoints HLK as Agency of Record
- **[S7]** Pre-Q4 Earnings: Should Byrna Stock be in Your Portfolio? (web) — https://finance.yahoo.com/news/pre-q4-earnings-byrna-stock-170700220.html
  - Byrna Technologies Inc. BYRN is set to report its fourth-quarter fiscal 2024 results on Feb. 7,...
- **[S8]** BYRN Q2 Deep Dive: Market Skepticism Amid Channel Expansion and Product Launches (web) — https://finance.yahoo.com/news/byrn-q2-deep-dive-market-054117905.html
  - Non-lethal weapons company Byrna (NASDAQ:BYRN) met Wall Street’s revenue expectations in Q2 CY2025, ...
- **[S9]** Here Is What You Need To Know Before Investing In Byrna Technologies Inc. (BYRN) (web) — https://finance.yahoo.com/news/know-investing-byrna-technologies-inc-115559141.html
  - Byrna Technologies Inc. (NASDAQ:BYRN) is among the 10 Best Small Cap Defense Stocks to Buy According...
- **[S10]** Why Byrna (BYRN) Shares Are Sliding Today (web) — https://finance.yahoo.com/markets/stocks/articles/why-byrna-byrn-shares-sliding-201134994.html
  - Shares of non-lethal weapons company Byrna (NASDAQ:BYRN) fell 4.1% in the afternoon session after the company announced the appointment of James White as...
- **[S11]** BYRN News Today | Why did Byrna Technologies stock go up today? (web_page) — https://www.marketbeat.com/stocks/NASDAQ/BYRN/news/
  - BYRN News Today | Why did Byrna Technologies stock go up today? Skip to main content → Here’s the stock symbol I’ve promised (From Stansberry Research) (Ad) Free BYRN Stock Aler…

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
- Price: 3.54
- 52-week range: $3.17 – $30.62
- Market cap: $80.33M
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
- FCF yield: -11.5%
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

- Spot price: $3.54
- Base revenue: $118.12M
- Shares: 22,693,356
- Net debt (Debt−Cash): -$11.38M

| Scenario | Growth | FCF margin | WACC | Term. g | Equity value | Share price | Upside |
|----------|--------|------------|------|---------|--------------|-------------|--------|
| bear | 25.0% | 1.0% | 12.0% | 1.5% | $39.46M | $1.74 | -50.9% |
| base | 35.0% | 3.0% | 10.0% | 2.5% | $180.36M | $7.95 | 124.5% |
| bull | 42.0% | 8.0% | 9.0% | 3.0% | $732.01M | $32.26 | 811.2% |

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
- ATM IV (est.): 183.6%
- IV rank: — (1 local samples)
- HV rank (20d realized): 100.0%


_Note: Delta band approximated via % OTM when greeks are unavailable; IV rank needs ~20+ local daily IV samples (have 1); run the options screen over time to build history.; HV rank is realized-vol rank (20d HV vs ~1y); useful when IV history is thin._

## Research loop (think → act)

1. _heuristic_ — Coverage looks adequate for this pass; stopping iterative loop.

## Sources

- **[S1]** BYRN fundamentals (yfinance)
  - Byrna Technologies, Inc.: price=3.54, rev=118120000.0, fcf=-9201000.0, shares=22693356.0, rev_cagr=0.3497464711860472, ROIC=0.2177063410328086, FCF yield=-0.11453363487259767
- **[S2]** BYRN DCF valuation (dcf)
  - Base share price=7.947753124041503, bull=32.256417371811665, bear=1.7389795505454393
- **[S3]** BYRN put screen (yfinance_options)
  - Expiration 2026-09-18 (DTE 56): 0 candidates; IV=1.8359383203124997, IV rank=None, HV rank=1.0. Delta band approximated via % OTM when greeks are unavailable; IV rank needs ~20+…

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
