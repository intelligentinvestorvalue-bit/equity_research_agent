# CAG — Full research pack

> Not investment advice. Local research draft only.

**Templates:** memo, valuation, deep, income, fast
**Generated:** 2026-07-28T06:55:33.541683+00:00



---

# Template: Institutional deep dive (memo) (`memo`)

# CAG — Planned Research Report

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
- Company: ConAgra Brands, Inc.
- Sector / industry: Consumer Defensive / Packaged Foods
- Price: 15.24
- 52-week range: $12.53 – $20.32
- Market cap: —
- Enterprise value: $14.55B
- Shares outstanding: 475.03M
- Beta: -0.047
- Book equity: $6.36B
- Revenue (latest): $11.28B
- EBITDA (latest): -$1.04B
- Free cash flow (latest): $978.70M
- Operating income: $1.26B
- Operating margin: 11.2%
- EV / EBITDA: -14.0x
- ROIC: -10.7%
- FCF yield: —
- Debt / Equity: 1.1432616081540203
- FCF / share: $2.06
- Revenue / share: $23.75

### Capital structure
- Cash: $218.00M
- Short-term debt: $812.40M
- Long-term debt: $6.46B
- Total debt: $7.27B
- Net debt: $7.05B
- Net debt / EBITDA: -6.8x

### Growth
- Revenue CAGR: -2.8%
- FCF CAGR: 15.6%
- Latest revenue YoY: -2.9%
- Latest FCF YoY: -24.9%

### Market expectations (yfinance, sparse)
- Mean target: $14.38
- Target range: $12.00 – $23.00
- Recommendation: hold

_Consensus revenue/EBITDA forecasts are often unavailable via free feeds; treat targets as point-in-time only._

### Historical KPIs (multi-year)

| Year | Revenue | OCF | Capex | FCF | EBITDA | LT debt | Cash | Net debt | Net income |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2026 | $11.28B | $1.40B | $423.40M | $978.70M | -$1.04B | $6.46B | $218.00M | $6.24B | -$1.92B |
| 2025 | $11.61B | $1.69B | $389.30M | $1.30B | $1.97B | $6.23B | $68.00M | $6.17B | $1.15B |
| 2024 | $12.05B | $2.02B | $388.10M | $1.63B | $1.45B | $7.49B | $77.70M | $7.41B | $347.20M |
| 2023 | $12.28B | $995.40M | $362.20M | $633.20M | $1.69B | $7.08B | $93.30M | $6.99B | $683.60M |

## Charts

### Revenue & FCF history
![Revenue & FCF history](/charts/CAG_memo_revenue_fcf.png)

### DCF scenario prices
![DCF scenario prices](/charts/CAG_memo_dcf_scenarios.png)

### Base-case FCF path
![Base-case FCF path](/charts/CAG_memo_base_fcf_path.png)

### EV/EBITDA scenario prices
![EV/EBITDA scenario prices](/charts/CAG_memo_ev_ebitda_scenarios.png)

### Headwind/tailwind price ranges
![Headwind/tailwind price ranges](/charts/CAG_memo_scenario_ranges.png)

### Normalized price vs peers
![Normalized price vs peers](/charts/CAG_memo_peers_normalized.png)

## DCF valuation (base / bull / bear) [S3]

> Simplified revenue->FCF DCF. Not investment advice; assumptions are editable heuristics.

- Spot price: $15.24
- Base revenue: $11.28B
- Shares: 475,029,042
- Net debt (Debt−Cash): $7.05B

| Scenario | Growth | FCF margin | WACC | Term. g | Equity value | Share price | Upside |
|----------|--------|------------|------|---------|--------------|-------------|--------|
| bear | -2.9% | 6.7% | 12.0% | 1.5% | -$968.83M | $-2.04 | -113.4% |
| base | 6.0% | 8.7% | 10.0% | 2.5% | $8.45B | $17.79 | 16.7% |
| bull | 15.0% | 11.7% | 9.0% | 3.0% | $30.26B | $63.71 | 318.0% |

### Assumption notes
- Base revenue growth seeded from historical rate (-2.9%).
- Recent revenue declined (-2.9% YoY); base/bull use normalized mid-cycle growth instead of extrapolating the decline.

- _bear: model equity value is negative after net debt (-968,831,953); showing $-2.04/sh._

### Base-case projected FCF

- Year 1: revenue $11.96B, FCF $1.04B (PV $943.11M)
- Year 2: revenue $12.68B, FCF $1.10B (PV $908.82M)
- Year 3: revenue $13.44B, FCF $1.17B (PV $875.77M)
- Year 4: revenue $14.24B, FCF $1.24B (PV $843.92M)
- Year 5: revenue $15.10B, FCF $1.31B (PV $813.23M)
- Terminal value $17.90B (PV $11.11B)

## Valuation — EV/EBITDA scenarios [S2]

> Priced-in model: implied price = (EBITDA × EV/EBITDA − net debt) ÷ shares. Not a forecast.

- Spot: $15.24
- Net debt used: $7.05B

| Scenario | EBITDA | EV/EBITDA | Implied EV | Equity value | Implied price |
|---|---:|---:|---:|---:|---:|
| bear | $700.00M | 6.0x | $4.20B | -$2.85B | $-6.00 |
| base | $1.00B | 8.0x | $8.00B | $949.60M | $2.00 |
| bull | $1.20B | 10.0x | $12.00B | $4.95B | $10.42 |

- EBITDA missing or non-positive; scenarios use placeholder $1B EBITDA — edit before relying on prices.
- No current EV/EBITDA; defaulted base multiple to 8.0x.

## Scenario price ranges (headwinds & tailwinds) [S39]

> Medium-term (18–36 months (medium / medium-long term)) driver → EV/EBITDA bridge. Distinct from the FCF DCF path. Not investment advice.

- Spot: $15.24
- Sparse Street mean target: $14.38
- Anchor multiple: 8.0x (driver_ev_ebitda_bridge)
- Anchor EBITDA: $1.00B
- Probability-weighted midpoint: **$3.97** (heuristic weights, not a rating)
- Driver extraction: `rules`

### Headwinds (bear-case fuel)

- **Balance-sheet / refinancing pressure** — sector=Consumer Defensive industry=Packaged Foods revenue=11281600000.0 ebitda=-1038300000.0 fcf=978700000.0 net_debt=7050400000.0 nd_ebitda=-6.790330347683714 target=14.38125 rec= _(source: fundamentals)_
- **Regulatory / legal risk** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin, supply chain, cyber _(source: item_1a)_
- **Competitive / pricing pressure** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin, supply chain, cyber _(source: item_1a)_
- **Margin / cost headwind** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin, supply chain, cyber _(source: item_1a)_
- **Operational / cyber risk** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin, supply chain, cyber _(source: item_1a)_
- **Macro / demand slowdown** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin, supply chain, cyber _(source: item_1a)_

### Tailwinds (bull-case fuel)

- **Manageable leverage** — Net debt / EBITDA ≈ -6.8x — room for reinvestment or returns _(source: fundamentals)_
- **Positive free cash flow** — FCF $978.70M _(source: fundamentals)_
- **Growth / execution upside** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin, supply chain, cyber _(source: item_1a)_
- **Product / pricing power** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin, supply chain, cyber _(source: item_1a)_
- **Margin expansion / cost takeout** — ### Item 7 — MD&A (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, revenue, margin, supply chain, cyber, interest rate, custo _(source: item_7)_
- **Deleveraging / BS repair** — ### Item 7 — MD&A (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, revenue, margin, supply chain, cyber, interest rate, custo _(source: item_7)_
- **Contract / backlog wins** — ### Item 7 — MD&A (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, revenue, margin, supply chain, cyber, interest rate, custo _(source: item_7)_
- **Capital returns / FCF inflection** — ### Item 7 — MD&A (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, revenue, margin, supply chain, cyber, interest rate, custo _(source: item_7)_

### Price ranges by case

| Case | Prob. | Metric vs TTM | Multiple | Price low | Mid | High | Upside vs spot |
|---|---:|---:|---:|---:|---:|---:|---:|
| bear | 0.21 | 0.72x | 5.1x | $-7.86 | $-7.08 | $-6.31 | -146% |
| base | 0.45 | 1.04x | 8.0x | $1.45 | $2.67 | $3.90 | -82% |
| bull | 0.34 | 1.25x | 10.4x | $9.79 | $12.52 | $15.26 | -18% |

#### Bear — headwinds dominate

Headwinds bite: weaker operating trajectory and multiple compression. Equity duration shrinks if cash generation fails to offset leverage / competitive pressure.

- **Range:** $-7.86 – $-6.31 (mid $-7.08) · EBITDA $720.00M · multiple 5.1x
- Driver: **Balance-sheet / refinancing pressure** — sector=Consumer Defensive industry=Packaged Foods revenue=11281600000.0 ebitda=-1038300000.0 fcf=978700000.0 net_debt=7050400000.0 nd_ebitda=-6.790330347683714 
- Driver: **Regulatory / legal risk** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin,
- Driver: **Competitive / pricing pressure** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin,
- Driver: **Margin / cost headwind** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin,
- Driver: **Operational / cyber risk** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin,

#### Base — mixed execution

Balanced path: some tailwinds offset headwinds. Operating scale roughly holds with modest repair/normalization; valuation stays near the current EV/EBITDA anchor.

- **Range:** $1.45 – $3.90 (mid $2.67) · EBITDA $1.04B · multiple 8.0x
- Driver: **Manageable leverage** — Net debt / EBITDA ≈ -6.8x — room for reinvestment or returns
- Driver: **Positive free cash flow** — FCF $978.70M
- Driver: **Balance-sheet / refinancing pressure** — sector=Consumer Defensive industry=Packaged Foods revenue=11281600000.0 ebitda=-1038300000.0 fcf=978700000.0 net_debt=7050400000.0 nd_ebitda=-6.790330347683714 
- Driver: **Regulatory / legal risk** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin,

#### Bull — tailwinds dominate

Tailwinds compound: operating improvement plus a re-rating toward peer or recovery multiples as balance-sheet and growth narratives improve.

- **Range:** $9.79 – $15.26 (mid $12.52) · EBITDA $1.25B · multiple 10.4x
- Driver: **Manageable leverage** — Net debt / EBITDA ≈ -6.8x — room for reinvestment or returns
- Driver: **Positive free cash flow** — FCF $978.70M
- Driver: **Growth / execution upside** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin,
- Driver: **Product / pricing power** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin,
- Driver: **Margin expansion / cost takeout** — ### Item 7 — MD&A (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, revenue, margin, supply chain, cyber, 

### Method notes

- Item 1A risks weighted toward headwinds.
- Current ev_ebitda multiple missing; anchored at 8.0x.
- Peer EV/EBITDA band 8.4x–8.4x (median 8.4x) informs multiple ranges.
- Mapping follows Gemini/Perplexity-style scenario memos: qualitative drivers → operating metric & multiple paths → share-price ranges over a medium-term horizon.

## Peer & factor comps

- Sector / industry: Consumer Defensive / Packaged Foods
- Peers: —

| Ticker | Mkt cap | EV/EBITDA | ND/EBITDA | Beta | 1y | 5y | Vol |
|---|---:|---:|---:|---:|---:|---:|---:|
| CAG | — | 8.4x | 4.2x | -0.05 | -13.8% | -41.8% | 24.0% |

- No industry peer map match; comps limited to the subject ticker.

_Price returns are price-only (dividends ignored). Peer set is heuristic, not a formal comps universe._

## Earnings, guidance & revision catalysts

- Next earnings (calendar): 2026-09-30

| Date | EPS est | EPS actual | Surprise | 1-day move |
|---|---:|---:|---:|---:|
| 2026-09-30 | 0.28 | — | — | — |
| 2026-07-15 | 0.46 | 0.47 | 0.01 | 2.7% |
| 2026-04-01 | 0.40 | 0.39 | -0.01 | 1.3% |
| 2025-12-19 | 0.44 | 0.45 | 0.01 | -0.5% |
| 2025-10-01 | 0.33 | 0.39 | 0.06 | -0.6% |
| 2025-07-10 | 0.58 | 0.56 | -0.02 | -0.5% |
| 2025-04-03 | 0.53 | 0.51 | -0.02 | -0.4% |
| 2024-12-19 | 0.67 | 0.70 | 0.03 | 1.1% |
| 2024-10-02 | 0.60 | 0.53 | -0.07 | -2.4% |
| 2024-07-11 | 0.57 | 0.61 | 0.04 | -0.1% |
| 2024-04-04 | 0.65 | 0.69 | 0.04 | 1.5% |
| 2024-01-04 | 0.68 | 0.71 | 0.03 | -1.8% |

_EPS surprise vs 1-day move Pearson r=0.344 (n=11, p≈0.272); treat as suggestive only._

_Guidance vs Street and adjusted EBITDA are often missing from free feeds; use web/SEC sections for narrative guidance._

## Recent SEC filings (10-Q / 8-K)

