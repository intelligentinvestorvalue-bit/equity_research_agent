# COE — Full research pack

> Not investment advice. Local research draft only.

**Templates:** memo, valuation, deep, income, fast
**Generated:** 2026-07-30T06:48:10.351605+00:00



---

# Template: Institutional deep dive (memo) (`memo`)

# COE — Planned Research Report

> Not investment advice. Local research draft only.

**Goal:** Institutional deep dive triggered by FilingDesk: Chief Executive Officer Huang Jack Jiajia open-market buy $3,080,724 (51Talk Online Education Group).
**Mode:** deep
**Template:** memo
**Planner:** template

## Plan executed

- **(1) Snapshot, KPIs & capital structure** (`fundamentals`): get_fundamentals
  - Multi-year KPI table, leverage, EV/EBITDA snapshot. Focus: Institutional deep dive triggered by FilingDesk: Chief Executive Officer Huang Jack Jiajia open-market buy $3,080,724 (51Talk Online Education Group).
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
- **(7g) Altman Z — medium-term bankruptcy risk** (`altman`): run_altman_z
  - Altman Z / Z'' distress screen from balance sheet + market equity; medium-term insolvency risk alongside scenario ranges
- **(8) Quarterly driver correlations** (`drivers`): analyze_drivers
  - Suggestive FCF/revenue/debt vs return correlations (small-n caveats)
- **(9) Thesis memo sections** (`memo`): draft_memo_sections
  - Exec summary, variant perception, catalysts, falsifiers, limitations

## Fundamentals [S1]
- Company: 51Talk Online Education Group
- Sector / industry: Consumer Defensive / Education & Training Services
- Price: 16.93
- 52-week range: $14.66 – $56.13
- Market cap: $101.70M
- Enterprise value: $69.03M
- Shares outstanding: 4.28M
- Beta: 0.748
- Book equity: -$31.36M
- Revenue (latest): $95.60M
- EBITDA (latest): -$13.99M
- Free cash flow (latest): $9.52M
- Operating income: -$14.43M
- Operating margin: -15.1%
- EV / EBITDA: -4.9x
- ROIC: 21.4%
- FCF yield: 9.4%
- Debt / Equity: -0.0937908600950346
- FCF / share: $2.22
- Revenue / share: $22.33

### Capital structure
- Cash: $38.87M
- Short-term debt: $1.76M
- Long-term debt: $1.18M
- Total debt: $2.94M
- Net debt: -$35.93M
- Net debt / EBITDA: 2.6x
- Working capital: -$34.96M
- Total assets: $66.09M
- Total liabilities: $97.34M
- Retained earnings: -$370.40M
- Current ratio: 0.6x

### Growth
- Revenue CAGR: 85.2%
- FCF CAGR: —
- Latest revenue YoY: 88.6%
- Latest FCF YoY: 72.3%

### Market expectations (yfinance, sparse)
- Mean target: —
- Target range: — – —
- Recommendation: none

_Consensus revenue/EBITDA forecasts are often unavailable via free feeds; treat targets as point-in-time only._

### Historical KPIs (multi-year)

| Year | Revenue | OCF | Capex | FCF | EBITDA | LT debt | Cash | Net debt | Net income |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2025 | $95.60M | $11.81M | $2.29M | $9.52M | -$13.99M | $2.94M | $38.87M | -$35.93M | -$16.80M |
| 2024 | $50.69M | $5.83M | $308.00K | $5.52M | -$7.91M | $2.68M | $27.76M | -$25.07M | -$7.24M |
| 2023 | $27.11M | $559.00K | $287.00K | $272.00K | -$13.56M | $631.00K | $21.30M | -$20.67M | -$15.03M |
| 2022 | $15.05M | -$45.70M | $5.00K | -$45.71M | -$12.26M | $734.00K | $18.19M | -$17.45M | -$42.56M |

## Charts

### Revenue & FCF history
![Revenue & FCF history](/charts/COE_memo_revenue_fcf.png)

### DCF scenario prices
![DCF scenario prices](/charts/COE_memo_dcf_scenarios.png)

### Base-case FCF path
![Base-case FCF path](/charts/COE_memo_base_fcf_path.png)

### EV/EBITDA scenario prices
![EV/EBITDA scenario prices](/charts/COE_memo_ev_ebitda_scenarios.png)

### Headwind/tailwind price ranges
![Headwind/tailwind price ranges](/charts/COE_memo_scenario_ranges.png)

### Normalized price vs peers
![Normalized price vs peers](/charts/COE_memo_peers_normalized.png)

## DCF valuation (base / bull / bear) [S3]

> Simplified revenue->FCF DCF. Not investment advice; assumptions are editable heuristics.

- Spot price: $16.93
- Base revenue: $95.60M
- Shares: 4,280,532
- Net debt (Debt−Cash): -$35.93M

| Scenario | Growth | FCF margin | WACC | Term. g | Equity value | Share price | Upside |
|----------|--------|------------|------|---------|--------------|-------------|--------|
| bear | 25.0% | 8.0% | 12.0% | 1.5% | $216.80M | $50.65 | 199.2% |
| base | 35.0% | 10.0% | 10.0% | 2.5% | $489.90M | $114.45 | 576.0% |
| bull | 42.0% | 13.0% | 9.0% | 3.0% | $980.64M | $229.09 | 1253.2% |

### Assumption notes
- Base revenue growth seeded from historical rate (88.6%).


### Base-case projected FCF

- Year 1: revenue $129.06M, FCF $12.85M (PV $11.68M)
- Year 2: revenue $174.23M, FCF $17.35M (PV $14.34M)
- Year 3: revenue $235.21M, FCF $23.42M (PV $17.60M)
- Year 4: revenue $317.54M, FCF $31.62M (PV $21.60M)
- Year 5: revenue $428.68M, FCF $42.69M (PV $26.51M)
- Terminal value $583.40M (PV $362.25M)

## Valuation — EV/EBITDA scenarios [S2]

> Priced-in model: implied price = (EBITDA × EV/EBITDA − net debt) ÷ shares. Not a forecast.

- Spot: $16.93
- Net debt used: -$35.93M

| Scenario | EBITDA | EV/EBITDA | Implied EV | Equity value | Implied price |
|---|---:|---:|---:|---:|---:|
| bear | $700.00M | 6.0x | $4.20B | $4.24B | $989.58 |
| base | $1.00B | 8.0x | $8.00B | $8.04B | $1877.32 |
| bull | $1.20B | 10.0x | $12.00B | $12.04B | $2811.78 |

- EBITDA missing or non-positive; scenarios use placeholder $1B EBITDA — edit before relying on prices.
- No current EV/EBITDA; defaulted base multiple to 8.0x.

## Scenario price ranges (headwinds & tailwinds) [S29]

> Medium-term (18–36 months (medium / medium-long term)) driver → EV/EBITDA bridge. Distinct from the FCF DCF path. Not investment advice.

- Spot: $16.93
- Anchor multiple: 8.0x (driver_ev_ebitda_bridge)
- Anchor EBITDA: $1.00B
- Probability-weighted midpoint: **$2034.99** (heuristic weights, not a rating)
- Driver extraction: `rules`

### Headwinds (bear-case fuel)

- **Balance-sheet / refinancing pressure** — sector=Consumer Defensive industry=Education & Training Services revenue=95601000.0 ebitda=-13995000.0 fcf=9520000.0 net_debt=-35928000.0 nd_ebitda=2.567202572347267 target=None re _(source: fundamentals)_
- **Competitive / pricing pressure** — Commodity Price Outlook | The Daily Spark Jun 15, 2026 · Commodity prices are moving higher across the board, but for different reasons in each segment. Subscribe for daily updates _(source: web)_
- **Margin / cost headwind** — Rare Earth Archives - MINING.COM 3 days ago · Algae breakthrough could double rare earth concentrations Researchers found using algae is a cleaner way to concentrate rare earths an _(source: web)_

### Tailwinds (bull-case fuel)

- **Positive free cash flow** — FCF $9.52M (yield 9.4%) _(source: fundamentals)_
- **Revenue growth momentum** — Latest revenue YoY ≈ 88.6% _(source: fundamentals)_
- **Product / pricing power** — sector=Consumer Defensive industry=Education & Training Services revenue=95601000.0 ebitda=-13995000.0 fcf=9520000.0 net_debt=-35928000.0 nd_ebitda=2.567202572347267 target=None re _(source: fundamentals)_
- **Multiple re-rating / Street upgrades** — Why Stanley Black & Decker Stock Popped Today Key Points Wolfe Research analyst Nigel Coe upgraded Stanley stock this morning. After two years of declining sales, Coe thinks the st _(source: web)_
- **Growth / execution upside** — 51Talk Online Education Group (COE) Earnings Forecast: Future EPS & Revenue Growth Estimates — TradingKey June 16, 2026 - See what Wall Street and leading analysts expect from 51Ta _(source: web)_

### Price ranges by case

| Case | Prob. | Metric vs TTM | Multiple | Price low | Mid | High | Upside vs spot |
|---|---:|---:|---:|---:|---:|---:|---:|
| bear | 0.21 | 0.78x | 5.6x | $926.78 | $1028.83 | $1130.87 | +5977% |
| base | 0.45 | 1.04x | 8.0x | $1816.02 | $1952.08 | $2088.13 | +11430% |
| bull | 0.34 | 1.19x | 9.9x | $2490.40 | $2766.18 | $3041.96 | +16239% |

#### Bear — headwinds dominate

Headwinds bite: weaker operating trajectory and multiple compression. Equity duration shrinks if cash generation fails to offset leverage / competitive pressure.

- **Range:** $926.78 – $1130.87 (mid $1028.83) · EBITDA $780.00M · multiple 5.6x
- Driver: **Balance-sheet / refinancing pressure** — sector=Consumer Defensive industry=Education & Training Services revenue=95601000.0 ebitda=-13995000.0 fcf=9520000.0 net_debt=-35928000.0 nd_ebitda=2.5672025723
- Driver: **Competitive / pricing pressure** — Commodity Price Outlook | The Daily Spark Jun 15, 2026 · Commodity prices are moving higher across the board, but for different reasons in each segment. Subscri
- Driver: **Margin / cost headwind** — Rare Earth Archives - MINING.COM 3 days ago · Algae breakthrough could double rare earth concentrations Researchers found using algae is a cleaner way to concen

#### Base — mixed execution

Balanced path: some tailwinds offset headwinds. Operating scale roughly holds with modest repair/normalization; valuation stays near the current EV/EBITDA anchor.

- **Range:** $1816.02 – $2088.13 (mid $1952.08) · EBITDA $1.04B · multiple 8.0x
- Driver: **Positive free cash flow** — FCF $9.52M (yield 9.4%)
- Driver: **Revenue growth momentum** — Latest revenue YoY ≈ 88.6%
- Driver: **Balance-sheet / refinancing pressure** — sector=Consumer Defensive industry=Education & Training Services revenue=95601000.0 ebitda=-13995000.0 fcf=9520000.0 net_debt=-35928000.0 nd_ebitda=2.5672025723
- Driver: **Competitive / pricing pressure** — Commodity Price Outlook | The Daily Spark Jun 15, 2026 · Commodity prices are moving higher across the board, but for different reasons in each segment. Subscri

#### Bull — tailwinds dominate

Tailwinds compound: operating improvement plus a re-rating toward peer or recovery multiples as balance-sheet and growth narratives improve.

- **Range:** $2490.40 – $3041.96 (mid $2766.18) · EBITDA $1.19B · multiple 9.9x
- Driver: **Positive free cash flow** — FCF $9.52M (yield 9.4%)
- Driver: **Revenue growth momentum** — Latest revenue YoY ≈ 88.6%
- Driver: **Product / pricing power** — sector=Consumer Defensive industry=Education & Training Services revenue=95601000.0 ebitda=-13995000.0 fcf=9520000.0 net_debt=-35928000.0 nd_ebitda=2.5672025723
- Driver: **Multiple re-rating / Street upgrades** — Why Stanley Black & Decker Stock Popped Today Key Points Wolfe Research analyst Nigel Coe upgraded Stanley stock this morning. After two years of declining sale
- Driver: **Growth / execution upside** — 51Talk Online Education Group (COE) Earnings Forecast: Future EPS & Revenue Growth Estimates — TradingKey June 16, 2026 - See what Wall Street and leading analy

### Method notes

- Item 1A risks weighted toward headwinds.
- Current ev_ebitda multiple missing; anchored at 8.0x.
- Mapping follows Gemini/Perplexity-style scenario memos: qualitative drivers → operating metric & multiple paths → share-price ranges over a medium-term horizon.

## Altman Z-score (medium-term bankruptcy risk) [S30]

**Ticker:** COE
**Primary model:** `z_double_prime`
**Z-score:** **-23.55** — Distress zone (Z'')

### Medium-term read (18–36 months)

Elevated medium-term bankruptcy risk under the non-manufacturer Altman model.

### Model scores

| Model | Score | Zone guide |
| --- | ---: | --- |
| Classic public Z | -7.13 | >2.99 safe · 1.81–2.99 grey · <1.81 distress |
| Non-manufacturer Z'' | -23.55 | >2.60 safe · 1.10–2.60 grey · <1.10 distress |

### Inputs (latest statements / market)

| Item | Value |
| --- | ---: |
| Total assets | $66.1M |
| Total liabilities | $97.3M |
| Working capital | $-35.0M |
| Current assets | $60.4M |
| Current liabilities | $95.4M |
| Retained earnings | $-370.4M |
| EBIT / operating income | $-14.4M |
| Sales / revenue | $95.6M |
| Market value of equity | $101.7M |
| Book equity | $-31.4M |

### Ratio components

| Component | Definition | Value |
| --- | --- | ---: |
| X1 | Working capital / Total assets | -0.529 |
| X2 | Retained earnings / Total assets | -5.604 |
| X3 | EBIT / Total assets | -0.218 |
| X4 | Market equity / Total liabilities | 1.045 |
| X4b | Book equity / Total liabilities (Z'') | -0.322 |
| X5 | Sales / Total assets | 1.446 |

### Formulas

- Classic Z = `1.2·X1 + 1.4·X2 + 3.3·X3 + 0.6·X4 + 1.0·X5`
- Z'' = `6.56·X1 + 3.26·X2 + 6.72·X3 + 1.05·X4b`

