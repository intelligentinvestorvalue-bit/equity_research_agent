# CMC — Full research pack

> Not investment advice. Local research draft only.

**Templates:** memo, valuation, deep, income, fast
**Generated:** 2026-07-28T04:26:50.168117+00:00



---

# Template: Institutional deep dive (memo) (`memo`)

# CMC — Planned Research Report

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
- Company: Commercial Metals Company
- Sector / industry: Industrials / Metal Fabrication
- Price: 68.04
- 52-week range: $49.66 – $84.87
- Market cap: —
- Enterprise value: $10.59B
- Shares outstanding: 109.53M
- Beta: 1.532
- Book equity: $4.19B
- Revenue (latest): $7.80B
- EBITDA (latest): $438.92M
- Free cash flow (latest): $312.25M
- Operating income: $519.92M
- Operating margin: 6.7%
- EV / EBITDA: 24.1x
- ROIC: 3.4%
- FCF yield: —
- Debt / Equity: 0.32298442237732483
- FCF / share: $2.85
- Revenue / share: $71.20

### Capital structure
- Cash: $1.04B
- Short-term debt: $44.29M
- Long-term debt: $1.31B
- Total debt: $1.35B
- Net debt: $311.04M
- Net debt / EBITDA: 0.7x

### Growth
- Revenue CAGR: -4.4%
- FCF CAGR: 7.6%
- Latest revenue YoY: -1.6%
- Latest FCF YoY: -45.7%

### Market expectations (yfinance, sparse)
- Mean target: $80.09
- Target range: $75.00 – $88.00
- Recommendation: buy

_Consensus revenue/EBITDA forecasts are often unavailable via free feeds; treat targets as point-in-time only._

### Historical KPIs (multi-year)

| Year | Revenue | OCF | Capex | FCF | EBITDA | LT debt | Cash | Net debt | Net income |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2025 | $7.80B | $715.07M | $402.82M | $312.25M | $438.92M | $1.31B | $1.04B | $266.75M | $84.66M |
| 2024 | $7.93B | $899.71M | $324.27M | $575.44M | $963.93M | $1.15B | $857.92M | $292.91M | $485.49M |
| 2023 | $8.80B | $1.34B | $606.66M | $737.44M | $1.38B | $1.11B | $592.33M | $521.95M | $859.76M |
| 2022 | $8.91B | $700.31M | $449.99M | $250.32M | $1.74B | $1.11B | $672.60M | $440.65M | $1.22B |

## Charts

### Revenue & FCF history
![Revenue & FCF history](/charts/CMC_memo_revenue_fcf.png)

### DCF scenario prices
![DCF scenario prices](/charts/CMC_memo_dcf_scenarios.png)

### Base-case FCF path
![Base-case FCF path](/charts/CMC_memo_base_fcf_path.png)

### EV/EBITDA scenario prices
![EV/EBITDA scenario prices](/charts/CMC_memo_ev_ebitda_scenarios.png)

### Headwind/tailwind price ranges
![Headwind/tailwind price ranges](/charts/CMC_memo_scenario_ranges.png)

### Normalized price vs peers
![Normalized price vs peers](/charts/CMC_memo_peers_normalized.png)

## DCF valuation (base / bull / bear) [S3]

> Simplified revenue->FCF DCF. Not investment advice; assumptions are editable heuristics.

- Spot price: $68.04
- Base revenue: $7.80B
- Shares: 109,528,048
- Net debt (Debt−Cash): $311.04M

| Scenario | Growth | FCF margin | WACC | Term. g | Equity value | Share price | Upside |
|----------|--------|------------|------|---------|--------------|-------------|--------|
| bear | -1.6% | 2.0% | 12.0% | 1.5% | $1.02B | $9.30 | -86.3% |
| base | 6.0% | 4.0% | 10.0% | 2.5% | $4.63B | $42.31 | -37.8% |
| bull | 15.0% | 7.0% | 9.0% | 3.0% | $15.16B | $138.44 | 103.5% |

### Assumption notes
- Base revenue growth seeded from historical rate (-1.6%).
- Recent revenue declined (-1.6% YoY); base/bull use normalized mid-cycle growth instead of extrapolating the decline.


### Base-case projected FCF

- Year 1: revenue $8.27B, FCF $330.98M (PV $300.89M)
- Year 2: revenue $8.76B, FCF $350.84M (PV $289.95M)
- Year 3: revenue $9.29B, FCF $371.89M (PV $279.41M)
- Year 4: revenue $9.85B, FCF $394.21M (PV $269.25M)
- Year 5: revenue $10.44B, FCF $417.86M (PV $259.46M)
- Terminal value $5.71B (PV $3.55B)

## Valuation — EV/EBITDA scenarios [S2]

> Priced-in model: implied price = (EBITDA × EV/EBITDA − net debt) ÷ shares. Not a forecast.

- Spot: $68.04
- Net debt used: $311.04M

| Scenario | EBITDA | EV/EBITDA | Implied EV | Equity value | Implied price |
|---|---:|---:|---:|---:|---:|
| bear | $307.24M | 18.1x | $5.56B | $5.25B | $47.93 |
| base | $438.92M | 24.1x | $10.59B | $10.28B | $93.87 |
| bull | $526.70M | 30.2x | $15.89B | $15.58B | $142.22 |

- Base EBITDA seeded from latest reported/TTM figure (438,920,000).
- Base multiple seeded from current EV/EBITDA (24.1x).

## Scenario price ranges (headwinds & tailwinds) [S39]

> Medium-term (18–36 months (medium / medium-long term)) driver → EV/EBITDA bridge. Distinct from the FCF DCF path. Not investment advice.

- Spot: $68.04
- Sparse Street mean target: $80.09
- Anchor multiple: 24.1x (driver_ev_ebitda_bridge)
- Anchor EBITDA: $438.92M
- Probability-weighted midpoint: **$116.76** (heuristic weights, not a rating)
- Driver extraction: `rules`

### Headwinds (bear-case fuel)

- **Balance-sheet / refinancing pressure** — sector=Industrials industry=Metal Fabrication revenue=7798480000.0 ebitda=438920000.0 fcf=312249000.0 net_debt=311043000.0 nd_ebitda=0.708655335824296 target=80.09091 rec=buy _(source: fundamentals)_
- **Regulatory / legal risk** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, litigation, regulation, competition, margin, supply chain, cyber, interest rate, custo _(source: item_1a)_
- **Competitive / pricing pressure** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, litigation, regulation, competition, margin, supply chain, cyber, interest rate, custo _(source: item_1a)_
- **Margin / cost headwind** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, litigation, regulation, competition, margin, supply chain, cyber, interest rate, custo _(source: item_1a)_
- **Operational / cyber risk** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, litigation, regulation, competition, margin, supply chain, cyber, interest rate, custo _(source: item_1a)_

### Tailwinds (bull-case fuel)

- **Manageable leverage** — Net debt / EBITDA ≈ 0.7x — room for reinvestment or returns _(source: fundamentals)_
- **Positive free cash flow** — FCF $312.25M _(source: fundamentals)_
- **Contract / backlog wins** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, litigation, regulation, competition, margin, supply chain, cyber, interest rate, custo _(source: item_1a)_
- **Product / pricing power** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, litigation, regulation, competition, margin, supply chain, cyber, interest rate, custo _(source: item_1a)_
- **Growth / execution upside** — ### Item 1 — Business (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, margin, supply chain, customer, segment,  _(source: item_1)_
- **Margin expansion / cost takeout** — ### Item 1 — Business (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, margin, supply chain, customer, segment,  _(source: item_1)_
- **Multiple re-rating / Street upgrades** — Up Over 100%: These 2 Monster Growth Stocks Earn an Upgrade Growth investing is a perennially popular strategy – and for good reason. While not all growth stock... _(source: web)_

### Price ranges by case

| Case | Prob. | Metric vs TTM | Multiple | Price low | Mid | High | Upside vs spot |
|---|---:|---:|---:|---:|---:|---:|---:|
| bear | 0.21 | 0.74x | 8.4x | $19.46 | $21.93 | $24.41 | -68% |
| base | 0.45 | 1.04x | 24.1x | $90.70 | $97.74 | $104.78 | +44% |
| bull | 0.34 | 1.23x | 41.3x | $180.16 | $200.49 | $220.83 | +195% |

#### Bear — headwinds dominate

Headwinds bite: weaker operating trajectory and multiple compression. Equity duration shrinks if cash generation fails to offset leverage / competitive pressure.

- **Range:** $19.46 – $24.41 (mid $21.93) · EBITDA $324.80M · multiple 8.4x
- Driver: **Balance-sheet / refinancing pressure** — sector=Industrials industry=Metal Fabrication revenue=7798480000.0 ebitda=438920000.0 fcf=312249000.0 net_debt=311043000.0 nd_ebitda=0.708655335824296 target=80
- Driver: **Regulatory / legal risk** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, litigation, regulation, competition, margin, supply chain, cyber, 
- Driver: **Competitive / pricing pressure** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, litigation, regulation, competition, margin, supply chain, cyber, 
- Driver: **Margin / cost headwind** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, litigation, regulation, competition, margin, supply chain, cyber, 
- Driver: **Operational / cyber risk** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, litigation, regulation, competition, margin, supply chain, cyber, 

#### Base — mixed execution

Balanced path: some tailwinds offset headwinds. Operating scale roughly holds with modest repair/normalization; valuation stays near the current EV/EBITDA anchor.

- **Range:** $90.70 – $104.78 (mid $97.74) · EBITDA $456.48M · multiple 24.1x
- Driver: **Manageable leverage** — Net debt / EBITDA ≈ 0.7x — room for reinvestment or returns
- Driver: **Positive free cash flow** — FCF $312.25M
- Driver: **Balance-sheet / refinancing pressure** — sector=Industrials industry=Metal Fabrication revenue=7798480000.0 ebitda=438920000.0 fcf=312249000.0 net_debt=311043000.0 nd_ebitda=0.708655335824296 target=80
- Driver: **Regulatory / legal risk** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, litigation, regulation, competition, margin, supply chain, cyber, 

#### Bull — tailwinds dominate

Tailwinds compound: operating improvement plus a re-rating toward peer or recovery multiples as balance-sheet and growth narratives improve.

- **Range:** $180.16 – $220.83 (mid $200.49) · EBITDA $539.87M · multiple 41.3x
- Driver: **Manageable leverage** — Net debt / EBITDA ≈ 0.7x — room for reinvestment or returns
- Driver: **Positive free cash flow** — FCF $312.25M
- Driver: **Contract / backlog wins** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, litigation, regulation, competition, margin, supply chain, cyber, 
- Driver: **Product / pricing power** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, litigation, regulation, competition, margin, supply chain, cyber, 
- Driver: **Growth / execution upside** — ### Item 1 — Business (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, margin, supply chain,

### Method notes

- Item 1A risks weighted toward headwinds.
- Peer EV/EBITDA band 8.8x–43.4x (median 11.1x) informs multiple ranges.
- Mapping follows Gemini/Perplexity-style scenario memos: qualitative drivers → operating metric & multiple paths → share-price ranges over a medium-term horizon.

## Peer & factor comps

- Sector / industry: Industrials / Metal Fabrication
- Peers: CCJ, UEC, NXE, UUUU, FCX

| Ticker | Mkt cap | EV/EBITDA | ND/EBITDA | Beta | 1y | 5y | Vol |
|---|---:|---:|---:|---:|---:|---:|---:|
| CMC | — | 8.8x | 2.5x | 1.53 | 29.1% | 129.0% | 35.9% |
| CCJ | — | 43.4x | -0.1x | 1.00 | 12.5% | 411.6% | 49.9% |
| UEC | — | -36.6x | 4.0x | 1.19 | 11.2% | 325.3% | 74.4% |
| NXE | $6.2B | -61.1x | 3.1x | 1.65 | 27.7% | 124.0% | 58.1% |
| UUUU | $2.9B | -33.2x | 2.9x | 1.58 | 17.0% | 114.5% | 73.1% |
| FCX | — | 11.1x | 0.7x | 1.36 | 41.2% | 83.2% | 45.2% |

- Peer set (heuristic by sector/industry): CCJ, UEC, NXE, UUUU, FCX
- Beta vs CCJ (daily, ~5y overlap): 0.23

_Price returns are price-only (dividends ignored). Peer set is heuristic, not a formal comps universe._

## Earnings, guidance & revision catalysts

- Next earnings (calendar): 2026-10-15

| Date | EPS est | EPS actual | Surprise | 1-day move |
|---|---:|---:|---:|---:|
| 2026-10-15 | 1.98 | — | — | — |
| 2026-06-25 | 1.71 | 1.73 | 0.02 | -6.6% |
| 2026-03-26 | 1.30 | 1.16 | -0.14 | -2.0% |
| 2026-01-08 | 1.50 | 1.84 | 0.34 | 2.6% |
| 2025-10-16 | 1.34 | 1.37 | 0.03 | 3.7% |
| 2025-06-23 | 0.85 | 0.74 | -0.11 | 1.6% |
| 2025-03-20 | 0.30 | 0.26 | -0.04 | -1.6% |
| 2025-01-06 | 0.79 | 0.78 | -0.01 | -3.0% |
| 2024-10-17 | 0.86 | 0.90 | 0.04 | -0.5% |
| 2024-06-20 | 1.02 | 1.02 | 0.00 | 3.3% |
| 2024-03-21 | 0.76 | 0.88 | 0.12 | -1.9% |
| 2024-01-08 | 1.47 | 1.63 | 0.16 | -4.8% |

_EPS surprise vs 1-day move Pearson r=0.09 (n=11, p≈0.787); treat as suggestive only._

_Guidance vs Street and adjusted EBITDA are often missing from free feeds; use web/SEC sections for narrative guidance._

## Recent SEC filings (10-Q / 8-K)

