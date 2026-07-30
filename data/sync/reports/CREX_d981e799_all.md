# CREX — Full research pack

> Not investment advice. Local research draft only.

**Templates:** memo, valuation, deep, income, fast
**Generated:** 2026-07-28T08:41:58.202561+00:00



---

# Template: Institutional deep dive (memo) (`memo`)

# CREX — Planned Research Report

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
- Company: Creative Realities, Inc.
- Sector / industry: Technology / Software - Application
- Price: 3.11
- 52-week range: $2.19 – $4.42
- Market cap: $40.73M
- Enterprise value: $129.24M
- Shares outstanding: 13.10M
- Beta: 1.458
- Book equity: $49.19M
- Revenue (latest): $57.23M
- EBITDA (latest): $1.86M
- Free cash flow (latest): -$10.24M
- Operating income: -$3.15M
- Operating margin: -5.5%
- EV / EBITDA: 69.5x
- ROIC: -4.0%
- FCF yield: -25.1%
- Debt / Equity: 1.3797625340544057
- FCF / share: -$0.78
- Revenue / share: $4.37

### Capital structure
- Cash: $1.56M
- Short-term debt: $4.43M
- Long-term debt: $39.52M
- Total debt: $67.86M
- Net debt: $66.31M
- Net debt / EBITDA: 35.6x

### Growth
- Revenue CAGR: 9.7%
- FCF CAGR: —
- Latest revenue YoY: 12.5%
- Latest FCF YoY: -1866.2%

### Market expectations (yfinance, sparse)
- Mean target: $8.17
- Target range: $7.00 – $10.00
- Recommendation: strong_buy

_Consensus revenue/EBITDA forecasts are often unavailable via free feeds; treat targets as point-in-time only._

### Historical KPIs (multi-year)

| Year | Revenue | OCF | Capex | FCF | EBITDA | LT debt | Cash | Net debt | Net income |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2025 | $57.23M | -$7.75M | $2.49M | -$10.24M | $1.86M | $39.52M | $1.56M | $37.96M | -$8.28M |
| 2024 | $50.85M | $3.38M | $2.80M | $580.00K | $2.45M | $13.04M | $1.04M | $12.01M | -$3.51M |
| 2023 | $45.17M | $5.17M | $4.03M | $1.14M | $3.36M | $9.83M | $2.91M | $6.92M | -$2.94M |
| 2022 | $43.35M | -$708.00K | $4.29M | -$5.00M | $7.53M | $13.07M | $1.63M | $11.44M | $1.88M |

## Charts

### Revenue & FCF history
![Revenue & FCF history](/charts/CREX_memo_revenue_fcf.png)

### DCF scenario prices
![DCF scenario prices](/charts/CREX_memo_dcf_scenarios.png)

### Base-case FCF path
![Base-case FCF path](/charts/CREX_memo_base_fcf_path.png)

### EV/EBITDA scenario prices
![EV/EBITDA scenario prices](/charts/CREX_memo_ev_ebitda_scenarios.png)

### Headwind/tailwind price ranges
![Headwind/tailwind price ranges](/charts/CREX_memo_scenario_ranges.png)

### Normalized price vs peers
![Normalized price vs peers](/charts/CREX_memo_peers_normalized.png)

## DCF valuation (base / bull / bear) [S3]

> Simplified revenue->FCF DCF. Not investment advice; assumptions are editable heuristics.

- Spot price: $3.11
- Base revenue: $57.23M
- Shares: 13,097,892
- Net debt (Debt−Cash): $66.31M

| Scenario | Growth | FCF margin | WACC | Term. g | Equity value | Share price | Upside |
|----------|--------|------------|------|---------|--------------|-------------|--------|
| bear | 5.5% | 1.0% | 12.0% | 1.5% | -$59.79M | $-4.57 | -246.8% |
| base | 12.5% | 3.0% | 10.0% | 2.5% | -$30.80M | $-2.35 | -175.6% |
| bull | 19.5% | 8.0% | 9.0% | 3.0% | $88.85M | $6.78 | 118.1% |

### Assumption notes
- Base revenue growth seeded from historical rate (12.5%).
- Latest FCF margin was -17.9%; scenarios use normalized positive margins for a going-concern DCF.

- _base: model equity value is negative after net debt (-30,803,035); showing $-2.35/sh._
- _bear: model equity value is negative after net debt (-59,791,969); showing $-4.57/sh._

### Base-case projected FCF

- Year 1: revenue $64.41M, FCF $1.93M (PV $1.76M)
- Year 2: revenue $72.49M, FCF $2.17M (PV $1.80M)
- Year 3: revenue $81.58M, FCF $2.45M (PV $1.84M)
- Year 4: revenue $91.81M, FCF $2.75M (PV $1.88M)
- Year 5: revenue $103.33M, FCF $3.10M (PV $1.92M)
- Terminal value $42.36M (PV $26.30M)

## Valuation — EV/EBITDA scenarios [S2]

> Priced-in model: implied price = (EBITDA × EV/EBITDA − net debt) ÷ shares. Not a forecast.

- Spot: $3.11
- Net debt used: $66.31M

| Scenario | EBITDA | EV/EBITDA | Implied EV | Equity value | Implied price |
|---|---:|---:|---:|---:|---:|
| bear | $1.30M | 30.0x | $39.06M | -$27.25M | $-2.08 |
| base | $1.86M | 40.0x | $74.40M | $8.09M | $0.62 |
| bull | $2.23M | 45.0x | $100.44M | $34.13M | $2.61 |

- Base EBITDA seeded from latest reported/TTM figure (1,860,000).
- Base multiple seeded from current EV/EBITDA (69.5x).

## Scenario price ranges (headwinds & tailwinds) [S35]

> Medium-term (18–36 months (medium / medium-long term)) driver → EV/EBITDA bridge. Distinct from the FCF DCF path. Not investment advice.

- Spot: $3.11
- Sparse Street mean target: $8.17
- Anchor multiple: 45.0x (driver_ev_ebitda_bridge)
- Anchor EBITDA: $1.86M
- Probability-weighted midpoint: **$0.82** (heuristic weights, not a rating)
- Driver extraction: `rules`

### Headwinds (bear-case fuel)

- **Elevated leverage (ND/EBITDA)** — Net debt / EBITDA ≈ 35.6x — refinancing and equity duration risk _(source: fundamentals)_
- **Negative free cash flow** — Latest FCF -$10.24M — cash burn raises financing risk _(source: fundamentals)_
- **Balance-sheet / refinancing pressure** — sector=Technology industry=Software - Application revenue=57232000.0 ebitda=1860000.0 fcf=-10244000.0 net_debt=66306000.0 nd_ebitda=35.648387096774194 target=8.16667 rec=strong_buy _(source: fundamentals)_
- **Regulatory / legal risk** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin, supply chain, cyber _(source: item_1a)_
- **Competitive / pricing pressure** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin, supply chain, cyber _(source: item_1a)_
- **Margin / cost headwind** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin, supply chain, cyber _(source: item_1a)_
- **Operational / cyber risk** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin, supply chain, cyber _(source: item_1a)_

### Tailwinds (bull-case fuel)

- **Revenue growth momentum** — Latest revenue YoY ≈ 12.5% _(source: fundamentals)_
- **Street target implies upside** — Mean target $8.17 vs spot $3.11 _(source: fundamentals)_
- **Product / pricing power** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin, supply chain, cyber _(source: item_1a)_
- **Contract / backlog wins** — ### Item 7 — MD&A (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, regulation, revenue, margin, customer, segment, product, service, market, operatio _(source: item_7)_
- **Multiple re-rating / Street upgrades** — Creative Realities (CREX) Analyst Ratings Current and historical analyst ratings for Creative Realities (CREX) stock. See upgrades, downgrades, price targets and more from professi _(source: web)_
- **Growth / execution upside** — Creative Realities (CREX) Stock Forecast and Price Target 2025 CREX's current price target is $8.00. Learn why top analysts are making this stock forecast for Creative Realities at _(source: web)_
- **Capital returns / FCF inflection** — CREX | Creative Realities Inc. Analyst Estimates & Ratings – WSJCreative Realities (CREX) Stock Price & OverviewCREX Stock Price Quote | MorningstarUpgrade - Personal Loans, Cards  _(source: web)_
- **Margin expansion / cost takeout** — Creative Realities (CREX) Q1 2026: $10M Synergy Target Drives... CREX is executing on the largest retail media network deployment in the U.S. for 2026, with 10,000 screens and 20,0 _(source: web)_

### Price ranges by case

| Case | Prob. | Metric vs TTM | Multiple | Price low | Mid | High | Upside vs spot |
|---|---:|---:|---:|---:|---:|---:|---:|
| bear | 0.24 | 0.70x | 9.4x | $-4.22 | $-4.13 | $-4.04 | -233% |
| base | 0.46 | 1.02x | 45.0x | $1.00 | $1.46 | $1.91 | -53% |
| bull | 0.3 | 1.25x | 50.0x | $2.93 | $3.81 | $4.70 | +23% |

#### Bear — headwinds dominate

Headwinds bite: weaker operating trajectory and multiple compression. Equity duration shrinks if cash generation fails to offset leverage / competitive pressure.

- **Range:** $-4.22 – $-4.04 (mid $-4.13) · EBITDA $1.30M · multiple 9.4x
- Driver: **Elevated leverage (ND/EBITDA)** — Net debt / EBITDA ≈ 35.6x — refinancing and equity duration risk
- Driver: **Negative free cash flow** — Latest FCF -$10.24M — cash burn raises financing risk
- Driver: **Balance-sheet / refinancing pressure** — sector=Technology industry=Software - Application revenue=57232000.0 ebitda=1860000.0 fcf=-10244000.0 net_debt=66306000.0 nd_ebitda=35.648387096774194 target=8.
- Driver: **Regulatory / legal risk** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin,
- Driver: **Competitive / pricing pressure** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin,

#### Base — mixed execution

Balanced path: some tailwinds offset headwinds. Operating scale roughly holds with modest repair/normalization; valuation stays near the current EV/EBITDA anchor.

- **Range:** $1.00 – $1.91 (mid $1.46) · EBITDA $1.90M · multiple 45.0x
- Driver: **Revenue growth momentum** — Latest revenue YoY ≈ 12.5%
- Driver: **Street target implies upside** — Mean target $8.17 vs spot $3.11
- Driver: **Elevated leverage (ND/EBITDA)** — Net debt / EBITDA ≈ 35.6x — refinancing and equity duration risk
- Driver: **Negative free cash flow** — Latest FCF -$10.24M — cash burn raises financing risk

#### Bull — tailwinds dominate

Tailwinds compound: operating improvement plus a re-rating toward peer or recovery multiples as balance-sheet and growth narratives improve.

- **Range:** $2.93 – $4.70 (mid $3.81) · EBITDA $2.33M · multiple 50.0x
- Driver: **Revenue growth momentum** — Latest revenue YoY ≈ 12.5%
- Driver: **Street target implies upside** — Mean target $8.17 vs spot $3.11
- Driver: **Product / pricing power** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin,
- Driver: **Contract / backlog wins** — ### Item 7 — MD&A (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, regulation, revenue, margin, customer, segment, product, servi
- Driver: **Multiple re-rating / Street upgrades** — Creative Realities (CREX) Analyst Ratings Current and historical analyst ratings for Creative Realities (CREX) stock. See upgrades, downgrades, price targets an

### Method notes

- Item 1A risks weighted toward headwinds.
- Peer EV/EBITDA band 9.9x–51.4x (median 16.0x) informs multiple ranges.
- Mapping follows Gemini/Perplexity-style scenario memos: qualitative drivers → operating metric & multiple paths → share-price ranges over a medium-term horizon.

## Peer & factor comps

- Sector / industry: Technology / Software - Application
- Peers: MSFT, ORCL, ADBE, CRM, NOW

| Ticker | Mkt cap | EV/EBITDA | ND/EBITDA | Beta | 1y | 5y | Vol |
|---|---:|---:|---:|---:|---:|---:|---:|
| CREX | $40.7M | 51.4x | 27.2x | 1.46 | 6.5% | -37.9% | 83.1% |
| MSFT | $2890.4B | 15.9x | 0.3x | 1.13 | -23.7% | 41.7% | 27.1% |
| ORCL | $345.4B | 16.0x | 4.4x | 1.71 | -50.5% | 47.1% | 42.8% |
| ADBE | $94.5B | 9.9x | 0.1x | 1.43 | -35.9% | -61.7% | 37.2% |
| CRM | — | 13.4x | 2.4x | 1.18 | -34.9% | -27.6% | 37.7% |
| NOW | $109.1B | 39.0x | 1.3x | 0.96 | -45.5% | -9.5% | 44.4% |

- Peer set (heuristic by sector/industry): MSFT, ORCL, ADBE, CRM, NOW
- Beta vs MSFT (daily, ~5y overlap): 0.50

_Price returns are price-only (dividends ignored). Peer set is heuristic, not a formal comps universe._

## Earnings, guidance & revision catalysts

- Next earnings (calendar): 2026-08-12

| Date | EPS est | EPS actual | Surprise | 1-day move |
|---|---:|---:|---:|---:|
| 2026-08-12 | 0.05 | — | — | — |
| 2026-05-15 | -0.46 | -0.74 | -0.28 | -4.8% |
| 2026-04-14 | -0.04 | -0.21 | -0.17 | -2.1% |
| 2025-11-12 | -0.10 | -0.75 | -0.65 | -0.7% |
| 2025-08-13 | -0.07 | -0.17 | -0.10 | -7.0% |
| 2025-05-14 | -0.15 | 0.32 | 0.47 | 5.2% |
| 2025-03-14 | -0.11 | -0.27 | -0.16 | 1.1% |
| 2024-11-13 | -0.04 | 0.01 | 0.05 | -11.1% |
| 2024-08-14 | -0.06 | -0.06 | 0.00 | 3.2% |
| 2024-05-10 | -0.06 | -0.01 | 0.05 | -3.3% |
| 2024-03-21 | — | 0.20 | — | 2.3% |
| 2023-11-09 | -0.07 | -0.06 | 0.01 | 7.3% |

_EPS surprise vs 1-day move Pearson r=0.247 (n=10, p≈0.471); treat as suggestive only._

_Guidance vs Street and adjusted EBITDA are often missing from free feeds; use web/SEC sections for narrative guidance._

## Recent SEC filings (10-Q / 8-K)