| Date | Form | Description |
|---|---|---|
| 2026-07-15 | 10-K | [10-K](https://www.sec.gov/Archives/edgar/data/23217/000110465926083905/tmb-20260531x10k.htm) |
| 2026-07-15 | 8-K | [8-K](https://www.sec.gov/Archives/edgar/data/23217/000002321726000022/tmb-20260715x8k.htm) |
| 2026-06-23 | 8-K | [8-K](https://www.sec.gov/Archives/edgar/data/23217/000002321726000018/tmb-20260622x8k.htm) |
| 2026-05-07 | 8-K | [8-K](https://www.sec.gov/Archives/edgar/data/23217/000002321726000015/tmb-20260505x8k.htm) |
| 2026-04-13 | 8-K | [8-K](https://www.sec.gov/Archives/edgar/data/23217/000002321726000013/tmb-20260408x8k.htm) |
| 2026-04-01 | 10-Q | [10-Q](https://www.sec.gov/Archives/edgar/data/23217/000110465926038548/tmb-20260222x10q.htm) |
| 2026-04-01 | 8-K | [8-K](https://www.sec.gov/Archives/edgar/data/23217/000002321726000010/tmb-20260401x8k.htm) |
| 2026-02-18 | 8-K | [8-K](https://www.sec.gov/Archives/edgar/data/23217/000002321726000005/tmb-20260218x8k.htm) |
| 2026-02-17 | 8-K | [8-K](https://www.sec.gov/Archives/edgar/data/23217/000002321726000002/tmb-20260216x8k.htm) |
| 2025-12-19 | 10-Q | [10-Q](https://www.sec.gov/Archives/edgar/data/23217/000110465925123200/tmb-20251123x10q.htm) |
| 2025-12-19 | 8-K | [8-K](https://www.sec.gov/Archives/edgar/data/23217/000002321725000094/tmb-20251219x8k.htm) |
| 2025-10-06 | 8-K | [8-K](https://www.sec.gov/Archives/edgar/data/23217/000002321725000089/tmb-20251002x8k.htm) |

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

ConAgra Brands, Inc. (CAG) trades near 15.24 with market cap — and EV $14.55B. Net debt is $7.05B (ND/EBITDA -6.790330347683714). Latest revenue $11.28B, EBITDA -$1.04B, FCF $978.70M.

**Goal focus:** Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers.

What matters most (framework): balance-sheet trajectory, cash generation vs leverage, and whether market expectations (sparse free-data targets) already price execution risk.

EV/EBITDA implied prices — bear $-6.00 / base $2.00 / bull $10.42.

## Company setup & business model

**Keyword hits:** risk, litigation, regulation, competition, margin, supply chain, customer, segment, product, service, market, operations, network

- Narrative Description of Business  We compete throughout the food industry and focus on adding value for our customers who operate in the retail food and foodservice channels.
- Our operations, including our reporting segments, are described below.
- Our locations, including manufacturing facilities, within each reporting segment, are described in Item 2, Properties.
- Reporting Segments  Our reporting segments are as follows:  Grocery & Snacks  The Grocery & Snacks reporting segment principally includes branded, shelf-stable food products sold in various retail channels in the United States.
- Refrigerated & Frozen  The Refrigerated & Frozen reporting segment principally includes branded, temperature-controlled food products sold in various retail channels in the United States.
- International  The International reporting segment principally includes branded food products, in various temperature states, sold in various retail and foodservice channels outside of the United States.
- Foodservice  The Foodservice reporting segment includes branded and customized food products, including meals, entrees, sauces, and a variety of custom-manufactured culinary products packaged for sale to restaurants and other foodservice establishments primarily in the United States.
- General  The following discussion pertains to all of our reporting segments.
- Conagra Brands is a branded consumer packaged goods food company that operates in many sectors of the food industry, with a significant focus on the sale of branded, value-added consumer food products, as well as foodservice items and ingredients.
- Raw Materials and Packaging  We use many different raw materials, most of which are commodities, to make and package our products.
- The prices paid for raw materials used in making our food generally reflect factors such as global economic conditions, trade barriers or restrictions, supply and demand, weather, commodity market fluctuations, currency fluctuations, tariffs, and the effects of governmental agricultural programs, and may be impacted by supply chain disruptions including disruptions caused by weather, natural  disasters, geopolitical and military conflicts, and disease, in humans, plants, and animals.
- We seek to mitigate higher input costs through productivity and pricing initiatives and the use of derivative instruments to economically hedge a portion of forecasted future consumption.
- Competition  We experience intense competition for sales of our food items in our major markets.
- We compete primarily on the basis of quality, product innovation, value, convenience, customer service, brand recognition, and brand loyalty.
- For example, sales of frozen foods tend to be marginally higher during the winter months, pie sales are highest in November and December due to holidays, and production of certain of our products occurs seasonally, during or immediately following the purchase of agricultural crops.
- Some of our products are sold under licensing  arrangements with others, including our licensing arrangement with Dolly Parton and our licenses of the P.F.
- Government Regulation  The manufacture and sale of consumer food is highly regulated.
- Our operations, our products, and our practices are subject to various federal, state, local, and international laws and regulations and related regulatory oversight by various government agencies, including the United States Department of Agriculture, the Federal Food and Drug Administration, the Federal Trade Commission, the Consumer Product Safety Commission, the Occupational Safety and Health Administration, the Environmental  Protection Agency, the   Department of Labor, and various other federal, state, local, and international authorities (including government authorities in Canada and Mexico).
- In particular, the production, packaging, transportation, storage, distribution, advertising, labeling, quality, and safety of food products, the health and safety of our employees, and the protection of the environment are each subject to governmental regulation.
- Additionally, we are subject to data privacy and security regulations, anticorruption, anti-bribery, trade sanction and export, extended producer responsibility (such as regulations governing plastic or packaging taxes, recycling, and waste management programs), tax, and securities laws and regulations, accounting and reporting standards, and other financial laws and regulations.
- Werelyon our procedures, policies, andcomplianceprograms, aswellas legal advice fromin-houseandoutsidecounsel, to align our operations, products, and practiceswith applicable laws and regulations.
- We  believe that we are in compliance with such laws and regulations in all material respects and do not expect that continued compliance with such regulations will have a material effect upon capital expenditures, earnings, or our competitive position.
- Customers  Our products are sold, directly and through distributors, to chain, wholesale, value, cooperative, club, and independent grocery, pharmacy and drug, convenience and other store operators; and foodservice customers, including restaurants and bars, travel and leisure customers, schools, health care facilities, and government customers.
- Our products are also sold online through various e-commerce platforms and retailers.
- We leverage our six timeless values, which form the framework of our Company culture, to guide our approach to human capital management:    Integrity: Do the right things and do things right      External Focus: Center on the consumer, customer, competitor, and investor      Broad-Mindedness: Seek out and respect varied perspectives; embrace collaboration and assume positive intent      Agility: Convert insights into action with the speed of an entrepreneur      Leadership: Simplify, make decisions, inspire others, and act like an owner      Results: Leverage a “refuse-to-lose” obsession with impact and value creation    As of May 31, 2026, we had approximately 17,400 employees, primarily in the United States.
- We are focused on maintaining a strong culture of safety, in which all employees strive to protect themselves and their colleagues by being proactive towards risk identification and mitigation for people and our food products.
- Our health and safety team audits each of our facilities every 2-5 years, depending on risk profile, to review compliance with Conagra’s safety management system.
- This audit includes examination of leadership,  accountability, defect loss identification processes, inspections, training, safety regulation adherence and compliance with corporate policies.

_Source: latest 10-K Item 1 (Business), summarized locally._

## Variant perception

- **Consensus frame (sparse):** recommendation=hold, mean target=14.38125.
- **Bear:** leverage and execution risk dominate; cash generation fails to cover refinancing / reinvestment needs; equity remains constrained by net debt.
- **Bull:** cash-flow and strategic optionality re-rate the equity as leverage falls and growth/mix improves.
- **Middle:** returns may track free-cash-flow more than headline revenue — verify with driver analysis tab.

## Catalysts & monitoring

- Next earnings window (calendar): 2026-09-30
- Peer tape to watch: n/a
- Monitor: FCF vs net debt, leverage (ND/EBITDA), refinancing headlines, and material 8-K strategy updates.
- Recent filing: 10-K on 2026-07-15 — 10-K
- Recent filing: 8-K on 2026-07-15 — 8-K
- Recent filing: 8-K on 2026-06-23 — 8-K
- Recent filing: 8-K on 2026-05-07 — 8-K
- Recent filing: 8-K on 2026-04-13 — 8-K

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
| Guidance / outlook | Forward cash/earnings path | Conagra Brands (CAG) Stock Forecast and Price Target 2026CAG Stock Price Prediction 2025, 2026 & 2030: Analyst Targets ...Conagra Brands, Inc. (CAG) Analyst Ratings, Estimates ...C | Conagra Brands (CAG) Stock Forecast and Price Target 2026CAG Stock Price Prediction 2025, 2026 & 2030: Analyst Targets ...Conagra Brands, Inc. (CAG) Analyst Ratings, Estimates ...CAG Stock Price Quote | MorningstarWhat is the current Price Target and Forecast for Conagra ...What's Going On With Conagra Stock Thursday? - Benzinga |
| Margin / EBITDA | Mix and operating leverage | CAG Q4 Earnings Call Highlights Margin Reset and Cost Focus Conagra Brands outlines a margin reset focused on restoring profitability, boosting supply chain capabilities and simpli | CAG Q4 Earnings Call Highlights Margin Reset and Cost Focus |
| Leverage / refinancing | Balance-sheet repair | List of Leverage episodes - Wikipedia List of Leverage episodes Leverage is a U.S. television drama series, which ran on TNT from December 7, 2008 to December 25, 2012. [1] The ser | List of Leverage episodes - Wikipedia |
| Contract / backlog | Demand durability | Contracts Finder You can find details of recent procurement reforms, including Contracts Finder, on GOV.UK. Contract information posted prior to 26 February 2015 will not appear on | Contracts Finder |

_Proxies are heuristic extractions from public web/SEC context; verify against primary filings._

## Catalyst calendar

| Window | Catalyst | Notes |
|---|---|---|
| 2026-09-30 | Earnings | Next report date from yfinance calendar |
| 2026-07-15 | 10-K | 10-K |
| 2026-07-15 | 8-K | 8-K |
| 2026-06-23 | 8-K | 8-K |
| 2026-05-07 | 8-K | 8-K |
| 2026-04-13 | 8-K | 8-K |
| 2026-04-01 | 10-Q | 10-Q |
| 2026-04-01 | 8-K | 8-K |
| 2026-02-18 | 8-K | 8-K |
| 2026-02-17 | 8-K | 8-K |
| 2025-12-19 | 10-Q | 10-Q |
| 2025-12-19 | 8-K | 8-K |
| 2025-10-06 | 8-K | 8-K |
| Nov 28, 2025 | Web event | Conagra Brands (CAG) Stock Forecast and Price Target 2026CAG Stock Price Prediction 2025, 2026 & 2030: Analyst Targets ...Conagra Brands, In |
| Jul 16, 2026 | Web event | Conagra Brands, Inc.: Target Price Consensus and Analysts ... |
| Jul 17, 2026 | Web event | CAG | Conagra Brands Inc. Analyst Estimates & Ratings – WSJConagra Brands Inc. Research & Ratings | CAG | Barron'sConagra Brands, Inc. (CAG) |
| Apr 8, 2018 | Web event | Full Frame Documentary Film Festival |
| Jan 7, 2026 | Web event | A Look At Conagra Brands (CAG) Valuation As Project Catalyst ... |
| Apr 01, 2026 | Web event | Conagra Brands, Inc. (CAG) - ANALYST REPORT |
| Nov 28, 2025 | Web event | CAG Stock Price Prediction 2025, 2026 & 2030: Analyst Targets ... |
| Jun 21, 2026 | Web event | Conagra Brands (CAG) Faces Cost Pressures and Weak Demand ... |
| Jul 18, 2025 | Web event | Why are food manufacturers like CAG, KHC, CBP, GIS, TSN ... - Reddit |
| May 17, 2026 | Web event | How The Conagra Brands (CAG) Investment Story Is Shifting As ... |
| December 7, 2008 | Web event | List of Leverage episodes - Wikipedia |

## Web research — web_analysts

- Queries: CAG analyst price target, ConAgra Brands, Inc. stock rating OR consensus OR upgrade OR downgrade, CAG Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers analyst, CAG guidance OR investor day OR catalyst
- Unique hits: 24
- Pages fetched: 3/3

### Web synthesis — web_analysts (rule-based fallback — Ollama unavailable)
**Keyword hits:** guidance, revenue, margin, supply chain, customer, service, market

- [HIT] Conagra Brands (CAG) Stock Forecast & Price Target | www.marketbeat.com | https://www.marketbeat.com/stocks/NYSE/CAG/forecast/ CAG's current price target is $14.07.
- Learn why top analysts are making this stock forecast for Conagra Brands at MarketBeat.
- (CAG) stock, with detailed revenue and earnings estimates.
- [HIT] Jefferies Sticks to Its Hold Rating for Conagra Brands (CAG) | The Globe and Mail | https://www.theglobeandmail.com/investing/markets/stocks/CAG/pressreleases/3328132/jefferies-sticks-to-its-hold-rating-for-conagra-brands-cag/ In a report released yesterday, Scott Marks CFA from Jefferies reiterated a Hold rating on Conagra Brands, with a price target of $14.00.
- [HIT] Analysts’ Opinions Are Mixed on These Consumer Goods Stocks: Costco (COST), JM Smucker (SJM) and Conagra Brands (CAG) | The Globe and Mail | https://www.theglobeandmail.com/investing/markets/stocks/COST/pressreleases/2341924/analysts-opinions-are-mixed-on-these-consumer-goods-stocks-costco-cost-jm-smucker-sjm-and-conagra-brands-cag/ Unlock trusted, data-backed investing tools with TipRanks Premium, from analyst ratings and forecasts to breaking news and portfolio analysis.
- [HIT] CAG Q4 Earnings Call Highlights Margin Reset and Cost Focus | Yahoo Finance | https://finance.yahoo.com/markets/stocks/articles/cag-q4-earnings-call-highlights-140000454.html Conagra Brands outlines a margin reset focused on restoring profitability, boosting supply chain capabilities and simplifying its portfolio for fiscal 2027.
- | www.marketscreener.com | https://www.marketscreener.com/quote/stock/CONAGRA-BRANDS-INC-11968/consensus/ Jul 16, 2026 · Conagra Brands, Inc.
- | www.wsj.com | https://www.wsj.com/market-data/quotes/CAG/research-ratings Conagra Brands Inc.

### Sources found
- [Conagra Brands (CAG) Stock Forecast & Price Target](https://www.marketbeat.com/stocks/NYSE/CAG/forecast/)
  - CAG's current price target is $14.07. Learn why top analysts are making this stock forecast for Conagra Brands at MarketBeat.
- [What is the current Price Target and Forecast for Conagra Brands (CAG)](https://www.zacks.com/stock/research/CAG/price-target-stock-forecast)
  - Price Target Based on short-term price targets offered by 14 analysts, the average price target for Conagra Brands comes to $13.79. The forecasts range from …
- [Conagra Brands (CAG) Stock Forecast & Analyst Price Targets](https://stockanalysis.com/stocks/cag/forecast/)
  - Stock forecasts and analyst price target predictions for Conagra Brands, Inc. (CAG) stock, with detailed revenue and earnings estimates.
- [Conagra Brands (CAG) Stock Forecast & Price Target](https://www.tipranks.com/stocks/cag/forecast)
  - Conagra Brands (CAG) Stock forecast & analyst price target predictions based on 13 analysts offering 12-months price targets for CAG in the last 3 months.
- [Jefferies Sticks to Its Hold Rating for Conagra Brands (CAG)](https://www.theglobeandmail.com/investing/markets/stocks/CAG/pressreleases/3328132/jefferies-sticks-to-its-hold-rating-for-conagra-brands-cag/)
  - In a report released yesterday, Scott Marks CFA from Jefferies reiterated a Hold rating on Conagra Brands, with a price target of $14.00. TipRanks Welcomes a…
- [Analysts’ Opinions Are Mixed on These Consumer Goods Stocks: Costco (COST), JM Smucker (SJM) and Conagra Brands (CAG)](https://www.theglobeandmail.com/investing/markets/stocks/COST/pressreleases/2341924/analysts-opinions-are-mixed-on-these-consumer-goods-stocks-costco-cost-jm-smucker-sjm-and-conagra-brands-cag/)
  - Unlock trusted, data-backed investing tools with TipRanks Premium, from analyst ratings and forecasts to breaking news and portfolio analysis. Discover high-…
- [CAG Q4 Earnings Call Highlights Margin Reset and Cost Focus](https://finance.yahoo.com/markets/stocks/articles/cag-q4-earnings-call-highlights-140000454.html)
  - Conagra Brands outlines a margin reset focused on restoring profitability, boosting supply chain capabilities and simplifying its portfolio for fiscal 2027.
- [Top Wall Street forecasters revamp Conagra Brands expectations ahead of Q4 earnings](https://www.msn.com/en-us/money/news/top-wall-street-forecasters-revamp-conagra-brands-expectations-ahead-of-q4-earnings/ar-AA27jIDJ?ocid=BingNewsVerp)
  - Conagra Brands, Inc. CAG will release its fourth quarter earnings report before the opening bell on Wednesday, July 15. Analysts expect the Chicago, Illinois…
- [Conagra Brands, Inc.: Target Price Consensus and Analysts ...](https://www.marketscreener.com/quote/stock/CONAGRA-BRANDS-INC-11968/consensus/)
  - Jul 16, 2026 · Conagra Brands, Inc. analysts consensus, targets, ratings and recommendations | NYSE: CAG | NYSE
- [CAG | Conagra Brands Inc. Analyst Estimates & Ratings – WSJConagra Brands Inc. Research & Ratings | CAG | Barron'sConagra Brands, Inc. (CAG) Analyst Ratings, Estimates ...Conagra Brands, Inc.: Fundamental Analysis and Financial ...](https://www.wsj.com/market-data/quotes/CAG/research-ratings)
  - Conagra Brands Inc. analyst ratings, historical stock prices, earnings estimates & actuals. CAG updated stock price target summary. Jul 17, 2026 · Conagra Br…
- [Stocks Climb as Tech Shares Rally](https://finance.yahoo.com/news/stocks-climb-tech-shares-rally-160609958.html)
  - The S&P 500 Index ($SPX ) (SPY ) today is up by +0.67%, the Dow Jones Industrials Index ($DOWI ) (DIA ) is up by +0.56%, and the Nasdaq 100 Index ($IUXX...
- [Stocks Settle Higher on Upbeat Tech Outlook and Cooling Inflation](https://finance.yahoo.com/news/stocks-settle-higher-upbeat-tech-213340919.html)
  - The S&P 500 Index ($SPX ) (SPY ) on Thursday closed up by +0.79%, the Dow Jones Industrials Index...

### Search warnings
- news:CAG Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers analyst: No results found.

## Web research — web_drivers

- Queries: CAG Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers, ConAgra Brands, Inc. CAG outlook OR catalyst OR commodity OR uranium OR rare earth OR vanadium, CAG sector drivers OR market demand, ConAgra Brands, Inc. CAG backlog OR contract OR refinancing OR leverage
- Unique hits: 16
- Pages fetched: 2/3

### Web synthesis — web_drivers (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, revenue, margin, supply chain, segment, product, service, market

- (CAG): 18-section interactive report covering thesis, valuation, catalysts, risks, and alternative data signals.
- [HIT] Conagra Brands (CAG): The Market Is Pricing In More Fear Than The ...
- | seekingalpha.com | https://seekingalpha.com/article/4916572-conagra-brands-market-is-pricing-in-more-fear-than-the-fundamentals-justify Conagra Brands' free cash flow remains sufficient to cover the dividend through FY2026, providing headroom despite current strain.
- (CAG) stock, with detailed revenue and earnings estimates.
- - Benzinga | www.marketbeat.com | https://www.marketbeat.com/stocks/NYSE/CAG/forecast/ CAG's current price target is $14.07.
- Learn why top analysts are making this stock forecast for Conagra Brands at MarketBeat.
- (CAG) stock analyst estimates, including earnings and revenue, EPS, upgrades and downgrades.
- (CAG) stock analyst estimates, including earnings and revenue, EPS, upgrades and downgrades.

### Sources found
- [Conagra Brands, Inc. (CAG) — Investment Research by Semper Signum](https://sempersignum.com/reports/cag/)
  - Institutional-depth research on Conagra Brands, Inc. (CAG): 18-section interactive report covering thesis, valuation, catalysts, risks, and alternative data …
- [Conagra Brands (CAG): The Market Is Pricing In More Fear Than The ...](https://seekingalpha.com/article/4916572-conagra-brands-market-is-pricing-in-more-fear-than-the-fundamentals-justify)
  - Conagra Brands' free cash flow remains sufficient to cover the dividend through FY2026, providing headroom despite current strain. Read why CAG stock is a Buy.
- [CAG Analysis | SymThesis Institutional Research](https://symthesis.app/stocks/CAG/)
  - Institutional-grade research for ConAgra Brands, Inc. (CAG). Stress-test matrix, conviction mandates, and valuation synthesis.
- [Conagra Brands, Inc. (CAG) - ANALYST REPORT](https://ultrastockanalysispro.com/Ultra_Stock_Lists/Top_Earnings_Weekly/UEW_20260329/CAG_Comprehensive_Analyst_Report.pdf)
  - Next Major Catalyst: Apr 01, 2026 earnings report Seasonality: Historical analysis shows positive momentum in backtest period Technical Setup: Neutral - wait…
- [Conagra Brands (CAG) Stock Forecast & Analyst Price Targets](https://stockanalysis.com/stocks/cag/forecast/)
  - Stock forecasts and analyst price target predictions for Conagra Brands, Inc. (CAG) stock, with detailed revenue and earnings estimates.
- [Conagra Brands (CAG) Stock Forecast and Price Target 2026CAG Stock Price Prediction 2025, 2026 & 2030: Analyst Targets ...Conagra Brands, Inc. (CAG) Analyst Ratings, Estimates ...CAG Stock Price Quote | MorningstarWhat is the current Price Target and Forecast for Conagra ...What's Going On With Conagra Stock Thursday? - Benzinga](https://www.marketbeat.com/stocks/NYSE/CAG/forecast/)
  - CAG's current price target is $14.07. Learn why top analysts are making this stock forecast for Conagra Brands at MarketBeat. Nov 28, 2025 · Discover CAG’s s…
- [CAG Stock Price Prediction 2025, 2026 & 2030: Analyst Targets ...](https://www.benzinga.com/money/cag-stock-price-prediction)
  - Nov 28, 2025 · Discover CAG’s stock price forecasts for 2025, 2026, and 2030. Explore algorithmic projections, analyst targets, and both bullish and bearish …
- [Conagra Brands, Inc. (CAG) Analyst Ratings, Estimates ...](https://finance.yahoo.com/quote/CAG/analysis/?fr=sycsrp_catchall)
  - See Conagra Brands, Inc. (CAG) stock analyst estimates, including earnings and revenue, EPS, upgrades and downgrades.
- [Conagra Brands (CAG) Faces Cost Pressures and Weak Demand ...](https://finance.yahoo.com/markets/stocks/articles/conagra-brands-cag-faces-cost-030510734.html)
  - Jun 21, 2026 ... She noted that she was cutting estimates "again," largely due to rising cost inflation that continues to weigh on the sector. Conagra Brands…
- [Conagra Brands Inc (CAG) AI Stock Analysis - Danelfin](https://danelfin.com/stock/CAG)
  - CAG probability advantage of beating the market (3M): -4.59% ; Sentiment Impact (Long Tail). -. N/A ; Fundamentals Impact (Long Tail). -. N/A ; Income (TTM).…
- [Why are food manufacturers like CAG, KHC, CBP, GIS, TSN ... - Reddit](https://www.reddit.com/r/ValueInvesting/comments/1m3hu99/why_are_food_manufacturers_like_cag_khc_cbp_gis/)
  - Jul 18, 2025 ... I love it when the market gives you a sector specific issue. It isn't company specific. That matters. These are the set ups I look for and ...
- [How The Conagra Brands (CAG) Investment Story Is Shifting As ...](https://finance.yahoo.com/markets/stocks/articles/conagra-brands-cag-investment-story-231002916.html)
  - May 17, 2026 ... Stock market · Newsletters · Crypto · Tech · Magnificent 7; More Topics ... sector-level recalibration. Bearish Takeaways. From late March ...

### Search warnings
- news:CAG Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers: No results found.
- news:ConAgra Brands, Inc. CAG outlook OR catalyst OR commodity OR uranium OR rare earth OR vanadium: No results found.
- news:CAG sector drivers OR market demand: No results found.
- news:ConAgra Brands, Inc. CAG backlog OR contract OR refinancing OR leverage: No results found.

## SEC filing [S27]
- Extraction OK: True
- Item 1 chars: 28227
- Item 1A chars: 50000
- Item 7 chars: 50000
- Meta: {'accession_number': '0001104659-26-083905', 'filing_date': '2026-07-15', 'source': 'edgartools', 'path': 'C:\\DevWork\\equity_research_agent\\data\\filings\\CAG_10k.txt'}

## Qualitative analysis (local LLM)

_Item 1 Business summary mode: rule_based (see Company setup & business model)._

### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin, supply chain, cyber, interest rate, customer, segment, product, service, market, operations, subsidiary

- Our business is subject to various risks and uncertainties.
- Any of the risks and uncertainties described below could materially adversely affect our business, financial condition, and results of operations and should be considered in evaluating us.
- Although the risks are organized by headings and each risk is described separately, many of the risks are interrelated.
- While we believe we have identified and discussed below the key risk factors affecting our business, there may be additional risks  and uncertainties that are not presently known or that are not currently believed to be significant that may adversely affect our business, performance, or financial condition in the future.
- Market Risks  Deterioration in general economic conditions, an economic recession or periods of slow growth, periods of inflation or increasing interest rates, or economic uncertainty may affect consumers resulting in reductions in consumer spending and have in the past harmed and could continue to harm our business and results of operations.
- Our business and results of operations have in the past been and may continue to be adversely affected by changes in national or global stability and economic conditions, including periods of inflation and rising interest rates; decreased energy and fuel availability coupled with increased oil, energy and fuel costs (including fuel surcharges); reduced consumer confidence and declining consumer spending rates; actual or threatened hostilities or war and/or other geopolitical conflicts; declining benefits or changing eligibility requirements under government food assistance programs for consumers; changing international trade, immigration, and tax policies; recessions and periods of slow growth, decreased availability of capital, volatility in financial markets; rising or sustained high unemployment; supply chain challenges; labor shortages; the effects of governmental initiatives to manage economic conditions; and the negative impacts caused by pandemics, epidemics, and disease, in  humans, plants, and animals.
- These economic factors could continue to impact our business and operations in a variety of ways, including as follows:    consumers seeking to reduce their spending on food by shifting purchases to more generic, lower-priced, or other value offerings, or foregoing certain purchases altogether during economic downt...
- volatility in commodity and other input costs could substantially impact our result of operations;      rising interest rates may adversely impact our results of operations;    ─────────────────────────────────────────────────────────────────────────    decreased demand in the restaurant business, particularly casual and fine dining, may adversely affect our Foodservice operations;    ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────    volatility in the equity markets or interest rates could substantially impact our pension costs and required pension contributions; and      it may become more costly or difficult to obtain debt or equity financing to fund operations or investment opportunities, or to refinance our debt in the future, in each case on terms and withi...


### Item 7 — MD&A (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, uncertainty, litigation, regulation, revenue, margin, supply chain, cyber, interest rate, customer, segment, product, service, market, operations

- AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERATIONS  The following discussion and analysis is intended to provide a summary of significant factors relevant to our financial performance and condition.
- Examples of forward-looking statements include statements regarding our expected future financial performance or position, results of operations, business strategy, plans and objectives of management for future operations, and other statements that are not historical facts.
- Forward-looking statements provide our current expectations and beliefs concerning future events and are subject to risks, uncertainties, and factors relating to our business and operations, all of which are difficult to predict and could cause our actual results to differ materially from the expectations expressed in or implied by such forward-looking statements.
- These  risks, uncertainties, and factors include: risks associated with general economic and industry conditions, including inflation, oil, energy and fuel costs, reduced consumer confidence and spending, increased tariffs and taxes, actual or threatened hostilities or war and/or other geopolitical conflicts, declining benefits or changing eligibility requirements under government food assistance programs for consumers, rising unemployment, recessions, supply chain challenges, labor cost increases or  shortages, interest rate and currency rate fluctuations; risks related to the availability and prices of commodities and other supply chain resources, including raw materials, packaging, energy, and transportation, weather conditions, pandemics, epidemics, and disease, in humans, plants, and animals; disruptions or inefficiencies in our supply chain and/or operations; risks related to the effectiveness of our hedging activities and ability to respond to volatility in commodities; risks related  to the ultimate impact of, including reputational harm caused by, any product recalls and product liability or labeling litigation; risks related to our ability to execute operating and value creation plans and achieve returns on our investments and targeted operating efficiencies from cost-saving initiatives, and to benefit from trade optimization programs; risks related to our ability to deleverage on currently anticipated timelines, and to continue to access capital on acceptable terms or at  all; risks related to the Company’s competitive environment, cost structure, and related market conditions; risks related to our ability to respond to changing consumer preferences, including health and wellness perceptions and the success of our innovation and marketing investments; risks associated with actions by our customers, including changes in distribution and purchasing terms; risks related to the seasonality of our business; risks associated with our contract manufacturing arrangements and other third-party service provider dependencies; risks associated with actions of governments and regulatory bodies that affect our businesses, including regulations or interpretations designed to address climate change; risks related to the Company’s ability to execute on its strategies or achieve expectations related to environmental, social, and governance matters, including as a result of evolving legal, regulatory, and other standards, processes, and assumptions, the pace of scientific  and technological developments, increased costs, the availability of requisite financing, and changes in carbon pricing or carbon taxes; risks related to a material failure in or breach of our or our vendors’ information technology systems and other cybersecurity incidents; risks related to our ability to identify, attract, hire, train, retain and develop qualified personnel; risk of increased pension, labor or people-related expenses; risks and uncertainties associated with intangible assets,  including any future goodwill or intangible assets impairment charges; risks relating to our ability to protect our intellectual property rights; risks relating to acquisition,   divestiture, joint venture or investment activities; the amount and timing of future dividends, which remain subject to Board approval and depend on market and other conditions; the amount and timing of future stock repurchases; and other risks described in our reports filed from time to time with the U.S.
- Trends Impacting our Business  We continue to expect our industry to be impacted by weak consumer sentiment, inflation, commodity cost fluctuations, supply chain pressures, trade and regulatory uncertainty, and other global macroeconomic challenges.
- tariffs and reciprocal tariffs caused increased uncertainty as well as input cost inflation in key  materials used in our products, including tin-plate steel used in packaging for our canned products, which we were able to partially offset with productivity initiatives and price increases on impacted products.
- We will continue to evaluate the evolving macroeconomic environment to take action to mitigate the impact on our business, consolidated results of operations, and financial condition.
- While we will continue to seek to offset input cost inflation with productivity initiatives and tariff mitigation efforts, we anticipate that we may need to increase prices on certain products in fiscal 2027 to mitigate margin impacts and would expect corresponding elasticity impacts.


## Research loop (think → act)

1. _heuristic_ — Coverage looks adequate for this pass; stopping iterative loop.

## Sources

- **[S1]** CAG fundamentals (yfinance)
  - ConAgra Brands, Inc.: price=15.24, rev=11281600000.0, fcf=978700000.0, shares=475029042.0, rev_cagr=-0.027791350655803293, ROIC=-0.10697344868735084, FCF yield=None
- **[S2]** CAG EV/EBITDA valuation (multiples)
  - Base implied price=1.9990356715916329, multiple=8.0
- **[S3]** CAG DCF valuation (dcf)
  - Base share price=17.78553979162984, bull=63.71028020338544, bear=-2.0395215193000564
- **[S4]** CAG peer comps (peers)
  - Peers: ; rows=1
- **[S5]** CAG earnings history (earnings)
  - rows=12; next=2026-09-30
- **[S6]** Conagra Brands (CAG) Stock Forecast & Price Target (web) — https://www.marketbeat.com/stocks/NYSE/CAG/forecast/
  - CAG's current price target is $14.07. Learn why top analysts are making this stock forecast for Conagra Brands at MarketBeat.
- **[S7]** What is the current Price Target and Forecast for Conagra Brands (CAG) (web) — https://www.zacks.com/stock/research/CAG/price-target-stock-forecast
  - Price Target Based on short-term price targets offered by 14 analysts, the average price target for Conagra Brands comes to $13.79. The forecasts range from a low of $12.00 to a…
- **[S8]** Conagra Brands (CAG) Stock Forecast & Analyst Price Targets (web) — https://stockanalysis.com/stocks/cag/forecast/
  - Stock forecasts and analyst price target predictions for Conagra Brands, Inc. (CAG) stock, with detailed revenue and earnings estimates.
- **[S9]** Conagra Brands (CAG) Stock Forecast & Price Target (web) — https://www.tipranks.com/stocks/cag/forecast
  - Conagra Brands (CAG) Stock forecast & analyst price target predictions based on 13 analysts offering 12-months price targets for CAG in the last 3 months.
- **[S10]** Jefferies Sticks to Its Hold Rating for Conagra Brands (CAG) (web) — https://www.theglobeandmail.com/investing/markets/stocks/CAG/pressreleases/3328132/jefferies-sticks-to-its-hold-rating-for-conagra-brands-cag/
  - In a report released yesterday, Scott Marks CFA from Jefferies reiterated a Hold rating on Conagra Brands, with a price target of $14.00. TipRanks Welcomes a New ETF – NYSE:RANK…
- **[S11]** Analysts’ Opinions Are Mixed on These Consumer Goods Stocks: Costco (COST), JM Smucker (SJM) and Conagra Brands (CAG) (web) — https://www.theglobeandmail.com/investing/markets/stocks/COST/pressreleases/2341924/analysts-opinions-are-mixed-on-these-consumer-goods-stocks-costco-cost-jm-smucker-sjm-and-conagra-brands-cag/
  - Unlock trusted, data-backed investing tools with TipRanks Premium, from analyst ratings and forecasts to breaking news and portfolio analysis. Discover high-conviction stock pic…
- **[S12]** CAG Q4 Earnings Call Highlights Margin Reset and Cost Focus (web) — https://finance.yahoo.com/markets/stocks/articles/cag-q4-earnings-call-highlights-140000454.html
  - Conagra Brands outlines a margin reset focused on restoring profitability, boosting supply chain capabilities and simplifying its portfolio for fiscal 2027.
- **[S13]** Top Wall Street forecasters revamp Conagra Brands expectations ahead of Q4 earnings (web) — https://www.msn.com/en-us/money/news/top-wall-street-forecasters-revamp-conagra-brands-expectations-ahead-of-q4-earnings/ar-AA27jIDJ?ocid=BingNewsVerp
  - Conagra Brands, Inc. CAG will release its fourth quarter earnings report before the opening bell on Wednesday, July 15. Analysts expect the Chicago, Illinois-based company to re…
- **[S14]** Conagra Brands (CAG) Stock Forecast and Price Target 2026 (web_page) — https://www.marketbeat.com/stocks/NYSE/CAG/forecast/
  - Conagra Brands (CAG) Stock Forecast and Price Target 2026 Skip to main content → Trump's New Dollar (From Porter & Company) (Ad) Free CAG Stock Alerts Conagra Brands (CAG)  Stoc…
- **[S15]** What is the current Price Target and Forecast for Conagra Brands (CAG) (web_page) — https://www.zacks.com/stock/research/CAG/price-target-stock-forecast
  - Pardon Our Interruption As you were browsing something about your browser made us think you were a bot. There are a few reasons this might happen: You're a power user moving thr…
- **[S16]** Conagra Brands (CAG) Stock Forecast & Analyst Price Targets (web_page) — https://stockanalysis.com/stocks/cag/forecast/
  - Conagra Brands (CAG) Stock Forecast & Analyst Price Targets Collapse Conagra Brands, Inc. (CAG) NYSE: CAG · Real-Time Price · USD Full Chart Watchlist Alerts Compare 15.24 +0.47…
- **[S17]** Conagra Brands, Inc. (CAG) — Investment Research by Semper Signum (web) — https://sempersignum.com/reports/cag/
  - Institutional-depth research on Conagra Brands, Inc. (CAG): 18-section interactive report covering thesis, valuation, catalysts, risks, and alternative data signals. By Semper S…
- **[S18]** Conagra Brands (CAG): The Market Is Pricing In More Fear Than The ... (web) — https://seekingalpha.com/article/4916572-conagra-brands-market-is-pricing-in-more-fear-than-the-fundamentals-justify
  - Conagra Brands' free cash flow remains sufficient to cover the dividend through FY2026, providing headroom despite current strain. Read why CAG stock is a Buy.
- **[S19]** CAG Analysis | SymThesis Institutional Research (web) — https://symthesis.app/stocks/CAG/
  - Institutional-grade research for ConAgra Brands, Inc. (CAG). Stress-test matrix, conviction mandates, and valuation synthesis.
- **[S20]** Conagra Brands, Inc. (CAG) - ANALYST REPORT (web) — https://ultrastockanalysispro.com/Ultra_Stock_Lists/Top_Earnings_Weekly/UEW_20260329/CAG_Comprehensive_Analyst_Report.pdf
  - Next Major Catalyst: Apr 01, 2026 earnings report Seasonality: Historical analysis shows positive momentum in backtest period Technical Setup: Neutral - waiting for confluence s…
- **[S21]** Conagra Brands (CAG) Stock Forecast & Analyst Price Targets (web) — https://stockanalysis.com/stocks/cag/forecast/
  - Stock forecasts and analyst price target predictions for Conagra Brands, Inc. (CAG) stock, with detailed revenue and earnings estimates.
- **[S22]** Conagra Brands (CAG) Stock Forecast and Price Target 2026CAG Stock Price Prediction 2025, 2026 & 2030: Analyst Targets ...Conagra Brands, Inc. (CAG) Analyst Ratings, Estimates ...CAG Stock Price Quote | MorningstarWhat is the current Price Target and Forecast for Conagra ...What's Going On With Conagra Stock Thursday? - Benzinga (web) — https://www.marketbeat.com/stocks/NYSE/CAG/forecast/
  - CAG's current price target is $14.07. Learn why top analysts are making this stock forecast for Conagra Brands at MarketBeat. Nov 28, 2025 · Discover CAG’s stock price forecasts…
- **[S23]** CAG Stock Price Prediction 2025, 2026 & 2030: Analyst Targets ... (web) — https://www.benzinga.com/money/cag-stock-price-prediction
  - Nov 28, 2025 · Discover CAG’s stock price forecasts for 2025, 2026, and 2030. Explore algorithmic projections, analyst targets, and both bullish and bearish scenarios for CAG’s …
- **[S24]** Conagra Brands, Inc. (CAG) Analyst Ratings, Estimates ... (web) — https://finance.yahoo.com/quote/CAG/analysis/?fr=sycsrp_catchall
  - See Conagra Brands, Inc. (CAG) stock analyst estimates, including earnings and revenue, EPS, upgrades and downgrades.
- **[S25]** Conagra Brands, Inc. (CAG) — Investment Research by Semper Signum (web_page) — https://sempersignum.com/reports/cag/
  - Conagra Brands, Inc. (CAG) — Investment Research by Semper Signum This report is best viewed on desktop for the full interactive experience. × Conagra Brands, Inc. CAG Long $14.…
- **[S26]** CAG Analysis | SymThesis Institutional Research (web_page) — https://symthesis.app/stocks/CAG/
  - CAG Analysis | SymThesis Institutional Research CAG Institutional Snapshot ConAgra Brands, Inc. · Consumer Defensive · Packaged Foods Current Price $13.38 P/E Ratio 8.0 PEG Rati…
- **[S27]** CAG 10-K (sec)
  - Item 1 chars=28227, Item 1A chars=50000, Item 7 chars=50000, ok=True, source=edgartools
- **[S28]** CAG 10-K 2026-07-15 (sec) — https://www.sec.gov/Archives/edgar/data/23217/000110465926083905/tmb-20260531x10k.htm
  - 10-K
- **[S29]** CAG 8-K 2026-07-15 (sec) — https://www.sec.gov/Archives/edgar/data/23217/000002321726000022/tmb-20260715x8k.htm
  - 8-K
- **[S30]** CAG 8-K 2026-06-23 (sec) — https://www.sec.gov/Archives/edgar/data/23217/000002321726000018/tmb-20260622x8k.htm
  - 8-K
- **[S31]** CAG 8-K 2026-05-07 (sec) — https://www.sec.gov/Archives/edgar/data/23217/000002321726000015/tmb-20260505x8k.htm
  - 8-K
- **[S32]** CAG 8-K 2026-04-13 (sec) — https://www.sec.gov/Archives/edgar/data/23217/000002321726000013/tmb-20260408x8k.htm
  - 8-K
- **[S33]** CAG 10-Q 2026-04-01 (sec) — https://www.sec.gov/Archives/edgar/data/23217/000110465926038548/tmb-20260222x10q.htm
  - 10-Q
- **[S34]** CAG 8-K 2026-04-01 (sec) — https://www.sec.gov/Archives/edgar/data/23217/000002321726000010/tmb-20260401x8k.htm
  - 8-K
- **[S35]** CAG 8-K 2026-02-18 (sec) — https://www.sec.gov/Archives/edgar/data/23217/000002321726000005/tmb-20260218x8k.htm
  - 8-K
- **[S36]** Item 1 Business summary (nlp)
  - ### Item 1 — Business (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, litigation, regulation, competition, margin, supply chain, customer, segment, product, s…
- **[S37]** Item 1A summary (nlp)
  - ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin, supply chain, cy…
- **[S38]** Item 7 summary (nlp)
  - ### Item 7 — MD&A (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, revenue, margin, supply chain, cyber, interest rate, cu…
- **[S39]** CAG scenario price ranges (scenarios)
  - ok=True; base mid=2.6726786948744072; headwinds=6; tailwinds=8
- **[S40]** CAG driver analysis (drivers)
  - ok=False; drivers=7
- **[S41]** CAG memo sections (memo)
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

# CAG — Planned Research Report

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
- Company: ConAgra Brands, Inc.
- Sector / industry: Consumer Defensive / Packaged Foods
- Price: 15.24
- 52-week range: $12.53 – $20.32
- Market cap: —
- Enterprise value: $14.55B
- Shares outstanding: 475.03M
- Beta: -0.047
- Book equity: $6.36B
- Revenue (latest): $11.28B
- EBITDA (latest): -$1.04B
- Free cash flow (latest): $978.70M
- Operating income: $1.26B
- Operating margin: 11.2%
- EV / EBITDA: -14.0x
- ROIC: -10.7%
- FCF yield: —
- Debt / Equity: 1.1432616081540203
- FCF / share: $2.06
- Revenue / share: $23.75

### Capital structure
- Cash: $218.00M
- Short-term debt: $812.40M
- Long-term debt: $6.46B
- Total debt: $7.27B
- Net debt: $7.05B
- Net debt / EBITDA: -6.8x

### Growth
- Revenue CAGR: -2.8%
- FCF CAGR: 15.6%
- Latest revenue YoY: -2.9%
- Latest FCF YoY: -24.9%

### Market expectations (yfinance, sparse)
- Mean target: $14.38
- Target range: $12.00 – $23.00
- Recommendation: hold

_Consensus revenue/EBITDA forecasts are often unavailable via free feeds; treat targets as point-in-time only._

### Historical KPIs (multi-year)

| Year | Revenue | OCF | Capex | FCF | EBITDA | LT debt | Cash | Net debt | Net income |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2026 | $11.28B | $1.40B | $423.40M | $978.70M | -$1.04B | $6.46B | $218.00M | $6.24B | -$1.92B |
| 2025 | $11.61B | $1.69B | $389.30M | $1.30B | $1.97B | $6.23B | $68.00M | $6.17B | $1.15B |
| 2024 | $12.05B | $2.02B | $388.10M | $1.63B | $1.45B | $7.49B | $77.70M | $7.41B | $347.20M |
| 2023 | $12.28B | $995.40M | $362.20M | $633.20M | $1.69B | $7.08B | $93.30M | $6.99B | $683.60M |

## Charts

### Revenue & FCF history
![Revenue & FCF history](/charts/CAG_valuation_revenue_fcf.png)

### DCF scenario prices
![DCF scenario prices](/charts/CAG_valuation_dcf_scenarios.png)

### Base-case FCF path
![Base-case FCF path](/charts/CAG_valuation_base_fcf_path.png)

### EV/EBITDA scenario prices
![EV/EBITDA scenario prices](/charts/CAG_valuation_ev_ebitda_scenarios.png)

### Headwind/tailwind price ranges
![Headwind/tailwind price ranges](/charts/CAG_valuation_scenario_ranges.png)

## DCF valuation (base / bull / bear) [S2]

> Simplified revenue->FCF DCF. Not investment advice; assumptions are editable heuristics.

- Spot price: $15.24
- Base revenue: $11.28B
- Shares: 475,029,042
- Net debt (Debt−Cash): $7.05B

| Scenario | Growth | FCF margin | WACC | Term. g | Equity value | Share price | Upside |
|----------|--------|------------|------|---------|--------------|-------------|--------|
| bear | -2.9% | 6.7% | 12.0% | 1.5% | -$968.83M | $-2.04 | -113.4% |
| base | 6.0% | 8.7% | 10.0% | 2.5% | $8.45B | $17.79 | 16.7% |
| bull | 15.0% | 11.7% | 9.0% | 3.0% | $30.26B | $63.71 | 318.0% |

### Assumption notes
- Base revenue growth seeded from historical rate (-2.9%).
- Recent revenue declined (-2.9% YoY); base/bull use normalized mid-cycle growth instead of extrapolating the decline.

- _bear: model equity value is negative after net debt (-968,831,953); showing $-2.04/sh._

### Base-case projected FCF

- Year 1: revenue $11.96B, FCF $1.04B (PV $943.11M)
- Year 2: revenue $12.68B, FCF $1.10B (PV $908.82M)
- Year 3: revenue $13.44B, FCF $1.17B (PV $875.77M)
- Year 4: revenue $14.24B, FCF $1.24B (PV $843.92M)
- Year 5: revenue $15.10B, FCF $1.31B (PV $813.23M)
- Terminal value $17.90B (PV $11.11B)

## Valuation — EV/EBITDA scenarios [S3]

> Priced-in model: implied price = (EBITDA × EV/EBITDA − net debt) ÷ shares. Not a forecast.

- Spot: $15.24
- Net debt used: $7.05B

| Scenario | EBITDA | EV/EBITDA | Implied EV | Equity value | Implied price |
|---|---:|---:|---:|---:|---:|
| bear | $700.00M | 6.0x | $4.20B | -$2.85B | $-6.00 |
| base | $1.00B | 8.0x | $8.00B | $949.60M | $2.00 |
| bull | $1.20B | 10.0x | $12.00B | $4.95B | $10.42 |

- EBITDA missing or non-positive; scenarios use placeholder $1B EBITDA — edit before relying on prices.
- No current EV/EBITDA; defaulted base multiple to 8.0x.

## Scenario price ranges (headwinds & tailwinds) [S29]

> Medium-term (18–36 months (medium / medium-long term)) driver → EV/EBITDA bridge. Distinct from the FCF DCF path. Not investment advice.

- Spot: $15.24
- Sparse Street mean target: $14.38
- Anchor multiple: 8.0x (driver_ev_ebitda_bridge)
- Anchor EBITDA: $1.00B
- Probability-weighted midpoint: **$3.97** (heuristic weights, not a rating)
- Driver extraction: `rules`

### Headwinds (bear-case fuel)

- **Balance-sheet / refinancing pressure** — sector=Consumer Defensive industry=Packaged Foods revenue=11281600000.0 ebitda=-1038300000.0 fcf=978700000.0 net_debt=7050400000.0 nd_ebitda=-6.790330347683714 target=14.38125 rec= _(source: fundamentals)_
- **Regulatory / legal risk** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin, supply chain, cyber _(source: item_1a)_
- **Competitive / pricing pressure** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin, supply chain, cyber _(source: item_1a)_
- **Margin / cost headwind** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin, supply chain, cyber _(source: item_1a)_
- **Operational / cyber risk** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin, supply chain, cyber _(source: item_1a)_
- **Macro / demand slowdown** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin, supply chain, cyber _(source: item_1a)_

### Tailwinds (bull-case fuel)

- **Manageable leverage** — Net debt / EBITDA ≈ -6.8x — room for reinvestment or returns _(source: fundamentals)_
- **Positive free cash flow** — FCF $978.70M _(source: fundamentals)_
- **Growth / execution upside** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin, supply chain, cyber _(source: item_1a)_
- **Product / pricing power** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin, supply chain, cyber _(source: item_1a)_
- **Margin expansion / cost takeout** — ### Item 7 — MD&A (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, revenue, margin, supply chain, cyber, interest rate, custo _(source: item_7)_
- **Deleveraging / BS repair** — ### Item 7 — MD&A (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, revenue, margin, supply chain, cyber, interest rate, custo _(source: item_7)_
- **Contract / backlog wins** — ### Item 7 — MD&A (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, revenue, margin, supply chain, cyber, interest rate, custo _(source: item_7)_
- **Capital returns / FCF inflection** — ### Item 7 — MD&A (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, revenue, margin, supply chain, cyber, interest rate, custo _(source: item_7)_

### Price ranges by case

| Case | Prob. | Metric vs TTM | Multiple | Price low | Mid | High | Upside vs spot |
|---|---:|---:|---:|---:|---:|---:|---:|
| bear | 0.21 | 0.72x | 5.1x | $-7.86 | $-7.08 | $-6.31 | -146% |
| base | 0.45 | 1.04x | 8.0x | $1.45 | $2.67 | $3.90 | -82% |
| bull | 0.34 | 1.25x | 10.4x | $9.79 | $12.52 | $15.26 | -18% |

#### Bear — headwinds dominate

Headwinds bite: weaker operating trajectory and multiple compression. Equity duration shrinks if cash generation fails to offset leverage / competitive pressure.

- **Range:** $-7.86 – $-6.31 (mid $-7.08) · EBITDA $720.00M · multiple 5.1x
- Driver: **Balance-sheet / refinancing pressure** — sector=Consumer Defensive industry=Packaged Foods revenue=11281600000.0 ebitda=-1038300000.0 fcf=978700000.0 net_debt=7050400000.0 nd_ebitda=-6.790330347683714 
- Driver: **Regulatory / legal risk** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin,
- Driver: **Competitive / pricing pressure** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin,
- Driver: **Margin / cost headwind** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin,
- Driver: **Operational / cyber risk** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin,

#### Base — mixed execution

Balanced path: some tailwinds offset headwinds. Operating scale roughly holds with modest repair/normalization; valuation stays near the current EV/EBITDA anchor.

- **Range:** $1.45 – $3.90 (mid $2.67) · EBITDA $1.04B · multiple 8.0x
- Driver: **Manageable leverage** — Net debt / EBITDA ≈ -6.8x — room for reinvestment or returns
- Driver: **Positive free cash flow** — FCF $978.70M
- Driver: **Balance-sheet / refinancing pressure** — sector=Consumer Defensive industry=Packaged Foods revenue=11281600000.0 ebitda=-1038300000.0 fcf=978700000.0 net_debt=7050400000.0 nd_ebitda=-6.790330347683714 
- Driver: **Regulatory / legal risk** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin,

#### Bull — tailwinds dominate

Tailwinds compound: operating improvement plus a re-rating toward peer or recovery multiples as balance-sheet and growth narratives improve.

- **Range:** $9.79 – $15.26 (mid $12.52) · EBITDA $1.25B · multiple 10.4x
- Driver: **Manageable leverage** — Net debt / EBITDA ≈ -6.8x — room for reinvestment or returns
- Driver: **Positive free cash flow** — FCF $978.70M
- Driver: **Growth / execution upside** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin,
- Driver: **Product / pricing power** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin,
- Driver: **Margin expansion / cost takeout** — ### Item 7 — MD&A (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, revenue, margin, supply chain, cyber, 

### Method notes

- Item 1A risks weighted toward headwinds.
- Current ev_ebitda multiple missing; anchored at 8.0x.
- Mapping follows Gemini/Perplexity-style scenario memos: qualitative drivers → operating metric & multiple paths → share-price ranges over a medium-term horizon.

## Web research — web_analysts

- Queries: CAG analyst price target, ConAgra Brands, Inc. stock rating OR consensus OR upgrade OR downgrade, CAG Estimate intrinsic value under base / bull / bear scenarios analyst
- Unique hits: 15
- Pages fetched: 2/3

### Web synthesis — web_analysts (rule-based fallback — Ollama unavailable)
**Keyword hits:** guidance, revenue, margin, service, market

- [HIT] Conagra Brands (CAG) Stock Forecast and Price Target 2026 | www.marketbeat.com | https://www.marketbeat.com/stocks/NYSE/CAG/forecast/ CAG's current price target is $15.00.
- Learn why top analysts are making this stock forecast for Conagra Brands at MarketBeat.According to the 18 analysts' twelve-month price targets for Conagra Brands, the average price target is $15.00.
- [HIT] Jefferies Sticks to Its Hold Rating for Conagra Brands (CAG) | The Globe and Mail | https://www.theglobeandmail.com/investing/markets/stocks/CAG/pressreleases/3328132/jefferies-sticks-to-its-hold-rating-for-conagra-brands-cag/ In a report released yesterday, Scott Marks CFA from Jefferies reiterated a Hold rating on Conagra Brands, with a price target of $14.00.
- [HIT] Analysts’ Opinions Are Mixed on These Consumer Goods Stocks: Costco (COST), JM Smucker (SJM) and Conagra Brands (CAG) | The Globe and Mail | https://www.theglobeandmail.com/investing/markets/stocks/COST/pressreleases/2341924/analysts-opinions-are-mixed-on-these-consumer-goods-stocks-costco-cost-jm-smucker-sjm-and-conagra-brands-cag/ Unlock trusted, data-backed investing tools with TipRanks Premium, from analyst ratings and forecasts to breaking news and portfolio analysis.
- [HIT] Conagra Brands (CAG) Faces Mounting Challenges as Bernstein Cuts Rating and Price Target | Yahoo Finance | https://finance.yahoo.com/markets/stocks/articles/conagra-brands-cag-faces-mounting-015938134.html The above button links to Coinbase.
- (CAG) stock, with detailed revenue and earnings estimates.
- Analyst Estimates & Ratings – WSJ | www.wsj.com | https://www.wsj.com/market-data/quotes/CAG/research-ratings Conagra Brands Inc.
- | m.marketscreener.com | https://m.marketscreener.com/quote/stock/CONAGRA-BRANDS-INC-11968/consensus/ Conagra Brands, Inc.

### Sources found
- [Conagra Brands (CAG) Stock Forecast and Price Target 2026](https://www.marketbeat.com/stocks/NYSE/CAG/forecast/)
  - CAG's current price target is $15.00. Learn why top analysts are making this stock forecast for Conagra Brands at MarketBeat.According to the 18 analysts' tw…
- [Conagra Brands Analyst Ratings and Price Targets | NYSE:CAG](https://www.benzinga.com/quote/CAG/analyst-ratings)
  - The latest price target for Conagra Brands (NYSE:CAG) was reported by UBS on July 16, 2026. The analyst firm set a price target for $14.00 expecting CAG to f…
- [Conagra Brands (CAG) Stock Forecast, Price Targets and Analysts...](https://www.tipranks.com/stocks/cag/forecast)
  - Analyze Forecast. Average Price Target.The average price target for Conagra Brands is 13.73. This is based on 11 Wall Streets Analysts 12-month price targets…
- [CAG Forecast — Price Target — Prediction for 2027 — TradingView](https://www.tradingview.com/symbols/NYSE-CAG/forecast/)
  - According to analysts, CAG price target is 15.20 USD with a max estimate of 18.00 USD and a min estimate of 13.00 USD. Check if this forecast comes true in a…
- [Jefferies Sticks to Its Hold Rating for Conagra Brands (CAG)](https://www.theglobeandmail.com/investing/markets/stocks/CAG/pressreleases/3328132/jefferies-sticks-to-its-hold-rating-for-conagra-brands-cag/)
  - In a report released yesterday, Scott Marks CFA from Jefferies reiterated a Hold rating on Conagra Brands, with a price target of $14.00. TipRanks Welcomes a…
- [Analysts’ Opinions Are Mixed on These Consumer Goods Stocks: Costco (COST), JM Smucker (SJM) and Conagra Brands (CAG)](https://www.theglobeandmail.com/investing/markets/stocks/COST/pressreleases/2341924/analysts-opinions-are-mixed-on-these-consumer-goods-stocks-costco-cost-jm-smucker-sjm-and-conagra-brands-cag/)
  - Unlock trusted, data-backed investing tools with TipRanks Premium, from analyst ratings and forecasts to breaking news and portfolio analysis. Discover high-…
- [BofA Trims Conagra Brands, Inc. (CAG)'s Price Target To $13, Keeps Underperform Rating](https://www.insidermonkey.com/blog/bofa-trims-conagra-brands-inc-cags-price-target-to-13-keeps-underperform-rating-1772427/)
  - Conagra Brands, Inc. (NYSE:CAG) is among the 10 Most Oversold S&P 500 Stocks So Far in 2026. On May 28, BofA analyst Peter Galbo lowered the price target on …
- [Conagra Brands (CAG) Faces Mounting Challenges as Bernstein Cuts Rating and Price Target](https://finance.yahoo.com/markets/stocks/articles/conagra-brands-cag-faces-mounting-015938134.html)
  - The above button links to Coinbase. Yahoo Finance is not a broker-dealer or investment adviser and does not offer securities or cryptocurrencies for sale or …
- [Conagra Brands (CAG) Stock Forecast & Analyst Price Targets](https://stockanalysis.com/stocks/cag/forecast/)
  - Stock forecasts and analyst price target predictions for Conagra Brands, Inc. (CAG) stock, with detailed revenue and earnings estimates.
- [CAG | Conagra Brands Inc. Analyst Estimates & Ratings – WSJ](https://www.wsj.com/market-data/quotes/CAG/research-ratings)
  - Conagra Brands Inc. analyst ratings, historical stock prices, earnings estimates & actuals. CAG updated stock price target summary.
- [Conagra Brands, Inc.: Target Price Consensus and Analysts ...](https://m.marketscreener.com/quote/stock/CONAGRA-BRANDS-INC-11968/consensus/)
  - Conagra Brands, Inc. analysts consensus, targets, ratings and recommendations | NYSE: CAG | NYSE
- [CAG | Conagra Brands Inc. Analyst Estimates | MarketWatch](https://www.marketwatch.com/investing/stock/cag/analystestimates)
  - CAG Analyst Estimates. Snapshot. Average Recommendation.Current Year's Estimate. 1.70. Median PE on CY Estimate.

### Search warnings
- news:ConAgra Brands, Inc. stock rating OR consensus OR upgrade OR downgrade: No results found.
- news:CAG Estimate intrinsic value under base / bull / bear scenarios analyst: No results found.

## Web research — web_drivers

- Queries: CAG Estimate intrinsic value under base / bull / bear scenarios, ConAgra Brands, Inc. CAG outlook OR catalyst OR commodity OR uranium OR rare earth OR vanadium, CAG sector drivers OR market demand
- Unique hits: 16
- Pages fetched: 3/3

### Web synthesis — web_drivers (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, guidance, capex, revenue, margin, customer, segment, market

- (CAG) appears undervalued — DCF intrinsic value $26.23 vs market price $13.56 (93% upside).
- [HIT] CAG Stock Pops After Earnings Beat—October Could Be the Bottom | www.marketbeat.com | https://www.marketbeat.com/articles/conagra-brands-high-yield-and-deep-value-are-a-buy-in-october/ Rare Earth Minerals.Get Conagra Brands alerts: Sign Up.
- Conagra struggled with headwinds in FQ1 but was able to outperform its consensus expectation with revenue of $2.63 billion.
- | finance.yahoo.com | https://finance.yahoo.com/markets/stocks/articles/conagra-brands-cag-faces-cost-030510734.html Jun 21, 2026 ...
- Revenue growth can be broken down into changes in price and volume (the number of units sold).
- [HIT] CAG Group lifted revenue, but earnings fell - MarketScreener | www.marketscreener.com | https://www.marketscreener.com/news/cag-group-lifted-revenue-but-earnings-fell-ce7f5ed3d180f527 Jul 17, 2026 ...
- At the same time, he emphasizes that the market remains challenging in several areas and that demand varies across segments and customers.
- [HIT] Shelf-Stable Food Stocks Q4 Teardown: Conagra (NYSE:CAG) Vs The Rest | StockStory · via Yahoo Finance | https://finance.yahoo.com/markets/stocks/articles/shelf-stable-food-stocks-q4-224922338.html Shelf-Stable Food Stocks Q4 Teardown: Conagra (NYSE:CAG) Vs The Rest Wrapping up Q4 earnings, we...

### Sources found
- [Conagra Brands, Inc. (CAG) DCF Valuation — Intrinsic Value & Fair Value ...](https://vcpscanner.com/valuation/cag/dcf)
  - Conagra Brands, Inc. (CAG) appears undervalued — DCF intrinsic value $26.23 vs market price $13.56 (93% upside). Bear/base/bull scenarios, reverse DCF, and f…
- [Scenario Analysis — How to Model Bull, Base & Bear Cases - equityref.com](https://equityref.com/financial-modeling/scenario-analysis/)
  - Learn how to build scenario analysis in financial models — base, bull, and bear cases, CHOOSE function method, and probability-weighted valuation.
- [Bull Base Bear Valuation for One Stock | Model Reef](https://modelreef.io/resources/articles/stock-valuation/how-to-create-a-bull-base-bear-valuation-for-one-stock-scenario-driven-intrinsic-value)
  - Build a bull, base, and bear valuation for one stock with clear drivers, scenario ranges, implied multiples, and decision rules you can defend.
- [Free Intrinsic Value Calculator – DCF for US Stocks](https://vcpscanner.com/valuation)
  - Free US stock screener and valuation tool for 5,800+ stocks. Calculate intrinsic value with a DCF model, adjustable growth and discount rates, and Bear, Base…
- [Conagra Brands: A New Captain Sets A Leaner... | Seeking Alpha](https://seekingalpha.com/article/4925393-conagra-brands-a-new-captain-sets-a-leaner-simpler-course-and-im-on-board)
  - Conagra Brands, Inc. remains a Buy: new CEO strategy, valuation upside, and a dividend cut that strengthens the balance sheet. Click for this CAG update.
- [Q3 2026 Conagra Brands Inc Earnings Call Transcript](https://www.gurufocus.com/stock/HAM:CAO/transcripts/8765684)
  - Conagra Brands Inc (CAG) faces potential challenges from broad-based inflation, which could impact pricing strategies and profitability. The company has less…
- [CAG Stock Pops After Earnings Beat—October Could Be the Bottom](https://www.marketbeat.com/articles/conagra-brands-high-yield-and-deep-value-are-a-buy-in-october/)
  - Rare Earth Minerals.Get Conagra Brands alerts: Sign Up. CAG stock chart. Conagra Outperforms Expectations Despite Macroeconomic Headwinds. Conagra struggled …
- [Autozone Inc (AZO) vs Conagra Brands Inc (CAG): Price... | Pluang](https://pluang.com/en/compare/azo-vs-cag)
  - Compare Autozone Inc and Conagra Brands Inc side by side — live prices, performance, key stats, technicals, Aura AI signals and investor sentiment on Pluang.
- [Conagra Brands (CAG) Faces Cost Pressures and Weak Demand ...](https://finance.yahoo.com/markets/stocks/articles/conagra-brands-cag-faces-cost-030510734.html)
  - Jun 21, 2026 ... She noted that she was cutting estimates "again," largely due to rising cost inflation that continues to weigh on the sector. Conagra Brands…
- [Conagra Brands (CAG) - Trefis](https://www.trefis.com/data/companies/CAG)
  - Fundamental Drivers. The -3.7% change in CAG stock from 3/31/2026 to 7/25 ... Conagra Brands (CAG). By Industry; By Sector; All Other Sectors; Sector Best Be…
- [3 Reasons to Sell CAG and 1 Stock to Buy Instead - StockStory](https://stockstory.org/us/stocks/nyse/cag/news/buy-or-sell/3-reasons-to-sell-cag-and-1-stock-to-buy-instead-2)
  - Feb 9, 2026 ... Demand Slipping as Sales Volumes Decline. Revenue growth can be broken down into changes in price and volume (the number of units sold). Whil…
- [CAG Group lifted revenue, but earnings fell - MarketScreener](https://www.marketscreener.com/news/cag-group-lifted-revenue-but-earnings-fell-ce7f5ed3d180f527)
  - Jul 17, 2026 ... At the same time, he emphasizes that the market remains challenging in several areas and that demand varies across segments and customers. C…

### Search warnings
- news:CAG Estimate intrinsic value under base / bull / bear scenarios: No results found.
- news:ConAgra Brands, Inc. CAG outlook OR catalyst OR commodity OR uranium OR rare earth OR vanadium: No results found.

## SEC filing [S25]
- Extraction OK: True
- Item 1 chars: 28227
- Item 1A chars: 50000
- Item 7 chars: 50000
- Meta: {'source': 'cache', 'path': 'C:\\DevWork\\equity_research_agent\\data\\filings\\CAG_10k.txt'}

## Company setup & business model

**Keyword hits:** risk, litigation, regulation, competition, margin, supply chain, customer, segment, product, service, market, operations, network

- Narrative Description of Business  We compete throughout the food industry and focus on adding value for our customers who operate in the retail food and foodservice channels.
- Our operations, including our reporting segments, are described below.
- Our locations, including manufacturing facilities, within each reporting segment, are described in Item 2, Properties.
- Reporting Segments  Our reporting segments are as follows:  Grocery & Snacks  The Grocery & Snacks reporting segment principally includes branded, shelf-stable food products sold in various retail channels in the United States.
- Refrigerated & Frozen  The Refrigerated & Frozen reporting segment principally includes branded, temperature-controlled food products sold in various retail channels in the United States.
- International  The International reporting segment principally includes branded food products, in various temperature states, sold in various retail and foodservice channels outside of the United States.
- Foodservice  The Foodservice reporting segment includes branded and customized food products, including meals, entrees, sauces, and a variety of custom-manufactured culinary products packaged for sale to restaurants and other foodservice establishments primarily in the United States.
- General  The following discussion pertains to all of our reporting segments.
- Conagra Brands is a branded consumer packaged goods food company that operates in many sectors of the food industry, with a significant focus on the sale of branded, value-added consumer food products, as well as foodservice items and ingredients.
- Raw Materials and Packaging  We use many different raw materials, most of which are commodities, to make and package our products.
- The prices paid for raw materials used in making our food generally reflect factors such as global economic conditions, trade barriers or restrictions, supply and demand, weather, commodity market fluctuations, currency fluctuations, tariffs, and the effects of governmental agricultural programs, and may be impacted by supply chain disruptions including disruptions caused by weather, natural  disasters, geopolitical and military conflicts, and disease, in humans, plants, and animals.
- We seek to mitigate higher input costs through productivity and pricing initiatives and the use of derivative instruments to economically hedge a portion of forecasted future consumption.
- Competition  We experience intense competition for sales of our food items in our major markets.
- We compete primarily on the basis of quality, product innovation, value, convenience, customer service, brand recognition, and brand loyalty.
- For example, sales of frozen foods tend to be marginally higher during the winter months, pie sales are highest in November and December due to holidays, and production of certain of our products occurs seasonally, during or immediately following the purchase of agricultural crops.
- Some of our products are sold under licensing  arrangements with others, including our licensing arrangement with Dolly Parton and our licenses of the P.F.
- Government Regulation  The manufacture and sale of consumer food is highly regulated.
- Our operations, our products, and our practices are subject to various federal, state, local, and international laws and regulations and related regulatory oversight by various government agencies, including the United States Department of Agriculture, the Federal Food and Drug Administration, the Federal Trade Commission, the Consumer Product Safety Commission, the Occupational Safety and Health Administration, the Environmental  Protection Agency, the   Department of Labor, and various other federal, state, local, and international authorities (including government authorities in Canada and Mexico).
- In particular, the production, packaging, transportation, storage, distribution, advertising, labeling, quality, and safety of food products, the health and safety of our employees, and the protection of the environment are each subject to governmental regulation.
- Additionally, we are subject to data privacy and security regulations, anticorruption, anti-bribery, trade sanction and export, extended producer responsibility (such as regulations governing plastic or packaging taxes, recycling, and waste management programs), tax, and securities laws and regulations, accounting and reporting standards, and other financial laws and regulations.
- Werelyon our procedures, policies, andcomplianceprograms, aswellas legal advice fromin-houseandoutsidecounsel, to align our operations, products, and practiceswith applicable laws and regulations.
- We  believe that we are in compliance with such laws and regulations in all material respects and do not expect that continued compliance with such regulations will have a material effect upon capital expenditures, earnings, or our competitive position.
- Customers  Our products are sold, directly and through distributors, to chain, wholesale, value, cooperative, club, and independent grocery, pharmacy and drug, convenience and other store operators; and foodservice customers, including restaurants and bars, travel and leisure customers, schools, health care facilities, and government customers.
- Our products are also sold online through various e-commerce platforms and retailers.
- We leverage our six timeless values, which form the framework of our Company culture, to guide our approach to human capital management:    Integrity: Do the right things and do things right      External Focus: Center on the consumer, customer, competitor, and investor      Broad-Mindedness: Seek out and respect varied perspectives; embrace collaboration and assume positive intent      Agility: Convert insights into action with the speed of an entrepreneur      Leadership: Simplify, make decisions, inspire others, and act like an owner      Results: Leverage a “refuse-to-lose” obsession with impact and value creation    As of May 31, 2026, we had approximately 17,400 employees, primarily in the United States.
- We are focused on maintaining a strong culture of safety, in which all employees strive to protect themselves and their colleagues by being proactive towards risk identification and mitigation for people and our food products.
- Our health and safety team audits each of our facilities every 2-5 years, depending on risk profile, to review compliance with Conagra’s safety management system.
- This audit includes examination of leadership,  accountability, defect loss identification processes, inspections, training, safety regulation adherence and compliance with corporate policies.

_Source: latest 10-K Item 1 (Business), summarized locally._

## Qualitative analysis (local LLM)

### Item 1 — Business (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, litigation, regulation, competition, margin, supply chain, customer, segment, product, service, market, operations, network

- Narrative Description of Business  We compete throughout the food industry and focus on adding value for our customers who operate in the retail food and foodservice channels.
- Our operations, including our reporting segments, are described below.
- Our locations, including manufacturing facilities, within each reporting segment, are described in Item 2, Properties.
- Reporting Segments  Our reporting segments are as follows:  Grocery & Snacks  The Grocery & Snacks reporting segment principally includes branded, shelf-stable food products sold in various retail channels in the United States.
- Refrigerated & Frozen  The Refrigerated & Frozen reporting segment principally includes branded, temperature-controlled food products sold in various retail channels in the United States.
- International  The International reporting segment principally includes branded food products, in various temperature states, sold in various retail and foodservice channels outside of the United States.
- Foodservice  The Foodservice reporting segment includes branded and customized food products, including meals, entrees, sauces, and a variety of custom-manufactured culinary products packaged for sale to restaurants and other foodservice establishments primarily in the United States.
- General  The following discussion pertains to all of our reporting segments.
- Conagra Brands is a branded consumer packaged goods food company that operates in many sectors of the food industry, with a significant focus on the sale of branded, value-added consumer food products, as well as foodservice items and ingredients.
- Raw Materials and Packaging  We use many different raw materials, most of which are commodities, to make and package our products.
- The prices paid for raw materials used in making our food generally reflect factors such as global economic conditions, trade barriers or restrictions, supply and demand, weather, commodity market fluctuations, currency fluctuations, tariffs, and the effects of governmental agricultural programs, and may be impacted by supply chain disruptions including disruptions caused by weather, natural  disasters, geopolitical and military conflicts, and disease, in humans, plants, and animals.
- We seek to mitigate higher input costs through productivity and pricing initiatives and the use of derivative instruments to economically hedge a portion of forecasted future consumption.
- Competition  We experience intense competition for sales of our food items in our major markets.
- We compete primarily on the basis of quality, product innovation, value, convenience, customer service, brand recognition, and brand loyalty.
- For example, sales of frozen foods tend to be marginally higher during the winter months, pie sales are highest in November and December due to holidays, and production of certain of our products occurs seasonally, during or immediately following the purchase of agricultural crops.
- Some of our products are sold under licensing  arrangements with others, including our licensing arrangement with Dolly Parton and our licenses of the P.F.
- Government Regulation  The manufacture and sale of consumer food is highly regulated.
- Our operations, our products, and our practices are subject to various federal, state, local, and international laws and regulations and related regulatory oversight by various government agencies, including the United States Department of Agriculture, the Federal Food and Drug Administration, the Federal Trade Commission, the Consumer Product Safety Commission, the Occupational Safety and Health Administration, the Environmental  Protection Agency, the   Department of Labor, and various other federal, state, local, and international authorities (including government authorities in Canada and Mexico).
- In particular, the production, packaging, transportation, storage, distribution, advertising, labeling, quality, and safety of food products, the health and safety of our employees, and the protection of the environment are each subject to governmental regulation.
- Additionally, we are subject to data privacy and security regulations, anticorruption, anti-bribery, trade sanction and export, extended producer responsibility (such as regulations governing plastic or packaging taxes, recycling, and waste management programs), tax, and securities laws and regulations, accounting and reporting standards, and other financial laws and regulations.
- Werelyon our procedures, policies, andcomplianceprograms, aswellas legal advice fromin-houseandoutsidecounsel, to align our operations, products, and practiceswith applicable laws and regulations.
- We  believe that we are in compliance with such laws and regulations in all material respects and do not expect that continued compliance with such regulations will have a material effect upon capital expenditures, earnings, or our competitive position.
- Customers  Our products are sold, directly and through distributors, to chain, wholesale, value, cooperative, club, and independent grocery, pharmacy and drug, convenience and other store operators; and foodservice customers, including restaurants and bars, travel and leisure customers, schools, health care facilities, and government customers.
- Our products are also sold online through various e-commerce platforms and retailers.
- We leverage our six timeless values, which form the framework of our Company culture, to guide our approach to human capital management:    Integrity: Do the right things and do things right      External Focus: Center on the consumer, customer, competitor, and investor      Broad-Mindedness: Seek out and respect varied perspectives; embrace collaboration and assume positive intent      Agility: Convert insights into action with the speed of an entrepreneur      Leadership: Simplify, make decisions, inspire others, and act like an owner      Results: Leverage a “refuse-to-lose” obsession with impact and value creation    As of May 31, 2026, we had approximately 17,400 employees, primarily in the United States.
- We are focused on maintaining a strong culture of safety, in which all employees strive to protect themselves and their colleagues by being proactive towards risk identification and mitigation for people and our food products.
- Our health and safety team audits each of our facilities every 2-5 years, depending on risk profile, to review compliance with Conagra’s safety management system.
- This audit includes examination of leadership,  accountability, defect loss identification processes, inspections, training, safety regulation adherence and compliance with corporate policies.


### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin, supply chain, cyber, interest rate, customer, segment, product, service, market, operations, subsidiary

- Our business is subject to various risks and uncertainties.
- Any of the risks and uncertainties described below could materially adversely affect our business, financial condition, and results of operations and should be considered in evaluating us.
- Although the risks are organized by headings and each risk is described separately, many of the risks are interrelated.
- While we believe we have identified and discussed below the key risk factors affecting our business, there may be additional risks  and uncertainties that are not presently known or that are not currently believed to be significant that may adversely affect our business, performance, or financial condition in the future.
- Market Risks  Deterioration in general economic conditions, an economic recession or periods of slow growth, periods of inflation or increasing interest rates, or economic uncertainty may affect consumers resulting in reductions in consumer spending and have in the past harmed and could continue to harm our business and results of operations.
- Our business and results of operations have in the past been and may continue to be adversely affected by changes in national or global stability and economic conditions, including periods of inflation and rising interest rates; decreased energy and fuel availability coupled with increased oil, energy and fuel costs (including fuel surcharges); reduced consumer confidence and declining consumer spending rates; actual or threatened hostilities or war and/or other geopolitical conflicts; declining benefits or changing eligibility requirements under government food assistance programs for consumers; changing international trade, immigration, and tax policies; recessions and periods of slow growth, decreased availability of capital, volatility in financial markets; rising or sustained high unemployment; supply chain challenges; labor shortages; the effects of governmental initiatives to manage economic conditions; and the negative impacts caused by pandemics, epidemics, and disease, in  humans, plants, and animals.
- These economic factors could continue to impact our business and operations in a variety of ways, including as follows:    consumers seeking to reduce their spending on food by shifting purchases to more generic, lower-priced, or other value offerings, or foregoing certain purchases altogether during economic downt...
- volatility in commodity and other input costs could substantially impact our result of operations;      rising interest rates may adversely impact our results of operations;    ─────────────────────────────────────────────────────────────────────────    decreased demand in the restaurant business, particularly casual and fine dining, may adversely affect our Foodservice operations;    ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────    volatility in the equity markets or interest rates could substantially impact our pension costs and required pension contributions; and      it may become more costly or difficult to obtain debt or equity financing to fund operations or investment opportunities, or to refinance our debt in the future, in each case on terms and withi...


### Item 7 — MD&A (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, uncertainty, litigation, regulation, revenue, margin, supply chain, cyber, interest rate, customer, segment, product, service, market, operations

- AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERATIONS  The following discussion and analysis is intended to provide a summary of significant factors relevant to our financial performance and condition.
- Examples of forward-looking statements include statements regarding our expected future financial performance or position, results of operations, business strategy, plans and objectives of management for future operations, and other statements that are not historical facts.
- Forward-looking statements provide our current expectations and beliefs concerning future events and are subject to risks, uncertainties, and factors relating to our business and operations, all of which are difficult to predict and could cause our actual results to differ materially from the expectations expressed in or implied by such forward-looking statements.
- These  risks, uncertainties, and factors include: risks associated with general economic and industry conditions, including inflation, oil, energy and fuel costs, reduced consumer confidence and spending, increased tariffs and taxes, actual or threatened hostilities or war and/or other geopolitical conflicts, declining benefits or changing eligibility requirements under government food assistance programs for consumers, rising unemployment, recessions, supply chain challenges, labor cost increases or  shortages, interest rate and currency rate fluctuations; risks related to the availability and prices of commodities and other supply chain resources, including raw materials, packaging, energy, and transportation, weather conditions, pandemics, epidemics, and disease, in humans, plants, and animals; disruptions or inefficiencies in our supply chain and/or operations; risks related to the effectiveness of our hedging activities and ability to respond to volatility in commodities; risks related  to the ultimate impact of, including reputational harm caused by, any product recalls and product liability or labeling litigation; risks related to our ability to execute operating and value creation plans and achieve returns on our investments and targeted operating efficiencies from cost-saving initiatives, and to benefit from trade optimization programs; risks related to our ability to deleverage on currently anticipated timelines, and to continue to access capital on acceptable terms or at  all; risks related to the Company’s competitive environment, cost structure, and related market conditions; risks related to our ability to respond to changing consumer preferences, including health and wellness perceptions and the success of our innovation and marketing investments; risks associated with actions by our customers, including changes in distribution and purchasing terms; risks related to the seasonality of our business; risks associated with our contract manufacturing arrangements and other third-party service provider dependencies; risks associated with actions of governments and regulatory bodies that affect our businesses, including regulations or interpretations designed to address climate change; risks related to the Company’s ability to execute on its strategies or achieve expectations related to environmental, social, and governance matters, including as a result of evolving legal, regulatory, and other standards, processes, and assumptions, the pace of scientific  and technological developments, increased costs, the availability of requisite financing, and changes in carbon pricing or carbon taxes; risks related to a material failure in or breach of our or our vendors’ information technology systems and other cybersecurity incidents; risks related to our ability to identify, attract, hire, train, retain and develop qualified personnel; risk of increased pension, labor or people-related expenses; risks and uncertainties associated with intangible assets,  including any future goodwill or intangible assets impairment charges; risks relating to our ability to protect our intellectual property rights; risks relating to acquisition,   divestiture, joint venture or investment activities; the amount and timing of future dividends, which remain subject to Board approval and depend on market and other conditions; the amount and timing of future stock repurchases; and other risks described in our reports filed from time to time with the U.S.
- Trends Impacting our Business  We continue to expect our industry to be impacted by weak consumer sentiment, inflation, commodity cost fluctuations, supply chain pressures, trade and regulatory uncertainty, and other global macroeconomic challenges.
- tariffs and reciprocal tariffs caused increased uncertainty as well as input cost inflation in key  materials used in our products, including tin-plate steel used in packaging for our canned products, which we were able to partially offset with productivity initiatives and price increases on impacted products.
- We will continue to evaluate the evolving macroeconomic environment to take action to mitigate the impact on our business, consolidated results of operations, and financial condition.
- While we will continue to seek to offset input cost inflation with productivity initiatives and tariff mitigation efforts, we anticipate that we may need to increase prices on certain products in fiscal 2027 to mitigate margin impacts and would expect corresponding elasticity impacts.


## Research loop (think → act)

1. _heuristic_ — Coverage looks adequate for this pass; stopping iterative loop.

## Sources

- **[S1]** CAG fundamentals (yfinance)
  - ConAgra Brands, Inc.: price=15.24, rev=11281600000.0, fcf=978700000.0, shares=475029042.0, rev_cagr=-0.027791350655803293, ROIC=-0.10697344868735084, FCF yield=None
- **[S2]** CAG DCF valuation (dcf)
  - Base share price=17.78553979162984, bull=63.71028020338544, bear=-2.0395215193000564
- **[S3]** CAG EV/EBITDA valuation (multiples)
  - Base implied price=1.9990356715916329, multiple=8.0
- **[S4]** Conagra Brands (CAG) Stock Forecast and Price Target 2026 (web) — https://www.marketbeat.com/stocks/NYSE/CAG/forecast/
  - CAG's current price target is $15.00. Learn why top analysts are making this stock forecast for Conagra Brands at MarketBeat.According to the 18 analysts' twelve-month price tar…
- **[S5]** Conagra Brands Analyst Ratings and Price Targets | NYSE:CAG (web) — https://www.benzinga.com/quote/CAG/analyst-ratings
  - The latest price target for Conagra Brands (NYSE:CAG) was reported by UBS on July 16, 2026. The analyst firm set a price target for $14.00 expecting CAG to fall to within 12 mon…
- **[S6]** Conagra Brands (CAG) Stock Forecast, Price Targets and Analysts... (web) — https://www.tipranks.com/stocks/cag/forecast
  - Analyze Forecast. Average Price Target.The average price target for Conagra Brands is 13.73. This is based on 11 Wall Streets Analysts 12-month price targets, issued in the past…
- **[S7]** CAG Forecast — Price Target — Prediction for 2027 — TradingView (web) — https://www.tradingview.com/symbols/NYSE-CAG/forecast/
  - According to analysts, CAG price target is 15.20 USD with a max estimate of 18.00 USD and a min estimate of 13.00 USD. Check if this forecast comes true in a year, meanwhile wat…
- **[S8]** Jefferies Sticks to Its Hold Rating for Conagra Brands (CAG) (web) — https://www.theglobeandmail.com/investing/markets/stocks/CAG/pressreleases/3328132/jefferies-sticks-to-its-hold-rating-for-conagra-brands-cag/
  - In a report released yesterday, Scott Marks CFA from Jefferies reiterated a Hold rating on Conagra Brands, with a price target of $14.00. TipRanks Welcomes a New ETF – NYSE:RANK…
- **[S9]** Analysts’ Opinions Are Mixed on These Consumer Goods Stocks: Costco (COST), JM Smucker (SJM) and Conagra Brands (CAG) (web) — https://www.theglobeandmail.com/investing/markets/stocks/COST/pressreleases/2341924/analysts-opinions-are-mixed-on-these-consumer-goods-stocks-costco-cost-jm-smucker-sjm-and-conagra-brands-cag/
  - Unlock trusted, data-backed investing tools with TipRanks Premium, from analyst ratings and forecasts to breaking news and portfolio analysis. Discover high-conviction stock pic…
- **[S10]** BofA Trims Conagra Brands, Inc. (CAG)'s Price Target To $13, Keeps Underperform Rating (web) — https://www.insidermonkey.com/blog/bofa-trims-conagra-brands-inc-cags-price-target-to-13-keeps-underperform-rating-1772427/
  - Conagra Brands, Inc. (NYSE:CAG) is among the 10 Most Oversold S&P 500 Stocks So Far in 2026. On May 28, BofA analyst Peter Galbo lowered the price target on the stock to $13 fro…
- **[S11]** Conagra Brands (CAG) Faces Mounting Challenges as Bernstein Cuts Rating and Price Target (web) — https://finance.yahoo.com/markets/stocks/articles/conagra-brands-cag-faces-mounting-015938134.html
  - The above button links to Coinbase. Yahoo Finance is not a broker-dealer or investment adviser and does not offer securities or cryptocurrencies for sale or facilitate trading. …
- **[S12]** Conagra Brands (CAG) Stock Forecast and Price Target 2026 (web_page) — https://www.marketbeat.com/stocks/NYSE/CAG/forecast/
  - Conagra Brands (CAG) Stock Forecast and Price Target 2026 Skip to main content → The dollar reset no one told you about (From Porter & Company) (Ad) Free CAG Stock Alerts Conagr…
- **[S13]** Conagra Brands Analyst Ratings and Price Targets | NYSE:CAG | Benzinga (web_page) — https://www.benzinga.com/quote/CAG/analyst-ratings
  - Conagra Brands Analyst Ratings and Price Targets | NYSE:CAG | Benzinga Benzinga España Italia 대한민국 日本 Français My Account Login SPY 738.87 0.03% QQQ 681.24 0.13% BTC/USD 63491.0…
- **[S14]** Conagra Brands, Inc. (CAG) DCF Valuation — Intrinsic Value & Fair Value ... (web) — https://vcpscanner.com/valuation/cag/dcf
  - Conagra Brands, Inc. (CAG) appears undervalued — DCF intrinsic value $26.23 vs market price $13.56 (93% upside). Bear/base/bull scenarios, reverse DCF, and full assumptions. Upd…
- **[S15]** Scenario Analysis — How to Model Bull, Base & Bear Cases - equityref.com (web) — https://equityref.com/financial-modeling/scenario-analysis/
  - Learn how to build scenario analysis in financial models — base, bull, and bear cases, CHOOSE function method, and probability-weighted valuation.
- **[S16]** Bull Base Bear Valuation for One Stock | Model Reef (web) — https://modelreef.io/resources/articles/stock-valuation/how-to-create-a-bull-base-bear-valuation-for-one-stock-scenario-driven-intrinsic-value
  - Build a bull, base, and bear valuation for one stock with clear drivers, scenario ranges, implied multiples, and decision rules you can defend.
- **[S17]** Free Intrinsic Value Calculator – DCF for US Stocks (web) — https://vcpscanner.com/valuation
  - Free US stock screener and valuation tool for 5,800+ stocks. Calculate intrinsic value with a DCF model, adjustable growth and discount rates, and Bear, Base, and Bull scenarios.
- **[S18]** Conagra Brands: A New Captain Sets A Leaner... | Seeking Alpha (web) — https://seekingalpha.com/article/4925393-conagra-brands-a-new-captain-sets-a-leaner-simpler-course-and-im-on-board
  - Conagra Brands, Inc. remains a Buy: new CEO strategy, valuation upside, and a dividend cut that strengthens the balance sheet. Click for this CAG update.
- **[S19]** Q3 2026 Conagra Brands Inc Earnings Call Transcript (web) — https://www.gurufocus.com/stock/HAM:CAO/transcripts/8765684
  - Conagra Brands Inc (CAG) faces potential challenges from broad-based inflation, which could impact pricing strategies and profitability. The company has less coverage on diesel …
- **[S20]** CAG Stock Pops After Earnings Beat—October Could Be the Bottom (web) — https://www.marketbeat.com/articles/conagra-brands-high-yield-and-deep-value-are-a-buy-in-october/
  - Rare Earth Minerals.Get Conagra Brands alerts: Sign Up. CAG stock chart. Conagra Outperforms Expectations Despite Macroeconomic Headwinds. Conagra struggled with headwinds in FQ…
- **[S21]** Autozone Inc (AZO) vs Conagra Brands Inc (CAG): Price... | Pluang (web) — https://pluang.com/en/compare/azo-vs-cag
  - Compare Autozone Inc and Conagra Brands Inc side by side — live prices, performance, key stats, technicals, Aura AI signals and investor sentiment on Pluang.
- **[S22]** Conagra Brands, Inc. (CAG) Intrinsic Value & DCF Model 2026 | VCP Scanner (web_page) — https://vcpscanner.com/valuation/cag/dcf
  - Conagra Brands, Inc. (CAG) Intrinsic Value & DCF Model 2026 | VCP Scanner Conagra Brands, Inc. ( CAG ) DCF Valuation • Discounted Cash Flow intrinsic value with Bear, Base & Bul…
- **[S23]** Scenario Analysis — How to Model Bull, Base & Bear Cases - equityref.com (web_page) — https://equityref.com/financial-modeling/scenario-analysis/
  - Scenario Analysis — How to Model Bull, Base & Bear Cases - equityref.com Scenario Analysis — How to Model Bull, Base & Bear Cases Scenario Analysis Scenario analysis tests how c…
- **[S24]** Bull Base Bear Valuation for One Stock | Model Reef (web_page) — https://modelreef.io/resources/articles/stock-valuation/how-to-create-a-bull-base-bear-valuation-for-one-stock-scenario-driven-intrinsic-value
  - Bull Base Bear Valuation for One Stock | Model Reef Back Published February 13, 2026 in For Teams Table of Contents Bull/Base/Bear Valuation Before You Begin Step-by-Step Implem…
- **[S25]** CAG 10-K (sec)
  - Item 1 chars=28227, Item 1A chars=50000, Item 7 chars=50000, ok=True, source=cache
- **[S26]** Item 1 Business summary (nlp)
  - ### Item 1 — Business (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, litigation, regulation, competition, margin, supply chain, customer, segment, product, s…
- **[S27]** Item 1A summary (nlp)
  - ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin, supply chain, cy…
- **[S28]** Item 7 summary (nlp)
  - ### Item 7 — MD&A (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, revenue, margin, supply chain, cyber, interest rate, cu…
- **[S29]** CAG scenario price ranges (scenarios)
  - ok=True; base mid=2.6726786948744072; headwinds=6; tailwinds=8

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

# CAG — Planned Research Report

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
- Company: ConAgra Brands, Inc.
- Sector / industry: Consumer Defensive / Packaged Foods
- Price: 15.24
- 52-week range: $12.53 – $20.32
- Market cap: —
- Enterprise value: $14.55B
- Shares outstanding: 475.03M
- Beta: -0.047
- Book equity: $6.36B
- Revenue (latest): $11.28B
- EBITDA (latest): -$1.04B
- Free cash flow (latest): $978.70M
- Operating income: $1.26B
- Operating margin: 11.2%
- EV / EBITDA: -14.0x
- ROIC: -10.7%
- FCF yield: —
- Debt / Equity: 1.1432616081540203
- FCF / share: $2.06
- Revenue / share: $23.75

### Capital structure
- Cash: $218.00M
- Short-term debt: $812.40M
- Long-term debt: $6.46B
- Total debt: $7.27B
- Net debt: $7.05B
- Net debt / EBITDA: -6.8x

### Growth
- Revenue CAGR: -2.8%
- FCF CAGR: 15.6%
- Latest revenue YoY: -2.9%
- Latest FCF YoY: -24.9%

### Market expectations (yfinance, sparse)
- Mean target: $14.38
- Target range: $12.00 – $23.00
- Recommendation: hold

_Consensus revenue/EBITDA forecasts are often unavailable via free feeds; treat targets as point-in-time only._

### Historical KPIs (multi-year)

| Year | Revenue | OCF | Capex | FCF | EBITDA | LT debt | Cash | Net debt | Net income |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2026 | $11.28B | $1.40B | $423.40M | $978.70M | -$1.04B | $6.46B | $218.00M | $6.24B | -$1.92B |
| 2025 | $11.61B | $1.69B | $389.30M | $1.30B | $1.97B | $6.23B | $68.00M | $6.17B | $1.15B |
| 2024 | $12.05B | $2.02B | $388.10M | $1.63B | $1.45B | $7.49B | $77.70M | $7.41B | $347.20M |
| 2023 | $12.28B | $995.40M | $362.20M | $633.20M | $1.69B | $7.08B | $93.30M | $6.99B | $683.60M |

## Charts

### Revenue & FCF history
![Revenue & FCF history](/charts/CAG_deep_revenue_fcf.png)

### DCF scenario prices
![DCF scenario prices](/charts/CAG_deep_dcf_scenarios.png)

### Base-case FCF path
![Base-case FCF path](/charts/CAG_deep_base_fcf_path.png)

## DCF valuation (base / bull / bear) [S2]

> Simplified revenue->FCF DCF. Not investment advice; assumptions are editable heuristics.

- Spot price: $15.24
- Base revenue: $11.28B
- Shares: 475,029,042
- Net debt (Debt−Cash): $7.05B

| Scenario | Growth | FCF margin | WACC | Term. g | Equity value | Share price | Upside |
|----------|--------|------------|------|---------|--------------|-------------|--------|
| bear | -2.9% | 6.7% | 12.0% | 1.5% | -$968.83M | $-2.04 | -113.4% |
| base | 6.0% | 8.7% | 10.0% | 2.5% | $8.45B | $17.79 | 16.7% |
| bull | 15.0% | 11.7% | 9.0% | 3.0% | $30.26B | $63.71 | 318.0% |

### Assumption notes
- Base revenue growth seeded from historical rate (-2.9%).
- Recent revenue declined (-2.9% YoY); base/bull use normalized mid-cycle growth instead of extrapolating the decline.

- _bear: model equity value is negative after net debt (-968,831,953); showing $-2.04/sh._

### Base-case projected FCF

- Year 1: revenue $11.96B, FCF $1.04B (PV $943.11M)
- Year 2: revenue $12.68B, FCF $1.10B (PV $908.82M)
- Year 3: revenue $13.44B, FCF $1.17B (PV $875.77M)
- Year 4: revenue $14.24B, FCF $1.24B (PV $843.92M)
- Year 5: revenue $15.10B, FCF $1.31B (PV $813.23M)
- Terminal value $17.90B (PV $11.11B)

## Web research — web_research

- Queries: Deep diligence: fundamentals, DCF, web, 10-K risks & MD&A
- Unique hits: 4
- Pages fetched: 3/3

### Web synthesis — web_research (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, litigation, revenue, margin, customer, product, service, market, network

- Connects to live market data via MCP servers to deliver company deep dives, due diligence reports, competitive landscape analysis, market sentiment, and DCF-based intrinsic value estimates — all from natural language prompts.
- [HIT] Deep Due Diligence Investors | | duediligenceclub.com | https://duediligenceclub.com/ A comprehensive online course offering due diligence training, equipping investors with essential skills to evaluate deals, mitigate risks, and make informed investment decisions.
- [HIT] Six skills for financial service professionals | Claude by Anthropic | claude.com | https://claude.com/resources/tutorials/claude-for-financial-services-skills Introduction to six specialized AI skills for financial professionals including valuation modeling, competitive analysis, research reports, and due diligence.
- You've been through preliminary Q&A sessions, shared high-level metrics, and convinced them on market and team.
- But now they want to see everything: your code architecture, financial models, legal structure, intellectual property, customer contracts, and every assumption that powers your business.
- Three diligence domains and their focus areas Technical diligence examines your product's foundation, scalability, and development practices.
- Financial diligence goes beyond basic metrics to examine unit economics modeling, cash flow forecasting, customer cohort analysis  [PAGE] GitHub - Lunatic16/deep-financial-research: A Claude/Qwen/Gemini skill for institutional-grade investment research.
- Connects to live market data via MCP servers to deliver company deep dives, due diligence reports, competitive landscape analysis, market sentiment, and DCF-based intrinsic value estimates — all from natural language prompts.

### Sources found
- [Deep Diligence Checklist for Startup Founders | Flux Capital Academy ...](https://www.fluxcapital.com/academy/boards-and-diligence/boards-and-diligence-deep-diligence-technical-financial-and-legal)
  - Deep diligence checklist for technical, financial, and legal review: prepare data rooms, models, IP, contracts, and investor Q&A for Series A.
- [GitHub - Lunatic16/deep-financial-research: A Claude/Qwen/Gemini skill ...](https://github.com/Lunatic16/deep-financial-research)
  - A Claude/Qwen/Gemini skill for institutional-grade investment research. Connects to live market data via MCP servers to deliver company deep dives, due dilig…
- [Deep Due Diligence Investors |](https://duediligenceclub.com/)
  - A comprehensive online course offering due diligence training, equipping investors with essential skills to evaluate deals, mitigate risks, and make informed…
- [Six skills for financial service professionals | Claude by Anthropic](https://claude.com/resources/tutorials/claude-for-financial-services-skills)
  - Introduction to six specialized AI skills for financial professionals including valuation modeling, competitive analysis, research reports, and due diligence.

### Search warnings
- news:Deep diligence: fundamentals, DCF, web, 10-K risks & MD&A: No results found.

## Put opportunities (heuristic) [S3]
- Expiration: 2026-08-28 (DTE 31)
- Candidates: 0
- ATM IV (est.): 3.9%
- IV rank: — (1 local samples)
- HV rank (20d realized): 96.1%


_Note: Delta band approximated via % OTM when greeks are unavailable; IV rank needs ~20+ local daily IV samples (have 1); run the options screen over time to build history.; HV rank is realized-vol rank (20d HV vs ~1y); useful when IV history is thin._

## SEC filing [S11]
- Extraction OK: True
- Item 1 chars: 28227
- Item 1A chars: 50000
- Item 7 chars: 50000
- Meta: {'source': 'cache', 'path': 'C:\\DevWork\\equity_research_agent\\data\\filings\\CAG_10k.txt'}

## Company setup & business model

**Keyword hits:** risk, litigation, regulation, competition, margin, supply chain, customer, segment, product, service, market, operations, network

- Narrative Description of Business  We compete throughout the food industry and focus on adding value for our customers who operate in the retail food and foodservice channels.
- Our operations, including our reporting segments, are described below.
- Our locations, including manufacturing facilities, within each reporting segment, are described in Item 2, Properties.
- Reporting Segments  Our reporting segments are as follows:  Grocery & Snacks  The Grocery & Snacks reporting segment principally includes branded, shelf-stable food products sold in various retail channels in the United States.
- Refrigerated & Frozen  The Refrigerated & Frozen reporting segment principally includes branded, temperature-controlled food products sold in various retail channels in the United States.
- International  The International reporting segment principally includes branded food products, in various temperature states, sold in various retail and foodservice channels outside of the United States.
- Foodservice  The Foodservice reporting segment includes branded and customized food products, including meals, entrees, sauces, and a variety of custom-manufactured culinary products packaged for sale to restaurants and other foodservice establishments primarily in the United States.
- General  The following discussion pertains to all of our reporting segments.
- Conagra Brands is a branded consumer packaged goods food company that operates in many sectors of the food industry, with a significant focus on the sale of branded, value-added consumer food products, as well as foodservice items and ingredients.
- Raw Materials and Packaging  We use many different raw materials, most of which are commodities, to make and package our products.
- The prices paid for raw materials used in making our food generally reflect factors such as global economic conditions, trade barriers or restrictions, supply and demand, weather, commodity market fluctuations, currency fluctuations, tariffs, and the effects of governmental agricultural programs, and may be impacted by supply chain disruptions including disruptions caused by weather, natural  disasters, geopolitical and military conflicts, and disease, in humans, plants, and animals.
- We seek to mitigate higher input costs through productivity and pricing initiatives and the use of derivative instruments to economically hedge a portion of forecasted future consumption.
- Competition  We experience intense competition for sales of our food items in our major markets.
- We compete primarily on the basis of quality, product innovation, value, convenience, customer service, brand recognition, and brand loyalty.
- For example, sales of frozen foods tend to be marginally higher during the winter months, pie sales are highest in November and December due to holidays, and production of certain of our products occurs seasonally, during or immediately following the purchase of agricultural crops.
- Some of our products are sold under licensing  arrangements with others, including our licensing arrangement with Dolly Parton and our licenses of the P.F.
- Government Regulation  The manufacture and sale of consumer food is highly regulated.
- Our operations, our products, and our practices are subject to various federal, state, local, and international laws and regulations and related regulatory oversight by various government agencies, including the United States Department of Agriculture, the Federal Food and Drug Administration, the Federal Trade Commission, the Consumer Product Safety Commission, the Occupational Safety and Health Administration, the Environmental  Protection Agency, the   Department of Labor, and various other federal, state, local, and international authorities (including government authorities in Canada and Mexico).
- In particular, the production, packaging, transportation, storage, distribution, advertising, labeling, quality, and safety of food products, the health and safety of our employees, and the protection of the environment are each subject to governmental regulation.
- Additionally, we are subject to data privacy and security regulations, anticorruption, anti-bribery, trade sanction and export, extended producer responsibility (such as regulations governing plastic or packaging taxes, recycling, and waste management programs), tax, and securities laws and regulations, accounting and reporting standards, and other financial laws and regulations.
- Werelyon our procedures, policies, andcomplianceprograms, aswellas legal advice fromin-houseandoutsidecounsel, to align our operations, products, and practiceswith applicable laws and regulations.
- We  believe that we are in compliance with such laws and regulations in all material respects and do not expect that continued compliance with such regulations will have a material effect upon capital expenditures, earnings, or our competitive position.
- Customers  Our products are sold, directly and through distributors, to chain, wholesale, value, cooperative, club, and independent grocery, pharmacy and drug, convenience and other store operators; and foodservice customers, including restaurants and bars, travel and leisure customers, schools, health care facilities, and government customers.
- Our products are also sold online through various e-commerce platforms and retailers.
- We leverage our six timeless values, which form the framework of our Company culture, to guide our approach to human capital management:    Integrity: Do the right things and do things right      External Focus: Center on the consumer, customer, competitor, and investor      Broad-Mindedness: Seek out and respect varied perspectives; embrace collaboration and assume positive intent      Agility: Convert insights into action with the speed of an entrepreneur      Leadership: Simplify, make decisions, inspire others, and act like an owner      Results: Leverage a “refuse-to-lose” obsession with impact and value creation    As of May 31, 2026, we had approximately 17,400 employees, primarily in the United States.
- We are focused on maintaining a strong culture of safety, in which all employees strive to protect themselves and their colleagues by being proactive towards risk identification and mitigation for people and our food products.
- Our health and safety team audits each of our facilities every 2-5 years, depending on risk profile, to review compliance with Conagra’s safety management system.
- This audit includes examination of leadership,  accountability, defect loss identification processes, inspections, training, safety regulation adherence and compliance with corporate policies.

_Source: latest 10-K Item 1 (Business), summarized locally._

## Qualitative analysis (local LLM)

### Item 1 — Business (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, litigation, regulation, competition, margin, supply chain, customer, segment, product, service, market, operations, network

- Narrative Description of Business  We compete throughout the food industry and focus on adding value for our customers who operate in the retail food and foodservice channels.
- Our operations, including our reporting segments, are described below.
- Our locations, including manufacturing facilities, within each reporting segment, are described in Item 2, Properties.
- Reporting Segments  Our reporting segments are as follows:  Grocery & Snacks  The Grocery & Snacks reporting segment principally includes branded, shelf-stable food products sold in various retail channels in the United States.
- Refrigerated & Frozen  The Refrigerated & Frozen reporting segment principally includes branded, temperature-controlled food products sold in various retail channels in the United States.
- International  The International reporting segment principally includes branded food products, in various temperature states, sold in various retail and foodservice channels outside of the United States.
- Foodservice  The Foodservice reporting segment includes branded and customized food products, including meals, entrees, sauces, and a variety of custom-manufactured culinary products packaged for sale to restaurants and other foodservice establishments primarily in the United States.
- General  The following discussion pertains to all of our reporting segments.
- Conagra Brands is a branded consumer packaged goods food company that operates in many sectors of the food industry, with a significant focus on the sale of branded, value-added consumer food products, as well as foodservice items and ingredients.
- Raw Materials and Packaging  We use many different raw materials, most of which are commodities, to make and package our products.
- The prices paid for raw materials used in making our food generally reflect factors such as global economic conditions, trade barriers or restrictions, supply and demand, weather, commodity market fluctuations, currency fluctuations, tariffs, and the effects of governmental agricultural programs, and may be impacted by supply chain disruptions including disruptions caused by weather, natural  disasters, geopolitical and military conflicts, and disease, in humans, plants, and animals.
- We seek to mitigate higher input costs through productivity and pricing initiatives and the use of derivative instruments to economically hedge a portion of forecasted future consumption.
- Competition  We experience intense competition for sales of our food items in our major markets.
- We compete primarily on the basis of quality, product innovation, value, convenience, customer service, brand recognition, and brand loyalty.
- For example, sales of frozen foods tend to be marginally higher during the winter months, pie sales are highest in November and December due to holidays, and production of certain of our products occurs seasonally, during or immediately following the purchase of agricultural crops.
- Some of our products are sold under licensing  arrangements with others, including our licensing arrangement with Dolly Parton and our licenses of the P.F.
- Government Regulation  The manufacture and sale of consumer food is highly regulated.
- Our operations, our products, and our practices are subject to various federal, state, local, and international laws and regulations and related regulatory oversight by various government agencies, including the United States Department of Agriculture, the Federal Food and Drug Administration, the Federal Trade Commission, the Consumer Product Safety Commission, the Occupational Safety and Health Administration, the Environmental  Protection Agency, the   Department of Labor, and various other federal, state, local, and international authorities (including government authorities in Canada and Mexico).
- In particular, the production, packaging, transportation, storage, distribution, advertising, labeling, quality, and safety of food products, the health and safety of our employees, and the protection of the environment are each subject to governmental regulation.
- Additionally, we are subject to data privacy and security regulations, anticorruption, anti-bribery, trade sanction and export, extended producer responsibility (such as regulations governing plastic or packaging taxes, recycling, and waste management programs), tax, and securities laws and regulations, accounting and reporting standards, and other financial laws and regulations.
- Werelyon our procedures, policies, andcomplianceprograms, aswellas legal advice fromin-houseandoutsidecounsel, to align our operations, products, and practiceswith applicable laws and regulations.
- We  believe that we are in compliance with such laws and regulations in all material respects and do not expect that continued compliance with such regulations will have a material effect upon capital expenditures, earnings, or our competitive position.
- Customers  Our products are sold, directly and through distributors, to chain, wholesale, value, cooperative, club, and independent grocery, pharmacy and drug, convenience and other store operators; and foodservice customers, including restaurants and bars, travel and leisure customers, schools, health care facilities, and government customers.
- Our products are also sold online through various e-commerce platforms and retailers.
- We leverage our six timeless values, which form the framework of our Company culture, to guide our approach to human capital management:    Integrity: Do the right things and do things right      External Focus: Center on the consumer, customer, competitor, and investor      Broad-Mindedness: Seek out and respect varied perspectives; embrace collaboration and assume positive intent      Agility: Convert insights into action with the speed of an entrepreneur      Leadership: Simplify, make decisions, inspire others, and act like an owner      Results: Leverage a “refuse-to-lose” obsession with impact and value creation    As of May 31, 2026, we had approximately 17,400 employees, primarily in the United States.
- We are focused on maintaining a strong culture of safety, in which all employees strive to protect themselves and their colleagues by being proactive towards risk identification and mitigation for people and our food products.
- Our health and safety team audits each of our facilities every 2-5 years, depending on risk profile, to review compliance with Conagra’s safety management system.
- This audit includes examination of leadership,  accountability, defect loss identification processes, inspections, training, safety regulation adherence and compliance with corporate policies.


### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin, supply chain, cyber, interest rate, customer, segment, product, service, market, operations, subsidiary

- Our business is subject to various risks and uncertainties.
- Any of the risks and uncertainties described below could materially adversely affect our business, financial condition, and results of operations and should be considered in evaluating us.
- Although the risks are organized by headings and each risk is described separately, many of the risks are interrelated.
- While we believe we have identified and discussed below the key risk factors affecting our business, there may be additional risks  and uncertainties that are not presently known or that are not currently believed to be significant that may adversely affect our business, performance, or financial condition in the future.
- Market Risks  Deterioration in general economic conditions, an economic recession or periods of slow growth, periods of inflation or increasing interest rates, or economic uncertainty may affect consumers resulting in reductions in consumer spending and have in the past harmed and could continue to harm our business and results of operations.
- Our business and results of operations have in the past been and may continue to be adversely affected by changes in national or global stability and economic conditions, including periods of inflation and rising interest rates; decreased energy and fuel availability coupled with increased oil, energy and fuel costs (including fuel surcharges); reduced consumer confidence and declining consumer spending rates; actual or threatened hostilities or war and/or other geopolitical conflicts; declining benefits or changing eligibility requirements under government food assistance programs for consumers; changing international trade, immigration, and tax policies; recessions and periods of slow growth, decreased availability of capital, volatility in financial markets; rising or sustained high unemployment; supply chain challenges; labor shortages; the effects of governmental initiatives to manage economic conditions; and the negative impacts caused by pandemics, epidemics, and disease, in  humans, plants, and animals.
- These economic factors could continue to impact our business and operations in a variety of ways, including as follows:    consumers seeking to reduce their spending on food by shifting purchases to more generic, lower-priced, or other value offerings, or foregoing certain purchases altogether during economic downt...
- volatility in commodity and other input costs could substantially impact our result of operations;      rising interest rates may adversely impact our results of operations;    ─────────────────────────────────────────────────────────────────────────    decreased demand in the restaurant business, particularly casual and fine dining, may adversely affect our Foodservice operations;    ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────    volatility in the equity markets or interest rates could substantially impact our pension costs and required pension contributions; and      it may become more costly or difficult to obtain debt or equity financing to fund operations or investment opportunities, or to refinance our debt in the future, in each case on terms and withi...


### Item 7 — MD&A (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, uncertainty, litigation, regulation, revenue, margin, supply chain, cyber, interest rate, customer, segment, product, service, market, operations

- AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERATIONS  The following discussion and analysis is intended to provide a summary of significant factors relevant to our financial performance and condition.
- Examples of forward-looking statements include statements regarding our expected future financial performance or position, results of operations, business strategy, plans and objectives of management for future operations, and other statements that are not historical facts.
- Forward-looking statements provide our current expectations and beliefs concerning future events and are subject to risks, uncertainties, and factors relating to our business and operations, all of which are difficult to predict and could cause our actual results to differ materially from the expectations expressed in or implied by such forward-looking statements.
- These  risks, uncertainties, and factors include: risks associated with general economic and industry conditions, including inflation, oil, energy and fuel costs, reduced consumer confidence and spending, increased tariffs and taxes, actual or threatened hostilities or war and/or other geopolitical conflicts, declining benefits or changing eligibility requirements under government food assistance programs for consumers, rising unemployment, recessions, supply chain challenges, labor cost increases or  shortages, interest rate and currency rate fluctuations; risks related to the availability and prices of commodities and other supply chain resources, including raw materials, packaging, energy, and transportation, weather conditions, pandemics, epidemics, and disease, in humans, plants, and animals; disruptions or inefficiencies in our supply chain and/or operations; risks related to the effectiveness of our hedging activities and ability to respond to volatility in commodities; risks related  to the ultimate impact of, including reputational harm caused by, any product recalls and product liability or labeling litigation; risks related to our ability to execute operating and value creation plans and achieve returns on our investments and targeted operating efficiencies from cost-saving initiatives, and to benefit from trade optimization programs; risks related to our ability to deleverage on currently anticipated timelines, and to continue to access capital on acceptable terms or at  all; risks related to the Company’s competitive environment, cost structure, and related market conditions; risks related to our ability to respond to changing consumer preferences, including health and wellness perceptions and the success of our innovation and marketing investments; risks associated with actions by our customers, including changes in distribution and purchasing terms; risks related to the seasonality of our business; risks associated with our contract manufacturing arrangements and other third-party service provider dependencies; risks associated with actions of governments and regulatory bodies that affect our businesses, including regulations or interpretations designed to address climate change; risks related to the Company’s ability to execute on its strategies or achieve expectations related to environmental, social, and governance matters, including as a result of evolving legal, regulatory, and other standards, processes, and assumptions, the pace of scientific  and technological developments, increased costs, the availability of requisite financing, and changes in carbon pricing or carbon taxes; risks related to a material failure in or breach of our or our vendors’ information technology systems and other cybersecurity incidents; risks related to our ability to identify, attract, hire, train, retain and develop qualified personnel; risk of increased pension, labor or people-related expenses; risks and uncertainties associated with intangible assets,  including any future goodwill or intangible assets impairment charges; risks relating to our ability to protect our intellectual property rights; risks relating to acquisition,   divestiture, joint venture or investment activities; the amount and timing of future dividends, which remain subject to Board approval and depend on market and other conditions; the amount and timing of future stock repurchases; and other risks described in our reports filed from time to time with the U.S.
- Trends Impacting our Business  We continue to expect our industry to be impacted by weak consumer sentiment, inflation, commodity cost fluctuations, supply chain pressures, trade and regulatory uncertainty, and other global macroeconomic challenges.
- tariffs and reciprocal tariffs caused increased uncertainty as well as input cost inflation in key  materials used in our products, including tin-plate steel used in packaging for our canned products, which we were able to partially offset with productivity initiatives and price increases on impacted products.
- We will continue to evaluate the evolving macroeconomic environment to take action to mitigate the impact on our business, consolidated results of operations, and financial condition.
- While we will continue to seek to offset input cost inflation with productivity initiatives and tariff mitigation efforts, we anticipate that we may need to increase prices on certain products in fiscal 2027 to mitigate margin impacts and would expect corresponding elasticity impacts.


## Research loop (think → act)

1. _heuristic_ — Coverage looks adequate for this pass; stopping iterative loop.

## Sources

- **[S1]** CAG fundamentals (yfinance)
  - ConAgra Brands, Inc.: price=15.24, rev=11281600000.0, fcf=978700000.0, shares=475029042.0, rev_cagr=-0.027791350655803293, ROIC=-0.10697344868735084, FCF yield=None
- **[S2]** CAG DCF valuation (dcf)
  - Base share price=17.78553979162984, bull=63.71028020338544, bear=-2.0395215193000564
- **[S3]** CAG put screen (yfinance_options)
  - Expiration 2026-08-28 (DTE 31): 0 candidates; IV=0.039072109375000004, IV rank=None, HV rank=0.9605103103324352. Delta band approximated via % OTM when greeks are unavailable; I…
- **[S4]** Deep Diligence Checklist for Startup Founders | Flux Capital Academy ... (web) — https://www.fluxcapital.com/academy/boards-and-diligence/boards-and-diligence-deep-diligence-technical-financial-and-legal
  - Deep diligence checklist for technical, financial, and legal review: prepare data rooms, models, IP, contracts, and investor Q&A for Series A.
- **[S5]** GitHub - Lunatic16/deep-financial-research: A Claude/Qwen/Gemini skill ... (web) — https://github.com/Lunatic16/deep-financial-research
  - A Claude/Qwen/Gemini skill for institutional-grade investment research. Connects to live market data via MCP servers to deliver company deep dives, due diligence reports, compet…
- **[S6]** Deep Due Diligence Investors | (web) — https://duediligenceclub.com/
  - A comprehensive online course offering due diligence training, equipping investors with essential skills to evaluate deals, mitigate risks, and make informed investment decisions.
- **[S7]** Six skills for financial service professionals | Claude by Anthropic (web) — https://claude.com/resources/tutorials/claude-for-financial-services-skills
  - Introduction to six specialized AI skills for financial professionals including valuation modeling, competitive analysis, research reports, and due diligence.
- **[S8]** Deep Diligence Checklist for Startup Founders | Flux Capital Academy | Flux Capital (web_page) — https://www.fluxcapital.com/academy/boards-and-diligence/boards-and-diligence-deep-diligence-technical-financial-and-legal
  - Deep Diligence Checklist for Startup Founders | Flux Capital Academy | Flux Capital Deep diligence: technical, financial, and legal Author Ari Stiegler Managing Partner, Flux Ca…
- **[S9]** GitHub - Lunatic16/deep-financial-research: A Claude/Qwen/Gemini skill for institutional-grade investment research. Connects to live market data via MCP servers to deliver company deep dives, due diligence reports, competitive landscape analysis, market sentiment, and DCF-based intrinsic value estimates — all from natural language prompts. · GitHub (web_page) — https://github.com/Lunatic16/deep-financial-research
  - GitHub - Lunatic16/deep-financial-research: A Claude/Qwen/Gemini skill for institutional-grade investment research. Connects to live market data via MCP servers to deliver compa…
- **[S10]** Deep Due Diligence Investors | (web_page) — https://duediligenceclub.com/
  - Deep Due Diligence Investors | Harness the collective wisdom of 50+ analytical investors & AI to screen opportunities, minimize risk, & amplify returns Submit an Opportunity » I…
- **[S11]** CAG 10-K (sec)
  - Item 1 chars=28227, Item 1A chars=50000, Item 7 chars=50000, ok=True, source=cache
- **[S12]** Item 1 Business summary (nlp)
  - ### Item 1 — Business (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, litigation, regulation, competition, margin, supply chain, customer, segment, product, s…
- **[S13]** Item 1A summary (nlp)
  - ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin, supply chain, cy…
- **[S14]** Item 7 summary (nlp)
  - ### Item 7 — MD&A (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, revenue, margin, supply chain, cyber, interest rate, cu…

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

# CAG — Planned Research Report

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
- Company: ConAgra Brands, Inc.
- Sector / industry: Consumer Defensive / Packaged Foods
- Price: 15.24
- 52-week range: $12.53 – $20.32
- Market cap: —
- Enterprise value: $14.55B
- Shares outstanding: 475.03M
- Beta: -0.047
- Book equity: $6.36B
- Revenue (latest): $11.28B
- EBITDA (latest): -$1.04B
- Free cash flow (latest): $978.70M
- Operating income: $1.26B
- Operating margin: 11.2%
- EV / EBITDA: -14.0x
- ROIC: -10.7%
- FCF yield: —
- Debt / Equity: 1.1432616081540203
- FCF / share: $2.06
- Revenue / share: $23.75

### Capital structure
- Cash: $218.00M
- Short-term debt: $812.40M
- Long-term debt: $6.46B
- Total debt: $7.27B
- Net debt: $7.05B
- Net debt / EBITDA: -6.8x

### Growth
- Revenue CAGR: -2.8%
- FCF CAGR: 15.6%
- Latest revenue YoY: -2.9%
- Latest FCF YoY: -24.9%

### Market expectations (yfinance, sparse)
- Mean target: $14.38
- Target range: $12.00 – $23.00
- Recommendation: hold

_Consensus revenue/EBITDA forecasts are often unavailable via free feeds; treat targets as point-in-time only._

### Historical KPIs (multi-year)

| Year | Revenue | OCF | Capex | FCF | EBITDA | LT debt | Cash | Net debt | Net income |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2026 | $11.28B | $1.40B | $423.40M | $978.70M | -$1.04B | $6.46B | $218.00M | $6.24B | -$1.92B |
| 2025 | $11.61B | $1.69B | $389.30M | $1.30B | $1.97B | $6.23B | $68.00M | $6.17B | $1.15B |
| 2024 | $12.05B | $2.02B | $388.10M | $1.63B | $1.45B | $7.49B | $77.70M | $7.41B | $347.20M |
| 2023 | $12.28B | $995.40M | $362.20M | $633.20M | $1.69B | $7.08B | $93.30M | $6.99B | $683.60M |

## Charts

### Revenue & FCF history
![Revenue & FCF history](/charts/CAG_income_revenue_fcf.png)

## Web research — web_research

- Queries: CAG news, ConAgra Brands, Inc. earnings OR catalyst
- Unique hits: 16
- Pages fetched: 1/3

### Web synthesis — web_research (rule-based fallback — Ollama unavailable)
**Keyword hits:** revenue, margin, supply chain, market

- [HIT] ConAgra Foods News | Markets Insider | markets.businessinsider.com | https://markets.businessinsider.com/news/cag-stock?p=2 ConAgra Foods News: This is the News-site for the company ConAgra Foods on Markets Insider.
- (CAG) earnings report: revenue, EPS, surprise, history, news and analysis.
- | finance.yahoo.com | https://finance.yahoo.com/news/conagra-brands-inc-cag-q4-070034369.html Conagra Brands Inc (CAG) reports robust innovation-driven sales growth and market share gains, while navigating inflationary pressures and supply chain hurdles.
- [HIT] Conagra Brands Q3 Earnings Call Highlights | MarketBeat · via Yahoo Finance | https://finance.yahoo.com/markets/stocks/articles/conagra-brands-q3-earnings-call-130649696.html Conagra Brands (NYSE:CAG) executives used the company’s fiscal third-quarter 2026 earnings Q&A to emphasize improving volume trends in key categories, ou...
- Q3 2026 Earnings Call Summary | Moby · via Yahoo Finance | https://finance.yahoo.com/markets/stocks/articles/conagra-brands-inc-q3-2026-123000596.html Conagra Brands, Inc.
- [HIT] CAG Q4 Earnings Call Highlights Margin Reset and Cost Focus | Zacks · via Yahoo Finance | https://finance.yahoo.com/markets/stocks/articles/cag-q4-earnings-call-highlights-140000454.html Conagra Brands outlines a margin reset focused on restoring profitability, boosting supply chain...
- | Zacks · via Yahoo Finance | https://finance.yahoo.com/markets/stocks/articles/general-mills-omnichannel-strategy-growth-143200504.html General Mills, Inc.
- [PAGE] ConAgra Foods News | Markets Insider | https://markets.businessinsider.com/news/cag-stock?p=2 ConAgra Foods News | Markets Insider News for ConAgra Foods Inc.

### Sources found
- [Cam Newton](https://en.wikipedia.org/wiki/Cam_Newton)
  - Cameron Jerrell Newton (born May 11, 1989) is an American former professional football quarterback who played in the National Football League (NFL) for 11 se…
- [ConAgra Foods News | Markets Insider](https://markets.businessinsider.com/news/cag-stock?p=2)
  - ConAgra Foods News: This is the News-site for the company ConAgra Foods on Markets Insider.
- [CAG: Latest News, Videos and Photos | www.narendramodi.in](https://www.narendramodi.in/category/news/cag)
  - CAG has a great role in developing Time bound and outcome based system of working in the country: PM.News Updates. Media Coverage. Reflections.
- [CAG slams Air India for Rs 200 crore loss](https://www.ndtv.com/india-news/cag-slams-air-india-for-rs-200-crore-loss-463906)
  - The CAG report comes a day after the Cabinet Committee on Economic Affairs approved a fresh equity infusion of Rs 1200 crore in the cash-strapped airline.
- [January 2028 Options Now Available For Conagra Brands (CAG)](https://www.nasdaq.com/articles/january-2028-options-now-available-conagra-brands-cag)
  - Investors in Conagra Brands Inc (Symbol: CAG) saw new options begin trading today, for the January 2028 expiration. One of the key data points that goes into…
- [Conagra Brands (CAG) Up More Than 10% in 3 Months: Here's Why](https://www.nasdaq.com/articles/conagra-brands-cag-up-more-than-10-in-3-months:-heres-why)
  - Conagra Brands, Inc. CAG appears in a solid position, with its shares up 14% in the past three months compared with the industry's rise of 11.2%. The consume…
- [CAG report alleges irregularities in Bengal Amphan relief](https://www.msn.com/en-in/news/other/cag-report-alleges-irregularities-in-bengal-amphan-relief/ar-AA28FGyc?ocid=BingNewsVerp)
  - Kolkata, Jul 25 (PTI) The CAG has flagged serious irregularities in the West Bengal government's post-Cyclone Amphan relief and restoration works, alleging t…
- [Bengal govt tables 28 CAG reports, accuses TMC of ‘constitutional lapse’ while in power](https://indianexpress.com/article/cities/kolkata/bengal-govt-tables-28-cag-reports-accuses-tmc-of-constitutional-lapse-while-in-power-10803882/)
  - In its compliance audit report on post-Amphan relief and restoration works, CAG said the state's assessment of damages ...
- [All Earnings Announcements | Conagra Brands](https://www.conagrabrands.com/investor-relations/financial-news/earnings-announcements)
  - Conagra combines a rich heritage of great food with a sharpened focus on innovation. Find company, investor and career information and learn more about our b…
- [Investor Relations | Conagra Brands](https://www.conagrabrands.com/investor-relations)
  - Conagra Brands is focused on capturing growth to drive shareholder value. Find investor events and presentations, financial news and reports, and stock infor…
- [CAG Conagra Brands, Inc. Earnings Date & History - Seeking Alpha](https://seekingalpha.com/symbol/CAG/earnings)
  - Conagra Brands, Inc. (CAG) earnings report: revenue, EPS, surprise, history, news and analysis.
- [Conagra Brands Inc (CAG) Q4 2025 Earnings Call Highlights: Strong ...](https://finance.yahoo.com/news/conagra-brands-inc-cag-q4-070034369.html)
  - Conagra Brands Inc (CAG) reports robust innovation-driven sales growth and market share gains, while navigating inflationary pressures and supply chain hurdles.

## Put opportunities (heuristic) [S2]
- Expiration: 2026-08-28 (DTE 31)
- Candidates: 0
- ATM IV (est.): 3.9%
- IV rank: — (1 local samples)
- HV rank (20d realized): 96.1%


_Note: Delta band approximated via % OTM when greeks are unavailable; IV rank needs ~20+ local daily IV samples (have 1); run the options screen over time to build history.; HV rank is realized-vol rank (20d HV vs ~1y); useful when IV history is thin._

## Research loop (think → act)

1. _heuristic_ — Coverage looks adequate for this pass; stopping iterative loop.

## Sources

- **[S1]** CAG fundamentals (yfinance)
  - ConAgra Brands, Inc.: price=15.24, rev=11281600000.0, fcf=978700000.0, shares=475029042.0, rev_cagr=-0.027791350655803293, ROIC=-0.10697344868735084, FCF yield=None
- **[S2]** CAG put screen (yfinance_options)
  - Expiration 2026-08-28 (DTE 31): 0 candidates; IV=0.039072109375000004, IV rank=None, HV rank=0.9605102586622007. Delta band approximated via % OTM when greeks are unavailable; I…
- **[S3]** Cam Newton (web) — https://en.wikipedia.org/wiki/Cam_Newton
  - Cameron Jerrell Newton (born May 11, 1989) is an American former professional football quarterback who played in the National Football League (NFL) for 11 seasons, primarily wit…
- **[S4]** ConAgra Foods News | Markets Insider (web) — https://markets.businessinsider.com/news/cag-stock?p=2
  - ConAgra Foods News: This is the News-site for the company ConAgra Foods on Markets Insider.
- **[S5]** CAG: Latest News, Videos and Photos | www.narendramodi.in (web) — https://www.narendramodi.in/category/news/cag
  - CAG has a great role in developing Time bound and outcome based system of working in the country: PM.News Updates. Media Coverage. Reflections.
- **[S6]** CAG slams Air India for Rs 200 crore loss (web) — https://www.ndtv.com/india-news/cag-slams-air-india-for-rs-200-crore-loss-463906
  - The CAG report comes a day after the Cabinet Committee on Economic Affairs approved a fresh equity infusion of Rs 1200 crore in the cash-strapped airline.
- **[S7]** January 2028 Options Now Available For Conagra Brands (CAG) (web) — https://www.nasdaq.com/articles/january-2028-options-now-available-conagra-brands-cag
  - Investors in Conagra Brands Inc (Symbol: CAG) saw new options begin trading today, for the January 2028 expiration. One of the key data points that goes into the price an option…
- **[S8]** Conagra Brands (CAG) Up More Than 10% in 3 Months: Here's Why (web) — https://www.nasdaq.com/articles/conagra-brands-cag-up-more-than-10-in-3-months:-heres-why
  - Conagra Brands, Inc. CAG appears in a solid position, with its shares up 14% in the past three months compared with the industry's rise of 11.2%. The consumer-packaged-goods foo…
- **[S9]** CAG report alleges irregularities in Bengal Amphan relief (web) — https://www.msn.com/en-in/news/other/cag-report-alleges-irregularities-in-bengal-amphan-relief/ar-AA28FGyc?ocid=BingNewsVerp
  - Kolkata, Jul 25 (PTI) The CAG has flagged serious irregularities in the West Bengal government's post-Cyclone Amphan relief and restoration works, alleging that damage assessmen…
- **[S10]** Bengal govt tables 28 CAG reports, accuses TMC of ‘constitutional lapse’ while in power (web) — https://indianexpress.com/article/cities/kolkata/bengal-govt-tables-28-cag-reports-accuses-tmc-of-constitutional-lapse-while-in-power-10803882/
  - In its compliance audit report on post-Amphan relief and restoration works, CAG said the state's assessment of damages ...
- **[S11]** ConAgra Foods News | Markets Insider (web_page) — https://markets.businessinsider.com/news/cag-stock?p=2
  - ConAgra Foods News | Markets Insider News for ConAgra Foods Inc. TipRanks 71d Wells Fargo Keeps Their Sell Rating on Conagra Brands (CAG) TipRanks 77d Analysts Offer Insights on…

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

# CAG — Planned Research Report

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
- Company: ConAgra Brands, Inc.
- Sector / industry: Consumer Defensive / Packaged Foods
- Price: 15.24
- 52-week range: $12.53 – $20.32
- Market cap: —
- Enterprise value: $14.55B
- Shares outstanding: 475.03M
- Beta: -0.047
- Book equity: $6.36B
- Revenue (latest): $11.28B
- EBITDA (latest): -$1.04B
- Free cash flow (latest): $978.70M
- Operating income: $1.26B
- Operating margin: 11.2%
- EV / EBITDA: -14.0x
- ROIC: -10.7%
- FCF yield: —
- Debt / Equity: 1.1432616081540203
- FCF / share: $2.06
- Revenue / share: $23.75

### Capital structure
- Cash: $218.00M
- Short-term debt: $812.40M
- Long-term debt: $6.46B
- Total debt: $7.27B
- Net debt: $7.05B
- Net debt / EBITDA: -6.8x

### Growth
- Revenue CAGR: -2.8%
- FCF CAGR: 15.6%
- Latest revenue YoY: -2.9%
- Latest FCF YoY: -24.9%

### Market expectations (yfinance, sparse)
- Mean target: $14.38
- Target range: $12.00 – $23.00
- Recommendation: hold

_Consensus revenue/EBITDA forecasts are often unavailable via free feeds; treat targets as point-in-time only._

### Historical KPIs (multi-year)

| Year | Revenue | OCF | Capex | FCF | EBITDA | LT debt | Cash | Net debt | Net income |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2026 | $11.28B | $1.40B | $423.40M | $978.70M | -$1.04B | $6.46B | $218.00M | $6.24B | -$1.92B |
| 2025 | $11.61B | $1.69B | $389.30M | $1.30B | $1.97B | $6.23B | $68.00M | $6.17B | $1.15B |
| 2024 | $12.05B | $2.02B | $388.10M | $1.63B | $1.45B | $7.49B | $77.70M | $7.41B | $347.20M |
| 2023 | $12.28B | $995.40M | $362.20M | $633.20M | $1.69B | $7.08B | $93.30M | $6.99B | $683.60M |

## Charts

### Revenue & FCF history
![Revenue & FCF history](/charts/CAG_fast_revenue_fcf.png)

### DCF scenario prices
![DCF scenario prices](/charts/CAG_fast_dcf_scenarios.png)

### Base-case FCF path
![Base-case FCF path](/charts/CAG_fast_base_fcf_path.png)

## DCF valuation (base / bull / bear) [S2]

> Simplified revenue->FCF DCF. Not investment advice; assumptions are editable heuristics.

- Spot price: $15.24
- Base revenue: $11.28B
- Shares: 475,029,042
- Net debt (Debt−Cash): $7.05B

| Scenario | Growth | FCF margin | WACC | Term. g | Equity value | Share price | Upside |
|----------|--------|------------|------|---------|--------------|-------------|--------|
| bear | -2.9% | 6.7% | 12.0% | 1.5% | -$968.83M | $-2.04 | -113.4% |
| base | 6.0% | 8.7% | 10.0% | 2.5% | $8.45B | $17.79 | 16.7% |
| bull | 15.0% | 11.7% | 9.0% | 3.0% | $30.26B | $63.71 | 318.0% |

### Assumption notes
- Base revenue growth seeded from historical rate (-2.9%).
- Recent revenue declined (-2.9% YoY); base/bull use normalized mid-cycle growth instead of extrapolating the decline.

- _bear: model equity value is negative after net debt (-968,831,953); showing $-2.04/sh._

### Base-case projected FCF

- Year 1: revenue $11.96B, FCF $1.04B (PV $943.11M)
- Year 2: revenue $12.68B, FCF $1.10B (PV $908.82M)
- Year 3: revenue $13.44B, FCF $1.17B (PV $875.77M)
- Year 4: revenue $14.24B, FCF $1.24B (PV $843.92M)
- Year 5: revenue $15.10B, FCF $1.31B (PV $813.23M)
- Terminal value $17.90B (PV $11.11B)

## Put opportunities (heuristic) [S3]
- Expiration: 2026-08-28 (DTE 31)
- Candidates: 0
- ATM IV (est.): 3.9%
- IV rank: — (1 local samples)
- HV rank (20d realized): 96.1%


_Note: Delta band approximated via % OTM when greeks are unavailable; IV rank needs ~20+ local daily IV samples (have 1); run the options screen over time to build history.; HV rank is realized-vol rank (20d HV vs ~1y); useful when IV history is thin._

## Research loop (think → act)

1. _heuristic_ — Coverage looks adequate for this pass; stopping iterative loop.

## Sources

- **[S1]** CAG fundamentals (yfinance)
  - ConAgra Brands, Inc.: price=15.24, rev=11281600000.0, fcf=978700000.0, shares=475029042.0, rev_cagr=-0.027791350655803293, ROIC=-0.10697344868735084, FCF yield=None
- **[S2]** CAG DCF valuation (dcf)
  - Base share price=17.78553979162984, bull=63.71028020338544, bear=-2.0395215193000564
- **[S3]** CAG put screen (yfinance_options)
  - Expiration 2026-08-28 (DTE 31): 0 candidates; IV=0.039072109375000004, IV rank=None, HV rank=0.9605102635844949. Delta band approximated via % OTM when greeks are unavailable; I…

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
