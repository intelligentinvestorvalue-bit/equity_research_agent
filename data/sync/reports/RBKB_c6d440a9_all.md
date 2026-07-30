# RBKB — Full research pack

> Not investment advice. Local research draft only.

**Templates:** memo, valuation, deep, income, fast
**Generated:** 2026-07-28T05:42:48.947975+00:00



---

# Template: Institutional deep dive (memo) (`memo`)

# RBKB — Planned Research Report

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
- Company: Rhinebeck Bancorp, Inc.
- Sector / industry: Financial Services / Banks - Regional
- Price: 12.3
- 52-week range: $6.74 – $12.88
- Market cap: $192.35M
- Enterprise value: -$161.05M
- Shares outstanding: 15.64M
- Beta: 0.148
- Book equity: $136.85M
- Revenue (latest): $53.35M
- EBITDA (latest): —
- Free cash flow (latest): $10.89M
- Operating income: —
- Operating margin: —
- EV / EBITDA: —
- ROIC: —
- FCF yield: 5.7%
- Debt / Equity: 0.22146552480051443
- FCF / share: $0.70
- Revenue / share: $3.41

### Capital structure
- Cash: $18.83M
- Short-term debt: $1.61M
- Long-term debt: $28.69M
- Total debt: $30.31M
- Net debt: $11.48M
- Net debt / EBITDA: —

### Growth
- Revenue CAGR: 3.8%
- FCF CAGR: -7.3%
- Latest revenue YoY: 85.7%
- Latest FCF YoY: 41.9%

### Market expectations (yfinance, sparse)
- Mean target: —
- Target range: — – —
- Recommendation: none

_Consensus revenue/EBITDA forecasts are often unavailable via free feeds; treat targets as point-in-time only._

### Historical KPIs (multi-year)

| Year | Revenue | OCF | Capex | FCF | EBITDA | LT debt | Cash | Net debt | Net income |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2025 | $53.35M | $11.74M | $850.00K | $10.89M | — | $28.69M | $18.83M | $9.87M | $10.04M |
| 2024 | $28.73M | $8.47M | $791.00K | $7.68M | — | $74.93M | $19.18M | $55.75M | -$8.62M |
| 2023 | $43.70M | $7.05M | $578.00K | $6.47M | — | $133.22M | $14.61M | $118.61M | $4.39M |
| 2022 | $47.77M | $14.79M | $1.13M | $13.66M | — | $62.88M | $16.82M | $46.06M | $7.00M |

## Charts

### Revenue & FCF history
![Revenue & FCF history](/charts/RBKB_memo_revenue_fcf.png)

### DCF scenario prices
![DCF scenario prices](/charts/RBKB_memo_dcf_scenarios.png)

### Base-case FCF path
![Base-case FCF path](/charts/RBKB_memo_base_fcf_path.png)

### EV/EBITDA scenario prices
![EV/EBITDA scenario prices](/charts/RBKB_memo_ev_ebitda_scenarios.png)

### Headwind/tailwind price ranges
![Headwind/tailwind price ranges](/charts/RBKB_memo_scenario_ranges.png)

### Normalized price vs peers
![Normalized price vs peers](/charts/RBKB_memo_peers_normalized.png)

## DCF valuation (base / bull / bear) [S3]

> Simplified revenue->FCF DCF. Not investment advice; assumptions are editable heuristics.

- Spot price: $12.30
- Base revenue: $53.35M
- Shares: 15,638,237
- Net debt (Debt−Cash): $11.48M

| Scenario | Growth | FCF margin | WACC | Term. g | Equity value | Share price | Upside |
|----------|--------|------------|------|---------|--------------|-------------|--------|
| bear | 25.0% | 18.4% | 12.0% | 1.5% | $222.13M | $14.20 | 15.5% |
| base | 35.0% | 20.4% | 10.0% | 2.5% | $507.96M | $32.48 | 164.1% |
| bull | 42.0% | 23.4% | 9.0% | 3.0% | $941.29M | $60.19 | 389.4% |

### Assumption notes
- Base revenue growth seeded from historical rate (85.7%).


### Base-case projected FCF

- Year 1: revenue $72.03M, FCF $14.71M (PV $13.37M)
- Year 2: revenue $97.24M, FCF $19.85M (PV $16.41M)
- Year 3: revenue $131.27M, FCF $26.80M (PV $20.14M)
- Year 4: revenue $177.22M, FCF $36.18M (PV $24.71M)
- Year 5: revenue $239.25M, FCF $48.84M (PV $30.33M)
- Terminal value $667.54M (PV $414.49M)

## Valuation — EV/EBITDA scenarios [S2]

> Priced-in model: implied price = (EBITDA × EV/EBITDA − net debt) ÷ shares. Not a forecast.

- Spot: $12.30
- Net debt used: $11.48M

| Scenario | EBITDA | EV/EBITDA | Implied EV | Equity value | Implied price |
|---|---:|---:|---:|---:|---:|
| bear | $700.00M | 6.0x | $4.20B | $4.19B | $267.84 |
| base | $1.00B | 8.0x | $8.00B | $7.99B | $510.83 |
| bull | $1.20B | 10.0x | $12.00B | $11.99B | $766.62 |

- EBITDA missing or non-positive; scenarios use placeholder $1B EBITDA — edit before relying on prices.
- No current EV/EBITDA; defaulted base multiple to 8.0x.

## Scenario price ranges (headwinds & tailwinds) [S36]

> Medium-term (18–36 months (medium / medium-long term)) driver → EV/EBITDA bridge. Distinct from the FCF DCF path. Not investment advice.

- Spot: $12.30
- Anchor multiple: 8.0x (driver_ev_ebitda_bridge)
- Anchor EBITDA: $1.00B
- Probability-weighted midpoint: **$598.73** (heuristic weights, not a rating)
- Driver extraction: `rules`

### Headwinds (bear-case fuel)

- **Balance-sheet / refinancing pressure** — sector=Financial Services industry=Banks - Regional revenue=53355000.0 ebitda=None fcf=10893000.0 net_debt=11479000.0 nd_ebitda=None target=None rec=none _(source: fundamentals)_
- **Regulatory / legal risk** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, guidance, revenue, margin, supply ch _(source: item_1a)_
- **Competitive / pricing pressure** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, guidance, revenue, margin, supply ch _(source: item_1a)_
- **Margin / cost headwind** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, guidance, revenue, margin, supply ch _(source: item_1a)_
- **Operational / cyber risk** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, guidance, revenue, margin, supply ch _(source: item_1a)_

### Tailwinds (bull-case fuel)

- **Positive free cash flow** — FCF $10.89M (yield 5.7%) _(source: fundamentals)_
- **Revenue growth momentum** — Latest revenue YoY ≈ 85.7% _(source: fundamentals)_
- **Contract / backlog wins** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, guidance, revenue, margin, supply ch _(source: item_1a)_
- **Product / pricing power** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, guidance, revenue, margin, supply ch _(source: item_1a)_
- **Growth / execution upside** — ### Item 7 — MD&A (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, margin, interest rate, customer, segment, product, service, market, operations, network - and A _(source: item_7)_
- **Margin expansion / cost takeout** — ### Item 7 — MD&A (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, margin, interest rate, customer, segment, product, service, market, operations, network - and A _(source: item_7)_
- **Multiple re-rating / Street upgrades** — Rhinebeck Bancorp, Inc. (RBKB) Analyst Ratings... - Yahoo Finance See Rhinebeck Bancorp, Inc. (RBKB) stock analyst estimates, including earnings and revenue, EPS, upgrades and down _(source: web)_
- **Capital returns / FCF inflection** — Rhinebeck Bancorp Inc Ordinary Shares (RBKB) See the latest Rhinebeck Bancorp Inc Ordinary Shares stock price (RBKB:XNAS), related news, valuation, dividends and more to help you m _(source: web)_

### Price ranges by case

| Case | Prob. | Metric vs TTM | Multiple | Price low | Mid | High | Upside vs spot |
|---|---:|---:|---:|---:|---:|---:|---:|
| bear | 0.18 | 0.74x | 5.3x | $224.13 | $249.12 | $274.10 | +1925% |
| base | 0.44 | 1.06x | 8.0x | $503.57 | $541.53 | $579.48 | +4303% |
| bull | 0.38 | 1.25x | 10.4x | $747.43 | $830.56 | $913.69 | +6653% |

#### Bear — headwinds dominate

Headwinds bite: weaker operating trajectory and multiple compression. Equity duration shrinks if cash generation fails to offset leverage / competitive pressure.

- **Range:** $224.13 – $274.10 (mid $249.12) · EBITDA $740.00M · multiple 5.3x
- Driver: **Balance-sheet / refinancing pressure** — sector=Financial Services industry=Banks - Regional revenue=53355000.0 ebitda=None fcf=10893000.0 net_debt=11479000.0 nd_ebitda=None target=None rec=none
- Driver: **Regulatory / legal risk** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, guidance, revenu
- Driver: **Competitive / pricing pressure** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, guidance, revenu
- Driver: **Margin / cost headwind** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, guidance, revenu
- Driver: **Operational / cyber risk** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, guidance, revenu

#### Base — mixed execution

Balanced path: some tailwinds offset headwinds. Operating scale roughly holds with modest repair/normalization; valuation stays near the current EV/EBITDA anchor.

- **Range:** $503.57 – $579.48 (mid $541.53) · EBITDA $1.06B · multiple 8.0x
- Driver: **Positive free cash flow** — FCF $10.89M (yield 5.7%)
- Driver: **Revenue growth momentum** — Latest revenue YoY ≈ 85.7%
- Driver: **Balance-sheet / refinancing pressure** — sector=Financial Services industry=Banks - Regional revenue=53355000.0 ebitda=None fcf=10893000.0 net_debt=11479000.0 nd_ebitda=None target=None rec=none
- Driver: **Regulatory / legal risk** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, guidance, revenu

#### Bull — tailwinds dominate

Tailwinds compound: operating improvement plus a re-rating toward peer or recovery multiples as balance-sheet and growth narratives improve.

- **Range:** $747.43 – $913.69 (mid $830.56) · EBITDA $1.25B · multiple 10.4x
- Driver: **Positive free cash flow** — FCF $10.89M (yield 5.7%)
- Driver: **Revenue growth momentum** — Latest revenue YoY ≈ 85.7%
- Driver: **Contract / backlog wins** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, guidance, revenu
- Driver: **Product / pricing power** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, guidance, revenu
- Driver: **Growth / execution upside** — ### Item 7 — MD&A (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, margin, interest rate, customer, segment, product, service, market, operati

### Method notes

- Item 1A risks weighted toward headwinds.
- Current ev_ebitda multiple missing; anchored at 8.0x.
- Mapping follows Gemini/Perplexity-style scenario memos: qualitative drivers → operating metric & multiple paths → share-price ranges over a medium-term horizon.

## Peer & factor comps

- Sector / industry: Financial Services / Banks - Regional
- Peers: JPM, BAC, WFC, C, GS

| Ticker | Mkt cap | EV/EBITDA | ND/EBITDA | Beta | 1y | 5y | Vol |
|---|---:|---:|---:|---:|---:|---:|---:|
| RBKB | $192.4M | — | — | 0.15 | 34.2% | 60.6% | 29.8% |
| JPM | — | — | — | 0.98 | 21.6% | 166.1% | 24.4% |
| BAC | — | — | — | 1.18 | 31.0% | 84.2% | 26.7% |
| WFC | $267.1B | — | — | 0.92 | 5.8% | 116.3% | 29.9% |
| C | $223.3B | — | — | 1.09 | 41.7% | 132.4% | 29.2% |
| GS | — | — | — | 1.29 | 46.7% | 216.2% | 28.5% |

- Peer set (heuristic by sector/industry): JPM, BAC, WFC, C, GS
- Beta vs JPM (daily, ~5y overlap): 0.07

_Price returns are price-only (dividends ignored). Peer set is heuristic, not a formal comps universe._

## Earnings, guidance & revision catalysts

_No earnings surprise history available from yfinance._

- No earnings dates available from yfinance

## Recent SEC filings (10-Q / 8-K)