| Date | Form | Description |
|---|---|---|
| 2026-06-30 | 8-K | [FORM 8-K](https://www.sec.gov/Archives/edgar/data/1356093/000143774926022083/crex20260626c_8k.htm) |
| 2026-06-29 | 8-K | [FORM 8-K](https://www.sec.gov/Archives/edgar/data/1356093/000143774926021905/crex20260625_8k.htm) |
| 2026-05-15 | 10-Q | [FORM 10-Q](https://www.sec.gov/Archives/edgar/data/1356093/000143774926017219/crex20260331c_10q.htm) |
| 2026-05-15 | 8-K | [FORM 8-K](https://www.sec.gov/Archives/edgar/data/1356093/000143774926017218/crex20260513_8k.htm) |
| 2026-04-15 | 10-K | [FORM 10-K](https://www.sec.gov/Archives/edgar/data/1356093/000143774926012302/crex20251231c_10k.htm) |
| 2026-04-14 | 8-K | [FORM 8-K](https://www.sec.gov/Archives/edgar/data/1356093/000143774926012193/crex20260413_8k.htm) |
| 2026-02-18 | 8-K | [FORM 8-K](https://www.sec.gov/Archives/edgar/data/1356093/000143774926004453/crex20260218_8k.htm) |
| 2026-01-02 | 8-K | [FORM 8-K](https://www.sec.gov/Archives/edgar/data/1356093/000143774926000084/crex20260102_8k.htm) |
| 2025-12-04 | 8-K | [FORM 8-K](https://www.sec.gov/Archives/edgar/data/1356093/000143774925036909/crex20251203_8k.htm) |
| 2025-11-19 | 8-K | [FORM 8-K](https://www.sec.gov/Archives/edgar/data/1356093/000143774925035743/crex20251119_8k.htm) |
| 2025-11-12 | 10-Q | [FORM 10-Q](https://www.sec.gov/Archives/edgar/data/1356093/000143774925034249/crex20250930_10q.htm) |
| 2025-11-12 | 8-K | [FORM 8-K](https://www.sec.gov/Archives/edgar/data/1356093/000143774925034248/crex20251109_8k.htm) |

_Headlines/meta only — documents not fully parsed in this pass._

## Key driver analysis (quarterly)

Pearson / Spearman correlations of quarterly stock returns with fundamentals.

| Driver | Pearson r | p | n | Spearman ρ | p |
|---|---:|---:|---:|---:|---:|
| Revenue growth (YoY) | — | — | 1 | — | — |
| Free cash flow | 0.525 | 0.286 | 5 | 0.600 | 0.194 |
| FCF margin | 0.830 | 0.010 | 5 | 0.700 | 0.090 |
| Operating cash flow | 0.512 | 0.302 | 5 | 0.300 | 0.586 |
| Long-term debt level | 0.136 | 0.812 | 5 | 0.000 | 1.000 |
| EBITDA | 0.079 | 0.891 | 5 | 0.100 | 0.862 |
| Capex (abs) | -0.321 | 0.557 | 5 | -0.300 | 0.586 |

### Regime check (FCF)

- later: r=0.525 (n=5, p≈0.286)

- Correlations describe association, not causation.
- Small samples (especially regime splits) are directional only.
- Regime split at 2023-12-31 (sample midpoint); directional only.

## Executive summary

Creative Realities, Inc. (CREX) trades near 3.11 with market cap $40.73M and EV $129.24M. Net debt is $66.31M (ND/EBITDA 35.648387096774194). Latest revenue $57.23M, EBITDA $1.86M, FCF -$10.24M.

**Goal focus:** Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers.

What matters most (framework): balance-sheet trajectory, cash generation vs leverage, and whether market expectations (sparse free-data targets) already price execution risk.

EV/EBITDA implied prices — bear $-2.08 / base $0.62 / bull $2.61.

## Company setup & business model

**Keyword hits:** risk, regulation, competition, guidance, revenue, margin, customer, segment, product, service, market, operations, network, subsidiary

- (“Creative Realities”, the “Company”, “we”, “us” or “our”) provides innovative digital signage and media solutions in North America to enhance communications in a wide-ranging variety of out-of-home environments, key market segments and use cases, including:    Retail                                                     Entertainment and Sports Venues                            Restaurants, including quick-serve restaurants (“QSR”)     Convenience Stores                                         Financial Services                                         Automotive                                                 Lottery                                                    Mixed Use Developments                                     Digital out of Home (“DOOH”) Advertising Networks         We serve market-leading companies, so there is a good chance that if you leave your home today to shop, work, eat or play, you will encounter one or more of our digital signage experiences.
- Our solutions are increasingly viable because we help our enterprise customers achieve a wide range of business objectives including:    Increased brand awareness/engagement               ───────────────────────────────────────────────────   Improved customer support                           Enhanced employee productivity and satisfaction     Increased revenue and profitability                 Improved guest experience                           Increased customer/guest engagement                 Traffic content and advertising                    Through a combination of organically grown platforms and a series of strategic acquisitions, the Company assists customers to design, deploy, manage, and monetize their digital signage and in-store retail media networks.
- The Company sources leads and opportunities for its solutions through its digital and content marketing initiatives, close relationships with key industry partners, equipment manufacturers, and the direct efforts of its in-house industry sales experts.
- Customer engagements focus on consultative conversations that ensure the Company’s solutions are positioned to help customers achieve their business objectives in the most cost-effective manner possible.
- When comparing Creative Realities to other digital signage competitors, our customers value the following competitive advantages:    Breadth of solutions – Creative Realities offers true solutions to our customers.
- 1      Managed labor pool – Unlike most companies in our industry, we have a curated labor pool of qualified and vetted field technicians available to service customers quickly nationwide.
- In-house creative resources – We assist customers in creating new content or repurposing existing content for digital signage experiences, an activity for which the Company has won several desi...
- Network scalability and reliability – Our software as a service (“SaaS”) content management platforms power some of the largest and most complex digital signage networks in North America, evide...
- Market sector expertise – Creative Realities has in-house experts in key market segments such as retail, quick-serve restaurants (“QSR”), convenience stores, and Digital Out of Home (“DOOH”) ad...
- Technical support – Digital signage networks present unique challenges for corporate IT departments.
- We simplify and improve end user support by leveraging our own Network Operations Center (“N...
- Retail Media Network – The Company owns and operates the largest mall shopping network in Canada.
- The three primary sources of revenue for the Company are:    Hardware sales from reselling digital signage hardware from original equipment manufacturers such as Samsung and BrightSign.
- Services revenue from helping customers design, deploy and manage their digital signage and in-store retail media networks, including:      Hardware system design/engineering     Hardware installation                  Content development                   2      Content scheduling                                                                       Post-deployment network and field support                                                AdTech to traffic advertising and content directly and through programmatic channels      Recurring subscription licensing and support revenue from our digital signage software platforms, which are generally sold via a SaaS model.
- Our platforms include:      ReflectView, the Company’s core digital signage platform for most applications, scalable and cost effective from 10 to 100,000+ devices;                                                                 Reflect Xperience, a web-based interface that allows customers to give content scheduling access to local users via the web or mobile devices, while still maintaining centralized programming co...
- AdLogic, the Company’s AdTech management platform for digital signage networks, which presently delivers approximately 50 million ads daily;                                                             CPM+, the Company’s demand side and supply side platform with campaign management and extensive capabilities for programmatic advertising;                                                               Clarity, the Company’s digital signage platform for menu board solutions, which has become a market leader for a range of restaurant, including QSR and convenience store applications; and              iShowroomProX, an omni-channel digital sales support platform targeted at original equipment manufacturers in the transportation sector, which integrates with dozens of key data services includ...
- While hardware sales and support services revenues can fluctuate more significantly year over year based on new, large-scale network deployments, the Company is focusing on maintaining and increasing recurring SaaS revenue as digital signage adoption/utilization expands across the vertical markets we serve.
- Flat panel displays, along with LED technology and digital media players typically constitute a large portion of the expenditure customers make relative to the entire cost of implementing a digital  marketing system implementation and can be a barrier to customer deployment.
- As a result, we believe that the broader adoption of digital marketing technology solutions is likely to increase, although we cannot predict the rate at which such adoption will occur.
- We believe the proliferation of in-store retail media networks will be an industrial catalyst for infrastructure and AdTech sales for which the Company is well situated from product set and technology stack standpoints.
- We believe that the selective acquisition and successful integration of certain companies will: accelerate our growth in targeted vertical and operating markets; enable us to cost-effectively aggregate multiple customer bases onto a single business and technology platform; provide us with greater operating scale on a consolidated basis; enable us to leverage a common set of processes and tools, and cost efficiencies company-wide; and ultimately result in higher operating profitability and cash flow from operations.
- Business Strategy  We believe that our existing business model is highly scalable and can be expanded successfully as we continue to grow organically, seek to acquire and integrate other companies in our target markets, strengthen our operational practices and procedures, further streamline our administrative office functions, and continue to capitalize on various marketing programs and activities.
- With a focus on SaaS revenues, we believe that our gross margins will rise as our business scales.
- 3    Industry Background  We believe certain digital marketing technology industry trends are creating the opportunity for retailers, brands, venue-operators, enterprises, non-profits and other organizations to create innovative shopping, marketing, and informational experiences for their customers and other stakeholders in various venues worldwide.
- These trends include: (i) the expectations of technology-savvy consumers; (ii) addressing on-line competitors by improving physical experiences; (iii) a decline in the cost  of hardware configurations (primarily flat panel displays) and software media players; (iv) the continued evolution of mobile, social, software and hardware technologies, applications and tools; (v) increasing sophistication of social networking platforms; (vi) increasingly complex customer requirements related to their specific digital marketing technology and solution objectives; and (vii) customer expectations of satisfactory consumer experiences with reduced installation and operating costs.
- As a result, a growing number of retailers, brands, venue-operators, and other organizations have identified the need and opportunity to implement increasingly agile, automated, targeted and cost-effective and “sales-lifting” digital marketing, and interactive experiences to market to their customers.
- We believe our customers consider capitalizing on these industry trends to be increasingly critical to any successful “store of the future” retail and brand sales environment, especially where sales staff turnover is high, training outcomes are inconsistent and product knowledge is low.
- Companies are implementing various digital marketing technology solutions, which: are implemented in multiple forms and types of configurations and locations; attempt to achieve any of a broad range of individual or combination of objectives; contain various levels of targeting; have the ability to instantly manage single or multiple locations remotely from a customer’s desktop or other connected device at each location; and are built to deliver or contain a standard or customized customer  experience unique to and within the customer’s environment.

_Source: latest 10-K Item 1 (Business), summarized locally._

## Variant perception

- **Consensus frame (sparse):** recommendation=strong_buy, mean target=8.16667.
- **Bear:** leverage and execution risk dominate; cash generation fails to cover refinancing / reinvestment needs; equity remains constrained by net debt.
- **Bull:** cash-flow and strategic optionality re-rate the equity as leverage falls and growth/mix improves.
- **Middle:** returns may track free-cash-flow more than headline revenue — verify with driver analysis tab.

## Catalysts & monitoring

- Next earnings window (calendar): 2026-08-12
- Peer tape to watch: MSFT, ORCL, ADBE, CRM, NOW
- Monitor: FCF vs net debt, leverage (ND/EBITDA), refinancing headlines, and material 8-K strategy updates.
- Recent filing: 8-K on 2026-06-30 — FORM 8-K
- Recent filing: 8-K on 2026-06-29 — FORM 8-K
- Recent filing: 10-Q on 2026-05-15 — FORM 10-Q
- Recent filing: 8-K on 2026-05-15 — FORM 8-K
- Recent filing: 10-K on 2026-04-15 — FORM 10-K

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
| Guidance / outlook | Forward cash/earnings path | Creative Realities (CREX) Stock Forecast, Price Targets and... Analyze Forecast. Average Price Target.The highest analyst price target is $9.00 ,the lowest forecast is $9.00. The a | Creative Realities (CREX) Stock Forecast, Price Targets and... |
| Contract / backlog | Demand durability | Creative Realities Inc Customers by Division and Industry - CSIMarket We currently market and sell our marketing technology solutions through our direct sales force and word-of-mou | Creative Realities Inc Customers by Division and Industry - CSIMarket |

_Proxies are heuristic extractions from public web/SEC context; verify against primary filings._

## Catalyst calendar

| Window | Catalyst | Notes |
|---|---|---|
| 2026-08-12 | Earnings | Next report date from yfinance calendar |
| 2026-06-30 | 8-K | FORM 8-K |
| 2026-06-29 | 8-K | FORM 8-K |
| 2026-05-15 | 10-Q | FORM 10-Q |
| 2026-05-15 | 8-K | FORM 8-K |
| 2026-04-15 | 10-K | FORM 10-K |
| 2026-04-14 | 8-K | FORM 8-K |
| 2026-02-18 | 8-K | FORM 8-K |
| 2026-01-02 | 8-K | FORM 8-K |
| 2025-12-04 | 8-K | FORM 8-K |
| 2025-11-19 | 8-K | FORM 8-K |
| 2025-11-12 | 10-Q | FORM 10-Q |
| 2025-11-12 | 8-K | FORM 8-K |
| Jun 22, 2026 | Web event | CREX | Creative Realities Inc. Analyst Estimates & Ratings – WSJCreative Realities (CREX) Stock Price & OverviewCREX Stock Price Quote | Mor |
| Jun 22, 2026 | Web event | Creative Realities (CREX) Stock Price & OverviewCREX Stock Price Quote | MorningstarUpgrade - Personal Loans, Cards and Rewards Checking | H |
| Jun 22, 2026 | Web event | CREX Stock Price Quote | MorningstarUpgrade - Personal Loans, Cards and Rewards Checking | HomeUpgrade - Personal Loans, Cards and Rewards C |
| October 20, 2023 | Web event | Creative Realities Stock Guidance | NASDAQ:CREX | Benzinga |
| Oct 12, 2010 | Web event | Case Studies in the Achievement of Air Superiority |
| Jun 30 2023 | Web event | Creative Realities Inc (CREX) Earnings Report, Financial Results... |

## Web research — web_analysts

- Queries: CREX analyst price target, Creative Realities, Inc. stock rating OR consensus OR upgrade OR downgrade, CREX Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers analyst, CREX guidance OR investor day OR catalyst
- Unique hits: 18
- Pages fetched: 1/3

### Web synthesis — web_analysts (rule-based fallback — Ollama unavailable)
**Keyword hits:** guidance, revenue, market

- [HIT] Creative Realities (CREX) Stock Forecast and Price Target 2025 | www.marketbeat.com | https://www.marketbeat.com/stocks/NASDAQ/CREX/forecast/ CREX's current price target is $8.00.
- Learn why top analysts are making this stock forecast for Creative Realities at MarketBeat.Creative Realities - Analysts' Recommendations and Stock Price Forecast (2025).
- How MarketBeat Calculates Price Target and Consensus Rating.
- · via Yahoo Finance | https://finance.yahoo.com/markets/stocks/articles/creative-realities-crex-story-shifting-080315391.html Creative Realities is back in focus after analysts revised their fair value price target from...
- (CREX) stock, with detailed revenue and earnings estimates.
- Analyst Estimates & Ratings – WSJCreative Realities (CREX) Stock Price & OverviewCREX Stock Price Quote | MorningstarUpgrade - Personal Loans, Cards and Rewards Checking | HomeUpgrade - Personal Loans, Cards and Rewards Checking | UpgradeHow to Use Consensus in Claude (via MCP) | www.wsj.com | https://www.wsj.com/market-data/quotes/CREX/research-ratings Creative Realities Inc.
- [HIT] Creative Realities (CREX) Institutional Ownership 2025 | www.marketbeat.com | https://www.marketbeat.com/stocks/nasdaq/crex/institutional-ownership/ View CREX institutional ownership (13F) transactions at MarketBeat.Institutional investors have bought a total of 620,391 shares in the last 24 months.
- | Nasdaq | www.nasdaq.com | https://www.nasdaq.com/market-activity/stocks/crex/institutional-holdings CREX Institutional Holdings.

### Sources found
- [Creative Realities (CREX) Stock Forecast, Price Targets and...](https://www.tipranks.com/stocks/crex/forecast)
  - Analyze Forecast. Average Price Target.The highest analyst price target is $9.00 ,the lowest forecast is $9.00. The average price target represents 138.73% I…
- [CREX Forecast — Price Target — Prediction for 2027 — TradingView](https://www.tradingview.com/symbols/NASDAQ-CREX/forecast/)
  - Price target. 8.130.000.00%. The 4 analysts offering 1-year price forecasts have a max estimate of — and a min estimate of —. Analyst rating. Based on 4 anal…
- [Creative Realities (CREX) Analyst Ratings](https://stockanalysis.com/stocks/crex/ratings/)
  - Current and historical analyst ratings for Creative Realities (CREX) stock. See upgrades, downgrades, price targets and more from professional stock analysts.
- [Creative Realities (CREX) Stock Forecast and Price Target 2025](https://www.marketbeat.com/stocks/NASDAQ/CREX/forecast/)
  - CREX's current price target is $8.00. Learn why top analysts are making this stock forecast for Creative Realities at MarketBeat.Creative Realities - Analyst…
- [Why The Narrative Around Creative Realities (CREX) Is Evolving With Its New...](https://finance.yahoo.com/news/why-narrative-around-creative-realities-120741632.html)
  - What the New Price Target Means for Creative Realities Analysts have moved from having no published...
- [How The Creative Realities (CREX) Story Is Shifting With New Targets And Theater...](https://finance.yahoo.com/markets/stocks/articles/creative-realities-crex-story-shifting-080315391.html)
  - Creative Realities is back in focus after analysts revised their fair value price target from...
- [How Recent Developments Are Reframing The Creative Realities (CREX) Investment...](https://finance.yahoo.com/news/recent-developments-reframing-creative-realities-101051024.html)
  - Why the Price Target Moved While Fair Value Stayed Put The headline change for Creative Realities is...
- [How the Narrative Around Creative Realities Is Shifting After Recent Analyst...](https://finance.yahoo.com/news/narrative-around-creative-realities-shifting-200619688.html)
  - Creative Realities stock has recently seen its Fair Value Estimate rise from $7.44 to $8.13. This...
- [Creative Realities (CREX) Stock Forecast & Analyst Price Targets](https://stockanalysis.com/stocks/crex/forecast/)
  - Stock forecasts and analyst price target predictions for Creative Realities, Inc. (CREX) stock, with detailed revenue and earnings estimates.
- [CREX | Creative Realities Inc. Analyst Estimates & Ratings – WSJCreative Realities (CREX) Stock Price & OverviewCREX Stock Price Quote | MorningstarUpgrade - Personal Loans, Cards and Rewards Checking | HomeUpgrade - Personal Loans, Cards and Rewards Checking | UpgradeHow to Use Consensus in Claude (via MCP)](https://www.wsj.com/market-data/quotes/CREX/research-ratings)
  - Creative Realities Inc. analyst ratings, historical stock prices, earnings estimates & actuals. CREX updated stock price target summary. 18 hours ago · A det…
- [Creative Realities (CREX) Stock Price & OverviewCREX Stock Price Quote | MorningstarUpgrade - Personal Loans, Cards and Rewards Checking | HomeUpgrade - Personal Loans, Cards and Rewards Checking | UpgradeHow to Use Consensus in Claude (via MCP)](https://stockanalysis.com/stocks/crex/)
  - 18 hours ago · A detailed overview of Creative Realities, Inc. (CREX) stock, including real-time price, chart, key statistics, news, and more. See the latest…
- [CREX Stock Price Quote | MorningstarUpgrade - Personal Loans, Cards and Rewards Checking | HomeUpgrade - Personal Loans, Cards and Rewards Checking | UpgradeHow to Use Consensus in Claude (via MCP)](https://www.morningstar.com/stocks/xnas/crex/quote)
  - See the latest Creative Realities Inc stock price (CREX:XNAS), related news, valuation, dividends and more to help you make your investing decisions. We woul…

### Search warnings
- news:Creative Realities, Inc. stock rating OR consensus OR upgrade OR downgrade: No results found.
- news:CREX Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers analyst: No results found.
- news:CREX guidance OR investor day OR catalyst: No results found.

## Web research — web_drivers

- Queries: CREX Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers, Creative Realities, Inc. CREX outlook OR catalyst OR commodity OR uranium OR rare earth OR vanadium, CREX sector drivers OR market demand, Creative Realities, Inc. CREX backlog OR contract OR refinancing OR leverage
- Unique hits: 16
- Pages fetched: 0/3

### Web synthesis — web_drivers (rule-based fallback — Ollama unavailable)
**Keyword hits:** revenue, customer, service, market, network

- [HIT] Creative Realities Inc 's (CREX) Outlook - CSIMarket | csimarket.com | https://csimarket.com/stocks/technicals.php?code=CREX Creative Realities Inc latest News.
- | LBank | www.lbank.com | https://www.lbank.com/stock/crex CREX, or Creative Realities, Inc., operates as a provider of digital marketing technology solutions.Creative Realities, Inc.
- | MarketWatch | www.marketwatch.com | https://www.marketwatch.com/investing/stock/crex CREX | Complete Creative Realities Inc.
- [HIT] Creative Realities Inc Customers by Division and Industry - CSIMarket | csimarket.com | https://csimarket.com/stocks/CREX-Customers We currently market and sell our marketing technology solutions through our direct sales force and word-of-mouth referrals from existing customers.CREX's vs.
- (Revenue and Income for Trailing 12 Months, in Millions of $, except Employees).
- | www.earningsiq.co | https://www.earningsiq.co/articles/creative_realities_crex_q1_2026_10m_synergy_target_drives CREX is executing on the largest retail media network deployment in the U.S.
- | investorshub.advfn.com | https://investorshub.advfn.com/stock-market/NASDAQ/creative-realities-CREX/stock-price Creative Realities (CREX) stock price, charts, trades & the US's most popular discussion forums.
- - Benzinga | www.benzinga.com | https://www.benzinga.com/markets/penny-stocks/23/04/31685631/whats-going-on-with-creative-realities-stock Creative Realities, Inc.

### Sources found
- [UNIVERSITY OF LONDON THESIS Degree ^ | / \ f ) Y e a r 2 0 0 $](https://discovery.ucl.ac.uk/1444254/1/U591556.pdf)
  - This thesis is a study of the posthumous literary reception and reputation of. Alfred Tennyson, from the year of his death, 1892, to 1950. Its focus is on.
- [Untitled](https://cs.arizona.edu/~mercer/Projects/BoggleWords)
  - ... catalysts catalytic catalytics catalyze catalyzed catalyzes catalyzing ... deep deepen deepened deepening deepens deeper deepest deeply deepness ...
- [Case Studies in the Achievement of Air Superiority](https://media.defense.gov/2010/Oct/12/2001330116/-1/-1/0/AFD-101012-038.pdf)
  - Oct 12, 2010 ... ... dive bomber ............................ Yak-9 fighter ... scenarios for future war flowed from these assumptions.*”. Douhet stated ...
- [dictionary.txt](http://web.stanford.edu/class/archive/cs/cs106b/cs106b.1178/lectures/10-RecursiveBacktracking2/code/clumsyThumbsy/res/dictionary.txt)
  - ... catalysts catalytic catalytical catalytically catalyze catalyzed catalyzer ... deep deepen deepened deepener deepeners deepening deepens deeper deepest ...
- [Creative Realities Inc 's (CREX) Outlook - CSIMarket](https://csimarket.com/stocks/technicals.php?code=CREX)
  - Creative Realities Inc latest News. Financial Terms. CREX's Outlook.
- [Creative Realities, Inc. (CREX) Valuation Measures & Financial...](https://finance.yahoo.com/quote/CREX/key-statistics/)
  - Find out all the key statistics for Creative Realities, Inc. (CREX), including valuation measures, fiscal year financial statistics, trading record, share st…
- [Creative Realities Inc (CREX) Stock Price, Earnings... | LBank](https://www.lbank.com/stock/crex)
  - CREX, or Creative Realities, Inc., operates as a provider of digital marketing technology solutions.Creative Realities, Inc. has opportunities in the growing…
- [CREX Stock Price | Creative Realities Inc. Stock... | MarketWatch](https://www.marketwatch.com/investing/stock/crex)
  - CREX | Complete Creative Realities Inc. stock news by MarketWatch. View real-time stock prices and stock quotes for a full financial overview.
- [Creative Realities Inc Customers by Division and Industry - CSIMarket](https://csimarket.com/stocks/CREX-Customers)
  - We currently market and sell our marketing technology solutions through our direct sales force and word-of-mouth referrals from existing customers.CREX's vs.…
- [Creative Realities Inc (CREX) Stock News Today - TipRanks.com](https://www.tipranks.com/stocks/crex/stock-news)
  - NASDAQ:CREX. US Market. Stock Report.Sector Average60%. See how Bullish or Bearish a stock is based on its recent media coverage. This score is generated usi…
- [Creative Realities (CREX) Q1 2026: $10M Synergy Target Drives...](https://www.earningsiq.co/articles/creative_realities_crex_q1_2026_10m_synergy_target_drives)
  - CREX is executing on the largest retail media network deployment in the U.S. for 2026, with 10,000 screens and 20,000 analytics devices rolling out this year…
- [Creative Realities Stock Quote CREX - Stock Price, News, Charts...](https://investorshub.advfn.com/stock-market/NASDAQ/creative-realities-CREX/stock-price)
  - Creative Realities (CREX) stock price, charts, trades & the US's most popular discussion forums. Free forex prices, toplists, indices and lots more.

### Search warnings
- news:CREX Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers: No results found.
- news:Creative Realities, Inc. CREX outlook OR catalyst OR commodity OR uranium OR rare earth OR vanadium: No results found.
- news:CREX sector drivers OR market demand: No results found.
- news:Creative Realities, Inc. CREX backlog OR contract OR refinancing OR leverage: No results found.

## SEC filing [S23]
- Extraction OK: True
- Item 1 chars: 24018
- Item 1A chars: 50000
- Item 7 chars: 43243
- Meta: {'accession_number': '0001437749-26-012302', 'filing_date': '2026-04-15', 'source': 'edgartools', 'path': 'C:\\DevWork\\equity_research_agent\\data\\filings\\CREX_10k.txt'}

## Qualitative analysis (local LLM)

_Item 1 Business summary mode: rule_based (see Company setup & business model)._

### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin, supply chain, cyber, interest rate, customer, product, service, market, operations, network, subsidiary

- Our business involves a high degree of risk.
- In evaluating our business, you should carefully consider the specific risks described below, and any risks described in our other filings with the Securities and Exchange Commission (the“SEC”), pursuant to Sections 13(a), 13(c), 14, or 15(d) of the Exchange Act.
- Any of the risks we describe below or in our other filings with the SEC could cause our business, financial condition, results of operations or future prospects to be materially adversely  affected.
- In addition, some of these risks contain forward-looking statements.
- RISKS RELATED TO OUR BUSINESS AND OUR INDUSTRY  We have generally incurred losses, and may never become or remain profitable.
- We have incurred historical net losses, and we have had negative cash flows from operations.
- We have formulated our business plans and strategies based on certain assumptions regarding the acceptance of our business model and the marketing of our products and services.
- Nevertheless, our assessments regarding market size, market share, market acceptance of our products and services and a variety of other factors may prove incorrect.


### Item 7 — MD&A (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, uncertainty, regulation, revenue, margin, customer, segment, product, service, market, operations, network, subsidiary

- ’ S DISCUSSION AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERATIONS  (All currency is rounded to the nearest thousands, except share and per share amounts.)  The following discussion should be read in conjunction with the financial statements and related notes for the years ended December 31, 2025 and 2024, which are included elsewhere in this Report.
- This Management’s Discussion and Analysis of Financial Condition and Results of Operations contains statements that are forward-looking.
- These statements are based on current expectations and assumptions that are subject to risk, uncertainties and other factors.
- You should review the “Cautionary Note Regarding Forward-Looking Statements; Risk Factor Summary”, and “Risk Factors” sections of this Report for a discussion of important factors that could cause actual results to differ materially from the results described in or implied by the forward-looking statements described in the following discussion and analysis.
- Overview  The Company transforms environments through digital solutions by providing innovative digital signage solutions for key market segments and use cases, including:    Retail                              Entertainment and Sports Venues     Restaurants, including QSRs         Convenience Stores                  Financial Services                  Automotive                          Lottery                             Mixed Use Developments              DOOH Advertising Networks          We serve market-leading companies, so there is a good chance that if you leave your home today to shop, work, eat or play, you will encounter one or more of our digital signage experiences.
- Our solutions are increasingly visible because we help our enterprise customers achieve a range of business objectives including:    Increased brand awareness;    ──────────────────────────────  20      Improved customer support;                           Enhanced employee productivity and satisfaction;     Increased revenue and profitability;                 Improved guest experience; and                       Increased customer/guest engagement.
- Traffic content and advertising                     Through a combination of organically grown platforms and a series of strategic acquisitions, the Company assists customers to design, deploy, manage, and monetize their digital signage and in-store retail media networks.
- The Company sources leads and opportunities for its solutions through its digital and content marketing initiatives, close relationships with key industry partners, specifically equipment manufacturers, and the direct efforts of its in-house industry sales experts.


## Research loop (think → act)

1. _heuristic_ — Coverage looks adequate for this pass; stopping iterative loop.

## Sources

- **[S1]** CREX fundamentals (yfinance)
  - Creative Realities, Inc.: price=3.11, rev=57232000.0, fcf=-10244000.0, shares=13097892.0, rev_cagr=0.09702520767150968, ROIC=-0.04009801544695737, FCF yield=-0.2514825045850632
- **[S2]** CREX EV/EBITDA valuation (multiples)
  - Base implied price=0.6179620354176076, multiple=40.0
- **[S3]** CREX DCF valuation (dcf)
  - Base share price=-2.351755156061878, bull=6.783857023575285, bear=-4.565007007607608
- **[S4]** CREX peer comps (peers)
  - Peers: MSFT, ORCL, ADBE, CRM, NOW; rows=6
- **[S5]** CREX earnings history (earnings)
  - rows=12; next=2026-08-12
- **[S6]** Creative Realities (CREX) Stock Forecast, Price Targets and... (web) — https://www.tipranks.com/stocks/crex/forecast
  - Analyze Forecast. Average Price Target.The highest analyst price target is $9.00 ,the lowest forecast is $9.00. The average price target represents 138.73% Increase from the cur…
- **[S7]** CREX Forecast — Price Target — Prediction for 2027 — TradingView (web) — https://www.tradingview.com/symbols/NASDAQ-CREX/forecast/
  - Price target. 8.130.000.00%. The 4 analysts offering 1-year price forecasts have a max estimate of — and a min estimate of —. Analyst rating. Based on 4 analysts giving stock ra…
- **[S8]** Creative Realities (CREX) Analyst Ratings (web) — https://stockanalysis.com/stocks/crex/ratings/
  - Current and historical analyst ratings for Creative Realities (CREX) stock. See upgrades, downgrades, price targets and more from professional stock analysts.
- **[S9]** Creative Realities (CREX) Stock Forecast and Price Target 2025 (web) — https://www.marketbeat.com/stocks/NASDAQ/CREX/forecast/
  - CREX's current price target is $8.00. Learn why top analysts are making this stock forecast for Creative Realities at MarketBeat.Creative Realities - Analysts' Recommendations a…
- **[S10]** Why The Narrative Around Creative Realities (CREX) Is Evolving With Its New... (web) — https://finance.yahoo.com/news/why-narrative-around-creative-realities-120741632.html
  - What the New Price Target Means for Creative Realities Analysts have moved from having no published...
- **[S11]** How The Creative Realities (CREX) Story Is Shifting With New Targets And Theater... (web) — https://finance.yahoo.com/markets/stocks/articles/creative-realities-crex-story-shifting-080315391.html
  - Creative Realities is back in focus after analysts revised their fair value price target from...
- **[S12]** How Recent Developments Are Reframing The Creative Realities (CREX) Investment... (web) — https://finance.yahoo.com/news/recent-developments-reframing-creative-realities-101051024.html
  - Why the Price Target Moved While Fair Value Stayed Put The headline change for Creative Realities is...
- **[S13]** How the Narrative Around Creative Realities Is Shifting After Recent Analyst... (web) — https://finance.yahoo.com/news/narrative-around-creative-realities-shifting-200619688.html
  - Creative Realities stock has recently seen its Fair Value Estimate rise from $7.44 to $8.13. This...
- **[S14]** CREX Forecast — Price Target — Prediction for 2027 — TradingView (web_page) — https://www.tradingview.com/symbols/NASDAQ-CREX/forecast/
  - CREX Forecast — Price Target — Prediction for 2027 — TradingView Search EN Get started Creative Realities, Inc. CREX Nasdaq Stock Market CREX Nasdaq Stock Market CREX Nasdaq Sto…
- **[S15]** UNIVERSITY OF LONDON THESIS Degree ^ | / \ f ) Y e a r 2 0 0 $ (web) — https://discovery.ucl.ac.uk/1444254/1/U591556.pdf
  - This thesis is a study of the posthumous literary reception and reputation of. Alfred Tennyson, from the year of his death, 1892, to 1950. Its focus is on.
- **[S16]** Untitled (web) — https://cs.arizona.edu/~mercer/Projects/BoggleWords
  - ... catalysts catalytic catalytics catalyze catalyzed catalyzes catalyzing ... deep deepen deepened deepening deepens deeper deepest deeply deepness ...
- **[S17]** Case Studies in the Achievement of Air Superiority (web) — https://media.defense.gov/2010/Oct/12/2001330116/-1/-1/0/AFD-101012-038.pdf
  - Oct 12, 2010 ... ... dive bomber ............................ Yak-9 fighter ... scenarios for future war flowed from these assumptions.*”. Douhet stated ...
- **[S18]** dictionary.txt (web) — http://web.stanford.edu/class/archive/cs/cs106b/cs106b.1178/lectures/10-RecursiveBacktracking2/code/clumsyThumbsy/res/dictionary.txt
  - ... catalysts catalytic catalytical catalytically catalyze catalyzed catalyzer ... deep deepen deepened deepener deepeners deepening deepens deeper deepest ...
- **[S19]** Creative Realities Inc 's (CREX) Outlook - CSIMarket (web) — https://csimarket.com/stocks/technicals.php?code=CREX
  - Creative Realities Inc latest News. Financial Terms. CREX's Outlook.
- **[S20]** Creative Realities, Inc. (CREX) Valuation Measures & Financial... (web) — https://finance.yahoo.com/quote/CREX/key-statistics/
  - Find out all the key statistics for Creative Realities, Inc. (CREX), including valuation measures, fiscal year financial statistics, trading record, share statistics and more.
- **[S21]** Creative Realities Inc (CREX) Stock Price, Earnings... | LBank (web) — https://www.lbank.com/stock/crex
  - CREX, or Creative Realities, Inc., operates as a provider of digital marketing technology solutions.Creative Realities, Inc. has opportunities in the growing adoption of digital…
- **[S22]** CREX Stock Price | Creative Realities Inc. Stock... | MarketWatch (web) — https://www.marketwatch.com/investing/stock/crex
  - CREX | Complete Creative Realities Inc. stock news by MarketWatch. View real-time stock prices and stock quotes for a full financial overview.
- **[S23]** CREX 10-K (sec)
  - Item 1 chars=24018, Item 1A chars=50000, Item 7 chars=43243, ok=True, source=edgartools
- **[S24]** CREX 8-K 2026-06-30 (sec) — https://www.sec.gov/Archives/edgar/data/1356093/000143774926022083/crex20260626c_8k.htm
  - FORM 8-K
- **[S25]** CREX 8-K 2026-06-29 (sec) — https://www.sec.gov/Archives/edgar/data/1356093/000143774926021905/crex20260625_8k.htm
  - FORM 8-K
- **[S26]** CREX 10-Q 2026-05-15 (sec) — https://www.sec.gov/Archives/edgar/data/1356093/000143774926017219/crex20260331c_10q.htm
  - FORM 10-Q
- **[S27]** CREX 8-K 2026-05-15 (sec) — https://www.sec.gov/Archives/edgar/data/1356093/000143774926017218/crex20260513_8k.htm
  - FORM 8-K
- **[S28]** CREX 10-K 2026-04-15 (sec) — https://www.sec.gov/Archives/edgar/data/1356093/000143774926012302/crex20251231c_10k.htm
  - FORM 10-K
- **[S29]** CREX 8-K 2026-04-14 (sec) — https://www.sec.gov/Archives/edgar/data/1356093/000143774926012193/crex20260413_8k.htm
  - FORM 8-K
- **[S30]** CREX 8-K 2026-02-18 (sec) — https://www.sec.gov/Archives/edgar/data/1356093/000143774926004453/crex20260218_8k.htm
  - FORM 8-K
- **[S31]** CREX 8-K 2026-01-02 (sec) — https://www.sec.gov/Archives/edgar/data/1356093/000143774926000084/crex20260102_8k.htm
  - FORM 8-K
- **[S32]** Item 1 Business summary (nlp)
  - ### Item 1 — Business (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, regulation, competition, guidance, revenue, margin, customer, segment, product, service,…
- **[S33]** Item 1A summary (nlp)
  - ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin, supply chain, cy…
- **[S34]** Item 7 summary (nlp)
  - ### Item 7 — MD&A (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, regulation, revenue, margin, customer, segment, product, service, market, opera…
- **[S35]** CREX scenario price ranges (scenarios)
  - ok=True; base mid=1.4558067817325109; headwinds=7; tailwinds=8
- **[S36]** CREX driver analysis (drivers)
  - ok=True; drivers=7
- **[S37]** CREX memo sections (memo)
  - mode=rules; proxies=2

## Self-critique

_Automated review (heuristic)._

### Strengths
- Combines local fundamentals, optional DCF scenarios, and cited sources where available.
- Keeps a non-advisory framing for local research drafts.

### Issues & gaps
- Base-case model equity value is negative - treat intrinsic-value output as stress/distress, not a buy signal.
- Base-case implies deep downside vs spot (<-70%); confirm whether near-term FCF normalization is appropriate for this business.

### Caution for readers
- Treat scenario prices as sensitivity output, not a forecast.
- Re-check primary filings and fresh market data before any decision.



---

# Template: Valuation (DCF + Street + drivers) (`valuation`)

# CREX — Planned Research Report

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
- Company: Creative Realities, Inc.
- Sector / industry: Technology / Software - Application
- Price: 3.11
- 52-week range: $2.19 – $4.42
- Market cap: $40.73M
- Enterprise value: $129.24M
- Shares outstanding: 13.10M
- Beta: 1.458
- Book equity: $49.19M
- Revenue (latest): $57.23M
- EBITDA (latest): $1.86M
- Free cash flow (latest): -$10.24M
- Operating income: -$3.15M
- Operating margin: -5.5%
- EV / EBITDA: 69.5x
- ROIC: -4.0%
- FCF yield: -25.1%
- Debt / Equity: 1.3797625340544057
- FCF / share: -$0.78
- Revenue / share: $4.37

### Capital structure
- Cash: $1.56M
- Short-term debt: $4.43M
- Long-term debt: $39.52M
- Total debt: $67.86M
- Net debt: $66.31M
- Net debt / EBITDA: 35.6x

### Growth
- Revenue CAGR: 9.7%
- FCF CAGR: —
- Latest revenue YoY: 12.5%
- Latest FCF YoY: -1866.2%

### Market expectations (yfinance, sparse)
- Mean target: $8.17
- Target range: $7.00 – $10.00
- Recommendation: strong_buy

_Consensus revenue/EBITDA forecasts are often unavailable via free feeds; treat targets as point-in-time only._

### Historical KPIs (multi-year)

| Year | Revenue | OCF | Capex | FCF | EBITDA | LT debt | Cash | Net debt | Net income |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2025 | $57.23M | -$7.75M | $2.49M | -$10.24M | $1.86M | $39.52M | $1.56M | $37.96M | -$8.28M |
| 2024 | $50.85M | $3.38M | $2.80M | $580.00K | $2.45M | $13.04M | $1.04M | $12.01M | -$3.51M |
| 2023 | $45.17M | $5.17M | $4.03M | $1.14M | $3.36M | $9.83M | $2.91M | $6.92M | -$2.94M |
| 2022 | $43.35M | -$708.00K | $4.29M | -$5.00M | $7.53M | $13.07M | $1.63M | $11.44M | $1.88M |

## Charts

### Revenue & FCF history
![Revenue & FCF history](/charts/CREX_valuation_revenue_fcf.png)

### DCF scenario prices
![DCF scenario prices](/charts/CREX_valuation_dcf_scenarios.png)

### Base-case FCF path
![Base-case FCF path](/charts/CREX_valuation_base_fcf_path.png)

### EV/EBITDA scenario prices
![EV/EBITDA scenario prices](/charts/CREX_valuation_ev_ebitda_scenarios.png)

### Headwind/tailwind price ranges
![Headwind/tailwind price ranges](/charts/CREX_valuation_scenario_ranges.png)

## DCF valuation (base / bull / bear) [S2]

> Simplified revenue->FCF DCF. Not investment advice; assumptions are editable heuristics.

- Spot price: $3.11
- Base revenue: $57.23M
- Shares: 13,097,892
- Net debt (Debt−Cash): $66.31M

| Scenario | Growth | FCF margin | WACC | Term. g | Equity value | Share price | Upside |
|----------|--------|------------|------|---------|--------------|-------------|--------|
| bear | 5.5% | 1.0% | 12.0% | 1.5% | -$59.79M | $-4.57 | -246.8% |
| base | 12.5% | 3.0% | 10.0% | 2.5% | -$30.80M | $-2.35 | -175.6% |
| bull | 19.5% | 8.0% | 9.0% | 3.0% | $88.85M | $6.78 | 118.1% |

### Assumption notes
- Base revenue growth seeded from historical rate (12.5%).
- Latest FCF margin was -17.9%; scenarios use normalized positive margins for a going-concern DCF.

- _base: model equity value is negative after net debt (-30,803,035); showing $-2.35/sh._
- _bear: model equity value is negative after net debt (-59,791,969); showing $-4.57/sh._

### Base-case projected FCF

- Year 1: revenue $64.41M, FCF $1.93M (PV $1.76M)
- Year 2: revenue $72.49M, FCF $2.17M (PV $1.80M)
- Year 3: revenue $81.58M, FCF $2.45M (PV $1.84M)
- Year 4: revenue $91.81M, FCF $2.75M (PV $1.88M)
- Year 5: revenue $103.33M, FCF $3.10M (PV $1.92M)
- Terminal value $42.36M (PV $26.30M)

## Valuation — EV/EBITDA scenarios [S3]

> Priced-in model: implied price = (EBITDA × EV/EBITDA − net debt) ÷ shares. Not a forecast.

- Spot: $3.11
- Net debt used: $66.31M

| Scenario | EBITDA | EV/EBITDA | Implied EV | Equity value | Implied price |
|---|---:|---:|---:|---:|---:|
| bear | $1.30M | 30.0x | $39.06M | -$27.25M | $-2.08 |
| base | $1.86M | 40.0x | $74.40M | $8.09M | $0.62 |
| bull | $2.23M | 45.0x | $100.44M | $34.13M | $2.61 |

- Base EBITDA seeded from latest reported/TTM figure (1,860,000).
- Base multiple seeded from current EV/EBITDA (69.5x).

## Scenario price ranges (headwinds & tailwinds) [S26]

> Medium-term (18–36 months (medium / medium-long term)) driver → EV/EBITDA bridge. Distinct from the FCF DCF path. Not investment advice.

- Spot: $3.11
- Sparse Street mean target: $8.17
- Anchor multiple: 45.0x (driver_ev_ebitda_bridge)
- Anchor EBITDA: $1.86M
- Probability-weighted midpoint: **$0.42** (heuristic weights, not a rating)
- Driver extraction: `rules`

### Headwinds (bear-case fuel)

- **Elevated leverage (ND/EBITDA)** — Net debt / EBITDA ≈ 35.6x — refinancing and equity duration risk _(source: fundamentals)_
- **Negative free cash flow** — Latest FCF -$10.24M — cash burn raises financing risk _(source: fundamentals)_
- **Balance-sheet / refinancing pressure** — sector=Technology industry=Software - Application revenue=57232000.0 ebitda=1860000.0 fcf=-10244000.0 net_debt=66306000.0 nd_ebitda=35.648387096774194 target=8.16667 rec=strong_buy _(source: fundamentals)_
- **Regulatory / legal risk** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin, supply chain, cyber _(source: item_1a)_
- **Competitive / pricing pressure** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin, supply chain, cyber _(source: item_1a)_
- **Margin / cost headwind** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin, supply chain, cyber _(source: item_1a)_
- **Operational / cyber risk** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin, supply chain, cyber _(source: item_1a)_

### Tailwinds (bull-case fuel)

- **Revenue growth momentum** — Latest revenue YoY ≈ 12.5% _(source: fundamentals)_
- **Street target implies upside** — Mean target $8.17 vs spot $3.11 _(source: fundamentals)_
- **Product / pricing power** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin, supply chain, cyber _(source: item_1a)_
- **Contract / backlog wins** — ### Item 7 — MD&A (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, regulation, revenue, margin, customer, segment, product, service, market, operatio _(source: item_7)_
- **Growth / execution upside** — Creative Realities (CREX) News Today - MarketBeat What's going on at Creative Realities (NASDAQ:CREX)? Read today's CREX news from trusted media outlets at MarketBeat. _(source: web)_

### Price ranges by case

| Case | Prob. | Metric vs TTM | Multiple | Price low | Mid | High | Upside vs spot |
|---|---:|---:|---:|---:|---:|---:|---:|
| bear | 0.34 | 0.70x | 27.9x | $-2.57 | $-2.29 | $-2.01 | -174% |
| base | 0.45 | 0.96x | 45.0x | $0.64 | $1.07 | $1.50 | -66% |
| bull | 0.21 | 1.19x | 50.0x | $2.54 | $3.39 | $4.23 | +9% |

#### Bear — headwinds dominate

Headwinds bite: weaker operating trajectory and multiple compression. Equity duration shrinks if cash generation fails to offset leverage / competitive pressure.

- **Range:** $-2.57 – $-2.01 (mid $-2.29) · EBITDA $1.30M · multiple 27.9x
- Driver: **Elevated leverage (ND/EBITDA)** — Net debt / EBITDA ≈ 35.6x — refinancing and equity duration risk
- Driver: **Negative free cash flow** — Latest FCF -$10.24M — cash burn raises financing risk
- Driver: **Balance-sheet / refinancing pressure** — sector=Technology industry=Software - Application revenue=57232000.0 ebitda=1860000.0 fcf=-10244000.0 net_debt=66306000.0 nd_ebitda=35.648387096774194 target=8.
- Driver: **Regulatory / legal risk** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin,
- Driver: **Competitive / pricing pressure** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin,

#### Base — mixed execution

Balanced path: some tailwinds offset headwinds. Operating scale roughly holds with modest repair/normalization; valuation stays near the current EV/EBITDA anchor.

- **Range:** $0.64 – $1.50 (mid $1.07) · EBITDA $1.79M · multiple 45.0x
- Driver: **Revenue growth momentum** — Latest revenue YoY ≈ 12.5%
- Driver: **Street target implies upside** — Mean target $8.17 vs spot $3.11
- Driver: **Elevated leverage (ND/EBITDA)** — Net debt / EBITDA ≈ 35.6x — refinancing and equity duration risk
- Driver: **Negative free cash flow** — Latest FCF -$10.24M — cash burn raises financing risk

#### Bull — tailwinds dominate

Tailwinds compound: operating improvement plus a re-rating toward peer or recovery multiples as balance-sheet and growth narratives improve.

- **Range:** $2.54 – $4.23 (mid $3.39) · EBITDA $2.21M · multiple 50.0x
- Driver: **Revenue growth momentum** — Latest revenue YoY ≈ 12.5%
- Driver: **Street target implies upside** — Mean target $8.17 vs spot $3.11
- Driver: **Product / pricing power** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin,
- Driver: **Contract / backlog wins** — ### Item 7 — MD&A (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, regulation, revenue, margin, customer, segment, product, servi
- Driver: **Growth / execution upside** — Creative Realities (CREX) News Today - MarketBeat What's going on at Creative Realities (NASDAQ:CREX)? Read today's CREX news from trusted media outlets at Mark

### Method notes

- Item 1A risks weighted toward headwinds.
- Mapping follows Gemini/Perplexity-style scenario memos: qualitative drivers → operating metric & multiple paths → share-price ranges over a medium-term horizon.

## Web research — web_analysts

- Queries: CREX analyst price target, Creative Realities, Inc. stock rating OR consensus OR upgrade OR downgrade, CREX Estimate intrinsic value under base / bull / bear scenarios analyst
- Unique hits: 14
- Pages fetched: 1/3

### Web synthesis — web_analysts (rule-based fallback — Ollama unavailable)
**Keyword hits:** customer, service, market

- [HIT] Creative Realities (CREX) Stock Forecast and Price Target 2026 | www.marketbeat.com | https://www.marketbeat.com/stocks/NASDAQ/CREX/forecast/ CREX's current price target is $0.00.
- Learn why top analysts are making this stock forecast for Creative Realities at MarketBeat.
- · via Yahoo Finance | https://finance.yahoo.com/markets/stocks/articles/creative-realities-crex-story-shifting-080315391.html Creative Realities is back in focus after analysts revised their fair value price target from...
- [HIT] Analysts Offer Insights on Technology Companies: Creative Realities (CREX) and Applied Digital Corporation (APLD) | The Globe and Mail | https://www.theglobeandmail.com/investing/markets/stocks/CREX/pressreleases/3376489/analysts-offer-insights-on-technology-companies-creative-realities-crex-and-applied-digital-corporation-apld/ Detailed price information for Creative Realities Inc (CREX-Q) from The Globe and Mail including charting and trades.
- [HIT] CREX Stock Quote Price and Forecast - CNN | www.cnn.com | https://www.cnn.com/markets/stocks/CREX Creative Realities, Inc.
- [PAGE] Creative Realities (CREX) Stock Forecast and Price Target 2026 | https://www.marketbeat.com/stocks/NASDAQ/CREX/forecast/ Creative Realities (CREX) Stock Forecast and Price Target 2026 Skip to main content → My top 3 AI picks for the next decade (From The Oxford Club) (Ad) Free CREX Stock Alerts Creative Realities (CREX)  Stock Forecast & Price Target $3.11 -0.09 (-2.81%) Closing price 07/27/2026 04:00 PM Eastern Extended Trading $3.16 +0.04 (+1.45%) As of 07/27/2026 07:59 PM Eastern Extended trading is trading that happens on electronic markets outside of regular trading hours.
- This is a fair market value extended hours price provided by Massive.
- Add Compare Share Share Analyst Forecasts Stock Analysis Analyst Forecasts Chart Competitors Earnings Financials Headlines Insider Trades Ownership SEC Filings Trends Buy This Stock Creative Realities - Analysts' Recommendations and Stock Price Forecast (2026) How MarketBeat Calculates Price Target and Consensus Rating Consensus Rating Hold Based on 3 Analyst Ratings Sell 1 Hold 1 Buy 1 Based on 3 Wall Street analysts who have issued ratings for Creative Realities in the last 12 months ,  the stock has a consensus rating of "Hold." Out of the 3 analysts, 1 has given a sell rating, 1 has given a hold rating, and 1 has given a buy rating for  CREX.

### Sources found
- [Creative Realities (CREX) Stock Forecast, Price Targets ... - TipRanks](https://www.tipranks.com/stocks/crex/forecast)
  - Based on 2 Wall Street analysts offering 12 month price targets for Creative Realities in the last 3 months. The average price target is $9.00 with a high ...
- [CREX Stock Forecast & Price Target | Creative Realities Inc (CREX)](https://valueinvesting.io/CREX/estimates)
  - The average stock forecast for Creative Realities Inc (CREX) is 8.80 USD. This price target corresponds to an upside of 174.92%. The range of stock ...
- [Creative Realities (CREX) Stock Forecast and Price Target 2026](https://www.marketbeat.com/stocks/NASDAQ/CREX/forecast/)
  - CREX's current price target is $0.00. Learn why top analysts are making this stock forecast for Creative Realities at MarketBeat.
- [CREX Forecast — Price Target — Prediction for 2027 - TradingView](https://www.tradingview.com/symbols/NASDAQ-CREX/forecast-price-target/)
  - The current price of CREX is 3.16 USD — it has decreased by −4.76% in the past 24 hours. Watch Creative Realities, Inc. stock price performance more closely …
- [Why The Narrative Around Creative Realities (CREX) Is Evolving With Its New...](https://finance.yahoo.com/news/why-narrative-around-creative-realities-120741632.html)
  - What the New Price Target Means for Creative Realities Analysts have moved from having no published...
- [How The Creative Realities (CREX) Story Is Shifting With New Targets And Theater...](https://finance.yahoo.com/markets/stocks/articles/creative-realities-crex-story-shifting-080315391.html)
  - Creative Realities is back in focus after analysts revised their fair value price target from...
- [How Recent Developments Are Reframing The Creative Realities (CREX) Investment...](https://finance.yahoo.com/news/recent-developments-reframing-creative-realities-101051024.html)
  - Why the Price Target Moved While Fair Value Stayed Put The headline change for Creative Realities is...
- [Analysts Offer Insights on Technology Companies: Creative Realities (CREX) and Applied Digital Corporation (APLD)](https://www.theglobeandmail.com/investing/markets/stocks/CREX/pressreleases/3376489/analysts-offer-insights-on-technology-companies-creative-realities-crex-and-applied-digital-corporation-apld/)
  - Detailed price information for Creative Realities Inc (CREX-Q) from The Globe and Mail including charting and trades.
- [Creative Realities, Inc. (CREX) Stock Price, News, Quote & History](https://finance.yahoo.com/quote/CREX/)
  - Creative Realities, Inc. (CREX) ... As of 12:24:07 PM EDT. Market Open.
- [CREX Stock Quote Price and Forecast - CNN](https://www.cnn.com/markets/stocks/CREX)
  - Creative Realities, Inc. ... CREX is trading in the middle of its 52-week range and below its 200-day simple moving average. ... The price of CREX shares has…
- [CREX (CREX) Intrinsic Value & DCF Model 2026 | VCP Scanner](https://vcpscanner.com/valuation/crex/dcf)
  - CREX (CREX) intrinsic value, DCF Model, and fair value analysis. See bear, base, and bull case scenarios with full assumptions. Updated 2026.
- [Intrinsik — Stock Valuation Tool | Fair Value in 60 Seconds](https://intrinsik.io/)
  - Fair value. Any stock. 60 seconds. Enter a ticker. Intrinsik reads the SEC filings, builds a full DCF model with bear, base & bull scenarios, and delivers in…

### Search warnings
- news:Creative Realities, Inc. stock rating OR consensus OR upgrade OR downgrade: No results found.
- news:CREX Estimate intrinsic value under base / bull / bear scenarios analyst: No results found.

## Web research — web_drivers

- Queries: CREX Estimate intrinsic value under base / bull / bear scenarios, Creative Realities, Inc. CREX outlook OR catalyst OR commodity OR uranium OR rare earth OR vanadium, CREX sector drivers OR market demand
- Unique hits: 10
- Pages fetched: 1/3

### Web synthesis — web_drivers (rule-based fallback — Ollama unavailable)
**Keyword hits:** revenue, customer, service, market

- Compared to the current market price of 3.57 USD, the stock is Undervalued by 52%.Base Case Scenario.
- [HIT] Creative Realities (CREX) Earnings Date and Reports 2026 | www.marketbeat.com | https://www.marketbeat.com/stocks/NASDAQ/CREX/earnings/ CREX Upcoming Earnings.
- Analyst Estimates | MarketWatch | www.marketwatch.com | https://www.marketwatch.com/investing/stock/crex/analystestimates CREX Analyst Estimates.
- [HIT] Creative Realities (CREX) News Today - MarketBeat | www.marketbeat.com | https://www.marketbeat.com/stocks/NASDAQ/CREX/news/ What's going on at Creative Realities (NASDAQ:CREX)?
- Read today's CREX news from trusted media outlets at MarketBeat.
- [HIT] Creative Realities (CREX) Stock Forecast and Price Target 2026 | www.marketbeat.com | https://www.marketbeat.com/stocks/NASDAQ/CREX/forecast/ Based on 3 Wall Street analysts who have issued ratings for Creative Realities in the last 12 months, the stock has a consensus rating of "Hold.
- The residual demand curve is the market demand that is not met by other firms in the industry at a given price.
- The residual demand curve is the market demand curve D (p), minus the supply of other organizations, So (p): Dr (p) = D (p) - So (p) [14]  [HIT] 3.1 Demand, Supply, and Equilibrium in Markets for Goods and ...

### Sources found
- [CREX DCF Valuation - Creative Realities Inc - Alpha Spread](https://www.alphaspread.com/security/nasdaq/crex/dcf-valuation)
  - Estimated DCF Value of one CREX stock is 7.36 USD. Compared to the current market price of 3.57 USD, the stock is Undervalued by 52%.Base Case Scenario. The …
- [Creative Realities (CREX) Earnings Date and Reports 2026](https://www.marketbeat.com/stocks/NASDAQ/CREX/earnings/)
  - CREX Upcoming Earnings. Creative Realities' next earnings date is estimated for Wednesday, August 12, 2026, based on past reporting schedules.
- [CREX | Creative Realities Inc. Analyst Estimates | MarketWatch](https://www.marketwatch.com/investing/stock/crex/analystestimates)
  - CREX Analyst Estimates. Snapshot. Average Recommendation.Current Year's Estimate. -0.64. Median PE on CY Estimate.
- [Creative Realities Inc. (CREX) Live Share Price, Invest From India](https://www.indmoney.com/us-stocks/creative-realities-inc-share-price-crex)
  - Creative Realities Inc. share touched a 52 week high of $4.42 on April 21, 2026 and a 52 week low of $2.19 on August 20, 2025 .
- [Creative Realities (CREX) News Today - MarketBeat](https://www.marketbeat.com/stocks/NASDAQ/CREX/news/)
  - What's going on at Creative Realities (NASDAQ:CREX)? Read today's CREX news from trusted media outlets at MarketBeat.
- [Creative Realities (CREX) Stock Forecast and Price Target 2026](https://www.marketbeat.com/stocks/NASDAQ/CREX/forecast/)
  - Based on 3 Wall Street analysts who have issued ratings for Creative Realities in the last 12 months, the stock has a consensus rating of "Hold.
- [Demand - Wikipedia](https://en.wikipedia.org/wiki/Demand)
  - The demand curve facing a particular firm is called the residual demand curve. The residual demand curve is the market demand that is not met by other firms …
- [3.1 Demand, Supply, and Equilibrium in Markets for Goods and ...](https://openstax.org/books/principles-economics-3e/pages/3-1-demand-supply-and-equilibrium-in-markets-for-goods-and-services)
  - We can show an example from the market for gasoline in a table or a graph. Economists call a table that shows the quantity demanded at each price, such as Ta…
- [Understanding Demand: Key Determinants and the Demand Curve](https://www.investopedia.com/terms/d/demand.asp)
  - Apr 7, 2026 · Market demand is the total quantity demanded by all consumers in a market for a given good, and aggregate demand is the total demand for all go…
- [Market Demand: Definition, How to Calculate, Determinants](https://penpoin.com/market-demand/)
  - Jan 21, 2025 · What’s it: Market demand is the sum of individual demand in the market at a given price. Economists define demand as our willingness and abili…

### Search warnings
- news:CREX Estimate intrinsic value under base / bull / bear scenarios: No results found.
- news:Creative Realities, Inc. CREX outlook OR catalyst OR commodity OR uranium OR rare earth OR vanadium: No results found.
- news:CREX sector drivers OR market demand: No results found.

## SEC filing [S22]
- Extraction OK: True
- Item 1 chars: 24018
- Item 1A chars: 50000
- Item 7 chars: 43243
- Meta: {'source': 'cache', 'path': 'C:\\DevWork\\equity_research_agent\\data\\filings\\CREX_10k.txt'}

## Company setup & business model

**Keyword hits:** risk, regulation, competition, guidance, revenue, margin, customer, segment, product, service, market, operations, network, subsidiary

- (“Creative Realities”, the “Company”, “we”, “us” or “our”) provides innovative digital signage and media solutions in North America to enhance communications in a wide-ranging variety of out-of-home environments, key market segments and use cases, including:    Retail                                                     Entertainment and Sports Venues                            Restaurants, including quick-serve restaurants (“QSR”)     Convenience Stores                                         Financial Services                                         Automotive                                                 Lottery                                                    Mixed Use Developments                                     Digital out of Home (“DOOH”) Advertising Networks         We serve market-leading companies, so there is a good chance that if you leave your home today to shop, work, eat or play, you will encounter one or more of our digital signage experiences.
- Our solutions are increasingly viable because we help our enterprise customers achieve a wide range of business objectives including:    Increased brand awareness/engagement               ───────────────────────────────────────────────────   Improved customer support                           Enhanced employee productivity and satisfaction     Increased revenue and profitability                 Improved guest experience                           Increased customer/guest engagement                 Traffic content and advertising                    Through a combination of organically grown platforms and a series of strategic acquisitions, the Company assists customers to design, deploy, manage, and monetize their digital signage and in-store retail media networks.
- The Company sources leads and opportunities for its solutions through its digital and content marketing initiatives, close relationships with key industry partners, equipment manufacturers, and the direct efforts of its in-house industry sales experts.
- Customer engagements focus on consultative conversations that ensure the Company’s solutions are positioned to help customers achieve their business objectives in the most cost-effective manner possible.
- When comparing Creative Realities to other digital signage competitors, our customers value the following competitive advantages:    Breadth of solutions – Creative Realities offers true solutions to our customers.
- 1      Managed labor pool – Unlike most companies in our industry, we have a curated labor pool of qualified and vetted field technicians available to service customers quickly nationwide.
- In-house creative resources – We assist customers in creating new content or repurposing existing content for digital signage experiences, an activity for which the Company has won several desi...
- Network scalability and reliability – Our software as a service (“SaaS”) content management platforms power some of the largest and most complex digital signage networks in North America, evide...
- Market sector expertise – Creative Realities has in-house experts in key market segments such as retail, quick-serve restaurants (“QSR”), convenience stores, and Digital Out of Home (“DOOH”) ad...
- Technical support – Digital signage networks present unique challenges for corporate IT departments.
- We simplify and improve end user support by leveraging our own Network Operations Center (“N...
- Retail Media Network – The Company owns and operates the largest mall shopping network in Canada.
- The three primary sources of revenue for the Company are:    Hardware sales from reselling digital signage hardware from original equipment manufacturers such as Samsung and BrightSign.
- Services revenue from helping customers design, deploy and manage their digital signage and in-store retail media networks, including:      Hardware system design/engineering     Hardware installation                  Content development                   2      Content scheduling                                                                       Post-deployment network and field support                                                AdTech to traffic advertising and content directly and through programmatic channels      Recurring subscription licensing and support revenue from our digital signage software platforms, which are generally sold via a SaaS model.
- Our platforms include:      ReflectView, the Company’s core digital signage platform for most applications, scalable and cost effective from 10 to 100,000+ devices;                                                                 Reflect Xperience, a web-based interface that allows customers to give content scheduling access to local users via the web or mobile devices, while still maintaining centralized programming co...
- AdLogic, the Company’s AdTech management platform for digital signage networks, which presently delivers approximately 50 million ads daily;                                                             CPM+, the Company’s demand side and supply side platform with campaign management and extensive capabilities for programmatic advertising;                                                               Clarity, the Company’s digital signage platform for menu board solutions, which has become a market leader for a range of restaurant, including QSR and convenience store applications; and              iShowroomProX, an omni-channel digital sales support platform targeted at original equipment manufacturers in the transportation sector, which integrates with dozens of key data services includ...
- While hardware sales and support services revenues can fluctuate more significantly year over year based on new, large-scale network deployments, the Company is focusing on maintaining and increasing recurring SaaS revenue as digital signage adoption/utilization expands across the vertical markets we serve.
- Flat panel displays, along with LED technology and digital media players typically constitute a large portion of the expenditure customers make relative to the entire cost of implementing a digital  marketing system implementation and can be a barrier to customer deployment.
- As a result, we believe that the broader adoption of digital marketing technology solutions is likely to increase, although we cannot predict the rate at which such adoption will occur.
- We believe the proliferation of in-store retail media networks will be an industrial catalyst for infrastructure and AdTech sales for which the Company is well situated from product set and technology stack standpoints.
- We believe that the selective acquisition and successful integration of certain companies will: accelerate our growth in targeted vertical and operating markets; enable us to cost-effectively aggregate multiple customer bases onto a single business and technology platform; provide us with greater operating scale on a consolidated basis; enable us to leverage a common set of processes and tools, and cost efficiencies company-wide; and ultimately result in higher operating profitability and cash flow from operations.
- Business Strategy  We believe that our existing business model is highly scalable and can be expanded successfully as we continue to grow organically, seek to acquire and integrate other companies in our target markets, strengthen our operational practices and procedures, further streamline our administrative office functions, and continue to capitalize on various marketing programs and activities.
- With a focus on SaaS revenues, we believe that our gross margins will rise as our business scales.
- 3    Industry Background  We believe certain digital marketing technology industry trends are creating the opportunity for retailers, brands, venue-operators, enterprises, non-profits and other organizations to create innovative shopping, marketing, and informational experiences for their customers and other stakeholders in various venues worldwide.
- These trends include: (i) the expectations of technology-savvy consumers; (ii) addressing on-line competitors by improving physical experiences; (iii) a decline in the cost  of hardware configurations (primarily flat panel displays) and software media players; (iv) the continued evolution of mobile, social, software and hardware technologies, applications and tools; (v) increasing sophistication of social networking platforms; (vi) increasingly complex customer requirements related to their specific digital marketing technology and solution objectives; and (vii) customer expectations of satisfactory consumer experiences with reduced installation and operating costs.
- As a result, a growing number of retailers, brands, venue-operators, and other organizations have identified the need and opportunity to implement increasingly agile, automated, targeted and cost-effective and “sales-lifting” digital marketing, and interactive experiences to market to their customers.
- We believe our customers consider capitalizing on these industry trends to be increasingly critical to any successful “store of the future” retail and brand sales environment, especially where sales staff turnover is high, training outcomes are inconsistent and product knowledge is low.
- Companies are implementing various digital marketing technology solutions, which: are implemented in multiple forms and types of configurations and locations; attempt to achieve any of a broad range of individual or combination of objectives; contain various levels of targeting; have the ability to instantly manage single or multiple locations remotely from a customer’s desktop or other connected device at each location; and are built to deliver or contain a standard or customized customer  experience unique to and within the customer’s environment.

_Source: latest 10-K Item 1 (Business), summarized locally._

## Qualitative analysis (local LLM)

### Item 1 — Business (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, regulation, competition, guidance, revenue, margin, customer, segment, product, service, market, operations, network, subsidiary

- (“Creative Realities”, the “Company”, “we”, “us” or “our”) provides innovative digital signage and media solutions in North America to enhance communications in a wide-ranging variety of out-of-home environments, key market segments and use cases, including:    Retail                                                     Entertainment and Sports Venues                            Restaurants, including quick-serve restaurants (“QSR”)     Convenience Stores                                         Financial Services                                         Automotive                                                 Lottery                                                    Mixed Use Developments                                     Digital out of Home (“DOOH”) Advertising Networks         We serve market-leading companies, so there is a good chance that if you leave your home today to shop, work, eat or play, you will encounter one or more of our digital signage experiences.
- Our solutions are increasingly viable because we help our enterprise customers achieve a wide range of business objectives including:    Increased brand awareness/engagement               ───────────────────────────────────────────────────   Improved customer support                           Enhanced employee productivity and satisfaction     Increased revenue and profitability                 Improved guest experience                           Increased customer/guest engagement                 Traffic content and advertising                    Through a combination of organically grown platforms and a series of strategic acquisitions, the Company assists customers to design, deploy, manage, and monetize their digital signage and in-store retail media networks.
- The Company sources leads and opportunities for its solutions through its digital and content marketing initiatives, close relationships with key industry partners, equipment manufacturers, and the direct efforts of its in-house industry sales experts.
- Customer engagements focus on consultative conversations that ensure the Company’s solutions are positioned to help customers achieve their business objectives in the most cost-effective manner possible.
- When comparing Creative Realities to other digital signage competitors, our customers value the following competitive advantages:    Breadth of solutions – Creative Realities offers true solutions to our customers.
- 1      Managed labor pool – Unlike most companies in our industry, we have a curated labor pool of qualified and vetted field technicians available to service customers quickly nationwide.
- In-house creative resources – We assist customers in creating new content or repurposing existing content for digital signage experiences, an activity for which the Company has won several desi...
- Network scalability and reliability – Our software as a service (“SaaS”) content management platforms power some of the largest and most complex digital signage networks in North America, evide...
- Market sector expertise – Creative Realities has in-house experts in key market segments such as retail, quick-serve restaurants (“QSR”), convenience stores, and Digital Out of Home (“DOOH”) ad...
- Technical support – Digital signage networks present unique challenges for corporate IT departments.
- We simplify and improve end user support by leveraging our own Network Operations Center (“N...
- Retail Media Network – The Company owns and operates the largest mall shopping network in Canada.
- The three primary sources of revenue for the Company are:    Hardware sales from reselling digital signage hardware from original equipment manufacturers such as Samsung and BrightSign.
- Services revenue from helping customers design, deploy and manage their digital signage and in-store retail media networks, including:      Hardware system design/engineering     Hardware installation                  Content development                   2      Content scheduling                                                                       Post-deployment network and field support                                                AdTech to traffic advertising and content directly and through programmatic channels      Recurring subscription licensing and support revenue from our digital signage software platforms, which are generally sold via a SaaS model.
- Our platforms include:      ReflectView, the Company’s core digital signage platform for most applications, scalable and cost effective from 10 to 100,000+ devices;                                                                 Reflect Xperience, a web-based interface that allows customers to give content scheduling access to local users via the web or mobile devices, while still maintaining centralized programming co...
- AdLogic, the Company’s AdTech management platform for digital signage networks, which presently delivers approximately 50 million ads daily;                                                             CPM+, the Company’s demand side and supply side platform with campaign management and extensive capabilities for programmatic advertising;                                                               Clarity, the Company’s digital signage platform for menu board solutions, which has become a market leader for a range of restaurant, including QSR and convenience store applications; and              iShowroomProX, an omni-channel digital sales support platform targeted at original equipment manufacturers in the transportation sector, which integrates with dozens of key data services includ...
- While hardware sales and support services revenues can fluctuate more significantly year over year based on new, large-scale network deployments, the Company is focusing on maintaining and increasing recurring SaaS revenue as digital signage adoption/utilization expands across the vertical markets we serve.
- Flat panel displays, along with LED technology and digital media players typically constitute a large portion of the expenditure customers make relative to the entire cost of implementing a digital  marketing system implementation and can be a barrier to customer deployment.
- As a result, we believe that the broader adoption of digital marketing technology solutions is likely to increase, although we cannot predict the rate at which such adoption will occur.
- We believe the proliferation of in-store retail media networks will be an industrial catalyst for infrastructure and AdTech sales for which the Company is well situated from product set and technology stack standpoints.
- We believe that the selective acquisition and successful integration of certain companies will: accelerate our growth in targeted vertical and operating markets; enable us to cost-effectively aggregate multiple customer bases onto a single business and technology platform; provide us with greater operating scale on a consolidated basis; enable us to leverage a common set of processes and tools, and cost efficiencies company-wide; and ultimately result in higher operating profitability and cash flow from operations.
- Business Strategy  We believe that our existing business model is highly scalable and can be expanded successfully as we continue to grow organically, seek to acquire and integrate other companies in our target markets, strengthen our operational practices and procedures, further streamline our administrative office functions, and continue to capitalize on various marketing programs and activities.
- With a focus on SaaS revenues, we believe that our gross margins will rise as our business scales.
- 3    Industry Background  We believe certain digital marketing technology industry trends are creating the opportunity for retailers, brands, venue-operators, enterprises, non-profits and other organizations to create innovative shopping, marketing, and informational experiences for their customers and other stakeholders in various venues worldwide.
- These trends include: (i) the expectations of technology-savvy consumers; (ii) addressing on-line competitors by improving physical experiences; (iii) a decline in the cost  of hardware configurations (primarily flat panel displays) and software media players; (iv) the continued evolution of mobile, social, software and hardware technologies, applications and tools; (v) increasing sophistication of social networking platforms; (vi) increasingly complex customer requirements related to their specific digital marketing technology and solution objectives; and (vii) customer expectations of satisfactory consumer experiences with reduced installation and operating costs.
- As a result, a growing number of retailers, brands, venue-operators, and other organizations have identified the need and opportunity to implement increasingly agile, automated, targeted and cost-effective and “sales-lifting” digital marketing, and interactive experiences to market to their customers.
- We believe our customers consider capitalizing on these industry trends to be increasingly critical to any successful “store of the future” retail and brand sales environment, especially where sales staff turnover is high, training outcomes are inconsistent and product knowledge is low.
- Companies are implementing various digital marketing technology solutions, which: are implemented in multiple forms and types of configurations and locations; attempt to achieve any of a broad range of individual or combination of objectives; contain various levels of targeting; have the ability to instantly manage single or multiple locations remotely from a customer’s desktop or other connected device at each location; and are built to deliver or contain a standard or customized customer  experience unique to and within the customer’s environment.


### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin, supply chain, cyber, interest rate, customer, product, service, market, operations, network, subsidiary

- Our business involves a high degree of risk.
- In evaluating our business, you should carefully consider the specific risks described below, and any risks described in our other filings with the Securities and Exchange Commission (the“SEC”), pursuant to Sections 13(a), 13(c), 14, or 15(d) of the Exchange Act.
- Any of the risks we describe below or in our other filings with the SEC could cause our business, financial condition, results of operations or future prospects to be materially adversely  affected.
- In addition, some of these risks contain forward-looking statements.
- RISKS RELATED TO OUR BUSINESS AND OUR INDUSTRY  We have generally incurred losses, and may never become or remain profitable.
- We have incurred historical net losses, and we have had negative cash flows from operations.
- We have formulated our business plans and strategies based on certain assumptions regarding the acceptance of our business model and the marketing of our products and services.
- Nevertheless, our assessments regarding market size, market share, market acceptance of our products and services and a variety of other factors may prove incorrect.


### Item 7 — MD&A (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, uncertainty, regulation, revenue, margin, customer, segment, product, service, market, operations, network, subsidiary

- ’ S DISCUSSION AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERATIONS  (All currency is rounded to the nearest thousands, except share and per share amounts.)  The following discussion should be read in conjunction with the financial statements and related notes for the years ended December 31, 2025 and 2024, which are included elsewhere in this Report.
- This Management’s Discussion and Analysis of Financial Condition and Results of Operations contains statements that are forward-looking.
- These statements are based on current expectations and assumptions that are subject to risk, uncertainties and other factors.
- You should review the “Cautionary Note Regarding Forward-Looking Statements; Risk Factor Summary”, and “Risk Factors” sections of this Report for a discussion of important factors that could cause actual results to differ materially from the results described in or implied by the forward-looking statements described in the following discussion and analysis.
- Overview  The Company transforms environments through digital solutions by providing innovative digital signage solutions for key market segments and use cases, including:    Retail                              Entertainment and Sports Venues     Restaurants, including QSRs         Convenience Stores                  Financial Services                  Automotive                          Lottery                             Mixed Use Developments              DOOH Advertising Networks          We serve market-leading companies, so there is a good chance that if you leave your home today to shop, work, eat or play, you will encounter one or more of our digital signage experiences.
- Our solutions are increasingly visible because we help our enterprise customers achieve a range of business objectives including:    Increased brand awareness;    ──────────────────────────────  20      Improved customer support;                           Enhanced employee productivity and satisfaction;     Increased revenue and profitability;                 Improved guest experience; and                       Increased customer/guest engagement.
- Traffic content and advertising                     Through a combination of organically grown platforms and a series of strategic acquisitions, the Company assists customers to design, deploy, manage, and monetize their digital signage and in-store retail media networks.
- The Company sources leads and opportunities for its solutions through its digital and content marketing initiatives, close relationships with key industry partners, specifically equipment manufacturers, and the direct efforts of its in-house industry sales experts.


## Research loop (think → act)

1. _heuristic_ — Coverage looks adequate for this pass; stopping iterative loop.

## Sources

- **[S1]** CREX fundamentals (yfinance)
  - Creative Realities, Inc.: price=3.11, rev=57232000.0, fcf=-10244000.0, shares=13097892.0, rev_cagr=0.09702520767150968, ROIC=-0.04009801544695737, FCF yield=-0.2514825045850632
- **[S2]** CREX DCF valuation (dcf)
  - Base share price=-2.351755156061878, bull=6.783857023575285, bear=-4.565007007607608
- **[S3]** CREX EV/EBITDA valuation (multiples)
  - Base implied price=0.6179620354176076, multiple=40.0
- **[S4]** Creative Realities (CREX) Stock Forecast, Price Targets ... - TipRanks (web) — https://www.tipranks.com/stocks/crex/forecast
  - Based on 2 Wall Street analysts offering 12 month price targets for Creative Realities in the last 3 months. The average price target is $9.00 with a high ...
- **[S5]** CREX Stock Forecast & Price Target | Creative Realities Inc (CREX) (web) — https://valueinvesting.io/CREX/estimates
  - The average stock forecast for Creative Realities Inc (CREX) is 8.80 USD. This price target corresponds to an upside of 174.92%. The range of stock ...
- **[S6]** Creative Realities (CREX) Stock Forecast and Price Target 2026 (web) — https://www.marketbeat.com/stocks/NASDAQ/CREX/forecast/
  - CREX's current price target is $0.00. Learn why top analysts are making this stock forecast for Creative Realities at MarketBeat.
- **[S7]** CREX Forecast — Price Target — Prediction for 2027 - TradingView (web) — https://www.tradingview.com/symbols/NASDAQ-CREX/forecast-price-target/
  - The current price of CREX is 3.16 USD — it has decreased by −4.76% in the past 24 hours. Watch Creative Realities, Inc. stock price performance more closely on ...
- **[S8]** Why The Narrative Around Creative Realities (CREX) Is Evolving With Its New... (web) — https://finance.yahoo.com/news/why-narrative-around-creative-realities-120741632.html
  - What the New Price Target Means for Creative Realities Analysts have moved from having no published...
- **[S9]** How The Creative Realities (CREX) Story Is Shifting With New Targets And Theater... (web) — https://finance.yahoo.com/markets/stocks/articles/creative-realities-crex-story-shifting-080315391.html
  - Creative Realities is back in focus after analysts revised their fair value price target from...
- **[S10]** How Recent Developments Are Reframing The Creative Realities (CREX) Investment... (web) — https://finance.yahoo.com/news/recent-developments-reframing-creative-realities-101051024.html
  - Why the Price Target Moved While Fair Value Stayed Put The headline change for Creative Realities is...
- **[S11]** Analysts Offer Insights on Technology Companies: Creative Realities (CREX) and Applied Digital Corporation (APLD) (web) — https://www.theglobeandmail.com/investing/markets/stocks/CREX/pressreleases/3376489/analysts-offer-insights-on-technology-companies-creative-realities-crex-and-applied-digital-corporation-apld/
  - Detailed price information for Creative Realities Inc (CREX-Q) from The Globe and Mail including charting and trades.
- **[S12]** Creative Realities (CREX) Stock Forecast and Price Target 2026 (web_page) — https://www.marketbeat.com/stocks/NASDAQ/CREX/forecast/
  - Creative Realities (CREX) Stock Forecast and Price Target 2026 Skip to main content → My top 3 AI picks for the next decade (From The Oxford Club) (Ad) Free CREX Stock Alerts Cr…
- **[S13]** CREX DCF Valuation - Creative Realities Inc - Alpha Spread (web) — https://www.alphaspread.com/security/nasdaq/crex/dcf-valuation
  - Estimated DCF Value of one CREX stock is 7.36 USD. Compared to the current market price of 3.57 USD, the stock is Undervalued by 52%.Base Case Scenario. The present value of cas…
- **[S14]** Creative Realities (CREX) Earnings Date and Reports 2026 (web) — https://www.marketbeat.com/stocks/NASDAQ/CREX/earnings/
  - CREX Upcoming Earnings. Creative Realities' next earnings date is estimated for Wednesday, August 12, 2026, based on past reporting schedules.
- **[S15]** CREX | Creative Realities Inc. Analyst Estimates | MarketWatch (web) — https://www.marketwatch.com/investing/stock/crex/analystestimates
  - CREX Analyst Estimates. Snapshot. Average Recommendation.Current Year's Estimate. -0.64. Median PE on CY Estimate.
- **[S16]** Creative Realities Inc. (CREX) Live Share Price, Invest From India (web) — https://www.indmoney.com/us-stocks/creative-realities-inc-share-price-crex
  - Creative Realities Inc. share touched a 52 week high of $4.42 on April 21, 2026 and a 52 week low of $2.19 on August 20, 2025 .
- **[S17]** Creative Realities (CREX) News Today - MarketBeat (web) — https://www.marketbeat.com/stocks/NASDAQ/CREX/news/
  - What's going on at Creative Realities (NASDAQ:CREX)? Read today's CREX news from trusted media outlets at MarketBeat.
- **[S18]** Creative Realities (CREX) Stock Forecast and Price Target 2026 (web) — https://www.marketbeat.com/stocks/NASDAQ/CREX/forecast/
  - Based on 3 Wall Street analysts who have issued ratings for Creative Realities in the last 12 months, the stock has a consensus rating of "Hold.
- **[S19]** Demand - Wikipedia (web) — https://en.wikipedia.org/wiki/Demand
  - The demand curve facing a particular firm is called the residual demand curve. The residual demand curve is the market demand that is not met by other firms in the industry at a…
- **[S20]** 3.1 Demand, Supply, and Equilibrium in Markets for Goods and ... (web) — https://openstax.org/books/principles-economics-3e/pages/3-1-demand-supply-and-equilibrium-in-markets-for-goods-and-services
  - We can show an example from the market for gasoline in a table or a graph. Economists call a table that shows the quantity demanded at each price, such as Table 3.1, a demand sc…
- **[S21]** Creative Realities (CREX) Earnings Date and Reports 2026 (web_page) — https://www.marketbeat.com/stocks/NASDAQ/CREX/earnings/
  - Creative Realities (CREX) Earnings Date and Reports 2026 Skip to main content → Here’s the stock symbol I’ve promised (From Stansberry Research) (Ad) Free CREX Stock Alerts Crea…
- **[S22]** CREX 10-K (sec)
  - Item 1 chars=24018, Item 1A chars=50000, Item 7 chars=43243, ok=True, source=cache
- **[S23]** Item 1 Business summary (nlp)
  - ### Item 1 — Business (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, regulation, competition, guidance, revenue, margin, customer, segment, product, service,…
- **[S24]** Item 1A summary (nlp)
  - ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin, supply chain, cy…
- **[S25]** Item 7 summary (nlp)
  - ### Item 7 — MD&A (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, regulation, revenue, margin, customer, segment, product, service, market, opera…
- **[S26]** CREX scenario price ranges (scenarios)
  - ok=True; base mid=1.0723863046053517; headwinds=7; tailwinds=5

## Self-critique

_Automated review (heuristic)._

### Strengths
- Combines local fundamentals, optional DCF scenarios, and cited sources where available.
- Keeps a non-advisory framing for local research drafts.

### Issues & gaps
- Base-case model equity value is negative - treat intrinsic-value output as stress/distress, not a buy signal.
- Base-case implies deep downside vs spot (<-70%); confirm whether near-term FCF normalization is appropriate for this business.

### Caution for readers
- Treat scenario prices as sensitivity output, not a forecast.
- Re-check primary filings and fresh market data before any decision.



---

# Template: Full diligence (`deep`)

# CREX — Planned Research Report

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
- Company: Creative Realities, Inc.
- Sector / industry: Technology / Software - Application
- Price: 3.1
- 52-week range: $2.19 – $4.42
- Market cap: $40.60M
- Enterprise value: $129.24M
- Shares outstanding: 13.10M
- Beta: 1.458
- Book equity: $49.19M
- Revenue (latest): $57.23M
- EBITDA (latest): $1.86M
- Free cash flow (latest): -$10.24M
- Operating income: -$3.15M
- Operating margin: -5.5%
- EV / EBITDA: 69.5x
- ROIC: -4.0%
- FCF yield: -25.2%
- Debt / Equity: 1.3797625340544057
- FCF / share: -$0.78
- Revenue / share: $4.37

### Capital structure
- Cash: $1.56M
- Short-term debt: $4.43M
- Long-term debt: $39.52M
- Total debt: $67.86M
- Net debt: $66.31M
- Net debt / EBITDA: 35.6x

### Growth
- Revenue CAGR: 9.7%
- FCF CAGR: —
- Latest revenue YoY: 12.5%
- Latest FCF YoY: -1866.2%

### Market expectations (yfinance, sparse)
- Mean target: $8.17
- Target range: $7.00 – $10.00
- Recommendation: strong_buy

_Consensus revenue/EBITDA forecasts are often unavailable via free feeds; treat targets as point-in-time only._

### Historical KPIs (multi-year)

| Year | Revenue | OCF | Capex | FCF | EBITDA | LT debt | Cash | Net debt | Net income |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2025 | $57.23M | -$7.75M | $2.49M | -$10.24M | $1.86M | $39.52M | $1.56M | $37.96M | -$8.28M |
| 2024 | $50.85M | $3.38M | $2.80M | $580.00K | $2.45M | $13.04M | $1.04M | $12.01M | -$3.51M |
| 2023 | $45.17M | $5.17M | $4.03M | $1.14M | $3.36M | $9.83M | $2.91M | $6.92M | -$2.94M |
| 2022 | $43.35M | -$708.00K | $4.29M | -$5.00M | $7.53M | $13.07M | $1.63M | $11.44M | $1.88M |

## Charts

### Revenue & FCF history
![Revenue & FCF history](/charts/CREX_deep_revenue_fcf.png)

### DCF scenario prices
![DCF scenario prices](/charts/CREX_deep_dcf_scenarios.png)

### Base-case FCF path
![Base-case FCF path](/charts/CREX_deep_base_fcf_path.png)

## DCF valuation (base / bull / bear) [S2]

> Simplified revenue->FCF DCF. Not investment advice; assumptions are editable heuristics.

- Spot price: $3.10
- Base revenue: $57.23M
- Shares: 13,097,892
- Net debt (Debt−Cash): $66.31M

| Scenario | Growth | FCF margin | WACC | Term. g | Equity value | Share price | Upside |
|----------|--------|------------|------|---------|--------------|-------------|--------|
| bear | 5.5% | 1.0% | 12.0% | 1.5% | -$59.79M | $-4.57 | -247.3% |
| base | 12.5% | 3.0% | 10.0% | 2.5% | -$30.80M | $-2.35 | -175.9% |
| bull | 19.5% | 8.0% | 9.0% | 3.0% | $88.85M | $6.78 | 118.8% |

### Assumption notes
- Base revenue growth seeded from historical rate (12.5%).
- Latest FCF margin was -17.9%; scenarios use normalized positive margins for a going-concern DCF.

- _base: model equity value is negative after net debt (-30,803,035); showing $-2.35/sh._
- _bear: model equity value is negative after net debt (-59,791,969); showing $-4.57/sh._

### Base-case projected FCF

- Year 1: revenue $64.41M, FCF $1.93M (PV $1.76M)
- Year 2: revenue $72.49M, FCF $2.17M (PV $1.80M)
- Year 3: revenue $81.58M, FCF $2.45M (PV $1.84M)
- Year 4: revenue $91.81M, FCF $2.75M (PV $1.88M)
- Year 5: revenue $103.33M, FCF $3.10M (PV $1.92M)
- Terminal value $42.36M (PV $26.30M)

## Web research — web_research

- Queries: Deep diligence: fundamentals, DCF, web, 10-K risks & MD&A
- Unique hits: 2
- Pages fetched: 2/2

### Web synthesis — web_research
Here are the summaries:

**Analyst views / price targets / ratings**
* No analyst views or price targets mentioned in the provided material.

**Recent company news and catalysts**
* No recent company news or catalysts mentioned in the provided material. The SAFER Web - Company Snapshot page appears to be a database of company information, but does not provide any specific news or events.

**Sector or commodity drivers mentioned (e.g. uranium, rare earths, pricing)**
* None mentioned in the provided material. The DCF Case Studies & Projects page is focused on discounted cash flow modeling and does not mention any specific sectors or commodities.

### Sources found
- [DCF Case Studies & Projects | Real Work Examples](https://noraveli.pro/projects/)
  - DCF Mastery. We're here to help junior analysts in Ottawa build real discounted cash flow models. Clear spreadsheet walkthroughs, practical examples, and the…
- [SAFER Web - Company Snapshot](https://safer.fmcsa.dot.gov/CompanySnapshot.aspx)
  - SAFER Home | Feedback | Privacy Policy | USA.gov | Freedom of Information Act (FOIA) | Accessibility | OIG Hotline | Web Policies and Important Links | Plug-…

### Search warnings
- news:Deep diligence: fundamentals, DCF, web, 10-K risks & MD&A: No results found.

## Put opportunities (heuristic) [S3]
- Expiration: None (DTE None)
- Candidates: 0
- ATM IV (est.): —
- IV rank: — (0 local samples)
- HV rank (20d realized): —


**Options error:** unexpected character: line 1 column 1 (char 0)

## SEC filing [S8]
- Extraction OK: True
- Item 1 chars: 24018
- Item 1A chars: 50000
- Item 7 chars: 43243
- Meta: {'source': 'cache', 'path': 'C:\\DevWork\\equity_research_agent\\data\\filings\\CREX_10k.txt'}

## Company setup & business model

**Keyword hits:** risk, regulation, competition, guidance, revenue, margin, customer, segment, product, service, market, operations, network, subsidiary

- (“Creative Realities”, the “Company”, “we”, “us” or “our”) provides innovative digital signage and media solutions in North America to enhance communications in a wide-ranging variety of out-of-home environments, key market segments and use cases, including:    Retail                                                     Entertainment and Sports Venues                            Restaurants, including quick-serve restaurants (“QSR”)     Convenience Stores                                         Financial Services                                         Automotive                                                 Lottery                                                    Mixed Use Developments                                     Digital out of Home (“DOOH”) Advertising Networks         We serve market-leading companies, so there is a good chance that if you leave your home today to shop, work, eat or play, you will encounter one or more of our digital signage experiences.
- Our solutions are increasingly viable because we help our enterprise customers achieve a wide range of business objectives including:    Increased brand awareness/engagement               ───────────────────────────────────────────────────   Improved customer support                           Enhanced employee productivity and satisfaction     Increased revenue and profitability                 Improved guest experience                           Increased customer/guest engagement                 Traffic content and advertising                    Through a combination of organically grown platforms and a series of strategic acquisitions, the Company assists customers to design, deploy, manage, and monetize their digital signage and in-store retail media networks.
- The Company sources leads and opportunities for its solutions through its digital and content marketing initiatives, close relationships with key industry partners, equipment manufacturers, and the direct efforts of its in-house industry sales experts.
- Customer engagements focus on consultative conversations that ensure the Company’s solutions are positioned to help customers achieve their business objectives in the most cost-effective manner possible.
- When comparing Creative Realities to other digital signage competitors, our customers value the following competitive advantages:    Breadth of solutions – Creative Realities offers true solutions to our customers.
- 1      Managed labor pool – Unlike most companies in our industry, we have a curated labor pool of qualified and vetted field technicians available to service customers quickly nationwide.
- In-house creative resources – We assist customers in creating new content or repurposing existing content for digital signage experiences, an activity for which the Company has won several desi...
- Network scalability and reliability – Our software as a service (“SaaS”) content management platforms power some of the largest and most complex digital signage networks in North America, evide...
- Market sector expertise – Creative Realities has in-house experts in key market segments such as retail, quick-serve restaurants (“QSR”), convenience stores, and Digital Out of Home (“DOOH”) ad...
- Technical support – Digital signage networks present unique challenges for corporate IT departments.
- We simplify and improve end user support by leveraging our own Network Operations Center (“N...
- Retail Media Network – The Company owns and operates the largest mall shopping network in Canada.
- The three primary sources of revenue for the Company are:    Hardware sales from reselling digital signage hardware from original equipment manufacturers such as Samsung and BrightSign.
- Services revenue from helping customers design, deploy and manage their digital signage and in-store retail media networks, including:      Hardware system design/engineering     Hardware installation                  Content development                   2      Content scheduling                                                                       Post-deployment network and field support                                                AdTech to traffic advertising and content directly and through programmatic channels      Recurring subscription licensing and support revenue from our digital signage software platforms, which are generally sold via a SaaS model.
- Our platforms include:      ReflectView, the Company’s core digital signage platform for most applications, scalable and cost effective from 10 to 100,000+ devices;                                                                 Reflect Xperience, a web-based interface that allows customers to give content scheduling access to local users via the web or mobile devices, while still maintaining centralized programming co...
- AdLogic, the Company’s AdTech management platform for digital signage networks, which presently delivers approximately 50 million ads daily;                                                             CPM+, the Company’s demand side and supply side platform with campaign management and extensive capabilities for programmatic advertising;                                                               Clarity, the Company’s digital signage platform for menu board solutions, which has become a market leader for a range of restaurant, including QSR and convenience store applications; and              iShowroomProX, an omni-channel digital sales support platform targeted at original equipment manufacturers in the transportation sector, which integrates with dozens of key data services includ...
- While hardware sales and support services revenues can fluctuate more significantly year over year based on new, large-scale network deployments, the Company is focusing on maintaining and increasing recurring SaaS revenue as digital signage adoption/utilization expands across the vertical markets we serve.
- Flat panel displays, along with LED technology and digital media players typically constitute a large portion of the expenditure customers make relative to the entire cost of implementing a digital  marketing system implementation and can be a barrier to customer deployment.
- As a result, we believe that the broader adoption of digital marketing technology solutions is likely to increase, although we cannot predict the rate at which such adoption will occur.
- We believe the proliferation of in-store retail media networks will be an industrial catalyst for infrastructure and AdTech sales for which the Company is well situated from product set and technology stack standpoints.
- We believe that the selective acquisition and successful integration of certain companies will: accelerate our growth in targeted vertical and operating markets; enable us to cost-effectively aggregate multiple customer bases onto a single business and technology platform; provide us with greater operating scale on a consolidated basis; enable us to leverage a common set of processes and tools, and cost efficiencies company-wide; and ultimately result in higher operating profitability and cash flow from operations.
- Business Strategy  We believe that our existing business model is highly scalable and can be expanded successfully as we continue to grow organically, seek to acquire and integrate other companies in our target markets, strengthen our operational practices and procedures, further streamline our administrative office functions, and continue to capitalize on various marketing programs and activities.
- With a focus on SaaS revenues, we believe that our gross margins will rise as our business scales.
- 3    Industry Background  We believe certain digital marketing technology industry trends are creating the opportunity for retailers, brands, venue-operators, enterprises, non-profits and other organizations to create innovative shopping, marketing, and informational experiences for their customers and other stakeholders in various venues worldwide.
- These trends include: (i) the expectations of technology-savvy consumers; (ii) addressing on-line competitors by improving physical experiences; (iii) a decline in the cost  of hardware configurations (primarily flat panel displays) and software media players; (iv) the continued evolution of mobile, social, software and hardware technologies, applications and tools; (v) increasing sophistication of social networking platforms; (vi) increasingly complex customer requirements related to their specific digital marketing technology and solution objectives; and (vii) customer expectations of satisfactory consumer experiences with reduced installation and operating costs.
- As a result, a growing number of retailers, brands, venue-operators, and other organizations have identified the need and opportunity to implement increasingly agile, automated, targeted and cost-effective and “sales-lifting” digital marketing, and interactive experiences to market to their customers.
- We believe our customers consider capitalizing on these industry trends to be increasingly critical to any successful “store of the future” retail and brand sales environment, especially where sales staff turnover is high, training outcomes are inconsistent and product knowledge is low.
- Companies are implementing various digital marketing technology solutions, which: are implemented in multiple forms and types of configurations and locations; attempt to achieve any of a broad range of individual or combination of objectives; contain various levels of targeting; have the ability to instantly manage single or multiple locations remotely from a customer’s desktop or other connected device at each location; and are built to deliver or contain a standard or customized customer  experience unique to and within the customer’s environment.

_Source: latest 10-K Item 1 (Business), summarized locally._

## Qualitative analysis (local LLM)

### Item 1 — Business (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, regulation, competition, guidance, revenue, margin, customer, segment, product, service, market, operations, network, subsidiary

- (“Creative Realities”, the “Company”, “we”, “us” or “our”) provides innovative digital signage and media solutions in North America to enhance communications in a wide-ranging variety of out-of-home environments, key market segments and use cases, including:    Retail                                                     Entertainment and Sports Venues                            Restaurants, including quick-serve restaurants (“QSR”)     Convenience Stores                                         Financial Services                                         Automotive                                                 Lottery                                                    Mixed Use Developments                                     Digital out of Home (“DOOH”) Advertising Networks         We serve market-leading companies, so there is a good chance that if you leave your home today to shop, work, eat or play, you will encounter one or more of our digital signage experiences.
- Our solutions are increasingly viable because we help our enterprise customers achieve a wide range of business objectives including:    Increased brand awareness/engagement               ───────────────────────────────────────────────────   Improved customer support                           Enhanced employee productivity and satisfaction     Increased revenue and profitability                 Improved guest experience                           Increased customer/guest engagement                 Traffic content and advertising                    Through a combination of organically grown platforms and a series of strategic acquisitions, the Company assists customers to design, deploy, manage, and monetize their digital signage and in-store retail media networks.
- The Company sources leads and opportunities for its solutions through its digital and content marketing initiatives, close relationships with key industry partners, equipment manufacturers, and the direct efforts of its in-house industry sales experts.
- Customer engagements focus on consultative conversations that ensure the Company’s solutions are positioned to help customers achieve their business objectives in the most cost-effective manner possible.
- When comparing Creative Realities to other digital signage competitors, our customers value the following competitive advantages:    Breadth of solutions – Creative Realities offers true solutions to our customers.
- 1      Managed labor pool – Unlike most companies in our industry, we have a curated labor pool of qualified and vetted field technicians available to service customers quickly nationwide.
- In-house creative resources – We assist customers in creating new content or repurposing existing content for digital signage experiences, an activity for which the Company has won several desi...
- Network scalability and reliability – Our software as a service (“SaaS”) content management platforms power some of the largest and most complex digital signage networks in North America, evide...
- Market sector expertise – Creative Realities has in-house experts in key market segments such as retail, quick-serve restaurants (“QSR”), convenience stores, and Digital Out of Home (“DOOH”) ad...
- Technical support – Digital signage networks present unique challenges for corporate IT departments.
- We simplify and improve end user support by leveraging our own Network Operations Center (“N...
- Retail Media Network – The Company owns and operates the largest mall shopping network in Canada.
- The three primary sources of revenue for the Company are:    Hardware sales from reselling digital signage hardware from original equipment manufacturers such as Samsung and BrightSign.
- Services revenue from helping customers design, deploy and manage their digital signage and in-store retail media networks, including:      Hardware system design/engineering     Hardware installation                  Content development                   2      Content scheduling                                                                       Post-deployment network and field support                                                AdTech to traffic advertising and content directly and through programmatic channels      Recurring subscription licensing and support revenue from our digital signage software platforms, which are generally sold via a SaaS model.
- Our platforms include:      ReflectView, the Company’s core digital signage platform for most applications, scalable and cost effective from 10 to 100,000+ devices;                                                                 Reflect Xperience, a web-based interface that allows customers to give content scheduling access to local users via the web or mobile devices, while still maintaining centralized programming co...
- AdLogic, the Company’s AdTech management platform for digital signage networks, which presently delivers approximately 50 million ads daily;                                                             CPM+, the Company’s demand side and supply side platform with campaign management and extensive capabilities for programmatic advertising;                                                               Clarity, the Company’s digital signage platform for menu board solutions, which has become a market leader for a range of restaurant, including QSR and convenience store applications; and              iShowroomProX, an omni-channel digital sales support platform targeted at original equipment manufacturers in the transportation sector, which integrates with dozens of key data services includ...
- While hardware sales and support services revenues can fluctuate more significantly year over year based on new, large-scale network deployments, the Company is focusing on maintaining and increasing recurring SaaS revenue as digital signage adoption/utilization expands across the vertical markets we serve.
- Flat panel displays, along with LED technology and digital media players typically constitute a large portion of the expenditure customers make relative to the entire cost of implementing a digital  marketing system implementation and can be a barrier to customer deployment.
- As a result, we believe that the broader adoption of digital marketing technology solutions is likely to increase, although we cannot predict the rate at which such adoption will occur.
- We believe the proliferation of in-store retail media networks will be an industrial catalyst for infrastructure and AdTech sales for which the Company is well situated from product set and technology stack standpoints.
- We believe that the selective acquisition and successful integration of certain companies will: accelerate our growth in targeted vertical and operating markets; enable us to cost-effectively aggregate multiple customer bases onto a single business and technology platform; provide us with greater operating scale on a consolidated basis; enable us to leverage a common set of processes and tools, and cost efficiencies company-wide; and ultimately result in higher operating profitability and cash flow from operations.
- Business Strategy  We believe that our existing business model is highly scalable and can be expanded successfully as we continue to grow organically, seek to acquire and integrate other companies in our target markets, strengthen our operational practices and procedures, further streamline our administrative office functions, and continue to capitalize on various marketing programs and activities.
- With a focus on SaaS revenues, we believe that our gross margins will rise as our business scales.
- 3    Industry Background  We believe certain digital marketing technology industry trends are creating the opportunity for retailers, brands, venue-operators, enterprises, non-profits and other organizations to create innovative shopping, marketing, and informational experiences for their customers and other stakeholders in various venues worldwide.
- These trends include: (i) the expectations of technology-savvy consumers; (ii) addressing on-line competitors by improving physical experiences; (iii) a decline in the cost  of hardware configurations (primarily flat panel displays) and software media players; (iv) the continued evolution of mobile, social, software and hardware technologies, applications and tools; (v) increasing sophistication of social networking platforms; (vi) increasingly complex customer requirements related to their specific digital marketing technology and solution objectives; and (vii) customer expectations of satisfactory consumer experiences with reduced installation and operating costs.
- As a result, a growing number of retailers, brands, venue-operators, and other organizations have identified the need and opportunity to implement increasingly agile, automated, targeted and cost-effective and “sales-lifting” digital marketing, and interactive experiences to market to their customers.
- We believe our customers consider capitalizing on these industry trends to be increasingly critical to any successful “store of the future” retail and brand sales environment, especially where sales staff turnover is high, training outcomes are inconsistent and product knowledge is low.
- Companies are implementing various digital marketing technology solutions, which: are implemented in multiple forms and types of configurations and locations; attempt to achieve any of a broad range of individual or combination of objectives; contain various levels of targeting; have the ability to instantly manage single or multiple locations remotely from a customer’s desktop or other connected device at each location; and are built to deliver or contain a standard or customized customer  experience unique to and within the customer’s environment.


### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin, supply chain, cyber, interest rate, customer, product, service, market, operations, network, subsidiary

- Our business involves a high degree of risk.
- In evaluating our business, you should carefully consider the specific risks described below, and any risks described in our other filings with the Securities and Exchange Commission (the“SEC”), pursuant to Sections 13(a), 13(c), 14, or 15(d) of the Exchange Act.
- Any of the risks we describe below or in our other filings with the SEC could cause our business, financial condition, results of operations or future prospects to be materially adversely  affected.
- In addition, some of these risks contain forward-looking statements.
- RISKS RELATED TO OUR BUSINESS AND OUR INDUSTRY  We have generally incurred losses, and may never become or remain profitable.
- We have incurred historical net losses, and we have had negative cash flows from operations.
- We have formulated our business plans and strategies based on certain assumptions regarding the acceptance of our business model and the marketing of our products and services.
- Nevertheless, our assessments regarding market size, market share, market acceptance of our products and services and a variety of other factors may prove incorrect.


### Item 7 — MD&A (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, uncertainty, regulation, revenue, margin, customer, segment, product, service, market, operations, network, subsidiary

- ’ S DISCUSSION AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERATIONS  (All currency is rounded to the nearest thousands, except share and per share amounts.)  The following discussion should be read in conjunction with the financial statements and related notes for the years ended December 31, 2025 and 2024, which are included elsewhere in this Report.
- This Management’s Discussion and Analysis of Financial Condition and Results of Operations contains statements that are forward-looking.
- These statements are based on current expectations and assumptions that are subject to risk, uncertainties and other factors.
- You should review the “Cautionary Note Regarding Forward-Looking Statements; Risk Factor Summary”, and “Risk Factors” sections of this Report for a discussion of important factors that could cause actual results to differ materially from the results described in or implied by the forward-looking statements described in the following discussion and analysis.
- Overview  The Company transforms environments through digital solutions by providing innovative digital signage solutions for key market segments and use cases, including:    Retail                              Entertainment and Sports Venues     Restaurants, including QSRs         Convenience Stores                  Financial Services                  Automotive                          Lottery                             Mixed Use Developments              DOOH Advertising Networks          We serve market-leading companies, so there is a good chance that if you leave your home today to shop, work, eat or play, you will encounter one or more of our digital signage experiences.
- Our solutions are increasingly visible because we help our enterprise customers achieve a range of business objectives including:    Increased brand awareness;    ──────────────────────────────  20      Improved customer support;                           Enhanced employee productivity and satisfaction;     Increased revenue and profitability;                 Improved guest experience; and                       Increased customer/guest engagement.
- Traffic content and advertising                     Through a combination of organically grown platforms and a series of strategic acquisitions, the Company assists customers to design, deploy, manage, and monetize their digital signage and in-store retail media networks.
- The Company sources leads and opportunities for its solutions through its digital and content marketing initiatives, close relationships with key industry partners, specifically equipment manufacturers, and the direct efforts of its in-house industry sales experts.


## Run warnings

- options: unexpected character: line 1 column 1 (char 0)

## Research loop (think → act)

1. _heuristic_ — Coverage looks adequate for this pass; stopping iterative loop.

## Sources

- **[S1]** CREX fundamentals (yfinance)
  - Creative Realities, Inc.: price=3.1, rev=57232000.0, fcf=-10244000.0, shares=13097892.0, rev_cagr=0.09702520767150968, ROIC=-0.04009801544695737, FCF yield=-0.25229374518390846
- **[S2]** CREX DCF valuation (dcf)
  - Base share price=-2.351755156061878, bull=6.783857023575285, bear=-4.565007007607608
- **[S3]** CREX put screen (yfinance_options)
  - Error: unexpected character: line 1 column 1 (char 0)
- **[S4]** DCF Case Studies & Projects | Real Work Examples (web) — https://noraveli.pro/projects/
  - DCF Mastery. We're here to help junior analysts in Ottawa build real discounted cash flow models. Clear spreadsheet walkthroughs, practical examples, and the fundamentals you ac…
- **[S5]** SAFER Web - Company Snapshot (web) — https://safer.fmcsa.dot.gov/CompanySnapshot.aspx
  - SAFER Home | Feedback | Privacy Policy | USA.gov | Freedom of Information Act (FOIA) | Accessibility | OIG Hotline | Web Policies and Important Links | Plug-ins.
- **[S6]** DCF Case Studies & Projects | Real Work Examples (web_page) — https://noraveli.pro/projects/
  - DCF Case Studies & Projects | Real Work Examples Our Work Practical DCF training programmes designed for junior analysts in Ottawa and across Canada Bootcamp Programme DCF Funda…
- **[S7]** SAFER Web - Company Snapshot (web_page) — https://safer.fmcsa.dot.gov/CompanySnapshot.aspx
  - SAFER Web - Company Snapshot SAFER Table Layout SAFER Table Layout Company Snapshot The Company Snapshot is a concise electronic record of a companyï¿½s  	identification, size,…
- **[S8]** CREX 10-K (sec)
  - Item 1 chars=24018, Item 1A chars=50000, Item 7 chars=43243, ok=True, source=cache
- **[S9]** Item 1 Business summary (nlp)
  - ### Item 1 — Business (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, regulation, competition, guidance, revenue, margin, customer, segment, product, service,…
- **[S10]** Item 1A summary (nlp)
  - ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, revenue, margin, supply chain, cy…
- **[S11]** Item 7 summary (nlp)
  - ### Item 7 — MD&A (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, regulation, revenue, margin, customer, segment, product, service, market, opera…

## Self-critique

_Automated review (heuristic)._

### Strengths
- Combines local fundamentals, optional DCF scenarios, and cited sources where available.
- Keeps a non-advisory framing for local research drafts.

### Issues & gaps
- Base-case model equity value is negative - treat intrinsic-value output as stress/distress, not a buy signal.
- Base-case implies deep downside vs spot (<-70%); confirm whether near-term FCF normalization is appropriate for this business.
- Run recorded 1 tool warning(s); see Run warnings before relying on the draft.

### Caution for readers
- Treat scenario prices as sensitivity output, not a forecast.
- Re-check primary filings and fresh market data before any decision.



---

# Template: Options income (`income`)

# CREX — Planned Research Report

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
- Company: Creative Realities, Inc.
- Sector / industry: Technology / Software - Application
- Price: 3.0615
- 52-week range: $2.19 – $4.42
- Market cap: $40.10M
- Enterprise value: $129.24M
- Shares outstanding: 13.10M
- Beta: 1.458
- Book equity: $49.19M
- Revenue (latest): $57.23M
- EBITDA (latest): $1.86M
- Free cash flow (latest): -$10.24M
- Operating income: -$3.15M
- Operating margin: -5.5%
- EV / EBITDA: 69.5x
- ROIC: -4.0%
- FCF yield: -25.5%
- Debt / Equity: 1.3797625340544057
- FCF / share: -$0.78
- Revenue / share: $4.37

### Capital structure
- Cash: $1.56M
- Short-term debt: $4.43M
- Long-term debt: $39.52M
- Total debt: $67.86M
- Net debt: $66.31M
- Net debt / EBITDA: 35.6x

### Growth
- Revenue CAGR: 9.7%
- FCF CAGR: —
- Latest revenue YoY: 12.5%
- Latest FCF YoY: -1866.2%

### Market expectations (yfinance, sparse)
- Mean target: $8.17
- Target range: $7.00 – $10.00
- Recommendation: strong_buy

_Consensus revenue/EBITDA forecasts are often unavailable via free feeds; treat targets as point-in-time only._

### Historical KPIs (multi-year)

| Year | Revenue | OCF | Capex | FCF | EBITDA | LT debt | Cash | Net debt | Net income |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2025 | $57.23M | -$7.75M | $2.49M | -$10.24M | $1.86M | $39.52M | $1.56M | $37.96M | -$8.28M |
| 2024 | $50.85M | $3.38M | $2.80M | $580.00K | $2.45M | $13.04M | $1.04M | $12.01M | -$3.51M |
| 2023 | $45.17M | $5.17M | $4.03M | $1.14M | $3.36M | $9.83M | $2.91M | $6.92M | -$2.94M |
| 2022 | $43.35M | -$708.00K | $4.29M | -$5.00M | $7.53M | $13.07M | $1.63M | $11.44M | $1.88M |

## Charts

### Revenue & FCF history
![Revenue & FCF history](/charts/CREX_income_revenue_fcf.png)

## Web research — web_research

- Queries: CREX news, Creative Realities, Inc. earnings OR catalyst
- Unique hits: 14
- Pages fetched: 1/3

### Web synthesis — web_research (rule-based fallback — Ollama unavailable)
**Keyword hits:** revenue, customer, service, market

- - MarketBeat | www.marketbeat.com | https://www.marketbeat.com/stocks/NASDAQ/CREX/news/ What's going on at Creative Realities (NASDAQ:CREX)?
- Read today's CREX news from trusted media outlets at MarketBeat.
- [HIT] Should Weakness in Creative Realities, Inc.'s (NASDAQ:CREX) Stock Be Seen As A Sign That Market Will Correct The Share Price Given Decent Financials?
- [HIT] Creative Realities Inc (CREX) Q3 2024 Earnings Call Highlights: Record Revenue and Strategic ...
- | Yahoo Finance | https://finance.yahoo.com/news/creative-realities-inc-crex-q3-070917936.html Creative Realities Inc (NASDAQ:CREX) reported record third-quarter revenue of $14.4 million, a 25% increase from the previous year.
- | Yahoo Finance | https://finance.yahoo.com/news/creative-realities-inc-crex-q4-070109545.html Revenue: $11 million for Q4 2024, down from $14.5 million in Q4 2023.
- I just want to thank you and your team for doing such a great job in regards to customer service and communication.
- [HIT] 4 Internet Stocks Poised to Top Estimates This Earnings Season | Zacks · via Yahoo Finance | https://finance.yahoo.com/markets/stocks/articles/4-internet-stocks-poised-top-144300356.html First-quarter 2026 presented Internet stocks with a turbulent yet opportunity-rich landscape, as the...

### Sources found
- [Cregneash](https://en.wikipedia.org/wiki/Cregneash)
  - Cregneash or Cregneish (Manx: Creneash) is a small village and tourist destination in the extreme south-west of the Isle of Man, about 1 mi (2 km) from Port …
- [Creative Realities, Inc. (CREX) Latest Stock News & Headlines - Yahoo ...](https://finance.yahoo.com/quote/CREX/news/)
  - Get the latest Creative Realities, Inc. (CREX) stock news and headlines to help you in your trading and investing decisions.
- [CREX News Today | Why did Creative Realities stock go down ... - MarketBeat](https://www.marketbeat.com/stocks/NASDAQ/CREX/news/)
  - What's going on at Creative Realities (NASDAQ:CREX)? Read today's CREX news from trusted media outlets at MarketBeat.
- [Creative Realities, Inc. (CREX) Stock Price, News, Quote & History ...](https://finance.yahoo.com/quote/CREX/)
  - Find the latest Creative Realities, Inc. (CREX) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Creative Realities Inc (CREX) Q3 2025 Earnings Call Highlights: Strategic Acquisition and ...](https://finance.yahoo.com/news/creative-realities-inc-crex-q3-210410170.html)
  - Creative Realities Inc (NASDAQ:CREX) completed the acquisition of Cineplex Digital Media (CDM), which is expected to double the company's size and accelerate…
- [Should Weakness in Creative Realities, Inc.'s (NASDAQ:CREX) Stock Be Seen As A Sign That Market Will Correct The Share Price Given Decent Financials?](https://finance.yahoo.com/news/weakness-creative-realities-inc-nasdaq-105753641.html)
  - Creative Realities (NASDAQ:CREX) has had a rough three months with its share price down 42%. However, the company's fundamentals look pretty decent, and long…
- [Creative Realities Inc (CREX) Q3 2024 Earnings Call Highlights: Record Revenue and Strategic ...](https://finance.yahoo.com/news/creative-realities-inc-crex-q3-070917936.html)
  - Creative Realities Inc (NASDAQ:CREX) reported record third-quarter revenue of $14.4 million, a 25% increase from the previous year. The company achieved a gr…
- [Creative Realities Inc (CREX) Q4 2024 Earnings Call Highlights: Navigating Challenges and ...](https://finance.yahoo.com/news/creative-realities-inc-crex-q4-070109545.html)
  - Revenue: $11 million for Q4 2024, down from $14.5 million in Q4 2023. Gross Profit: $4.9 million for Q4 2024, compared to $7.5 million in Q4 2023. Adjusted E…
- [Digital Signage Solutions and Experiences | Creative Realities](https://cri.com/)
  - Jun 30, 2026 · Creative Realities is a leader in smart, end-to-end digital signage solutions and experiences that connect people and brands in the places the…
- [Custom Supplement Manufacturer | Catalyst Nutraceuticals](https://catalystnutra.com/)
  - At Catalyst Nutraceuticals, we’re your trusted nutraceutical and dietary supplement manufacturers in Georgia, providing custom formulations and packaging sol…
- [Catalyst Shop](https://catalystshop.com/)
  - Catalyst Shop "Excellent! I just want to thank you and your team for doing such a great job in regards to customer service and communication. I know how many…
- [Catalyst Brands](https://www.catalystbrands.com/index.html)
  - We are Catalyst Brands. We now bring together the rich heritage of five unique brands, with modern energy and a bold vision for success. Just as a catalyst i…

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

- **[S1]** CREX fundamentals (yfinance)
  - Creative Realities, Inc.: price=3.0615, rev=57232000.0, fcf=-10244000.0, shares=13097892.0, rev_cagr=0.09702520767150968, ROIC=-0.04009801544695737, FCF yield=-0.2554664687042603
- **[S2]** CREX put screen (yfinance_options)
  - Expiration None (DTE None): 0 candidates; IV=None, IV rank=None, HV rank=None. No options chain available
- **[S3]** Cregneash (web) — https://en.wikipedia.org/wiki/Cregneash
  - Cregneash or Cregneish (Manx: Creneash) is a small village and tourist destination in the extreme south-west of the Isle of Man, about 1 mi (2 km) from Port Erin. Most of the vi…
- **[S4]** Creative Realities, Inc. (CREX) Latest Stock News & Headlines - Yahoo ... (web) — https://finance.yahoo.com/quote/CREX/news/
  - Get the latest Creative Realities, Inc. (CREX) stock news and headlines to help you in your trading and investing decisions.
- **[S5]** CREX News Today | Why did Creative Realities stock go down ... - MarketBeat (web) — https://www.marketbeat.com/stocks/NASDAQ/CREX/news/
  - What's going on at Creative Realities (NASDAQ:CREX)? Read today's CREX news from trusted media outlets at MarketBeat.
- **[S6]** Creative Realities, Inc. (CREX) Stock Price, News, Quote & History ... (web) — https://finance.yahoo.com/quote/CREX/
  - Find the latest Creative Realities, Inc. (CREX) stock quote, history, news and other vital information to help you with your stock trading and investing.
- **[S7]** Creative Realities Inc (CREX) Q3 2025 Earnings Call Highlights: Strategic Acquisition and ... (web) — https://finance.yahoo.com/news/creative-realities-inc-crex-q3-210410170.html
  - Creative Realities Inc (NASDAQ:CREX) completed the acquisition of Cineplex Digital Media (CDM), which is expected to double the company's size and accelerate growth. The acquisi…
- **[S8]** Should Weakness in Creative Realities, Inc.'s (NASDAQ:CREX) Stock Be Seen As A Sign That Market Will Correct The Share Price Given Decent Financials? (web) — https://finance.yahoo.com/news/weakness-creative-realities-inc-nasdaq-105753641.html
  - Creative Realities (NASDAQ:CREX) has had a rough three months with its share price down 42%. However, the company's fundamentals look pretty decent, and long-term financials are…
- **[S9]** Creative Realities Inc (CREX) Q3 2024 Earnings Call Highlights: Record Revenue and Strategic ... (web) — https://finance.yahoo.com/news/creative-realities-inc-crex-q3-070917936.html
  - Creative Realities Inc (NASDAQ:CREX) reported record third-quarter revenue of $14.4 million, a 25% increase from the previous year. The company achieved a gross profit of $6.6 m…
- **[S10]** Creative Realities Inc (CREX) Q4 2024 Earnings Call Highlights: Navigating Challenges and ... (web) — https://finance.yahoo.com/news/creative-realities-inc-crex-q4-070109545.html
  - Revenue: $11 million for Q4 2024, down from $14.5 million in Q4 2023. Gross Profit: $4.9 million for Q4 2024, compared to $7.5 million in Q4 2023. Adjusted EBITDA: Approximately…
- **[S11]** CREX News Today | Why did Creative Realities stock go down today? (web_page) — https://www.marketbeat.com/stocks/NASDAQ/CREX/news/
  - CREX News Today | Why did Creative Realities stock go down today? Skip to main content → Your book attached (From Profits Run) (Ad) Free CREX Stock Alerts Creative Realities (CR…

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

# CREX — Planned Research Report

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
- Company: Creative Realities, Inc.
- Sector / industry: Technology / Software - Application
- Price: 3.08
- 52-week range: $2.19 – $4.42
- Market cap: $40.34M
- Enterprise value: $129.24M
- Shares outstanding: 13.10M
- Beta: 1.458
- Book equity: $49.19M
- Revenue (latest): $57.23M
- EBITDA (latest): $1.86M
- Free cash flow (latest): -$10.24M
- Operating income: -$3.15M
- Operating margin: -5.5%
- EV / EBITDA: 69.5x
- ROIC: -4.0%
- FCF yield: -25.4%
- Debt / Equity: 1.3797625340544057
- FCF / share: -$0.78
- Revenue / share: $4.37

### Capital structure
- Cash: $1.56M
- Short-term debt: $4.43M
- Long-term debt: $39.52M
- Total debt: $67.86M
- Net debt: $66.31M
- Net debt / EBITDA: 35.6x

### Growth
- Revenue CAGR: 9.7%
- FCF CAGR: —
- Latest revenue YoY: 12.5%
- Latest FCF YoY: -1866.2%

### Market expectations (yfinance, sparse)
- Mean target: $8.17
- Target range: $7.00 – $10.00
- Recommendation: strong_buy

_Consensus revenue/EBITDA forecasts are often unavailable via free feeds; treat targets as point-in-time only._

### Historical KPIs (multi-year)

| Year | Revenue | OCF | Capex | FCF | EBITDA | LT debt | Cash | Net debt | Net income |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2025 | $57.23M | -$7.75M | $2.49M | -$10.24M | $1.86M | $39.52M | $1.56M | $37.96M | -$8.28M |
| 2024 | $50.85M | $3.38M | $2.80M | $580.00K | $2.45M | $13.04M | $1.04M | $12.01M | -$3.51M |
| 2023 | $45.17M | $5.17M | $4.03M | $1.14M | $3.36M | $9.83M | $2.91M | $6.92M | -$2.94M |
| 2022 | $43.35M | -$708.00K | $4.29M | -$5.00M | $7.53M | $13.07M | $1.63M | $11.44M | $1.88M |

## Charts

### Revenue & FCF history
![Revenue & FCF history](/charts/CREX_fast_revenue_fcf.png)

### DCF scenario prices
![DCF scenario prices](/charts/CREX_fast_dcf_scenarios.png)

### Base-case FCF path
![Base-case FCF path](/charts/CREX_fast_base_fcf_path.png)

## DCF valuation (base / bull / bear) [S2]

> Simplified revenue->FCF DCF. Not investment advice; assumptions are editable heuristics.

- Spot price: $3.08
- Base revenue: $57.23M
- Shares: 13,097,892
- Net debt (Debt−Cash): $66.31M

| Scenario | Growth | FCF margin | WACC | Term. g | Equity value | Share price | Upside |
|----------|--------|------------|------|---------|--------------|-------------|--------|
| bear | 5.5% | 1.0% | 12.0% | 1.5% | -$59.79M | $-4.57 | -248.2% |
| base | 12.5% | 3.0% | 10.0% | 2.5% | -$30.80M | $-2.35 | -176.4% |
| bull | 19.5% | 8.0% | 9.0% | 3.0% | $88.85M | $6.78 | 120.3% |

### Assumption notes
- Base revenue growth seeded from historical rate (12.5%).
- Latest FCF margin was -17.9%; scenarios use normalized positive margins for a going-concern DCF.

- _base: model equity value is negative after net debt (-30,803,035); showing $-2.35/sh._
- _bear: model equity value is negative after net debt (-59,791,969); showing $-4.57/sh._

### Base-case projected FCF

- Year 1: revenue $64.41M, FCF $1.93M (PV $1.76M)
- Year 2: revenue $72.49M, FCF $2.17M (PV $1.80M)
- Year 3: revenue $81.58M, FCF $2.45M (PV $1.84M)
- Year 4: revenue $91.81M, FCF $2.75M (PV $1.88M)
- Year 5: revenue $103.33M, FCF $3.10M (PV $1.92M)
- Terminal value $42.36M (PV $26.30M)

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

- **[S1]** CREX fundamentals (yfinance)
  - Creative Realities, Inc.: price=3.08, rev=57232000.0, fcf=-10244000.0, shares=13097892.0, rev_cagr=0.09702520767150968, ROIC=-0.04009801544695737, FCF yield=-0.2539320047232741
- **[S2]** CREX DCF valuation (dcf)
  - Base share price=-2.351755156061878, bull=6.783857023575285, bear=-4.565007007607608
- **[S3]** CREX put screen (yfinance_options)
  - Expiration None (DTE None): 0 candidates; IV=None, IV rank=None, HV rank=None. No options chain available

## Self-critique

_Automated review (heuristic)._

### Strengths
- Combines local fundamentals, optional DCF scenarios, and cited sources where available.
- Keeps a non-advisory framing for local research drafts.

### Issues & gaps
- Base-case model equity value is negative - treat intrinsic-value output as stress/distress, not a buy signal.
- Base-case implies deep downside vs spot (<-70%); confirm whether near-term FCF normalization is appropriate for this business.

### Caution for readers
- Treat scenario prices as sensitivity output, not a forecast.
- Re-check primary filings and fresh market data before any decision.