| Date | Form | Description |
|---|---|---|
| 2026-06-29 | 10-Q | [10-Q](https://www.sec.gov/Archives/edgar/data/22444/000002244426000041/cmc-20260531.htm) |
| 2026-06-25 | 8-K | [8-K](https://www.sec.gov/Archives/edgar/data/22444/000002244426000038/cmc-20260625.htm) |
| 2026-06-24 | 8-K | [8-K](https://www.sec.gov/Archives/edgar/data/22444/000002244426000035/cmc-20260624.htm) |
| 2026-04-13 | 8-K | [8-K](https://www.sec.gov/Archives/edgar/data/22444/000119312526152960/d117730d8k.htm) |
| 2026-03-31 | 10-Q | [10-Q](https://www.sec.gov/Archives/edgar/data/22444/000002244426000031/cmc-20260228.htm) |
| 2026-03-26 | 8-K | [8-K](https://www.sec.gov/Archives/edgar/data/22444/000002244426000025/cmc-20260326.htm) |
| 2026-03-25 | 8-K | [8-K](https://www.sec.gov/Archives/edgar/data/22444/000002244426000021/cmc-20260325.htm) |
| 2026-01-15 | 8-K | [8-K](https://www.sec.gov/Archives/edgar/data/22444/000119312526014157/d66572d8k.htm) |
| 2026-01-08 | 10-Q | [10-Q](https://www.sec.gov/Archives/edgar/data/22444/000002244426000010/cmc-20251130.htm) |
| 2026-01-08 | 8-K | [8-K](https://www.sec.gov/Archives/edgar/data/22444/000002244426000009/cmc-20260108.htm) |
| 2026-01-05 | 8-K | [8-K](https://www.sec.gov/Archives/edgar/data/22444/000002244426000003/cmc-20260105.htm) |
| 2025-12-17 | 8-K | [8-K](https://www.sec.gov/Archives/edgar/data/22444/000119312525322952/d21012d8k.htm) |

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

Commercial Metals Company (CMC) trades near 68.04 with market cap — and EV $10.59B. Net debt is $311.04M (ND/EBITDA 0.708655335824296). Latest revenue $7.80B, EBITDA $438.92M, FCF $312.25M.

**Goal focus:** Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers.

What matters most (framework): balance-sheet trajectory, cash generation vs leverage, and whether market expectations (sparse free-data targets) already price execution risk.

EV/EBITDA implied prices — bear $47.93 / base $93.87 / bull $142.22.

## Company setup & business model

**Keyword hits:** risk, uncertainty, litigation, regulation, competition, margin, supply chain, customer, segment, product, service, market, operations, network

- DISCLOSURE REGARDING FORWARD-LOOKING STATEMENTS  This annual report on Form 10-K (hereinafter referred to as the "Annual Report") contains forward-looking statements within the meaning of Section 27A of the Securities Act of 1933, as amended (the "Securities Act"), Section 21E of the Securities Exchange Act of 1934, as amended (the "Exchange Act") and the Private Securities Litigation Reform Act of 1995.
- Actual results, performance or achievements could differ materially from those projected in the forward-looking statements as a result of a  number of risks, uncertainties and other factors.
- For a discussion of important factors that could cause our results, performance or achievements to differ materially from any future results, performance or achievements expressed or implied by our forward-looking statements, please refer to Part I, Item 1A, Risk Factors and Part II, Item 7, Management's Discussion and Analysis of Financial Condition and Results of Operations in this Annual Report.
- Certain trademarks or service marks of CMC appearing in this Annual Report are the property of CMC and are protected under applicable intellectual property laws.
- Today, through an extensive manufacturing network principally located in the United States ("U.S.") and Central Europe, we offer products and technologies to meet the critical reinforcement needs of the global construction sector.
- Our operations are conducted through three reportable segments: North America Steel Group, Emerging Businesses Group and Europe Steel Group.
- At CMC, we believe "it’s what’s inside that counts." This reflects the nature of our products, which are found in critical infrastructure worldwide, and also applies to our culture and employees.
- We operate under the guiding principles of placing the customer at the core of all we do, staying committed to our employees, giving back to our communities and creating value for our investors, all while continuing our commitment to sustainability.
- From our inception, our business model has been  strategically built on sustainable principles, including recycling metals, manufacturing products from approximately 98% recycled material using energy-efficient technology and employing closed-loop water recycling processes.
- We provide differentiating value for our customers through our industry-leading customer service with a low cost, high-quality production process.
- Further, we have achieved market leadership through our commitment to transformation, advancement and long-term growth by investing in our business and in our people.
- As our customers' needs and preferences have evolved, our products have expanded to include diverse and innovative solutions and future growth platforms.
- Through a combination of both value-accretive organic growth that captures available internal synergies, and capability-enhancing inorganic growth that broadens our portfolio, we aim to provide our customers with a comprehensive solution.
- Segments  The Company has three reportable segments that represent the primary businesses reported in our consolidated financial statements: North America Steel Group, Emerging Businesses Group and Europe Steel Group.
- The following chart summarizes net sales to external customers by major product category within each reportable segment during the year ended August 31, 2025.
- For a historical breakout of our net sales to external customers by major product category within each reportable segment, see Note  19, Segment Information, in Part II, Item 8 of this Annual Report.
- Sales by product.jpg  NORTH AMERICA STEEL GROUP SEGMENT  Our North America Steel Group segment provides a diverse offering of products and solutions to support the construction sector.
- Composed of a vertically integrated network of recycling facilities, steel mills and fabrication operations, our strategy in North America is to optimize our vertically integrated value chain to maximize profitability while providing industry-leading customer service.
- To execute our strategy, we seek to (i) obtain inputs at the lowest possible cost, including materials  procured from our recycling facilities, which are operated to provide low-cost scrap to our steel mills, (ii) operate modern, efficient electric arc furnace ("EAF") steel mills and (iii) enhance operational efficiency by utilizing our fabrication operations to optimize our steel mill volumes and obtain the highest possible selling prices to maximize metal margin.
- We strive to maximize cash flow generation through increased productivity, high-capacity utilization and optimal product mix.
- We have invested approximately 80%, 77% and 88% of total capital expenditures in our North America Steel Group segment during 2025, 2024 and 2023, respectively.
- Raw materials margin per ton is defined as the difference between the selling prices for processed and recycled ferrous and nonferrous  scrap metals and the price paid to purchase obsolete and industrial scrap.
- Our steel mill operations consist of six EAF mini mills, three EAF micro mills and one rerolling mill.
- Our steel mills manufacture finished long steel products including rebar, merchant bar, light structural and other special sections and wire rod, as well as semi-finished billets for rerolling and forging applications (collectively referred to as "steel products" in the context of the North America Steel Group segment).
- Each EAF mini mill consists of:  • a melt shop with an EAF;  • continuous casting equipment that shapes molten metal into billets;  • a reheating furnace that prepares billets for rolling;  • a rolling line that forms products from heated billets;  • a mechanical cooling bed that receives hot products from the rolling line;  • finishing facilities that shear, straighten, bundle and prepare products for shipping;  • baghouse systems that control particulate emissions from steelmaking operations; and  • supporting facilities such as maintenance, warehouse and office areas.
- Our EAF micro mills utilize similar equipment and processes as described above; however, these facilities utilize unique continuous process technology where metal flows uninterrupted from melting to casting to rolling into finished steel products.
- Our rerolling mill does not utilize a melt shop; the rerolling process begins by reheating billets to roll into finished steel products.
- The est imated annual  capacity for our steel mills, included in Part I, Item 2, Properties, of this Annual Report assumes a typical product mix and is not necessarily indicative of the expected production volumes or shipments in any fiscal year.

_Source: latest 10-K Item 1 (Business), summarized locally._

## Variant perception

- **Consensus frame (sparse):** recommendation=buy, mean target=80.09091.
- **Bear:** leverage and execution risk dominate; cash generation fails to cover refinancing / reinvestment needs; equity remains constrained by net debt.
- **Bull:** cash-flow and strategic optionality re-rate the equity as leverage falls and growth/mix improves.
- **Middle:** returns may track free-cash-flow more than headline revenue — verify with driver analysis tab.

## Catalysts & monitoring

- Next earnings window (calendar): 2026-10-15
- Peer tape to watch: CCJ, UEC, NXE, UUUU, FCX
- Monitor: FCF vs net debt, leverage (ND/EBITDA), refinancing headlines, and material 8-K strategy updates.
- Recent filing: 10-Q on 2026-06-29 — 10-Q
- Recent filing: 8-K on 2026-06-25 — 8-K
- Recent filing: 8-K on 2026-06-24 — 8-K
- Recent filing: 8-K on 2026-04-13 — 8-K
- Recent filing: 10-Q on 2026-03-31 — 10-Q

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
| Guidance / outlook | Forward cash/earnings path | Commercial Metals Company (CMC) Stock Forecast, Price Targets ... Based on 12 Wall Street analysts offering 12 month price targets for Commercial Metals Company in the last 3 month | Commercial Metals Company (CMC) Stock Forecast, Price Targets ... |
| Leverage / refinancing | Balance-sheet repair | Fitch Revises Commercial Metals' Outlook to Stable; Affirms IDR at ... Oct 22, 2025 ... The rating reflects Fitch's expectation that CMC's EBITDA leverage will be sustained below 3 | Fitch Revises Commercial Metals' Outlook to Stable; Affirms IDR at ... |
| Margin / EBITDA | Mix and operating leverage | Fitch Revises Commercial Metals' Outlook to Stable; Affirms IDR at ... Oct 22, 2025 ... The rating reflects Fitch's expectation that CMC's EBITDA leverage will be sustained below 3 | Fitch Revises Commercial Metals' Outlook to Stable; Affirms IDR at ... |
| Contract / backlog | Demand durability | commercial metals company completes acquisition of ... - SEC.gov Irving, Texas - November 5, 2018 - Commercial Metals Company (NYSE: CMC) ... leverage our existing rebar manufactur | commercial metals company completes acquisition of ... - SEC.gov |

_Proxies are heuristic extractions from public web/SEC context; verify against primary filings._

## Catalyst calendar

| Window | Catalyst | Notes |
|---|---|---|
| 2026-10-15 | Earnings | Next report date from yfinance calendar |
| 2026-06-29 | 10-Q | 10-Q |
| 2026-06-25 | 8-K | 8-K |
| 2026-06-24 | 8-K | 8-K |
| 2026-04-13 | 8-K | 8-K |
| 2026-03-31 | 10-Q | 10-Q |
| 2026-03-26 | 8-K | 8-K |
| 2026-03-25 | 8-K | 8-K |
| 2026-01-15 | 8-K | 8-K |
| 2026-01-08 | 10-Q | 10-Q |
| 2026-01-08 | 8-K | 8-K |
| 2026-01-05 | 8-K | 8-K |
| 2025-12-17 | 8-K | 8-K |
| June 1, 2026 | Web event | Commercial Metals Co stock (US2017231034): Investor Day puts strategy in focus |
| Jan 20, 2025 | Web event | Concrete Reinforcing Steel - CMC |
| Jan 8, 2026 | Web event | CMC Reports First Quarter of Fiscal 2026 Results |
| Oct 22, 2025 | Web event | Fitch Revises Commercial Metals' Outlook to Stable; Affirms IDR at ... |
| November 5, 2018 | Web event | commercial metals company completes acquisition of ... - SEC.gov |

## Web research — web_analysts

- Queries: CMC analyst price target, Commercial Metals Company stock rating OR consensus OR upgrade OR downgrade, CMC Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers analyst, CMC guidance OR investor day OR catalyst
- Unique hits: 23
- Pages fetched: 2/3

### Web synthesis — web_analysts (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, guidance, revenue, margin, segment, product, market, operations, network

- [HIT] CMC Stock Quote Price and Forecast - CNN | www.cnn.com | https://www.cnn.com/markets/stocks/CMC The price of CMC shares has increased $0.91 since the market last closed.
- [HIT] CMC Markets (LSE:CMCX) Stock Sees Fair Value Lift After Analysts Raised Growth...
- · via Yahoo Finance | https://finance.yahoo.com/markets/stocks/articles/cmc-markets-lse-cmcx-stock-071054783.html CMC Markets is back in focus as fair value estimates shift from £4.47 to £6.30, while some bullish...
- | www.marketwatch.com | https://www.marketwatch.com/investing/stock/CMC CMC | Complete Commercial Metals Co.
- [HIT] Top Stock Reports for Bank of America, Netflix & TotalEnergies | Zacks · via Yahoo Finance | https://finance.yahoo.com/markets/stocks/articles/top-stock-reports-bank-america-201500862.html Bank of America's trading, investment banking and digital expansion drive growth, but rising costs...
- [HIT] Stocks Push Higher on Strength in Tech and a Solid US Retail Sales Report | Barchart · via Yahoo Finance | https://finance.yahoo.com/markets/stocks/articles/stocks-push-higher-strength-tech-140338927.html The S&P 500 Index ($SPX ) (SPY ) today is up +0.44%, the Dow Jones Industrial Average ($DOWI ) (DIA...
- [HIT] Commercial Metals Company (CMC) — Investment Memo | app.marginofinsight.com | https://app.marginofinsight.com/memo/cmc Commercial Metals Company investment memo: research conclusion, bull/bear case, business model + moat, top catalysts and risks, Wall Street debate.
- | markets.financialcontent.com | https://markets.financialcontent.com/stocks/article/predictstreet-2026-1-8-the-infrastructure-titan-a-deep-dive-into-cmcs-strategic-evolution-and-fiscal-q1-earnings-beat Investor Sentiment and Analyst Coverage Following the Q1 earnings beat, Wall Street sentiment is overwhelmingly positive.

### Sources found
- [Commercial Metals Company (CMC) Stock Forecast, Price Targets ...](https://www.tipranks.com/stocks/cmc/forecast)
  - Based on 12 Wall Street analysts offering 12 month price targets for Commercial Metals Company in the last 3 months. The average price target is $80.45 with …
- [CMC Stock Quote Price and Forecast - CNN](https://www.cnn.com/markets/stocks/CMC)
  - The price of CMC shares has increased $0.91 since the market last closed. This is a 1.34% rise. Closed at $68.95. The stock has remained unchanged ...
- [Commercial Metals (CMC) Stock Forecast: Analyst Ratings ...](https://public.com/stocks/cmc/forecast-price-target)
  - Wall Street analysts have set a price target of $79.40, reflecting a 0.00% increase from the current stock price. What is the 2026 price prediction for ...
- [Commercial Metals Company (CMC) Stock Price, News, Quote ...](https://finance.yahoo.com/quote/CMC/)
  - 19 hours ago ... COMMERCIAL METALS CO has an Investment Rating of HOLD; a target price of $59.000000; an Industry Subrating of High; a Management Subrating o…
- [CMC Markets (LSE:CMCX) Stock Sees Fair Value Lift After Analysts Raised Growth...](https://finance.yahoo.com/markets/stocks/articles/cmc-markets-lse-cmcx-stock-071054783.html)
  - CMC Markets is back in focus as fair value estimates shift from £4.47 to £6.30, while some bullish...
- [Exploring the Valuation of Commercial Metals (CMC) Following Its Recent Share...](https://finance.yahoo.com/news/exploring-valuation-commercial-metals-cmc-170527250.html)
  - Commercial Metals (CMC) stock has seen gradual movement lately, which has attracted the attention of...
- [Commercial Metals price target lowered to $58 from $61 at BMO Capital](https://finance.yahoo.com/news/commercial-metals-price-target-lowered-123507201.html)
  - BMO Capital lowered the firm’s price target on Commercial Metals (CMC) to $58 from $61 and keeps a M...
- [Commercial Metals (CMC) Valuation Check After Q1 Earnings Beat And Growth...](https://finance.yahoo.com/news/commercial-metals-cmc-valuation-check-101305742.html)
  - Commercial Metals (CMC) grabbed investor attention after reporting a stronger than expected first...
- [Commercial Metals Company (CMC) Stock Price & Overview](https://stockanalysis.com/stocks/cmc/)
  - A detailed overview of Commercial Metals Company (CMC) stock, including real-time price, chart, key statistics, news, and more.
- [Commercial Metals - CMC - Stock Price Today - Zacks](https://www.zacks.com/stock/quote/CMC)
  - View Commercial Metals Company CMC investment & stock information. Get the latest Commercial Metals Company CMC detailed stock quotes, stock data, Real-Time …
- [CMC Stock Price | Commercial Metals Co. Stock Quote (U.S.: NYSE ...](https://www.marketwatch.com/investing/stock/CMC)
  - CMC | Complete Commercial Metals Co. stock news by MarketWatch. View real-time stock prices and stock quotes for a full financial overview.
- [Up Over 100%: These 2 Monster Growth Stocks Earn an Upgrade](https://finance.yahoo.com/news/over-100-2-monster-growth-170647806.html)
  - Growth investing is a perennially popular strategy – and for good reason. While not all growth stock...

### Search warnings
- news:CMC Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers analyst: No results found.
- news:CMC guidance OR investor day OR catalyst: No results found.

## Web research — web_drivers

- Queries: CMC Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers, Commercial Metals Company CMC outlook OR catalyst OR commodity OR uranium OR rare earth OR vanadium, CMC sector drivers OR market demand, Commercial Metals Company CMC backlog OR contract OR refinancing OR leverage
- Unique hits: 14
- Pages fetched: 3/3

### Web synthesis — web_drivers (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, margin, customer, segment, product, service, market

- [HIT] Commercial Metals (CMC) Stock Price, News & Analysis - MarketBeat | www.marketbeat.com | https://www.marketbeat.com/stocks/NYSE/CMC/ Commercial Metals Company (NYSE: CMC) is a leading global steel and metal recycler, manufacturer and fabricator based in Irving, Texas.
- This document is a Type III environmental product declaration by Commercial Metals Company that is certified by.
- [HIT] Sodium CarboxyMethyl Cellulose (CMC) Market Report | dataintelo.com | https://dataintelo.com/report/global-sodium-carboxymethyl-cellulose-cmc-market Within the sodium carboxymethyl cellulose market, product type segmentation plays a crucial role in addressing the diverse needs of various industries.
- Food grade CMC is expected to dominate the market due to its prominence in the food and beverage sector.
- [HIT] Carboxymethyl Cellulose Market Demand, Research, Forecast 2025-35 | www.pristinemarketinsights.com | https://www.pristinemarketinsights.com/carboxymethyl-cellulose-market-report The pharmaceutical sector is a significant driver of the CMC market, with its implementation in drug preparations growing progressively due to CMC’s multipurpose properties.
- The overall pharmaceutical market is expected to attain US$2363.25 billion in the year 2030.
- [HIT] Carboxymethyl Cellulose Market Size to Attain USD 19.04 Bn by 2035 | www.precedenceresearch.com | https://www.precedenceresearch.com/carboxymethyl-cellulose-market Carboxymethyl Cellulose Market Growth Factors.
- The growing demand for processed food and convenience products drives the need for carboxymethyl cellulose (CMC) as a thickening, stabilizing, and emulsifying agent in various food and beverage applications.

### Sources found
- [Deep Dive Dubai: Scuba Diving, Freediving, & Snorkelling](https://www.deepdivedubai.com/)
  - Explore Deep Dive Dubai, the world’s deepest pool for scuba diving, freediving, and snorkelling in the UAE.
- [Understanding "throw in at the deep end" Idiom... - CrossIdiomas.com](https://crossidiomas.com/throw-in-at-the-deep-end/)
  - Understanding the Idiom: "throw in at the deep end" - Meaning, Origins, and Usage. Category: TAuthor: James Anderson PronunciationJump into the deep end. Div…
- [Scenarios](https://www.scenario.blondinka.org/)
  - Список сценариев. Развлечение госпожи Марии от пользователя Blondinka. 12 заданий Госпожей от пользователя Blondinka. Начальная тренировка членососки от поль…
- [Commercial Metals Stock Price Today | NYSE: CMC Live](https://www.investing.com/equities/commercial-metals-comp)
  - Commercial Metals Company News & Analysis. Summarize CMC's latest news. Recent; Analysis; Earnings; Transcripts; Company ... USA Rare Earth. 14.42. USAR. -4.…
- [CMC Stock Price Quote - Commercial Metals Co - Morningstar](https://www.morningstar.com/stocks/xnys/cmc/quote)
  - MLI. —, $14B. Aurubis AG ADR. AIAGY. —, $9B. ESAB Corp. ESAB. $5B. JL Mag Rare-Earth Co Ltd ADR. JMREY. —, $5B. GPGI Inc Class A. GPGI. —, $4B. Worthington ...
- [Commercial Metals (CMC) Stock Price, News & Analysis - MarketBeat](https://www.marketbeat.com/stocks/NYSE/CMC/)
  - Commercial Metals Company (NYSE: CMC) is a leading global steel and metal recycler, manufacturer and fabricator based in Irving, Texas. The company operates ...
- [Concrete Reinforcing Steel - CMC](https://www.cmc.com/getmedia/2fe6e226-e1b6-4c42-a3b8-8714ef62335b/Concrete-Re-)
  - Jan 20, 2025 ... This document is a Type III environmental product declaration by Commercial Metals Company that is certified by. ASTM International (ASTM) a…
- [Sodium CarboxyMethyl Cellulose (CMC) Market Report](https://dataintelo.com/report/global-sodium-carboxymethyl-cellulose-cmc-market)
  - Within the sodium carboxymethyl cellulose market, product type segmentation plays a crucial role in addressing the diverse needs of various industries. Food …
- [Carboxymethyl Cellulose Market Demand, Research, Forecast 2025-35](https://www.pristinemarketinsights.com/carboxymethyl-cellulose-market-report)
  - The pharmaceutical sector is a significant driver of the CMC market, with its implementation in drug preparations growing progressively due to CMC’s multipur…
- [Carboxymethyl Cellulose Market Size to Attain USD 19.04 Bn by 2035](https://www.precedenceresearch.com/carboxymethyl-cellulose-market)
  - Carboxymethyl Cellulose Market Growth Factors. The growing demand for processed food and convenience products drives the need for carboxymethyl cellulose (CM…
- [CMC Reports First Quarter of Fiscal 2026 Results](https://ir.cmc.com/cmc-reports-first-quarter-of-fiscal-2026-results/)
  - Jan 8, 2026 ... IRVING, Texas, Jan. 8, 2026 /PRNewswire/ — Commercial Metals Company (NYSE: CMC) today announced financial results for its fiscal first quart…
- [Fitch Revises Commercial Metals' Outlook to Stable; Affirms IDR at ...](https://www.fitchratings.com/research/corporate-finance/fitch-revises-commercial-metals-outlook-to-stable-affirms-idr-at-bb-22-10-2025)
  - Oct 22, 2025 ... The rating reflects Fitch's expectation that CMC's EBITDA leverage will be sustained below 3.5x and that EBITDA margins will be sustained ab…

### Search warnings
- news:CMC Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers: No results found.
- news:Commercial Metals Company CMC outlook OR catalyst OR commodity OR uranium OR rare earth OR vanadium: No results found.
- news:CMC sector drivers OR market demand: No results found.
- news:Commercial Metals Company CMC backlog OR contract OR refinancing OR leverage: No results found.

## SEC filing [S27]
- Extraction OK: True
- Item 1 chars: 45984
- Item 1A chars: 50000
- Item 7 chars: 50000
- Meta: {'accession_number': '0000022444-25-000138', 'filing_date': '2025-10-16', 'source': 'edgartools', 'path': 'C:\\DevWork\\equity_research_agent\\data\\filings\\CMC_10k.txt'}

## Qualitative analysis (local LLM)

_Item 1 Business summary mode: rule_based (see Company setup & business model)._

### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, litigation, regulation, competition, margin, supply chain, cyber, interest rate, customer, segment, product, service, market, operations, network

- There are inherent risks and uncertainties associated with our business that could adversely affect our business, results of operations and financial condition.
- Set forth below are descriptions of those risks and uncertainties that we currently believe to be material, but the risks and uncertainties described below are not the only risks and uncertainties that could adversely affect our business, results of operations and financial condition.
- If any of these risks actually occur, our business,  results of operations and financial condition could be materially adversely affected.
- RISKS RELATED TO OUR BUSINESS  Scrap and other inputs for our business are subject to significant price fluctuations and limited availability, which may adversely affect our business, results of operations and financial condition.
- We depend on ferrous scrap, the primary raw material used by our steel mills, and other inputs such as graphite electrodes and alloys for our steel mill operations.
- The price of scrap and other inputs has historically been subject to significant fluctuation, and we may not be able to adjust our product prices to recover the costs of rapid increases in raw  material prices, especially over the short-term and in our fixed price contracts.
- The profitability of our operations would be adversely affected if we are unable to pass increased raw material and input costs on to our customers.
- A prolonged period of low scrap prices or a fall in scrap prices could impair our ability to obtain, process, sell and consume  recycled material, which could have a material adverse effect on our business, results of operations and financial condition.


### Item 7 — MD&A (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, uncertainty, litigation, regulation, revenue, margin, interest rate, customer, segment, product, service, market, operations, network

- AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERATIONS  This Management's Discussion and Analysis of Financial Condition and Results of Operations should be read in conjunction with our consolidated financial statements and the accompanying notes contained in this Annual Report.
- Our discussion and analysis of fiscal year 2024 compared to fiscal year 2023 can be found in Part II, Item 7, Management's Discussion and Analysis of Financial Condition and  Results of Operations, in our Annual Report on Form 10-K for the year ended August 31, 2024, which was filed with the SEC on October 17, 2024.
- Today, through an extensive manufacturing network principally located in the U.S.
- and Central Europe, the Company offers products and technologies to meet the critical reinforcement needs of the global construction sector.
- Our operations are conducted through three reportable segments: North America Steel Group, Emerging Businesses Group and Europe Steel Group.
- See Part I, Item 1, Business, of this Annual Report for further information regarding our business and reportable segments.
- Key Performance Indicators  When evaluating our results, we compare net sales, in the aggregate and for each of our reportable segments, in the current period to net sales in the corresponding period.
- For the North America Steel Group and the Europe Steel Group segments, we focus on changes in average selling price per ton and tons shipped compared to the corresponding period for each of our vertically integrated product categories as these are the two variables that typically have the greatest impact on our net sales for  those reportable segments.


## Research loop (think → act)

1. _heuristic_ — Coverage looks adequate for this pass; stopping iterative loop.

## Sources

- **[S1]** CMC fundamentals (yfinance)
  - Commercial Metals Company: price=68.04, rev=7798480000.0, fcf=312249000.0, shares=109528048.0, rev_cagr=-0.04356776135013685, ROIC=0.033978529382836874, FCF yield=None
- **[S2]** CMC EV/EBITDA valuation (multiples)
  - Base implied price=93.86835890656975, multiple=24.13255518089857
- **[S3]** CMC DCF valuation (dcf)
  - Base share price=42.30738539488079, bull=138.43786429322256, bear=9.295473994309154
- **[S4]** CMC peer comps (peers)
  - Peers: CCJ, UEC, NXE, UUUU, FCX; rows=6
- **[S5]** CMC earnings history (earnings)
  - rows=12; next=2026-10-15
- **[S6]** Commercial Metals Company (CMC) Stock Forecast, Price Targets ... (web) — https://www.tipranks.com/stocks/cmc/forecast
  - Based on 12 Wall Street analysts offering 12 month price targets for Commercial Metals Company in the last 3 months. The average price target is $80.45 with a ...
- **[S7]** CMC Stock Quote Price and Forecast - CNN (web) — https://www.cnn.com/markets/stocks/CMC
  - The price of CMC shares has increased $0.91 since the market last closed. This is a 1.34% rise. Closed at $68.95. The stock has remained unchanged ...
- **[S8]** Commercial Metals (CMC) Stock Forecast: Analyst Ratings ... (web) — https://public.com/stocks/cmc/forecast-price-target
  - Wall Street analysts have set a price target of $79.40, reflecting a 0.00% increase from the current stock price. What is the 2026 price prediction for ...
- **[S9]** Commercial Metals Company (CMC) Stock Price, News, Quote ... (web) — https://finance.yahoo.com/quote/CMC/
  - 19 hours ago ... COMMERCIAL METALS CO has an Investment Rating of HOLD; a target price of $59.000000; an Industry Subrating of High; a Management Subrating of ...
- **[S10]** CMC Markets (LSE:CMCX) Stock Sees Fair Value Lift After Analysts Raised Growth... (web) — https://finance.yahoo.com/markets/stocks/articles/cmc-markets-lse-cmcx-stock-071054783.html
  - CMC Markets is back in focus as fair value estimates shift from £4.47 to £6.30, while some bullish...
- **[S11]** Exploring the Valuation of Commercial Metals (CMC) Following Its Recent Share... (web) — https://finance.yahoo.com/news/exploring-valuation-commercial-metals-cmc-170527250.html
  - Commercial Metals (CMC) stock has seen gradual movement lately, which has attracted the attention of...
- **[S12]** Commercial Metals price target lowered to $58 from $61 at BMO Capital (web) — https://finance.yahoo.com/news/commercial-metals-price-target-lowered-123507201.html
  - BMO Capital lowered the firm’s price target on Commercial Metals (CMC) to $58 from $61 and keeps a M...
- **[S13]** Commercial Metals (CMC) Valuation Check After Q1 Earnings Beat And Growth... (web) — https://finance.yahoo.com/news/commercial-metals-cmc-valuation-check-101305742.html
  - Commercial Metals (CMC) grabbed investor attention after reporting a stronger than expected first...
- **[S14]** CMC Stock Quote Price and Forecast | CNN (web_page) — https://www.cnn.com/markets/stocks/CMC
  - CMC Stock Quote Price and Forecast | CNN CMC Commercial Metals Company Commercial Metals Company CMC Facts Insights Learn 1d 5d 1m 6m YTD 1y 5y Price Momentum CMC is trading in …
- **[S15]** Commercial Metals (CMC) Stock Forecast: Analyst Ratings, Predictions & Price Target 2026 (web_page) — https://public.com/stocks/cmc/forecast-price-target
  - Commercial Metals (CMC) Stock Forecast: Analyst Ratings, Predictions & Price Target 2026 Skip to main About CMC Options chain Market cap P/E ratio Forecast Earnings News Pre-mar…
- **[S16]** Deep Dive Dubai: Scuba Diving, Freediving, & Snorkelling (web) — https://www.deepdivedubai.com/
  - Explore Deep Dive Dubai, the world’s deepest pool for scuba diving, freediving, and snorkelling in the UAE.
- **[S17]** Understanding "throw in at the deep end" Idiom... - CrossIdiomas.com (web) — https://crossidiomas.com/throw-in-at-the-deep-end/
  - Understanding the Idiom: "throw in at the deep end" - Meaning, Origins, and Usage. Category: TAuthor: James Anderson PronunciationJump into the deep end. Dive right in. Be throw…
- **[S18]** Scenarios (web) — https://www.scenario.blondinka.org/
  - Список сценариев. Развлечение госпожи Марии от пользователя Blondinka. 12 заданий Госпожей от пользователя Blondinka. Начальная тренировка членососки от пользователя Mistress_Ta…
- **[S19]** Commercial Metals Stock Price Today | NYSE: CMC Live (web) — https://www.investing.com/equities/commercial-metals-comp
  - Commercial Metals Company News & Analysis. Summarize CMC's latest news. Recent; Analysis; Earnings; Transcripts; Company ... USA Rare Earth. 14.42. USAR. -4.79% ...
- **[S20]** CMC Stock Price Quote - Commercial Metals Co - Morningstar (web) — https://www.morningstar.com/stocks/xnys/cmc/quote
  - MLI. —, $14B. Aurubis AG ADR. AIAGY. —, $9B. ESAB Corp. ESAB. $5B. JL Mag Rare-Earth Co Ltd ADR. JMREY. —, $5B. GPGI Inc Class A. GPGI. —, $4B. Worthington ...
- **[S21]** Commercial Metals (CMC) Stock Price, News & Analysis - MarketBeat (web) — https://www.marketbeat.com/stocks/NYSE/CMC/
  - Commercial Metals Company (NYSE: CMC) is a leading global steel and metal recycler, manufacturer and fabricator based in Irving, Texas. The company operates ...
- **[S22]** Concrete Reinforcing Steel - CMC (web) — https://www.cmc.com/getmedia/2fe6e226-e1b6-4c42-a3b8-8714ef62335b/Concrete-Re-
  - Jan 20, 2025 ... This document is a Type III environmental product declaration by Commercial Metals Company that is certified by. ASTM International (ASTM) as ...
- **[S23]** Sodium CarboxyMethyl Cellulose (CMC) Market Report (web) — https://dataintelo.com/report/global-sodium-carboxymethyl-cellulose-cmc-market
  - Within the sodium carboxymethyl cellulose market, product type segmentation plays a crucial role in addressing the diverse needs of various industries. Food grade CMC is expecte…
- **[S24]** Deep Dive Dubai: Scuba Diving, Freediving, & Snorkelling (web_page) — https://www.deepdivedubai.com/
  - Deep Dive Dubai: Scuba Diving, Freediving, & Snorkelling BOOK NOW  We’re closed every Monday to keep the world’s deepest pool at its very best. See you from Tuesday onwards. Di…
- **[S25]** Understanding "throw in at the deep end" Idiom: Meaning, Origins & Usage - CrossIdiomas.com (web_page) — https://crossidiomas.com/throw-in-at-the-deep-end/
  - Understanding "throw in at the deep end" Idiom: Meaning, Origins & Usage - CrossIdiomas.com Skip to content All idioms Idiom language: English Etymology: From allusion to an act…
- **[S26]** Scenarios (web_page) — https://www.scenario.blondinka.org/
  - Scenarios Список сценариев Развлечение госпожи Марии от пользователя Blondinka 12 заданий Госпожей от пользователя Blondinka Начальная тренировка членососки от пользователя Mist…
- **[S27]** CMC 10-K (sec)
  - Item 1 chars=45984, Item 1A chars=50000, Item 7 chars=50000, ok=True, source=edgartools
- **[S28]** CMC 10-Q 2026-06-29 (sec) — https://www.sec.gov/Archives/edgar/data/22444/000002244426000041/cmc-20260531.htm
  - 10-Q
- **[S29]** CMC 8-K 2026-06-25 (sec) — https://www.sec.gov/Archives/edgar/data/22444/000002244426000038/cmc-20260625.htm
  - 8-K
- **[S30]** CMC 8-K 2026-06-24 (sec) — https://www.sec.gov/Archives/edgar/data/22444/000002244426000035/cmc-20260624.htm
  - 8-K
- **[S31]** CMC 8-K 2026-04-13 (sec) — https://www.sec.gov/Archives/edgar/data/22444/000119312526152960/d117730d8k.htm
  - 8-K
- **[S32]** CMC 10-Q 2026-03-31 (sec) — https://www.sec.gov/Archives/edgar/data/22444/000002244426000031/cmc-20260228.htm
  - 10-Q
- **[S33]** CMC 8-K 2026-03-26 (sec) — https://www.sec.gov/Archives/edgar/data/22444/000002244426000025/cmc-20260326.htm
  - 8-K
- **[S34]** CMC 8-K 2026-03-25 (sec) — https://www.sec.gov/Archives/edgar/data/22444/000002244426000021/cmc-20260325.htm
  - 8-K
- **[S35]** CMC 8-K 2026-01-15 (sec) — https://www.sec.gov/Archives/edgar/data/22444/000119312526014157/d66572d8k.htm
  - 8-K
- **[S36]** Item 1 Business summary (nlp)
  - ### Item 1 — Business (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, margin, supply chain, customer, segmen…
- **[S37]** Item 1A summary (nlp)
  - ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, litigation, regulation, competition, margin, supply chain, cyber, interest rate, cu…
- **[S38]** Item 7 summary (nlp)
  - ### Item 7 — MD&A (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, revenue, margin, interest rate, customer, segment, prod…
- **[S39]** CMC scenario price ranges (scenarios)
  - ok=True; base mid=97.73668717989023; headwinds=5; tailwinds=7
- **[S40]** CMC driver analysis (drivers)
  - ok=False; drivers=7
- **[S41]** CMC memo sections (memo)
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

# CMC — Planned Research Report

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
- Company: Commercial Metals Company
- Sector / industry: Industrials / Metal Fabrication
- Price: 68.04
- 52-week range: $49.66 – $84.87
- Market cap: —
- Enterprise value: $10.59B
- Shares outstanding: 109.53M
- Beta: 1.532
- Book equity: $4.19B
- Revenue (latest): $7.80B
- EBITDA (latest): $438.92M
- Free cash flow (latest): $312.25M
- Operating income: $519.92M
- Operating margin: 6.7%
- EV / EBITDA: 24.1x
- ROIC: 3.4%
- FCF yield: —
- Debt / Equity: 0.32298442237732483
- FCF / share: $2.85
- Revenue / share: $71.20

### Capital structure
- Cash: $1.04B
- Short-term debt: $44.29M
- Long-term debt: $1.31B
- Total debt: $1.35B
- Net debt: $311.04M
- Net debt / EBITDA: 0.7x

### Growth
- Revenue CAGR: -4.4%
- FCF CAGR: 7.6%
- Latest revenue YoY: -1.6%
- Latest FCF YoY: -45.7%

### Market expectations (yfinance, sparse)
- Mean target: $80.09
- Target range: $75.00 – $88.00
- Recommendation: buy

_Consensus revenue/EBITDA forecasts are often unavailable via free feeds; treat targets as point-in-time only._

### Historical KPIs (multi-year)

| Year | Revenue | OCF | Capex | FCF | EBITDA | LT debt | Cash | Net debt | Net income |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2025 | $7.80B | $715.07M | $402.82M | $312.25M | $438.92M | $1.31B | $1.04B | $266.75M | $84.66M |
| 2024 | $7.93B | $899.71M | $324.27M | $575.44M | $963.93M | $1.15B | $857.92M | $292.91M | $485.49M |
| 2023 | $8.80B | $1.34B | $606.66M | $737.44M | $1.38B | $1.11B | $592.33M | $521.95M | $859.76M |
| 2022 | $8.91B | $700.31M | $449.99M | $250.32M | $1.74B | $1.11B | $672.60M | $440.65M | $1.22B |

## Charts

### Revenue & FCF history
![Revenue & FCF history](/charts/CMC_valuation_revenue_fcf.png)

### DCF scenario prices
![DCF scenario prices](/charts/CMC_valuation_dcf_scenarios.png)

### Base-case FCF path
![Base-case FCF path](/charts/CMC_valuation_base_fcf_path.png)

### EV/EBITDA scenario prices
![EV/EBITDA scenario prices](/charts/CMC_valuation_ev_ebitda_scenarios.png)

### Headwind/tailwind price ranges
![Headwind/tailwind price ranges](/charts/CMC_valuation_scenario_ranges.png)

## DCF valuation (base / bull / bear) [S2]

> Simplified revenue->FCF DCF. Not investment advice; assumptions are editable heuristics.

- Spot price: $68.04
- Base revenue: $7.80B
- Shares: 109,528,048
- Net debt (Debt−Cash): $311.04M

| Scenario | Growth | FCF margin | WACC | Term. g | Equity value | Share price | Upside |
|----------|--------|------------|------|---------|--------------|-------------|--------|
| bear | -1.6% | 2.0% | 12.0% | 1.5% | $1.02B | $9.30 | -86.3% |
| base | 6.0% | 4.0% | 10.0% | 2.5% | $4.63B | $42.31 | -37.8% |
| bull | 15.0% | 7.0% | 9.0% | 3.0% | $15.16B | $138.44 | 103.5% |

### Assumption notes
- Base revenue growth seeded from historical rate (-1.6%).
- Recent revenue declined (-1.6% YoY); base/bull use normalized mid-cycle growth instead of extrapolating the decline.


### Base-case projected FCF

- Year 1: revenue $8.27B, FCF $330.98M (PV $300.89M)
- Year 2: revenue $8.76B, FCF $350.84M (PV $289.95M)
- Year 3: revenue $9.29B, FCF $371.89M (PV $279.41M)
- Year 4: revenue $9.85B, FCF $394.21M (PV $269.25M)
- Year 5: revenue $10.44B, FCF $417.86M (PV $259.46M)
- Terminal value $5.71B (PV $3.55B)

## Valuation — EV/EBITDA scenarios [S3]

> Priced-in model: implied price = (EBITDA × EV/EBITDA − net debt) ÷ shares. Not a forecast.

- Spot: $68.04
- Net debt used: $311.04M

| Scenario | EBITDA | EV/EBITDA | Implied EV | Equity value | Implied price |
|---|---:|---:|---:|---:|---:|
| bear | $307.24M | 18.1x | $5.56B | $5.25B | $47.93 |
| base | $438.92M | 24.1x | $10.59B | $10.28B | $93.87 |
| bull | $526.70M | 30.2x | $15.89B | $15.58B | $142.22 |

- Base EBITDA seeded from latest reported/TTM figure (438,920,000).
- Base multiple seeded from current EV/EBITDA (24.1x).

## Scenario price ranges (headwinds & tailwinds) [S29]

> Medium-term (18–36 months (medium / medium-long term)) driver → EV/EBITDA bridge. Distinct from the FCF DCF path. Not investment advice.

- Spot: $68.04
- Sparse Street mean target: $80.09
- Anchor multiple: 24.1x (driver_ev_ebitda_bridge)
- Anchor EBITDA: $438.92M
- Probability-weighted midpoint: **$104.11** (heuristic weights, not a rating)
- Driver extraction: `rules`

### Headwinds (bear-case fuel)

- **Balance-sheet / refinancing pressure** — sector=Industrials industry=Metal Fabrication revenue=7798480000.0 ebitda=438920000.0 fcf=312249000.0 net_debt=311043000.0 nd_ebitda=0.708655335824296 target=80.09091 rec=buy _(source: fundamentals)_
- **Regulatory / legal risk** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, litigation, regulation, competition, margin, supply chain, cyber, interest rate, custo _(source: item_1a)_
- **Competitive / pricing pressure** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, litigation, regulation, competition, margin, supply chain, cyber, interest rate, custo _(source: item_1a)_
- **Margin / cost headwind** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, litigation, regulation, competition, margin, supply chain, cyber, interest rate, custo _(source: item_1a)_
- **Operational / cyber risk** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, litigation, regulation, competition, margin, supply chain, cyber, interest rate, custo _(source: item_1a)_

### Tailwinds (bull-case fuel)

- **Manageable leverage** — Net debt / EBITDA ≈ 0.7x — room for reinvestment or returns _(source: fundamentals)_
- **Positive free cash flow** — FCF $312.25M _(source: fundamentals)_
- **Contract / backlog wins** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, litigation, regulation, competition, margin, supply chain, cyber, interest rate, custo _(source: item_1a)_
- **Product / pricing power** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, litigation, regulation, competition, margin, supply chain, cyber, interest rate, custo _(source: item_1a)_
- **Growth / execution upside** — ### Item 1 — Business (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, margin, supply chain, customer, segment,  _(source: item_1)_
- **Margin expansion / cost takeout** — ### Item 1 — Business (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, margin, supply chain, customer, segment,  _(source: item_1)_
- **Multiple re-rating / Street upgrades** — Up Over 100%: These 2 Monster Growth Stocks Earn an Upgrade Growth investing is a perennially popular strategy – and for good reason. While not all growth stock... _(source: web)_

### Price ranges by case

| Case | Prob. | Metric vs TTM | Multiple | Price low | Mid | High | Upside vs spot |
|---|---:|---:|---:|---:|---:|---:|---:|
| bear | 0.21 | 0.74x | 15.9x | $39.67 | $44.39 | $49.12 | -35% |
| base | 0.45 | 1.04x | 24.1x | $90.70 | $97.74 | $104.78 | +44% |
| bull | 0.34 | 1.23x | 30.9x | $134.19 | $149.42 | $164.64 | +120% |

#### Bear — headwinds dominate

Headwinds bite: weaker operating trajectory and multiple compression. Equity duration shrinks if cash generation fails to offset leverage / competitive pressure.

- **Range:** $39.67 – $49.12 (mid $44.39) · EBITDA $324.80M · multiple 15.9x
- Driver: **Balance-sheet / refinancing pressure** — sector=Industrials industry=Metal Fabrication revenue=7798480000.0 ebitda=438920000.0 fcf=312249000.0 net_debt=311043000.0 nd_ebitda=0.708655335824296 target=80
- Driver: **Regulatory / legal risk** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, litigation, regulation, competition, margin, supply chain, cyber, 
- Driver: **Competitive / pricing pressure** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, litigation, regulation, competition, margin, supply chain, cyber, 
- Driver: **Margin / cost headwind** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, litigation, regulation, competition, margin, supply chain, cyber, 
- Driver: **Operational / cyber risk** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, litigation, regulation, competition, margin, supply chain, cyber, 

#### Base — mixed execution

Balanced path: some tailwinds offset headwinds. Operating scale roughly holds with modest repair/normalization; valuation stays near the current EV/EBITDA anchor.

- **Range:** $90.70 – $104.78 (mid $97.74) · EBITDA $456.48M · multiple 24.1x
- Driver: **Manageable leverage** — Net debt / EBITDA ≈ 0.7x — room for reinvestment or returns
- Driver: **Positive free cash flow** — FCF $312.25M
- Driver: **Balance-sheet / refinancing pressure** — sector=Industrials industry=Metal Fabrication revenue=7798480000.0 ebitda=438920000.0 fcf=312249000.0 net_debt=311043000.0 nd_ebitda=0.708655335824296 target=80
- Driver: **Regulatory / legal risk** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, litigation, regulation, competition, margin, supply chain, cyber, 

#### Bull — tailwinds dominate

Tailwinds compound: operating improvement plus a re-rating toward peer or recovery multiples as balance-sheet and growth narratives improve.

- **Range:** $134.19 – $164.64 (mid $149.42) · EBITDA $539.87M · multiple 30.9x
- Driver: **Manageable leverage** — Net debt / EBITDA ≈ 0.7x — room for reinvestment or returns
- Driver: **Positive free cash flow** — FCF $312.25M
- Driver: **Contract / backlog wins** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, litigation, regulation, competition, margin, supply chain, cyber, 
- Driver: **Product / pricing power** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, litigation, regulation, competition, margin, supply chain, cyber, 
- Driver: **Growth / execution upside** — ### Item 1 — Business (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, margin, supply chain,

### Method notes

- Item 1A risks weighted toward headwinds.
- Mapping follows Gemini/Perplexity-style scenario memos: qualitative drivers → operating metric & multiple paths → share-price ranges over a medium-term horizon.

## Web research — web_analysts

- Queries: CMC analyst price target, Commercial Metals Company stock rating OR consensus OR upgrade OR downgrade, CMC Estimate intrinsic value under base / bull / bear scenarios analyst
- Unique hits: 19
- Pages fetched: 2/3

### Web synthesis — web_analysts (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, guidance, revenue, margin, segment, market

- [HIT] CMC Stock Price, Quote & Chart | ChartMill.com | www.chartmill.com | https://www.chartmill.com/stock/quote/CMC/profile 1 month ago - In its latest reported quarter, CMC missed EPS estimates by 11.86% and beat revenue estimates by 0.95%.
- [HIT] Analysts Offer Insights on Industrial Goods Companies: Helios Technologies (HLIO), Commercial Metals Company (CMC) and Emerson Electric Company (EMR) | The Globe and Mail | https://www.theglobeandmail.com/investing/markets/stocks/CMC/pressreleases/3267801/analysts-offer-insights-on-industrial-goods-companies-helios-technologies-hlio-commercial-metals-company-cmc-and-emerson-electric-company-emr/ Detailed price information for Commercial Metals Company (CMC-N) from The Globe and Mail including charting and trades.
- [HIT] Analysts Are Neutral on Top Industrial Goods Stocks: Commercial Metals Company (CMC), Fastenal Company (FAST) | The Globe and Mail | https://www.theglobeandmail.com/investing/markets/markets-news/Tipranks/3319682/analysts-are-neutral-on-top-industrial-goods-stocks-commercial-metals-company-cmc-fastenal-company-fast/ Analysts fell to the sidelines weighing in on Commercial Metals Company (CMC) and Fastenal Company (FAST) with neutral ratings, indicating that the experts are neither bullish nor bearish on the ...
- [HIT] Commercial Metals Company (CMC) stock forecast and price target | Yahoo Finance | https://finance.yahoo.com/research/stock-forecast/CMC/ At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage rates that help you manage your financial life.
- [HIT] Commercial Metals Posts Strong Fiscal Q3 Earnings Surge | The Globe and Mail | https://www.theglobeandmail.com/investing/markets/stocks/CMC/pressreleases/15967/commercial-metals-posts-strong-fiscal-q3-earnings-surge/ Detailed price information for Commercial Metals Company (CMC-N) from The Globe and Mail including charting and trades.
- [HIT] CrowdStrike (CRWD) Stock Forecast and Price Target 2026 | www.marketbeat.com | https://www.marketbeat.com/stocks/NASDAQ/CRWD/forecast/ MarketBeat calculates consensus analyst ratings for stocks using the most recent rating from each Wall Street analyst that has rated a stock within the last twelve months.
- [HIT] Breaking Stock Market & Investing News | Seeking Alpha | seekingalpha.com | https://seekingalpha.com/market-news Breaking news and real-time stock market updates from Seeking Alpha.
- [HIT] Top Stock Reports for Bank of America, Netflix & TotalEnergies | Zacks · via Yahoo Finance | https://finance.yahoo.com/markets/stocks/articles/top-stock-reports-bank-america-201500862.html Bank of America's trading, investment banking and digital expansion drive growth, but rising costs...

### Sources found
- [Commercial Metals (CMC) Stock Forecast, Price Targets and Analysts Predictions - TipRanks.com](https://www.tipranks.com/stocks/cmc/forecast)
  - Based on analyst ratings, Commercial Metals’s 12-month average price target is 76.60. What is CMC’s upside potential, based on the analysts’ average price ta…
- [Commercial Metals (CMC) Stock Forecast: Analyst Ratings, Predictions & Price Target 2026](https://public.com/stocks/cmc/forecast-price-target)
  - This rating is provided by third-party analysts and is not investment advice from Public.com. Wall Street analysts have set a price target of $73.33, reflect…
- [Commercial Metals Company (CMC) Stock Forecast & Price Targets](https://stockanalysis.com/stocks/cmc/forecast/)
  - The 9 analysts that cover Commercial Metals Company stock have a consensus rating of "Strong Buy" and an average price target of $73.33, which forecasts a 3.…
- [CMC Stock Price, Quote & Chart | ChartMill.com](https://www.chartmill.com/stock/quote/CMC/profile)
  - 1 month ago - In its latest reported quarter, CMC missed EPS estimates by 11.86% and beat revenue estimates by 0.95%. ... The average analyst price target fo…
- [Analysts Offer Insights on Industrial Goods Companies: Helios Technologies (HLIO), Commercial Metals Company (CMC) and Emerson Electric Company (EMR)](https://www.theglobeandmail.com/investing/markets/stocks/CMC/pressreleases/3267801/analysts-offer-insights-on-industrial-goods-companies-helios-technologies-hlio-commercial-metals-company-cmc-and-emerson-electric-company-emr/)
  - Detailed price information for Commercial Metals Company (CMC-N) from The Globe and Mail including charting and trades.
- [Analysts Are Neutral on Top Industrial Goods Stocks: Commercial Metals Company (CMC), Fastenal Company (FAST)](https://www.theglobeandmail.com/investing/markets/markets-news/Tipranks/3319682/analysts-are-neutral-on-top-industrial-goods-stocks-commercial-metals-company-cmc-fastenal-company-fast/)
  - Analysts fell to the sidelines weighing in on Commercial Metals Company (CMC) and Fastenal Company (FAST) with neutral ratings, indicating that the experts a…
- [Commercial Metals Company (CMC) stock forecast and price target](https://finance.yahoo.com/research/stock-forecast/CMC/)
  - At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage rate…
- [Commercial Metals Posts Strong Fiscal Q3 Earnings Surge](https://www.theglobeandmail.com/investing/markets/stocks/CMC/pressreleases/15967/commercial-metals-posts-strong-fiscal-q3-earnings-surge/)
  - Detailed price information for Commercial Metals Company (CMC-N) from The Globe and Mail including charting and trades.
- [Which Is a Better Investment, Commercial Metals Company or... | AAII](https://www.aaii.com/investingideas/article/27111-which-is-a-better-investment-commercial-metals-company-or-united-states-steel-corporation-stock)
  - Learn more about whether Commercial Metals Company or United States Steel Corporation is a better investment based on AAII's A+ Investor grades, which compar…
- [CrowdStrike (CRWD) Stock Forecast and Price Target 2026](https://www.marketbeat.com/stocks/NASDAQ/CRWD/forecast/)
  - MarketBeat calculates consensus analyst ratings for stocks using the most recent rating from each Wall Street analyst that has rated a stock within the last …
- [Breaking Stock Market & Investing News | Seeking Alpha](https://seekingalpha.com/market-news)
  - Breaking news and real-time stock market updates from Seeking Alpha. Check out the latest investing news and financial headlines.
- [Up Over 100%: These 2 Monster Growth Stocks Earn an Upgrade](https://finance.yahoo.com/news/over-100-2-monster-growth-170647806.html)
  - Growth investing is a perennially popular strategy – and for good reason. While not all growth stock...

### Search warnings
- news:CMC Estimate intrinsic value under base / bull / bear scenarios analyst: No results found.

## Web research — web_drivers

- Queries: CMC Estimate intrinsic value under base / bull / bear scenarios, Commercial Metals Company CMC outlook OR catalyst OR commodity OR uranium OR rare earth OR vanadium, CMC sector drivers OR market demand
- Unique hits: 16
- Pages fetched: 3/3

### Web synthesis — web_drivers (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, guidance, capex, revenue, margin, market

- | www.marketbeat.com | https://www.marketbeat.com/instant-alerts/what-is-zacks-researchs-forecast-for-cmc-fy2026-earnings-2026-07-27/ 23 hours ago ...
- [HIT] Data centers drive long steel demand: CMC | Latest Market News | www.argusmedia.com | https://www.argusmedia.com/en/news-and-insights/latest-market-news/2806536-data-centers-drive-long-steel-demand-cmc March 27, 2026 - Data center construction drove demand for long steel in the quarter latest quarter, helping US long steel manufacturer Commercial Metals (CMC) widen its margins to a three-year high.
- [HIT] Carboxymethyl Cellulose Market Size, Share & Forecast, 2035 | www.gminsights.com | https://www.gminsights.com/industry-analysis/carboxymethyl-cellulose-cmc-market December 1, 2025 - The increased demand is due to growth in processed foods and cosmetic formulations.
- Asia Pacific carboxymethyl cellulose market accounted for 39.5% market share in 2025 and is anticipated to show lucrative growth over the forecast period.
- [HIT] Carboxymethyl Cellulose (CMC) Market Size & Report 2034 | www.imarcgroup.com | https://www.imarcgroup.com/carboxymethyl-cellulose-market Its high purity ensures consistent ...
- [HIT] Detergent CMC Marke, Global Market Analysis Report - 2036 | www.factmr.com | https://www.factmr.com/report/detergent-cmc-market 2 weeks ago - Ashland, headquartered in Wilmington, Delaware, and CP Kelco, headquartered in Atlanta, Georgia, supply a market where liquid detergent holds about 42% of retail value and pods keep taking volume from powder, steering CMC grades toward liquid-compatible viscosity.
- Germany's CMC demand expands at a 6.1% CAGR from 2026 to 2036, in a market that invented the modern self-acting detergent and still enforces strict surfactant biodegradability rules.
- [HIT] Commercial Metals (CMC) Margin Falls to 0.5% on $368.5M Loss, Undercutting...

### Sources found
- [Bull Base Bear Valuation for One Stock | Model Reef](https://modelreef.io/resources/articles/stock-valuation/how-to-create-a-bull-base-bear-valuation-for-one-stock-scenario-driven-intrinsic-value)
  - Build a bull, base, and bear valuation for one stock with clear drivers, scenario ranges, implied multiples, and decision rules you can defend.
- [Scenario Analysis — How to Model Bull, Base & Bear Cases - equityref.com](https://equityref.com/financial-modeling/scenario-analysis/)
  - Learn how to build scenario analysis in financial models — base, bull, and bear cases, CHOOSE function method, and probability-weighted valuation.
- [Intrinsik — Stock Valuation Tool | Fair Value in 60 Seconds](https://intrinsik.io/)
  - Fair value. Any stock. 60 seconds. Enter a ticker. Intrinsik reads the SEC filings, builds a full DCF model with bear, base & bull scenarios, and delivers in…
- [Intrinsic Value Calculator - Basis Report](https://www.basisreport.com/tools/intrinsic-value-calculator)
  - Calculate intrinsic value for any stock using Graham Number, DCF, and P/E methods. Now with Bull/Base/Bear scenario panel to stress-test your assumptions. Fr…
- [What is Zacks Research's Forecast for CMC FY2026 Earnings?](https://www.marketbeat.com/instant-alerts/what-is-zacks-researchs-forecast-for-cmc-fy2026-earnings-2026-07-27/)
  - 23 hours ago ... Commercial Metals Company (NYSE:CMC - Free Report) - Investment analysts at Zacks Research upped their FY2026 EPS estimates for Commercial ...
- [Commercial Metals (NYSE:CMC) Stock Forecast & Analyst Predictions](https://simplywall.st/stocks/us/materials/nyse-cmc/commercial-metals/future)
  - Jul 15, 2026 ... The consensus outlook for fiscal year 2025 has been updated. 2025 EPS estimate fell from US$1.77 to US$1.42 per share. Revenue forecast stea…
- [Commercial Metals Stock Price Today | NYSE: CMC Live](https://www.investing.com/equities/commercial-metals-comp)
  - Commercial Metals Company News & Analysis. Summarize CMC's latest news. Recent; Analysis; Earnings; Transcripts; Company ... USA Rare Earth. 14.42. USAR. -4.…
- [Analyst Names Top US Metals Stocks Amidst Structural Shift - The Bull](https://thebull.com.au/us-news/analyst-names-top-us-metals-stocks-amidst-structural-shift/)
  - May 22, 2026 ... ... rare earth magnet consumption. Freeport-McMoRan received an ... CMCCommercial Metals Company. $67.70. 0.00%. $7.49B. 0.25. LUN.TO ...
- [Data centers drive long steel demand: CMC | Latest Market News](https://www.argusmedia.com/en/news-and-insights/latest-market-news/2806536-data-centers-drive-long-steel-demand-cmc)
  - March 27, 2026 - Data center construction drove demand for long steel in the quarter latest quarter, helping US long steel manufacturer Commercial Metals (CM…
- [Carboxymethyl Cellulose Market Size, Share & Forecast, 2035](https://www.gminsights.com/industry-analysis/carboxymethyl-cellulose-cmc-market)
  - December 1, 2025 - The increased demand is due to growth in processed foods and cosmetic formulations. Asia Pacific carboxymethyl cellulose market accounted …
- [Carboxymethyl Cellulose (CMC) Market Size & Report 2034](https://www.imarcgroup.com/carboxymethyl-cellulose-market)
  - Its high purity ensures consistent ... drug formulations, food additives, and high-end cosmetics. The demand for high-quality, reliable ingredients in these …
- [Detergent CMC Marke, Global Market Analysis Report - 2036](https://www.factmr.com/report/detergent-cmc-market)
  - 2 weeks ago - Ashland, headquartered in Wilmington, Delaware, and CP Kelco, headquartered in Atlanta, Georgia, supply a market where liquid detergent holds a…

### Search warnings
- news:CMC Estimate intrinsic value under base / bull / bear scenarios: No results found.
- news:Commercial Metals Company CMC outlook OR catalyst OR commodity OR uranium OR rare earth OR vanadium: No results found.

## SEC filing [S25]
- Extraction OK: True
- Item 1 chars: 45984
- Item 1A chars: 50000
- Item 7 chars: 50000
- Meta: {'source': 'cache', 'path': 'C:\\DevWork\\equity_research_agent\\data\\filings\\CMC_10k.txt'}

## Company setup & business model

**Keyword hits:** risk, uncertainty, litigation, regulation, competition, margin, supply chain, customer, segment, product, service, market, operations, network

- DISCLOSURE REGARDING FORWARD-LOOKING STATEMENTS  This annual report on Form 10-K (hereinafter referred to as the "Annual Report") contains forward-looking statements within the meaning of Section 27A of the Securities Act of 1933, as amended (the "Securities Act"), Section 21E of the Securities Exchange Act of 1934, as amended (the "Exchange Act") and the Private Securities Litigation Reform Act of 1995.
- Actual results, performance or achievements could differ materially from those projected in the forward-looking statements as a result of a  number of risks, uncertainties and other factors.
- For a discussion of important factors that could cause our results, performance or achievements to differ materially from any future results, performance or achievements expressed or implied by our forward-looking statements, please refer to Part I, Item 1A, Risk Factors and Part II, Item 7, Management's Discussion and Analysis of Financial Condition and Results of Operations in this Annual Report.
- Certain trademarks or service marks of CMC appearing in this Annual Report are the property of CMC and are protected under applicable intellectual property laws.
- Today, through an extensive manufacturing network principally located in the United States ("U.S.") and Central Europe, we offer products and technologies to meet the critical reinforcement needs of the global construction sector.
- Our operations are conducted through three reportable segments: North America Steel Group, Emerging Businesses Group and Europe Steel Group.
- At CMC, we believe "it’s what’s inside that counts." This reflects the nature of our products, which are found in critical infrastructure worldwide, and also applies to our culture and employees.
- We operate under the guiding principles of placing the customer at the core of all we do, staying committed to our employees, giving back to our communities and creating value for our investors, all while continuing our commitment to sustainability.
- From our inception, our business model has been  strategically built on sustainable principles, including recycling metals, manufacturing products from approximately 98% recycled material using energy-efficient technology and employing closed-loop water recycling processes.
- We provide differentiating value for our customers through our industry-leading customer service with a low cost, high-quality production process.
- Further, we have achieved market leadership through our commitment to transformation, advancement and long-term growth by investing in our business and in our people.
- As our customers' needs and preferences have evolved, our products have expanded to include diverse and innovative solutions and future growth platforms.
- Through a combination of both value-accretive organic growth that captures available internal synergies, and capability-enhancing inorganic growth that broadens our portfolio, we aim to provide our customers with a comprehensive solution.
- Segments  The Company has three reportable segments that represent the primary businesses reported in our consolidated financial statements: North America Steel Group, Emerging Businesses Group and Europe Steel Group.
- The following chart summarizes net sales to external customers by major product category within each reportable segment during the year ended August 31, 2025.
- For a historical breakout of our net sales to external customers by major product category within each reportable segment, see Note  19, Segment Information, in Part II, Item 8 of this Annual Report.
- Sales by product.jpg  NORTH AMERICA STEEL GROUP SEGMENT  Our North America Steel Group segment provides a diverse offering of products and solutions to support the construction sector.
- Composed of a vertically integrated network of recycling facilities, steel mills and fabrication operations, our strategy in North America is to optimize our vertically integrated value chain to maximize profitability while providing industry-leading customer service.
- To execute our strategy, we seek to (i) obtain inputs at the lowest possible cost, including materials  procured from our recycling facilities, which are operated to provide low-cost scrap to our steel mills, (ii) operate modern, efficient electric arc furnace ("EAF") steel mills and (iii) enhance operational efficiency by utilizing our fabrication operations to optimize our steel mill volumes and obtain the highest possible selling prices to maximize metal margin.
- We strive to maximize cash flow generation through increased productivity, high-capacity utilization and optimal product mix.
- We have invested approximately 80%, 77% and 88% of total capital expenditures in our North America Steel Group segment during 2025, 2024 and 2023, respectively.
- Raw materials margin per ton is defined as the difference between the selling prices for processed and recycled ferrous and nonferrous  scrap metals and the price paid to purchase obsolete and industrial scrap.
- Our steel mill operations consist of six EAF mini mills, three EAF micro mills and one rerolling mill.
- Our steel mills manufacture finished long steel products including rebar, merchant bar, light structural and other special sections and wire rod, as well as semi-finished billets for rerolling and forging applications (collectively referred to as "steel products" in the context of the North America Steel Group segment).
- Each EAF mini mill consists of:  • a melt shop with an EAF;  • continuous casting equipment that shapes molten metal into billets;  • a reheating furnace that prepares billets for rolling;  • a rolling line that forms products from heated billets;  • a mechanical cooling bed that receives hot products from the rolling line;  • finishing facilities that shear, straighten, bundle and prepare products for shipping;  • baghouse systems that control particulate emissions from steelmaking operations; and  • supporting facilities such as maintenance, warehouse and office areas.
- Our EAF micro mills utilize similar equipment and processes as described above; however, these facilities utilize unique continuous process technology where metal flows uninterrupted from melting to casting to rolling into finished steel products.
- Our rerolling mill does not utilize a melt shop; the rerolling process begins by reheating billets to roll into finished steel products.
- The est imated annual  capacity for our steel mills, included in Part I, Item 2, Properties, of this Annual Report assumes a typical product mix and is not necessarily indicative of the expected production volumes or shipments in any fiscal year.

_Source: latest 10-K Item 1 (Business), summarized locally._

## Qualitative analysis (local LLM)

### Item 1 — Business (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, uncertainty, litigation, regulation, competition, margin, supply chain, customer, segment, product, service, market, operations, network

- DISCLOSURE REGARDING FORWARD-LOOKING STATEMENTS  This annual report on Form 10-K (hereinafter referred to as the "Annual Report") contains forward-looking statements within the meaning of Section 27A of the Securities Act of 1933, as amended (the "Securities Act"), Section 21E of the Securities Exchange Act of 1934, as amended (the "Exchange Act") and the Private Securities Litigation Reform Act of 1995.
- Actual results, performance or achievements could differ materially from those projected in the forward-looking statements as a result of a  number of risks, uncertainties and other factors.
- For a discussion of important factors that could cause our results, performance or achievements to differ materially from any future results, performance or achievements expressed or implied by our forward-looking statements, please refer to Part I, Item 1A, Risk Factors and Part II, Item 7, Management's Discussion and Analysis of Financial Condition and Results of Operations in this Annual Report.
- Certain trademarks or service marks of CMC appearing in this Annual Report are the property of CMC and are protected under applicable intellectual property laws.
- Today, through an extensive manufacturing network principally located in the United States ("U.S.") and Central Europe, we offer products and technologies to meet the critical reinforcement needs of the global construction sector.
- Our operations are conducted through three reportable segments: North America Steel Group, Emerging Businesses Group and Europe Steel Group.
- At CMC, we believe "it’s what’s inside that counts." This reflects the nature of our products, which are found in critical infrastructure worldwide, and also applies to our culture and employees.
- We operate under the guiding principles of placing the customer at the core of all we do, staying committed to our employees, giving back to our communities and creating value for our investors, all while continuing our commitment to sustainability.
- From our inception, our business model has been  strategically built on sustainable principles, including recycling metals, manufacturing products from approximately 98% recycled material using energy-efficient technology and employing closed-loop water recycling processes.
- We provide differentiating value for our customers through our industry-leading customer service with a low cost, high-quality production process.
- Further, we have achieved market leadership through our commitment to transformation, advancement and long-term growth by investing in our business and in our people.
- As our customers' needs and preferences have evolved, our products have expanded to include diverse and innovative solutions and future growth platforms.
- Through a combination of both value-accretive organic growth that captures available internal synergies, and capability-enhancing inorganic growth that broadens our portfolio, we aim to provide our customers with a comprehensive solution.
- Segments  The Company has three reportable segments that represent the primary businesses reported in our consolidated financial statements: North America Steel Group, Emerging Businesses Group and Europe Steel Group.
- The following chart summarizes net sales to external customers by major product category within each reportable segment during the year ended August 31, 2025.
- For a historical breakout of our net sales to external customers by major product category within each reportable segment, see Note  19, Segment Information, in Part II, Item 8 of this Annual Report.
- Sales by product.jpg  NORTH AMERICA STEEL GROUP SEGMENT  Our North America Steel Group segment provides a diverse offering of products and solutions to support the construction sector.
- Composed of a vertically integrated network of recycling facilities, steel mills and fabrication operations, our strategy in North America is to optimize our vertically integrated value chain to maximize profitability while providing industry-leading customer service.
- To execute our strategy, we seek to (i) obtain inputs at the lowest possible cost, including materials  procured from our recycling facilities, which are operated to provide low-cost scrap to our steel mills, (ii) operate modern, efficient electric arc furnace ("EAF") steel mills and (iii) enhance operational efficiency by utilizing our fabrication operations to optimize our steel mill volumes and obtain the highest possible selling prices to maximize metal margin.
- We strive to maximize cash flow generation through increased productivity, high-capacity utilization and optimal product mix.
- We have invested approximately 80%, 77% and 88% of total capital expenditures in our North America Steel Group segment during 2025, 2024 and 2023, respectively.
- Raw materials margin per ton is defined as the difference between the selling prices for processed and recycled ferrous and nonferrous  scrap metals and the price paid to purchase obsolete and industrial scrap.
- Our steel mill operations consist of six EAF mini mills, three EAF micro mills and one rerolling mill.
- Our steel mills manufacture finished long steel products including rebar, merchant bar, light structural and other special sections and wire rod, as well as semi-finished billets for rerolling and forging applications (collectively referred to as "steel products" in the context of the North America Steel Group segment).
- Each EAF mini mill consists of:  • a melt shop with an EAF;  • continuous casting equipment that shapes molten metal into billets;  • a reheating furnace that prepares billets for rolling;  • a rolling line that forms products from heated billets;  • a mechanical cooling bed that receives hot products from the rolling line;  • finishing facilities that shear, straighten, bundle and prepare products for shipping;  • baghouse systems that control particulate emissions from steelmaking operations; and  • supporting facilities such as maintenance, warehouse and office areas.
- Our EAF micro mills utilize similar equipment and processes as described above; however, these facilities utilize unique continuous process technology where metal flows uninterrupted from melting to casting to rolling into finished steel products.
- Our rerolling mill does not utilize a melt shop; the rerolling process begins by reheating billets to roll into finished steel products.
- The est imated annual  capacity for our steel mills, included in Part I, Item 2, Properties, of this Annual Report assumes a typical product mix and is not necessarily indicative of the expected production volumes or shipments in any fiscal year.


### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, litigation, regulation, competition, margin, supply chain, cyber, interest rate, customer, segment, product, service, market, operations, network

- There are inherent risks and uncertainties associated with our business that could adversely affect our business, results of operations and financial condition.
- Set forth below are descriptions of those risks and uncertainties that we currently believe to be material, but the risks and uncertainties described below are not the only risks and uncertainties that could adversely affect our business, results of operations and financial condition.
- If any of these risks actually occur, our business,  results of operations and financial condition could be materially adversely affected.
- RISKS RELATED TO OUR BUSINESS  Scrap and other inputs for our business are subject to significant price fluctuations and limited availability, which may adversely affect our business, results of operations and financial condition.
- We depend on ferrous scrap, the primary raw material used by our steel mills, and other inputs such as graphite electrodes and alloys for our steel mill operations.
- The price of scrap and other inputs has historically been subject to significant fluctuation, and we may not be able to adjust our product prices to recover the costs of rapid increases in raw  material prices, especially over the short-term and in our fixed price contracts.
- The profitability of our operations would be adversely affected if we are unable to pass increased raw material and input costs on to our customers.
- A prolonged period of low scrap prices or a fall in scrap prices could impair our ability to obtain, process, sell and consume  recycled material, which could have a material adverse effect on our business, results of operations and financial condition.


### Item 7 — MD&A (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, uncertainty, litigation, regulation, revenue, margin, interest rate, customer, segment, product, service, market, operations, network

- AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERATIONS  This Management's Discussion and Analysis of Financial Condition and Results of Operations should be read in conjunction with our consolidated financial statements and the accompanying notes contained in this Annual Report.
- Our discussion and analysis of fiscal year 2024 compared to fiscal year 2023 can be found in Part II, Item 7, Management's Discussion and Analysis of Financial Condition and  Results of Operations, in our Annual Report on Form 10-K for the year ended August 31, 2024, which was filed with the SEC on October 17, 2024.
- Today, through an extensive manufacturing network principally located in the U.S.
- and Central Europe, the Company offers products and technologies to meet the critical reinforcement needs of the global construction sector.
- Our operations are conducted through three reportable segments: North America Steel Group, Emerging Businesses Group and Europe Steel Group.
- See Part I, Item 1, Business, of this Annual Report for further information regarding our business and reportable segments.
- Key Performance Indicators  When evaluating our results, we compare net sales, in the aggregate and for each of our reportable segments, in the current period to net sales in the corresponding period.
- For the North America Steel Group and the Europe Steel Group segments, we focus on changes in average selling price per ton and tons shipped compared to the corresponding period for each of our vertically integrated product categories as these are the two variables that typically have the greatest impact on our net sales for  those reportable segments.


## Research loop (think → act)

1. _heuristic_ — Coverage looks adequate for this pass; stopping iterative loop.

## Sources

- **[S1]** CMC fundamentals (yfinance)
  - Commercial Metals Company: price=68.04, rev=7798480000.0, fcf=312249000.0, shares=109528048.0, rev_cagr=-0.04356776135013685, ROIC=0.033978529382836874, FCF yield=None
- **[S2]** CMC DCF valuation (dcf)
  - Base share price=42.30738539488079, bull=138.43786429322256, bear=9.295473994309154
- **[S3]** CMC EV/EBITDA valuation (multiples)
  - Base implied price=93.86835890656975, multiple=24.13255518089857
- **[S4]** Commercial Metals (CMC) Stock Forecast, Price Targets and Analysts Predictions - TipRanks.com (web) — https://www.tipranks.com/stocks/cmc/forecast
  - Based on analyst ratings, Commercial Metals’s 12-month average price target is 76.60. What is CMC’s upside potential, based on the analysts’ average price target?
- **[S5]** Commercial Metals (CMC) Stock Forecast: Analyst Ratings, Predictions & Price Target 2026 (web) — https://public.com/stocks/cmc/forecast-price-target
  - This rating is provided by third-party analysts and is not investment advice from Public.com. Wall Street analysts have set a price target of $73.33, reflecting a 0.00% increase…
- **[S6]** Commercial Metals Company (CMC) Stock Forecast & Price Targets (web) — https://stockanalysis.com/stocks/cmc/forecast/
  - The 9 analysts that cover Commercial Metals Company stock have a consensus rating of "Strong Buy" and an average price target of $73.33, which forecasts a 3.98% increase in the …
- **[S7]** CMC Stock Price, Quote & Chart | ChartMill.com (web) — https://www.chartmill.com/stock/quote/CMC/profile
  - 1 month ago - In its latest reported quarter, CMC missed EPS estimates by 11.86% and beat revenue estimates by 0.95%. ... The average analyst price target for CMC is 79.92 USD, …
- **[S8]** Analysts Offer Insights on Industrial Goods Companies: Helios Technologies (HLIO), Commercial Metals Company (CMC) and Emerson Electric Company (EMR) (web) — https://www.theglobeandmail.com/investing/markets/stocks/CMC/pressreleases/3267801/analysts-offer-insights-on-industrial-goods-companies-helios-technologies-hlio-commercial-metals-company-cmc-and-emerson-electric-company-emr/
  - Detailed price information for Commercial Metals Company (CMC-N) from The Globe and Mail including charting and trades.
- **[S9]** Analysts Are Neutral on Top Industrial Goods Stocks: Commercial Metals Company (CMC), Fastenal Company (FAST) (web) — https://www.theglobeandmail.com/investing/markets/markets-news/Tipranks/3319682/analysts-are-neutral-on-top-industrial-goods-stocks-commercial-metals-company-cmc-fastenal-company-fast/
  - Analysts fell to the sidelines weighing in on Commercial Metals Company (CMC) and Fastenal Company (FAST) with neutral ratings, indicating that the experts are neither bullish n…
- **[S10]** Commercial Metals Company (CMC) stock forecast and price target (web) — https://finance.yahoo.com/research/stock-forecast/CMC/
  - At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage rates that help you mana…
- **[S11]** Commercial Metals Posts Strong Fiscal Q3 Earnings Surge (web) — https://www.theglobeandmail.com/investing/markets/stocks/CMC/pressreleases/15967/commercial-metals-posts-strong-fiscal-q3-earnings-surge/
  - Detailed price information for Commercial Metals Company (CMC-N) from The Globe and Mail including charting and trades.
- **[S12]** Commercial Metals (CMC) Stock Forecast: Analyst Ratings, Predictions & Price Target 2026 (web_page) — https://public.com/stocks/cmc/forecast-price-target
  - Commercial Metals (CMC) Stock Forecast: Analyst Ratings, Predictions & Price Target 2026 Skip to main About CMC Options chain Market cap P/E ratio Forecast Earnings News Pre-mar…
- **[S13]** Commercial Metals Company (CMC) Stock Forecast & Price Targets (web_page) — https://stockanalysis.com/stocks/cmc/forecast/
  - Commercial Metals Company (CMC) Stock Forecast & Price Targets Collapse Commercial Metals Company (CMC) NYSE: CMC · Real-Time Price · USD Full Chart Watchlist Alerts Compare 68.…
- **[S14]** Bull Base Bear Valuation for One Stock | Model Reef (web) — https://modelreef.io/resources/articles/stock-valuation/how-to-create-a-bull-base-bear-valuation-for-one-stock-scenario-driven-intrinsic-value
  - Build a bull, base, and bear valuation for one stock with clear drivers, scenario ranges, implied multiples, and decision rules you can defend.
- **[S15]** Scenario Analysis — How to Model Bull, Base & Bear Cases - equityref.com (web) — https://equityref.com/financial-modeling/scenario-analysis/
  - Learn how to build scenario analysis in financial models — base, bull, and bear cases, CHOOSE function method, and probability-weighted valuation.
- **[S16]** Intrinsik — Stock Valuation Tool | Fair Value in 60 Seconds (web) — https://intrinsik.io/
  - Fair value. Any stock. 60 seconds. Enter a ticker. Intrinsik reads the SEC filings, builds a full DCF model with bear, base & bull scenarios, and delivers intrinsic value — auto…
- **[S17]** Intrinsic Value Calculator - Basis Report (web) — https://www.basisreport.com/tools/intrinsic-value-calculator
  - Calculate intrinsic value for any stock using Graham Number, DCF, and P/E methods. Now with Bull/Base/Bear scenario panel to stress-test your assumptions. Free, no signup.
- **[S18]** What is Zacks Research's Forecast for CMC FY2026 Earnings? (web) — https://www.marketbeat.com/instant-alerts/what-is-zacks-researchs-forecast-for-cmc-fy2026-earnings-2026-07-27/
  - 23 hours ago ... Commercial Metals Company (NYSE:CMC - Free Report) - Investment analysts at Zacks Research upped their FY2026 EPS estimates for Commercial ...
- **[S19]** Commercial Metals (NYSE:CMC) Stock Forecast & Analyst Predictions (web) — https://simplywall.st/stocks/us/materials/nyse-cmc/commercial-metals/future
  - Jul 15, 2026 ... The consensus outlook for fiscal year 2025 has been updated. 2025 EPS estimate fell from US$1.77 to US$1.42 per share. Revenue forecast steady ...
- **[S20]** Commercial Metals Stock Price Today | NYSE: CMC Live (web) — https://www.investing.com/equities/commercial-metals-comp
  - Commercial Metals Company News & Analysis. Summarize CMC's latest news. Recent; Analysis; Earnings; Transcripts; Company ... USA Rare Earth. 14.42. USAR. -4.79% ...
- **[S21]** Analyst Names Top US Metals Stocks Amidst Structural Shift - The Bull (web) — https://thebull.com.au/us-news/analyst-names-top-us-metals-stocks-amidst-structural-shift/
  - May 22, 2026 ... ... rare earth magnet consumption. Freeport-McMoRan received an ... CMCCommercial Metals Company. $67.70. 0.00%. $7.49B. 0.25. LUN.TO ...
- **[S22]** Bull Base Bear Valuation for One Stock | Model Reef (web_page) — https://modelreef.io/resources/articles/stock-valuation/how-to-create-a-bull-base-bear-valuation-for-one-stock-scenario-driven-intrinsic-value
  - Bull Base Bear Valuation for One Stock | Model Reef Back Published February 13, 2026 in For Teams Table of Contents Bull/Base/Bear Valuation Before You Begin Step-by-Step Implem…
- **[S23]** Scenario Analysis — How to Model Bull, Base & Bear Cases - equityref.com (web_page) — https://equityref.com/financial-modeling/scenario-analysis/
  - Scenario Analysis — How to Model Bull, Base & Bear Cases - equityref.com Scenario Analysis — How to Model Bull, Base & Bear Cases Scenario Analysis Scenario analysis tests how c…
- **[S24]** Intrinsik — Free Stock Valuation Tool | DCF Analysis & Fair Value Calculator (web_page) — https://intrinsik.io/
  - Intrinsik — Free Stock Valuation Tool | DCF Analysis & Fair Value Calculator
- **[S25]** CMC 10-K (sec)
  - Item 1 chars=45984, Item 1A chars=50000, Item 7 chars=50000, ok=True, source=cache
- **[S26]** Item 1 Business summary (nlp)
  - ### Item 1 — Business (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, margin, supply chain, customer, segmen…
- **[S27]** Item 1A summary (nlp)
  - ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, litigation, regulation, competition, margin, supply chain, cyber, interest rate, cu…
- **[S28]** Item 7 summary (nlp)
  - ### Item 7 — MD&A (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, revenue, margin, interest rate, customer, segment, prod…
- **[S29]** CMC scenario price ranges (scenarios)
  - ok=True; base mid=97.73668717989023; headwinds=5; tailwinds=7

## Self-critique

_Automated review (heuristic)._

### Strengths
- Combines local fundamentals, optional DCF scenarios, and cited sources where available.
- Keeps a non-advisory framing for local research drafts.

### Issues & gaps
- Draft uses strong recommendation language; this local agent should stay descriptive, not advisory.

### Caution for readers
- Treat scenario prices as sensitivity output, not a forecast.
- Re-check primary filings and fresh market data before any decision.



---

# Template: Full diligence (`deep`)

# CMC — Planned Research Report

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
- Company: Commercial Metals Company
- Sector / industry: Industrials / Metal Fabrication
- Price: 68.04
- 52-week range: $49.66 – $84.87
- Market cap: —
- Enterprise value: $10.59B
- Shares outstanding: 109.53M
- Beta: 1.532
- Book equity: $4.19B
- Revenue (latest): $7.80B
- EBITDA (latest): $438.92M
- Free cash flow (latest): $312.25M
- Operating income: $519.92M
- Operating margin: 6.7%
- EV / EBITDA: 24.1x
- ROIC: 3.4%
- FCF yield: —
- Debt / Equity: 0.32298442237732483
- FCF / share: $2.85
- Revenue / share: $71.20

### Capital structure
- Cash: $1.04B
- Short-term debt: $44.29M
- Long-term debt: $1.31B
- Total debt: $1.35B
- Net debt: $311.04M
- Net debt / EBITDA: 0.7x

### Growth
- Revenue CAGR: -4.4%
- FCF CAGR: 7.6%
- Latest revenue YoY: -1.6%
- Latest FCF YoY: -45.7%

### Market expectations (yfinance, sparse)
- Mean target: $80.09
- Target range: $75.00 – $88.00
- Recommendation: buy

_Consensus revenue/EBITDA forecasts are often unavailable via free feeds; treat targets as point-in-time only._

### Historical KPIs (multi-year)

| Year | Revenue | OCF | Capex | FCF | EBITDA | LT debt | Cash | Net debt | Net income |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2025 | $7.80B | $715.07M | $402.82M | $312.25M | $438.92M | $1.31B | $1.04B | $266.75M | $84.66M |
| 2024 | $7.93B | $899.71M | $324.27M | $575.44M | $963.93M | $1.15B | $857.92M | $292.91M | $485.49M |
| 2023 | $8.80B | $1.34B | $606.66M | $737.44M | $1.38B | $1.11B | $592.33M | $521.95M | $859.76M |
| 2022 | $8.91B | $700.31M | $449.99M | $250.32M | $1.74B | $1.11B | $672.60M | $440.65M | $1.22B |

## Charts

### Revenue & FCF history
![Revenue & FCF history](/charts/CMC_deep_revenue_fcf.png)

### DCF scenario prices
![DCF scenario prices](/charts/CMC_deep_dcf_scenarios.png)

### Base-case FCF path
![Base-case FCF path](/charts/CMC_deep_base_fcf_path.png)

## DCF valuation (base / bull / bear) [S2]

> Simplified revenue->FCF DCF. Not investment advice; assumptions are editable heuristics.

- Spot price: $68.04
- Base revenue: $7.80B
- Shares: 109,528,048
- Net debt (Debt−Cash): $311.04M

| Scenario | Growth | FCF margin | WACC | Term. g | Equity value | Share price | Upside |
|----------|--------|------------|------|---------|--------------|-------------|--------|
| bear | -1.6% | 2.0% | 12.0% | 1.5% | $1.02B | $9.30 | -86.3% |
| base | 6.0% | 4.0% | 10.0% | 2.5% | $4.63B | $42.31 | -37.8% |
| bull | 15.0% | 7.0% | 9.0% | 3.0% | $15.16B | $138.44 | 103.5% |

### Assumption notes
- Base revenue growth seeded from historical rate (-1.6%).
- Recent revenue declined (-1.6% YoY); base/bull use normalized mid-cycle growth instead of extrapolating the decline.


### Base-case projected FCF

- Year 1: revenue $8.27B, FCF $330.98M (PV $300.89M)
- Year 2: revenue $8.76B, FCF $350.84M (PV $289.95M)
- Year 3: revenue $9.29B, FCF $371.89M (PV $279.41M)
- Year 4: revenue $9.85B, FCF $394.21M (PV $269.25M)
- Year 5: revenue $10.44B, FCF $417.86M (PV $259.46M)
- Terminal value $5.71B (PV $3.55B)

## Web research — web_research

- Queries: Deep diligence: fundamentals, DCF, web, 10-K risks & MD&A
- Unique hits: 4
- Pages fetched: 3/3

### Web synthesis — web_research (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, capex, revenue, margin, supply chain, customer, segment, product, service, market, operations, network

- Market Sentiment & Analyst Coverage · Main sources: 10K, 10Q, Investors Day report, earnings call transcript, company’s website, financial data providers (TIKR terminal, Seeking Alpha)  [HIT] How to Conduct Financial Due Diligence + Checklist | dealroom.net | https://dealroom.net/blog/how-to-conduct-financial-due-diligence 2 weeks ago - Think of financial due diligence as a deep investigation into a company’s financial statements—its income statement, balance sheet, and cash flow reports.
- Master the M&A Full Due Diligence course that prepares you to analyze, evaluate, and manage every risk in the merger acquisition due diligence process!
- [PAGE] Due Diligence: Types and How to Perform | https://www.investopedia.com/terms/d/duediligence.asp Due Diligence: Types and How to Perform ​ Top Stories Average Retirement Savings for a 75 Year Old Your Wealth Depends on the Stock Market More Than Ever Generational Divides Over Retirement Preparedness 21 Top Floriday Retirement Locations Table of Contents Expand Table of Contents What Is Due Diligence?
- Due diligence refers to the thorough research and evaluation carried out to confirm the accuracy of information and assess any potential risks before committing to a transaction, agreement, or important decision.
- Key Takeaways Due diligence is a systematic way to analyze and mitigate risk from a business or investment decision.
- Due diligence is applied in many other contexts, for example, conducting a background check on a potential employee or reading product reviews.
- Context-Specific Due Diligence Commercial due diligence considers a company's market share and competitive positioning, including its future prospects and growth opportunities.
- This will consider the company's supply chain from vendors to customers, market analysis, sales pipeline, and R&D pipeline.

### Sources found
- [Due Diligence: Types and How to Perform](https://www.investopedia.com/terms/d/duediligence.asp)
  - May 21, 2025 - Hard due diligence is concerned with the numbers and data found on the financial statements, like the balance sheet and income statement. This…
- [DCF Due Diligence: A Step-by-Step Guide for Company Valuation - BlackNote Investment](https://blacknoteinvestment.com/dcf-due-diligence-guide/)
  - June 13, 2024 - To help investors and professional analysts in their jobs we draw up a must-follow guide that thoroughly covers every crucial aspect of due d…
- [How to Conduct Financial Due Diligence + Checklist](https://dealroom.net/blog/how-to-conduct-financial-due-diligence)
  - 2 weeks ago - Think of financial due diligence as a deep investigation into a company’s financial statements—its income statement, balance sheet, and cash fl…
- [DCF Sensitivity Analysis: 3 Powerful Scenario Tables](https://mnainstitute.com/dcf-sensitivity-analysis-scenario/)
  - June 17, 2026 - Second, each scenario must be commercially believable. Master the M&A Full Due Diligence course that prepares you to analyze, evaluate, and m…

### Search warnings
- news:Deep diligence: fundamentals, DCF, web, 10-K risks & MD&A: No results found.

## Put opportunities (heuristic) [S3]
- Expiration: 2026-09-18 (DTE 52)
- Candidates: 0
- ATM IV (est.): 2.0%
- IV rank: — (1 local samples)
- HV rank (20d realized): 64.6%


_Note: Delta band approximated via % OTM when greeks are unavailable; IV rank needs ~20+ local daily IV samples (have 1); run the options screen over time to build history.; HV rank is realized-vol rank (20d HV vs ~1y); useful when IV history is thin._

## SEC filing [S11]
- Extraction OK: True
- Item 1 chars: 45984
- Item 1A chars: 50000
- Item 7 chars: 50000
- Meta: {'source': 'cache', 'path': 'C:\\DevWork\\equity_research_agent\\data\\filings\\CMC_10k.txt'}

## Company setup & business model

**Keyword hits:** risk, uncertainty, litigation, regulation, competition, margin, supply chain, customer, segment, product, service, market, operations, network

- DISCLOSURE REGARDING FORWARD-LOOKING STATEMENTS  This annual report on Form 10-K (hereinafter referred to as the "Annual Report") contains forward-looking statements within the meaning of Section 27A of the Securities Act of 1933, as amended (the "Securities Act"), Section 21E of the Securities Exchange Act of 1934, as amended (the "Exchange Act") and the Private Securities Litigation Reform Act of 1995.
- Actual results, performance or achievements could differ materially from those projected in the forward-looking statements as a result of a  number of risks, uncertainties and other factors.
- For a discussion of important factors that could cause our results, performance or achievements to differ materially from any future results, performance or achievements expressed or implied by our forward-looking statements, please refer to Part I, Item 1A, Risk Factors and Part II, Item 7, Management's Discussion and Analysis of Financial Condition and Results of Operations in this Annual Report.
- Certain trademarks or service marks of CMC appearing in this Annual Report are the property of CMC and are protected under applicable intellectual property laws.
- Today, through an extensive manufacturing network principally located in the United States ("U.S.") and Central Europe, we offer products and technologies to meet the critical reinforcement needs of the global construction sector.
- Our operations are conducted through three reportable segments: North America Steel Group, Emerging Businesses Group and Europe Steel Group.
- At CMC, we believe "it’s what’s inside that counts." This reflects the nature of our products, which are found in critical infrastructure worldwide, and also applies to our culture and employees.
- We operate under the guiding principles of placing the customer at the core of all we do, staying committed to our employees, giving back to our communities and creating value for our investors, all while continuing our commitment to sustainability.
- From our inception, our business model has been  strategically built on sustainable principles, including recycling metals, manufacturing products from approximately 98% recycled material using energy-efficient technology and employing closed-loop water recycling processes.
- We provide differentiating value for our customers through our industry-leading customer service with a low cost, high-quality production process.
- Further, we have achieved market leadership through our commitment to transformation, advancement and long-term growth by investing in our business and in our people.
- As our customers' needs and preferences have evolved, our products have expanded to include diverse and innovative solutions and future growth platforms.
- Through a combination of both value-accretive organic growth that captures available internal synergies, and capability-enhancing inorganic growth that broadens our portfolio, we aim to provide our customers with a comprehensive solution.
- Segments  The Company has three reportable segments that represent the primary businesses reported in our consolidated financial statements: North America Steel Group, Emerging Businesses Group and Europe Steel Group.
- The following chart summarizes net sales to external customers by major product category within each reportable segment during the year ended August 31, 2025.
- For a historical breakout of our net sales to external customers by major product category within each reportable segment, see Note  19, Segment Information, in Part II, Item 8 of this Annual Report.
- Sales by product.jpg  NORTH AMERICA STEEL GROUP SEGMENT  Our North America Steel Group segment provides a diverse offering of products and solutions to support the construction sector.
- Composed of a vertically integrated network of recycling facilities, steel mills and fabrication operations, our strategy in North America is to optimize our vertically integrated value chain to maximize profitability while providing industry-leading customer service.
- To execute our strategy, we seek to (i) obtain inputs at the lowest possible cost, including materials  procured from our recycling facilities, which are operated to provide low-cost scrap to our steel mills, (ii) operate modern, efficient electric arc furnace ("EAF") steel mills and (iii) enhance operational efficiency by utilizing our fabrication operations to optimize our steel mill volumes and obtain the highest possible selling prices to maximize metal margin.
- We strive to maximize cash flow generation through increased productivity, high-capacity utilization and optimal product mix.
- We have invested approximately 80%, 77% and 88% of total capital expenditures in our North America Steel Group segment during 2025, 2024 and 2023, respectively.
- Raw materials margin per ton is defined as the difference between the selling prices for processed and recycled ferrous and nonferrous  scrap metals and the price paid to purchase obsolete and industrial scrap.
- Our steel mill operations consist of six EAF mini mills, three EAF micro mills and one rerolling mill.
- Our steel mills manufacture finished long steel products including rebar, merchant bar, light structural and other special sections and wire rod, as well as semi-finished billets for rerolling and forging applications (collectively referred to as "steel products" in the context of the North America Steel Group segment).
- Each EAF mini mill consists of:  • a melt shop with an EAF;  • continuous casting equipment that shapes molten metal into billets;  • a reheating furnace that prepares billets for rolling;  • a rolling line that forms products from heated billets;  • a mechanical cooling bed that receives hot products from the rolling line;  • finishing facilities that shear, straighten, bundle and prepare products for shipping;  • baghouse systems that control particulate emissions from steelmaking operations; and  • supporting facilities such as maintenance, warehouse and office areas.
- Our EAF micro mills utilize similar equipment and processes as described above; however, these facilities utilize unique continuous process technology where metal flows uninterrupted from melting to casting to rolling into finished steel products.
- Our rerolling mill does not utilize a melt shop; the rerolling process begins by reheating billets to roll into finished steel products.
- The est imated annual  capacity for our steel mills, included in Part I, Item 2, Properties, of this Annual Report assumes a typical product mix and is not necessarily indicative of the expected production volumes or shipments in any fiscal year.

_Source: latest 10-K Item 1 (Business), summarized locally._

## Qualitative analysis (local LLM)

### Item 1 — Business (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, uncertainty, litigation, regulation, competition, margin, supply chain, customer, segment, product, service, market, operations, network

- DISCLOSURE REGARDING FORWARD-LOOKING STATEMENTS  This annual report on Form 10-K (hereinafter referred to as the "Annual Report") contains forward-looking statements within the meaning of Section 27A of the Securities Act of 1933, as amended (the "Securities Act"), Section 21E of the Securities Exchange Act of 1934, as amended (the "Exchange Act") and the Private Securities Litigation Reform Act of 1995.
- Actual results, performance or achievements could differ materially from those projected in the forward-looking statements as a result of a  number of risks, uncertainties and other factors.
- For a discussion of important factors that could cause our results, performance or achievements to differ materially from any future results, performance or achievements expressed or implied by our forward-looking statements, please refer to Part I, Item 1A, Risk Factors and Part II, Item 7, Management's Discussion and Analysis of Financial Condition and Results of Operations in this Annual Report.
- Certain trademarks or service marks of CMC appearing in this Annual Report are the property of CMC and are protected under applicable intellectual property laws.
- Today, through an extensive manufacturing network principally located in the United States ("U.S.") and Central Europe, we offer products and technologies to meet the critical reinforcement needs of the global construction sector.
- Our operations are conducted through three reportable segments: North America Steel Group, Emerging Businesses Group and Europe Steel Group.
- At CMC, we believe "it’s what’s inside that counts." This reflects the nature of our products, which are found in critical infrastructure worldwide, and also applies to our culture and employees.
- We operate under the guiding principles of placing the customer at the core of all we do, staying committed to our employees, giving back to our communities and creating value for our investors, all while continuing our commitment to sustainability.
- From our inception, our business model has been  strategically built on sustainable principles, including recycling metals, manufacturing products from approximately 98% recycled material using energy-efficient technology and employing closed-loop water recycling processes.
- We provide differentiating value for our customers through our industry-leading customer service with a low cost, high-quality production process.
- Further, we have achieved market leadership through our commitment to transformation, advancement and long-term growth by investing in our business and in our people.
- As our customers' needs and preferences have evolved, our products have expanded to include diverse and innovative solutions and future growth platforms.
- Through a combination of both value-accretive organic growth that captures available internal synergies, and capability-enhancing inorganic growth that broadens our portfolio, we aim to provide our customers with a comprehensive solution.
- Segments  The Company has three reportable segments that represent the primary businesses reported in our consolidated financial statements: North America Steel Group, Emerging Businesses Group and Europe Steel Group.
- The following chart summarizes net sales to external customers by major product category within each reportable segment during the year ended August 31, 2025.
- For a historical breakout of our net sales to external customers by major product category within each reportable segment, see Note  19, Segment Information, in Part II, Item 8 of this Annual Report.
- Sales by product.jpg  NORTH AMERICA STEEL GROUP SEGMENT  Our North America Steel Group segment provides a diverse offering of products and solutions to support the construction sector.
- Composed of a vertically integrated network of recycling facilities, steel mills and fabrication operations, our strategy in North America is to optimize our vertically integrated value chain to maximize profitability while providing industry-leading customer service.
- To execute our strategy, we seek to (i) obtain inputs at the lowest possible cost, including materials  procured from our recycling facilities, which are operated to provide low-cost scrap to our steel mills, (ii) operate modern, efficient electric arc furnace ("EAF") steel mills and (iii) enhance operational efficiency by utilizing our fabrication operations to optimize our steel mill volumes and obtain the highest possible selling prices to maximize metal margin.
- We strive to maximize cash flow generation through increased productivity, high-capacity utilization and optimal product mix.
- We have invested approximately 80%, 77% and 88% of total capital expenditures in our North America Steel Group segment during 2025, 2024 and 2023, respectively.
- Raw materials margin per ton is defined as the difference between the selling prices for processed and recycled ferrous and nonferrous  scrap metals and the price paid to purchase obsolete and industrial scrap.
- Our steel mill operations consist of six EAF mini mills, three EAF micro mills and one rerolling mill.
- Our steel mills manufacture finished long steel products including rebar, merchant bar, light structural and other special sections and wire rod, as well as semi-finished billets for rerolling and forging applications (collectively referred to as "steel products" in the context of the North America Steel Group segment).
- Each EAF mini mill consists of:  • a melt shop with an EAF;  • continuous casting equipment that shapes molten metal into billets;  • a reheating furnace that prepares billets for rolling;  • a rolling line that forms products from heated billets;  • a mechanical cooling bed that receives hot products from the rolling line;  • finishing facilities that shear, straighten, bundle and prepare products for shipping;  • baghouse systems that control particulate emissions from steelmaking operations; and  • supporting facilities such as maintenance, warehouse and office areas.
- Our EAF micro mills utilize similar equipment and processes as described above; however, these facilities utilize unique continuous process technology where metal flows uninterrupted from melting to casting to rolling into finished steel products.
- Our rerolling mill does not utilize a melt shop; the rerolling process begins by reheating billets to roll into finished steel products.
- The est imated annual  capacity for our steel mills, included in Part I, Item 2, Properties, of this Annual Report assumes a typical product mix and is not necessarily indicative of the expected production volumes or shipments in any fiscal year.


### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, litigation, regulation, competition, margin, supply chain, cyber, interest rate, customer, segment, product, service, market, operations, network

- There are inherent risks and uncertainties associated with our business that could adversely affect our business, results of operations and financial condition.
- Set forth below are descriptions of those risks and uncertainties that we currently believe to be material, but the risks and uncertainties described below are not the only risks and uncertainties that could adversely affect our business, results of operations and financial condition.
- If any of these risks actually occur, our business,  results of operations and financial condition could be materially adversely affected.
- RISKS RELATED TO OUR BUSINESS  Scrap and other inputs for our business are subject to significant price fluctuations and limited availability, which may adversely affect our business, results of operations and financial condition.
- We depend on ferrous scrap, the primary raw material used by our steel mills, and other inputs such as graphite electrodes and alloys for our steel mill operations.
- The price of scrap and other inputs has historically been subject to significant fluctuation, and we may not be able to adjust our product prices to recover the costs of rapid increases in raw  material prices, especially over the short-term and in our fixed price contracts.
- The profitability of our operations would be adversely affected if we are unable to pass increased raw material and input costs on to our customers.
- A prolonged period of low scrap prices or a fall in scrap prices could impair our ability to obtain, process, sell and consume  recycled material, which could have a material adverse effect on our business, results of operations and financial condition.


### Item 7 — MD&A (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, uncertainty, litigation, regulation, revenue, margin, interest rate, customer, segment, product, service, market, operations, network

- AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERATIONS  This Management's Discussion and Analysis of Financial Condition and Results of Operations should be read in conjunction with our consolidated financial statements and the accompanying notes contained in this Annual Report.
- Our discussion and analysis of fiscal year 2024 compared to fiscal year 2023 can be found in Part II, Item 7, Management's Discussion and Analysis of Financial Condition and  Results of Operations, in our Annual Report on Form 10-K for the year ended August 31, 2024, which was filed with the SEC on October 17, 2024.
- Today, through an extensive manufacturing network principally located in the U.S.
- and Central Europe, the Company offers products and technologies to meet the critical reinforcement needs of the global construction sector.
- Our operations are conducted through three reportable segments: North America Steel Group, Emerging Businesses Group and Europe Steel Group.
- See Part I, Item 1, Business, of this Annual Report for further information regarding our business and reportable segments.
- Key Performance Indicators  When evaluating our results, we compare net sales, in the aggregate and for each of our reportable segments, in the current period to net sales in the corresponding period.
- For the North America Steel Group and the Europe Steel Group segments, we focus on changes in average selling price per ton and tons shipped compared to the corresponding period for each of our vertically integrated product categories as these are the two variables that typically have the greatest impact on our net sales for  those reportable segments.


## Research loop (think → act)

1. _heuristic_ — Coverage looks adequate for this pass; stopping iterative loop.

## Sources

- **[S1]** CMC fundamentals (yfinance)
  - Commercial Metals Company: price=68.04, rev=7798480000.0, fcf=312249000.0, shares=109528048.0, rev_cagr=-0.04356776135013685, ROIC=0.033978529382836874, FCF yield=None
- **[S2]** CMC DCF valuation (dcf)
  - Base share price=42.30738539488079, bull=138.43786429322256, bear=9.295473994309154
- **[S3]** CMC put screen (yfinance_options)
  - Expiration 2026-09-18 (DTE 52): 0 candidates; IV=0.0195410546875, IV rank=None, HV rank=0.6461628837943942. Delta band approximated via % OTM when greeks are unavailable; IV ran…
- **[S4]** Due Diligence: Types and How to Perform (web) — https://www.investopedia.com/terms/d/duediligence.asp
  - May 21, 2025 - Hard due diligence is concerned with the numbers and data found on the financial statements, like the balance sheet and income statement. This can entail fundamen…
- **[S5]** DCF Due Diligence: A Step-by-Step Guide for Company Valuation - BlackNote Investment (web) — https://blacknoteinvestment.com/dcf-due-diligence-guide/
  - June 13, 2024 - To help investors and professional analysts in their jobs we draw up a must-follow guide that thoroughly covers every crucial aspect of due diligence required fo…
- **[S6]** How to Conduct Financial Due Diligence + Checklist (web) — https://dealroom.net/blog/how-to-conduct-financial-due-diligence
  - 2 weeks ago - Think of financial due diligence as a deep investigation into a company’s financial statements—its income statement, balance sheet, and cash flow reports. While an…
- **[S7]** DCF Sensitivity Analysis: 3 Powerful Scenario Tables (web) — https://mnainstitute.com/dcf-sensitivity-analysis-scenario/
  - June 17, 2026 - Second, each scenario must be commercially believable. Master the M&A Full Due Diligence course that prepares you to analyze, evaluate, and manage every risk in …
- **[S8]** Due Diligence: Types and How to Perform (web_page) — https://www.investopedia.com/terms/d/duediligence.asp
  - Due Diligence: Types and How to Perform ​ Top Stories Average Retirement Savings for a 75 Year Old Your Wealth Depends on the Stock Market More Than Ever Generational Divides Ov…
- **[S9]** DCF Due Diligence: A Step-by-Step Guide for Company Valuation - BlackNote Investment (web_page) — https://blacknoteinvestment.com/dcf-due-diligence-guide/
  - DCF Due Diligence: A Step-by-Step Guide for Company Valuation - BlackNote Investment Home » Blog » DCF Due Diligence: A Step-by-Step Guide for Company Valuation DCF Due Diligenc…
- **[S10]** M&A Career Path: Analyst to MD (Comp + Hours, 2026) (web_page) — https://dealroom.net/blog/how-to-conduct-financial-due-diligence
  - M&A Career Path: Analyst to MD (Comp + Hours, 2026) FREE M&A Skills Library 🚀 Ready-to-run AI skills for every stage of your deal. Unlock now👉🏻 DealRoom Logo Table of Contents T…
- **[S11]** CMC 10-K (sec)
  - Item 1 chars=45984, Item 1A chars=50000, Item 7 chars=50000, ok=True, source=cache
- **[S12]** Item 1 Business summary (nlp)
  - ### Item 1 — Business (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, margin, supply chain, customer, segmen…
- **[S13]** Item 1A summary (nlp)
  - ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, litigation, regulation, competition, margin, supply chain, cyber, interest rate, cu…
- **[S14]** Item 7 summary (nlp)
  - ### Item 7 — MD&A (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, revenue, margin, interest rate, customer, segment, prod…

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

# CMC — Planned Research Report

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
- Company: Commercial Metals Company
- Sector / industry: Industrials / Metal Fabrication
- Price: 68.04
- 52-week range: $49.66 – $84.87
- Market cap: —
- Enterprise value: $10.59B
- Shares outstanding: 109.53M
- Beta: 1.532
- Book equity: $4.19B
- Revenue (latest): $7.80B
- EBITDA (latest): $438.92M
- Free cash flow (latest): $312.25M
- Operating income: $519.92M
- Operating margin: 6.7%
- EV / EBITDA: 24.1x
- ROIC: 3.4%
- FCF yield: —
- Debt / Equity: 0.32298442237732483
- FCF / share: $2.85
- Revenue / share: $71.20

### Capital structure
- Cash: $1.04B
- Short-term debt: $44.29M
- Long-term debt: $1.31B
- Total debt: $1.35B
- Net debt: $311.04M
- Net debt / EBITDA: 0.7x

### Growth
- Revenue CAGR: -4.4%
- FCF CAGR: 7.6%
- Latest revenue YoY: -1.6%
- Latest FCF YoY: -45.7%

### Market expectations (yfinance, sparse)
- Mean target: $80.09
- Target range: $75.00 – $88.00
- Recommendation: buy

_Consensus revenue/EBITDA forecasts are often unavailable via free feeds; treat targets as point-in-time only._

### Historical KPIs (multi-year)

| Year | Revenue | OCF | Capex | FCF | EBITDA | LT debt | Cash | Net debt | Net income |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2025 | $7.80B | $715.07M | $402.82M | $312.25M | $438.92M | $1.31B | $1.04B | $266.75M | $84.66M |
| 2024 | $7.93B | $899.71M | $324.27M | $575.44M | $963.93M | $1.15B | $857.92M | $292.91M | $485.49M |
| 2023 | $8.80B | $1.34B | $606.66M | $737.44M | $1.38B | $1.11B | $592.33M | $521.95M | $859.76M |
| 2022 | $8.91B | $700.31M | $449.99M | $250.32M | $1.74B | $1.11B | $672.60M | $440.65M | $1.22B |

## Charts

### Revenue & FCF history
![Revenue & FCF history](/charts/CMC_income_revenue_fcf.png)

## Web research — web_research

- Queries: CMC news, Commercial Metals Company earnings OR catalyst
- Unique hits: 14
- Pages fetched: 2/3

### Web synthesis — web_research (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, revenue, service, market, network

- Along with ABC News and NBC News, it has long been among the big three broadcast news networks in the United States.CBS News emerged as a radio news broadcast service in 1929.
- [HIT] Cmc outlines $150M annualized EBITDA run-rate target for TAG program while expanding precast platform integration | Seeking Alpha | https://seekingalpha.com/news/4569633-cmc-outlines-150m-annualized-ebitda-run-rate-target-for-tag-program-while-expanding-precast CEO Peter Matt stated that "the CMC team delivered another excellent financial performance this quarter, propelled by solid operational and commercial execution, a favorable market backdrop in most ...
- [HIT] Catalyst Corporate FCU | Credit Union Liquidity Asset Management | www.catalystcorp.org | https://www.catalystcorp.org/ Catalyst empowers credit unions to attract members and grow with financial solutions like asset management, payment services, risk management, liquidity solutions, treasury support, and much more.
- | MSN | https://www.msn.com/en-us/money/topstocks/commercial-metals-cmc-earnings-expected-to-grow-should-you-buy/ar-AA25YMyd The market expects Commercial Metals (CMC) to deliver a year-over-year increase in earnings on higher revenues when it reports results for the quarter ended May 2026.

### Sources found
- [CBS News](https://en.wikipedia.org/wiki/CBS_News)
  - CBS News is the news division of the American television broadcaster CBS headquartered in New York City. Along with ABC News and NBC News, it has long been a…
- [Christian McCaffrey News - ESPN](https://www.espn.com/nfl/player/news/_/id/3117251/christian-mccaffrey)
  - Find the latest news about San Francisco 49ers Running Back Christian McCaffrey on ESPN. Check out news, rumors, and game highlights.
- [CMC News - Colorado Mountain College](https://coloradomtn.edu/cmc-news/)
  - July 16, 2025 - CMC News - News and Feature Stories for Colorado Mountain College Find news articles and up-to-date official communications from CMC Featured…
- [Christian McCaffrey - NFL News, Rumors, & Updates | FOX Sports](https://www.foxsports.com/nfl/christian-mccaffrey-player)
  - 2 days ago - This Worrying Stat Could Be Bad News for 49ers RB Christian McCaffrey What can we expect from Christian McCaffrey in 2026?
- [CMC ROCKS QLD to Mark 20th Anniversary With 2027 Return to Willowbank](https://www.broadwayworld.com/westend/article/CMC-ROCKS-QLD-to-Mark-20th-Anniversary-With-2027-Return-to-Willowbank-20260727)
  - CMC Rocks QLD announced dates for its 20th anniversary festival, which will return to Willowbank...
- [Commercial Metals Co (CMC)](https://www.morningstar.com/stocks/xnys/cmc/quote)
  - See the latest Commercial Metals Co stock price (CMC:XNYS), related news, valuation, dividends and more to help you make your investing decisions.
- [Christian McCaffrey Fantasy Football News, Rankings, Projections | San Francisco...](https://www.fantasypros.com/nfl/players/christian-mccaffrey.php)
  - View expert consensus rankings for Christian McCaffrey (San Francisco 49ers), read the latest news...
- [Cmc outlines $150M annualized EBITDA run-rate target for TAG program while expanding precast platform integration](https://seekingalpha.com/news/4569633-cmc-outlines-150m-annualized-ebitda-run-rate-target-for-tag-program-while-expanding-precast)
  - CEO Peter Matt stated that "the CMC team delivered another excellent financial performance this quarter, propelled by solid operational and commercial execut…
- [Matrix Catalyst Guide for Midnight - Crafting Tier Set Pieces](https://www.wowhead.com/guide/midnight/matrix-catalyst-crafting-tier-set)
  - The Matrix Catalyst in World of Warcraft: Midnight is a system that converts non-tier armor pieces into tier set armor pieces of the same type. Learn everyth…
- [Catalyst Metals • ASX:CYL](https://catalystmetals.com.au/)
  - Catalyst Metals (ASX:CYL) is a Western Australian gold producer generating 100,000oz a year from its flagship asset, the Plutonic Gold Belt.
- [Catalyst Investors | Growth Equity | New York](https://catalyst.com/)
  - At Catalyst, We Are True Growth Investors With 20+ years of providing growth capital to B2B businesses, Catalyst is the consummate partner to support your ne…
- [Catalyst Corporate FCU | Credit Union Liquidity Asset Management](https://www.catalystcorp.org/)
  - Catalyst empowers credit unions to attract members and grow with financial solutions like asset management, payment services, risk management, liquidity solu…

## Put opportunities (heuristic) [S2]
- Expiration: 2026-09-18 (DTE 52)
- Candidates: 0
- ATM IV (est.): 2.0%
- IV rank: — (1 local samples)
- HV rank (20d realized): 64.6%


_Note: Delta band approximated via % OTM when greeks are unavailable; IV rank needs ~20+ local daily IV samples (have 1); run the options screen over time to build history.; HV rank is realized-vol rank (20d HV vs ~1y); useful when IV history is thin._

## Research loop (think → act)

1. _heuristic_ — Coverage looks adequate for this pass; stopping iterative loop.

## Sources

- **[S1]** CMC fundamentals (yfinance)
  - Commercial Metals Company: price=68.04, rev=7798480000.0, fcf=312249000.0, shares=109528048.0, rev_cagr=-0.04356776135013685, ROIC=0.033978529382836874, FCF yield=None
- **[S2]** CMC put screen (yfinance_options)
  - Expiration 2026-09-18 (DTE 52): 0 candidates; IV=0.0195410546875, IV rank=None, HV rank=0.6461627113937596. Delta band approximated via % OTM when greeks are unavailable; IV ran…
- **[S3]** CBS News (web) — https://en.wikipedia.org/wiki/CBS_News
  - CBS News is the news division of the American television broadcaster CBS headquartered in New York City. Along with ABC News and NBC News, it has long been among the big three b…
- **[S4]** Christian McCaffrey News - ESPN (web) — https://www.espn.com/nfl/player/news/_/id/3117251/christian-mccaffrey
  - Find the latest news about San Francisco 49ers Running Back Christian McCaffrey on ESPN. Check out news, rumors, and game highlights.
- **[S5]** CMC News - Colorado Mountain College (web) — https://coloradomtn.edu/cmc-news/
  - July 16, 2025 - CMC News - News and Feature Stories for Colorado Mountain College Find news articles and up-to-date official communications from CMC Featured Story Contact Media…
- **[S6]** Christian McCaffrey - NFL News, Rumors, & Updates | FOX Sports (web) — https://www.foxsports.com/nfl/christian-mccaffrey-player
  - 2 days ago - This Worrying Stat Could Be Bad News for 49ers RB Christian McCaffrey What can we expect from Christian McCaffrey in 2026?
- **[S7]** CMC ROCKS QLD to Mark 20th Anniversary With 2027 Return to Willowbank (web) — https://www.broadwayworld.com/westend/article/CMC-ROCKS-QLD-to-Mark-20th-Anniversary-With-2027-Return-to-Willowbank-20260727
  - CMC Rocks QLD announced dates for its 20th anniversary festival, which will return to Willowbank...
- **[S8]** Commercial Metals Co (CMC) (web) — https://www.morningstar.com/stocks/xnys/cmc/quote
  - See the latest Commercial Metals Co stock price (CMC:XNYS), related news, valuation, dividends and more to help you make your investing decisions.
- **[S9]** Christian McCaffrey Fantasy Football News, Rankings, Projections | San Francisco... (web) — https://www.fantasypros.com/nfl/players/christian-mccaffrey.php
  - View expert consensus rankings for Christian McCaffrey (San Francisco 49ers), read the latest news...
- **[S10]** Cmc outlines $150M annualized EBITDA run-rate target for TAG program while expanding precast platform integration (web) — https://seekingalpha.com/news/4569633-cmc-outlines-150m-annualized-ebitda-run-rate-target-for-tag-program-while-expanding-precast
  - CEO Peter Matt stated that "the CMC team delivered another excellent financial performance this quarter, propelled by solid operational and commercial execution, a favorable mar…
- **[S11]** Christian McCaffrey News - ESPN (web_page) — https://www.espn.com/nfl/player/news/_/id/3117251/christian-mccaffrey
  - Christian McCaffrey News - ESPN Skip to main content Skip to navigation Christian McCaffrey San Francisco 49ers #23 Running Back HT/WT 5' 11", 210 lbs Birthdate 6/7/1996 (30) Co…
- **[S12]** CMC News - Colorado Mountain College (web_page) — https://coloradomtn.edu/cmc-news/
  - CMC News - Colorado Mountain College CMC News — News and Feature Stories for Colorado Mountain College Find news articles and up-to-date official communications from CMC Feature…

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

# CMC — Planned Research Report

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
- Company: Commercial Metals Company
- Sector / industry: Industrials / Metal Fabrication
- Price: 68.04
- 52-week range: $49.66 – $84.87
- Market cap: —
- Enterprise value: $10.59B
- Shares outstanding: 109.53M
- Beta: 1.532
- Book equity: $4.19B
- Revenue (latest): $7.80B
- EBITDA (latest): $438.92M
- Free cash flow (latest): $312.25M
- Operating income: $519.92M
- Operating margin: 6.7%
- EV / EBITDA: 24.1x
- ROIC: 3.4%
- FCF yield: —
- Debt / Equity: 0.32298442237732483
- FCF / share: $2.85
- Revenue / share: $71.20

### Capital structure
- Cash: $1.04B
- Short-term debt: $44.29M
- Long-term debt: $1.31B
- Total debt: $1.35B
- Net debt: $311.04M
- Net debt / EBITDA: 0.7x

### Growth
- Revenue CAGR: -4.4%
- FCF CAGR: 7.6%
- Latest revenue YoY: -1.6%
- Latest FCF YoY: -45.7%

### Market expectations (yfinance, sparse)
- Mean target: $80.09
- Target range: $75.00 – $88.00
- Recommendation: buy

_Consensus revenue/EBITDA forecasts are often unavailable via free feeds; treat targets as point-in-time only._

### Historical KPIs (multi-year)

| Year | Revenue | OCF | Capex | FCF | EBITDA | LT debt | Cash | Net debt | Net income |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2025 | $7.80B | $715.07M | $402.82M | $312.25M | $438.92M | $1.31B | $1.04B | $266.75M | $84.66M |
| 2024 | $7.93B | $899.71M | $324.27M | $575.44M | $963.93M | $1.15B | $857.92M | $292.91M | $485.49M |
| 2023 | $8.80B | $1.34B | $606.66M | $737.44M | $1.38B | $1.11B | $592.33M | $521.95M | $859.76M |
| 2022 | $8.91B | $700.31M | $449.99M | $250.32M | $1.74B | $1.11B | $672.60M | $440.65M | $1.22B |

## Charts

### Revenue & FCF history
![Revenue & FCF history](/charts/CMC_fast_revenue_fcf.png)

### DCF scenario prices
![DCF scenario prices](/charts/CMC_fast_dcf_scenarios.png)

### Base-case FCF path
![Base-case FCF path](/charts/CMC_fast_base_fcf_path.png)

## DCF valuation (base / bull / bear) [S2]

> Simplified revenue->FCF DCF. Not investment advice; assumptions are editable heuristics.

- Spot price: $68.04
- Base revenue: $7.80B
- Shares: 109,528,048
- Net debt (Debt−Cash): $311.04M

| Scenario | Growth | FCF margin | WACC | Term. g | Equity value | Share price | Upside |
|----------|--------|------------|------|---------|--------------|-------------|--------|
| bear | -1.6% | 2.0% | 12.0% | 1.5% | $1.02B | $9.30 | -86.3% |
| base | 6.0% | 4.0% | 10.0% | 2.5% | $4.63B | $42.31 | -37.8% |
| bull | 15.0% | 7.0% | 9.0% | 3.0% | $15.16B | $138.44 | 103.5% |

### Assumption notes
- Base revenue growth seeded from historical rate (-1.6%).
- Recent revenue declined (-1.6% YoY); base/bull use normalized mid-cycle growth instead of extrapolating the decline.


### Base-case projected FCF

- Year 1: revenue $8.27B, FCF $330.98M (PV $300.89M)
- Year 2: revenue $8.76B, FCF $350.84M (PV $289.95M)
- Year 3: revenue $9.29B, FCF $371.89M (PV $279.41M)
- Year 4: revenue $9.85B, FCF $394.21M (PV $269.25M)
- Year 5: revenue $10.44B, FCF $417.86M (PV $259.46M)
- Terminal value $5.71B (PV $3.55B)

## Put opportunities (heuristic) [S3]
- Expiration: 2026-09-18 (DTE 52)
- Candidates: 0
- ATM IV (est.): 2.0%
- IV rank: — (1 local samples)
- HV rank (20d realized): 64.6%


_Note: Delta band approximated via % OTM when greeks are unavailable; IV rank needs ~20+ local daily IV samples (have 1); run the options screen over time to build history.; HV rank is realized-vol rank (20d HV vs ~1y); useful when IV history is thin._

## Research loop (think → act)

1. _heuristic_ — Coverage looks adequate for this pass; stopping iterative loop.

## Sources

- **[S1]** CMC fundamentals (yfinance)
  - Commercial Metals Company: price=68.04, rev=7798480000.0, fcf=312249000.0, shares=109528048.0, rev_cagr=-0.04356776135013685, ROIC=0.033978529382836874, FCF yield=None
- **[S2]** CMC DCF valuation (dcf)
  - Base share price=42.30738539488079, bull=138.43786429322256, bear=9.295473994309154
- **[S3]** CMC put screen (yfinance_options)
  - Expiration 2026-09-18 (DTE 52): 0 candidates; IV=0.0195410546875, IV rank=None, HV rank=0.6461627094663688. Delta band approximated via % OTM when greeks are unavailable; IV ran…

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