- _Altman Z is a statistical screen from historical samples — not a forecast or credit rating._
- _Use alongside liquidity, covenants, and refinancing calendar over an 18–36 month horizon._
- _Sector/industry (Consumer Defensive / Education & Training Services) leans non-manufacturing; primary screen uses Z'' when available._

_Not investment advice. Altman thresholds are historical; banks/REITs/financials are poorly suited to these models._

## Peer & factor comps

- Sector / industry: Consumer Defensive / Education & Training Services
- Peers: —

| Ticker | Mkt cap | EV/EBITDA | ND/EBITDA | Beta | 1y | 5y | Vol |
|---|---:|---:|---:|---:|---:|---:|---:|
| COE | $101.7M | -5.0x | 2.4x | 0.75 | -41.4% | 47.5% | 80.8% |

- No industry peer map match; comps limited to the subject ticker.

_Price returns are price-only (dividends ignored). Peer set is heuristic, not a formal comps universe._

## Earnings, guidance & revision catalysts

| Date | EPS est | EPS actual | Surprise | 1-day move |
|---|---:|---:|---:|---:|
| 2021-09-28 | -7.52 | -3.36 | 4.16 | -5.7% |
| 2021-05-17 | 1.30 | 2.83 | 1.53 | -2.8% |
| 2021-03-05 | 3.96 | 6.76 | 2.80 | -2.8% |
| 2020-11-23 | 1.64 | 6.58 | 4.94 | -2.8% |
| 2020-09-08 | 4.85 | 6.85 | 2.00 | -2.8% |
| 2020-05-26 | 1.11 | 10.27 | 9.16 | -2.8% |
| 2020-03-09 | -2.22 | 0.83 | 3.05 | -2.8% |
| 2017-08-25 | -0.24 | -26.40 | -26.16 | -2.8% |
| 2017-05-22 | -22.04 | -25.20 | -3.16 | -2.8% |
| 2017-03-22 | -95.40 | -28.96 | 66.44 | -2.8% |
| 2016-11-21 | -65.88 | -22.64 | 43.24 | -2.8% |
| 2016-08-23 | -38.42 | -73.60 | -35.18 | -2.8% |

_EPS surprise vs 1-day move Pearson r=0.022 (n=12, p≈0.944); treat as suggestive only._

_Guidance vs Street and adjusted EBITDA are often missing from free feeds; use web/SEC sections for narrative guidance._

## Recent SEC filings (10-Q / 8-K)

_No recent filings found._

## Key driver analysis (quarterly)

Pearson / Spearman correlations of quarterly stock returns with fundamentals.

| Driver | Pearson r | p | n | Spearman ρ | p |
|---|---:|---:|---:|---:|---:|
| Revenue growth (YoY) | — | — | 1 | — | — |
| Free cash flow | — | — | — | — | — |
| FCF margin | — | — | — | — | — |
| Operating cash flow | — | — | — | — | — |
| Long-term debt level | -0.393 | 0.459 | 5 | -0.300 | 0.586 |
| EBITDA | 0.044 | 0.940 | 5 | -0.300 | 0.586 |
| Capex (abs) | — | — | — | — | — |

- Correlations describe association, not causation.
- Small samples (especially regime splits) are directional only.

## Executive summary

51Talk Online Education Group (COE) trades near 16.93 with market cap $101.70M and EV $69.03M. Net debt is -$35.93M (ND/EBITDA 2.567202572347267). Latest revenue $95.60M, EBITDA -$13.99M, FCF $9.52M.

**Goal focus:** Institutional deep dive triggered by FilingDesk: Chief Executive Officer Huang Jack Jiajia open-market buy $3,080,724 (51Talk Online Education Group)..

What matters most (framework): balance-sheet trajectory, cash generation vs leverage, and whether market expectations (sparse free-data targets) already price execution risk.

EV/EBITDA implied prices — bear $989.58 / base $1877.32 / bull $2811.78.

## Company setup & business model

No Item 1 Business text extracted.

_Source: latest 10-K Item 1 (Business), summarized locally._

## Variant perception

- **Consensus frame (sparse):** recommendation=none, mean target=—.
- **Bear:** leverage and execution risk dominate; cash generation fails to cover refinancing / reinvestment needs; equity remains constrained by net debt.
- **Bull:** cash-flow and strategic optionality re-rate the equity as leverage falls and growth/mix improves.
- **Middle:** returns may track free-cash-flow more than headline revenue — verify with driver analysis tab.

## Catalysts & monitoring

- Next earnings window (calendar): unconfirmed
- Peer tape to watch: n/a
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
| --- | --- | --- | --- |
| Guidance / outlook | Forward cash/earnings path | China Online Education Group (COE) Stock Forecast, Price Targets... COE average Analyst price target in the past 3 months is ―. Each month's total comprises the sum of three months | China Online Education Group (COE) Stock Forecast, Price Targets... |
| Margin / EBITDA | Mix and operating leverage | GTES Q1 Earnings Call: Margin Initiatives, Tariff Mitigation, and Stable Outlook... Power transmission and fluid power solutions provider Gates Corporation (NYSE:GTES) reported Q1 | GTES Q1 Earnings Call: Margin Initiatives, Tariff Mitigation, and Stable Outlook... |
| Leverage / refinancing | Balance-sheet repair | 51Talk Online Education Group: In-Depth Analysis and 2025 ... Surging Revenues: 51Talk Online Education Group (NYSE: COE), known in China ... on its strength in online language ins | 51Talk Online Education Group: In-Depth Analysis and 2025 ... |

_Proxies are heuristic extractions from public web/SEC context; verify against primary filings._

## Catalyst calendar

| Window | Catalyst | Notes |
|---|---|---|
| January 18, 2026 | Web event | Why 51Talk Online Education Group’s (COE) Stock Is Down 7.28% | AAII |
| June 16, 2026 | Web event | 51Talk Online Education Group (COE) Earnings Forecast: Future EPS & Revenue Growth Estimates — TradingKey |
| Jul 2, 2026 | Web event | Jack Jiajia Huang Insider Trading Activity, SEC Form 4 Filings |
| February 25, 2025 | Web event | Home - Investor Day |
| Jun 15, 2026 | Web event | Commodity Price Outlook | The Daily Spark |

## Web research — web_analysts

- Queries: COE analyst price target, 51Talk Online Education Group stock rating OR consensus OR upgrade OR downgrade, COE Institutional deep dive triggered by FilingDesk: Chief Executive Officer Huang Jack Jiajia open-market buy $3,080,724 (51Talk Online Education Group). analyst, COE guidance OR investor day OR catalyst
- Unique hits: 22
- Pages fetched: 1/3

### Web synthesis — web_analysts (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, revenue, interest rate, product, service, market

- | StockStory · via Yahoo Finance | https://finance.yahoo.com/news/5-most-interesting-analyst-questions-054029242.html Stanley Black & Decker’s fourth quarter results were met with a negative market response, as revenue...
- [HIT] The Top 5 Analyst Questions From Hubbell’s Q4 Earnings Call | StockStory · via Yahoo Finance | https://finance.yahoo.com/news/top-5-analyst-questions-hubbell-053739165.html Hubbell’s fourth-quarter results were met with a positive market response, underscoring the strength...
- [HIT] 51Talk Online Education Group (COE) Earnings Forecast: Future EPS & Revenue Growth Estimates — TradingKey | www.tradingkey.com | https://www.tradingkey.com/markets/stocks/nasdaq-coe/earnings June 16, 2026 - See what Wall Street and leading analysts expect from 51Talk Online Education Group (COE).
- Track quarterly and annual EPS forecasts, revenue growth targets, and rating upgrade or downgrade activity in real time so you can prepare for earnings season early.
- [HIT] 51Talk Online Education Group (NYSEAM:COE) Stock Valuation, Peer Comparison & Price Targets - Simply Wall St | simplywall.st | https://simplywall.st/stocks/us/consumer-services/nysemkt-coe/51talk-online-education-group/valuation Research 51Talk Online Education Group's (NYSEAM:COE) stock key valuation metrics while comparing it with its industry peers & market side by side.
- [HIT] Credit Card, Mortgage, Banking, Auto | Chase Online | Chase.com | www.chase.com | https://www.chase.com/ Chase online; credit cards, mortgages, commercial banking, auto loans, investing & retirement planning, checking and business banking.Open a savings account or open a Certificate of Deposit ( see interest rates ) and start saving your money.
- [HIT] Investor Day | JPMorganChase | www.jpmorganchase.com | https://www.jpmorganchase.com/ir/investor-day Investor Relations 2025 Investor Day Investor Relations Quarterly Earnings Press Releases  [HIT] Home - Investor Day | paypal2025irday.q4ir.com | https://paypal2025irday.q4ir.com/home/default.aspx Overview On February 25, 2025, President and CEO Alex Chriss and the leadership team presented PayPal's strategy, growth priorities, and product innovation during our Investor Day.
- [PAGE] COE Stock IQ Score, Analysis & Analyst Targets | StocksRunner | https://stocksrunner.com/symbol/COE COE Stock IQ Score, Analysis & Analyst Targets | StocksRunner × Recently Viewed COE 51Talk Online Education Most Trending QCOM QUALCOMM -4.42% SOFI SoFi Technologies In -9.02% SBUX Starbucks +1.01% HUM Humana -5.99% GEHC GE HealthCare Technologies +12.15% COE Stock Analysis & IQ Rating | COE COE 51Talk Online Education $16.91 +$0.24 | +1.56% Follow Set Alerts Overview Comments Insights Risks Rating Chart Analysts Street Sentiment Signals 52W High $56.13 MKT CAP $101.58M 52W Low $14.66 VOL $9.28K P/E Ratio N/A AVG VOL $20.85K RSI 24.85 TREND Sideways COE Stock IQ Login to see 51Talk Online Education (COE) Stock IQ rating Get instant clarity on whether to Buy, Hold, or Avoid.