| Date | Form | Description |
|---|---|---|
| 2026-07-23 | 8-K | [8-K](https://www.sec.gov/Archives/edgar/data/1751783/000175178326000035/rbkb-20260723x8k.htm) |
| 2026-07-21 | 8-K | [8-K](https://www.sec.gov/Archives/edgar/data/1751783/000175178326000032/rbkb-20260721x8k.htm) |
| 2026-07-17 | 8-K | [8-K](https://www.sec.gov/Archives/edgar/data/1751783/000175178326000029/rbkb-20260717x8k.htm) |
| 2026-06-29 | 8-K | [8-K](https://www.sec.gov/Archives/edgar/data/1751783/000175178326000027/rbkb-20260629x8k.htm) |
| 2026-05-26 | 8-K | [8-K](https://www.sec.gov/Archives/edgar/data/1751783/000175178326000022/rbkb-20260526x8k.htm) |
| 2026-05-19 | 8-K | [8-K](https://www.sec.gov/Archives/edgar/data/1751783/000175178326000020/rbkb-20260519x8k.htm) |
| 2026-05-14 | 8-K | [FORM 8-K](https://www.sec.gov/Archives/edgar/data/1751783/000110465926061328/tm2614362d1_8k.htm) |
| 2026-05-14 | 10-Q | [10-Q](https://www.sec.gov/Archives/edgar/data/1751783/000175178326000018/rbkb-20260331x10q.htm) |
| 2026-04-23 | 8-K | [8-K](https://www.sec.gov/Archives/edgar/data/1751783/000175178326000015/rbkb-20260423x8k.htm) |
| 2026-03-13 | 10-K | [10-K](https://www.sec.gov/Archives/edgar/data/1751783/000175178326000005/rbkb-20251231x10k.htm) |
| 2026-02-10 | 8-K | [FORM 8-K](https://www.sec.gov/Archives/edgar/data/1751783/000110465926012668/tm265741d1_8k.htm) |
| 2026-01-29 | 8-K | [8-K](https://www.sec.gov/Archives/edgar/data/1751783/000175178326000002/rbkb-20260129x8k.htm) |

_Headlines/meta only — documents not fully parsed in this pass._

## Key driver analysis (quarterly)

Pearson / Spearman correlations of quarterly stock returns with fundamentals.

| Driver | Pearson r | p | n | Spearman ρ | p |
|---|---:|---:|---:|---:|---:|
| Revenue growth (YoY) | — | — | 1 | — | — |
| Free cash flow | -0.074 | 0.898 | 5 | 0.300 | 0.586 |
| FCF margin | -0.007 | 0.991 | 5 | 0.300 | 0.586 |
| Operating cash flow | 0.098 | 0.864 | 5 | 0.300 | 0.586 |
| Long-term debt level | -0.653 | 0.136 | 5 | -0.500 | 0.317 |
| EBITDA | — | — | — | — | — |
| Capex (abs) | 0.709 | 0.081 | 5 | 0.500 | 0.317 |

### Regime check (FCF)

- later: r=-0.074 (n=5, p≈0.898)

- Correlations describe association, not causation.
- Small samples (especially regime splits) are directional only.
- Regime split at 2023-12-31 (sample midpoint); directional only.

## Executive summary

Rhinebeck Bancorp, Inc. (RBKB) trades near 12.3 with market cap $192.35M and EV -$161.05M. Net debt is $11.48M (ND/EBITDA —). Latest revenue $53.35M, EBITDA —, FCF $10.89M.

**Goal focus:** Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers.

What matters most (framework): balance-sheet trajectory, cash generation vs leverage, and whether market expectations (sparse free-data targets) already price execution risk.

EV/EBITDA implied prices — bear $267.84 / base $510.83 / bull $766.62.

## Company setup & business model

**Keyword hits:** risk, regulation, competition, margin, interest rate, customer, segment, product, service, market, operations

- The Company is regulated by the Board of Governors of the Federal Reserve System (the “Federal Reserve Board”) and the New York State Department of Financial Services (the “NYSDFS”).
- We provide a full range of banking and financial services to consumer and commercial customers through our corporate office and 12 branches located in Dutchess, Orange and Ulster Counties.
- We also maintain a representative office in Albany County to originate indirect automobile and commercial loans and a representative office in Dutchess County for financial services.
- Financial services, including investment  advisory and financial product sales, are offered through a division of the Bank doing business as Rhinebeck Asset Management (“RAM”).
- We offer a variety of deposit accounts, including savings accounts, certificates of deposit, money market accounts, commercial and personal checking accounts and individual retirement accounts.
- We are subject to regulation and examination by the NYSDFS and by the Federal Deposit Insurance Corporation (the “FDIC”).
- Market Area  Our primary market area encompasses Dutchess, Orange, Ulster and Albany Counties (and their contiguous counties), which are located in the Hudson Valley region of New York.
- The Hudson Valley region has a diversified economy and representative industries include education, health, government, leisure and hospitality and professional business services.
- The four counties in our primary market area each had a lower unemployment rate than New York State (Dutchess County, 3.2%, Orange County, 3.6%, Ulster County, 3.5% and Albany County, 3.3%).
- Competition  We face significant competition for deposits and loans.
- Our most direct competition for deposits has historically come from the numerous financial institutions operating in our market area (including other community and commercial banks, credit unions and financial technology companies), many of which are significantly larger than we are and have greater resources.
- We also face competition for investors’ funds from other sources such as brokerage firms, money market funds and mutual funds, as  well as securities, such as Treasury bills, offered by the Federal Government.
- Based on FDIC data, at June 30, 2025 (the latest date for which information is available), we had 10.44% of the FDIC-insured deposit market share in Dutchess County, which was fourth among the 15 institutions with offices in the county, 1.59% of the FDIC-insured deposit market share in Ulster County, which was 12thamong the 18 institutions with offices in the county, and 1.28% of the FDIC-insured deposit market share  in Orange County, which was 14thamong the 22 institutions with offices in the county.
- We expect competition to remain intense in the future as a result of legislative, regulatory and technological changes and the continuing trend of consolidation in the financial services industry.
- Technological advances, for example, have lowered barriers to entry, allowed banks to expand their geographic reach by providing services over the internet and made it possible for non-depository institutions, including financial technology companies, to offer products and services that traditionally  have been provided by banks.
- Competition for deposits and the origination of loans could limit our growth in the future.
- We seek to meet this competition with convenient branch locations and online offerings, emphasizing personalized banking and the advantage of local decision-making in our banking businesses.
- Specifically, we promote and maintain relationships and build customer loyalty within local communities by focusing our marketing and community involvement on the specific needs of individual neighborhoods.
- At December  31, 2025, substantially all of our commercial real estate loans were secured by properties located in our market area.
- However, occasionally we will originate commercial real estate loans on properties located outside our market area based on an established relationship with a strong borrower.
- The interest rate on commercial real estate loans is generally adjustable and based on a margin over an index, typically The Wall Street Journal Prime Rate or the Federal Home Loan Bank of New York Amortizing Advance Rate.
- We selectively offer interest rate swaps for both commercial and multi-family real estate loans.
- In underwriting commercial real estate loans, we consider a number of factors, including the projected net cash flows to the loan’s debt service requirement (generally requiring a minimum of 1.20x), the age and condition of the collateral, the financial resources and income level of the borrower and the borrower’s experience in owning or managing similar properties.
- Our multi-family real estate loans are generally secured by multi-unit rental properties, consisting of five to 100 rental units, in our market area.
- The interest rates on our multi-family real estate loans are generally adjustable based on a margin over an index.
- In underwriting multi-family real estate loans, we consider a number of factors including the projected net cash flows to the loan’s debt service requirement (generally requiring a minimum of 1.20x), the age and condition of the collateral, the financial resources and income level of the borrower, and the borrower’s experience in owning or managing similar properties.
- All these loans are secured by properties located in our primary market area.
- The interest rate is generally a variable rate based on an index rate, typically The Wall Street Journal Prime Rate plus a margin.

_Source: latest 10-K Item 1 (Business), summarized locally._

## Variant perception

- **Consensus frame (sparse):** recommendation=none, mean target=—.
- **Bear:** leverage and execution risk dominate; cash generation fails to cover refinancing / reinvestment needs; equity remains constrained by net debt.
- **Bull:** cash-flow and strategic optionality re-rate the equity as leverage falls and growth/mix improves.
- **Middle:** returns may track free-cash-flow more than headline revenue — verify with driver analysis tab.

## Catalysts & monitoring

- Next earnings window (calendar): unconfirmed
- Peer tape to watch: JPM, BAC, WFC, C, GS
- Monitor: FCF vs net debt, leverage (ND/EBITDA), refinancing headlines, and material 8-K strategy updates.
- Recent filing: 8-K on 2026-07-23 — 8-K
- Recent filing: 8-K on 2026-07-21 — 8-K
- Recent filing: 8-K on 2026-07-17 — 8-K
- Recent filing: 8-K on 2026-06-29 — 8-K
- Recent filing: 8-K on 2026-05-26 — 8-K

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
| Guidance / outlook | Forward cash/earnings path | Rhinebeck Bancorp Inc (RBKB) Stock Forecast, Price Targets and... RBKB average Analyst price target in the past 3 months is ―. Each month's total comprises the sum of three months' | Rhinebeck Bancorp Inc (RBKB) Stock Forecast, Price Targets and... |
| Margin / EBITDA | Mix and operating leverage | RBKB (Rhinebeck Bancorp): De-risking Meets Margin Headwinds Jun 21, 2026 · Core thesis: The market is discounting the bank's structural de-risking, which reduced total borrowings t | RBKB (Rhinebeck Bancorp): De-risking Meets Margin Headwinds |
| Leverage / refinancing | Balance-sheet repair | Rhinebeck Bancorp (RBKB) 10K Form and Latest SEC Filings 2026 4 days ago · For investors, these filings are the primary source of verified financial data — covering everything from | Rhinebeck Bancorp (RBKB) 10K Form and Latest SEC Filings 2026 |
| Contract / backlog | Demand durability | Rhinebeck Bancorp Inc Customers by Division and Industry - CSIMarket RBKB's vs. Customers, Data. (Revenue and Income for Trailing 12 Months, in Millions of $, except Employees). Co | Rhinebeck Bancorp Inc Customers by Division and Industry - CSIMarket |

_Proxies are heuristic extractions from public web/SEC context; verify against primary filings._

## Catalyst calendar

| Window | Catalyst | Notes |
|---|---|---|
| 2026-07-23 | 8-K | 8-K |
| 2026-07-21 | 8-K | 8-K |
| 2026-07-17 | 8-K | 8-K |
| 2026-06-29 | 8-K | 8-K |
| 2026-05-26 | 8-K | 8-K |
| 2026-05-19 | 8-K | 8-K |
| 2026-05-14 | 8-K | FORM 8-K |
| 2026-05-14 | 10-Q | 10-Q |
| 2026-04-23 | 8-K | 8-K |
| 2026-03-13 | 10-K | 10-K |
| 2026-02-10 | 8-K | FORM 8-K |
| 2026-01-29 | 8-K | 8-K |
| November 15, 2025 | Web event | Rubrik (RBRK) Deep Dive: 8 Trading Insights on Business Model, Financials, Competition, and 2025 Catalysts | Flash News Detail |
| June 26, 2023 | Web event | RBKB Stock Quote Price and Forecast | CNN |
| June 1, 2026 | Web event | Rubrik: Even A Strong Analyst Day May Not Be Enough (NYSE:RBRK) | Seeking Alpha |
| Jul 21, 2026 | Web event | RBKB SEC Filings - Rhinebeck Bancorp, Inc. 10-K, 10-Q, 8-K Forms |
| Jun 21, 2026 | Web event | RBKB (Rhinebeck Bancorp): De-risking Meets Margin Headwinds |
| Jul 17, 2026 | Web event | RBKB SEC Filings - Rhinebeck Bancorp, Inc.- Annual Report ... |
| May 26, 2026 | Web event | Rhinebeck Bancorp, Inc. Announces Commencement of Stock Offering |

## Web research — web_analysts

- Queries: RBKB analyst price target, Rhinebeck Bancorp, Inc. stock rating OR consensus OR upgrade OR downgrade, RBKB Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers analyst, RBKB guidance OR investor day OR catalyst
- Unique hits: 16
- Pages fetched: 0/3

### Web synthesis — web_analysts (rule-based fallback — Ollama unavailable)
**Keyword hits:** competition, revenue, service, market

- Objective stock score based on 6 market factors.
- Analyst Estimates | MarketWatch | www.marketwatch.com | https://www.marketwatch.com/investing/stock/rbkb/analystestimates RBKB Analyst Estimates.
- (RBKB) stock analyst estimates, including earnings and revenue, EPS, upgrades and downgrades.NasdaqCM - Nasdaq Real Time Price•USD.
- [HIT] Analyst Upgrades & Downgrades - MarketWatch | www.marketwatch.com | https://www.marketwatch.com/tools/upgrades-downgrades Real-time information on stock upgrades and downgrades by MarketWatch.
- [HIT] Downgrade: What It Is, How It Works, and Warning Signs | www.investopedia.com | https://www.investopedia.com/terms/d/downgrade.asp A downgrade is a negative change in an estimate for a stock's performance, issued by an analyst for a financial services firm.
- [HIT] Rubrik (RBRK) Deep Dive: 8 Trading Insights on Business Model, Financials, Competition, and 2025 Catalysts | Flash News Detail | blockchain.news | https://blockchain.news/flashnews/rubrik-rbrk-deep-dive-8-trading-insights-on-business-model-financials-competition-and-2025-catalysts November 15, 2025 - According to @StockMarketNerd, a new deep dive on Rubrik (RBRK) covering the business model, financials, competitive landscape, and investment case has been published, which traders can use to fram  [HIT] Building an Investment Thesis | Street Of Walls | www.streetofwalls.com | https://www.streetofwalls.com/finance-training-courses/hedge-fund-training/building-an-investment-thesis/ Catalysts are extremely important in identifying when you are going to “get paid.” This is a crucial factor in sizing positions.
- This year RBC Capital Markets had their best performance ever, placing #7, with 20 ranked analysts across 22 sectors.
- [HIT] RBKB Stock Quote Price and Forecast | CNN | www.cnn.com | https://www.cnn.com/markets/stocks/RBKB June 26, 2023 - RBKB is trading in the middle of its 52-week range and below its 200-day simple moving average.

### Sources found
- [Rhinebeck Bancorp Inc (RBKB) Stock Forecast, Price Targets and...](https://www.tipranks.com/stocks/rbkb/forecast)
  - RBKB average Analyst price target in the past 3 months is ―. Each month's total comprises the sum of three months' worth of ratings.What is RBKB’s average 12…
- [Consensus and price targets from Wall Street analysts on RBKB.](https://www.investing.com/equities/rhinebeck-insights?analysts&source=desktop&medium=instrument)
  - Wall Street analyst price targets and ratings. Stock sentiment by bloggers, insiders, and financial gurus. News sentiment and score for thousands of stocks. …
- [RBKB | Rhinebeck Bancorp Inc. Analyst Estimates | MarketWatch](https://www.marketwatch.com/investing/stock/rbkb/analystestimates)
  - RBKB Analyst Estimates. Snapshot. Average Recommendation.Stock Price Targets. High. N/A.
- [Rhinebeck Bancorp, Inc. (RBKB) Analyst Ratings... - Yahoo Finance](https://finance.yahoo.com/quote/RBKB/analysis/)
  - See Rhinebeck Bancorp, Inc. (RBKB) stock analyst estimates, including earnings and revenue, EPS, upgrades and downgrades.NasdaqCM - Nasdaq Real Time Price•USD.
- [Analyst Upgrades & Downgrades - MarketWatch](https://www.marketwatch.com/tools/upgrades-downgrades)
  - Real-time information on stock upgrades and downgrades by MarketWatch. View information on strong stocks to buy and weak stocks to sell.
- [Upgrade - Personal Loans, Cards and Rewards Checking | Upgrade](https://www.upgrade.com/)
  - Check your rate for a personal loan up to $50,000 with low, fixed rates. Or get started with Upgrade Cards, Rewards Checking, and Premier Savings. Start in m…
- [Downgrade: What It Is, How It Works, and Warning Signs](https://www.investopedia.com/terms/d/downgrade.asp)
  - A downgrade is a negative change in an estimate for a stock's performance, issued by an analyst for a financial services firm. Learn how it impacts investing…
- [Rhinebeck Bank | Home](https://www.rhinebeckbank.com/)
  - Rhinebeck Bank, Your Community Bank. From your banking needs to our community, see all that we have to offer. View options.
- [Rhinebeck Bancorp, Inc. (RBKB) Stock Price, Quote, News & Analysis | Seeking Alpha](https://seekingalpha.com/symbol/RBKB)
  - A high-level overview of Rhinebeck Bancorp, Inc. (RBKB) stock. View (RBKB) real-time stock price, chart, news, analysis, analyst reviews and more.
- [Rubrik (RBRK) Deep Dive: 8 Trading Insights on Business Model, Financials, Competition, and 2025 Catalysts | Flash News Detail](https://blockchain.news/flashnews/rubrik-rbrk-deep-dive-8-trading-insights-on-business-model-financials-competition-and-2025-catalysts)
  - November 15, 2025 - According to @StockMarketNerd, a new deep dive on Rubrik (RBRK) covering the business model, financials, competitive landscape, and inves…
- [Building an Investment Thesis | Street Of Walls](https://www.streetofwalls.com/finance-training-courses/hedge-fund-training/building-an-investment-thesis/)
  - Catalysts are extremely important in identifying when you are going to “get paid.” This is a crucial factor in sizing positions. If a catalyst is expected to…
- [Institutional Investor All-American Research Poll](https://www.rbccm.com/en/about-us/story.page?dcr=templatedata/article/news/data/2019/10/the_results_are_in_institutional_inves)
  - Every year, thousands of investment professionals (nearly 4,000 to be exact) vote to determine the top equity research analysts — and firms — on Wall Street.…

### Search warnings
- news:RBKB analyst price target: No results found.
- news:Rhinebeck Bancorp, Inc. stock rating OR consensus OR upgrade OR downgrade: No results found.
- news:RBKB Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers analyst: No results found.
- news:RBKB guidance OR investor day OR catalyst: No results found.

## Web research — web_drivers

- Queries: RBKB Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers, Rhinebeck Bancorp, Inc. RBKB outlook OR catalyst OR commodity OR uranium OR rare earth OR vanadium, RBKB sector drivers OR market demand, Rhinebeck Bancorp, Inc. RBKB backlog OR contract OR refinancing OR leverage
- Unique hits: 15
- Pages fetched: 2/3

### Web synthesis — web_drivers (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, competition, revenue, margin, supply chain, customer, segment, product, service, market, operations, network

- [HIT] RBKB (Rhinebeck Bancorp): De-risking Meets Margin Headwinds | graphvest.com | https://graphvest.com/rbkb Jun 21, 2026 · Core thesis: The market is discounting the bank's structural de-risking, which reduced total borrowings to sixteen point four eight million dollars.
- This aggressive pay-down of higher-rate liabilities protects the underlying asset spread from local deposit competition.
- [HIT] Rhinebeck Bancorp (RBKB) 10K Form and Latest SEC Filings 2026 | www.marketbeat.com | https://www.marketbeat.com/stocks/NASDAQ/RBKB/sec-filings/ 4 days ago · For investors, these filings are the primary source of verified financial data — covering everything from annual revenue and debt levels in the 10-K, to material business events in 8-K current reports, to insider buying and selling activity in Form 4 disclosures.
- [HIT] Commodity Prices | Commodity Market | Markets Insider | markets.businessinsider.com | https://markets.businessinsider.com/commodities?op=1 Get all information on the commodity market.
- [HIT] Rare Earth Archives - MINING.COM | www.mining.com | https://www.mining.com/commodity/rare-earth/ Algae breakthrough could double rare earth concentrations Researchers found using algae is a cleaner way to concentrate rare earths and help the US strengthen critical mineral supply chains.
- [HIT] Rhinebeck Bancorp Inc Customers by Division and Industry - CSIMarket | csimarket.com | https://csimarket.com/stocks/RBKB-Customers RBKB's vs.
- (Revenue and Income for Trailing 12 Months, in Millions of $, except Employees).
- Market cap.CSIMarket Company, Sector, Industry, Market Analysis, Stock Quotes, Earnings, Economy, News and Research.

### Sources found
- [RBKB SEC Filings - Rhinebeck Bancorp, Inc. 10-K, 10-Q, 8-K Forms](https://www.stocktitan.net/sec-filings/RBKB/)
  - Jul 21, 2026 · Welcome to our dedicated page for Rhinebeck Bancorp SEC filings (Ticker: RBKB), a comprehensive resource for investors and traders seeking off…
- [RBKB (Rhinebeck Bancorp): De-risking Meets Margin Headwinds](https://graphvest.com/rbkb)
  - Jun 21, 2026 · Core thesis: The market is discounting the bank's structural de-risking, which reduced total borrowings to sixteen point four eight million do…
- [RBKB SEC Filings - Rhinebeck Bancorp, Inc.- Annual Report ...](https://fintel.io/sfs/us/rbkb)
  - Jul 17, 2026 · This page shows recent SEC filings related to Rhinebeck Bancorp, Inc.
- [Rhinebeck Bancorp (RBKB) 10K Form and Latest SEC Filings 2026](https://www.marketbeat.com/stocks/NASDAQ/RBKB/sec-filings/)
  - 4 days ago · For investors, these filings are the primary source of verified financial data — covering everything from annual revenue and debt levels in the …
- [Rare earth elements 2025 - Analysis - IEA](https://www.iea.org/reports/rare-earth-elements-2025)
  - Rare earth elements 2025 - Analysis and key findings. A report by the International Energy Agency.
- [Top 5 Uranium News Stories of 2025 | INN](https://investingnews.com/top-uranium-news-stories-2025/)
  - In 2025, uranium prices surged amid reactor restarts and new nuclear projects, drawing investor attention. The US aims to reduce reliance on Russian uranium,…
- [Commodity Prices | Commodity Market | Markets Insider](https://markets.businessinsider.com/commodities?op=1)
  - Get all information on the commodity market. Find the latest commodity prices including News, Charts, Realtime Quotes and even more about commodities.
- [Rare Earth Archives - MINING.COM](https://www.mining.com/commodity/rare-earth/)
  - Algae breakthrough could double rare earth concentrations Researchers found using algae is a cleaner way to concentrate rare earths and help the US strengthe…
- [Rhinebeck Bancorp, Inc. (RBKB) Stock Valuation... | Seeking Alpha](https://seekingalpha.com/symbol/RBKB/valuation/metrics)
  - Rhinebeck Bancorp, Inc. (RBKB) Valuation Grade and underlying metrics. Quant Ratings. PE ratios, EBITDA, EPS, cash flow, ROE. Compounded. Charts. Compare wit…
- [Rhinebeck Bancorp Inc Customers by Division and Industry - CSIMarket](https://csimarket.com/stocks/RBKB-Customers)
  - RBKB's vs. Customers, Data. (Revenue and Income for Trailing 12 Months, in Millions of $, except Employees). Company name. Market cap.CSIMarket Company, Sect…
- [RBKB 8-K & SEC Filings - Yahoo Finance](https://finance.yahoo.com/sec-filing/RBKB/0001751783-26-000035_1751783/)
  - RBKB 8-K and SEC filings offer investors the in-depth insights and information you've come to expect from Yahoo Finance.Highest open interest. Highest implie…
- [Rhinebeck Bank | Investor Relations](https://www.rhinebeckbank.com/Investor-Relations)
  - Rhinebeck Bank is a full service, locally focused bank headquartered in Poughkeepsie, NY. We offer a full range of personal checking, savings, money market a…

### Search warnings
- news:RBKB Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers: No results found.
- news:Rhinebeck Bancorp, Inc. RBKB outlook OR catalyst OR commodity OR uranium OR rare earth OR vanadium: No results found.
- news:RBKB sector drivers OR market demand: No results found.
- news:Rhinebeck Bancorp, Inc. RBKB backlog OR contract OR refinancing OR leverage: No results found.

## SEC filing [S24]
- Extraction OK: True
- Item 1 chars: 80000
- Item 1A chars: 50000
- Item 7 chars: 50000
- Meta: {'accession_number': '0001751783-26-000005', 'filing_date': '2026-03-13', 'source': 'edgartools', 'path': 'C:\\DevWork\\equity_research_agent\\data\\filings\\RBKB_10k.txt'}

## Qualitative analysis (local LLM)

_Item 1 Business summary mode: rule_based (see Company setup & business model)._

### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, uncertainty, litigation, regulation, competition, guidance, revenue, margin, supply chain, cyber, interest rate, customer, product, service, market, operations, network

- In addition to factors discussed in the description of our business and elsewhere in this report, the following are factors that could adversely affect our future results of operations and financial condition.
- Risks Related to Our Lending Activities  Our emphasis on commercial real estate and commercial business lending involves risks that could adversely affect our financial condition and results of operations.
- While these types of loans are potentially more profitable than residential mortgage loans due primarily to bearing generally higher interest rates and larger balances, they present greater risk  due to greater dependency on the successful operation of the properties and are generally more sensitive to regional and local economic conditions, making future losses more difficult to predict.
- Consequently, an adverse development with respect to one loan or one credit relationship can expose us to a  significantly greater risk of loss compared to an adverse development with respect to a residential mortgage loan.
- These loans also expose us to greater credit risk than loans secured by residential real estate because the collateral securing these loans typically cannot be liquidated as easily as residential real estate.
- Business - Loan Underwriting Risks.”  Our automobile loan portfolio exposes us to increased credit risks.
- Automobile loans are inherently risky as they are secured by assets that may be difficult to locate, have high loan-to-value ratios, and can depreciate rapidly.
- Furthermore, our consumer lending activities are subject to numerous consumer protection laws and regulations, and the application of various federal and state laws, including bankruptcy and insolvency laws, may limit our ability to recover on such loans.


### Item 7 — MD&A (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, margin, interest rate, customer, segment, product, service, market, operations, network

- and Analysis of Financial Condition and Results of Operations  This discussion and analysis reflects information contained in our audited consolidated financial statements and other relevant statistical data, and is intended to enhance your understanding of our financial condition and results of operations.
- Our primary sources of non-interest income are service charges on deposit accounts, investment advisory income, net gains in the cash surrender value of bank owned life insurance and other income.
- Our non-interest expenses consist of salaries and employee benefits, net occupancy and equipment, data processing, professional fees, marketing expenses, premium payments we make to the FDIC for insurance of our deposits and other general and administrative expenses.
- Smith’s executive leadership experience includes overseeing community bank operations, spearheading the implementation of digital banking and banking-as-a-service programs and integrating acquired financial institutions.
- As we realign our strategies  for growth, we intend to continue to operate as a well-capitalized and profitable community bank dedicated to providing exceptional personal service to our individual and business customers.
- We believe that we have a competitive advantage in the markets we serve because of our knowledge of the local marketplace and our long-standing history of providing superior, relationship-based customer service.
- Our current business strategy includes the following key components, which are designed to improve earnings by expanding our net interest margin, increasing non-interest income and improving efficiency:    Emphasize relationship-based commercial lending.
- ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────  Increasing our commercial real estate loans and commercial business loans involves risk, as described in “Risk Factors - Risks Related to Our Lending Activities - Our emphasis on commercial real estate and commercial business lending involves risks that could adversely affect our financial condition and results of operations” and “ - Our non-owner occupied commercial real estate loans may expose us to increased credit risk.”    Grow and enhance our low-cost deposit base.


## Research loop (think → act)

1. _heuristic_ — Coverage looks adequate for this pass; stopping iterative loop.

## Sources

- **[S1]** RBKB fundamentals (yfinance)
  - Rhinebeck Bancorp, Inc.: price=12.3, rev=53355000.0, fcf=10893000.0, shares=15638237.0, rev_cagr=0.03754424938432588, ROIC=None, FCF yield=0.056631046935612064
- **[S2]** RBKB EV/EBITDA valuation (multiples)
  - Base implied price=510.83258298234, multiple=8.0
- **[S3]** RBKB DCF valuation (dcf)
  - Base share price=32.4822323870783, bull=60.191263927521966, bear=14.204002046386439
- **[S4]** RBKB peer comps (peers)
  - Peers: JPM, BAC, WFC, C, GS; rows=6
- **[S5]** RBKB earnings history (earnings)
  - rows=0; next=None
- **[S6]** Rhinebeck Bancorp Inc (RBKB) Stock Forecast, Price Targets and... (web) — https://www.tipranks.com/stocks/rbkb/forecast
  - RBKB average Analyst price target in the past 3 months is ―. Each month's total comprises the sum of three months' worth of ratings.What is RBKB’s average 12-month price target,…
- **[S7]** Consensus and price targets from Wall Street analysts on RBKB. (web) — https://www.investing.com/equities/rhinebeck-insights?analysts&source=desktop&medium=instrument
  - Wall Street analyst price targets and ratings. Stock sentiment by bloggers, insiders, and financial gurus. News sentiment and score for thousands of stocks. Simplified screener …
- **[S8]** RBKB | Rhinebeck Bancorp Inc. Analyst Estimates | MarketWatch (web) — https://www.marketwatch.com/investing/stock/rbkb/analystestimates
  - RBKB Analyst Estimates. Snapshot. Average Recommendation.Stock Price Targets. High. N/A.
- **[S9]** Rhinebeck Bancorp, Inc. (RBKB) Analyst Ratings... - Yahoo Finance (web) — https://finance.yahoo.com/quote/RBKB/analysis/
  - See Rhinebeck Bancorp, Inc. (RBKB) stock analyst estimates, including earnings and revenue, EPS, upgrades and downgrades.NasdaqCM - Nasdaq Real Time Price•USD.
- **[S10]** Analyst Upgrades & Downgrades - MarketWatch (web) — https://www.marketwatch.com/tools/upgrades-downgrades
  - Real-time information on stock upgrades and downgrades by MarketWatch. View information on strong stocks to buy and weak stocks to sell.
- **[S11]** Upgrade - Personal Loans, Cards and Rewards Checking | Upgrade (web) — https://www.upgrade.com/
  - Check your rate for a personal loan up to $50,000 with low, fixed rates. Or get started with Upgrade Cards, Rewards Checking, and Premier Savings. Start in minutes.
- **[S12]** Downgrade: What It Is, How It Works, and Warning Signs (web) — https://www.investopedia.com/terms/d/downgrade.asp
  - A downgrade is a negative change in an estimate for a stock's performance, issued by an analyst for a financial services firm. Learn how it impacts investing strategies.
- **[S13]** Rhinebeck Bank | Home (web) — https://www.rhinebeckbank.com/
  - Rhinebeck Bank, Your Community Bank. From your banking needs to our community, see all that we have to offer. View options.
- **[S14]** RBKB SEC Filings - Rhinebeck Bancorp, Inc. 10-K, 10-Q, 8-K Forms (web) — https://www.stocktitan.net/sec-filings/RBKB/
  - Jul 21, 2026 · Welcome to our dedicated page for Rhinebeck Bancorp SEC filings (Ticker: RBKB), a comprehensive resource for investors and traders seeking official regulatory doc…
- **[S15]** RBKB (Rhinebeck Bancorp): De-risking Meets Margin Headwinds (web) — https://graphvest.com/rbkb
  - Jun 21, 2026 · Core thesis: The market is discounting the bank's structural de-risking, which reduced total borrowings to sixteen point four eight million dollars. This aggressi…
- **[S16]** RBKB SEC Filings - Rhinebeck Bancorp, Inc.- Annual Report ... (web) — https://fintel.io/sfs/us/rbkb
  - Jul 17, 2026 · This page shows recent SEC filings related to Rhinebeck Bancorp, Inc.
- **[S17]** Rhinebeck Bancorp (RBKB) 10K Form and Latest SEC Filings 2026 (web) — https://www.marketbeat.com/stocks/NASDAQ/RBKB/sec-filings/
  - 4 days ago · For investors, these filings are the primary source of verified financial data — covering everything from annual revenue and debt levels in the 10-K, to material bu…
- **[S18]** Rare earth elements 2025 - Analysis - IEA (web) — https://www.iea.org/reports/rare-earth-elements-2025
  - Rare earth elements 2025 - Analysis and key findings. A report by the International Energy Agency.
- **[S19]** Top 5 Uranium News Stories of 2025 | INN (web) — https://investingnews.com/top-uranium-news-stories-2025/
  - In 2025, uranium prices surged amid reactor restarts and new nuclear projects, drawing investor attention. The US aims to reduce reliance on Russian uranium, while China leads i…
- **[S20]** Commodity Prices | Commodity Market | Markets Insider (web) — https://markets.businessinsider.com/commodities?op=1
  - Get all information on the commodity market. Find the latest commodity prices including News, Charts, Realtime Quotes and even more about commodities.
- **[S21]** Rare Earth Archives - MINING.COM (web) — https://www.mining.com/commodity/rare-earth/
  - Algae breakthrough could double rare earth concentrations Researchers found using algae is a cleaner way to concentrate rare earths and help the US strengthen critical mineral s…
- **[S22]** RBKB SEC Filings - Rhinebeck Bancorp, Inc. 10-K, 10-Q, 8-K Forms (web_page) — https://www.stocktitan.net/sec-filings/RBKB/
  - RBKB SEC Filings - Rhinebeck Bancorp, Inc. 10-K, 10-Q, 8-K Forms Home SEC-Filings RBKB Rhinebeck Bancorp, Inc. SEC Filings RBKB NASDAQ Follow Welcome to our dedicated page for R…
- **[S23]** RBKB (Rhinebeck Bancorp): De-risking Meets Margin Headwinds | RBKB - GraphVest (web_page) — https://graphvest.com/rbkb
  - RBKB (Rhinebeck Bancorp): De-risking Meets Margin Headwinds | RBKB - GraphVest R RBKB Rhinebeck Bancorp, Inc. $12.43 +$0.08 (+0.65%) Mkt Cap: $194.38M RBKB Price Action & Cataly…
- **[S24]** RBKB 10-K (sec)
  - Item 1 chars=80000, Item 1A chars=50000, Item 7 chars=50000, ok=True, source=edgartools
- **[S25]** RBKB 8-K 2026-07-23 (sec) — https://www.sec.gov/Archives/edgar/data/1751783/000175178326000035/rbkb-20260723x8k.htm
  - 8-K
- **[S26]** RBKB 8-K 2026-07-21 (sec) — https://www.sec.gov/Archives/edgar/data/1751783/000175178326000032/rbkb-20260721x8k.htm
  - 8-K
- **[S27]** RBKB 8-K 2026-07-17 (sec) — https://www.sec.gov/Archives/edgar/data/1751783/000175178326000029/rbkb-20260717x8k.htm
  - 8-K
- **[S28]** RBKB 8-K 2026-06-29 (sec) — https://www.sec.gov/Archives/edgar/data/1751783/000175178326000027/rbkb-20260629x8k.htm
  - 8-K
- **[S29]** RBKB 8-K 2026-05-26 (sec) — https://www.sec.gov/Archives/edgar/data/1751783/000175178326000022/rbkb-20260526x8k.htm
  - 8-K
- **[S30]** RBKB 8-K 2026-05-19 (sec) — https://www.sec.gov/Archives/edgar/data/1751783/000175178326000020/rbkb-20260519x8k.htm
  - 8-K
- **[S31]** RBKB 8-K 2026-05-14 (sec) — https://www.sec.gov/Archives/edgar/data/1751783/000110465926061328/tm2614362d1_8k.htm
  - FORM 8-K
- **[S32]** RBKB 10-Q 2026-05-14 (sec) — https://www.sec.gov/Archives/edgar/data/1751783/000175178326000018/rbkb-20260331x10q.htm
  - 10-Q
- **[S33]** Item 1 Business summary (nlp)
  - ### Item 1 — Business (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, regulation, competition, margin, interest rate, customer, segment, product, service, mar…
- **[S34]** Item 1A summary (nlp)
  - ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, guidance, revenue, margin, supply…
- **[S35]** Item 7 summary (nlp)
  - ### Item 7 — MD&A (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, margin, interest rate, customer, segment, product, service, market, operations, network  - a…
- **[S36]** RBKB scenario price ranges (scenarios)
  - ok=True; base mid=541.5265800102659; headwinds=5; tailwinds=8
- **[S37]** RBKB driver analysis (drivers)
  - ok=True; drivers=7
- **[S38]** RBKB memo sections (memo)
  - mode=rules; proxies=4

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

# Template: Valuation (DCF + Street + drivers) (`valuation`)

# RBKB — Planned Research Report

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
- Company: Rhinebeck Bancorp, Inc.
- Sector / industry: Financial Services / Banks - Regional
- Price: 12.3
- 52-week range: $6.74 – $12.88
- Market cap: $192.35M
- Enterprise value: -$161.05M
- Shares outstanding: 15.64M
- Beta: 0.148
- Book equity: $136.85M
- Revenue (latest): $53.35M
- EBITDA (latest): —
- Free cash flow (latest): $10.89M
- Operating income: —
- Operating margin: —
- EV / EBITDA: —
- ROIC: —
- FCF yield: 5.7%
- Debt / Equity: 0.22146552480051443
- FCF / share: $0.70
- Revenue / share: $3.41

### Capital structure
- Cash: $18.83M
- Short-term debt: $1.61M
- Long-term debt: $28.69M
- Total debt: $30.31M
- Net debt: $11.48M
- Net debt / EBITDA: —

### Growth
- Revenue CAGR: 3.8%
- FCF CAGR: -7.3%
- Latest revenue YoY: 85.7%
- Latest FCF YoY: 41.9%

### Market expectations (yfinance, sparse)
- Mean target: —
- Target range: — – —
- Recommendation: none

_Consensus revenue/EBITDA forecasts are often unavailable via free feeds; treat targets as point-in-time only._

### Historical KPIs (multi-year)

| Year | Revenue | OCF | Capex | FCF | EBITDA | LT debt | Cash | Net debt | Net income |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2025 | $53.35M | $11.74M | $850.00K | $10.89M | — | $28.69M | $18.83M | $9.87M | $10.04M |
| 2024 | $28.73M | $8.47M | $791.00K | $7.68M | — | $74.93M | $19.18M | $55.75M | -$8.62M |
| 2023 | $43.70M | $7.05M | $578.00K | $6.47M | — | $133.22M | $14.61M | $118.61M | $4.39M |
| 2022 | $47.77M | $14.79M | $1.13M | $13.66M | — | $62.88M | $16.82M | $46.06M | $7.00M |

## Charts

### Revenue & FCF history
![Revenue & FCF history](/charts/RBKB_valuation_revenue_fcf.png)

### DCF scenario prices
![DCF scenario prices](/charts/RBKB_valuation_dcf_scenarios.png)

### Base-case FCF path
![Base-case FCF path](/charts/RBKB_valuation_base_fcf_path.png)

### EV/EBITDA scenario prices
![EV/EBITDA scenario prices](/charts/RBKB_valuation_ev_ebitda_scenarios.png)

### Headwind/tailwind price ranges
![Headwind/tailwind price ranges](/charts/RBKB_valuation_scenario_ranges.png)

## DCF valuation (base / bull / bear) [S2]

> Simplified revenue->FCF DCF. Not investment advice; assumptions are editable heuristics.

- Spot price: $12.30
- Base revenue: $53.35M
- Shares: 15,638,237
- Net debt (Debt−Cash): $11.48M

| Scenario | Growth | FCF margin | WACC | Term. g | Equity value | Share price | Upside |
|----------|--------|------------|------|---------|--------------|-------------|--------|
| bear | 25.0% | 18.4% | 12.0% | 1.5% | $222.13M | $14.20 | 15.5% |
| base | 35.0% | 20.4% | 10.0% | 2.5% | $507.96M | $32.48 | 164.1% |
| bull | 42.0% | 23.4% | 9.0% | 3.0% | $941.29M | $60.19 | 389.4% |

### Assumption notes
- Base revenue growth seeded from historical rate (85.7%).


### Base-case projected FCF

- Year 1: revenue $72.03M, FCF $14.71M (PV $13.37M)
- Year 2: revenue $97.24M, FCF $19.85M (PV $16.41M)
- Year 3: revenue $131.27M, FCF $26.80M (PV $20.14M)
- Year 4: revenue $177.22M, FCF $36.18M (PV $24.71M)
- Year 5: revenue $239.25M, FCF $48.84M (PV $30.33M)
- Terminal value $667.54M (PV $414.49M)

## Valuation — EV/EBITDA scenarios [S3]

> Priced-in model: implied price = (EBITDA × EV/EBITDA − net debt) ÷ shares. Not a forecast.

- Spot: $12.30
- Net debt used: $11.48M

| Scenario | EBITDA | EV/EBITDA | Implied EV | Equity value | Implied price |
|---|---:|---:|---:|---:|---:|
| bear | $700.00M | 6.0x | $4.20B | $4.19B | $267.84 |
| base | $1.00B | 8.0x | $8.00B | $7.99B | $510.83 |
| bull | $1.20B | 10.0x | $12.00B | $11.99B | $766.62 |

- EBITDA missing or non-positive; scenarios use placeholder $1B EBITDA — edit before relying on prices.
- No current EV/EBITDA; defaulted base multiple to 8.0x.

## Scenario price ranges (headwinds & tailwinds) [S27]

> Medium-term (18–36 months (medium / medium-long term)) driver → EV/EBITDA bridge. Distinct from the FCF DCF path. Not investment advice.

- Spot: $12.30
- Anchor multiple: 8.0x (driver_ev_ebitda_bridge)
- Anchor EBITDA: $1.00B
- Probability-weighted midpoint: **$564.99** (heuristic weights, not a rating)
- Driver extraction: `rules`

### Headwinds (bear-case fuel)

- **Balance-sheet / refinancing pressure** — sector=Financial Services industry=Banks - Regional revenue=53355000.0 ebitda=None fcf=10893000.0 net_debt=11479000.0 nd_ebitda=None target=None rec=none _(source: fundamentals)_
- **Regulatory / legal risk** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, guidance, revenue, margin, supply ch _(source: item_1a)_
- **Competitive / pricing pressure** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, guidance, revenue, margin, supply ch _(source: item_1a)_
- **Margin / cost headwind** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, guidance, revenue, margin, supply ch _(source: item_1a)_
- **Operational / cyber risk** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, guidance, revenue, margin, supply ch _(source: item_1a)_

### Tailwinds (bull-case fuel)

- **Positive free cash flow** — FCF $10.89M (yield 5.7%) _(source: fundamentals)_
- **Revenue growth momentum** — Latest revenue YoY ≈ 85.7% _(source: fundamentals)_
- **Contract / backlog wins** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, guidance, revenue, margin, supply ch _(source: item_1a)_
- **Product / pricing power** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, guidance, revenue, margin, supply ch _(source: item_1a)_
- **Growth / execution upside** — ### Item 7 — MD&A (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, margin, interest rate, customer, segment, product, service, market, operations, network - and A _(source: item_7)_
- **Margin expansion / cost takeout** — ### Item 7 — MD&A (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, margin, interest rate, customer, segment, product, service, market, operations, network - and A _(source: item_7)_
- **Multiple re-rating / Street upgrades** — RBKB Analyst Ratings, Price Targets and Consensus | Rallies See RBKB analyst ratings, consensus rating, price targets, upgrades, downgrades, analyst firms, and recent Wall Street r _(source: web)_

### Price ranges by case

| Case | Prob. | Metric vs TTM | Multiple | Price low | Mid | High | Upside vs spot |
|---|---:|---:|---:|---:|---:|---:|---:|
| bear | 0.21 | 0.74x | 5.3x | $224.13 | $249.12 | $274.10 | +1925% |
| base | 0.45 | 1.04x | 8.0x | $494.05 | $531.30 | $568.54 | +4219% |
| bull | 0.34 | 1.23x | 10.2x | $724.14 | $804.68 | $885.22 | +6442% |

#### Bear — headwinds dominate

Headwinds bite: weaker operating trajectory and multiple compression. Equity duration shrinks if cash generation fails to offset leverage / competitive pressure.

- **Range:** $224.13 – $274.10 (mid $249.12) · EBITDA $740.00M · multiple 5.3x
- Driver: **Balance-sheet / refinancing pressure** — sector=Financial Services industry=Banks - Regional revenue=53355000.0 ebitda=None fcf=10893000.0 net_debt=11479000.0 nd_ebitda=None target=None rec=none
- Driver: **Regulatory / legal risk** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, guidance, revenu
- Driver: **Competitive / pricing pressure** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, guidance, revenu
- Driver: **Margin / cost headwind** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, guidance, revenu
- Driver: **Operational / cyber risk** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, guidance, revenu

#### Base — mixed execution

Balanced path: some tailwinds offset headwinds. Operating scale roughly holds with modest repair/normalization; valuation stays near the current EV/EBITDA anchor.

- **Range:** $494.05 – $568.54 (mid $531.30) · EBITDA $1.04B · multiple 8.0x
- Driver: **Positive free cash flow** — FCF $10.89M (yield 5.7%)
- Driver: **Revenue growth momentum** — Latest revenue YoY ≈ 85.7%
- Driver: **Balance-sheet / refinancing pressure** — sector=Financial Services industry=Banks - Regional revenue=53355000.0 ebitda=None fcf=10893000.0 net_debt=11479000.0 nd_ebitda=None target=None rec=none
- Driver: **Regulatory / legal risk** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, guidance, revenu

#### Bull — tailwinds dominate

Tailwinds compound: operating improvement plus a re-rating toward peer or recovery multiples as balance-sheet and growth narratives improve.

- **Range:** $724.14 – $885.22 (mid $804.68) · EBITDA $1.23B · multiple 10.2x
- Driver: **Positive free cash flow** — FCF $10.89M (yield 5.7%)
- Driver: **Revenue growth momentum** — Latest revenue YoY ≈ 85.7%
- Driver: **Contract / backlog wins** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, guidance, revenu
- Driver: **Product / pricing power** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, guidance, revenu
- Driver: **Growth / execution upside** — ### Item 7 — MD&A (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, margin, interest rate, customer, segment, product, service, market, operati

### Method notes

- Item 1A risks weighted toward headwinds.
- Current ev_ebitda multiple missing; anchored at 8.0x.
- Mapping follows Gemini/Perplexity-style scenario memos: qualitative drivers → operating metric & multiple paths → share-price ranges over a medium-term horizon.

## Web research — web_analysts

- Queries: RBKB analyst price target, Rhinebeck Bancorp, Inc. stock rating OR consensus OR upgrade OR downgrade, RBKB Estimate intrinsic value under base / bull / bear scenarios analyst
- Unique hits: 12
- Pages fetched: 3/3

### Web synthesis — web_analysts (rule-based fallback — Ollama unavailable)
**Keyword hits:** revenue, margin, customer, service, market

- [HIT] Berkshire Hathaway (BRK.B) Stock Forecast & Price Target | www.marketbeat.com | https://www.marketbeat.com/stocks/NYSE/BRK-B/forecast/ BRK.B's current price target is $524.50.
- Learn why top analysts are making this stock forecast for Berkshire Hathaway at MarketBeat.
- [HIT] RBKB Stock Quote Price and Forecast - CNN | www.cnn.com | https://www.cnn.com/markets/stocks/RBKB Rhinebeck Bancorp Inc · Price Momentum.
- Common Stock (RBKB) is a publicly traded Financial Services sector company.
- As of July 28, 2026, RBKB trades at $12.41 with a market cap of $194.38M and a P/E ratio of 13.51.
- RBKB Key Metrics Key financial metrics for RBKB Metric Value Price $12.41 Market Cap $194.38M P/E Ratio 13.51 EPS $0.92 Dividend Yield 0.00% 52-Week High $17.99 52-Week Low $9.31 Volume 11.36K Avg Volume 0 Revenue (TTM) $2.98M Net Income $9.97M Gross Margin 0.00% RBKB Analyst Consensus RBKB analyst coverage data.
- [PAGE] Berkshire Hathaway (BRK.B) Stock Forecast and Price Target 2026 | https://www.marketbeat.com/stocks/NYSE/BRK-B/forecast/ Berkshire Hathaway (BRK.B) Stock Forecast and Price Target 2026 Skip to main content → The dollar reset no one told you about (From Porter & Company) (Ad) Free BRK.B Stock Alerts Berkshire Hathaway (BRK.B)  Stock Forecast & Price Target $497.09 +2.16 (+0.44%) Closing price 07/27/2026 03:59 PM Eastern Extended Trading $496.80 -0.28 (-0.06%) As of 07/27/2026 07:59 PM Eastern Extended trading is trading that happens on electronic markets outside of regular trading hours.
- This is a fair market value extended hours price provided by Massive.

### Sources found
- [RBKB Analyst Ratings, Price Targets and Consensus | Rallies](https://rallies.ai/research/RBKB/analysts)
  - See RBKB analyst ratings, consensus rating, price targets, upgrades, downgrades, analyst firms, and recent Wall Street rating changes.
- [Berkshire Hathaway (BRK.B) Stock Forecast & Price Target](https://www.marketbeat.com/stocks/NYSE/BRK-B/forecast/)
  - BRK.B's current price target is $524.50. Learn why top analysts are making this stock forecast for Berkshire Hathaway at MarketBeat.
- [RBKB Analyst Ratings & Price Targets 2026 - Lician](https://lician.com/analyst/rbkb)
  - RBKB analyst ratings and price targets. See Wall Street recommendations, consensus rating, average price target, and analyst upgrades/downgrades.
- [RBKB Price Target 2026 - Analyst Target Prices & Forecast | Lician](https://lician.com/target-price/rbkb)
  - RBKB price target and analyst target prices. See average, high, low price targets, consensus estimates, and upside potential from Wall Street analysts.
- [Rhinebeck Bancorp Inc Ordinary Shares (RBKB) - Morningstar](https://www.morningstar.com/stocks/xnas/rbkb/quote)
  - See the latest Rhinebeck Bancorp Inc Ordinary Shares stock price ... Rhinebeck Bancorp Inc Ordinary Shares RBKB. Morningstar Rating. Unlock. Stock XNAS Ratin…
- [Rhinebeck Bancorp, Inc. (RBKB) Stock Price, News, Quote & History](https://finance.yahoo.com/quote/RBKB/)
  - Find the latest Rhinebeck Bancorp, Inc. (RBKB) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [RBKB Stock Price Quote & News - Rhinebeck Bancorp - Robinhood](https://robinhood.com/us/en/stocks/RBKB/)
  - On 2026-07-26, Rhinebeck Bancorp(RBKB) stock moved within a range of $12.34 to $12.70. With shares now at $12.43, the stock is trading +0.8% above its intrad…
- [RBKB Stock Quote Price and Forecast - CNN](https://www.cnn.com/markets/stocks/RBKB)
  - Rhinebeck Bancorp Inc · Price Momentum. RBKB is trading in the middle of its 52-week range and below its 200-day simple moving average. · Price change. The p…
- [RBKB Intrinsic Valuation and Fundamental Analysis - Rhinebeck ...](https://www.alphaspread.com/security/nasdaq/rbkb/summary)
  - Rhinebeck Bancorp Inc (NASDAQ:RBKB) Intrinsic Valuation. Check if RBKB is overvalued or undervalued under the bear, base, and bull scenarios of the company's…
- [RBKB (RBKB) Intrinsic Value & DCF Valuation 2026 | VCP Scanner](https://vcpscanner.com/valuation/rbkb/dcf)
  - RBKB (RBKB) intrinsic value, DCF model, and fair value analysis. See bear, base, and bull case scenarios with full assumptions. Updated 2026.
- [Rhinebeck Bancorp, Inc. (RBKB) Estimates & Forecasts — EPS ...](https://vcpscanner.com/valuation/rbkb/estimates)
  - Our scenario-based model produces three price targets for Rhinebeck Bancorp, Inc.: Bear case $8, Base case $11, and Bull case $39. These targets are derived …
- [Intrinsik — Stock Valuation Tool | Fair Value in 60 Seconds](https://intrinsik.io/)
  - Institutional-grade stock valuation in 60 seconds. DCF model with bear, base & bull scenarios, SEC filing extraction, sensitivity tables, and 26 analysis pan…

### Search warnings
- news:RBKB analyst price target: No results found.
- news:Rhinebeck Bancorp, Inc. stock rating OR consensus OR upgrade OR downgrade: No results found.
- news:RBKB Estimate intrinsic value under base / bull / bear scenarios analyst: No results found.

## Web research — web_drivers

- Queries: RBKB Estimate intrinsic value under base / bull / bear scenarios, Rhinebeck Bancorp, Inc. RBKB outlook OR catalyst OR commodity OR uranium OR rare earth OR vanadium, RBKB sector drivers OR market demand
- Unique hits: 12
- Pages fetched: 0/3

### Web synthesis — web_drivers (rule-based fallback — Ollama unavailable)
**Keyword hits:** revenue, customer, market

- Find market predictions, RBKB financials and market news.
- [HIT] Rhinebeck Bancorp Inc Customers by Division and Industry - CSIMarket | csimarket.com | https://csimarket.com/stocks/RBKB-Customers RBKB's vs.
- (Revenue and Income for Trailing 12 Months, in Millions of $, except Employees).
- Market cap.CSIMarket Company, Sector, Industry, Market Analysis, Stock Quotes, Earnings, Economy, News and Research.
- | Aim.market | aim.market | https://aim.market/ru Нажмите кнопку продажи, подтвердите обмен в приложении Steam на телефоне и выберите удобный способ вывода.
- Вы можете продать скины с моментальным выводом на банковские карты, СБП, баланс Aim Market или в криптовалюту.

### Sources found
- [RBRK Intrinsic Valuation and Fundamental Analysis - Rubrik Inc - Alpha Spread](https://www.alphaspread.com/security/nyse/rbrk/summary)
  - The intrinsic value of one RBRK stock under the Base Case scenario is 28.16 USD.
- [3 Ways of Calculating a Stock's Intrinsic Value - HubPages](https://discover.hubpages.com/money/Stock-Valuation-Using-Bear-Bull-and-Base-Case-Scenarios)
  - September 12, 2024 - When calculating intrinsic value, it can be helpful to have 3 probability-weighted, projected scenarios mapped out in order to dial in a…
- [3 Ways of Calculating a Stock's Intrinsic Value - ToughNickel](https://toughnickel.com/personal-finance/Stock-Valuation-Using-Bear-Bull-and-Base-Case-Scenarios)
  - March 22, 2023 - When calculating intrinsic value, it can be helpful to have 3 probability-weighted, projected scenarios mapped out in order to dial in a spe…
- [Bull Base Bear Valuation for One Stock | Model Reef](https://modelreef.io/resources/articles/stock-valuation/how-to-create-a-bull-base-bear-valuation-for-one-stock-scenario-driven-intrinsic-value)
  - April 15, 2026 - The point of bull/base/bear is to show what must be true-not to pretend the world can be summarised in one number. If you want a quick quali…
- [Rhinebeck Bancorp, Inc. (RBKB) Stock Price, News... - Yahoo Finance](https://finance.yahoo.com/quote/RBKB/)
  - Find the latest Rhinebeck Bancorp, Inc. (RBKB) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Rhinebeck Bancorp, Inc. (RBKB) Stock Price, Quote... | Seeking Alpha](https://seekingalpha.com/symbol/RBKB)
  - A high-level overview of Rhinebeck Bancorp, Inc. (RBKB) stock. View (RBKB) real-time stock price, chart, news, analysis, analyst reviews and more.
- [RBKB Stock Price and Chart — NASDAQ:RBKB — TradingView](https://www.tradingview.com/symbols/NASDAQ-RBKB/)
  - View live Rhinebeck Bancorp, Inc. chart to track its stock's price action. Find market predictions, RBKB financials and market news.
- [Rhinebeck Bancorp Inc Stock Price Today | NASDAQ: RBKB Live](https://www.investing.com/equities/rhinebeck)
  - POUGHKEEPSIE, N.Y. - Rhinebeck Bancorp, Inc. (NASDAQ:RBKB) announced today it has commenced a stock offering of up to 8,912,500... Investing.com. May 26, 2026.
- [Rhinebeck Bancorp, Inc. (RBKB) Stock Valuation... | Seeking Alpha](https://seekingalpha.com/symbol/RBKB/valuation/metrics)
  - Rhinebeck Bancorp, Inc. (RBKB) Valuation Grade and underlying metrics. Quant Ratings. PE ratios, EBITDA, EPS, cash flow, ROE. Compounded. Charts. Compare wit…
- [Rhinebeck Bancorp Inc Customers by Division and Industry - CSIMarket](https://csimarket.com/stocks/RBKB-Customers)
  - RBKB's vs. Customers, Data. (Revenue and Income for Trailing 12 Months, in Millions of $, except Employees). Company name. Market cap.CSIMarket Company, Sect…
- [RBKB 8-K & SEC Filings - Yahoo Finance](https://finance.yahoo.com/sec-filing/RBKB/0001751783-26-000035_1751783/)
  - RBKB 8-K and SEC filings offer investors the in-depth insights and information you've come to expect from Yahoo Finance.Highest open interest. Highest implie…
- [Продать скины КС2 выгодно: моментальный вывод... | Aim.market](https://aim.market/ru)
  - Нажмите кнопку продажи, подтвердите обмен в приложении Steam на телефоне и выберите удобный способ вывода. Вы можете продать скины с моментальным выводом на …

### Search warnings
- news:RBKB Estimate intrinsic value under base / bull / bear scenarios: No results found.
- news:Rhinebeck Bancorp, Inc. RBKB outlook OR catalyst OR commodity OR uranium OR rare earth OR vanadium: No results found.
- news:RBKB sector drivers OR market demand: No results found.

## SEC filing [S23]
- Extraction OK: True
- Item 1 chars: 80000
- Item 1A chars: 50000
- Item 7 chars: 50000
- Meta: {'source': 'cache', 'path': 'C:\\DevWork\\equity_research_agent\\data\\filings\\RBKB_10k.txt'}

## Company setup & business model

**Keyword hits:** risk, regulation, competition, margin, interest rate, customer, segment, product, service, market, operations

- The Company is regulated by the Board of Governors of the Federal Reserve System (the “Federal Reserve Board”) and the New York State Department of Financial Services (the “NYSDFS”).
- We provide a full range of banking and financial services to consumer and commercial customers through our corporate office and 12 branches located in Dutchess, Orange and Ulster Counties.
- We also maintain a representative office in Albany County to originate indirect automobile and commercial loans and a representative office in Dutchess County for financial services.
- Financial services, including investment  advisory and financial product sales, are offered through a division of the Bank doing business as Rhinebeck Asset Management (“RAM”).
- We offer a variety of deposit accounts, including savings accounts, certificates of deposit, money market accounts, commercial and personal checking accounts and individual retirement accounts.
- We are subject to regulation and examination by the NYSDFS and by the Federal Deposit Insurance Corporation (the “FDIC”).
- Market Area  Our primary market area encompasses Dutchess, Orange, Ulster and Albany Counties (and their contiguous counties), which are located in the Hudson Valley region of New York.
- The Hudson Valley region has a diversified economy and representative industries include education, health, government, leisure and hospitality and professional business services.
- The four counties in our primary market area each had a lower unemployment rate than New York State (Dutchess County, 3.2%, Orange County, 3.6%, Ulster County, 3.5% and Albany County, 3.3%).
- Competition  We face significant competition for deposits and loans.
- Our most direct competition for deposits has historically come from the numerous financial institutions operating in our market area (including other community and commercial banks, credit unions and financial technology companies), many of which are significantly larger than we are and have greater resources.
- We also face competition for investors’ funds from other sources such as brokerage firms, money market funds and mutual funds, as  well as securities, such as Treasury bills, offered by the Federal Government.
- Based on FDIC data, at June 30, 2025 (the latest date for which information is available), we had 10.44% of the FDIC-insured deposit market share in Dutchess County, which was fourth among the 15 institutions with offices in the county, 1.59% of the FDIC-insured deposit market share in Ulster County, which was 12thamong the 18 institutions with offices in the county, and 1.28% of the FDIC-insured deposit market share  in Orange County, which was 14thamong the 22 institutions with offices in the county.
- We expect competition to remain intense in the future as a result of legislative, regulatory and technological changes and the continuing trend of consolidation in the financial services industry.
- Technological advances, for example, have lowered barriers to entry, allowed banks to expand their geographic reach by providing services over the internet and made it possible for non-depository institutions, including financial technology companies, to offer products and services that traditionally  have been provided by banks.
- Competition for deposits and the origination of loans could limit our growth in the future.
- We seek to meet this competition with convenient branch locations and online offerings, emphasizing personalized banking and the advantage of local decision-making in our banking businesses.
- Specifically, we promote and maintain relationships and build customer loyalty within local communities by focusing our marketing and community involvement on the specific needs of individual neighborhoods.
- At December  31, 2025, substantially all of our commercial real estate loans were secured by properties located in our market area.
- However, occasionally we will originate commercial real estate loans on properties located outside our market area based on an established relationship with a strong borrower.
- The interest rate on commercial real estate loans is generally adjustable and based on a margin over an index, typically The Wall Street Journal Prime Rate or the Federal Home Loan Bank of New York Amortizing Advance Rate.
- We selectively offer interest rate swaps for both commercial and multi-family real estate loans.
- In underwriting commercial real estate loans, we consider a number of factors, including the projected net cash flows to the loan’s debt service requirement (generally requiring a minimum of 1.20x), the age and condition of the collateral, the financial resources and income level of the borrower and the borrower’s experience in owning or managing similar properties.
- Our multi-family real estate loans are generally secured by multi-unit rental properties, consisting of five to 100 rental units, in our market area.
- The interest rates on our multi-family real estate loans are generally adjustable based on a margin over an index.
- In underwriting multi-family real estate loans, we consider a number of factors including the projected net cash flows to the loan’s debt service requirement (generally requiring a minimum of 1.20x), the age and condition of the collateral, the financial resources and income level of the borrower, and the borrower’s experience in owning or managing similar properties.
- All these loans are secured by properties located in our primary market area.
- The interest rate is generally a variable rate based on an index rate, typically The Wall Street Journal Prime Rate plus a margin.

_Source: latest 10-K Item 1 (Business), summarized locally._

## Qualitative analysis (local LLM)

### Item 1 — Business (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, regulation, competition, margin, interest rate, customer, segment, product, service, market, operations

- The Company is regulated by the Board of Governors of the Federal Reserve System (the “Federal Reserve Board”) and the New York State Department of Financial Services (the “NYSDFS”).
- We provide a full range of banking and financial services to consumer and commercial customers through our corporate office and 12 branches located in Dutchess, Orange and Ulster Counties.
- We also maintain a representative office in Albany County to originate indirect automobile and commercial loans and a representative office in Dutchess County for financial services.
- Financial services, including investment  advisory and financial product sales, are offered through a division of the Bank doing business as Rhinebeck Asset Management (“RAM”).
- We offer a variety of deposit accounts, including savings accounts, certificates of deposit, money market accounts, commercial and personal checking accounts and individual retirement accounts.
- We are subject to regulation and examination by the NYSDFS and by the Federal Deposit Insurance Corporation (the “FDIC”).
- Market Area  Our primary market area encompasses Dutchess, Orange, Ulster and Albany Counties (and their contiguous counties), which are located in the Hudson Valley region of New York.
- The Hudson Valley region has a diversified economy and representative industries include education, health, government, leisure and hospitality and professional business services.
- The four counties in our primary market area each had a lower unemployment rate than New York State (Dutchess County, 3.2%, Orange County, 3.6%, Ulster County, 3.5% and Albany County, 3.3%).
- Competition  We face significant competition for deposits and loans.
- Our most direct competition for deposits has historically come from the numerous financial institutions operating in our market area (including other community and commercial banks, credit unions and financial technology companies), many of which are significantly larger than we are and have greater resources.
- We also face competition for investors’ funds from other sources such as brokerage firms, money market funds and mutual funds, as  well as securities, such as Treasury bills, offered by the Federal Government.
- Based on FDIC data, at June 30, 2025 (the latest date for which information is available), we had 10.44% of the FDIC-insured deposit market share in Dutchess County, which was fourth among the 15 institutions with offices in the county, 1.59% of the FDIC-insured deposit market share in Ulster County, which was 12thamong the 18 institutions with offices in the county, and 1.28% of the FDIC-insured deposit market share  in Orange County, which was 14thamong the 22 institutions with offices in the county.
- We expect competition to remain intense in the future as a result of legislative, regulatory and technological changes and the continuing trend of consolidation in the financial services industry.
- Technological advances, for example, have lowered barriers to entry, allowed banks to expand their geographic reach by providing services over the internet and made it possible for non-depository institutions, including financial technology companies, to offer products and services that traditionally  have been provided by banks.
- Competition for deposits and the origination of loans could limit our growth in the future.
- We seek to meet this competition with convenient branch locations and online offerings, emphasizing personalized banking and the advantage of local decision-making in our banking businesses.
- Specifically, we promote and maintain relationships and build customer loyalty within local communities by focusing our marketing and community involvement on the specific needs of individual neighborhoods.
- At December  31, 2025, substantially all of our commercial real estate loans were secured by properties located in our market area.
- However, occasionally we will originate commercial real estate loans on properties located outside our market area based on an established relationship with a strong borrower.
- The interest rate on commercial real estate loans is generally adjustable and based on a margin over an index, typically The Wall Street Journal Prime Rate or the Federal Home Loan Bank of New York Amortizing Advance Rate.
- We selectively offer interest rate swaps for both commercial and multi-family real estate loans.
- In underwriting commercial real estate loans, we consider a number of factors, including the projected net cash flows to the loan’s debt service requirement (generally requiring a minimum of 1.20x), the age and condition of the collateral, the financial resources and income level of the borrower and the borrower’s experience in owning or managing similar properties.
- Our multi-family real estate loans are generally secured by multi-unit rental properties, consisting of five to 100 rental units, in our market area.
- The interest rates on our multi-family real estate loans are generally adjustable based on a margin over an index.
- In underwriting multi-family real estate loans, we consider a number of factors including the projected net cash flows to the loan’s debt service requirement (generally requiring a minimum of 1.20x), the age and condition of the collateral, the financial resources and income level of the borrower, and the borrower’s experience in owning or managing similar properties.
- All these loans are secured by properties located in our primary market area.
- The interest rate is generally a variable rate based on an index rate, typically The Wall Street Journal Prime Rate plus a margin.


### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, uncertainty, litigation, regulation, competition, guidance, revenue, margin, supply chain, cyber, interest rate, customer, product, service, market, operations, network

- In addition to factors discussed in the description of our business and elsewhere in this report, the following are factors that could adversely affect our future results of operations and financial condition.
- Risks Related to Our Lending Activities  Our emphasis on commercial real estate and commercial business lending involves risks that could adversely affect our financial condition and results of operations.
- While these types of loans are potentially more profitable than residential mortgage loans due primarily to bearing generally higher interest rates and larger balances, they present greater risk  due to greater dependency on the successful operation of the properties and are generally more sensitive to regional and local economic conditions, making future losses more difficult to predict.
- Consequently, an adverse development with respect to one loan or one credit relationship can expose us to a  significantly greater risk of loss compared to an adverse development with respect to a residential mortgage loan.
- These loans also expose us to greater credit risk than loans secured by residential real estate because the collateral securing these loans typically cannot be liquidated as easily as residential real estate.
- Business - Loan Underwriting Risks.”  Our automobile loan portfolio exposes us to increased credit risks.
- Automobile loans are inherently risky as they are secured by assets that may be difficult to locate, have high loan-to-value ratios, and can depreciate rapidly.
- Furthermore, our consumer lending activities are subject to numerous consumer protection laws and regulations, and the application of various federal and state laws, including bankruptcy and insolvency laws, may limit our ability to recover on such loans.


### Item 7 — MD&A (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, margin, interest rate, customer, segment, product, service, market, operations, network

- and Analysis of Financial Condition and Results of Operations  This discussion and analysis reflects information contained in our audited consolidated financial statements and other relevant statistical data, and is intended to enhance your understanding of our financial condition and results of operations.
- Our primary sources of non-interest income are service charges on deposit accounts, investment advisory income, net gains in the cash surrender value of bank owned life insurance and other income.
- Our non-interest expenses consist of salaries and employee benefits, net occupancy and equipment, data processing, professional fees, marketing expenses, premium payments we make to the FDIC for insurance of our deposits and other general and administrative expenses.
- Smith’s executive leadership experience includes overseeing community bank operations, spearheading the implementation of digital banking and banking-as-a-service programs and integrating acquired financial institutions.
- As we realign our strategies  for growth, we intend to continue to operate as a well-capitalized and profitable community bank dedicated to providing exceptional personal service to our individual and business customers.
- We believe that we have a competitive advantage in the markets we serve because of our knowledge of the local marketplace and our long-standing history of providing superior, relationship-based customer service.
- Our current business strategy includes the following key components, which are designed to improve earnings by expanding our net interest margin, increasing non-interest income and improving efficiency:    Emphasize relationship-based commercial lending.
- ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────  Increasing our commercial real estate loans and commercial business loans involves risk, as described in “Risk Factors - Risks Related to Our Lending Activities - Our emphasis on commercial real estate and commercial business lending involves risks that could adversely affect our financial condition and results of operations” and “ - Our non-owner occupied commercial real estate loans may expose us to increased credit risk.”    Grow and enhance our low-cost deposit base.


## Research loop (think → act)

1. _heuristic_ — Coverage looks adequate for this pass; stopping iterative loop.

## Sources

- **[S1]** RBKB fundamentals (yfinance)
  - Rhinebeck Bancorp, Inc.: price=12.3, rev=53355000.0, fcf=10893000.0, shares=15638237.0, rev_cagr=0.03754424938432588, ROIC=None, FCF yield=0.056631046935612064
- **[S2]** RBKB DCF valuation (dcf)
  - Base share price=32.4822323870783, bull=60.191263927521966, bear=14.204002046386439
- **[S3]** RBKB EV/EBITDA valuation (multiples)
  - Base implied price=510.83258298234, multiple=8.0
- **[S4]** RBKB Analyst Ratings, Price Targets and Consensus | Rallies (web) — https://rallies.ai/research/RBKB/analysts
  - See RBKB analyst ratings, consensus rating, price targets, upgrades, downgrades, analyst firms, and recent Wall Street rating changes.
- **[S5]** Berkshire Hathaway (BRK.B) Stock Forecast & Price Target (web) — https://www.marketbeat.com/stocks/NYSE/BRK-B/forecast/
  - BRK.B's current price target is $524.50. Learn why top analysts are making this stock forecast for Berkshire Hathaway at MarketBeat.
- **[S6]** RBKB Analyst Ratings & Price Targets 2026 - Lician (web) — https://lician.com/analyst/rbkb
  - RBKB analyst ratings and price targets. See Wall Street recommendations, consensus rating, average price target, and analyst upgrades/downgrades.
- **[S7]** RBKB Price Target 2026 - Analyst Target Prices & Forecast | Lician (web) — https://lician.com/target-price/rbkb
  - RBKB price target and analyst target prices. See average, high, low price targets, consensus estimates, and upside potential from Wall Street analysts.
- **[S8]** Rhinebeck Bancorp Inc Ordinary Shares (RBKB) - Morningstar (web) — https://www.morningstar.com/stocks/xnas/rbkb/quote
  - See the latest Rhinebeck Bancorp Inc Ordinary Shares stock price ... Rhinebeck Bancorp Inc Ordinary Shares RBKB. Morningstar Rating. Unlock. Stock XNAS Rating ...
- **[S9]** Rhinebeck Bancorp, Inc. (RBKB) Stock Price, News, Quote & History (web) — https://finance.yahoo.com/quote/RBKB/
  - Find the latest Rhinebeck Bancorp, Inc. (RBKB) stock quote, history, news and other vital information to help you with your stock trading and investing.
- **[S10]** RBKB Stock Price Quote & News - Rhinebeck Bancorp - Robinhood (web) — https://robinhood.com/us/en/stocks/RBKB/
  - On 2026-07-26, Rhinebeck Bancorp(RBKB) stock moved within a range of $12.34 to $12.70. With shares now at $12.43, the stock is trading +0.8% above its intraday ...
- **[S11]** RBKB Stock Quote Price and Forecast - CNN (web) — https://www.cnn.com/markets/stocks/RBKB
  - Rhinebeck Bancorp Inc · Price Momentum. RBKB is trading in the middle of its 52-week range and below its 200-day simple moving average. · Price change. The price ...
- **[S12]** RBKB Analyst Ratings, Price Targets and Consensus | Rallies (web_page) — https://rallies.ai/research/RBKB/analysts
  - RBKB Analyst Ratings, Price Targets and Consensus | Rallies Rhinebeck Bancorp Watchlist Chart Financials Insiders Analysts Rhinebeck Bancorp Watchlist Chart Financials Insiders …
- **[S13]** Berkshire Hathaway (BRK.B) Stock Forecast and Price Target 2026 (web_page) — https://www.marketbeat.com/stocks/NYSE/BRK-B/forecast/
  - Berkshire Hathaway (BRK.B) Stock Forecast and Price Target 2026 Skip to main content → The dollar reset no one told you about (From Porter & Company) (Ad) Free BRK.B Stock Alert…
- **[S14]** RBKB Analyst Ratings 2026 - Price Targets & Recommendations | Lician (web_page) — https://lician.com/analyst/rbkb
  - RBKB Analyst Ratings 2026 - Price Targets & Recommendations | Lician RBKB Analyst Ratings 2026 Rhinebeck Bancorp Inc - Wall Street recommendations & price targets Consensus Rati…
- **[S15]** RBRK Intrinsic Valuation and Fundamental Analysis - Rubrik Inc - Alpha Spread (web) — https://www.alphaspread.com/security/nyse/rbrk/summary
  - The intrinsic value of one RBRK stock under the Base Case scenario is 28.16 USD.
- **[S16]** 3 Ways of Calculating a Stock's Intrinsic Value - HubPages (web) — https://discover.hubpages.com/money/Stock-Valuation-Using-Bear-Bull-and-Base-Case-Scenarios
  - September 12, 2024 - When calculating intrinsic value, it can be helpful to have 3 probability-weighted, projected scenarios mapped out in order to dial in a specific number.
- **[S17]** 3 Ways of Calculating a Stock's Intrinsic Value - ToughNickel (web) — https://toughnickel.com/personal-finance/Stock-Valuation-Using-Bear-Bull-and-Base-Case-Scenarios
  - March 22, 2023 - When calculating intrinsic value, it can be helpful to have 3 probability-weighted, projected scenarios mapped out in order to dial in a specific number.
- **[S18]** Bull Base Bear Valuation for One Stock | Model Reef (web) — https://modelreef.io/resources/articles/stock-valuation/how-to-create-a-bull-base-bear-valuation-for-one-stock-scenario-driven-intrinsic-value
  - April 15, 2026 - The point of bull/base/bear is to show what must be true-not to pretend the world can be summarised in one number. If you want a quick quality check, compare yo…
- **[S19]** Rhinebeck Bancorp, Inc. (RBKB) Stock Price, News... - Yahoo Finance (web) — https://finance.yahoo.com/quote/RBKB/
  - Find the latest Rhinebeck Bancorp, Inc. (RBKB) stock quote, history, news and other vital information to help you with your stock trading and investing.
- **[S20]** Rhinebeck Bancorp, Inc. (RBKB) Stock Price, Quote... | Seeking Alpha (web) — https://seekingalpha.com/symbol/RBKB
  - A high-level overview of Rhinebeck Bancorp, Inc. (RBKB) stock. View (RBKB) real-time stock price, chart, news, analysis, analyst reviews and more.
- **[S21]** RBKB Stock Price and Chart — NASDAQ:RBKB — TradingView (web) — https://www.tradingview.com/symbols/NASDAQ-RBKB/
  - View live Rhinebeck Bancorp, Inc. chart to track its stock's price action. Find market predictions, RBKB financials and market news.
- **[S22]** Rhinebeck Bancorp Inc Stock Price Today | NASDAQ: RBKB Live (web) — https://www.investing.com/equities/rhinebeck
  - POUGHKEEPSIE, N.Y. - Rhinebeck Bancorp, Inc. (NASDAQ:RBKB) announced today it has commenced a stock offering of up to 8,912,500... Investing.com. May 26, 2026.
- **[S23]** RBKB 10-K (sec)
  - Item 1 chars=80000, Item 1A chars=50000, Item 7 chars=50000, ok=True, source=cache
- **[S24]** Item 1 Business summary (nlp)
  - ### Item 1 — Business (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, regulation, competition, margin, interest rate, customer, segment, product, service, mar…
- **[S25]** Item 1A summary (nlp)
  - ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, guidance, revenue, margin, supply…
- **[S26]** Item 7 summary (nlp)
  - ### Item 7 — MD&A (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, margin, interest rate, customer, segment, product, service, market, operations, network  - a…
- **[S27]** RBKB scenario price ranges (scenarios)
  - ok=True; base mid=531.2952476676239; headwinds=5; tailwinds=7

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

# RBKB — Planned Research Report

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

**Fundamentals error:** Failed to perform, curl: (7) Failed to connect to query2.finance.yahoo.com port 443 after 13 ms: Could not connect to server. See https://curl.se/libcurl/c/libcurl-errors.html first for more details.

## DCF valuation (base / bull / bear) [S2]

> Simplified revenue->FCF DCF. Not investment advice; assumptions are editable heuristics.

- **Error:** Cannot run DCF without positive base revenue.
- **Error:** Cannot run DCF without shares outstanding.

## Web research — web_research

- Queries: Deep diligence: fundamentals, DCF, web, 10-K risks & MD&A
- Unique hits: 0
- Pages fetched: 0/0

### Web synthesis — web_research
No text extracted.

### Search warnings
- text:Deep diligence: fundamentals, DCF, web, 10-K risks & MD&A: ConnectError: ConnectError('[Errno 11001] getaddrinfo failed')
- news:Deep diligence: fundamentals, DCF, web, 10-K risks & MD&A: ConnectError: ConnectError('error sending request for url (https://news.search.yahoo.com/search?p=Deep+diligence%3A+fundamentals%2C+DCF%2C+web%2C+10-K+risks+%26+MD%26A) > client error (Connect) > dns error > no connections available')

## Web research — loop_followup

- Queries: RBKB analyst price target, RBKB stock news
- Unique hits: 12
- Pages fetched: 3/3

### Web synthesis — loop_followup (rule-based fallback — Ollama unavailable)
**Keyword hits:** revenue, margin, service, market

- [HIT] Berkshire Hathaway (BRK.B) Stock Forecast & Price Target | www.marketbeat.com | https://www.marketbeat.com/stocks/NYSE/BRK-B/forecast/ BRK.B's current price target is $524.50.
- Learn why top analysts are making this stock forecast for Berkshire Hathaway at MarketBeat.
- | www.marketbeat.com | https://www.marketbeat.com/stocks/NASDAQ/RBKB/news/ Read today's RBKB news from trusted media outlets at MarketBeat.
- [HIT] Rhinebeck Bancorp Engages KBW to Support Stock Offering | The Globe and Mail | https://www.theglobeandmail.com/investing/markets/stocks/RBKB/pressreleases/1967826/rhinebeck-bancorp-engages-kbw-to-support-stock-offering/ The latest update is out from Rhinebeck Bancorp ( (RBKB)).
- Common Stock (RBKB) | Nasdaq | https://www.nasdaq.com/market-activity/stocks/rbkb/analyst-research Nasdaq Analyst Research provides analyst research for ratings consensus and a summary of stock price targets.
- Common Stock (RBKB) | Nasdaq | https://www.nasdaq.com/market-activity/stocks/rbkb/after-hours Investors may trade in the Pre-Market (4:00-9:30 a.m.
- ET) and the After Hours Market (4:00-8:00 p.m.
- Participation from Market Makers and ECNs is strictly voluntary and as a result, these ...

### Sources found
- [Berkshire Hathaway (BRK.B) Stock Forecast & Price Target](https://www.marketbeat.com/stocks/NYSE/BRK-B/forecast/)
  - BRK.B's current price target is $524.50. Learn why top analysts are making this stock forecast for Berkshire Hathaway at MarketBeat.
- [RBKB Analyst Ratings, Price Targets and Consensus | Rallies](https://rallies.ai/research/RBKB/analysts)
  - See RBKB analyst ratings, consensus rating, price targets, upgrades, downgrades, analyst firms, and recent Wall Street rating changes.
- [RBKB Analyst Ratings & Price Targets 2026 - Lician](https://lician.com/analyst/rbkb)
  - RBKB analyst ratings and price targets. See Wall Street recommendations, consensus rating, average price target, and analyst upgrades/downgrades.
- [RBKB Price Target 2026 - Analyst Target Prices & Forecast | Lician](https://lician.com/target-price/rbkb)
  - RBKB price target and analyst target prices. See average, high, low price targets, consensus estimates, and upside potential from Wall Street analysts.
- [Rhinebeck Bancorp, Inc. (RBKB) Stock Price, News... - Yahoo Finance](https://finance.yahoo.com/quote/RBKB/)
  - Find the latest Rhinebeck Bancorp, Inc. (RBKB) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Rhinebeck Bancorp Inc News (RBKB) - Investing.com](https://www.investing.com/equities/rhinebeck-news)
  - Get today's Rhinebeck stock news.Rhinebeck Bancorp, Inc. (RBKB) stock has soared to a 52-week high, reaching a price level of $10.59 USD. According to Invest…
- [RBKB News Today | Why did Rhinebeck Bancorp stock go down today?](https://www.marketbeat.com/stocks/NASDAQ/RBKB/news/)
  - Read today's RBKB news from trusted media outlets at MarketBeat. 1 RBKB Articles Average Week. Get the Latest News and Ratings for RBKB and Related Stocks.
- [Rhinebeck Bancorp, Inc. (RBKB) Stock Price, Quote, News & Analysis](https://seekingalpha.com/symbol/RBKB)
  - View (RBKB) real-time stock price, chart, news, analysis, analyst reviews and more.
- [Rhinebeck Bancorp Engages KBW to Support Stock Offering](https://www.theglobeandmail.com/investing/markets/stocks/RBKB/pressreleases/1967826/rhinebeck-bancorp-engages-kbw-to-support-stock-offering/)
  - The latest update is out from Rhinebeck Bancorp ( (RBKB)). On May 14, 2026, Rhinebeck Bancorp, MHC, Rhinebeck Bancorp, Inc., and Rhinebeck Bank entered into …
- [Rhinebeck Bancorp, Inc. Common Stock (RBKB)](https://www.nasdaq.com/market-activity/stocks/rbkb/analyst-research)
  - Nasdaq Analyst Research provides analyst research for ratings consensus and a summary of stock price targets. Analysts evaluate the stock’s expected performa…
- [Rhinebeck Bancorp, Inc. Common Stock (RBKB)](https://www.nasdaq.com/market-activity/stocks/rbkb/after-hours)
  - Investors may trade in the Pre-Market (4:00-9:30 a.m. ET) and the After Hours Market (4:00-8:00 p.m. ET). Participation from Market Makers and ECNs is strict…
- [Rhinebeck Bancorp, Inc. Common Stock (RBKB)](https://www.nasdaq.com/market-activity/stocks/rbkb/pre-market)
  - Investors may trade in the Pre-Market (4:00-9:30 a.m. ET) and the After Hours Market (4:00-8:00 p.m. ET). Participation from Market Makers and ECNs is strict…

### Search warnings
- news:RBKB analyst price target: No results found.

## Put opportunities (heuristic) [S3]
- Expiration: None (DTE None)
- Candidates: 0
- ATM IV (est.): —
- IV rank: — (0 local samples)
- HV rank (20d realized): —


**Options error:** Failed to perform, curl: (7) Failed to connect to query2.finance.yahoo.com port 443 after 22 ms: Could not connect to server. See https://curl.se/libcurl/c/libcurl-errors.html first for more details.

## SEC filing [S4]
- Extraction OK: True
- Item 1 chars: 80000
- Item 1A chars: 50000
- Item 7 chars: 50000
- Meta: {'source': 'cache', 'path': 'C:\\DevWork\\equity_research_agent\\data\\filings\\RBKB_10k.txt'}

## Company setup & business model

**Keyword hits:** risk, regulation, competition, margin, interest rate, customer, segment, product, service, market, operations

- The Company is regulated by the Board of Governors of the Federal Reserve System (the “Federal Reserve Board”) and the New York State Department of Financial Services (the “NYSDFS”).
- We provide a full range of banking and financial services to consumer and commercial customers through our corporate office and 12 branches located in Dutchess, Orange and Ulster Counties.
- We also maintain a representative office in Albany County to originate indirect automobile and commercial loans and a representative office in Dutchess County for financial services.
- Financial services, including investment  advisory and financial product sales, are offered through a division of the Bank doing business as Rhinebeck Asset Management (“RAM”).
- We offer a variety of deposit accounts, including savings accounts, certificates of deposit, money market accounts, commercial and personal checking accounts and individual retirement accounts.
- We are subject to regulation and examination by the NYSDFS and by the Federal Deposit Insurance Corporation (the “FDIC”).
- Market Area  Our primary market area encompasses Dutchess, Orange, Ulster and Albany Counties (and their contiguous counties), which are located in the Hudson Valley region of New York.
- The Hudson Valley region has a diversified economy and representative industries include education, health, government, leisure and hospitality and professional business services.
- The four counties in our primary market area each had a lower unemployment rate than New York State (Dutchess County, 3.2%, Orange County, 3.6%, Ulster County, 3.5% and Albany County, 3.3%).
- Competition  We face significant competition for deposits and loans.
- Our most direct competition for deposits has historically come from the numerous financial institutions operating in our market area (including other community and commercial banks, credit unions and financial technology companies), many of which are significantly larger than we are and have greater resources.
- We also face competition for investors’ funds from other sources such as brokerage firms, money market funds and mutual funds, as  well as securities, such as Treasury bills, offered by the Federal Government.
- Based on FDIC data, at June 30, 2025 (the latest date for which information is available), we had 10.44% of the FDIC-insured deposit market share in Dutchess County, which was fourth among the 15 institutions with offices in the county, 1.59% of the FDIC-insured deposit market share in Ulster County, which was 12thamong the 18 institutions with offices in the county, and 1.28% of the FDIC-insured deposit market share  in Orange County, which was 14thamong the 22 institutions with offices in the county.
- We expect competition to remain intense in the future as a result of legislative, regulatory and technological changes and the continuing trend of consolidation in the financial services industry.
- Technological advances, for example, have lowered barriers to entry, allowed banks to expand their geographic reach by providing services over the internet and made it possible for non-depository institutions, including financial technology companies, to offer products and services that traditionally  have been provided by banks.
- Competition for deposits and the origination of loans could limit our growth in the future.
- We seek to meet this competition with convenient branch locations and online offerings, emphasizing personalized banking and the advantage of local decision-making in our banking businesses.
- Specifically, we promote and maintain relationships and build customer loyalty within local communities by focusing our marketing and community involvement on the specific needs of individual neighborhoods.
- At December  31, 2025, substantially all of our commercial real estate loans were secured by properties located in our market area.
- However, occasionally we will originate commercial real estate loans on properties located outside our market area based on an established relationship with a strong borrower.
- The interest rate on commercial real estate loans is generally adjustable and based on a margin over an index, typically The Wall Street Journal Prime Rate or the Federal Home Loan Bank of New York Amortizing Advance Rate.
- We selectively offer interest rate swaps for both commercial and multi-family real estate loans.
- In underwriting commercial real estate loans, we consider a number of factors, including the projected net cash flows to the loan’s debt service requirement (generally requiring a minimum of 1.20x), the age and condition of the collateral, the financial resources and income level of the borrower and the borrower’s experience in owning or managing similar properties.
- Our multi-family real estate loans are generally secured by multi-unit rental properties, consisting of five to 100 rental units, in our market area.
- The interest rates on our multi-family real estate loans are generally adjustable based on a margin over an index.
- In underwriting multi-family real estate loans, we consider a number of factors including the projected net cash flows to the loan’s debt service requirement (generally requiring a minimum of 1.20x), the age and condition of the collateral, the financial resources and income level of the borrower, and the borrower’s experience in owning or managing similar properties.
- All these loans are secured by properties located in our primary market area.
- The interest rate is generally a variable rate based on an index rate, typically The Wall Street Journal Prime Rate plus a margin.

_Source: latest 10-K Item 1 (Business), summarized locally._

## Qualitative analysis (local LLM)

### Item 1 — Business (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, regulation, competition, margin, interest rate, customer, segment, product, service, market, operations

- The Company is regulated by the Board of Governors of the Federal Reserve System (the “Federal Reserve Board”) and the New York State Department of Financial Services (the “NYSDFS”).
- We provide a full range of banking and financial services to consumer and commercial customers through our corporate office and 12 branches located in Dutchess, Orange and Ulster Counties.
- We also maintain a representative office in Albany County to originate indirect automobile and commercial loans and a representative office in Dutchess County for financial services.
- Financial services, including investment  advisory and financial product sales, are offered through a division of the Bank doing business as Rhinebeck Asset Management (“RAM”).
- We offer a variety of deposit accounts, including savings accounts, certificates of deposit, money market accounts, commercial and personal checking accounts and individual retirement accounts.
- We are subject to regulation and examination by the NYSDFS and by the Federal Deposit Insurance Corporation (the “FDIC”).
- Market Area  Our primary market area encompasses Dutchess, Orange, Ulster and Albany Counties (and their contiguous counties), which are located in the Hudson Valley region of New York.
- The Hudson Valley region has a diversified economy and representative industries include education, health, government, leisure and hospitality and professional business services.
- The four counties in our primary market area each had a lower unemployment rate than New York State (Dutchess County, 3.2%, Orange County, 3.6%, Ulster County, 3.5% and Albany County, 3.3%).
- Competition  We face significant competition for deposits and loans.
- Our most direct competition for deposits has historically come from the numerous financial institutions operating in our market area (including other community and commercial banks, credit unions and financial technology companies), many of which are significantly larger than we are and have greater resources.
- We also face competition for investors’ funds from other sources such as brokerage firms, money market funds and mutual funds, as  well as securities, such as Treasury bills, offered by the Federal Government.
- Based on FDIC data, at June 30, 2025 (the latest date for which information is available), we had 10.44% of the FDIC-insured deposit market share in Dutchess County, which was fourth among the 15 institutions with offices in the county, 1.59% of the FDIC-insured deposit market share in Ulster County, which was 12thamong the 18 institutions with offices in the county, and 1.28% of the FDIC-insured deposit market share  in Orange County, which was 14thamong the 22 institutions with offices in the county.
- We expect competition to remain intense in the future as a result of legislative, regulatory and technological changes and the continuing trend of consolidation in the financial services industry.
- Technological advances, for example, have lowered barriers to entry, allowed banks to expand their geographic reach by providing services over the internet and made it possible for non-depository institutions, including financial technology companies, to offer products and services that traditionally  have been provided by banks.
- Competition for deposits and the origination of loans could limit our growth in the future.
- We seek to meet this competition with convenient branch locations and online offerings, emphasizing personalized banking and the advantage of local decision-making in our banking businesses.
- Specifically, we promote and maintain relationships and build customer loyalty within local communities by focusing our marketing and community involvement on the specific needs of individual neighborhoods.
- At December  31, 2025, substantially all of our commercial real estate loans were secured by properties located in our market area.
- However, occasionally we will originate commercial real estate loans on properties located outside our market area based on an established relationship with a strong borrower.
- The interest rate on commercial real estate loans is generally adjustable and based on a margin over an index, typically The Wall Street Journal Prime Rate or the Federal Home Loan Bank of New York Amortizing Advance Rate.
- We selectively offer interest rate swaps for both commercial and multi-family real estate loans.
- In underwriting commercial real estate loans, we consider a number of factors, including the projected net cash flows to the loan’s debt service requirement (generally requiring a minimum of 1.20x), the age and condition of the collateral, the financial resources and income level of the borrower and the borrower’s experience in owning or managing similar properties.
- Our multi-family real estate loans are generally secured by multi-unit rental properties, consisting of five to 100 rental units, in our market area.
- The interest rates on our multi-family real estate loans are generally adjustable based on a margin over an index.
- In underwriting multi-family real estate loans, we consider a number of factors including the projected net cash flows to the loan’s debt service requirement (generally requiring a minimum of 1.20x), the age and condition of the collateral, the financial resources and income level of the borrower, and the borrower’s experience in owning or managing similar properties.
- All these loans are secured by properties located in our primary market area.
- The interest rate is generally a variable rate based on an index rate, typically The Wall Street Journal Prime Rate plus a margin.


### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, uncertainty, litigation, regulation, competition, guidance, revenue, margin, supply chain, cyber, interest rate, customer, product, service, market, operations, network

- In addition to factors discussed in the description of our business and elsewhere in this report, the following are factors that could adversely affect our future results of operations and financial condition.
- Risks Related to Our Lending Activities  Our emphasis on commercial real estate and commercial business lending involves risks that could adversely affect our financial condition and results of operations.
- While these types of loans are potentially more profitable than residential mortgage loans due primarily to bearing generally higher interest rates and larger balances, they present greater risk  due to greater dependency on the successful operation of the properties and are generally more sensitive to regional and local economic conditions, making future losses more difficult to predict.
- Consequently, an adverse development with respect to one loan or one credit relationship can expose us to a  significantly greater risk of loss compared to an adverse development with respect to a residential mortgage loan.
- These loans also expose us to greater credit risk than loans secured by residential real estate because the collateral securing these loans typically cannot be liquidated as easily as residential real estate.
- Business - Loan Underwriting Risks.”  Our automobile loan portfolio exposes us to increased credit risks.
- Automobile loans are inherently risky as they are secured by assets that may be difficult to locate, have high loan-to-value ratios, and can depreciate rapidly.
- Furthermore, our consumer lending activities are subject to numerous consumer protection laws and regulations, and the application of various federal and state laws, including bankruptcy and insolvency laws, may limit our ability to recover on such loans.


### Item 7 — MD&A (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, margin, interest rate, customer, segment, product, service, market, operations, network

- and Analysis of Financial Condition and Results of Operations  This discussion and analysis reflects information contained in our audited consolidated financial statements and other relevant statistical data, and is intended to enhance your understanding of our financial condition and results of operations.
- Our primary sources of non-interest income are service charges on deposit accounts, investment advisory income, net gains in the cash surrender value of bank owned life insurance and other income.
- Our non-interest expenses consist of salaries and employee benefits, net occupancy and equipment, data processing, professional fees, marketing expenses, premium payments we make to the FDIC for insurance of our deposits and other general and administrative expenses.
- Smith’s executive leadership experience includes overseeing community bank operations, spearheading the implementation of digital banking and banking-as-a-service programs and integrating acquired financial institutions.
- As we realign our strategies  for growth, we intend to continue to operate as a well-capitalized and profitable community bank dedicated to providing exceptional personal service to our individual and business customers.
- We believe that we have a competitive advantage in the markets we serve because of our knowledge of the local marketplace and our long-standing history of providing superior, relationship-based customer service.
- Our current business strategy includes the following key components, which are designed to improve earnings by expanding our net interest margin, increasing non-interest income and improving efficiency:    Emphasize relationship-based commercial lending.
- ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────  Increasing our commercial real estate loans and commercial business loans involves risk, as described in “Risk Factors - Risks Related to Our Lending Activities - Our emphasis on commercial real estate and commercial business lending involves risks that could adversely affect our financial condition and results of operations” and “ - Our non-owner occupied commercial real estate loans may expose us to increased credit risk.”    Grow and enhance our low-cost deposit base.


## Run warnings

- fundamentals: Failed to perform, curl: (7) Failed to connect to query2.finance.yahoo.com port 443 after 13 ms: Could not connect to server. See https://curl.se/libcurl/c/libcurl-errors.html first for more details.
- dcf: Cannot run DCF without positive base revenue.; Cannot run DCF without shares outstanding.
- options: Failed to perform, curl: (7) Failed to connect to query2.finance.yahoo.com port 443 after 22 ms: Could not connect to server. See https://curl.se/libcurl/c/libcurl-errors.html first for more details.

## Research loop (think → act)

1. _heuristic_ — Only 0 web hits so far; broadening news/analyst search.
   - act `search_web`: sparse web coverage · RBKB analyst price target, RBKB stock news
2. _heuristic_ — Coverage looks adequate for this pass; stopping iterative loop.

## Sources

- **[S1]** RBKB fundamentals (yfinance)
  - Error: Failed to perform, curl: (7) Failed to connect to query2.finance.yahoo.com port 443 after 13 ms: Could not connect to server. See https://curl.se/libcurl/c/libcurl-errors…
- **[S2]** RBKB DCF valuation (dcf)
  - DCF failed: Cannot run DCF without positive base revenue.; Cannot run DCF without shares outstanding.
- **[S3]** RBKB put screen (yfinance_options)
  - Error: Failed to perform, curl: (7) Failed to connect to query2.finance.yahoo.com port 443 after 22 ms: Could not connect to server. See https://curl.se/libcurl/c/libcurl-errors…
- **[S4]** RBKB 10-K (sec)
  - Item 1 chars=80000, Item 1A chars=50000, Item 7 chars=50000, ok=True, source=cache
- **[S5]** Item 1 Business summary (nlp)
  - ### Item 1 — Business (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, regulation, competition, margin, interest rate, customer, segment, product, service, mar…
- **[S6]** Item 1A summary (nlp)
  - ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, guidance, revenue, margin, supply…
- **[S7]** Item 7 summary (nlp)
  - ### Item 7 — MD&A (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, margin, interest rate, customer, segment, product, service, market, operations, network  - a…
- **[S8]** Berkshire Hathaway (BRK.B) Stock Forecast & Price Target (web) — https://www.marketbeat.com/stocks/NYSE/BRK-B/forecast/
  - BRK.B's current price target is $524.50. Learn why top analysts are making this stock forecast for Berkshire Hathaway at MarketBeat.
- **[S9]** RBKB Analyst Ratings, Price Targets and Consensus | Rallies (web) — https://rallies.ai/research/RBKB/analysts
  - See RBKB analyst ratings, consensus rating, price targets, upgrades, downgrades, analyst firms, and recent Wall Street rating changes.
- **[S10]** RBKB Analyst Ratings & Price Targets 2026 - Lician (web) — https://lician.com/analyst/rbkb
  - RBKB analyst ratings and price targets. See Wall Street recommendations, consensus rating, average price target, and analyst upgrades/downgrades.
- **[S11]** RBKB Price Target 2026 - Analyst Target Prices & Forecast | Lician (web) — https://lician.com/target-price/rbkb
  - RBKB price target and analyst target prices. See average, high, low price targets, consensus estimates, and upside potential from Wall Street analysts.
- **[S12]** Rhinebeck Bancorp, Inc. (RBKB) Stock Price, News... - Yahoo Finance (web) — https://finance.yahoo.com/quote/RBKB/
  - Find the latest Rhinebeck Bancorp, Inc. (RBKB) stock quote, history, news and other vital information to help you with your stock trading and investing.
- **[S13]** Rhinebeck Bancorp Inc News (RBKB) - Investing.com (web) — https://www.investing.com/equities/rhinebeck-news
  - Get today's Rhinebeck stock news.Rhinebeck Bancorp, Inc. (RBKB) stock has soared to a 52-week high, reaching a price level of $10.59 USD. According to InvestingPro...
- **[S14]** RBKB News Today | Why did Rhinebeck Bancorp stock go down today? (web) — https://www.marketbeat.com/stocks/NASDAQ/RBKB/news/
  - Read today's RBKB news from trusted media outlets at MarketBeat. 1 RBKB Articles Average Week. Get the Latest News and Ratings for RBKB and Related Stocks.
- **[S15]** Rhinebeck Bancorp, Inc. (RBKB) Stock Price, Quote, News & Analysis (web) — https://seekingalpha.com/symbol/RBKB
  - View (RBKB) real-time stock price, chart, news, analysis, analyst reviews and more.
- **[S16]** Berkshire Hathaway (BRK.B) Stock Forecast and Price Target 2026 (web_page) — https://www.marketbeat.com/stocks/NYSE/BRK-B/forecast/
  - Berkshire Hathaway (BRK.B) Stock Forecast and Price Target 2026 Skip to main content → Universal basic income is not impossible. It exist (kind of) (From Freedom Financial) (Ad)…
- **[S17]** RBKB Analyst Ratings, Price Targets and Consensus | Rallies (web_page) — https://rallies.ai/research/RBKB/analysts
  - RBKB Analyst Ratings, Price Targets and Consensus | Rallies Rhinebeck Bancorp Watchlist Chart Financials Insiders Analysts Rhinebeck Bancorp Watchlist Chart Financials Insiders …
- **[S18]** RBKB Analyst Ratings 2026 - Price Targets & Recommendations | Lician (web_page) — https://lician.com/analyst/rbkb
  - RBKB Analyst Ratings 2026 - Price Targets & Recommendations | Lician RBKB Analyst Ratings 2026 Rhinebeck Bancorp Inc - Wall Street recommendations & price targets Consensus Rati…

## Self-critique

_Automated review (heuristic)._

### Strengths
- Combines local fundamentals, optional DCF scenarios, and cited sources where available.
- Keeps a non-advisory framing for local research drafts.

### Issues & gaps
- DCF section was planned but valuation did not complete successfully.
- Run recorded 3 tool warning(s); see Run warnings before relying on the draft.

### Caution for readers
- Treat scenario prices as sensitivity output, not a forecast.
- Re-check primary filings and fresh market data before any decision.



---

# Template: Options income (`income`)

# RBKB — Planned Research Report

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
- Company: Rhinebeck Bancorp, Inc.
- Sector / industry: Financial Services / Banks - Regional
- Price: 12.3
- 52-week range: $6.74 – $12.88
- Market cap: $192.35M
- Enterprise value: -$161.05M
- Shares outstanding: 15.64M
- Beta: 0.148
- Book equity: $136.85M
- Revenue (latest): $53.35M
- EBITDA (latest): —
- Free cash flow (latest): $10.89M
- Operating income: —
- Operating margin: —
- EV / EBITDA: —
- ROIC: —
- FCF yield: 5.7%
- Debt / Equity: 0.22146552480051443
- FCF / share: $0.70
- Revenue / share: $3.41

### Capital structure
- Cash: $18.83M
- Short-term debt: $1.61M
- Long-term debt: $28.69M
- Total debt: $30.31M
- Net debt: $11.48M
- Net debt / EBITDA: —

### Growth
- Revenue CAGR: 3.8%
- FCF CAGR: -7.3%
- Latest revenue YoY: 85.7%
- Latest FCF YoY: 41.9%

### Market expectations (yfinance, sparse)
- Mean target: —
- Target range: — – —
- Recommendation: none

_Consensus revenue/EBITDA forecasts are often unavailable via free feeds; treat targets as point-in-time only._

### Historical KPIs (multi-year)

| Year | Revenue | OCF | Capex | FCF | EBITDA | LT debt | Cash | Net debt | Net income |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2025 | $53.35M | $11.74M | $850.00K | $10.89M | — | $28.69M | $18.83M | $9.87M | $10.04M |
| 2024 | $28.73M | $8.47M | $791.00K | $7.68M | — | $74.93M | $19.18M | $55.75M | -$8.62M |
| 2023 | $43.70M | $7.05M | $578.00K | $6.47M | — | $133.22M | $14.61M | $118.61M | $4.39M |
| 2022 | $47.77M | $14.79M | $1.13M | $13.66M | — | $62.88M | $16.82M | $46.06M | $7.00M |

## Charts

### Revenue & FCF history
![Revenue & FCF history](/charts/RBKB_income_revenue_fcf.png)

## Web research — web_research

- Queries: RBKB news, Rhinebeck Bancorp, Inc. earnings OR catalyst
- Unique hits: 12
- Pages fetched: 0/3

### Web synthesis — web_research (rule-based fallback — Ollama unavailable)
**Keyword hits:** customer, product, service, market

- | www.marketbeat.com | https://www.marketbeat.com/stocks/NASDAQ/RBKB/news/ Read today's RBKB news from trusted media outlets at MarketBeat.View real-time investing headlines and stock market news for your watchlist or the broader market.
- [HIT] Rhinebeck Bank | Investor Relations | www.rhinebeckbank.com | https://www.rhinebeckbank.com/Investor-Relations Rhinebeck Bank is a full service, locally focused bank headquartered in Poughkeepsie, NY.
- We offer a full range of personal checking, savings, money market and certificates of deposit as well as, home equity lines of credit and mortgages.
- For commercial customers we offer a broad variety of products and services for sole proprietors, partnerships, and corporations.

### Sources found
- [RBC News](https://en.wikipedia.org/wiki/RBC_News)
  - The RBC Group, or RosBusinessConsulting, is a Russian media group headquartered in Moscow. It was established in 1993.The company holds an informational agen…
- [Rhinebeck Bancorp Inc News (RBKB) - Investing.com](https://www.investing.com/equities/rhinebeck-news)
  - Get today's Rhinebeck stock news.Rhinebeck Bancorp, Inc. (RBKB) stock has soared to a 52-week high, reaching a price level of $10.59 USD. According to Invest…
- [Rhinebeck Bancorp, Inc. (RBKB) Stock Price, News... - Yahoo Finance](https://finance.yahoo.com/quote/RBKB/?p=RBKB)
  - Find the latest Rhinebeck Bancorp, Inc. (RBKB) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [RBKB News Today | Why did Rhinebeck Bancorp stock go down today?](https://www.marketbeat.com/stocks/NASDAQ/RBKB/news/)
  - Read today's RBKB news from trusted media outlets at MarketBeat.View real-time investing headlines and stock market news for your watchlist or the broader ma…
- [Rhinebeck Bancorp Stock Short Interest Report | NASDAQ:RBKB | Benzinga](https://www.benzinga.com/quote/RBKB/short-interest)
  - Short interest in Rhinebeck Bancorp Inc (NASDAQ:RBKB) increased during the last reporting period, rising from 86.78K to 181.74K. This put 4.01% of the compan…
- [Rhinebeck Bancorp, Inc.'s (NASDAQ:RBKB) largest shareholders are private companies with 58% ownership, individual investors own 19%](https://finance.yahoo.com/news/rhinebeck-bancorp-inc-nasdaq-rbkb-135825434.html)
  - The above button links to Coinbase. Yahoo Finance is not a broker-dealer or investment adviser and does not offer securities or cryptocurrencies for sale or …
- [Is Rhinebeck Bancorp, Inc. (RBKB) A Good Stock To Buy Now?](https://finance.yahoo.com/news/rhinebeck-bancorp-inc-rbkb-good-200906442.html)
  - The above button links to Coinbase. Yahoo Finance is not a broker-dealer or investment adviser and does not offer securities or cryptocurrencies for sale or …
- [Individual investors own 22% of Rhinebeck Bancorp, Inc. (NASDAQ:RBKB) shares but private companies control 59% of the company](https://finance.yahoo.com/news/individual-investors-own-22-rhinebeck-141201638.html)
  - The above button links to Coinbase. Yahoo Finance is not a broker-dealer or investment adviser and does not offer securities or cryptocurrencies for sale or …
- [Rhinebeck Bank | Investor Relations](https://www.rhinebeckbank.com/Investor-Relations)
  - Rhinebeck Bank is a full service, locally focused bank headquartered in Poughkeepsie, NY. We offer a full range of personal checking, savings, money market a…
- [Catalyst Access - About the University of Cincinnati | A Top Public ...](https://www.uc.edu/about/financial-aid/manage-aid/check-my-aid/catalyst-access.html)
  - Catalyst Access Catalyst is the University of Cincinnati student information system. This online resource and student portal is the entry point to your acade…
- [Catalyst Investors | Growth Equity | New York](https://catalyst.com/)
  - At Catalyst, We Are True Growth Investors With 20+ years of providing growth capital to B2B businesses, Catalyst is the consummate partner to support your ne…
- [[Release] cs2-external-catalyst - UnknownCheats](https://www.unknowncheats.me/forum/counter-strike-2-releases/744009-cs2-external-catalyst.html)
  - cs2-external-catalyst ... Tags [release], hitmarker, triggerbot, delay, hitchance, autowall, autostop, misc, flash, predictive « Previous Thread | Next Threa…

### Search warnings
- news:Rhinebeck Bancorp, Inc. earnings OR catalyst: No results found.

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

- **[S1]** RBKB fundamentals (yfinance)
  - Rhinebeck Bancorp, Inc.: price=12.3, rev=53355000.0, fcf=10893000.0, shares=15638237.0, rev_cagr=0.03754424938432588, ROIC=None, FCF yield=0.056631046935612064
- **[S2]** RBKB put screen (yfinance_options)
  - Expiration None (DTE None): 0 candidates; IV=None, IV rank=None, HV rank=None. No options chain available
- **[S3]** RBC News (web) — https://en.wikipedia.org/wiki/RBC_News
  - The RBC Group, or RosBusinessConsulting, is a Russian media group headquartered in Moscow. It was established in 1993.The company holds an informational agency RosBusinessConsul…
- **[S4]** Rhinebeck Bancorp Inc News (RBKB) - Investing.com (web) — https://www.investing.com/equities/rhinebeck-news
  - Get today's Rhinebeck stock news.Rhinebeck Bancorp, Inc. (RBKB) stock has soared to a 52-week high, reaching a price level of $10.59 USD. According to InvestingPro...
- **[S5]** Rhinebeck Bancorp, Inc. (RBKB) Stock Price, News... - Yahoo Finance (web) — https://finance.yahoo.com/quote/RBKB/?p=RBKB
  - Find the latest Rhinebeck Bancorp, Inc. (RBKB) stock quote, history, news and other vital information to help you with your stock trading and investing.
- **[S6]** RBKB News Today | Why did Rhinebeck Bancorp stock go down today? (web) — https://www.marketbeat.com/stocks/NASDAQ/RBKB/news/
  - Read today's RBKB news from trusted media outlets at MarketBeat.View real-time investing headlines and stock market news for your watchlist or the broader market.
- **[S7]** Rhinebeck Bancorp Stock Short Interest Report | NASDAQ:RBKB | Benzinga (web) — https://www.benzinga.com/quote/RBKB/short-interest
  - Short interest in Rhinebeck Bancorp Inc (NASDAQ:RBKB) increased during the last reporting period, rising from 86.78K to 181.74K. This put 4.01% of the company's publicly availab…
- **[S8]** Rhinebeck Bancorp, Inc.'s (NASDAQ:RBKB) largest shareholders are private companies with 58% ownership, individual investors own 19% (web) — https://finance.yahoo.com/news/rhinebeck-bancorp-inc-nasdaq-rbkb-135825434.html
  - The above button links to Coinbase. Yahoo Finance is not a broker-dealer or investment adviser and does not offer securities or cryptocurrencies for sale or facilitate trading. …
- **[S9]** Is Rhinebeck Bancorp, Inc. (RBKB) A Good Stock To Buy Now? (web) — https://finance.yahoo.com/news/rhinebeck-bancorp-inc-rbkb-good-200906442.html
  - The above button links to Coinbase. Yahoo Finance is not a broker-dealer or investment adviser and does not offer securities or cryptocurrencies for sale or facilitate trading. …
- **[S10]** Individual investors own 22% of Rhinebeck Bancorp, Inc. (NASDAQ:RBKB) shares but private companies control 59% of the company (web) — https://finance.yahoo.com/news/individual-investors-own-22-rhinebeck-141201638.html
  - The above button links to Coinbase. Yahoo Finance is not a broker-dealer or investment adviser and does not offer securities or cryptocurrencies for sale or facilitate trading. …

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

# RBKB — Planned Research Report

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
- Company: Rhinebeck Bancorp, Inc.
- Sector / industry: Financial Services / Banks - Regional
- Price: 12.3
- 52-week range: $6.74 – $12.88
- Market cap: $192.35M
- Enterprise value: -$161.05M
- Shares outstanding: 15.64M
- Beta: 0.148
- Book equity: $136.85M
- Revenue (latest): $53.35M
- EBITDA (latest): —
- Free cash flow (latest): $10.89M
- Operating income: —
- Operating margin: —
- EV / EBITDA: —
- ROIC: —
- FCF yield: 5.7%
- Debt / Equity: 0.22146552480051443
- FCF / share: $0.70
- Revenue / share: $3.41

### Capital structure
- Cash: $18.83M
- Short-term debt: $1.61M
- Long-term debt: $28.69M
- Total debt: $30.31M
- Net debt: $11.48M
- Net debt / EBITDA: —

### Growth
- Revenue CAGR: 3.8%
- FCF CAGR: -7.3%
- Latest revenue YoY: 85.7%
- Latest FCF YoY: 41.9%

### Market expectations (yfinance, sparse)
- Mean target: —
- Target range: — – —
- Recommendation: none

_Consensus revenue/EBITDA forecasts are often unavailable via free feeds; treat targets as point-in-time only._

### Historical KPIs (multi-year)

| Year | Revenue | OCF | Capex | FCF | EBITDA | LT debt | Cash | Net debt | Net income |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2025 | $53.35M | $11.74M | $850.00K | $10.89M | — | $28.69M | $18.83M | $9.87M | $10.04M |
| 2024 | $28.73M | $8.47M | $791.00K | $7.68M | — | $74.93M | $19.18M | $55.75M | -$8.62M |
| 2023 | $43.70M | $7.05M | $578.00K | $6.47M | — | $133.22M | $14.61M | $118.61M | $4.39M |
| 2022 | $47.77M | $14.79M | $1.13M | $13.66M | — | $62.88M | $16.82M | $46.06M | $7.00M |

## Charts

### Revenue & FCF history
![Revenue & FCF history](/charts/RBKB_fast_revenue_fcf.png)

### DCF scenario prices
![DCF scenario prices](/charts/RBKB_fast_dcf_scenarios.png)

### Base-case FCF path
![Base-case FCF path](/charts/RBKB_fast_base_fcf_path.png)

## DCF valuation (base / bull / bear) [S2]

> Simplified revenue->FCF DCF. Not investment advice; assumptions are editable heuristics.

- Spot price: $12.30
- Base revenue: $53.35M
- Shares: 15,638,237
- Net debt (Debt−Cash): $11.48M

| Scenario | Growth | FCF margin | WACC | Term. g | Equity value | Share price | Upside |
|----------|--------|------------|------|---------|--------------|-------------|--------|
| bear | 25.0% | 18.4% | 12.0% | 1.5% | $222.13M | $14.20 | 15.5% |
| base | 35.0% | 20.4% | 10.0% | 2.5% | $507.96M | $32.48 | 164.1% |
| bull | 42.0% | 23.4% | 9.0% | 3.0% | $941.29M | $60.19 | 389.4% |

### Assumption notes
- Base revenue growth seeded from historical rate (85.7%).


### Base-case projected FCF

- Year 1: revenue $72.03M, FCF $14.71M (PV $13.37M)
- Year 2: revenue $97.24M, FCF $19.85M (PV $16.41M)
- Year 3: revenue $131.27M, FCF $26.80M (PV $20.14M)
- Year 4: revenue $177.22M, FCF $36.18M (PV $24.71M)
- Year 5: revenue $239.25M, FCF $48.84M (PV $30.33M)
- Terminal value $667.54M (PV $414.49M)

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

- **[S1]** RBKB fundamentals (yfinance)
  - Rhinebeck Bancorp, Inc.: price=12.3, rev=53355000.0, fcf=10893000.0, shares=15638237.0, rev_cagr=0.03754424938432588, ROIC=None, FCF yield=0.056631046935612064
- **[S2]** RBKB DCF valuation (dcf)
  - Base share price=32.4822323870783, bull=60.191263927521966, bear=14.204002046386439
- **[S3]** RBKB put screen (yfinance_options)
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