### Sources found
- [COE Stock IQ Score, Analysis & Analyst Targets | StocksRunner](https://stocksrunner.com/symbol/COE)
  - Analyst price target data for COE is tracked and updated on StocksRunner as new analyst coverage is published. Visit stocksrunner.com/symbol/COE for the late…
- [China Online Education Group (COE) Stock Forecast, Price Targets...](https://www.tipranks.com/stocks/coe/forecast)
  - COE average Analyst price target in the past 3 months is ―. Each month's total comprises the sum of three months' worth of ratings.What is COE’s average 12-m…
- [51Talk Online Education Group (COE) Analyst Insights, Price Targets...](https://finance.yahoo.com/quote/COE/analyst-insights/)
  - Most active penny stocks. Analyst strong buy. Stock comparison.+0.52 +0.66%. ADVERTISEMENT. COE. 51Talk Online Education Group. 16.34 -5.39%.
- [Analyst Ratings of 51 TALK ONLINE EDUCATION... | ChartMill.com](https://www.chartmill.com/stock/quote/COE/analyst-ratings)
  - Analysts have set a mean price target forecast of 9.18. This target is 37.63% above the current price. COE was analyzed by 8 analysts. The buy percentage con…
- [The 5 Most Interesting Analyst Questions From Stanley Black & Decker’s Q4 Earnin...](https://finance.yahoo.com/news/5-most-interesting-analyst-questions-054029242.html)
  - Stanley Black & Decker’s fourth quarter results were met with a negative market response, as revenue...
- [5 Revealing Analyst Questions From Carrier Global’s Q4 Earnings Call](https://finance.yahoo.com/news/5-revealing-analyst-questions-carrier-053529400.html)
  - Carrier Global’s fourth quarter results were shaped by persistent softness in its residential and li...
- [The Top 5 Analyst Questions From Hubbell’s Q4 Earnings Call](https://finance.yahoo.com/news/top-5-analyst-questions-hubbell-053739165.html)
  - Hubbell’s fourth-quarter results were met with a positive market response, underscoring the strength...
- [Why Stanley Black & Decker Stock Popped Today](https://finance.yahoo.com/news/why-stanley-black-decker-stock-203017219.html)
  - Key Points Wolfe Research analyst Nigel Coe upgraded Stanley stock this morning. After two years of declining sales, Coe thinks the stock looks...
- [51Talk Online Education Group (NYSE:COE) Stock Passes Below 50 Day Moving Average – Here’s What Happened - Daily Political](https://www.dailypolitical.com/2026/07/18/51talk-online-education-group-nysecoe-stock-passes-below-50-day-moving-average-heres-what-happened.html)
  - 2 weeks ago - 51Talk Online Education Group (NYSE:COE – Get Free Report) passed below its 50 day moving average during trading on Friday . The stock has a 50…
- [Why 51Talk Online Education Group’s (COE) Stock Is Down 7.28% | AAII](https://www.aaii.com/investingideas/article/311491-why-51talk-online-education-group8217s-coe-stock-is-down-728)
  - January 18, 2026 - As of Thursday, July 03, 51Talk Online Education Group’s COE share price has dipped by 7.28%, which has investors questioning if this is r…
- [51Talk Online Education Group (COE) Earnings Forecast: Future EPS & Revenue Growth Estimates — TradingKey](https://www.tradingkey.com/markets/stocks/nasdaq-coe/earnings)
  - June 16, 2026 - See what Wall Street and leading analysts expect from 51Talk Online Education Group (COE). Track quarterly and annual EPS forecasts, revenue …
- [51Talk Online Education Group (NYSEAM:COE) Stock Valuation, Peer Comparison & Price Targets - Simply Wall St](https://simplywall.st/stocks/us/consumer-services/nysemkt-coe/51talk-online-education-group/valuation)
  - Research 51Talk Online Education Group's (NYSEAM:COE) stock key valuation metrics while comparing it with its industry peers & market side by side.

### Search warnings
- news:51Talk Online Education Group stock rating OR consensus OR upgrade OR downgrade: No results found.

## Web research — web_drivers

- Queries: COE Institutional deep dive triggered by FilingDesk: Chief Executive Officer Huang Jack Jiajia open-market buy $3,080,724 (51Talk Online Education Group)., 51Talk Online Education Group COE outlook OR catalyst OR commodity OR uranium OR rare earth OR vanadium, COE sector drivers OR market demand, 51Talk Online Education Group COE backlog OR contract OR refinancing OR leverage
- Unique hits: 17
- Pages fetched: 2/3

### Web synthesis — web_drivers (rule-based fallback — Ollama unavailable)
**Keyword hits:** revenue, margin, supply chain, segment, product, service, market, operations, subsidiary

- | trendspider.com | https://trendspider.com/markets/symbols/COE/ 51Talk Online Education Group ("51Talk", or the "Company") (NYSE:COE), a global online education platform with core expertise in English education, today announced that its board of directors has authorized a new share.
- [HIT] Commodity Price Outlook | The Daily Spark | www.apollo.com | https://www.apollo.com/wealth/insights-news/insights/daily-spark/Commodity-Price-Outlook Jun 15, 2026 · Commodity prices are moving higher across the board, but for different reasons in each segment.
- [HIT] Rare Earth Archives - MINING.COM | www.mining.com | https://www.mining.com/commodity/rare-earth/ 3 days ago · Algae breakthrough could double rare earth concentrations Researchers found using algae is a cleaner way to concentrate rare earths and help the US strengthen critical mineral supply chains.
- [HIT] Commodity Prices | Commodity Market | Markets Insider | markets.businessinsider.com | https://markets.businessinsider.com/commodities?op=1 Get all information on the commodity market.
- [HIT] Developing labour market metrics for the market sector, UK - Office...
- | www.ons.gov.uk | https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/labourproductivity/articles/developinglabourmarketmetricsforthemarketsectoruk/2016 Figure 5 shows COE for the market and non-market sectors by industry in 2015.
- Non-market sector COE is zero for industries with entirely market sector output, and is small relative to market sector output for all hybrid industries except public administration, education and health.
- [HIT] How Are Enterprises Investing in the Automation COE Market?

### Sources found
- [COE - 51 Talk Online Education Group ADR Stock Price and Quote](https://finviz.com/stock?t=COE)
  - 51Talk Online Education Group is a global online education platform focusing on English lessons.Huang Jack Jiajia. Chief Executive Officer. Jun 30 '26. Optio…
- [COE (51Talk Online Education Group) – Technical Charts and...](https://trendspider.com/markets/symbols/COE/)
  - 51Talk Online Education Group ("51Talk", or the "Company") (NYSE:COE), a global online education platform with core expertise in English education, today ann…
- [China Online Education Group Enters into Definitive Agreement to](https://www.stocktitan.net/news/COE/china-online-education-group-enters-into-definitive-agreement-to-y14z5da9rg4i.html)
  - China Online Education Group ("51Talk" or the "Company") (NYSE: COE), a global online education platform with core expertise in.Industry Professional and Man…
- [COE Stock Price, Quote & Chart | 51 TALK ONLINE EDUCATION...](https://www.chartmill.com/stock/quote/COE/profile)
  - 51 TALK ONLINE EDUCATION GRO (COE) Stock Price & Overview. NYSEARCA:COE • US16954L2043.CEO: Jack Jiajia Huang. Employees: 360. COE Company Website. COE Inves…
- [51Talk Online Education Group (COE) Q1 2026 Earnings Call Transcript](https://seekingalpha.com/article/4914549-51talk-online-education-group-coe-q1-2026-earnings-call-transcript)
  - Hello, ladies and gentlemen. Thank you for standing by for 51Talk Online Education Group's First Quarter 2026 Earnings Conference Call. [Operator Instruction…
- [Uranium - Wikipedia](https://en.wikipedia.org/wiki/Uranium)
  - Uranium is a chemical element; it has symbol U and atomic number 92. It is a silvery-grey metal in the actinide series of the periodic table. A uranium atom …
- [Commodity Price Outlook | The Daily Spark](https://www.apollo.com/wealth/insights-news/insights/daily-spark/Commodity-Price-Outlook)
  - Jun 15, 2026 · Commodity prices are moving higher across the board, but for different reasons in each segment. Subscribe for daily updates.
- [Rare Earth Archives - MINING.COM](https://www.mining.com/commodity/rare-earth/)
  - 3 days ago · Algae breakthrough could double rare earth concentrations Researchers found using algae is a cleaner way to concentrate rare earths and help the…
- [Commodity Prices | Commodity Market | Markets Insider](https://markets.businessinsider.com/commodities?op=1)
  - Get all information on the commodity market. Find the latest commodity prices including News, Charts, Realtime Quotes and even more about commodities.
- [Developing labour market metrics for the market sector, UK - Office...](https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/labourproductivity/articles/developinglabourmarketmetricsforthemarketsectoruk/2016)
  - Figure 5 shows COE for the market and non-market sectors by industry in 2015. Non-market sector COE is zero for industries with entirely market sector output…
- [How Are Enterprises Investing in the Automation COE Market?](https://xn----jtbtibrbj7a4dza.xn--p1ai/blogs/44171/How-Are-Enterprises-Investing-in-the-Automation-COE-Market)
  - Another factor driving market growth is the rising demand for automation solutions in the healthcare sector.Alternative Market Research Questions for Automat…
- [5 Revealing Analyst Questions From Emerson Electric’s Q4 Earnings Call](https://finance.yahoo.com/news/5-revealing-analyst-questions-emerson-053149645.html)
  - Emerson’s fourth quarter results received a positive market response, as the company met Wall Street...

### Search warnings
- news:51Talk Online Education Group COE outlook OR catalyst OR commodity OR uranium OR rare earth OR vanadium: No results found.
- news:51Talk Online Education Group COE backlog OR contract OR refinancing OR leverage: No results found.

## SEC filing [S25]
- Extraction OK: False
- Item 1 chars: 0
- Item 1A chars: 0
- Item 7 chars: 0
- Meta: {'accession_number': None, 'filing_date': '', 'source': 'edgartools', 'path': 'C:\\DevWork\\equity_research_agent\\data\\filings\\COE_10k.txt'}

## Qualitative analysis (local LLM)

_Item 1 Business summary mode: empty (see Company setup & business model)._

### Item 1A — Risk Factors
No text extracted.


### Item 7 — MD&A
No text extracted.


## Research loop (think → act)

1. _heuristic_ — Coverage looks adequate for this pass; stopping iterative loop.

## Sources

- **[S1]** COE fundamentals (yfinance)
  - 51Talk Online Education Group: price=16.93, rev=95601000.0, fcf=9520000.0, shares=4280532.0, rev_cagr=0.8520862926062147, ROIC=0.21444601322731663, FCF yield=0.09360511118517365
- **[S2]** COE EV/EBITDA valuation (multiples)
  - Base implied price=1877.3199219162477, multiple=8.0
- **[S3]** COE DCF valuation (dcf)
  - Base share price=114.44814308174645, bull=229.09247777968184, bear=50.64858919987204
- **[S4]** COE peer comps (peers)
  - Peers: ; rows=1
- **[S5]** COE earnings history (earnings)
  - rows=12; next=None
- **[S6]** COE Stock IQ Score, Analysis & Analyst Targets | StocksRunner (web) — https://stocksrunner.com/symbol/COE
  - Analyst price target data for COE is tracked and updated on StocksRunner as new analyst coverage is published. Visit stocksrunner.com/symbol/COE for the latest target price info…
- **[S7]** China Online Education Group (COE) Stock Forecast, Price Targets... (web) — https://www.tipranks.com/stocks/coe/forecast
  - COE average Analyst price target in the past 3 months is ―. Each month's total comprises the sum of three months' worth of ratings.What is COE’s average 12-month price target, a…
- **[S8]** 51Talk Online Education Group (COE) Analyst Insights, Price Targets... (web) — https://finance.yahoo.com/quote/COE/analyst-insights/
  - Most active penny stocks. Analyst strong buy. Stock comparison.+0.52 +0.66%. ADVERTISEMENT. COE. 51Talk Online Education Group. 16.34 -5.39%.
- **[S9]** Analyst Ratings of 51 TALK ONLINE EDUCATION... | ChartMill.com (web) — https://www.chartmill.com/stock/quote/COE/analyst-ratings
  - Analysts have set a mean price target forecast of 9.18. This target is 37.63% above the current price. COE was analyzed by 8 analysts. The buy percentage consensus is at 45.
- **[S10]** The 5 Most Interesting Analyst Questions From Stanley Black & Decker’s Q4 Earnin... (web) — https://finance.yahoo.com/news/5-most-interesting-analyst-questions-054029242.html
  - Stanley Black & Decker’s fourth quarter results were met with a negative market response, as revenue...
- **[S11]** 5 Revealing Analyst Questions From Carrier Global’s Q4 Earnings Call (web) — https://finance.yahoo.com/news/5-revealing-analyst-questions-carrier-053529400.html
  - Carrier Global’s fourth quarter results were shaped by persistent softness in its residential and li...
- **[S12]** The Top 5 Analyst Questions From Hubbell’s Q4 Earnings Call (web) — https://finance.yahoo.com/news/top-5-analyst-questions-hubbell-053739165.html
  - Hubbell’s fourth-quarter results were met with a positive market response, underscoring the strength...
- **[S13]** Why Stanley Black & Decker Stock Popped Today (web) — https://finance.yahoo.com/news/why-stanley-black-decker-stock-203017219.html
  - Key Points Wolfe Research analyst Nigel Coe upgraded Stanley stock this morning. After two years of declining sales, Coe thinks the stock looks...
- **[S14]** COE Stock IQ Score, Analysis & Analyst Targets | StocksRunner (web_page) — https://stocksrunner.com/symbol/COE
  - COE Stock IQ Score, Analysis & Analyst Targets | StocksRunner × Recently Viewed COE 51Talk Online Education Most Trending QCOM QUALCOMM -4.42% SOFI SoFi Technologies In -9.02% S…
- **[S15]** COE - 51 Talk Online Education Group ADR Stock Price and Quote (web) — https://finviz.com/stock?t=COE
  - 51Talk Online Education Group is a global online education platform focusing on English lessons.Huang Jack Jiajia. Chief Executive Officer. Jun 30 '26. Option Exercise.
- **[S16]** COE (51Talk Online Education Group) – Technical Charts and... (web) — https://trendspider.com/markets/symbols/COE/
  - 51Talk Online Education Group ("51Talk", or the "Company") (NYSE:COE), a global online education platform with core expertise in English education, today announced that its boar…
- **[S17]** China Online Education Group Enters into Definitive Agreement to (web) — https://www.stocktitan.net/news/COE/china-online-education-group-enters-into-definitive-agreement-to-y14z5da9rg4i.html
  - China Online Education Group ("51Talk" or the "Company") (NYSE: COE), a global online education platform with core expertise in.Industry Professional and Management Development …
- **[S18]** COE Stock Price, Quote & Chart | 51 TALK ONLINE EDUCATION... (web) — https://www.chartmill.com/stock/quote/COE/profile
  - 51 TALK ONLINE EDUCATION GRO (COE) Stock Price & Overview. NYSEARCA:COE • US16954L2043.CEO: Jack Jiajia Huang. Employees: 360. COE Company Website. COE Investor Relations. Phone…
- **[S19]** 51Talk Online Education Group (COE) Q1 2026 Earnings Call Transcript (web) — https://seekingalpha.com/article/4914549-51talk-online-education-group-coe-q1-2026-earnings-call-transcript
  - Hello, ladies and gentlemen. Thank you for standing by for 51Talk Online Education Group's First Quarter 2026 Earnings Conference Call. [Operator Instructions] Today's conferenc…
- **[S20]** Uranium - Wikipedia (web) — https://en.wikipedia.org/wiki/Uranium
  - Uranium is a chemical element; it has symbol U and atomic number 92. It is a silvery-grey metal in the actinide series of the periodic table. A uranium atom has 92 protons and 9…
- **[S21]** Commodity Price Outlook | The Daily Spark (web) — https://www.apollo.com/wealth/insights-news/insights/daily-spark/Commodity-Price-Outlook
  - Jun 15, 2026 · Commodity prices are moving higher across the board, but for different reasons in each segment. Subscribe for daily updates.
- **[S22]** Rare Earth Archives - MINING.COM (web) — https://www.mining.com/commodity/rare-earth/
  - 3 days ago · Algae breakthrough could double rare earth concentrations Researchers found using algae is a cleaner way to concentrate rare earths and help the US strengthen criti…
- **[S23]** COE - 51 Talk Online Education Group ADR Stock Price and Quote (web_page) — https://finviz.com/stock?t=COE
  - COE - 51 Talk Online Education Group ADR Stock Price and Quote Home News Screener Charts Maps Groups Portfolio Insider Futures Forex Crypto Calendar Pricing Theme Help Login Reg…
- **[S24]** China Online Education Group Enters into Definitive Agreement to Spin off China Mainland Business | COE Stock News (web_page) — https://www.stocktitan.net/news/COE/china-online-education-group-enters-into-definitive-agreement-to-y14z5da9rg4i.html
  - China Online Education Group Enters into Definitive Agreement to Spin off China Mainland Business | COE Stock News Home News COE China Online Education Group Enters into Definit…
- **[S25]** COE 10-K (sec)
  - Item 1 chars=0, Item 1A chars=0, Item 7 chars=0, ok=False, source=edgartools
- **[S26]** Item 1 Business summary (nlp)
  - ### Item 1 — Business No Item 1 Business text extracted. 
- **[S27]** Item 1A summary (nlp)
  - ### Item 1A — Risk Factors No text extracted. 
- **[S28]** Item 7 summary (nlp)
  - ### Item 7 — MD&A No text extracted. 
- **[S29]** COE scenario price ranges (scenarios)
  - ok=True; base mid=1952.0769848233817; headwinds=3; tailwinds=5
- **[S30]** COE Altman Z-score (altman)
  - ok=True; model=z_double_prime; Z=-23.54543902075005; zone=distress
- **[S31]** COE driver analysis (drivers)
  - ok=True; drivers=7
- **[S32]** COE memo sections (memo)
  - mode=rules; proxies=3

## Self-critique

_Automated review (heuristic)._

### Strengths
- Combines local fundamentals, optional DCF scenarios, and cited sources where available.
- Keeps a non-advisory framing for local research drafts.

### Issues & gaps
- Base-case upside vs spot is extreme (>150%); check growth/margin/WACC assumptions for optimism bias.
- Draft uses strong recommendation language; this local agent should stay descriptive, not advisory.

### Caution for readers
- Treat scenario prices as sensitivity output, not a forecast.
- Re-check primary filings and fresh market data before any decision.



---

# Template: Valuation (DCF + Street + drivers) (`valuation`)

# COE — Planned Research Report

> Not investment advice. Local research draft only.

**Goal:** Institutional deep dive triggered by FilingDesk: Chief Executive Officer Huang Jack Jiajia open-market buy $3,080,724 (51Talk Online Education Group).
**Mode:** deep
**Template:** valuation
**Planner:** template

## Plan executed

- **(1) Financial statements & key metrics** (`fundamentals`): get_fundamentals
  - Revenue, free cash flow, shares outstanding, historical growth rates, margins and leverage. Focus: Institutional deep dive triggered by FilingDesk: Chief Executive Officer Huang Jack Jiajia open-market buy $3,080,724 (51Talk Online Education Group).
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
- **(7) Altman Z — medium-term bankruptcy risk** (`altman`): run_altman_z
  - Classic Altman Z + Z'' screen for 18–36m distress risk; complements scenario ranges, not a credit rating

## Fundamentals [S1]
- Company: 51Talk Online Education Group
- Sector / industry: Consumer Defensive / Education & Training Services
- Price: 16.93
- 52-week range: $14.66 – $56.13
- Market cap: $101.70M
- Enterprise value: $69.03M
- Shares outstanding: 4.28M
- Beta: 0.748
- Book equity: -$31.36M
- Revenue (latest): $95.60M
- EBITDA (latest): -$13.99M
- Free cash flow (latest): $9.52M
- Operating income: -$14.43M
- Operating margin: -15.1%
- EV / EBITDA: -4.9x
- ROIC: 21.4%
- FCF yield: 9.4%
- Debt / Equity: -0.0937908600950346
- FCF / share: $2.22
- Revenue / share: $22.33

### Capital structure
- Cash: $38.87M
- Short-term debt: $1.76M
- Long-term debt: $1.18M
- Total debt: $2.94M
- Net debt: -$35.93M
- Net debt / EBITDA: 2.6x
- Working capital: -$34.96M
- Total assets: $66.09M
- Total liabilities: $97.34M
- Retained earnings: -$370.40M
- Current ratio: 0.6x

### Growth
- Revenue CAGR: 85.2%
- FCF CAGR: —
- Latest revenue YoY: 88.6%
- Latest FCF YoY: 72.3%

### Market expectations (yfinance, sparse)
- Mean target: —
- Target range: — – —
- Recommendation: none

_Consensus revenue/EBITDA forecasts are often unavailable via free feeds; treat targets as point-in-time only._

### Historical KPIs (multi-year)

| Year | Revenue | OCF | Capex | FCF | EBITDA | LT debt | Cash | Net debt | Net income |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2025 | $95.60M | $11.81M | $2.29M | $9.52M | -$13.99M | $2.94M | $38.87M | -$35.93M | -$16.80M |
| 2024 | $50.69M | $5.83M | $308.00K | $5.52M | -$7.91M | $2.68M | $27.76M | -$25.07M | -$7.24M |
| 2023 | $27.11M | $559.00K | $287.00K | $272.00K | -$13.56M | $631.00K | $21.30M | -$20.67M | -$15.03M |
| 2022 | $15.05M | -$45.70M | $5.00K | -$45.71M | -$12.26M | $734.00K | $18.19M | -$17.45M | -$42.56M |

## Charts

### Revenue & FCF history
![Revenue & FCF history](/charts/COE_valuation_revenue_fcf.png)

### DCF scenario prices
![DCF scenario prices](/charts/COE_valuation_dcf_scenarios.png)

### Base-case FCF path
![Base-case FCF path](/charts/COE_valuation_base_fcf_path.png)

### EV/EBITDA scenario prices
![EV/EBITDA scenario prices](/charts/COE_valuation_ev_ebitda_scenarios.png)

### Headwind/tailwind price ranges
![Headwind/tailwind price ranges](/charts/COE_valuation_scenario_ranges.png)

## DCF valuation (base / bull / bear) [S2]

> Simplified revenue->FCF DCF. Not investment advice; assumptions are editable heuristics.

- Spot price: $16.93
- Base revenue: $95.60M
- Shares: 4,280,532
- Net debt (Debt−Cash): -$35.93M

| Scenario | Growth | FCF margin | WACC | Term. g | Equity value | Share price | Upside |
|----------|--------|------------|------|---------|--------------|-------------|--------|
| bear | 25.0% | 8.0% | 12.0% | 1.5% | $216.80M | $50.65 | 199.2% |
| base | 35.0% | 10.0% | 10.0% | 2.5% | $489.90M | $114.45 | 576.0% |
| bull | 42.0% | 13.0% | 9.0% | 3.0% | $980.64M | $229.09 | 1253.2% |

### Assumption notes
- Base revenue growth seeded from historical rate (88.6%).


### Base-case projected FCF

- Year 1: revenue $129.06M, FCF $12.85M (PV $11.68M)
- Year 2: revenue $174.23M, FCF $17.35M (PV $14.34M)
- Year 3: revenue $235.21M, FCF $23.42M (PV $17.60M)
- Year 4: revenue $317.54M, FCF $31.62M (PV $21.60M)
- Year 5: revenue $428.68M, FCF $42.69M (PV $26.51M)
- Terminal value $583.40M (PV $362.25M)

## Valuation — EV/EBITDA scenarios [S3]

> Priced-in model: implied price = (EBITDA × EV/EBITDA − net debt) ÷ shares. Not a forecast.

- Spot: $16.93
- Net debt used: -$35.93M

| Scenario | EBITDA | EV/EBITDA | Implied EV | Equity value | Implied price |
|---|---:|---:|---:|---:|---:|
| bear | $700.00M | 6.0x | $4.20B | $4.24B | $989.58 |
| base | $1.00B | 8.0x | $8.00B | $8.04B | $1877.32 |
| bull | $1.20B | 10.0x | $12.00B | $12.04B | $2811.78 |

- EBITDA missing or non-positive; scenarios use placeholder $1B EBITDA — edit before relying on prices.
- No current EV/EBITDA; defaulted base multiple to 8.0x.

## Scenario price ranges (headwinds & tailwinds) [S29]

> Medium-term (18–36 months (medium / medium-long term)) driver → EV/EBITDA bridge. Distinct from the FCF DCF path. Not investment advice.

- Spot: $16.93
- Anchor multiple: 8.0x (driver_ev_ebitda_bridge)
- Anchor EBITDA: $1.00B
- Probability-weighted midpoint: **$2146.50** (heuristic weights, not a rating)
- Driver extraction: `rules`

### Headwinds (bear-case fuel)

- **Balance-sheet / refinancing pressure** — sector=Consumer Defensive industry=Education & Training Services revenue=95601000.0 ebitda=-13995000.0 fcf=9520000.0 net_debt=-35928000.0 nd_ebitda=2.567202572347267 target=None re _(source: fundamentals)_
- **Competitive / pricing pressure** — 51Talk Online Education Group Sponsored ADR... - stockrow 51Talk Online Education Group reported its third quarter 2025 financial results, highlighting key metrics such as revenue  _(source: web)_
- **Margin / cost headwind** — Rare Earth Archives - MINING.COM 3 days ago · Algae breakthrough could double rare earth concentrations Researchers found using algae is a cleaner way to concentrate rare earths an _(source: web)_

### Tailwinds (bull-case fuel)

- **Positive free cash flow** — FCF $9.52M (yield 9.4%) _(source: fundamentals)_
- **Revenue growth momentum** — Latest revenue YoY ≈ 88.6% _(source: fundamentals)_
- **Product / pricing power** — sector=Consumer Defensive industry=Education & Training Services revenue=95601000.0 ebitda=-13995000.0 fcf=9520000.0 net_debt=-35928000.0 nd_ebitda=2.567202572347267 target=None re _(source: fundamentals)_
- **Multiple re-rating / Street upgrades** — Why Stanley Black & Decker Stock Popped Today Key Points Wolfe Research analyst Nigel Coe upgraded Stanley stock this morning. After two years of declining sales, Coe thinks the st _(source: web)_
- **Growth / execution upside** — 51Talk Online Education Group Sponsored ADR... - stockrow 51Talk Online Education Group reported its third quarter 2025 financial results, highlighting key metrics such as revenue  _(source: web)_
- **Contract / backlog wins** — 51Talk Online Education stock (KYG3323L1005): Insider equity moves draw focus to COE on NYSE June 2, 2026 - New York-listed 51Talk Online Education saw fresh insider activity as di _(source: web)_

### Price ranges by case

| Case | Prob. | Metric vs TTM | Multiple | Price low | Mid | High | Upside vs spot |
|---|---:|---:|---:|---:|---:|---:|---:|
| bear | 0.18 | 0.78x | 5.6x | $926.78 | $1028.83 | $1130.87 | +5977% |
| base | 0.44 | 1.06x | 8.0x | $1850.78 | $1989.46 | $2128.13 | +11651% |
| bull | 0.38 | 1.21x | 10.1x | $2572.82 | $2857.76 | $3142.70 | +16780% |

#### Bear — headwinds dominate

Headwinds bite: weaker operating trajectory and multiple compression. Equity duration shrinks if cash generation fails to offset leverage / competitive pressure.

- **Range:** $926.78 – $1130.87 (mid $1028.83) · EBITDA $780.00M · multiple 5.6x
- Driver: **Balance-sheet / refinancing pressure** — sector=Consumer Defensive industry=Education & Training Services revenue=95601000.0 ebitda=-13995000.0 fcf=9520000.0 net_debt=-35928000.0 nd_ebitda=2.5672025723
- Driver: **Competitive / pricing pressure** — 51Talk Online Education Group Sponsored ADR... - stockrow 51Talk Online Education Group reported its third quarter 2025 financial results, highlighting key metr
- Driver: **Margin / cost headwind** — Rare Earth Archives - MINING.COM 3 days ago · Algae breakthrough could double rare earth concentrations Researchers found using algae is a cleaner way to concen

#### Base — mixed execution

Balanced path: some tailwinds offset headwinds. Operating scale roughly holds with modest repair/normalization; valuation stays near the current EV/EBITDA anchor.

- **Range:** $1850.78 – $2128.13 (mid $1989.46) · EBITDA $1.06B · multiple 8.0x
- Driver: **Positive free cash flow** — FCF $9.52M (yield 9.4%)
- Driver: **Revenue growth momentum** — Latest revenue YoY ≈ 88.6%
- Driver: **Balance-sheet / refinancing pressure** — sector=Consumer Defensive industry=Education & Training Services revenue=95601000.0 ebitda=-13995000.0 fcf=9520000.0 net_debt=-35928000.0 nd_ebitda=2.5672025723
- Driver: **Competitive / pricing pressure** — 51Talk Online Education Group Sponsored ADR... - stockrow 51Talk Online Education Group reported its third quarter 2025 financial results, highlighting key metr

#### Bull — tailwinds dominate

Tailwinds compound: operating improvement plus a re-rating toward peer or recovery multiples as balance-sheet and growth narratives improve.

- **Range:** $2572.82 – $3142.70 (mid $2857.76) · EBITDA $1.21B · multiple 10.1x
- Driver: **Positive free cash flow** — FCF $9.52M (yield 9.4%)
- Driver: **Revenue growth momentum** — Latest revenue YoY ≈ 88.6%
- Driver: **Product / pricing power** — sector=Consumer Defensive industry=Education & Training Services revenue=95601000.0 ebitda=-13995000.0 fcf=9520000.0 net_debt=-35928000.0 nd_ebitda=2.5672025723
- Driver: **Multiple re-rating / Street upgrades** — Why Stanley Black & Decker Stock Popped Today Key Points Wolfe Research analyst Nigel Coe upgraded Stanley stock this morning. After two years of declining sale
- Driver: **Growth / execution upside** — 51Talk Online Education Group Sponsored ADR... - stockrow 51Talk Online Education Group reported its third quarter 2025 financial results, highlighting key metr

### Method notes

- Item 1A risks weighted toward headwinds.
- Current ev_ebitda multiple missing; anchored at 8.0x.
- Mapping follows Gemini/Perplexity-style scenario memos: qualitative drivers → operating metric & multiple paths → share-price ranges over a medium-term horizon.

## Altman Z-score (medium-term bankruptcy risk) [S30]

**Ticker:** COE
**Primary model:** `z_double_prime`
**Z-score:** **-23.55** — Distress zone (Z'')

### Medium-term read (18–36 months)

Elevated medium-term bankruptcy risk under the non-manufacturer Altman model.

### Model scores

| Model | Score | Zone guide |
| --- | ---: | --- |
| Classic public Z | -7.13 | >2.99 safe · 1.81–2.99 grey · <1.81 distress |
| Non-manufacturer Z'' | -23.55 | >2.60 safe · 1.10–2.60 grey · <1.10 distress |

### Inputs (latest statements / market)

| Item | Value |
| --- | ---: |
| Total assets | $66.1M |
| Total liabilities | $97.3M |
| Working capital | $-35.0M |
| Current assets | $60.4M |
| Current liabilities | $95.4M |
| Retained earnings | $-370.4M |
| EBIT / operating income | $-14.4M |
| Sales / revenue | $95.6M |
| Market value of equity | $101.7M |
| Book equity | $-31.4M |

### Ratio components

| Component | Definition | Value |
| --- | --- | ---: |
| X1 | Working capital / Total assets | -0.529 |
| X2 | Retained earnings / Total assets | -5.604 |
| X3 | EBIT / Total assets | -0.218 |
| X4 | Market equity / Total liabilities | 1.045 |
| X4b | Book equity / Total liabilities (Z'') | -0.322 |
| X5 | Sales / Total assets | 1.446 |

### Formulas

- Classic Z = `1.2·X1 + 1.4·X2 + 3.3·X3 + 0.6·X4 + 1.0·X5`
- Z'' = `6.56·X1 + 3.26·X2 + 6.72·X3 + 1.05·X4b`

- _Altman Z is a statistical screen from historical samples — not a forecast or credit rating._
- _Use alongside liquidity, covenants, and refinancing calendar over an 18–36 month horizon._
- _Sector/industry (Consumer Defensive / Education & Training Services) leans non-manufacturing; primary screen uses Z'' when available._

_Not investment advice. Altman thresholds are historical; banks/REITs/financials are poorly suited to these models._

## Web research — web_analysts

- Queries: COE analyst price target, 51Talk Online Education Group stock rating OR consensus OR upgrade OR downgrade, COE Institutional deep dive triggered by FilingDesk: Chief Executive Officer Huang Jack Jiajia open-market buy $3,080,724 (51Talk Online Education Group). analyst
- Unique hits: 16
- Pages fetched: 2/3

### Web synthesis — web_analysts (rule-based fallback — Ollama unavailable)
**Keyword hits:** revenue, margin, segment, service, market

- [HIT] COE Stock Price - 51Talk Online Education Group ADR - MarketWatch | www.marketwatch.com | https://www.marketwatch.com/investing/stock/coe Needham analyst Vincent Yu assigned a Buy rating to China Online Education Group (COE) today and set a price target of $36.00.[...] May.
- [HIT] COE Stock Quote Price and Forecast - CNN | www.cnn.com | https://www.cnn.com/markets/stocks/COE The price of COE shares has increased $0.26 since the market last closed.
- [HIT] 51Talk Online Education Group (COE) Stock Price, News & Analysis | www.marketbeat.com | https://www.marketbeat.com/stocks/NYSE/COE/ Should You Buy or Sell 51Talk Online Education Group Stock?
- | StockStory · via Yahoo Finance | https://finance.yahoo.com/news/5-most-interesting-analyst-questions-054029242.html Stanley Black & Decker’s fourth quarter results were met with a negative market response, as revenue...
- [HIT] The Top 5 Analyst Questions From Hubbell’s Q4 Earnings Call | StockStory · via Yahoo Finance | https://finance.yahoo.com/news/top-5-analyst-questions-hubbell-053739165.html Hubbell’s fourth-quarter results were met with a positive market response, underscoring the strength...
- - stockrow | stockrow.com | https://stockrow.com/COE 51Talk Online Education Group reported its third quarter 2025 financial results, highlighting key metrics such as revenue growth and user engagement.
- The company continues to expand its online education platform, focusing on enhancing user experience and increasing market share.
- [HIT] 51Talk Online Education Group (NYSEAMERICAN...) | GoMarketCap | gomarketcap.com | https://gomarketcap.com/companies/NYSEAMERICAN-COE/51talk-online-education-group 51Talk Online Education Group has a market cap of $175.55M USD (January 2026), ranking #21268 globally and #200 in Singapore.

### Sources found
- [COE Stock Price - 51Talk Online Education Group ADR - MarketWatch](https://www.marketwatch.com/investing/stock/coe)
  - Needham analyst Vincent Yu assigned a Buy rating to China Online Education Group (COE) today and set a price target of $36.00.[...] May. 18, 2021 at 7:11 ...
- [COE Stock Quote Price and Forecast - CNN](https://www.cnn.com/markets/stocks/COE)
  - The price of COE shares has increased $0.26 since the market last closed. This is a 1.56% rise. Closed at $16.93. The stock has since risen ...
- [COE 51Talk Online Education Group - Yahoo Finance](https://finance.yahoo.com/quote/COE/)
  - Target · Ulta · Walmart · Wayfair · Zappos · Shopping guides · Best cordless stick ... NYSE American - Nasdaq Real Time Price • USD. 51Talk Online Education …
- [51Talk Online Education Group (COE) Stock Price, News & Analysis](https://www.marketbeat.com/stocks/NYSE/COE/)
  - Should You Buy or Sell 51Talk Online Education Group Stock? Get The Latest COE Stock Analysis, Price Target, Earnings Estimates, Headlines, ...
- [The 5 Most Interesting Analyst Questions From Stanley Black & Decker’s Q4 Earnin...](https://finance.yahoo.com/news/5-most-interesting-analyst-questions-054029242.html)
  - Stanley Black & Decker’s fourth quarter results were met with a negative market response, as revenue...
- [The Top 5 Analyst Questions From Hubbell’s Q4 Earnings Call](https://finance.yahoo.com/news/top-5-analyst-questions-hubbell-053739165.html)
  - Hubbell’s fourth-quarter results were met with a positive market response, underscoring the strength...
- [5 Revealing Analyst Questions From Carrier Global’s Q4 Earnings Call](https://finance.yahoo.com/news/5-revealing-analyst-questions-carrier-053529400.html)
  - Carrier Global’s fourth quarter results were shaped by persistent softness in its residential and li...
- [Why Stanley Black & Decker Stock Popped Today](https://finance.yahoo.com/news/why-stanley-black-decker-stock-203017219.html)
  - Key Points Wolfe Research analyst Nigel Coe upgraded Stanley stock this morning. After two years of declining sales, Coe thinks the stock looks...
- [51 Talk Online Education Stock Short Interest Report | Benzinga](https://www.benzinga.com/quote/COE/short-interest)
  - 51 Talk Online Education Group Short Interest Report. COEAMEX.Short interest in 51 Talk Online Education Group (AMEX:COE) increased during the last reporting…
- [51Talk Online Education Group Sponsored ADR... - stockrow](https://stockrow.com/COE)
  - 51Talk Online Education Group reported its third quarter 2025 financial results, highlighting key metrics such as revenue growth and user engagement. The com…
- [51Talk Online Education Group (NYSEAMERICAN...) | GoMarketCap](https://gomarketcap.com/companies/NYSEAMERICAN-COE/51talk-online-education-group)
  - 51Talk Online Education Group has a market cap of $175.55M USD (January 2026), ranking #21268 globally and #200 in Singapore.
- [51Talk Online Education Group to Present on the Emerging Growth...](https://finviz.com/news/79042/51talk-online-education-group-to-present-on-the-emerging-growth-conference-on-june-17-2025)
  - 51Talk Online Education Group will be presenting at 9:05 AM Eastern time for 30 minutes. Please register here to ensure you are able to attend the conference…

### Search warnings
- news:51Talk Online Education Group stock rating OR consensus OR upgrade OR downgrade: No results found.

## Web research — web_drivers

- Queries: COE Institutional deep dive triggered by FilingDesk: Chief Executive Officer Huang Jack Jiajia open-market buy $3,080,724 (51Talk Online Education Group)., 51Talk Online Education Group COE outlook OR catalyst OR commodity OR uranium OR rare earth OR vanadium, COE sector drivers OR market demand
- Unique hits: 14
- Pages fetched: 3/3

### Web synthesis — web_drivers (rule-based fallback — Ollama unavailable)
**Keyword hits:** regulation, revenue, margin, supply chain, interest rate, segment, service, market, operations

- It operates through the following geographical segments: China, Hong Kong, Philippines, Singapore, Malaysia, Thailand and Saudi Arabia.
- [HIT] Credit Card, Mortgage, Banking, Auto | Chase Online | Chase.com | www.chase.com | https://www.chase.com/ Chase online; credit cards, mortgages, commercial banking, auto loans, investing & retirement planning, checking and business banking.Open a savings account or open a Certificate of Deposit ( see interest rates ) and start saving your money.
- [HIT] Commodity Price Outlook | The Daily Spark | www.apollo.com | https://www.apollo.com/wealth/insights-news/insights/daily-spark/Commodity-Price-Outlook Jun 15, 2026 · Commodity prices are moving higher across the board, but for different reasons in each segment.
- [HIT] Rare Earth Archives - MINING.COM | www.mining.com | https://www.mining.com/commodity/rare-earth/ 3 days ago · Algae breakthrough could double rare earth concentrations Researchers found using algae is a cleaner way to concentrate rare earths and help the US strengthen critical mineral supply chains.
- [HIT] Commodity Prices | Commodity Market | Markets Insider | markets.businessinsider.com | https://markets.businessinsider.com/commodities?op=1 Get all information on the commodity market.
- [HIT] Center of Excellence for Labor Market Research: Home | coeccc.net | https://coeccc.net/ This collection of 12 sector profiles maps workforce demand across the Far North subregion.
- [HIT] Data Tools - Center of Excellence for Labor Market Research | coeccc.net | https://coeccc.net/data-tools/ This data tool shows projected 2023–2028 employment demand in California.
- [HIT] Labor market research - Bay Area Community College Consortium | coe.baccc.net | https://coe.baccc.net/ Or for any other data or project requests, complete the COE request form, or contact us by phone or email if you have any questions.

### Sources found
- [COE - 51 Talk Online Education Group ADR Stock Price and Quote](https://finviz.com/quote.ashx?t=COE&p=d)
  - 51Talk Online Education Group is a global online education platform focusing on English lessons. It operates through the following geographical segments: Chi…
- [China Online Education Group Announces Receipt of a Non-Binding...](https://www.stocktitan.net/news/COE/china-online-education-group-announces-receipt-of-a-non-binding-ujk4w1i05pua.html)
  - China Online Education Group ("51Talk" or the "Company") (NYSE: COE), a leading online education platform in China, with core expertise in English education,…
- [Credit Card, Mortgage, Banking, Auto | Chase Online | Chase.com](https://www.chase.com/)
  - Chase online; credit cards, mortgages, commercial banking, auto loans, investing & retirement planning, checking and business banking.Open a savings account …
- [Form an LLC Online by Having a Conversation | FilingDesk](https://filingdesk.com/)
  - Form your LLC by describing it in plain English — FilingDesk checks the name, files with the state, gets your EIN, and drafts your operating agreement. One f…
- [51Talk Online Education Group (COE) Q1 2026 Earnings Call Transcript](https://seekingalpha.com/article/4914549-51talk-online-education-group-coe-q1-2026-earnings-call-transcript)
  - Hello, ladies and gentlemen. Thank you for standing by for 51Talk Online Education Group's First Quarter 2026 Earnings Conference Call. [Operator Instruction…
- [Uranium - Wikipedia](https://en.wikipedia.org/wiki/Uranium)
  - Uranium is a chemical element; it has symbol U and atomic number 92. It is a silvery-grey metal in the actinide series of the periodic table. A uranium atom …
- [Commodity Price Outlook | The Daily Spark](https://www.apollo.com/wealth/insights-news/insights/daily-spark/Commodity-Price-Outlook)
  - Jun 15, 2026 · Commodity prices are moving higher across the board, but for different reasons in each segment. Subscribe for daily updates.
- [Rare Earth Archives - MINING.COM](https://www.mining.com/commodity/rare-earth/)
  - 3 days ago · Algae breakthrough could double rare earth concentrations Researchers found using algae is a cleaner way to concentrate rare earths and help the…
- [Commodity Prices | Commodity Market | Markets Insider](https://markets.businessinsider.com/commodities?op=1)
  - Get all information on the commodity market. Find the latest commodity prices including News, Charts, Realtime Quotes and even more about commodities.
- [Center of Excellence for Labor Market Research: Home](https://coeccc.net/)
  - This collection of 12 sector profiles maps workforce demand across the Far North subregion. Each profile covers a priority industry sector, drawing on curren…
- [Data Tools - Center of Excellence for Labor Market Research](https://coeccc.net/data-tools/)
  - This data tool shows projected 2023–2028 employment demand in California. Filter by region, occupation, skill level, career cluster, or sector group. View jo…
- [Labor market research - Bay Area Community College Consortium](https://coe.baccc.net/)
  - Or for any other data or project requests, complete the COE request form, or contact us by phone or email if you have any questions. Marcela Reyes ...

### Search warnings
- news:51Talk Online Education Group COE outlook OR catalyst OR commodity OR uranium OR rare earth OR vanadium: No results found.

## SEC filing [S25]
- Extraction OK: False
- Item 1 chars: 0
- Item 1A chars: 0
- Item 7 chars: 0
- Meta: {'source': 'cache', 'path': 'C:\\DevWork\\equity_research_agent\\data\\filings\\COE_10k.txt'}

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

- **[S1]** COE fundamentals (yfinance)
  - 51Talk Online Education Group: price=16.93, rev=95601000.0, fcf=9520000.0, shares=4280532.0, rev_cagr=0.8520862926062147, ROIC=0.21444601322731663, FCF yield=0.09360511118517365
- **[S2]** COE DCF valuation (dcf)
  - Base share price=114.44814308174645, bull=229.09247777968184, bear=50.64858919987204
- **[S3]** COE EV/EBITDA valuation (multiples)
  - Base implied price=1877.3199219162477, multiple=8.0
- **[S4]** COE Stock Price - 51Talk Online Education Group ADR - MarketWatch (web) — https://www.marketwatch.com/investing/stock/coe
  - Needham analyst Vincent Yu assigned a Buy rating to China Online Education Group (COE) today and set a price target of $36.00.[...] May. 18, 2021 at 7:11 ...
- **[S5]** COE Stock Quote Price and Forecast - CNN (web) — https://www.cnn.com/markets/stocks/COE
  - The price of COE shares has increased $0.26 since the market last closed. This is a 1.56% rise. Closed at $16.93. The stock has since risen ...
- **[S6]** COE 51Talk Online Education Group - Yahoo Finance (web) — https://finance.yahoo.com/quote/COE/
  - Target · Ulta · Walmart · Wayfair · Zappos · Shopping guides · Best cordless stick ... NYSE American - Nasdaq Real Time Price • USD. 51Talk Online Education Group ...
- **[S7]** 51Talk Online Education Group (COE) Stock Price, News & Analysis (web) — https://www.marketbeat.com/stocks/NYSE/COE/
  - Should You Buy or Sell 51Talk Online Education Group Stock? Get The Latest COE Stock Analysis, Price Target, Earnings Estimates, Headlines, ...
- **[S8]** The 5 Most Interesting Analyst Questions From Stanley Black & Decker’s Q4 Earnin... (web) — https://finance.yahoo.com/news/5-most-interesting-analyst-questions-054029242.html
  - Stanley Black & Decker’s fourth quarter results were met with a negative market response, as revenue...
- **[S9]** The Top 5 Analyst Questions From Hubbell’s Q4 Earnings Call (web) — https://finance.yahoo.com/news/top-5-analyst-questions-hubbell-053739165.html
  - Hubbell’s fourth-quarter results were met with a positive market response, underscoring the strength...
- **[S10]** 5 Revealing Analyst Questions From Carrier Global’s Q4 Earnings Call (web) — https://finance.yahoo.com/news/5-revealing-analyst-questions-carrier-053529400.html
  - Carrier Global’s fourth quarter results were shaped by persistent softness in its residential and li...
- **[S11]** Why Stanley Black & Decker Stock Popped Today (web) — https://finance.yahoo.com/news/why-stanley-black-decker-stock-203017219.html
  - Key Points Wolfe Research analyst Nigel Coe upgraded Stanley stock this morning. After two years of declining sales, Coe thinks the stock looks...
- **[S12]** COE Stock Quote Price and Forecast | CNN (web_page) — https://www.cnn.com/markets/stocks/COE
  - COE Stock Quote Price and Forecast | CNN COE 51Talk Online Education Group Sponsored ADR 51Talk Online Education Group Sponsored ADR COE Facts Insights Learn 1d 5d 1m 6m YTD 1y …
- **[S13]** 51Talk Online Education Group (COE) Stock Price, News, Quote & History - Yahoo Finance (web_page) — https://finance.yahoo.com/quote/COE/
  - 51Talk Online Education Group (COE) Stock Price, News, Quote & History - Yahoo Finance Oops, something went wrong Skip to navigation Skip to main content Skip to right column We…
- **[S14]** COE - 51 Talk Online Education Group ADR Stock Price and Quote (web) — https://finviz.com/quote.ashx?t=COE&p=d
  - 51Talk Online Education Group is a global online education platform focusing on English lessons. It operates through the following geographical segments: China, Hong Kong, Phili…
- **[S15]** China Online Education Group Announces Receipt of a Non-Binding... (web) — https://www.stocktitan.net/news/COE/china-online-education-group-announces-receipt-of-a-non-binding-ujk4w1i05pua.html
  - China Online Education Group ("51Talk" or the "Company") (NYSE: COE), a leading online education platform in China, with core expertise in English education, announced that its …
- **[S16]** Credit Card, Mortgage, Banking, Auto | Chase Online | Chase.com (web) — https://www.chase.com/
  - Chase online; credit cards, mortgages, commercial banking, auto loans, investing & retirement planning, checking and business banking.Open a savings account or open a Certificat…
- **[S17]** Form an LLC Online by Having a Conversation | FilingDesk (web) — https://filingdesk.com/
  - Form your LLC by describing it in plain English — FilingDesk checks the name, files with the state, gets your EIN, and drafts your operating agreement. One flat price, no upsell…
- **[S18]** 51Talk Online Education Group (COE) Q1 2026 Earnings Call Transcript (web) — https://seekingalpha.com/article/4914549-51talk-online-education-group-coe-q1-2026-earnings-call-transcript
  - Hello, ladies and gentlemen. Thank you for standing by for 51Talk Online Education Group's First Quarter 2026 Earnings Conference Call. [Operator Instructions] Today's conferenc…
- **[S19]** Uranium - Wikipedia (web) — https://en.wikipedia.org/wiki/Uranium
  - Uranium is a chemical element; it has symbol U and atomic number 92. It is a silvery-grey metal in the actinide series of the periodic table. A uranium atom has 92 protons and 9…
- **[S20]** Commodity Price Outlook | The Daily Spark (web) — https://www.apollo.com/wealth/insights-news/insights/daily-spark/Commodity-Price-Outlook
  - Jun 15, 2026 · Commodity prices are moving higher across the board, but for different reasons in each segment. Subscribe for daily updates.
- **[S21]** Rare Earth Archives - MINING.COM (web) — https://www.mining.com/commodity/rare-earth/
  - 3 days ago · Algae breakthrough could double rare earth concentrations Researchers found using algae is a cleaner way to concentrate rare earths and help the US strengthen criti…
- **[S22]** COE - 51 Talk Online Education Group ADR Stock Price and Quote (web_page) — https://finviz.com/quote.ashx?t=COE&p=d
  - COE - 51 Talk Online Education Group ADR Stock Price and Quote Home News Screener Charts Maps Groups Portfolio Insider Futures Forex Crypto Calendar Pricing Theme Help Login Reg…
- **[S23]** China Online Education Group Announces Receipt of a Non-Binding Proposal to Acquire Mainland China Business of the Company | COE Stock News (web_page) — https://www.stocktitan.net/news/COE/china-online-education-group-announces-receipt-of-a-non-binding-ujk4w1i05pua.html
  - China Online Education Group Announces Receipt of a Non-Binding Proposal to Acquire Mainland China Business of the Company | COE Stock News Home News COE China Online Education …
- **[S24]** Credit Card, Mortgage, Banking, Auto | Chase Online | Chase.com (web_page) — https://www.chase.com/
  - Credit Card, Mortgage, Banking, Auto | Chase Online | Chase.com Skip to main content Chase home page Username Password Show Password Remember username Use token Sign in Or Passw…
- **[S25]** COE 10-K (sec)
  - Item 1 chars=0, Item 1A chars=0, Item 7 chars=0, ok=False, source=cache
- **[S26]** Item 1 Business summary (nlp)
  - ### Item 1 — Business No Item 1 Business text extracted. 
- **[S27]** Item 1A summary (nlp)
  - ### Item 1A — Risk Factors No text extracted. 
- **[S28]** Item 7 summary (nlp)
  - ### Item 7 — MD&A No text extracted. 
- **[S29]** COE scenario price ranges (scenarios)
  - ok=True; base mid=1989.4555162769489; headwinds=3; tailwinds=6
- **[S30]** COE Altman Z-score (altman)
  - ok=True; model=z_double_prime; Z=-23.54543902075005; zone=distress

## Self-critique

_Automated review (heuristic)._

### Strengths
- Combines local fundamentals, optional DCF scenarios, and cited sources where available.
- Keeps a non-advisory framing for local research drafts.

### Issues & gaps
- Base-case upside vs spot is extreme (>150%); check growth/margin/WACC assumptions for optimism bias.

### Caution for readers
- Treat scenario prices as sensitivity output, not a forecast.
- Re-check primary filings and fresh market data before any decision.



---

# Template: Full diligence (`deep`)

# COE — Planned Research Report

> Not investment advice. Local research draft only.

**Goal:** Institutional deep dive triggered by FilingDesk: Chief Executive Officer Huang Jack Jiajia open-market buy $3,080,724 (51Talk Online Education Group).
**Mode:** deep
**Template:** deep
**Planner:** template

## Plan executed

- **Fundamentals & ratios** (`fundamentals`): get_fundamentals
  - Revenue, FCF, shares, growth rates, ROIC, FCF yield, debt/equity. Focus: Institutional deep dive triggered by FilingDesk: Chief Executive Officer Huang Jack Jiajia open-market buy $3,080,724 (51Talk Online Education Group).
- **DCF valuation (base / bull / bear)** (`valuation`): run_dcf
  - Intrinsic value from growth, FCF margin, and WACC assumptions. Focus: Institutional deep dive triggered by FilingDesk: Chief Executive Officer Huang Jack Jiajia open-market buy $3,080,724 (51Talk Online Education Group).
- **Put income screen** (`options`): screen_puts
  - ~30–60 DTE OTM puts targeting ~10–15% annualized premium
- **News, analysts & market drivers** (`web_research`): search_web
  - Street targets, recent news, sector/commodity drivers via web search + page fetch. Focus: Institutional deep dive triggered by FilingDesk: Chief Executive Officer Huang Jack Jiajia open-market buy $3,080,724 (51Talk Online Education Group).
- **SEC 10-K intake** (`sec_fetch`): fetch_10k
  - Latest 10-K; extract Item 1 (Business), Item 1A, and Item 7
- **Business overview (Item 1)** (`business`): summarize_item_1
  - Company setup from 10-K Item 1 Business
- **Risk factors (Item 1A)** (`risks`): summarize_item_1a
  - Qualitative risks from the filing
- **MD&A (Item 7)** (`mda`): summarize_item_7
  - Management discussion, tone, guidance cues
- **Altman Z — medium-term bankruptcy risk** (`altman`): run_altman_z
  - Distress screen (classic Z / Z'') for medium-term solvency risk

## Fundamentals [S1]
- Company: 51Talk Online Education Group
- Sector / industry: Consumer Defensive / Education & Training Services
- Price: 16.93
- 52-week range: $14.66 – $56.13
- Market cap: $101.70M
- Enterprise value: $69.03M
- Shares outstanding: 4.28M
- Beta: 0.748
- Book equity: -$31.36M
- Revenue (latest): $95.60M
- EBITDA (latest): -$13.99M
- Free cash flow (latest): $9.52M
- Operating income: -$14.43M
- Operating margin: -15.1%
- EV / EBITDA: -4.9x
- ROIC: 21.4%
- FCF yield: 9.4%
- Debt / Equity: -0.0937908600950346
- FCF / share: $2.22
- Revenue / share: $22.33

### Capital structure
- Cash: $38.87M
- Short-term debt: $1.76M
- Long-term debt: $1.18M
- Total debt: $2.94M
- Net debt: -$35.93M
- Net debt / EBITDA: 2.6x
- Working capital: -$34.96M
- Total assets: $66.09M
- Total liabilities: $97.34M
- Retained earnings: -$370.40M
- Current ratio: 0.6x

### Growth
- Revenue CAGR: 85.2%
- FCF CAGR: —
- Latest revenue YoY: 88.6%
- Latest FCF YoY: 72.3%

### Market expectations (yfinance, sparse)
- Mean target: —
- Target range: — – —
- Recommendation: none

_Consensus revenue/EBITDA forecasts are often unavailable via free feeds; treat targets as point-in-time only._

### Historical KPIs (multi-year)

| Year | Revenue | OCF | Capex | FCF | EBITDA | LT debt | Cash | Net debt | Net income |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2025 | $95.60M | $11.81M | $2.29M | $9.52M | -$13.99M | $2.94M | $38.87M | -$35.93M | -$16.80M |
| 2024 | $50.69M | $5.83M | $308.00K | $5.52M | -$7.91M | $2.68M | $27.76M | -$25.07M | -$7.24M |
| 2023 | $27.11M | $559.00K | $287.00K | $272.00K | -$13.56M | $631.00K | $21.30M | -$20.67M | -$15.03M |
| 2022 | $15.05M | -$45.70M | $5.00K | -$45.71M | -$12.26M | $734.00K | $18.19M | -$17.45M | -$42.56M |

## Charts

### Revenue & FCF history
![Revenue & FCF history](/charts/COE_deep_revenue_fcf.png)

### DCF scenario prices
![DCF scenario prices](/charts/COE_deep_dcf_scenarios.png)

### Base-case FCF path
![Base-case FCF path](/charts/COE_deep_base_fcf_path.png)

## DCF valuation (base / bull / bear) [S2]

> Simplified revenue->FCF DCF. Not investment advice; assumptions are editable heuristics.

- Spot price: $16.93
- Base revenue: $95.60M
- Shares: 4,280,532
- Net debt (Debt−Cash): -$35.93M

| Scenario | Growth | FCF margin | WACC | Term. g | Equity value | Share price | Upside |
|----------|--------|------------|------|---------|--------------|-------------|--------|
| bear | 25.0% | 8.0% | 12.0% | 1.5% | $216.80M | $50.65 | 199.2% |
| base | 35.0% | 10.0% | 10.0% | 2.5% | $489.90M | $114.45 | 576.0% |
| bull | 42.0% | 13.0% | 9.0% | 3.0% | $980.64M | $229.09 | 1253.2% |

### Assumption notes
- Base revenue growth seeded from historical rate (88.6%).


### Base-case projected FCF

- Year 1: revenue $129.06M, FCF $12.85M (PV $11.68M)
- Year 2: revenue $174.23M, FCF $17.35M (PV $14.34M)
- Year 3: revenue $235.21M, FCF $23.42M (PV $17.60M)
- Year 4: revenue $317.54M, FCF $31.62M (PV $21.60M)
- Year 5: revenue $428.68M, FCF $42.69M (PV $26.51M)
- Terminal value $583.40M (PV $362.25M)

## Altman Z-score (medium-term bankruptcy risk) [S14]

**Ticker:** COE
**Primary model:** `z_double_prime`
**Z-score:** **-23.55** — Distress zone (Z'')

### Medium-term read (18–36 months)

Elevated medium-term bankruptcy risk under the non-manufacturer Altman model.

### Model scores

| Model | Score | Zone guide |
| --- | ---: | --- |
| Classic public Z | -7.13 | >2.99 safe · 1.81–2.99 grey · <1.81 distress |
| Non-manufacturer Z'' | -23.55 | >2.60 safe · 1.10–2.60 grey · <1.10 distress |

### Inputs (latest statements / market)

| Item | Value |
| --- | ---: |
| Total assets | $66.1M |
| Total liabilities | $97.3M |
| Working capital | $-35.0M |
| Current assets | $60.4M |
| Current liabilities | $95.4M |
| Retained earnings | $-370.4M |
| EBIT / operating income | $-14.4M |
| Sales / revenue | $95.6M |
| Market value of equity | $101.7M |
| Book equity | $-31.4M |

### Ratio components

| Component | Definition | Value |
| --- | --- | ---: |
| X1 | Working capital / Total assets | -0.529 |
| X2 | Retained earnings / Total assets | -5.604 |
| X3 | EBIT / Total assets | -0.218 |
| X4 | Market equity / Total liabilities | 1.045 |
| X4b | Book equity / Total liabilities (Z'') | -0.322 |
| X5 | Sales / Total assets | 1.446 |

### Formulas

- Classic Z = `1.2·X1 + 1.4·X2 + 3.3·X3 + 0.6·X4 + 1.0·X5`
- Z'' = `6.56·X1 + 3.26·X2 + 6.72·X3 + 1.05·X4b`

- _Altman Z is a statistical screen from historical samples — not a forecast or credit rating._
- _Use alongside liquidity, covenants, and refinancing calendar over an 18–36 month horizon._
- _Sector/industry (Consumer Defensive / Education & Training Services) leans non-manufacturing; primary screen uses Z'' when available._

_Not investment advice. Altman thresholds are historical; banks/REITs/financials are poorly suited to these models._

## Web research — web_research

- Queries: Institutional deep dive triggered by FilingDesk: Chief Executive Officer Huang Jack Jiajia open-market buy $3,080,724 (51Talk Online Education Group).
- Unique hits: 3
- Pages fetched: 3/3

### Web synthesis — web_research (rule-based fallback — Ollama unavailable)
**Keyword hits:** revenue, margin, interest rate, segment, product, service, market

- It operates through the following geographical segments: China, Hong Kong, Philippines, Singapore, Malaysia, Thailand and Saudi Arabia.
- [HIT] Credit Card, Mortgage, Banking, Auto | Chase Online | Chase.com | www.chase.com | https://www.chase.com/ Chase online; credit cards, mortgages, commercial banking, auto loans, investing & retirement planning, checking and business banking.Open a savings account or open a Certificate of Deposit ( see interest rates ) and start saving your money.
- [PAGE] COE - 51 Talk Online Education Group ADR Stock Price and Quote | https://finviz.com/stock?t=COE&p=d COE - 51 Talk Online Education Group ADR Stock Price and Quote Home News Screener Charts Maps Groups Portfolio Insider Futures Forex Crypto Calendar Pricing Theme Help Login Register C COE 51 Talk Online Education Group ADR Last Close 16.93 Jul 29 • 3:45 PM ET Dollar change +0.26 Percentage change (1.56%) Aftermarket Close 16.93 Aftermarket • 7:34 PM ET Dollar change 0.00 Percentage change (0.00%) Overview Compare Short Interest Financials Options Filings Latest Filings Consumer Defensive Education & Training Services Singapore Micro AMEX Peers : GOTU LGCY FC EDU APEI LINC LAUR LRN PRDO LOPE Scroll to Statements Index - Market Cap 72.46M Enterprise Value 39.92M Income -16.63M Sales 108.88M Book/sh -5.61 Cash/sh 8.30 Dividend Est.
- - - Insider Own 11.09% Insider Trans - Inst Own 6.50% Inst Trans -3.25% ROA -30.02% ROE - ROIC - Gross Margin 73.39% Oper.
- Margin -12.43% Profit Margin -15.28% SMA20 3.35% SMA50 -12.85% SMA200 -41.10% Trades Shs Outstand 4.26M Shs Float 3.81M Short Float 0.28% Short Ratio 0.78 Short Interest 0.01M 52W High 56.13 -69.84% 52W Low 14.66 15.48% Volatility 6.27% 7.06% ATR (14) 1.26 RSI (14) 48.62 Beta 0.81 Rel Volume 0.67 Avg Volume 13.81K Volume 9,300 Perf Week 8.53% Perf Month 12.49% Perf Quarter -39.41% Perf Half Y -34.96% Perf YTD -46.98% Perf Year -41.42% Perf 3Y 91.73% Perf 5Y 39.69% Perf 10Y -78.93% Recom 1.00 Target Price 55.88 Prev Close 16.67 Price 16.93 Change 1.56% Date Action Analyst Rating Change Price Target Change Jul-26-21 Downgrade The Benchmark Company Buy → Hold Jul-22-21 Reiterated Needham Buy $36 → $32 Mar-10-20 Initiated Needham Buy $36 Jan-10-20 Initiated The Benchmark Company Buy $14 Jul-07-26 08:00PM 51Talk Marks 15th Anniversary with Global Curriculum Upgrade to Enhance Children's English Communication Skills (PR Newswire) Jun-12-26 03:00PM 51 Talk Online Education Group (COE) Q1 2026 Earnings Call Highlights: Surging Revenues Amid ...
- Start yours → F FilingDesk Product preview I'm opening a pottery studio with my sister — thinking "ClayNest".
- The first formation service built for how people start companies now.

### Sources found
- [COE - 51 Talk Online Education Group ADR Stock Price and Quote](https://finviz.com/stock?t=COE&p=d)
  - 51Talk Online Education Group is a global online education platform focusing on English lessons. It operates through the following geographical segments: Chi…
- [Form an LLC Online by Having a Conversation | FilingDesk](https://filingdesk.com/)
  - Form your LLC by describing it in plain English — FilingDesk checks the name, files with the state, gets your EIN, and drafts your operating agreement. One f…
- [Credit Card, Mortgage, Banking, Auto | Chase Online | Chase.com](https://www.chase.com/)
  - Chase online; credit cards, mortgages, commercial banking, auto loans, investing & retirement planning, checking and business banking.Open a savings account …

### Search warnings
- news:Institutional deep dive triggered by FilingDesk: Chief Executive Officer Huang Jack Jiajia open-market buy $3,080,724 (51Talk Online Education Group).: No results found.

## Put opportunities (heuristic) [S3]
- Expiration: None (DTE None)
- Candidates: 0
- ATM IV (est.): —
- IV rank: — (0 local samples)
- HV rank (20d realized): —


_Note: No options chain available_

## SEC filing [S10]
- Extraction OK: False
- Item 1 chars: 0
- Item 1A chars: 0
- Item 7 chars: 0
- Meta: {'source': 'cache', 'path': 'C:\\DevWork\\equity_research_agent\\data\\filings\\COE_10k.txt'}

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

- **[S1]** COE fundamentals (yfinance)
  - 51Talk Online Education Group: price=16.93, rev=95601000.0, fcf=9520000.0, shares=4280532.0, rev_cagr=0.8520862926062147, ROIC=0.21444601322731663, FCF yield=0.09360511118517365
- **[S2]** COE DCF valuation (dcf)
  - Base share price=114.44814308174645, bull=229.09247777968184, bear=50.64858919987204
- **[S3]** COE put screen (yfinance_options)
  - Expiration None (DTE None): 0 candidates; IV=None, IV rank=None, HV rank=None. No options chain available
- **[S4]** COE - 51 Talk Online Education Group ADR Stock Price and Quote (web) — https://finviz.com/stock?t=COE&p=d
  - 51Talk Online Education Group is a global online education platform focusing on English lessons. It operates through the following geographical segments: China, Hong Kong, Phili…
- **[S5]** Form an LLC Online by Having a Conversation | FilingDesk (web) — https://filingdesk.com/
  - Form your LLC by describing it in plain English — FilingDesk checks the name, files with the state, gets your EIN, and drafts your operating agreement. One flat price, no upsell…
- **[S6]** Credit Card, Mortgage, Banking, Auto | Chase Online | Chase.com (web) — https://www.chase.com/
  - Chase online; credit cards, mortgages, commercial banking, auto loans, investing & retirement planning, checking and business banking.Open a savings account or open a Certificat…
- **[S7]** COE - 51 Talk Online Education Group ADR Stock Price and Quote (web_page) — https://finviz.com/stock?t=COE&p=d
  - COE - 51 Talk Online Education Group ADR Stock Price and Quote Home News Screener Charts Maps Groups Portfolio Insider Futures Forex Crypto Calendar Pricing Theme Help Login Reg…
- **[S8]** Form an LLC Online by Having a Conversation | FilingDesk (web_page) — https://filingdesk.com/
  - Form an LLC Online by Having a Conversation | FilingDesk Live in Wyoming, Florida & Delaware — more states on the way The conversation is the paperwork. Tell us about your busin…
- **[S9]** Credit Card, Mortgage, Banking, Auto | Chase Online | Chase.com (web_page) — https://www.chase.com/
  - Credit Card, Mortgage, Banking, Auto | Chase Online | Chase.com Skip to main content Chase home page Username Password Show Password Remember username Use token Sign in Or Passw…
- **[S10]** COE 10-K (sec)
  - Item 1 chars=0, Item 1A chars=0, Item 7 chars=0, ok=False, source=cache
- **[S11]** Item 1 Business summary (nlp)
  - ### Item 1 — Business No Item 1 Business text extracted. 
- **[S12]** Item 1A summary (nlp)
  - ### Item 1A — Risk Factors No text extracted. 
- **[S13]** Item 7 summary (nlp)
  - ### Item 7 — MD&A No text extracted. 
- **[S14]** COE Altman Z-score (altman)
  - ok=True; model=z_double_prime; Z=-23.54543902075005; zone=distress

## Self-critique

_Automated review (heuristic)._

### Strengths
- Combines local fundamentals, optional DCF scenarios, and cited sources where available.
- Keeps a non-advisory framing for local research drafts.

### Issues & gaps
- Base-case upside vs spot is extreme (>150%); check growth/margin/WACC assumptions for optimism bias.

### Caution for readers
- Treat scenario prices as sensitivity output, not a forecast.
- Re-check primary filings and fresh market data before any decision.



---

# Template: Options income (`income`)

# COE — Planned Research Report

> Not investment advice. Local research draft only.

**Goal:** Institutional deep dive triggered by FilingDesk: Chief Executive Officer Huang Jack Jiajia open-market buy $3,080,724 (51Talk Online Education Group).
**Mode:** deep
**Template:** income
**Planner:** template

## Plan executed

- **Fundamentals check** (`fundamentals`): get_fundamentals
  - Liquidity, leverage, and volatility context for income overlays. Focus: Institutional deep dive triggered by FilingDesk: Chief Executive Officer Huang Jack Jiajia open-market buy $3,080,724 (51Talk Online Education Group).
- **Put income screen** (`options`): screen_puts
  - ~30–60 DTE OTM puts targeting ~10–15% annualized premium
- **Recent news & catalysts** (`web_research`): search_web
  - Near-term events that could spoil a short-premium thesis

## Fundamentals [S1]
- Company: 51Talk Online Education Group
- Sector / industry: Consumer Defensive / Education & Training Services
- Price: 16.93
- 52-week range: $14.66 – $56.13
- Market cap: $101.70M
- Enterprise value: $69.03M
- Shares outstanding: 4.28M
- Beta: 0.748
- Book equity: -$31.36M
- Revenue (latest): $95.60M
- EBITDA (latest): -$13.99M
- Free cash flow (latest): $9.52M
- Operating income: -$14.43M
- Operating margin: -15.1%
- EV / EBITDA: -4.9x
- ROIC: 21.4%
- FCF yield: 9.4%
- Debt / Equity: -0.0937908600950346
- FCF / share: $2.22
- Revenue / share: $22.33

### Capital structure
- Cash: $38.87M
- Short-term debt: $1.76M
- Long-term debt: $1.18M
- Total debt: $2.94M
- Net debt: -$35.93M
- Net debt / EBITDA: 2.6x
- Working capital: -$34.96M
- Total assets: $66.09M
- Total liabilities: $97.34M
- Retained earnings: -$370.40M
- Current ratio: 0.6x

### Growth
- Revenue CAGR: 85.2%
- FCF CAGR: —
- Latest revenue YoY: 88.6%
- Latest FCF YoY: 72.3%

### Market expectations (yfinance, sparse)
- Mean target: —
- Target range: — – —
- Recommendation: none

_Consensus revenue/EBITDA forecasts are often unavailable via free feeds; treat targets as point-in-time only._

### Historical KPIs (multi-year)

| Year | Revenue | OCF | Capex | FCF | EBITDA | LT debt | Cash | Net debt | Net income |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2025 | $95.60M | $11.81M | $2.29M | $9.52M | -$13.99M | $2.94M | $38.87M | -$35.93M | -$16.80M |
| 2024 | $50.69M | $5.83M | $308.00K | $5.52M | -$7.91M | $2.68M | $27.76M | -$25.07M | -$7.24M |
| 2023 | $27.11M | $559.00K | $287.00K | $272.00K | -$13.56M | $631.00K | $21.30M | -$20.67M | -$15.03M |
| 2022 | $15.05M | -$45.70M | $5.00K | -$45.71M | -$12.26M | $734.00K | $18.19M | -$17.45M | -$42.56M |

## Charts

### Revenue & FCF history
![Revenue & FCF history](/charts/COE_income_revenue_fcf.png)

## Web research — web_research

- Queries: COE news, 51Talk Online Education Group earnings OR catalyst
- Unique hits: 12
- Pages fetched: 2/3

### Web synthesis — web_research (rule-based fallback — Ollama unavailable)
**Keyword hits:** revenue, segment, service, market, network

- | Benzinga | www.benzinga.com | https://www.benzinga.com/quote/COE/earnings Discover 51 Talk Online Education stock earnings estimates, EPS, and revenue analysis with Benzinga.
- | MarketWatch | www.marketwatch.com | https://www.marketwatch.com/investing/stock/coe 51Talk Online Education Group is a global online education platform focusing on English lessons.
- It operates through the following geographical segments: China, Hong Kong, Philippines, Singapore, Malaysia, Thailand and Saudi Arabia.
- [HIT] Q1 2025 51Talk Online Education Group Earnings Call Transcript | www.gurufocus.com | https://www.gurufocus.com/stock/COE/transcripts/2917268 51Talk Online Education Group at OTC Markets and Deutsche Bank dbVIC ADR Virtual Investor Conference Transcript.Thank you for standing by for 51Talk Online Education Group's first quarter 2025 earnings conference call.
- | www.marketbeat.com | https://www.marketbeat.com/stocks/NYSE/COE/news/ 51Talk Online Education Group (COE) Q1 2026 Earnings Call Transcript.51Talk Online Education Group Announces Engagement of Ernst & Young LLP, as the Company's Independent Registered Public Accounting Firm.
- Nationally ranked for accessible professors, internships, career services and alumni network by The Princeton Review, all Kohawks have access to the resources and personal instruction to build connections and a full resume before graduation.
- The superior services on campus allow students to quickly excel and improve their lives personally and professionally, as well as impact the world around them.

### Sources found
- [Wesley Coe](https://en.wikipedia.org/wiki/Wesley_Coe)
  - Wesley William Coe Jr. (May 8, 1879 – December 24, 1926), sometimes listed as William Wesley Coe Jr., was an American track and field athlete who competed pr…
- [Best for social mobility in Iowa | Coe College](https://www.coe.edu/why-coe/news/coe-news/coe-named-top-performer-social-mobility-iowa-us-news-world-report)
  - Coe is the highest ranked college or university in Iowa on the Social Mobility list. U.S. News & World Report also named Coe its No. 142 National Liberal Art…
- [Singapore mainstream car COE down 9% to S$85,000, lowest level in...](https://www.businesstimes.com.sg/singapore/mainstream-car-coe-down-9-2-s85000-lowest-level-nearly-year)
  - The last time Category A COE premiums went lower than this current round's S$85,000 was in March 2024’s first round of bidding, when it was S$83,000.
- [coE-News: November 15, 2006 VOL. 2 ISSUE 3 - News](https://education.ufl.edu/news/2006/11/15/coe-news-november-15-2006-vol-2-issue-3/)
  - 15, 2006. You’re reading coE-News, an electronic newsletter produced monthly during the academic year by the College of Education News & Publications Office …
- [Category A COE overtakes Category B for third time in 2026, premiums mostly down](https://www.channelnewsasia.com/singapore/coe-premiums-cat-prices-jun-17-bidding-exercise-6188786)
  - SINGAPORE: Certificate of Entitlement (COE) premiums closed lower in the latest bidding exercise on Wednesday (Jun 17), with Category A premiums priced highe…
- [David Allan Coe, country music outlaw and 'Take This Job and Shove It' songwriter, dies at 86](https://www.msn.com/en-us/entertainment/news/david-allan-coe-country-music-outlaw-and-take-this-job-and-shove-it-songwriter-dies-at-86/ar-AA224nyD?ocid=BingNewsVerp)
  - Coe was part of country's outlaw movement in the '70s and was widely criticized for releasing songs that used racist slurs David Allan Coe has died at the ag…
- [David Allan Coe, who wrote ‘Take This Job and Shove It’ and other country hits, dies at 86](https://wtop.com/national/2026/04/david-allan-coe-who-wrote-take-this-job-and-shove-it-and-other-country-hits-dies-at-86/)
  - FILE - David Allan Coe, sporting Willie Nelson braids, performs at the Willie Nelson July 4th Picnic, on July 4, 1983 at Atlanta International Raceway in Ham…
- [David Allan Coe, who wrote ‘Take This Job and Shove It’ and other country hits, dies at 86](https://www.wfla.com/entertainment-news/ap-entertainment/ap-david-allan-coe-who-wrote-take-this-job-and-shove-it-and-other-country-hits-dies-at-86/)
  - David Allan Coe, the country singer-songwriter who wrote the working-class anthem “Take This Job and Shove It″ and had hits with “Mona Lisa Lost Her Smile” a…
- [51 Talk Online Education Earnings Estimates, EPS... | Benzinga](https://www.benzinga.com/quote/COE/earnings)
  - Discover 51 Talk Online Education stock earnings estimates, EPS, and revenue analysis with Benzinga. Stay informed on COE's financial performance.
- [COE Stock Price | 51Talk Online Education Group... | MarketWatch](https://www.marketwatch.com/investing/stock/coe)
  - 51Talk Online Education Group is a global online education platform focusing on English lessons. It operates through the following geographical segments: Chi…
- [Q1 2025 51Talk Online Education Group Earnings Call Transcript](https://www.gurufocus.com/stock/COE/transcripts/2917268)
  - 51Talk Online Education Group at OTC Markets and Deutsche Bank dbVIC ADR Virtual Investor Conference Transcript.Thank you for standing by for 51Talk Online E…
- [COE News Today | Why did 51Talk Online Education Group stock go...](https://www.marketbeat.com/stocks/NYSE/COE/news/)
  - 51Talk Online Education Group (COE) Q1 2026 Earnings Call Transcript.51Talk Online Education Group Announces Engagement of Ernst & Young LLP, as the Company'…

### Search warnings
- news:51Talk Online Education Group earnings OR catalyst: No results found.

## Put opportunities (heuristic) [S2]
- Expiration: None (DTE None)
- Candidates: 0
- ATM IV (est.): —
- IV rank: — (0 local samples)
- HV rank (20d realized): —


_Note: No options chain available_

## Research loop (think → act)

1. _heuristic_ — Coverage looks adequate for this pass; stopping iterative loop.

## Sources

- **[S1]** COE fundamentals (yfinance)
  - 51Talk Online Education Group: price=16.93, rev=95601000.0, fcf=9520000.0, shares=4280532.0, rev_cagr=0.8520862926062147, ROIC=0.21444601322731663, FCF yield=0.09360511118517365
- **[S2]** COE put screen (yfinance_options)
  - Expiration None (DTE None): 0 candidates; IV=None, IV rank=None, HV rank=None. No options chain available
- **[S3]** Wesley Coe (web) — https://en.wikipedia.org/wiki/Wesley_Coe
  - Wesley William Coe Jr. (May 8, 1879 – December 24, 1926), sometimes listed as William Wesley Coe Jr., was an American track and field athlete who competed principally in the sho…
- **[S4]** Best for social mobility in Iowa | Coe College (web) — https://www.coe.edu/why-coe/news/coe-news/coe-named-top-performer-social-mobility-iowa-us-news-world-report
  - Coe is the highest ranked college or university in Iowa on the Social Mobility list. U.S. News & World Report also named Coe its No. 142 National Liberal Arts College.
- **[S5]** Singapore mainstream car COE down 9% to S$85,000, lowest level in... (web) — https://www.businesstimes.com.sg/singapore/mainstream-car-coe-down-9-2-s85000-lowest-level-nearly-year
  - The last time Category A COE premiums went lower than this current round's S$85,000 was in March 2024’s first round of bidding, when it was S$83,000.
- **[S6]** coE-News: November 15, 2006 VOL. 2 ISSUE 3 - News (web) — https://education.ufl.edu/news/2006/11/15/coe-news-november-15-2006-vol-2-issue-3/
  - 15, 2006. You’re reading coE-News, an electronic newsletter produced monthly during the academic year by the College of Education News & Publications Office to keep faculty and …
- **[S7]** Category A COE overtakes Category B for third time in 2026, premiums mostly down (web) — https://www.channelnewsasia.com/singapore/coe-premiums-cat-prices-jun-17-bidding-exercise-6188786
  - SINGAPORE: Certificate of Entitlement (COE) premiums closed lower in the latest bidding exercise on Wednesday (Jun 17), with Category A premiums priced higher than Category B fo…
- **[S8]** David Allan Coe, country music outlaw and 'Take This Job and Shove It' songwriter, dies at 86 (web) — https://www.msn.com/en-us/entertainment/news/david-allan-coe-country-music-outlaw-and-take-this-job-and-shove-it-songwriter-dies-at-86/ar-AA224nyD?ocid=BingNewsVerp
  - Coe was part of country's outlaw movement in the '70s and was widely criticized for releasing songs that used racist slurs David Allan Coe has died at the age of 86 Coe died at …
- **[S9]** David Allan Coe, who wrote ‘Take This Job and Shove It’ and other country hits, dies at 86 (web) — https://wtop.com/national/2026/04/david-allan-coe-who-wrote-take-this-job-and-shove-it-and-other-country-hits-dies-at-86/
  - FILE - David Allan Coe, sporting Willie Nelson braids, performs at the Willie Nelson July 4th Picnic, on July 4, 1983 at Atlanta International Raceway in Hampton, Ga. (AP Photo/…
- **[S10]** David Allan Coe, who wrote ‘Take This Job and Shove It’ and other country hits, dies at 86 (web) — https://www.wfla.com/entertainment-news/ap-entertainment/ap-david-allan-coe-who-wrote-take-this-job-and-shove-it-and-other-country-hits-dies-at-86/
  - David Allan Coe, the country singer-songwriter who wrote the working-class anthem “Take This Job and Shove It″ and had hits with “Mona Lisa Lost Her Smile” and “The Ride” among …
- **[S11]** Best for social mobility in Iowa (web_page) — https://www.coe.edu/why-coe/news/coe-news/coe-named-top-performer-social-mobility-iowa-us-news-world-report
  - Best for social mobility in Iowa Skip to main content Sep 14, 2022 After being listed as a top college in the country based on contributions to the public good by Washington Mon…
- **[S12]** Singapore mainstream car COE down 9% to S$85,000, lowest level in almost a year - The Business Times (web_page) — https://www.businesstimes.com.sg/singapore/mainstream-car-coe-down-9-2-s85000-lowest-level-nearly-year
  - Singapore mainstream car COE down 9% to S$85,000, lowest level in almost a year - The Business Times Mainstream car COE down 9.2% at S$85,000, lowest level in nearly a year Slow…

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

# COE — Planned Research Report

> Not investment advice. Local research draft only.

**Goal:** Institutional deep dive triggered by FilingDesk: Chief Executive Officer Huang Jack Jiajia open-market buy $3,080,724 (51Talk Online Education Group).
**Mode:** fast
**Template:** fast
**Planner:** template

## Plan executed

- **Fundamentals & ratios** (`fundamentals`): get_fundamentals
  - Revenue, FCF, shares, growth rates, ROIC, FCF yield, debt/equity. Focus: Institutional deep dive triggered by FilingDesk: Chief Executive Officer Huang Jack Jiajia open-market buy $3,080,724 (51Talk Online Education Group).
- **DCF valuation (base / bull / bear)** (`valuation`): run_dcf
  - Intrinsic value from growth, FCF margin, and WACC assumptions
- **Put income screen** (`options`): screen_puts
  - ~30–60 DTE OTM puts targeting ~10–15% annualized premium

## Fundamentals [S1]
- Company: 51Talk Online Education Group
- Sector / industry: Consumer Defensive / Education & Training Services
- Price: 16.93
- 52-week range: $14.66 – $56.13
- Market cap: $101.70M
- Enterprise value: $69.03M
- Shares outstanding: 4.28M
- Beta: 0.748
- Book equity: -$31.36M
- Revenue (latest): $95.60M
- EBITDA (latest): -$13.99M
- Free cash flow (latest): $9.52M
- Operating income: -$14.43M
- Operating margin: -15.1%
- EV / EBITDA: -4.9x
- ROIC: 21.4%
- FCF yield: 9.4%
- Debt / Equity: -0.0937908600950346
- FCF / share: $2.22
- Revenue / share: $22.33

### Capital structure
- Cash: $38.87M
- Short-term debt: $1.76M
- Long-term debt: $1.18M
- Total debt: $2.94M
- Net debt: -$35.93M
- Net debt / EBITDA: 2.6x
- Working capital: -$34.96M
- Total assets: $66.09M
- Total liabilities: $97.34M
- Retained earnings: -$370.40M
- Current ratio: 0.6x

### Growth
- Revenue CAGR: 85.2%
- FCF CAGR: —
- Latest revenue YoY: 88.6%
- Latest FCF YoY: 72.3%

### Market expectations (yfinance, sparse)
- Mean target: —
- Target range: — – —
- Recommendation: none

_Consensus revenue/EBITDA forecasts are often unavailable via free feeds; treat targets as point-in-time only._

### Historical KPIs (multi-year)

| Year | Revenue | OCF | Capex | FCF | EBITDA | LT debt | Cash | Net debt | Net income |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2025 | $95.60M | $11.81M | $2.29M | $9.52M | -$13.99M | $2.94M | $38.87M | -$35.93M | -$16.80M |
| 2024 | $50.69M | $5.83M | $308.00K | $5.52M | -$7.91M | $2.68M | $27.76M | -$25.07M | -$7.24M |
| 2023 | $27.11M | $559.00K | $287.00K | $272.00K | -$13.56M | $631.00K | $21.30M | -$20.67M | -$15.03M |
| 2022 | $15.05M | -$45.70M | $5.00K | -$45.71M | -$12.26M | $734.00K | $18.19M | -$17.45M | -$42.56M |

## Charts

### Revenue & FCF history
![Revenue & FCF history](/charts/COE_fast_revenue_fcf.png)

### DCF scenario prices
![DCF scenario prices](/charts/COE_fast_dcf_scenarios.png)

### Base-case FCF path
![Base-case FCF path](/charts/COE_fast_base_fcf_path.png)

## DCF valuation (base / bull / bear) [S2]

> Simplified revenue->FCF DCF. Not investment advice; assumptions are editable heuristics.

- Spot price: $16.93
- Base revenue: $95.60M
- Shares: 4,280,532
- Net debt (Debt−Cash): -$35.93M

| Scenario | Growth | FCF margin | WACC | Term. g | Equity value | Share price | Upside |
|----------|--------|------------|------|---------|--------------|-------------|--------|
| bear | 25.0% | 8.0% | 12.0% | 1.5% | $216.80M | $50.65 | 199.2% |
| base | 35.0% | 10.0% | 10.0% | 2.5% | $489.90M | $114.45 | 576.0% |
| bull | 42.0% | 13.0% | 9.0% | 3.0% | $980.64M | $229.09 | 1253.2% |

### Assumption notes
- Base revenue growth seeded from historical rate (88.6%).


### Base-case projected FCF

- Year 1: revenue $129.06M, FCF $12.85M (PV $11.68M)
- Year 2: revenue $174.23M, FCF $17.35M (PV $14.34M)
- Year 3: revenue $235.21M, FCF $23.42M (PV $17.60M)
- Year 4: revenue $317.54M, FCF $31.62M (PV $21.60M)
- Year 5: revenue $428.68M, FCF $42.69M (PV $26.51M)
- Terminal value $583.40M (PV $362.25M)

## Put opportunities (heuristic) [S3]
- Expiration: None (DTE None)
- Candidates: 0
- ATM IV (est.): —
- IV rank: — (0 local samples)
- HV rank (20d realized): —


_Note: No options chain available_

## Research loop (think → act)

1. _heuristic_ — Coverage looks adequate for this pass; stopping iterative loop.

## Sources

- **[S1]** COE fundamentals (yfinance)
  - 51Talk Online Education Group: price=16.93, rev=95601000.0, fcf=9520000.0, shares=4280532.0, rev_cagr=0.8520862926062147, ROIC=0.21444601322731663, FCF yield=0.09360511118517365
- **[S2]** COE DCF valuation (dcf)
  - Base share price=114.44814308174645, bull=229.09247777968184, bear=50.64858919987204
- **[S3]** COE put screen (yfinance_options)
  - Expiration None (DTE None): 0 candidates; IV=None, IV rank=None, HV rank=None. No options chain available

## Self-critique

_Automated review (heuristic)._

### Strengths
- Combines local fundamentals, optional DCF scenarios, and cited sources where available.
- Keeps a non-advisory framing for local research drafts.

### Issues & gaps
- Base-case upside vs spot is extreme (>150%); check growth/margin/WACC assumptions for optimism bias.

### Caution for readers
- Treat scenario prices as sensitivity output, not a forecast.
- Re-check primary filings and fresh market data before any decision.
