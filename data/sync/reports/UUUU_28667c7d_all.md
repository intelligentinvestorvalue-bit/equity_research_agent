# UUUU — Full research pack

> Not investment advice. Local research draft only.

**Templates:** memo, valuation, deep, income, fast
**Generated:** 2026-07-21T22:45:59.746113+00:00



---

# Template: Institutional deep dive (memo) (`memo`)

# UUUU — Planned Research Report

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
- Company: Energy Fuels Inc
- Sector / industry: Energy / Uranium
- Price: 12.35
- 52-week range: $8.16 – $27.90
- Market cap: $3.09B
- Enterprise value: $2.70B
- Shares outstanding: 249.92M
- Beta: 1.583
- Book equity: $678.40M
- Revenue (latest): $65.92M
- EBITDA (latest): -$95.72M
- Free cash flow (latest): -$141.27M
- Operating income: -$101.16M
- Operating margin: -153.4%
- EV / EBITDA: -28.3x
- ROIC: -7.8%
- FCF yield: -4.6%
- Debt / Equity: 0.9959950177254
- FCF / share: -$0.57
- Revenue / share: $0.26

### Capital structure
- Cash: $64.74M
- Short-term debt: —
- Long-term debt: $675.69M
- Total debt: $675.69M
- Net debt: $610.95M
- Net debt / EBITDA: -6.4x

### Growth
- Revenue CAGR: 74.0%
- FCF CAGR: —
- Latest revenue YoY: -15.6%
- Latest FCF YoY: -88.4%

### Market expectations (yfinance, sparse)
- Mean target: $26.12
- Target range: $16.00 – $32.50
- Recommendation: strong_buy

_Consensus revenue/EBITDA forecasts are often unavailable via free feeds; treat targets as point-in-time only._

### Historical KPIs (multi-year)

| Year | Revenue | OCF | Capex | FCF | EBITDA | LT debt | Cash | Net debt | Net income |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2025 | $65.92M | -$89.48M | $51.79M | -$141.27M | -$95.72M | $675.69M | $64.74M | $610.95M | -$85.63M |
| 2024 | $78.11M | -$43.97M | $31.02M | -$75.00M | -$34.05M | — | $38.60M | -$38.60M | -$47.77M |
| 2023 | $37.93M | -$15.41M | $44.71M | -$60.12M | -$29.62M | — | $57.45M | -$57.45M | $99.86M |
| 2022 | $12.52M | -$49.70M | $2.00M | -$51.70M | -$56.51M | — | $62.82M | -$62.82M | -$59.85M |

## Charts

### Revenue & FCF history
![Revenue & FCF history](/charts/UUUU_memo_revenue_fcf.png)

### DCF scenario prices
![DCF scenario prices](/charts/UUUU_memo_dcf_scenarios.png)

### Base-case FCF path
![Base-case FCF path](/charts/UUUU_memo_base_fcf_path.png)

### EV/EBITDA scenario prices
![EV/EBITDA scenario prices](/charts/UUUU_memo_ev_ebitda_scenarios.png)

### Headwind/tailwind price ranges
![Headwind/tailwind price ranges](/charts/UUUU_memo_scenario_ranges.png)

### Normalized price vs peers
![Normalized price vs peers](/charts/UUUU_memo_peers_normalized.png)

## DCF valuation (base / bull / bear) [S3]

> Simplified revenue->FCF DCF. Not investment advice; assumptions are editable heuristics.

- Spot price: $12.35
- Base revenue: $65.92M
- Shares: 249,919,146
- Net debt (Debt−Cash): $610.95M

| Scenario | Growth | FCF margin | WACC | Term. g | Equity value | Share price | Upside |
|----------|--------|------------|------|---------|--------------|-------------|--------|
| bear | -15.6% | 1.0% | 12.0% | 1.5% | -$607.88M | $-2.43 | -119.7% |
| base | 6.0% | 3.0% | 10.0% | 2.5% | -$579.63M | $-2.32 | -118.8% |
| bull | 15.0% | 8.0% | 9.0% | 3.0% | -$461.55M | $-1.85 | -115.0% |

### Assumption notes
- Base revenue growth seeded from historical rate (-15.6%).
- Recent revenue declined (-15.6% YoY); base/bull use normalized mid-cycle growth instead of extrapolating the decline.
- Latest FCF margin was -214.3%; scenarios use normalized positive margins for a going-concern DCF.

- _base: model equity value is negative after net debt (-579,633,059); showing $-2.32/sh._
- _bull: model equity value is negative after net debt (-461,547,058); showing $-1.85/sh._
- _bear: model equity value is negative after net debt (-607,878,518); showing $-2.43/sh._

### Base-case projected FCF

- Year 1: revenue $69.88M, FCF $2.10M (PV $1.91M)
- Year 2: revenue $74.07M, FCF $2.22M (PV $1.84M)
- Year 3: revenue $78.51M, FCF $2.36M (PV $1.77M)
- Year 4: revenue $83.23M, FCF $2.50M (PV $1.71M)
- Year 5: revenue $88.22M, FCF $2.65M (PV $1.64M)
- Terminal value $36.17M (PV $22.46M)

## Valuation — EV/EBITDA scenarios [S2]

> Priced-in model: implied price = (EBITDA × EV/EBITDA − net debt) ÷ shares. Not a forecast.

- Spot: $12.35
- Net debt used: $610.95M

| Scenario | EBITDA | EV/EBITDA | Implied EV | Equity value | Implied price |
|---|---:|---:|---:|---:|---:|
| bear | $700.00M | 6.0x | $4.20B | $3.59B | $14.36 |
| base | $1.00B | 8.0x | $8.00B | $7.39B | $29.57 |
| bull | $1.20B | 10.0x | $12.00B | $11.39B | $45.57 |

- EBITDA missing or non-positive; scenarios use placeholder $1B EBITDA — edit before relying on prices.
- No current EV/EBITDA; defaulted base multiple to 8.0x.

## Scenario price ranges (headwinds & tailwinds) [S39]

> Medium-term (18–36 months (medium / medium-long term)) driver → EV/EBITDA bridge. Distinct from the FCF DCF path. Not investment advice.

- Spot: $12.35
- Sparse Street mean target: $26.12
- Anchor multiple: 8.0x (driver_ev_ebitda_bridge)
- Anchor EBITDA: $1.00B
- Probability-weighted midpoint: **$27.22** (heuristic weights, not a rating)
- Driver extraction: `rules`

### Headwinds (bear-case fuel)

- **Negative free cash flow** — Latest FCF -$141.27M — cash burn raises financing risk _(source: fundamentals)_
- **Revenue contraction** — Latest revenue YoY ≈ -15.6% _(source: fundamentals)_
- **Balance-sheet / refinancing pressure** — sector=Energy industry=Uranium revenue=65922000.0 ebitda=-95724000.0 fcf=-141273000.0 net_debt=610952000.0 nd_ebitda=-6.382432827713008 target=26.125 rec=strong_buy _(source: fundamentals)_
- **Regulatory / legal risk** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, supply chain, interest rate, custome _(source: item_1a)_
- **Competitive / pricing pressure** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, supply chain, interest rate, custome _(source: item_1a)_
- **Margin / cost headwind** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, supply chain, interest rate, custome _(source: item_1a)_
- **Operational / cyber risk** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, supply chain, interest rate, custome _(source: item_1a)_
- **Dilution / liquidity stress** — UUUU — Energy Fuels Inc. - Deep Dives Hub The stock is cheap relative to analyst targets and offers a way to bet on a U.S. nuclear revival and rising uranium prices. The main risks _(source: web)_

### Tailwinds (bull-case fuel)

- **Manageable leverage** — Net debt / EBITDA ≈ -6.4x — room for reinvestment or returns _(source: fundamentals)_
- **Street target implies upside** — Mean target $26.12 vs spot $12.35 _(source: fundamentals)_
- **Growth / execution upside** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, supply chain, interest rate, custome _(source: item_1a)_
- **Product / pricing power** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, supply chain, interest rate, custome _(source: item_1a)_
- **Multiple re-rating / Street upgrades** — Energy Fuels Inc. (UUUU) Analyst Ratings, Estimates ... See Energy Fuels Inc. (UUUU) stock analyst estimates, including earnings and revenue, EPS, upgrades and downgrades. _(source: web)_
- **Contract / backlog wins** — UUUU — Energy Fuels Inc. - Deep Dives Hub The stock is cheap relative to analyst targets and offers a way to bet on a U.S. nuclear revival and rising uranium prices. The main risks _(source: web)_

### Price ranges by case

| Case | Prob. | Metric vs TTM | Multiple | Price low | Mid | High | Upside vs spot |
|---|---:|---:|---:|---:|---:|---:|---:|
| bear | 0.34 | 0.68x | 4.8x | $9.31 | $10.62 | $11.92 | -14% |
| base | 0.45 | 0.96x | 8.0x | $26.13 | $28.29 | $30.44 | +129% |
| bull | 0.21 | 1.21x | 11.2x | $46.39 | $51.82 | $57.25 | +320% |

#### Bear — headwinds dominate

Headwinds bite: weaker operating trajectory and multiple compression. Equity duration shrinks if cash generation fails to offset leverage / competitive pressure.

- **Range:** $9.31 – $11.92 (mid $10.62) · EBITDA $680.00M · multiple 4.8x
- Driver: **Negative free cash flow** — Latest FCF -$141.27M — cash burn raises financing risk
- Driver: **Revenue contraction** — Latest revenue YoY ≈ -15.6%
- Driver: **Balance-sheet / refinancing pressure** — sector=Energy industry=Uranium revenue=65922000.0 ebitda=-95724000.0 fcf=-141273000.0 net_debt=610952000.0 nd_ebitda=-6.382432827713008 target=26.125 rec=strong
- Driver: **Regulatory / legal risk** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, supply chain, in
- Driver: **Competitive / pricing pressure** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, supply chain, in

#### Base — mixed execution

Balanced path: some tailwinds offset headwinds. Operating scale roughly holds with modest repair/normalization; valuation stays near the current EV/EBITDA anchor.

- **Range:** $26.13 – $30.44 (mid $28.29) · EBITDA $960.00M · multiple 8.0x
- Driver: **Manageable leverage** — Net debt / EBITDA ≈ -6.4x — room for reinvestment or returns
- Driver: **Street target implies upside** — Mean target $26.12 vs spot $12.35
- Driver: **Negative free cash flow** — Latest FCF -$141.27M — cash burn raises financing risk
- Driver: **Revenue contraction** — Latest revenue YoY ≈ -15.6%

#### Bull — tailwinds dominate

Tailwinds compound: operating improvement plus a re-rating toward peer or recovery multiples as balance-sheet and growth narratives improve.

- **Range:** $46.39 – $57.25 (mid $51.82) · EBITDA $1.21B · multiple 11.2x
- Driver: **Manageable leverage** — Net debt / EBITDA ≈ -6.4x — room for reinvestment or returns
- Driver: **Street target implies upside** — Mean target $26.12 vs spot $12.35
- Driver: **Growth / execution upside** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, supply chain, in
- Driver: **Product / pricing power** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, supply chain, in
- Driver: **Multiple re-rating / Street upgrades** — Energy Fuels Inc. (UUUU) Analyst Ratings, Estimates ... See Energy Fuels Inc. (UUUU) stock analyst estimates, including earnings and revenue, EPS, upgrades and 

### Method notes

- Item 1A risks weighted toward headwinds.
- Current ev_ebitda multiple missing; anchored at 8.0x.
- Peer EV/EBITDA band 6.3x–11.8x (median 10.5x) informs multiple ranges.
- Mapping follows Gemini/Perplexity-style scenario memos: qualitative drivers → operating metric & multiple paths → share-price ranges over a medium-term horizon.

## Peer & factor comps

- Sector / industry: Energy / Uranium
- Peers: XOM, CVX, COP, SLB, EOG

| Ticker | Mkt cap | EV/EBITDA | ND/EBITDA | Beta | 1y | 5y | Vol |
|---|---:|---:|---:|---:|---:|---:|---:|
| UUUU | $3.1B | -33.3x | 2.9x | 1.58 | 34.1% | 138.4% | 73.2% |
| XOM | $628.8B | 11.8x | 0.7x | 0.16 | 44.9% | 219.3% | 26.7% |
| CVX | $380.5B | 11.1x | 1.1x | 0.49 | 33.0% | 137.4% | 25.1% |
| COP | $143.1B | 6.8x | 0.7x | 0.12 | 33.4% | 147.8% | 32.7% |
| SLB | $69.7B | 10.5x | 1.1x | 0.73 | 42.7% | 85.8% | 37.4% |
| EOG | $76.4B | 6.3x | 0.4x | 0.26 | 27.4% | 146.5% | 32.6% |

- Peer set (heuristic by sector/industry): XOM, CVX, COP, SLB, EOG
- Beta vs XOM (daily, ~5y overlap): 0.65

_Price returns are price-only (dividends ignored). Peer set is heuristic, not a formal comps universe._

## Earnings, guidance & revision catalysts

- Next earnings (calendar): 2026-08-06

| Date | EPS est | EPS actual | Surprise | 1-day move |
|---|---:|---:|---:|---:|
| 2026-08-06 | -0.04 | — | — | — |
| 2026-05-06 | -0.01 | -0.04 | -0.03 | -0.7% |
| 2026-02-26 | -0.07 | -0.09 | -0.02 | -6.7% |
| 2025-11-03 | -0.05 | -0.07 | -0.02 | -4.4% |
| 2025-08-06 | -0.04 | -0.10 | -0.06 | -0.8% |
| 2025-05-07 | -0.07 | -0.13 | -0.06 | 0.2% |
| 2025-02-26 | — | -0.19 | — | -9.5% |
| 2024-10-31 | -0.04 | -0.07 | -0.03 | -7.0% |
| 2024-08-02 | -0.07 | -0.04 | 0.03 | -3.5% |
| 2024-05-03 | 0.02 | 0.02 | 0.00 | 4.0% |
| 2024-02-23 | -0.06 | -0.14 | -0.08 | 5.3% |
| 2023-11-03 | -0.03 | 0.07 | 0.10 | -3.5% |

_EPS surprise vs 1-day move Pearson r=-0.355 (n=10, p≈0.283); treat as suggestive only._

_Guidance vs Street and adjusted EBITDA are often missing from free feeds; use web/SEC sections for narrative guidance._

## Recent SEC filings (10-Q / 8-K)

| Date | Form | Description |
|---|---|---|
| 2026-07-14 | 8-K | [FORM 8-K](https://www.sec.gov/Archives/edgar/data/1385849/000106299326003630/form8k.htm) |
| 2026-06-26 | 8-K | [FORM 8-K](https://www.sec.gov/Archives/edgar/data/1385849/000106299326003385/form8k.htm) |
| 2026-06-23 | 8-K | [FORM 8-K](https://www.sec.gov/Archives/edgar/data/1385849/000106299326003317/form8k.htm) |
| 2026-05-15 | 8-K | [FORM 8-K](https://www.sec.gov/Archives/edgar/data/1385849/000106299326002713/form8k.htm) |
| 2026-05-06 | 10-Q | [10-Q](https://www.sec.gov/Archives/edgar/data/1385849/000138584926000021/efr-20260331.htm) |
| 2026-04-17 | 8-K | [FORM 8-K](https://www.sec.gov/Archives/edgar/data/1385849/000106299326002047/form8k.htm) |
| 2026-03-18 | 8-K | [FORM 8-K](https://www.sec.gov/Archives/edgar/data/1385849/000106299326001527/form8k.htm) |
| 2026-03-03 | 8-K | [FORM 8-K](https://www.sec.gov/Archives/edgar/data/1385849/000106299326001257/form8k.htm) |
| 2026-02-26 | 10-K | [10-K](https://www.sec.gov/Archives/edgar/data/1385849/000138584926000009/efr-20251231.htm) |
| 2026-02-26 | 8-K | [FORM 8-K](https://www.sec.gov/Archives/edgar/data/1385849/000106299326001182/form8k.htm) |
| 2026-01-26 | 8-K | [FORM 8-K](https://www.sec.gov/Archives/edgar/data/1385849/000106299326000431/form8k.htm) |
| 2026-01-13 | 8-K | [FORM 8-K](https://www.sec.gov/Archives/edgar/data/1385849/000106299326000229/form8k.htm) |

_Headlines/meta only — documents not fully parsed in this pass._

## Key driver analysis (quarterly)

Pearson / Spearman correlations of quarterly stock returns with fundamentals.

| Driver | Pearson r | p | n | Spearman ρ | p |
|---|---:|---:|---:|---:|---:|
| Revenue growth (YoY) | — | — | 1 | — | — |
| Free cash flow | -0.456 | 0.375 | 5 | -0.700 | 0.090 |
| FCF margin | -0.225 | 0.689 | 5 | -0.500 | 0.317 |
| Operating cash flow | -0.423 | 0.419 | 5 | -0.600 | 0.194 |
| Long-term debt level | — | — | 2 | — | — |
| EBITDA | -0.286 | 0.605 | 5 | -0.300 | 0.586 |
| Capex (abs) | 0.187 | 0.741 | 5 | 0.300 | 0.586 |

### Regime check (FCF)

- later: r=-0.456 (n=5, p≈0.375)

- Correlations describe association, not causation.
- Small samples (especially regime splits) are directional only.
- Regime split at 2023-12-31 (sample midpoint); directional only.

## Executive summary

Energy Fuels Inc (UUUU) trades near 12.35 with market cap $3.09B and EV $2.70B. Net debt is $610.95M (ND/EBITDA -6.382432827713008). Latest revenue $65.92M, EBITDA -$95.72M, FCF -$141.27M.

**Goal focus:** Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers.

What matters most (framework): balance-sheet trajectory, cash generation vs leverage, and whether market expectations (sparse free-data targets) already price execution risk.

EV/EBITDA implied prices — bear $14.36 / base $29.57 / bull $45.57.

## Company setup & business model

**Keyword hits:** risk, uncertainty, guidance, revenue, margin, supply chain, customer, segment, product, market, operations, subsidiary

- On August 16, 2024, the Company acquired RadTran LLC (“RadTran”), a private company specializing in the separation of critical radioisotopes, to further the Company’s plans for development  and production of medical isotopes used in cancer treatments.
- All of the Company’s U.S.-based employees are employed by its subsidiary Energy Fuels Resources (USA) Inc.
- (“EFUSA”), a wholly owned subsidiary of EF Holdings, which also serves as operator of all the Company’s U.S.
- On February 10, 2023, the Company, through its wholly owned subsidiary Energy Fuels Brazil Ltda., acquired the Bahia Project in the State of Bahia, Brazil.
- On October 2, 2024, the Company acquired Base Resources, which owned the Kwale Project, which is now in reclamation, and the Vara Mada Project in Madagascar, which is currently in permitting and development, thereby further increasing its portfolio of HMS/monazite/REE projects to support a U.S.-controlled REE supply chain.
- The primary trading market for Energy Fuels’ Common Shares is the NYSE American under the trading symbol “ UUUU,” and the Company’s Common Shares are also listed on the TSX under the trading symbol “EFR.” Energy Fuels is a U.S.
- The Designated Primary Market Maker for the Options is Group One Trading, LP.
- Citadel Securities is the Company’s Market Maker on the NYSE American.
- Table of Conten t s  Business Overview  Energy Fuels produces several of the critical minerals essential to the United States (“U.S.”), energy security and other advanced technologies, including uranium, vanadium, REEs (including NdPr, Dy and Tb) and HMS (including titanium and zirconium minerals), in an effort to strengthen domestic supply chains and reduce reliance on foreign-controlled sources.
- due to its notable ability to process uranium, vanadium, REE products, and, potentially, radioisotopes for medical applications.
- We produce vanadium as a co-product from certain of our uranium mines, as market conditions  warrant.
- The REE products we produce are essential to manufacture permanent magnets for traction motors in electric  vehicles (“EVs”), hybrid EVs, defense systems, robotics and other advanced technologies.
- The titanium and zirconium products derived from our HMS products are used in national security and other key industries.
- In processing Alternate Feed Materials, the Mill also helps reduce the quantity of  industry materials permanently disposed of and, by extension, the overall tailings footprint of mining and milling operations.
- controlled REE supply chain, which include:  • the Vara Mada Project acquired through the Company’s 100% acquisition of Base Resources on October 2, 2024, see Part I, Item 2.
- Upon closing of this transaction, which is expected as  early as June 2026, the Company believes it will be the largest, fully integrated REE “mine-to-metal and alloy” producer outside of China closing a critical strategic gap in global supply chains for magnet applications, including automotive, robotic, energy and defense technologies.
- Segment Information  We have three reportable segments based on our operations and the financial information regularly reviewed by our Chief Operating Decision Maker (“ CODM”): (i) uranium, (ii) REE, and (iii) HMS.
- The uranium segment engages in conventional and ISR uranium extraction, recovery and sales of uranium from mineral properties and the recycling of uranium-bearing materials generated by third parties (Alternate Feed Materials) along with the exploration, permitting and evaluation of uranium properties in the U.S.
- The Company’s final uranium product is natural uranium concentrate, or U3 O8, which is sold to customers for further processing into fuel for nuclear reactors.
- The Company also produces vanadium pentoxide, V2 O5, as a co-product of uranium at the Mill within the uranium segment.
- In addition,  Table of Conten t s  within the uranium segment, the Company is exploring opportunities to separate radium-226 (“Ra-226”) and radium-228 (“Ra-228”) as a byproduct of its existing uranium and REE process streams for potential use in the production of medical isotopes for emerging TAT cancer treatments.
- The REE segment is engaged in the Company’s initiatives to progress towards full REE separation capabilities at the Mill to produce both “light” and “heavy” separated REE oxides.
- The Company has the current capacity to produce separated REE products in  its Phase 1 Circuit.
- The Company is planning further enhancements to expand its heavy REE production at its Phase 1 Circuit for the planned recovery of dysprosium (“Dy”), terbium (“Tb”), samarium (“Sm”), europium (“Eu”) and gadolinium (“Gd”), with the ability to separate other heavy REEs such as yttrium (“Y”) and lutetium (“Lu”) if market conditions warrant, subject to the receipt of regulatory approvals, financing, completion of engineering and the receipt of sufficient feed materials.
- The  Company also plans to expand its NdPr, Dy and Tb production recovery and potentially other REE material production recovery in the future, subject to the receipt of regulatory approvals, completion of engineering, financing and the receipt of sufficient feed materials, through the development of its proposed stand-alone phase 2 REE production circuit (the “Phase 2 Circuit”) with a total planned production recovery (from the Phase 1 Circuit and Phase 2 Circuit) of up to approximately 6,000 tonnes of NdPr, 200 tonnes of Dy and 60 tonnes of Tb per year, along with other REEs, described in more detail below, from monazite concentrates, mixed rare earth carbonates (“MREC”) or similar feed materials.
- The monazite feedstock for the Company’s REE production is expected to be procured through Company-owned mines like the Vara Mada Project and Bahia Project, as well as its joint venture interest in the Donald Project, along with other potential acquisitions, joint ventures, open market offtake,  and/or other collaborations, in each case upon successful completion of development of the projects and transactions.
- The HMS segment engages in the exploration and development, and planned recovery, of HMS at the Vara Mada Project, Bahia Project and through the Company’s investment in the Donald Project JV.
- The HMS segment also includes the Kwale Project, which ceased mine operations on December 31, 2024 and is now in reclamation.

_Source: latest 10-K Item 1 (Business), summarized locally._

## Variant perception

- **Consensus frame (sparse):** recommendation=strong_buy, mean target=26.125.
- **Bear:** leverage and execution risk dominate; cash generation fails to cover refinancing / reinvestment needs; equity remains constrained by net debt.
- **Bull:** cash-flow and strategic optionality re-rate the equity as leverage falls and growth/mix improves.
- **Middle:** returns may track free-cash-flow more than headline revenue — verify with driver analysis tab.

## Catalysts & monitoring

- Next earnings window (calendar): 2026-08-06
- Peer tape to watch: XOM, CVX, COP, SLB, EOG
- Monitor: FCF vs net debt, leverage (ND/EBITDA), refinancing headlines, and material 8-K strategy updates.
- Recent filing: 8-K on 2026-07-14 — FORM 8-K
- Recent filing: 8-K on 2026-06-26 — FORM 8-K
- Recent filing: 8-K on 2026-06-23 — FORM 8-K
- Recent filing: 8-K on 2026-05-15 — FORM 8-K
- Recent filing: 10-Q on 2026-05-06 — 10-Q

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
| Guidance / outlook | Forward cash/earnings path | Energy Fuels (UUUU) Stock Forecast and Price Target 2026 UUUU's current price target is $23.25. Learn why top analysts are making this stock forecast for Energy Fuels at MarketBeat | Energy Fuels (UUUU) Stock Forecast and Price Target 2026 |
| Capex / capacity | Leading indicator of future revenue | Energy Fuels Inc. (UUUU) Deep Dive - by Danny Green The uranium spot price appears well-supported at current levels, with potential for a catch-up trade in 2026. The structural the | Energy Fuels Inc. (UUUU) Deep Dive - by Danny Green |
| Margin / EBITDA | Mix and operating leverage | Energy Fuels (UUUU) / Trefis / Trefis The gross margin for uranium is projected to increase from 31% in 2025 to 50% in 2026. Growing demand for nuclear power, particularly to fuel  | Energy Fuels (UUUU) | Trefis | Trefis |

_Proxies are heuristic extractions from public web/SEC context; verify against primary filings._

## Catalyst calendar

| Window | Catalyst | Notes |
|---|---|---|
| 2026-08-06 | Earnings | Next report date from yfinance calendar |
| 2026-07-14 | 8-K | FORM 8-K |
| 2026-06-26 | 8-K | FORM 8-K |
| 2026-06-23 | 8-K | FORM 8-K |
| 2026-05-15 | 8-K | FORM 8-K |
| 2026-05-06 | 10-Q | 10-Q |
| 2026-04-17 | 8-K | FORM 8-K |
| 2026-03-18 | 8-K | FORM 8-K |
| 2026-03-03 | 8-K | FORM 8-K |
| 2026-02-26 | 10-K | 10-K |
| 2026-02-26 | 8-K | FORM 8-K |
| 2026-01-26 | 8-K | FORM 8-K |
| 2026-01-13 | 8-K | FORM 8-K |
| June 11, 2026 | Web event | This Critical Materials Stock Surged Over 150% In A Year – The Firm’s Now Ready To Hit 2026 Production Guidance In Just 6 Months |
| April 27, 2026 | Web event | UUUU stock forecast, quote, news & analysis |
| August 27, 2025 | Web event | The Surging UUUU Stock: Decoding the Catalyst Behind Its Recent Rally |
| Jan 15, 2026 | Web event | Energy Fuels (UUUU) Stock Price & OverviewEnergy Fuels' U.S. Rare Earth Processing Expansion Boasts ...Energy Fuels Inc. (UUUU) Analyst Insi |
| Jan 15, 2026 | Web event | Energy Fuels' U.S. Rare Earth Processing Expansion Boasts ... |
| June 8, 2026 | Web event | UUUU Trades at a Premium to the Industry: How to Play the Stock? |
| July 25, 2025 | Web event | Energy Fuels (UUUU): Is This Uranium Play Poised to Outperform the Market Amid a Resurging Nuclear Sector? |
| December 23, 2024 | Web event | Zacks Industry Outlook Highlights Southern Copper, Coeur Mining and Energy Fuels |

## Web research — web_analysts

- Queries: UUUU analyst price target, Energy Fuels Inc stock rating OR consensus OR upgrade OR downgrade, UUUU Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers analyst, UUUU guidance OR investor day OR catalyst
- Unique hits: 21
- Pages fetched: 3/3

### Web synthesis — web_analysts (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, guidance, revenue, customer, product, service, market

- [HIT] Energy Fuels (UUUU) Stock Forecast and Price Target 2026 | www.marketbeat.com | https://www.marketbeat.com/stocks/NYSEAMERICAN/UUUU/forecast/ UUUU's current price target is $23.25.
- Learn why top analysts are making this stock forecast for Energy Fuels at MarketBeat.
- (UUUU) stock, with detailed revenue and earnings estimates.
- [HIT] Roth MKM Reaffirms Their Hold Rating on Energy Fuels (UUUU) | The Globe and Mail | https://www.theglobeandmail.com/investing/markets/stocks/UUUU/pressreleases/14495/roth-mkm-reaffirms-their-hold-rating-on-energy-fuels-uuuu/ Detailed price information for Energy Fuels Inc (UUUU-A) from The Globe and Mail including charting and trades.
- [HIT] Roth MKM Remains a Hold on Energy Fuels (UUUU) | The Globe and Mail | https://www.theglobeandmail.com/investing/markets/stocks/UUUU-A/pressreleases/2604873/roth-mkm-remains-a-hold-on-energy-fuels-uuuu/ Detailed price information for Energy Fuels Inc (UUUU-A) from The Globe and Mail including charting and trades.
- (UUUU) stock analyst estimates, including earnings and revenue, EPS, upgrades and downgrades.
- [HIT] Energy Fuels (UUUU) Stock Price, News & Analysis - MarketBeatEnergy Fuels Inc (UUUU) Stock Forecast & Price TargetEnergy Fuels - UUUU - Stock Price Today - ZacksUUUU News Today | Why did Energy Fuels stock go up today?
- | www.marketbeat.com | https://www.marketbeat.com/stocks/NYSEAMERICAN/UUUU/ Should You Buy or Sell Energy Fuels Stock?

### Sources found
- [Energy Fuels (UUUU) Stock Forecast and Price Target 2026](https://www.marketbeat.com/stocks/NYSEAMERICAN/UUUU/forecast/)
  - UUUU's current price target is $23.25. Learn why top analysts are making this stock forecast for Energy Fuels at MarketBeat.
- [UUUU Price Target: $22 (+87%) | 9 Analyst Ratings 2026](https://vcpscanner.com/stock/uuuu/price-target)
  - Energy Fuels Inc. (UUUU) has a $22 consensus price target from 9 analysts (Buy). View upside analysis, rating distribution & peer comparison.
- [What is the current Price Target and Forecast for Energy Fuels (UUUU)](https://www.zacks.com/stock/research/UUUU/price-target-stock-forecast)
  - Price Target Based on short-term price targets offered by five analysts, the average price target for Energy Fuels comes to $25.69. The forecasts range from …
- [Energy Fuels (UUUU) Stock Forecast & Analyst Price Targets](https://stockanalysis.com/stocks/uuuu/forecast/)
  - Stock forecasts and analyst price target predictions for Energy Fuels Inc. (UUUU) stock, with detailed revenue and earnings estimates.
- [Is Energy Fuels Inc. (UUUU) Stock Still a Long-Term Opportunity After Analyst Price Target Cut?](https://finance.yahoo.com/energy/articles/energy-fuels-inc-uuuu-stock-200741850.html)
  - We recently compiled a list of the 8 Best Rare Earth Stocks to Buy in 2026. Energy Fuels Inc. (NYSEAMERICAN:UUUU) is among the best rare earth stocks on this…
- [Roth MKM Reaffirms Their Hold Rating on Energy Fuels (UUUU)](https://www.theglobeandmail.com/investing/markets/stocks/UUUU/pressreleases/14495/roth-mkm-reaffirms-their-hold-rating-on-energy-fuels-uuuu/)
  - Detailed price information for Energy Fuels Inc (UUUU-A) from The Globe and Mail including charting and trades.
- [Roth MKM Remains a Hold on Energy Fuels (UUUU)](https://www.theglobeandmail.com/investing/markets/stocks/UUUU-A/pressreleases/2604873/roth-mkm-remains-a-hold-on-energy-fuels-uuuu/)
  - Detailed price information for Energy Fuels Inc (UUUU-A) from The Globe and Mail including charting and trades.
- [Wall Street bulls look optimistic about Energy Fuels (UUUU): Should you buy?](https://www.msn.com/en-us/money/top-stocks/wall-street-bulls-look-optimistic-about-energy-fuels-uuuu-should-you-buy/ar-AA27uqQa?ocid=BingNewsVerp)
  - Investors often turn to recommendations made by Wall Street analysts before making a Buy, Sell, or Hold decision about a ...
- [Energy Fuels Inc. (UUUU) Analyst Ratings, Estimates ...](https://finance.yahoo.com/quote/UUUU/analysis/?fr=sycsrp_catchall)
  - See Energy Fuels Inc. (UUUU) stock analyst estimates, including earnings and revenue, EPS, upgrades and downgrades.
- [Energy Fuels Inc. (UUUU) Stock Price, News, Quote & History ...](https://finance.yahoo.com/quote/UUUU/?fr=sycsrp_catchall)
  - Find the latest Energy Fuels Inc. (UUUU) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Energy Fuels (UUUU) Stock Price, News & Analysis - MarketBeatEnergy Fuels Inc (UUUU) Stock Forecast & Price TargetEnergy Fuels - UUUU - Stock Price Today - ZacksUUUU News Today | Why did Energy Fuels stock go up today?](https://www.marketbeat.com/stocks/NYSEAMERICAN/UUUU/)
  - Should You Buy or Sell Energy Fuels Stock? Get The Latest UUUU Stock Analysis, Price Target, Earnings Estimates, and Headlines at MarketBeat. Find the latest…
- [Energy Fuels Inc (UUUU) is attracting investor attention: Here is what you should know](https://www.msn.com/en-us/money/investment/energy-fuels-inc-uuuu-is-attracting-investor-attention-here-is-what-you-should-know/ar-AA28j4fe)
  - Energy Fuels (UUUU) is one of the stocks most watched by Zacks.com visitors lately. So, it might be a good idea to review some of the factors that might affe…

### Search warnings
- news:UUUU Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers analyst: No results found.
- news:UUUU guidance OR investor day OR catalyst: No results found.

## Web research — web_drivers

- Queries: UUUU Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers, Energy Fuels Inc UUUU outlook OR catalyst OR commodity OR uranium OR rare earth OR vanadium, UUUU sector drivers OR market demand, Energy Fuels Inc UUUU backlog OR contract OR refinancing OR leverage
- Unique hits: 19
- Pages fetched: 2/3

### Web synthesis — web_drivers (rule-based fallback — Ollama unavailable)
**Keyword hits:** capex, revenue, margin, supply chain, customer, product, service, market

- [HIT] Energy Fuels (UUUU) Institutional Ownership 2026 | www.marketbeat.com | https://www.marketbeat.com/stocks/NYSEAMERICAN/UUUU/institutional-ownership/ View UUUU institutional ownership (13F) transactions at MarketBeat.Institutional investors have sold a total of 30,298,766 shares in the last 24 months.
- | www.nasdaq.com | https://www.nasdaq.com/market-activity/stocks/uuuu/institutional-holdings About Institutional Holdings.
- (UUUU) stock, with detailed revenue and earnings estimates.
- rare earth supply chain that is world-competitive.
- Read today's UUUU news from trusted media outlets at MarketBeat.
- (NYSE: UUUU), following its collaboration with Vulcan Elements to establish a domestic supply chain for rare earth magnets, saw its stock rise 18% on Tuesday, August 26, 2025 ...
- | investors.energyfuels.com | https://investors.energyfuels.com/2026-01-15-Energy-Fuels-U-S-Rare-Earth-Processing-Expansion-Boasts-Lower-Than-Expected-CAPEX,-Significant-Annual-EBITDA,-and-Among-the-Lowest-Cost-NdPr-Production-in-the-World Jan 15, 2026 · A redacted copy of the BFS can be found here.
- rare earth supply chain that is world-competitive.

### Sources found
- [Energy Fuels (UUUU) Institutional Ownership 2026](https://www.marketbeat.com/stocks/NYSEAMERICAN/UUUU/institutional-ownership/)
  - View UUUU institutional ownership (13F) transactions at MarketBeat.Institutional investors have sold a total of 30,298,766 shares in the last 24 months. This…
- [Energy Fuels Inc Ordinary Shares (Canada) (UUUU) Institutional...](https://www.nasdaq.com/market-activity/stocks/uuuu/institutional-holdings)
  - About Institutional Holdings. Nasdaq provides the ownership stake information in a company, including the number of shares held by those institutions in a fi…
- [Deep Dive Dubai: Scuba Diving, Freediving, & Snorkelling](https://www.deepdivedubai.com/)
  - Explore Deep Dive Dubai, the world’s deepest pool for scuba diving, freediving, and snorkelling in the UAE.
- [Scenarios](https://www.scenario.blondinka.org/)
  - Список сценариев. Развлечение госпожи Марии от пользователя Blondinka. 12 заданий Госпожей от пользователя Blondinka. Начальная тренировка членососки от поль…
- [Energy Fuels Inc. (UUUU) Stock Price, News, Quote & History ...](https://finance.yahoo.com/quote/UUUU/?fr=sycsrp_catchall)
  - Find the latest Energy Fuels Inc. (UUUU) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Energy Fuels (UUUU) Stock Forecast & Analyst Price Targets](https://stockanalysis.com/stocks/uuuu/forecast/)
  - Stock forecasts and analyst price target predictions for Energy Fuels Inc. (UUUU) stock, with detailed revenue and earnings estimates.
- [Energy Fuels (UUUU) Stock Price & OverviewEnergy Fuels' U.S. Rare Earth Processing Expansion Boasts ...Energy Fuels Inc. (UUUU) Analyst Insights, Price Targets ...UUUU News Today | Why did Energy Fuels stock go up today?Energy Fuels: More Upside For UUUU Stock After 2x Gains? - Forbes](https://stockanalysis.com/stocks/uuuu/)
  - A detailed overview of Energy Fuels Inc. (UUUU) stock, including real-time price, chart, key statistics, news, and more. Jan 15, 2026 · A redacted copy of th…
- [Energy Fuels' U.S. Rare Earth Processing Expansion Boasts ...](https://investors.energyfuels.com/2026-01-15-Energy-Fuels-U-S-Rare-Earth-Processing-Expansion-Boasts-Lower-Than-Expected-CAPEX,-Significant-Annual-EBITDA,-and-Among-the-Lowest-Cost-NdPr-Production-in-the-World)
  - Jan 15, 2026 · A redacted copy of the BFS can be found here. "Energy Fuels is on the cusp of solving America's rare earth processing 'bottleneck'," stated Ma…
- [UUUU Trades at a Premium to the Industry: How to Play the Stock?](https://finance.yahoo.com/markets/stocks/articles/uuuu-trades-premium-industry-play-171800358.html)
  - June 8, 2026 - ... Both the estimates have undergone negative revisions in the past 60 days, as shown in the chart below. ... The company's long-term outlook…
- [Energy Fuels (UUUU): Is This Uranium Play Poised to Outperform the Market Amid a Resurging Nuclear Sector?](https://www.ainvest.com/news/energy-fuels-uuuu-uranium-play-poised-outperform-market-resurging-nuclear-sector-2507/)
  - July 25, 2025 - This institutional backing is critical in a market where large investors can drive liquidity and momentum, especially in a high-beta stock li…
- [Energy Fuels (UUUU) | Trefis | Trefis](https://www.trefis.com/data/companies/uuuu)
  - The gross margin for uranium is projected to increase from 31% in 2025 to 50% in 2026. Growing demand for nuclear power, particularly to fuel energy-intensiv…
- [Markets - Financial Advisors - Latest News about Energy Fuels Inc Ordinary Shares (Canada) (NYSE:UUUU) | Energy Fuels Inc Ordinary Shares (Canada) (NYSE:UUUU) News](https://markets.financialcontent.com/1discountbrokerage/quote/news?CurrentPage=3&ChannelType=NEWS&Symbol=NY:UUUU)
  - The convergence of booming energy demands with severely constrained supplies positions uranium mining for substantial price increases. ... One of the biggest…

### Search warnings
- news:UUUU Institutional deep dive: thesis, priced-in scenarios, catalysts, falsifiers: No results found.
- news:Energy Fuels Inc UUUU outlook OR catalyst OR commodity OR uranium OR rare earth OR vanadium: No results found.
- news:Energy Fuels Inc UUUU backlog OR contract OR refinancing OR leverage: No results found.

## SEC filing [S27]
- Extraction OK: True
- Item 1 chars: 80000
- Item 1A chars: 50000
- Item 7 chars: 50000
- Meta: {'source': 'cache', 'path': 'C:\\DevWork\\equity_research_agent\\data\\filings\\UUUU_10k.txt'}

## Qualitative analysis (local LLM)

_Item 1 Business summary mode: rule_based (see Company setup & business model)._

### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, uncertainty, litigation, regulation, competition, supply chain, interest rate, customer, product, service, market, operations

- Other factors may arise in the future that are currently not foreseen by management of Energy Fuels that may present additional risks, including risks that the Company currently feels are immaterial.
- Current and prospective shareholders of Energy Fuels should carefully consider these risk factors when making investment decisions.
- Our failure to successfully address any of the risks and uncertainties described below could have a material adverse effect on our business, financial condition and/or results of operations, and the trading price of our Common Shares may fluctuate widely.
- We cannot assure you that we have or will successfully or fully address these risks or other unknown risks that may affect our business.
- Risks Related to our Industry  We are subject to the risks normally encountered by companies in the mineral extraction industry.
- We are subject to the risks normally encountered by companies in the mineral extraction industry, such as:  • the discovery of unusual or unexpected geological formations, and variations in ore radiation levels;  • wild/bushfires, floods, earthquakes, tornados, tropical cyclones, droughts, landslides and other natural disasters;  • accidental fires, unplanned power outages and water shortages;  • controlling water, emissions and other similar mining hazards;  • operating labor disruptions and labor disputes;  • the ability to obtain and maintain suitable or adequate machinery, equipment or labor;  • our liability for potential or existing pollution or other hazards; and  • other known and unknown risks involved in the conduct of exploration, development and operation of mines, E&R facilities and mills, and metals and alloys plants (pending the successful acquisition of ASM), along with the markets for uranium, rare earths, vanadium, HMS and metals and alloys.
- The development of mineral properties is affected by many factors, including, but not limited to: the cost of operations; variations in the grade of mineralized material; fluctuations in metal markets; costs of extraction and processing equipment; availability of equipment and labor; labor costs and possible labor strikes; government regulations, including without limitation, regulations relating to taxes, royalties, allowable extraction or production, and importing and exporting of minerals;  government actions, including without limitation the establishment or expansion of mineral withdrawals, parks and monuments; land exchanges; foreign exchange; employment; worker safety; transportation; and environmental protection.
- Our results of operations are significantly affected by the market prices of uranium, vanadium, rare earth elements and heavy mineral sands, which are cyclical and subject to substantial price fluctuations.


### Item 7 — MD&A (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, regulation, guidance, revenue, margin, supply chain, segment, product, market, operations, subsidiary

- AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERATIONS.
- The purpose of this Item 7 is: (i) to provide material relevant to an assessment of the financial condition and results of operations of Energy Fuels Inc., including an evaluation of the amounts and certainty of cash flows from operations and from outside information sources; and (ii) to focus specifically on  material events and uncertainties known to management that are reasonably likely to cause reported financial information not necessarily indicative of future operating results or of future financial condition.
- This Discussion and Analysis contains forward-looking statements that involve risks, uncertainties, and assumptions.
- Risk Factors and elsewhere in this Annual Report.
- energy security and advanced technologies, including uranium, vanadium, REEs and HMS, strengthening domestic supply chains and reducing reliance on foreign sources.
- The Company’s White Mesa Mill, near  Blanding, Utah, is the only licensed and operating uranium mill, and the only uranium mill capable of producing separated REE products, in the U.S.
- The titanium and zirconium products derived from our HMS production are used in national security and other key industries.
- The Company has secured its own sources of REE- and uranium-bearing monazite sands in furtherance of a fully integrated U.S.-based REE supply chain.


## Research loop (think → act)

1. _heuristic_ — Coverage looks adequate for this pass; stopping iterative loop.

## Sources

- **[S1]** UUUU fundamentals (yfinance)
  - Energy Fuels Inc: price=12.35, rev=65922000.0, fcf=-141273000.0, shares=249919146.0, rev_cagr=0.7399355982144395, ROIC=-0.07845383396530209, FCF yield=-0.045771237745452775
- **[S2]** UUUU EV/EBITDA valuation (multiples)
  - Base implied price=29.565754037907926, multiple=8.0
- **[S3]** UUUU DCF valuation (dcf)
  - Base share price=-2.319282330772069, bull=-1.8467855109534992, bear=-2.4323007189325736
- **[S4]** UUUU peer comps (peers)
  - Peers: XOM, CVX, COP, SLB, EOG; rows=6
- **[S5]** UUUU earnings history (earnings)
  - rows=12; next=2026-08-06
- **[S6]** Energy Fuels (UUUU) Stock Forecast and Price Target 2026 (web) — https://www.marketbeat.com/stocks/NYSEAMERICAN/UUUU/forecast/
  - UUUU's current price target is $23.25. Learn why top analysts are making this stock forecast for Energy Fuels at MarketBeat.
- **[S7]** UUUU Price Target: $22 (+87%) | 9 Analyst Ratings 2026 (web) — https://vcpscanner.com/stock/uuuu/price-target
  - Energy Fuels Inc. (UUUU) has a $22 consensus price target from 9 analysts (Buy). View upside analysis, rating distribution & peer comparison.
- **[S8]** What is the current Price Target and Forecast for Energy Fuels (UUUU) (web) — https://www.zacks.com/stock/research/UUUU/price-target-stock-forecast
  - Price Target Based on short-term price targets offered by five analysts, the average price target for Energy Fuels comes to $25.69. The forecasts range from a low of $16.00 to a…
- **[S9]** Energy Fuels (UUUU) Stock Forecast & Analyst Price Targets (web) — https://stockanalysis.com/stocks/uuuu/forecast/
  - Stock forecasts and analyst price target predictions for Energy Fuels Inc. (UUUU) stock, with detailed revenue and earnings estimates.
- **[S10]** Is Energy Fuels Inc. (UUUU) Stock Still a Long-Term Opportunity After Analyst Price Target Cut? (web) — https://finance.yahoo.com/energy/articles/energy-fuels-inc-uuuu-stock-200741850.html
  - We recently compiled a list of the 8 Best Rare Earth Stocks to Buy in 2026. Energy Fuels Inc. (NYSEAMERICAN:UUUU) is among the best rare earth stocks on this list. TheFly report…
- **[S11]** Roth MKM Reaffirms Their Hold Rating on Energy Fuels (UUUU) (web) — https://www.theglobeandmail.com/investing/markets/stocks/UUUU/pressreleases/14495/roth-mkm-reaffirms-their-hold-rating-on-energy-fuels-uuuu/
  - Detailed price information for Energy Fuels Inc (UUUU-A) from The Globe and Mail including charting and trades.
- **[S12]** Roth MKM Remains a Hold on Energy Fuels (UUUU) (web) — https://www.theglobeandmail.com/investing/markets/stocks/UUUU-A/pressreleases/2604873/roth-mkm-remains-a-hold-on-energy-fuels-uuuu/
  - Detailed price information for Energy Fuels Inc (UUUU-A) from The Globe and Mail including charting and trades.
- **[S13]** Wall Street bulls look optimistic about Energy Fuels (UUUU): Should you buy? (web) — https://www.msn.com/en-us/money/top-stocks/wall-street-bulls-look-optimistic-about-energy-fuels-uuuu-should-you-buy/ar-AA27uqQa?ocid=BingNewsVerp
  - Investors often turn to recommendations made by Wall Street analysts before making a Buy, Sell, or Hold decision about a ...
- **[S14]** Energy Fuels (UUUU) Stock Forecast and Price Target 2026 (web_page) — https://www.marketbeat.com/stocks/NYSEAMERICAN/UUUU/forecast/
  - Energy Fuels (UUUU) Stock Forecast and Price Target 2026 Skip to main content → ALERT: Drop these 5 stocks before the market opens tomorrow! (From Weiss Ratings) (Ad) Free UUUU …
- **[S15]** UUUU Price Target: $22 (+87%) | 9 Analyst Ratings 2026 | VCP Scanner (web_page) — https://vcpscanner.com/stock/uuuu/price-target
  - UUUU Price Target: $22 (+87%) | 9 Analyst Ratings 2026 | VCP Scanner ← Back to Screener Energy Fuels Inc. ( UUUU ) Price Target Analysis Updated Jul 17, 2026 Analyst Rating: Buy…
- **[S16]** What is the current Price Target and Forecast for Energy Fuels (UUUU) (web_page) — https://www.zacks.com/stock/research/UUUU/price-target-stock-forecast
  - Pardon Our Interruption As you were browsing something about your browser made us think you were a bot. There are a few reasons this might happen: You're a power user moving thr…
- **[S17]** Energy Fuels (UUUU) Institutional Ownership 2026 (web) — https://www.marketbeat.com/stocks/NYSEAMERICAN/UUUU/institutional-ownership/
  - View UUUU institutional ownership (13F) transactions at MarketBeat.Institutional investors have sold a total of 30,298,766 shares in the last 24 months. This volume of shares so…
- **[S18]** Energy Fuels Inc Ordinary Shares (Canada) (UUUU) Institutional... (web) — https://www.nasdaq.com/market-activity/stocks/uuuu/institutional-holdings
  - About Institutional Holdings. Nasdaq provides the ownership stake information in a company, including the number of shares held by those institutions in a firm, along with recen…
- **[S19]** Deep Dive Dubai: Scuba Diving, Freediving, & Snorkelling (web) — https://www.deepdivedubai.com/
  - Explore Deep Dive Dubai, the world’s deepest pool for scuba diving, freediving, and snorkelling in the UAE.
- **[S20]** Scenarios (web) — https://www.scenario.blondinka.org/
  - Список сценариев. Развлечение госпожи Марии от пользователя Blondinka. 12 заданий Госпожей от пользователя Blondinka. Начальная тренировка членососки от пользователя Mistress_Ta…
- **[S21]** Energy Fuels Inc. (UUUU) Stock Price, News, Quote & History ... (web) — https://finance.yahoo.com/quote/UUUU/?fr=sycsrp_catchall
  - Find the latest Energy Fuels Inc. (UUUU) stock quote, history, news and other vital information to help you with your stock trading and investing.
- **[S22]** Energy Fuels (UUUU) Stock Forecast & Analyst Price Targets (web) — https://stockanalysis.com/stocks/uuuu/forecast/
  - Stock forecasts and analyst price target predictions for Energy Fuels Inc. (UUUU) stock, with detailed revenue and earnings estimates.
- **[S23]** Energy Fuels (UUUU) Stock Price & OverviewEnergy Fuels' U.S. Rare Earth Processing Expansion Boasts ...Energy Fuels Inc. (UUUU) Analyst Insights, Price Targets ...UUUU News Today | Why did Energy Fuels stock go up today?Energy Fuels: More Upside For UUUU Stock After 2x Gains? - Forbes (web) — https://stockanalysis.com/stocks/uuuu/
  - A detailed overview of Energy Fuels Inc. (UUUU) stock, including real-time price, chart, key statistics, news, and more. Jan 15, 2026 · A redacted copy of the BFS can be found h…
- **[S24]** Energy Fuels' U.S. Rare Earth Processing Expansion Boasts ... (web) — https://investors.energyfuels.com/2026-01-15-Energy-Fuels-U-S-Rare-Earth-Processing-Expansion-Boasts-Lower-Than-Expected-CAPEX,-Significant-Annual-EBITDA,-and-Among-the-Lowest-Cost-NdPr-Production-in-the-World
  - Jan 15, 2026 · A redacted copy of the BFS can be found here. "Energy Fuels is on the cusp of solving America's rare earth processing 'bottleneck'," stated Mark S. Chalmers, CEO …
- **[S25]** Energy Fuels (UUUU) Institutional Ownership 2026 (web_page) — https://www.marketbeat.com/stocks/NYSEAMERICAN/UUUU/institutional-ownership/
  - Energy Fuels (UUUU) Institutional Ownership 2026 Skip to main content → Buy this stock today (From Chaikin Analytics) (Ad) Free UUUU Stock Alerts Energy Fuels (UUUU) Institution…
- **[S26]** Deep Dive Dubai: Scuba Diving, Freediving, & Snorkelling (web_page) — https://www.deepdivedubai.com/
  - Deep Dive Dubai: Scuba Diving, Freediving, & Snorkelling BOOK NOW  We’re closed every Monday to keep the world’s deepest pool at its very best. See you from Tuesday onwards. Di…
- **[S27]** UUUU 10-K (sec)
  - Item 1 chars=80000, Item 1A chars=50000, Item 7 chars=50000, ok=True, source=cache
- **[S28]** UUUU 8-K 2026-07-14 (sec) — https://www.sec.gov/Archives/edgar/data/1385849/000106299326003630/form8k.htm
  - FORM 8-K
- **[S29]** UUUU 8-K 2026-06-26 (sec) — https://www.sec.gov/Archives/edgar/data/1385849/000106299326003385/form8k.htm
  - FORM 8-K
- **[S30]** UUUU 8-K 2026-06-23 (sec) — https://www.sec.gov/Archives/edgar/data/1385849/000106299326003317/form8k.htm
  - FORM 8-K
- **[S31]** UUUU 8-K 2026-05-15 (sec) — https://www.sec.gov/Archives/edgar/data/1385849/000106299326002713/form8k.htm
  - FORM 8-K
- **[S32]** UUUU 10-Q 2026-05-06 (sec) — https://www.sec.gov/Archives/edgar/data/1385849/000138584926000021/efr-20260331.htm
  - 10-Q
- **[S33]** UUUU 8-K 2026-04-17 (sec) — https://www.sec.gov/Archives/edgar/data/1385849/000106299326002047/form8k.htm
  - FORM 8-K
- **[S34]** UUUU 8-K 2026-03-18 (sec) — https://www.sec.gov/Archives/edgar/data/1385849/000106299326001527/form8k.htm
  - FORM 8-K
- **[S35]** UUUU 8-K 2026-03-03 (sec) — https://www.sec.gov/Archives/edgar/data/1385849/000106299326001257/form8k.htm
  - FORM 8-K
- **[S36]** Item 1 Business summary (nlp)
  - ### Item 1 — Business (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, guidance, revenue, margin, supply chain, customer, segment, product, market…
- **[S37]** Item 1A summary (nlp)
  - ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, supply chain, interest rate, cust…
- **[S38]** Item 7 summary (nlp)
  - ### Item 7 — MD&A (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, regulation, guidance, revenue, margin, supply chain, segment, product, market, operations, s…
- **[S39]** UUUU scenario price ranges (scenarios)
  - ok=True; base mid=28.285339931499287; headwinds=8; tailwinds=6
- **[S40]** UUUU driver analysis (drivers)
  - ok=True; drivers=7
- **[S41]** UUUU memo sections (memo)
  - mode=rules; proxies=3

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

# UUUU — Planned Research Report

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
- Company: Energy Fuels Inc
- Sector / industry: Energy / Uranium
- Price: 12.35
- 52-week range: $8.16 – $27.90
- Market cap: $3.09B
- Enterprise value: $2.70B
- Shares outstanding: 249.92M
- Beta: 1.583
- Book equity: $678.40M
- Revenue (latest): $65.92M
- EBITDA (latest): -$95.72M
- Free cash flow (latest): -$141.27M
- Operating income: -$101.16M
- Operating margin: -153.4%
- EV / EBITDA: -28.3x
- ROIC: -7.8%
- FCF yield: -4.6%
- Debt / Equity: 0.9959950177254
- FCF / share: -$0.57
- Revenue / share: $0.26

### Capital structure
- Cash: $64.74M
- Short-term debt: —
- Long-term debt: $675.69M
- Total debt: $675.69M
- Net debt: $610.95M
- Net debt / EBITDA: -6.4x

### Growth
- Revenue CAGR: 74.0%
- FCF CAGR: —
- Latest revenue YoY: -15.6%
- Latest FCF YoY: -88.4%

### Market expectations (yfinance, sparse)
- Mean target: $26.12
- Target range: $16.00 – $32.50
- Recommendation: strong_buy

_Consensus revenue/EBITDA forecasts are often unavailable via free feeds; treat targets as point-in-time only._

### Historical KPIs (multi-year)

| Year | Revenue | OCF | Capex | FCF | EBITDA | LT debt | Cash | Net debt | Net income |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2025 | $65.92M | -$89.48M | $51.79M | -$141.27M | -$95.72M | $675.69M | $64.74M | $610.95M | -$85.63M |
| 2024 | $78.11M | -$43.97M | $31.02M | -$75.00M | -$34.05M | — | $38.60M | -$38.60M | -$47.77M |
| 2023 | $37.93M | -$15.41M | $44.71M | -$60.12M | -$29.62M | — | $57.45M | -$57.45M | $99.86M |
| 2022 | $12.52M | -$49.70M | $2.00M | -$51.70M | -$56.51M | — | $62.82M | -$62.82M | -$59.85M |

## Charts

### Revenue & FCF history
![Revenue & FCF history](/charts/UUUU_valuation_revenue_fcf.png)

### DCF scenario prices
![DCF scenario prices](/charts/UUUU_valuation_dcf_scenarios.png)

### Base-case FCF path
![Base-case FCF path](/charts/UUUU_valuation_base_fcf_path.png)

### EV/EBITDA scenario prices
![EV/EBITDA scenario prices](/charts/UUUU_valuation_ev_ebitda_scenarios.png)

### Headwind/tailwind price ranges
![Headwind/tailwind price ranges](/charts/UUUU_valuation_scenario_ranges.png)

## DCF valuation (base / bull / bear) [S2]

> Simplified revenue->FCF DCF. Not investment advice; assumptions are editable heuristics.

- Spot price: $12.35
- Base revenue: $65.92M
- Shares: 249,919,146
- Net debt (Debt−Cash): $610.95M

| Scenario | Growth | FCF margin | WACC | Term. g | Equity value | Share price | Upside |
|----------|--------|------------|------|---------|--------------|-------------|--------|
| bear | -15.6% | 1.0% | 12.0% | 1.5% | -$607.88M | $-2.43 | -119.7% |
| base | 6.0% | 3.0% | 10.0% | 2.5% | -$579.63M | $-2.32 | -118.8% |
| bull | 15.0% | 8.0% | 9.0% | 3.0% | -$461.55M | $-1.85 | -115.0% |

### Assumption notes
- Base revenue growth seeded from historical rate (-15.6%).
- Recent revenue declined (-15.6% YoY); base/bull use normalized mid-cycle growth instead of extrapolating the decline.
- Latest FCF margin was -214.3%; scenarios use normalized positive margins for a going-concern DCF.

- _base: model equity value is negative after net debt (-579,633,059); showing $-2.32/sh._
- _bull: model equity value is negative after net debt (-461,547,058); showing $-1.85/sh._
- _bear: model equity value is negative after net debt (-607,878,518); showing $-2.43/sh._

### Base-case projected FCF

- Year 1: revenue $69.88M, FCF $2.10M (PV $1.91M)
- Year 2: revenue $74.07M, FCF $2.22M (PV $1.84M)
- Year 3: revenue $78.51M, FCF $2.36M (PV $1.77M)
- Year 4: revenue $83.23M, FCF $2.50M (PV $1.71M)
- Year 5: revenue $88.22M, FCF $2.65M (PV $1.64M)
- Terminal value $36.17M (PV $22.46M)

## Valuation — EV/EBITDA scenarios [S3]

> Priced-in model: implied price = (EBITDA × EV/EBITDA − net debt) ÷ shares. Not a forecast.

- Spot: $12.35
- Net debt used: $610.95M

| Scenario | EBITDA | EV/EBITDA | Implied EV | Equity value | Implied price |
|---|---:|---:|---:|---:|---:|
| bear | $700.00M | 6.0x | $4.20B | $3.59B | $14.36 |
| base | $1.00B | 8.0x | $8.00B | $7.39B | $29.57 |
| bull | $1.20B | 10.0x | $12.00B | $11.39B | $45.57 |

- EBITDA missing or non-positive; scenarios use placeholder $1B EBITDA — edit before relying on prices.
- No current EV/EBITDA; defaulted base multiple to 8.0x.

## Scenario price ranges (headwinds & tailwinds) [S28]

> Medium-term (18–36 months (medium / medium-long term)) driver → EV/EBITDA bridge. Distinct from the FCF DCF path. Not investment advice.

- Spot: $12.35
- Sparse Street mean target: $26.12
- Anchor multiple: 8.0x (driver_ev_ebitda_bridge)
- Anchor EBITDA: $1.00B
- Probability-weighted midpoint: **$29.34** (heuristic weights, not a rating)
- Driver extraction: `rules`

### Headwinds (bear-case fuel)

- **Negative free cash flow** — Latest FCF -$141.27M — cash burn raises financing risk _(source: fundamentals)_
- **Revenue contraction** — Latest revenue YoY ≈ -15.6% _(source: fundamentals)_
- **Balance-sheet / refinancing pressure** — sector=Energy industry=Uranium revenue=65922000.0 ebitda=-95724000.0 fcf=-141273000.0 net_debt=610952000.0 nd_ebitda=-6.382432827713008 target=26.125 rec=strong_buy _(source: fundamentals)_
- **Regulatory / legal risk** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, supply chain, interest rate, custome _(source: item_1a)_
- **Competitive / pricing pressure** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, supply chain, interest rate, custome _(source: item_1a)_
- **Margin / cost headwind** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, supply chain, interest rate, custome _(source: item_1a)_
- **Operational / cyber risk** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, supply chain, interest rate, custome _(source: item_1a)_

### Tailwinds (bull-case fuel)

- **Manageable leverage** — Net debt / EBITDA ≈ -6.4x — room for reinvestment or returns _(source: fundamentals)_
- **Street target implies upside** — Mean target $26.12 vs spot $12.35 _(source: fundamentals)_
- **Growth / execution upside** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, supply chain, interest rate, custome _(source: item_1a)_
- **Product / pricing power** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, supply chain, interest rate, custome _(source: item_1a)_
- **Contract / backlog wins** — Energy Fuels Inc.: Target Price Consensus and Analysts Recommendations | EFR | CA2926717083 | MarketScreener This composite rating is the result of an average of the rankings based _(source: web)_
- **Multiple re-rating / Street upgrades** — UUUU / Energy Fuels Inc. (NYSEAM) - Forecast, Price Target, Estimates, Predictions We provide the high, low, average, and median values for the stock. ... Line chart with 4 lines.  _(source: web)_
- **Capital returns / FCF inflection** — UUUU Intrinsic Valuation and Fundamental Analysis - Energy Fuels Inc - Alpha Spread UUUU Intrinsic Valuation and Fundamental Analysis - Energy Fuels Inc - Alpha Spread Alpha Spread _(source: web_page)_

### Price ranges by case

| Case | Prob. | Metric vs TTM | Multiple | Price low | Mid | High | Upside vs spot |
|---|---:|---:|---:|---:|---:|---:|---:|
| bear | 0.26 | 0.70x | 5.0x | $10.06 | $11.45 | $12.84 | -7% |
| base | 0.47 | 1.00x | 8.0x | $27.33 | $29.57 | $31.81 | +139% |
| bull | 0.26 | 1.23x | 10.2x | $42.91 | $47.95 | $52.99 | +288% |

#### Bear — headwinds dominate

Headwinds bite: weaker operating trajectory and multiple compression. Equity duration shrinks if cash generation fails to offset leverage / competitive pressure.

- **Range:** $10.06 – $12.84 (mid $11.45) · EBITDA $700.00M · multiple 5.0x
- Driver: **Negative free cash flow** — Latest FCF -$141.27M — cash burn raises financing risk
- Driver: **Revenue contraction** — Latest revenue YoY ≈ -15.6%
- Driver: **Balance-sheet / refinancing pressure** — sector=Energy industry=Uranium revenue=65922000.0 ebitda=-95724000.0 fcf=-141273000.0 net_debt=610952000.0 nd_ebitda=-6.382432827713008 target=26.125 rec=strong
- Driver: **Regulatory / legal risk** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, supply chain, in
- Driver: **Competitive / pricing pressure** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, supply chain, in

#### Base — mixed execution

Balanced path: some tailwinds offset headwinds. Operating scale roughly holds with modest repair/normalization; valuation stays near the current EV/EBITDA anchor.

- **Range:** $27.33 – $31.81 (mid $29.57) · EBITDA $1.00B · multiple 8.0x
- Driver: **Manageable leverage** — Net debt / EBITDA ≈ -6.4x — room for reinvestment or returns
- Driver: **Street target implies upside** — Mean target $26.12 vs spot $12.35
- Driver: **Negative free cash flow** — Latest FCF -$141.27M — cash burn raises financing risk
- Driver: **Revenue contraction** — Latest revenue YoY ≈ -15.6%

#### Bull — tailwinds dominate

Tailwinds compound: operating improvement plus a re-rating toward peer or recovery multiples as balance-sheet and growth narratives improve.

- **Range:** $42.91 – $52.99 (mid $47.95) · EBITDA $1.23B · multiple 10.2x
- Driver: **Manageable leverage** — Net debt / EBITDA ≈ -6.4x — room for reinvestment or returns
- Driver: **Street target implies upside** — Mean target $26.12 vs spot $12.35
- Driver: **Growth / execution upside** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, supply chain, in
- Driver: **Product / pricing power** — ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, supply chain, in
- Driver: **Contract / backlog wins** — Energy Fuels Inc.: Target Price Consensus and Analysts Recommendations | EFR | CA2926717083 | MarketScreener This composite rating is the result of an average o

### Method notes

- Item 1A risks weighted toward headwinds.
- Current ev_ebitda multiple missing; anchored at 8.0x.
- Mapping follows Gemini/Perplexity-style scenario memos: qualitative drivers → operating metric & multiple paths → share-price ranges over a medium-term horizon.

## Web research — web_analysts

- Queries: UUUU analyst price target, Energy Fuels Inc stock rating OR consensus OR upgrade OR downgrade, UUUU Estimate intrinsic value under base / bull / bear scenarios analyst
- Unique hits: 20
- Pages fetched: 3/3

### Web synthesis — web_analysts (rule-based fallback — Ollama unavailable)
**Keyword hits:** guidance, revenue, customer, product, service, market

- [HIT] Energy Fuels (UUUU) Stock Forecast and Price Target 2026 | www.marketbeat.com | https://www.marketbeat.com/stocks/NYSEAMERICAN/UUUU/forecast/ UUUU's current price target is $23.25.
- Learn why top analysts are making this stock forecast for Energy Fuels at MarketBeat.
- (UUUU) stock, with detailed revenue and earnings estimates.
- [HIT] Roth MKM Reaffirms Their Hold Rating on Energy Fuels (UUUU) | The Globe and Mail | https://www.theglobeandmail.com/investing/markets/stocks/UUUU-A/pressreleases/14495/roth-mkm-reaffirms-their-hold-rating-on-energy-fuels-uuuu/ Detailed price information for Energy Fuels Inc (UUUU-A) from The Globe and Mail including charting and trades.
- [HIT] Roth MKM Remains a Hold on Energy Fuels (UUUU) | The Globe and Mail | https://www.theglobeandmail.com/investing/markets/stocks/UUUU-A/pressreleases/2604873/roth-mkm-remains-a-hold-on-energy-fuels-uuuu/ Detailed price information for Energy Fuels Inc (UUUU-A) from The Globe and Mail including charting and trades.
- [HIT] Energy Fuels Inc.: Target Price Consensus and Analysts Recommendations | EFR | CA2926717083 | MarketScreener | www.marketscreener.com | https://www.marketscreener.com/quote/stock/ENERGY-FUELS-INC-1409846/consensus/ This composite rating is the result of an average of the rankings based on the following ratings: Fundamentals (Composite), Valuation (Composite), Financial Estimates Revisions (Composite), Consensus (Composite) and Visibility (Composite).
- [HIT] Energy Fuels (UUUU) Stock Forecast: Analyst Ratings, Predictions & Price Target 2026 | public.com | https://public.com/stocks/uuuu/forecast-price-target 4 analysts have given Energy Fuels (UUUU) a consensus rating of Buy while the Energy Fuels (UUUU) price prediction in 2026 is $23.12  [HIT] Tech Earnings Optimism Powers Stocks Higher | Barchart · via Yahoo Finance | https://finance.yahoo.com/markets/stocks/articles/tech-earnings-optimism-powers-stocks-203403985.html The S&P 500 Index ($SPX ) (SPY ) on Monday closed up +0.12%, the Dow Jones Industrial Average ($DOWI ) (DIA ) closed down -0.13%, and the Nasdaq 100...
- [HIT] Stocks Mixed as US Set to Blockade the Strait of Hormuz | Barchart · via Yahoo Finance | https://finance.yahoo.com/markets/stocks/articles/stocks-mixed-us-set-blockade-135719693.html The S&P 500 Index ($SPX ) (SPY ) today is up +0.05%, the Dow Jones Industrial Average ($DOWI ) (DIA...

### Sources found
- [Energy Fuels (UUUU) Stock Forecast and Price Target 2026](https://www.marketbeat.com/stocks/NYSEAMERICAN/UUUU/forecast/)
  - UUUU's current price target is $23.25. Learn why top analysts are making this stock forecast for Energy Fuels at MarketBeat.
- [What is the current Price Target and Forecast for Energy Fuels (UUUU)](https://www.zacks.com/stock/research/UUUU/price-target-stock-forecast)
  - Price Target Based on short-term price targets offered by five analysts, the average price target for Energy Fuels comes to $25.69. The forecasts range from …
- [Energy Fuels (UUUU) Stock Forecast & Analyst Price Targets](https://stockanalysis.com/stocks/uuuu/forecast/)
  - Stock forecasts and analyst price target predictions for Energy Fuels Inc. (UUUU) stock, with detailed revenue and earnings estimates.
- [UUUU Price Target: $22 (+87%) | 9 Analyst Ratings 2026](https://vcpscanner.com/stock/uuuu/price-target)
  - Energy Fuels Inc. (UUUU) has a $22 consensus price target from 9 analysts (Buy). View upside analysis, rating distribution & peer comparison.
- [Is Energy Fuels Inc. (UUUU) Stock Still a Long-Term Opportunity After Analyst Price Target Cut?](https://finance.yahoo.com/energy/articles/energy-fuels-inc-uuuu-stock-200741850.html)
  - We recently compiled a list of the 8 Best Rare Earth Stocks to Buy in 2026. Energy Fuels Inc. (NYSEAMERICAN:UUUU) is among the best rare earth stocks on this…
- [Roth MKM Reaffirms Their Hold Rating on Energy Fuels (UUUU)](https://www.theglobeandmail.com/investing/markets/stocks/UUUU-A/pressreleases/14495/roth-mkm-reaffirms-their-hold-rating-on-energy-fuels-uuuu/)
  - Detailed price information for Energy Fuels Inc (UUUU-A) from The Globe and Mail including charting and trades.
- [Roth MKM Remains a Hold on Energy Fuels (UUUU)](https://www.theglobeandmail.com/investing/markets/stocks/UUUU-A/pressreleases/2604873/roth-mkm-remains-a-hold-on-energy-fuels-uuuu/)
  - Detailed price information for Energy Fuels Inc (UUUU-A) from The Globe and Mail including charting and trades.
- [Wall Street bulls look optimistic about Energy Fuels (UUUU): Should you buy?](https://www.msn.com/en-us/money/top-stocks/wall-street-bulls-look-optimistic-about-energy-fuels-uuuu-should-you-buy/ar-AA27uqQa?ocid=BingNewsVerp)
  - Investors often turn to recommendations made by Wall Street analysts before making a Buy, Sell, or Hold decision about a ...
- [Energy Fuels Inc.: Target Price Consensus and Analysts Recommendations | EFR | CA2926717083 | MarketScreener](https://www.marketscreener.com/quote/stock/ENERGY-FUELS-INC-1409846/consensus/)
  - This composite rating is the result of an average of the rankings based on the following ratings: Fundamentals (Composite), Valuation (Composite), Financial …
- [UUUU / Energy Fuels Inc. (NYSEAM) - Forecast, Price Target, Estimates, Predictions](https://fintel.io/sfo/us/uuuu)
  - We provide the high, low, average, and median values for the stock. ... Line chart with 4 lines. ... The chart has 1 X axis displaying Date. Data ranges from…
- [Energy Fuels (UUUU) Analyst Ratings](https://stockanalysis.com/stocks/uuuu/ratings/)
  - (UUUU) NYSEAMERICAN: UUUU · Real-Time ... 8:00 PM EST · All Analysts Top Analysts · Total Analysts · 6 · Consensus Rating · Strong Buy · Price Target · $19.8…
- [Energy Fuels (UUUU) Stock Forecast: Analyst Ratings, Predictions & Price Target 2026](https://public.com/stocks/uuuu/forecast-price-target)
  - 4 analysts have given Energy Fuels (UUUU) a consensus rating of Buy while the Energy Fuels (UUUU) price prediction in 2026 is $23.12

### Search warnings
- news:UUUU Estimate intrinsic value under base / bull / bear scenarios analyst: No results found.

## Web research — web_drivers

- Queries: UUUU Estimate intrinsic value under base / bull / bear scenarios, Energy Fuels Inc UUUU outlook OR catalyst OR commodity OR uranium OR rare earth OR vanadium, UUUU sector drivers OR market demand
- Unique hits: 12
- Pages fetched: 1/3

### Web synthesis — web_drivers (rule-based fallback — Ollama unavailable)
**Keyword hits:** revenue, margin, market

- [HIT] Energy Fuels (UUUU): Is This Uranium Play Poised to Outperform the Market Amid a Resurging Nuclear Sector?
- | www.ainvest.com | https://www.ainvest.com/news/energy-fuels-uuuu-uranium-play-poised-outperform-market-resurging-nuclear-sector-2507/ July 25, 2025 - This institutional backing is critical in a market where large investors can drive liquidity and momentum, especially in a high-beta stock like UUUU.
- The broader uranium market is experiencing a perfect storm of tight supply, surging demand, and policy-driven growth.
- | finance.yahoo.com | https://finance.yahoo.com/markets/stocks/articles/uuuu-trades-premium-industry-play-171800358.html June 8, 2026 - ...
- [HIT] Energy Fuels (UUUU) | Trefis | Trefis | www.trefis.com | https://www.trefis.com/data/companies/uuuu The gross margin for uranium is projected to increase from 31% in 2025 to 50% in 2026.
- [HIT] Markets - Financial Advisors - Latest News about Energy Fuels Inc Ordinary Shares (Canada) (NYSE:UUUU) | Energy Fuels Inc Ordinary Shares (Canada) (NYSE:UUUU) News | markets.financialcontent.com | https://markets.financialcontent.com/1discountbrokerage/quote/news?CurrentPage=3&ChannelType=NEWS&Symbol=NY:UUUU The convergence of booming energy demands with severely constrained supplies positions uranium mining for substantial price increases.
- One of the biggest impacts that the threat of tariffs is creating is within the gold and silver market.
- [PAGE] UUUU Intrinsic Valuation and Fundamental Analysis - Energy Fuels Inc - Alpha Spread | https://www.alphaspread.com/security/amex/uuuu/summary UUUU Intrinsic Valuation and Fundamental Analysis - Energy Fuels Inc - Alpha Spread Alpha Spread Dashboard Tools Market News Investing Ideas Pricing Search 100,000+ stocks...

### Sources found
- [UUUU Intrinsic Valuation and Fundamental Analysis - Energy Fuels Inc - Alpha Spread](https://www.alphaspread.com/security/amex/uuuu/summary)
  - UUUU stock discount rate: cost of equity and WACC. ... The intrinsic value for Energy Fuels Inc (UUUU) under the Base Case is 4.86 USD.
- [3 Ways of Calculating a Stock's Intrinsic Value - HubPages](https://discover.hubpages.com/money/Stock-Valuation-Using-Bear-Bull-and-Base-Case-Scenarios)
  - September 12, 2024 - It's highly probable that reality ... following scenarios plotted out, you can make a valuation like so: Base case: 50% probability of $…
- [3 Ways of Calculating a Stock's Intrinsic Value - ToughNickel](https://toughnickel.com/personal-finance/Stock-Valuation-Using-Bear-Bull-and-Base-Case-Scenarios)
  - March 22, 2023 - It's highly probable that reality ... following scenarios plotted out, you can make a valuation like so: Base case: 50% probability of $150 …
- [Bull Base Bear Valuation for One Stock | Model Reef](https://modelreef.io/resources/articles/stock-valuation/how-to-create-a-bull-base-bear-valuation-for-one-stock-scenario-driven-intrinsic-value)
  - April 15, 2026 - The point of bull/base/bear is to show what must be true-not to pretend the world can be summarised in one number. If you want a quick quali…
- [Energy Fuels Inc: Investors | Uranium Stocks and Press Releases](https://investors.energyfuels.com/)
  - Articles and press releases about Uranium stocks for investors of Energy Fuels and their partners. Energy Fuels is a fully-integrated producer of both ...
- [Energy Fuels - Uranium, Rare Earths & Critical Minerals](https://www.energyfuels.com/)
  - American producer of uranium for the nuclear fuel cycle, rare earth oxides and critical minerals, operating the only U.S. conventional uranium mill.
- [Energy Fuels Announces Q1-2026 Results - PR Newswire](https://www.prnewswire.com/news-releases/energy-fuels-announces-q1-2026-results-302764727.html)
  - May 6, 2026 ... ... Energy Fuels Inc. (NYSE American: UUUU) ... Energy Fuels is a leading U.S. critical materials company specializing in uranium, rare earth…
- [Energy Fuels Inc. (UUUU) Stock Price, News, Quote & History](https://finance.yahoo.com/quote/UUUU/)
  - It produces and sells vanadium pentoxide, rare earth elements, carbonate, and heavy mineral sands, such as ilmenite, rutile, zircon, and monazite. The compan…
- [Energy Fuels (UUUU): Is This Uranium Play Poised to Outperform the Market Amid a Resurging Nuclear Sector?](https://www.ainvest.com/news/energy-fuels-uuuu-uranium-play-poised-outperform-market-resurging-nuclear-sector-2507/)
  - July 25, 2025 - This institutional backing is critical in a market where large investors can drive liquidity and momentum, especially in a high-beta stock li…
- [UUUU Trades at a Premium to the Industry: How to Play the Stock?](https://finance.yahoo.com/markets/stocks/articles/uuuu-trades-premium-industry-play-171800358.html)
  - June 8, 2026 - ... Both the estimates have undergone negative revisions in the past 60 days, as shown in the chart below. ... The company's long-term outlook…
- [Energy Fuels (UUUU) | Trefis | Trefis](https://www.trefis.com/data/companies/uuuu)
  - The gross margin for uranium is projected to increase from 31% in 2025 to 50% in 2026. Growing demand for nuclear power, particularly to fuel energy-intensiv…
- [Markets - Financial Advisors - Latest News about Energy Fuels Inc Ordinary Shares (Canada) (NYSE:UUUU) | Energy Fuels Inc Ordinary Shares (Canada) (NYSE:UUUU) News](https://markets.financialcontent.com/1discountbrokerage/quote/news?CurrentPage=3&ChannelType=NEWS&Symbol=NY:UUUU)
  - The convergence of booming energy demands with severely constrained supplies positions uranium mining for substantial price increases. ... One of the biggest…

### Search warnings
- news:UUUU Estimate intrinsic value under base / bull / bear scenarios: No results found.
- news:Energy Fuels Inc UUUU outlook OR catalyst OR commodity OR uranium OR rare earth OR vanadium: No results found.
- news:UUUU sector drivers OR market demand: No results found.

## SEC filing [S24]
- Extraction OK: True
- Item 1 chars: 80000
- Item 1A chars: 50000
- Item 7 chars: 50000
- Meta: {'source': 'cache', 'path': 'C:\\DevWork\\equity_research_agent\\data\\filings\\UUUU_10k.txt'}

## Company setup & business model

**Keyword hits:** risk, uncertainty, guidance, revenue, margin, supply chain, customer, segment, product, market, operations, subsidiary

- On August 16, 2024, the Company acquired RadTran LLC (“RadTran”), a private company specializing in the separation of critical radioisotopes, to further the Company’s plans for development  and production of medical isotopes used in cancer treatments.
- All of the Company’s U.S.-based employees are employed by its subsidiary Energy Fuels Resources (USA) Inc.
- (“EFUSA”), a wholly owned subsidiary of EF Holdings, which also serves as operator of all the Company’s U.S.
- On February 10, 2023, the Company, through its wholly owned subsidiary Energy Fuels Brazil Ltda., acquired the Bahia Project in the State of Bahia, Brazil.
- On October 2, 2024, the Company acquired Base Resources, which owned the Kwale Project, which is now in reclamation, and the Vara Mada Project in Madagascar, which is currently in permitting and development, thereby further increasing its portfolio of HMS/monazite/REE projects to support a U.S.-controlled REE supply chain.
- The primary trading market for Energy Fuels’ Common Shares is the NYSE American under the trading symbol “ UUUU,” and the Company’s Common Shares are also listed on the TSX under the trading symbol “EFR.” Energy Fuels is a U.S.
- The Designated Primary Market Maker for the Options is Group One Trading, LP.
- Citadel Securities is the Company’s Market Maker on the NYSE American.
- Table of Conten t s  Business Overview  Energy Fuels produces several of the critical minerals essential to the United States (“U.S.”), energy security and other advanced technologies, including uranium, vanadium, REEs (including NdPr, Dy and Tb) and HMS (including titanium and zirconium minerals), in an effort to strengthen domestic supply chains and reduce reliance on foreign-controlled sources.
- due to its notable ability to process uranium, vanadium, REE products, and, potentially, radioisotopes for medical applications.
- We produce vanadium as a co-product from certain of our uranium mines, as market conditions  warrant.
- The REE products we produce are essential to manufacture permanent magnets for traction motors in electric  vehicles (“EVs”), hybrid EVs, defense systems, robotics and other advanced technologies.
- The titanium and zirconium products derived from our HMS products are used in national security and other key industries.
- In processing Alternate Feed Materials, the Mill also helps reduce the quantity of  industry materials permanently disposed of and, by extension, the overall tailings footprint of mining and milling operations.
- controlled REE supply chain, which include:  • the Vara Mada Project acquired through the Company’s 100% acquisition of Base Resources on October 2, 2024, see Part I, Item 2.
- Upon closing of this transaction, which is expected as  early as June 2026, the Company believes it will be the largest, fully integrated REE “mine-to-metal and alloy” producer outside of China closing a critical strategic gap in global supply chains for magnet applications, including automotive, robotic, energy and defense technologies.
- Segment Information  We have three reportable segments based on our operations and the financial information regularly reviewed by our Chief Operating Decision Maker (“ CODM”): (i) uranium, (ii) REE, and (iii) HMS.
- The uranium segment engages in conventional and ISR uranium extraction, recovery and sales of uranium from mineral properties and the recycling of uranium-bearing materials generated by third parties (Alternate Feed Materials) along with the exploration, permitting and evaluation of uranium properties in the U.S.
- The Company’s final uranium product is natural uranium concentrate, or U3 O8, which is sold to customers for further processing into fuel for nuclear reactors.
- The Company also produces vanadium pentoxide, V2 O5, as a co-product of uranium at the Mill within the uranium segment.
- In addition,  Table of Conten t s  within the uranium segment, the Company is exploring opportunities to separate radium-226 (“Ra-226”) and radium-228 (“Ra-228”) as a byproduct of its existing uranium and REE process streams for potential use in the production of medical isotopes for emerging TAT cancer treatments.
- The REE segment is engaged in the Company’s initiatives to progress towards full REE separation capabilities at the Mill to produce both “light” and “heavy” separated REE oxides.
- The Company has the current capacity to produce separated REE products in  its Phase 1 Circuit.
- The Company is planning further enhancements to expand its heavy REE production at its Phase 1 Circuit for the planned recovery of dysprosium (“Dy”), terbium (“Tb”), samarium (“Sm”), europium (“Eu”) and gadolinium (“Gd”), with the ability to separate other heavy REEs such as yttrium (“Y”) and lutetium (“Lu”) if market conditions warrant, subject to the receipt of regulatory approvals, financing, completion of engineering and the receipt of sufficient feed materials.
- The  Company also plans to expand its NdPr, Dy and Tb production recovery and potentially other REE material production recovery in the future, subject to the receipt of regulatory approvals, completion of engineering, financing and the receipt of sufficient feed materials, through the development of its proposed stand-alone phase 2 REE production circuit (the “Phase 2 Circuit”) with a total planned production recovery (from the Phase 1 Circuit and Phase 2 Circuit) of up to approximately 6,000 tonnes of NdPr, 200 tonnes of Dy and 60 tonnes of Tb per year, along with other REEs, described in more detail below, from monazite concentrates, mixed rare earth carbonates (“MREC”) or similar feed materials.
- The monazite feedstock for the Company’s REE production is expected to be procured through Company-owned mines like the Vara Mada Project and Bahia Project, as well as its joint venture interest in the Donald Project, along with other potential acquisitions, joint ventures, open market offtake,  and/or other collaborations, in each case upon successful completion of development of the projects and transactions.
- The HMS segment engages in the exploration and development, and planned recovery, of HMS at the Vara Mada Project, Bahia Project and through the Company’s investment in the Donald Project JV.
- The HMS segment also includes the Kwale Project, which ceased mine operations on December 31, 2024 and is now in reclamation.

_Source: latest 10-K Item 1 (Business), summarized locally._

## Qualitative analysis (local LLM)

### Item 1 — Business (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, uncertainty, guidance, revenue, margin, supply chain, customer, segment, product, market, operations, subsidiary

- On August 16, 2024, the Company acquired RadTran LLC (“RadTran”), a private company specializing in the separation of critical radioisotopes, to further the Company’s plans for development  and production of medical isotopes used in cancer treatments.
- All of the Company’s U.S.-based employees are employed by its subsidiary Energy Fuels Resources (USA) Inc.
- (“EFUSA”), a wholly owned subsidiary of EF Holdings, which also serves as operator of all the Company’s U.S.
- On February 10, 2023, the Company, through its wholly owned subsidiary Energy Fuels Brazil Ltda., acquired the Bahia Project in the State of Bahia, Brazil.
- On October 2, 2024, the Company acquired Base Resources, which owned the Kwale Project, which is now in reclamation, and the Vara Mada Project in Madagascar, which is currently in permitting and development, thereby further increasing its portfolio of HMS/monazite/REE projects to support a U.S.-controlled REE supply chain.
- The primary trading market for Energy Fuels’ Common Shares is the NYSE American under the trading symbol “ UUUU,” and the Company’s Common Shares are also listed on the TSX under the trading symbol “EFR.” Energy Fuels is a U.S.
- The Designated Primary Market Maker for the Options is Group One Trading, LP.
- Citadel Securities is the Company’s Market Maker on the NYSE American.
- Table of Conten t s  Business Overview  Energy Fuels produces several of the critical minerals essential to the United States (“U.S.”), energy security and other advanced technologies, including uranium, vanadium, REEs (including NdPr, Dy and Tb) and HMS (including titanium and zirconium minerals), in an effort to strengthen domestic supply chains and reduce reliance on foreign-controlled sources.
- due to its notable ability to process uranium, vanadium, REE products, and, potentially, radioisotopes for medical applications.
- We produce vanadium as a co-product from certain of our uranium mines, as market conditions  warrant.
- The REE products we produce are essential to manufacture permanent magnets for traction motors in electric  vehicles (“EVs”), hybrid EVs, defense systems, robotics and other advanced technologies.
- The titanium and zirconium products derived from our HMS products are used in national security and other key industries.
- In processing Alternate Feed Materials, the Mill also helps reduce the quantity of  industry materials permanently disposed of and, by extension, the overall tailings footprint of mining and milling operations.
- controlled REE supply chain, which include:  • the Vara Mada Project acquired through the Company’s 100% acquisition of Base Resources on October 2, 2024, see Part I, Item 2.
- Upon closing of this transaction, which is expected as  early as June 2026, the Company believes it will be the largest, fully integrated REE “mine-to-metal and alloy” producer outside of China closing a critical strategic gap in global supply chains for magnet applications, including automotive, robotic, energy and defense technologies.
- Segment Information  We have three reportable segments based on our operations and the financial information regularly reviewed by our Chief Operating Decision Maker (“ CODM”): (i) uranium, (ii) REE, and (iii) HMS.
- The uranium segment engages in conventional and ISR uranium extraction, recovery and sales of uranium from mineral properties and the recycling of uranium-bearing materials generated by third parties (Alternate Feed Materials) along with the exploration, permitting and evaluation of uranium properties in the U.S.
- The Company’s final uranium product is natural uranium concentrate, or U3 O8, which is sold to customers for further processing into fuel for nuclear reactors.
- The Company also produces vanadium pentoxide, V2 O5, as a co-product of uranium at the Mill within the uranium segment.
- In addition,  Table of Conten t s  within the uranium segment, the Company is exploring opportunities to separate radium-226 (“Ra-226”) and radium-228 (“Ra-228”) as a byproduct of its existing uranium and REE process streams for potential use in the production of medical isotopes for emerging TAT cancer treatments.
- The REE segment is engaged in the Company’s initiatives to progress towards full REE separation capabilities at the Mill to produce both “light” and “heavy” separated REE oxides.
- The Company has the current capacity to produce separated REE products in  its Phase 1 Circuit.
- The Company is planning further enhancements to expand its heavy REE production at its Phase 1 Circuit for the planned recovery of dysprosium (“Dy”), terbium (“Tb”), samarium (“Sm”), europium (“Eu”) and gadolinium (“Gd”), with the ability to separate other heavy REEs such as yttrium (“Y”) and lutetium (“Lu”) if market conditions warrant, subject to the receipt of regulatory approvals, financing, completion of engineering and the receipt of sufficient feed materials.
- The  Company also plans to expand its NdPr, Dy and Tb production recovery and potentially other REE material production recovery in the future, subject to the receipt of regulatory approvals, completion of engineering, financing and the receipt of sufficient feed materials, through the development of its proposed stand-alone phase 2 REE production circuit (the “Phase 2 Circuit”) with a total planned production recovery (from the Phase 1 Circuit and Phase 2 Circuit) of up to approximately 6,000 tonnes of NdPr, 200 tonnes of Dy and 60 tonnes of Tb per year, along with other REEs, described in more detail below, from monazite concentrates, mixed rare earth carbonates (“MREC”) or similar feed materials.
- The monazite feedstock for the Company’s REE production is expected to be procured through Company-owned mines like the Vara Mada Project and Bahia Project, as well as its joint venture interest in the Donald Project, along with other potential acquisitions, joint ventures, open market offtake,  and/or other collaborations, in each case upon successful completion of development of the projects and transactions.
- The HMS segment engages in the exploration and development, and planned recovery, of HMS at the Vara Mada Project, Bahia Project and through the Company’s investment in the Donald Project JV.
- The HMS segment also includes the Kwale Project, which ceased mine operations on December 31, 2024 and is now in reclamation.


### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, uncertainty, litigation, regulation, competition, supply chain, interest rate, customer, product, service, market, operations

- Other factors may arise in the future that are currently not foreseen by management of Energy Fuels that may present additional risks, including risks that the Company currently feels are immaterial.
- Current and prospective shareholders of Energy Fuels should carefully consider these risk factors when making investment decisions.
- Our failure to successfully address any of the risks and uncertainties described below could have a material adverse effect on our business, financial condition and/or results of operations, and the trading price of our Common Shares may fluctuate widely.
- We cannot assure you that we have or will successfully or fully address these risks or other unknown risks that may affect our business.
- Risks Related to our Industry  We are subject to the risks normally encountered by companies in the mineral extraction industry.
- We are subject to the risks normally encountered by companies in the mineral extraction industry, such as:  • the discovery of unusual or unexpected geological formations, and variations in ore radiation levels;  • wild/bushfires, floods, earthquakes, tornados, tropical cyclones, droughts, landslides and other natural disasters;  • accidental fires, unplanned power outages and water shortages;  • controlling water, emissions and other similar mining hazards;  • operating labor disruptions and labor disputes;  • the ability to obtain and maintain suitable or adequate machinery, equipment or labor;  • our liability for potential or existing pollution or other hazards; and  • other known and unknown risks involved in the conduct of exploration, development and operation of mines, E&R facilities and mills, and metals and alloys plants (pending the successful acquisition of ASM), along with the markets for uranium, rare earths, vanadium, HMS and metals and alloys.
- The development of mineral properties is affected by many factors, including, but not limited to: the cost of operations; variations in the grade of mineralized material; fluctuations in metal markets; costs of extraction and processing equipment; availability of equipment and labor; labor costs and possible labor strikes; government regulations, including without limitation, regulations relating to taxes, royalties, allowable extraction or production, and importing and exporting of minerals;  government actions, including without limitation the establishment or expansion of mineral withdrawals, parks and monuments; land exchanges; foreign exchange; employment; worker safety; transportation; and environmental protection.
- Our results of operations are significantly affected by the market prices of uranium, vanadium, rare earth elements and heavy mineral sands, which are cyclical and subject to substantial price fluctuations.


### Item 7 — MD&A (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, regulation, guidance, revenue, margin, supply chain, segment, product, market, operations, subsidiary

- AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERATIONS.
- The purpose of this Item 7 is: (i) to provide material relevant to an assessment of the financial condition and results of operations of Energy Fuels Inc., including an evaluation of the amounts and certainty of cash flows from operations and from outside information sources; and (ii) to focus specifically on  material events and uncertainties known to management that are reasonably likely to cause reported financial information not necessarily indicative of future operating results or of future financial condition.
- This Discussion and Analysis contains forward-looking statements that involve risks, uncertainties, and assumptions.
- Risk Factors and elsewhere in this Annual Report.
- energy security and advanced technologies, including uranium, vanadium, REEs and HMS, strengthening domestic supply chains and reducing reliance on foreign sources.
- The Company’s White Mesa Mill, near  Blanding, Utah, is the only licensed and operating uranium mill, and the only uranium mill capable of producing separated REE products, in the U.S.
- The titanium and zirconium products derived from our HMS production are used in national security and other key industries.
- The Company has secured its own sources of REE- and uranium-bearing monazite sands in furtherance of a fully integrated U.S.-based REE supply chain.


## Research loop (think → act)

1. _heuristic_ — Coverage looks adequate for this pass; stopping iterative loop.

## Sources

- **[S1]** UUUU fundamentals (yfinance)
  - Energy Fuels Inc: price=12.35, rev=65922000.0, fcf=-141273000.0, shares=249919146.0, rev_cagr=0.7399355982144395, ROIC=-0.07845383396530209, FCF yield=-0.045771237745452775
- **[S2]** UUUU DCF valuation (dcf)
  - Base share price=-2.319282330772069, bull=-1.8467855109534992, bear=-2.4323007189325736
- **[S3]** UUUU EV/EBITDA valuation (multiples)
  - Base implied price=29.565754037907926, multiple=8.0
- **[S4]** Energy Fuels (UUUU) Stock Forecast and Price Target 2026 (web) — https://www.marketbeat.com/stocks/NYSEAMERICAN/UUUU/forecast/
  - UUUU's current price target is $23.25. Learn why top analysts are making this stock forecast for Energy Fuels at MarketBeat.
- **[S5]** What is the current Price Target and Forecast for Energy Fuels (UUUU) (web) — https://www.zacks.com/stock/research/UUUU/price-target-stock-forecast
  - Price Target Based on short-term price targets offered by five analysts, the average price target for Energy Fuels comes to $25.69. The forecasts range from a low of $16.00 to a…
- **[S6]** Energy Fuels (UUUU) Stock Forecast & Analyst Price Targets (web) — https://stockanalysis.com/stocks/uuuu/forecast/
  - Stock forecasts and analyst price target predictions for Energy Fuels Inc. (UUUU) stock, with detailed revenue and earnings estimates.
- **[S7]** UUUU Price Target: $22 (+87%) | 9 Analyst Ratings 2026 (web) — https://vcpscanner.com/stock/uuuu/price-target
  - Energy Fuels Inc. (UUUU) has a $22 consensus price target from 9 analysts (Buy). View upside analysis, rating distribution & peer comparison.
- **[S8]** Is Energy Fuels Inc. (UUUU) Stock Still a Long-Term Opportunity After Analyst Price Target Cut? (web) — https://finance.yahoo.com/energy/articles/energy-fuels-inc-uuuu-stock-200741850.html
  - We recently compiled a list of the 8 Best Rare Earth Stocks to Buy in 2026. Energy Fuels Inc. (NYSEAMERICAN:UUUU) is among the best rare earth stocks on this list. TheFly report…
- **[S9]** Roth MKM Reaffirms Their Hold Rating on Energy Fuels (UUUU) (web) — https://www.theglobeandmail.com/investing/markets/stocks/UUUU-A/pressreleases/14495/roth-mkm-reaffirms-their-hold-rating-on-energy-fuels-uuuu/
  - Detailed price information for Energy Fuels Inc (UUUU-A) from The Globe and Mail including charting and trades.
- **[S10]** Roth MKM Remains a Hold on Energy Fuels (UUUU) (web) — https://www.theglobeandmail.com/investing/markets/stocks/UUUU-A/pressreleases/2604873/roth-mkm-remains-a-hold-on-energy-fuels-uuuu/
  - Detailed price information for Energy Fuels Inc (UUUU-A) from The Globe and Mail including charting and trades.
- **[S11]** Wall Street bulls look optimistic about Energy Fuels (UUUU): Should you buy? (web) — https://www.msn.com/en-us/money/top-stocks/wall-street-bulls-look-optimistic-about-energy-fuels-uuuu-should-you-buy/ar-AA27uqQa?ocid=BingNewsVerp
  - Investors often turn to recommendations made by Wall Street analysts before making a Buy, Sell, or Hold decision about a ...
- **[S12]** Energy Fuels (UUUU) Stock Forecast and Price Target 2026 (web_page) — https://www.marketbeat.com/stocks/NYSEAMERICAN/UUUU/forecast/
  - Energy Fuels (UUUU) Stock Forecast and Price Target 2026 Skip to main content → Buy this stock today (From Chaikin Analytics) (Ad) Free UUUU Stock Alerts Energy Fuels (UUUU)  St…
- **[S13]** What is the current Price Target and Forecast for Energy Fuels (UUUU) (web_page) — https://www.zacks.com/stock/research/UUUU/price-target-stock-forecast
  - Pardon Our Interruption As you were browsing something about your browser made us think you were a bot. There are a few reasons this might happen: You're a power user moving thr…
- **[S14]** Energy Fuels (UUUU) Stock Forecast & Analyst Price Targets (web_page) — https://stockanalysis.com/stocks/uuuu/forecast/
  - Energy Fuels (UUUU) Stock Forecast & Analyst Price Targets Collapse Energy Fuels Inc. (UUUU) NYSEAMERICAN: UUUU · Real-Time Price · USD Full Chart Watchlist Alerts Compare 12.35…
- **[S15]** UUUU Intrinsic Valuation and Fundamental Analysis - Energy Fuels Inc - Alpha Spread (web) — https://www.alphaspread.com/security/amex/uuuu/summary
  - UUUU stock discount rate: cost of equity and WACC. ... The intrinsic value for Energy Fuels Inc (UUUU) under the Base Case is 4.86 USD.
- **[S16]** 3 Ways of Calculating a Stock's Intrinsic Value - HubPages (web) — https://discover.hubpages.com/money/Stock-Valuation-Using-Bear-Bull-and-Base-Case-Scenarios
  - September 12, 2024 - It's highly probable that reality ... following scenarios plotted out, you can make a valuation like so: Base case: 50% probability of $150 intrinsic value...
- **[S17]** 3 Ways of Calculating a Stock's Intrinsic Value - ToughNickel (web) — https://toughnickel.com/personal-finance/Stock-Valuation-Using-Bear-Bull-and-Base-Case-Scenarios
  - March 22, 2023 - It's highly probable that reality ... following scenarios plotted out, you can make a valuation like so: Base case: 50% probability of $150 intrinsic value...
- **[S18]** Bull Base Bear Valuation for One Stock | Model Reef (web) — https://modelreef.io/resources/articles/stock-valuation/how-to-create-a-bull-base-bear-valuation-for-one-stock-scenario-driven-intrinsic-value
  - April 15, 2026 - The point of bull/base/bear is to show what must be true-not to pretend the world can be summarised in one number. If you want a quick quality check, compare yo…
- **[S19]** Energy Fuels Inc: Investors | Uranium Stocks and Press Releases (web) — https://investors.energyfuels.com/
  - Articles and press releases about Uranium stocks for investors of Energy Fuels and their partners. Energy Fuels is a fully-integrated producer of both ...
- **[S20]** Energy Fuels - Uranium, Rare Earths & Critical Minerals (web) — https://www.energyfuels.com/
  - American producer of uranium for the nuclear fuel cycle, rare earth oxides and critical minerals, operating the only U.S. conventional uranium mill.
- **[S21]** Energy Fuels Announces Q1-2026 Results - PR Newswire (web) — https://www.prnewswire.com/news-releases/energy-fuels-announces-q1-2026-results-302764727.html
  - May 6, 2026 ... ... Energy Fuels Inc. (NYSE American: UUUU) ... Energy Fuels is a leading U.S. critical materials company specializing in uranium, rare earth ...
- **[S22]** Energy Fuels Inc. (UUUU) Stock Price, News, Quote & History (web) — https://finance.yahoo.com/quote/UUUU/
  - It produces and sells vanadium pentoxide, rare earth elements, carbonate, and heavy mineral sands, such as ilmenite, rutile, zircon, and monazite. The company ...
- **[S23]** UUUU Intrinsic Valuation and Fundamental Analysis - Energy Fuels Inc - Alpha Spread (web_page) — https://www.alphaspread.com/security/amex/uuuu/summary
  - UUUU Intrinsic Valuation and Fundamental Analysis - Energy Fuels Inc - Alpha Spread Alpha Spread Dashboard Tools Market News Investing Ideas Pricing Search 100,000+ stocks... EN…
- **[S24]** UUUU 10-K (sec)
  - Item 1 chars=80000, Item 1A chars=50000, Item 7 chars=50000, ok=True, source=cache
- **[S25]** Item 1 Business summary (nlp)
  - ### Item 1 — Business (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, guidance, revenue, margin, supply chain, customer, segment, product, market…
- **[S26]** Item 1A summary (nlp)
  - ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, supply chain, interest rate, cust…
- **[S27]** Item 7 summary (nlp)
  - ### Item 7 — MD&A (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, regulation, guidance, revenue, margin, supply chain, segment, product, market, operations, s…
- **[S28]** UUUU scenario price ranges (scenarios)
  - ok=True; base mid=29.565754037907926; headwinds=7; tailwinds=7

## Self-critique

_Automated review (heuristic)._

### Strengths
- Combines local fundamentals, optional DCF scenarios, and cited sources where available.
- Keeps a non-advisory framing for local research drafts.

### Issues & gaps
- Base-case model equity value is negative - treat intrinsic-value output as stress/distress, not a buy signal.
- Base-case implies deep downside vs spot (<-70%); confirm whether near-term FCF normalization is appropriate for this business.
- Draft uses strong recommendation language; this local agent should stay descriptive, not advisory.

### Caution for readers
- Treat scenario prices as sensitivity output, not a forecast.
- Re-check primary filings and fresh market data before any decision.



---

# Template: Full diligence (`deep`)

# UUUU — Planned Research Report

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
- Company: Energy Fuels Inc
- Sector / industry: Energy / Uranium
- Price: 12.35
- 52-week range: $8.16 – $27.90
- Market cap: $3.09B
- Enterprise value: $2.70B
- Shares outstanding: 249.92M
- Beta: 1.583
- Book equity: $678.40M
- Revenue (latest): $65.92M
- EBITDA (latest): -$95.72M
- Free cash flow (latest): -$141.27M
- Operating income: -$101.16M
- Operating margin: -153.4%
- EV / EBITDA: -28.3x
- ROIC: -7.8%
- FCF yield: -4.6%
- Debt / Equity: 0.9959950177254
- FCF / share: -$0.57
- Revenue / share: $0.26

### Capital structure
- Cash: $64.74M
- Short-term debt: —
- Long-term debt: $675.69M
- Total debt: $675.69M
- Net debt: $610.95M
- Net debt / EBITDA: -6.4x

### Growth
- Revenue CAGR: 74.0%
- FCF CAGR: —
- Latest revenue YoY: -15.6%
- Latest FCF YoY: -88.4%

### Market expectations (yfinance, sparse)
- Mean target: $26.12
- Target range: $16.00 – $32.50
- Recommendation: strong_buy

_Consensus revenue/EBITDA forecasts are often unavailable via free feeds; treat targets as point-in-time only._

### Historical KPIs (multi-year)

| Year | Revenue | OCF | Capex | FCF | EBITDA | LT debt | Cash | Net debt | Net income |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2025 | $65.92M | -$89.48M | $51.79M | -$141.27M | -$95.72M | $675.69M | $64.74M | $610.95M | -$85.63M |
| 2024 | $78.11M | -$43.97M | $31.02M | -$75.00M | -$34.05M | — | $38.60M | -$38.60M | -$47.77M |
| 2023 | $37.93M | -$15.41M | $44.71M | -$60.12M | -$29.62M | — | $57.45M | -$57.45M | $99.86M |
| 2022 | $12.52M | -$49.70M | $2.00M | -$51.70M | -$56.51M | — | $62.82M | -$62.82M | -$59.85M |

## Charts

### Revenue & FCF history
![Revenue & FCF history](/charts/UUUU_deep_revenue_fcf.png)

### DCF scenario prices
![DCF scenario prices](/charts/UUUU_deep_dcf_scenarios.png)

### Base-case FCF path
![Base-case FCF path](/charts/UUUU_deep_base_fcf_path.png)

## DCF valuation (base / bull / bear) [S2]

> Simplified revenue->FCF DCF. Not investment advice; assumptions are editable heuristics.

- Spot price: $12.35
- Base revenue: $65.92M
- Shares: 249,919,146
- Net debt (Debt−Cash): $610.95M

| Scenario | Growth | FCF margin | WACC | Term. g | Equity value | Share price | Upside |
|----------|--------|------------|------|---------|--------------|-------------|--------|
| bear | -15.6% | 1.0% | 12.0% | 1.5% | -$607.88M | $-2.43 | -119.7% |
| base | 6.0% | 3.0% | 10.0% | 2.5% | -$579.63M | $-2.32 | -118.8% |
| bull | 15.0% | 8.0% | 9.0% | 3.0% | -$461.55M | $-1.85 | -115.0% |

### Assumption notes
- Base revenue growth seeded from historical rate (-15.6%).
- Recent revenue declined (-15.6% YoY); base/bull use normalized mid-cycle growth instead of extrapolating the decline.
- Latest FCF margin was -214.3%; scenarios use normalized positive margins for a going-concern DCF.

- _base: model equity value is negative after net debt (-579,633,059); showing $-2.32/sh._
- _bull: model equity value is negative after net debt (-461,547,058); showing $-1.85/sh._
- _bear: model equity value is negative after net debt (-607,878,518); showing $-2.43/sh._

### Base-case projected FCF

- Year 1: revenue $69.88M, FCF $2.10M (PV $1.91M)
- Year 2: revenue $74.07M, FCF $2.22M (PV $1.84M)
- Year 3: revenue $78.51M, FCF $2.36M (PV $1.77M)
- Year 4: revenue $83.23M, FCF $2.50M (PV $1.71M)
- Year 5: revenue $88.22M, FCF $2.65M (PV $1.64M)
- Terminal value $36.17M (PV $22.46M)

## Web research — web_research

- Queries: Deep diligence: fundamentals, DCF, web, 10-K risks & MD&A
- Unique hits: 4
- Pages fetched: 3/3

### Web synthesis — web_research (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, revenue, margin, cyber, customer, segment, product, service, market, network

- Where are the main threats and risks to the business?
- [HIT] What's Inside a 10-K Report | paperswithbacktest.com | https://paperswithbacktest.com/datasets/10-k-report-contents-access These can include market and economic risks, industry-specific challenges, regulatory and legal risks, operational hazards, financial risks, cybersecurity ...
- What are the company’s products and services?
- Who are its main customers and competitors?
- Does it generate good margins and returns?
- Where are the main threats and risks to the business?
- Assessing the business 10k /Annual Report: Almost always the best place to start Company overview section Products/services Differentiation and strategy End markets Competitors Customers Risk Factors: mostly legalese but look for outliers Management Discussion and Analysis (MD&A): how has the business performed recently Financial Statements Cash flow statement is king Notes Don't worry about things such as revenue recognition or goodwill accounting Chairman or CEO Letter: Always worth reading for context (for a few years and look at the consistency and promises of the management) Company conference presentations: transcripts and PowerPoints Company Website: can have a treasure trove of information Sell-side initiation report available?
- Can offer a very helpful overview Beware of inherent bias and of "price targets" Recently quarterly conference call transcripts Other web-based content: Industry primers Write-ups from other investors (Seeking Alpha or Value Investors Club) Proceed with caution Industry blogs and trade magazines Fundamentals  and quality of business Business quality Margin and return analysis: ROIC > WACC?

### Sources found
- [How do you actually do due diligence on a stock? - Reddit](https://www.reddit.com/r/stocks/comments/1m56g5u/how_do_you_actually_do_due_diligence_on_a_stock/)
  - Jul 21, 2025 ... The company should have an investors section on their website where you can find their SEC filings. You want to look at the latest 10-K annu…
- [How to: Due diligence in 48 hours - Roiss' Conclusions - Substack](https://roiss.substack.com/p/how-to-due-diligence-in-48-hours)
  - Apr 22, 2021 ... Where are the main threats and risks to the business? Assessing the business. 10k /Annual Report: Almost ...
- [Due Diligence Checklist for Stock Research 2026 | Minalyst Blog](https://minalyst.com/blog/research-guides/due-diligence-checklist)
  - Mar 18, 2026 ... A 10-K runs 150–300 pages. An earnings call transcript adds 30 more. MD&A, footnotes, proxy statements, prior-year comparisons — the materia…
- [What's Inside a 10-K Report](https://paperswithbacktest.com/datasets/10-k-report-contents-access)
  - These can include market and economic risks, industry-specific challenges, regulatory and legal risks, operational hazards, financial risks, cybersecurity ...

### Search warnings
- news:Deep diligence: fundamentals, DCF, web, 10-K risks & MD&A: No results found.

## Put opportunities (heuristic) [S3]
- Expiration: 2026-08-21 (DTE 31)
- Candidates: 0
- ATM IV (est.): 79.5%
- IV rank: — (1 local samples)
- HV rank (20d realized): 6.1%


_Note: Delta band approximated via % OTM when greeks are unavailable; IV rank needs ~20+ local daily IV samples (have 1); run the options screen over time to build history.; HV rank is realized-vol rank (20d HV vs ~1y); useful when IV history is thin._

## SEC filing [S11]
- Extraction OK: True
- Item 1 chars: 80000
- Item 1A chars: 50000
- Item 7 chars: 50000
- Meta: {'source': 'cache', 'path': 'C:\\DevWork\\equity_research_agent\\data\\filings\\UUUU_10k.txt'}

## Company setup & business model

**Keyword hits:** risk, uncertainty, guidance, revenue, margin, supply chain, customer, segment, product, market, operations, subsidiary

- On August 16, 2024, the Company acquired RadTran LLC (“RadTran”), a private company specializing in the separation of critical radioisotopes, to further the Company’s plans for development  and production of medical isotopes used in cancer treatments.
- All of the Company’s U.S.-based employees are employed by its subsidiary Energy Fuels Resources (USA) Inc.
- (“EFUSA”), a wholly owned subsidiary of EF Holdings, which also serves as operator of all the Company’s U.S.
- On February 10, 2023, the Company, through its wholly owned subsidiary Energy Fuels Brazil Ltda., acquired the Bahia Project in the State of Bahia, Brazil.
- On October 2, 2024, the Company acquired Base Resources, which owned the Kwale Project, which is now in reclamation, and the Vara Mada Project in Madagascar, which is currently in permitting and development, thereby further increasing its portfolio of HMS/monazite/REE projects to support a U.S.-controlled REE supply chain.
- The primary trading market for Energy Fuels’ Common Shares is the NYSE American under the trading symbol “ UUUU,” and the Company’s Common Shares are also listed on the TSX under the trading symbol “EFR.” Energy Fuels is a U.S.
- The Designated Primary Market Maker for the Options is Group One Trading, LP.
- Citadel Securities is the Company’s Market Maker on the NYSE American.
- Table of Conten t s  Business Overview  Energy Fuels produces several of the critical minerals essential to the United States (“U.S.”), energy security and other advanced technologies, including uranium, vanadium, REEs (including NdPr, Dy and Tb) and HMS (including titanium and zirconium minerals), in an effort to strengthen domestic supply chains and reduce reliance on foreign-controlled sources.
- due to its notable ability to process uranium, vanadium, REE products, and, potentially, radioisotopes for medical applications.
- We produce vanadium as a co-product from certain of our uranium mines, as market conditions  warrant.
- The REE products we produce are essential to manufacture permanent magnets for traction motors in electric  vehicles (“EVs”), hybrid EVs, defense systems, robotics and other advanced technologies.
- The titanium and zirconium products derived from our HMS products are used in national security and other key industries.
- In processing Alternate Feed Materials, the Mill also helps reduce the quantity of  industry materials permanently disposed of and, by extension, the overall tailings footprint of mining and milling operations.
- controlled REE supply chain, which include:  • the Vara Mada Project acquired through the Company’s 100% acquisition of Base Resources on October 2, 2024, see Part I, Item 2.
- Upon closing of this transaction, which is expected as  early as June 2026, the Company believes it will be the largest, fully integrated REE “mine-to-metal and alloy” producer outside of China closing a critical strategic gap in global supply chains for magnet applications, including automotive, robotic, energy and defense technologies.
- Segment Information  We have three reportable segments based on our operations and the financial information regularly reviewed by our Chief Operating Decision Maker (“ CODM”): (i) uranium, (ii) REE, and (iii) HMS.
- The uranium segment engages in conventional and ISR uranium extraction, recovery and sales of uranium from mineral properties and the recycling of uranium-bearing materials generated by third parties (Alternate Feed Materials) along with the exploration, permitting and evaluation of uranium properties in the U.S.
- The Company’s final uranium product is natural uranium concentrate, or U3 O8, which is sold to customers for further processing into fuel for nuclear reactors.
- The Company also produces vanadium pentoxide, V2 O5, as a co-product of uranium at the Mill within the uranium segment.
- In addition,  Table of Conten t s  within the uranium segment, the Company is exploring opportunities to separate radium-226 (“Ra-226”) and radium-228 (“Ra-228”) as a byproduct of its existing uranium and REE process streams for potential use in the production of medical isotopes for emerging TAT cancer treatments.
- The REE segment is engaged in the Company’s initiatives to progress towards full REE separation capabilities at the Mill to produce both “light” and “heavy” separated REE oxides.
- The Company has the current capacity to produce separated REE products in  its Phase 1 Circuit.
- The Company is planning further enhancements to expand its heavy REE production at its Phase 1 Circuit for the planned recovery of dysprosium (“Dy”), terbium (“Tb”), samarium (“Sm”), europium (“Eu”) and gadolinium (“Gd”), with the ability to separate other heavy REEs such as yttrium (“Y”) and lutetium (“Lu”) if market conditions warrant, subject to the receipt of regulatory approvals, financing, completion of engineering and the receipt of sufficient feed materials.
- The  Company also plans to expand its NdPr, Dy and Tb production recovery and potentially other REE material production recovery in the future, subject to the receipt of regulatory approvals, completion of engineering, financing and the receipt of sufficient feed materials, through the development of its proposed stand-alone phase 2 REE production circuit (the “Phase 2 Circuit”) with a total planned production recovery (from the Phase 1 Circuit and Phase 2 Circuit) of up to approximately 6,000 tonnes of NdPr, 200 tonnes of Dy and 60 tonnes of Tb per year, along with other REEs, described in more detail below, from monazite concentrates, mixed rare earth carbonates (“MREC”) or similar feed materials.
- The monazite feedstock for the Company’s REE production is expected to be procured through Company-owned mines like the Vara Mada Project and Bahia Project, as well as its joint venture interest in the Donald Project, along with other potential acquisitions, joint ventures, open market offtake,  and/or other collaborations, in each case upon successful completion of development of the projects and transactions.
- The HMS segment engages in the exploration and development, and planned recovery, of HMS at the Vara Mada Project, Bahia Project and through the Company’s investment in the Donald Project JV.
- The HMS segment also includes the Kwale Project, which ceased mine operations on December 31, 2024 and is now in reclamation.

_Source: latest 10-K Item 1 (Business), summarized locally._

## Qualitative analysis (local LLM)

### Item 1 — Business (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, uncertainty, guidance, revenue, margin, supply chain, customer, segment, product, market, operations, subsidiary

- On August 16, 2024, the Company acquired RadTran LLC (“RadTran”), a private company specializing in the separation of critical radioisotopes, to further the Company’s plans for development  and production of medical isotopes used in cancer treatments.
- All of the Company’s U.S.-based employees are employed by its subsidiary Energy Fuels Resources (USA) Inc.
- (“EFUSA”), a wholly owned subsidiary of EF Holdings, which also serves as operator of all the Company’s U.S.
- On February 10, 2023, the Company, through its wholly owned subsidiary Energy Fuels Brazil Ltda., acquired the Bahia Project in the State of Bahia, Brazil.
- On October 2, 2024, the Company acquired Base Resources, which owned the Kwale Project, which is now in reclamation, and the Vara Mada Project in Madagascar, which is currently in permitting and development, thereby further increasing its portfolio of HMS/monazite/REE projects to support a U.S.-controlled REE supply chain.
- The primary trading market for Energy Fuels’ Common Shares is the NYSE American under the trading symbol “ UUUU,” and the Company’s Common Shares are also listed on the TSX under the trading symbol “EFR.” Energy Fuels is a U.S.
- The Designated Primary Market Maker for the Options is Group One Trading, LP.
- Citadel Securities is the Company’s Market Maker on the NYSE American.
- Table of Conten t s  Business Overview  Energy Fuels produces several of the critical minerals essential to the United States (“U.S.”), energy security and other advanced technologies, including uranium, vanadium, REEs (including NdPr, Dy and Tb) and HMS (including titanium and zirconium minerals), in an effort to strengthen domestic supply chains and reduce reliance on foreign-controlled sources.
- due to its notable ability to process uranium, vanadium, REE products, and, potentially, radioisotopes for medical applications.
- We produce vanadium as a co-product from certain of our uranium mines, as market conditions  warrant.
- The REE products we produce are essential to manufacture permanent magnets for traction motors in electric  vehicles (“EVs”), hybrid EVs, defense systems, robotics and other advanced technologies.
- The titanium and zirconium products derived from our HMS products are used in national security and other key industries.
- In processing Alternate Feed Materials, the Mill also helps reduce the quantity of  industry materials permanently disposed of and, by extension, the overall tailings footprint of mining and milling operations.
- controlled REE supply chain, which include:  • the Vara Mada Project acquired through the Company’s 100% acquisition of Base Resources on October 2, 2024, see Part I, Item 2.
- Upon closing of this transaction, which is expected as  early as June 2026, the Company believes it will be the largest, fully integrated REE “mine-to-metal and alloy” producer outside of China closing a critical strategic gap in global supply chains for magnet applications, including automotive, robotic, energy and defense technologies.
- Segment Information  We have three reportable segments based on our operations and the financial information regularly reviewed by our Chief Operating Decision Maker (“ CODM”): (i) uranium, (ii) REE, and (iii) HMS.
- The uranium segment engages in conventional and ISR uranium extraction, recovery and sales of uranium from mineral properties and the recycling of uranium-bearing materials generated by third parties (Alternate Feed Materials) along with the exploration, permitting and evaluation of uranium properties in the U.S.
- The Company’s final uranium product is natural uranium concentrate, or U3 O8, which is sold to customers for further processing into fuel for nuclear reactors.
- The Company also produces vanadium pentoxide, V2 O5, as a co-product of uranium at the Mill within the uranium segment.
- In addition,  Table of Conten t s  within the uranium segment, the Company is exploring opportunities to separate radium-226 (“Ra-226”) and radium-228 (“Ra-228”) as a byproduct of its existing uranium and REE process streams for potential use in the production of medical isotopes for emerging TAT cancer treatments.
- The REE segment is engaged in the Company’s initiatives to progress towards full REE separation capabilities at the Mill to produce both “light” and “heavy” separated REE oxides.
- The Company has the current capacity to produce separated REE products in  its Phase 1 Circuit.
- The Company is planning further enhancements to expand its heavy REE production at its Phase 1 Circuit for the planned recovery of dysprosium (“Dy”), terbium (“Tb”), samarium (“Sm”), europium (“Eu”) and gadolinium (“Gd”), with the ability to separate other heavy REEs such as yttrium (“Y”) and lutetium (“Lu”) if market conditions warrant, subject to the receipt of regulatory approvals, financing, completion of engineering and the receipt of sufficient feed materials.
- The  Company also plans to expand its NdPr, Dy and Tb production recovery and potentially other REE material production recovery in the future, subject to the receipt of regulatory approvals, completion of engineering, financing and the receipt of sufficient feed materials, through the development of its proposed stand-alone phase 2 REE production circuit (the “Phase 2 Circuit”) with a total planned production recovery (from the Phase 1 Circuit and Phase 2 Circuit) of up to approximately 6,000 tonnes of NdPr, 200 tonnes of Dy and 60 tonnes of Tb per year, along with other REEs, described in more detail below, from monazite concentrates, mixed rare earth carbonates (“MREC”) or similar feed materials.
- The monazite feedstock for the Company’s REE production is expected to be procured through Company-owned mines like the Vara Mada Project and Bahia Project, as well as its joint venture interest in the Donald Project, along with other potential acquisitions, joint ventures, open market offtake,  and/or other collaborations, in each case upon successful completion of development of the projects and transactions.
- The HMS segment engages in the exploration and development, and planned recovery, of HMS at the Vara Mada Project, Bahia Project and through the Company’s investment in the Donald Project JV.
- The HMS segment also includes the Kwale Project, which ceased mine operations on December 31, 2024 and is now in reclamation.


### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, uncertainty, litigation, regulation, competition, supply chain, interest rate, customer, product, service, market, operations

- Other factors may arise in the future that are currently not foreseen by management of Energy Fuels that may present additional risks, including risks that the Company currently feels are immaterial.
- Current and prospective shareholders of Energy Fuels should carefully consider these risk factors when making investment decisions.
- Our failure to successfully address any of the risks and uncertainties described below could have a material adverse effect on our business, financial condition and/or results of operations, and the trading price of our Common Shares may fluctuate widely.
- We cannot assure you that we have or will successfully or fully address these risks or other unknown risks that may affect our business.
- Risks Related to our Industry  We are subject to the risks normally encountered by companies in the mineral extraction industry.
- We are subject to the risks normally encountered by companies in the mineral extraction industry, such as:  • the discovery of unusual or unexpected geological formations, and variations in ore radiation levels;  • wild/bushfires, floods, earthquakes, tornados, tropical cyclones, droughts, landslides and other natural disasters;  • accidental fires, unplanned power outages and water shortages;  • controlling water, emissions and other similar mining hazards;  • operating labor disruptions and labor disputes;  • the ability to obtain and maintain suitable or adequate machinery, equipment or labor;  • our liability for potential or existing pollution or other hazards; and  • other known and unknown risks involved in the conduct of exploration, development and operation of mines, E&R facilities and mills, and metals and alloys plants (pending the successful acquisition of ASM), along with the markets for uranium, rare earths, vanadium, HMS and metals and alloys.
- The development of mineral properties is affected by many factors, including, but not limited to: the cost of operations; variations in the grade of mineralized material; fluctuations in metal markets; costs of extraction and processing equipment; availability of equipment and labor; labor costs and possible labor strikes; government regulations, including without limitation, regulations relating to taxes, royalties, allowable extraction or production, and importing and exporting of minerals;  government actions, including without limitation the establishment or expansion of mineral withdrawals, parks and monuments; land exchanges; foreign exchange; employment; worker safety; transportation; and environmental protection.
- Our results of operations are significantly affected by the market prices of uranium, vanadium, rare earth elements and heavy mineral sands, which are cyclical and subject to substantial price fluctuations.


### Item 7 — MD&A (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, regulation, guidance, revenue, margin, supply chain, segment, product, market, operations, subsidiary

- AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERATIONS.
- The purpose of this Item 7 is: (i) to provide material relevant to an assessment of the financial condition and results of operations of Energy Fuels Inc., including an evaluation of the amounts and certainty of cash flows from operations and from outside information sources; and (ii) to focus specifically on  material events and uncertainties known to management that are reasonably likely to cause reported financial information not necessarily indicative of future operating results or of future financial condition.
- This Discussion and Analysis contains forward-looking statements that involve risks, uncertainties, and assumptions.
- Risk Factors and elsewhere in this Annual Report.
- energy security and advanced technologies, including uranium, vanadium, REEs and HMS, strengthening domestic supply chains and reducing reliance on foreign sources.
- The Company’s White Mesa Mill, near  Blanding, Utah, is the only licensed and operating uranium mill, and the only uranium mill capable of producing separated REE products, in the U.S.
- The titanium and zirconium products derived from our HMS production are used in national security and other key industries.
- The Company has secured its own sources of REE- and uranium-bearing monazite sands in furtherance of a fully integrated U.S.-based REE supply chain.


## Research loop (think → act)

1. _heuristic_ — Coverage looks adequate for this pass; stopping iterative loop.

## Sources

- **[S1]** UUUU fundamentals (yfinance)
  - Energy Fuels Inc: price=12.35, rev=65922000.0, fcf=-141273000.0, shares=249919146.0, rev_cagr=0.7399355982144395, ROIC=-0.07845383396530209, FCF yield=-0.045771237745452775
- **[S2]** UUUU DCF valuation (dcf)
  - Base share price=-2.319282330772069, bull=-1.8467855109534992, bear=-2.4323007189325736
- **[S3]** UUUU put screen (yfinance_options)
  - Expiration 2026-08-21 (DTE 31): 0 candidates; IV=0.7949239257812499, IV rank=None, HV rank=0.060543710579782355. Delta band approximated via % OTM when greeks are unavailable; I…
- **[S4]** How do you actually do due diligence on a stock? - Reddit (web) — https://www.reddit.com/r/stocks/comments/1m56g5u/how_do_you_actually_do_due_diligence_on_a_stock/
  - Jul 21, 2025 ... The company should have an investors section on their website where you can find their SEC filings. You want to look at the latest 10-K annual ...
- **[S5]** How to: Due diligence in 48 hours - Roiss' Conclusions - Substack (web) — https://roiss.substack.com/p/how-to-due-diligence-in-48-hours
  - Apr 22, 2021 ... Where are the main threats and risks to the business? Assessing the business. 10k /Annual Report: Almost ...
- **[S6]** Due Diligence Checklist for Stock Research 2026 | Minalyst Blog (web) — https://minalyst.com/blog/research-guides/due-diligence-checklist
  - Mar 18, 2026 ... A 10-K runs 150–300 pages. An earnings call transcript adds 30 more. MD&A, footnotes, proxy statements, prior-year comparisons — the material is ...
- **[S7]** What's Inside a 10-K Report (web) — https://paperswithbacktest.com/datasets/10-k-report-contents-access
  - These can include market and economic risks, industry-specific challenges, regulatory and legal risks, operational hazards, financial risks, cybersecurity ...
- **[S8]** Reddit - Please wait for verification (web_page) — https://www.reddit.com/r/stocks/comments/1m56g5u/how_do_you_actually_do_due_diligence_on_a_stock/
  - Reddit - Please wait for verification
- **[S9]** How to: Due diligence in 48 hours - Roiss' Conclusions (web_page) — https://roiss.substack.com/p/how-to-due-diligence-in-48-hours
  - How to: Due diligence in 48 hours - Roiss' Conclusions Roiss' Conclusions Subscribe Sign in How to: Due diligence in 48 hours Transcription from Cove Street's portfolio manager …
- **[S10]** Due Diligence Checklist for Stock Research 2026 | Minalyst Blog (web_page) — https://minalyst.com/blog/research-guides/due-diligence-checklist
  - Due Diligence Checklist for Stock Research 2026 | Minalyst Blog Own a production AI investment-research platform. Minalyst is available for acquisition — get in touch to make it…
- **[S11]** UUUU 10-K (sec)
  - Item 1 chars=80000, Item 1A chars=50000, Item 7 chars=50000, ok=True, source=cache
- **[S12]** Item 1 Business summary (nlp)
  - ### Item 1 — Business (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, guidance, revenue, margin, supply chain, customer, segment, product, market…
- **[S13]** Item 1A summary (nlp)
  - ### Item 1A — Risk Factors (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, uncertainty, litigation, regulation, competition, supply chain, interest rate, cust…
- **[S14]** Item 7 summary (nlp)
  - ### Item 7 — MD&A (rule-based fallback — Ollama unavailable) **Keyword hits:** risk, regulation, guidance, revenue, margin, supply chain, segment, product, market, operations, s…

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

# Template: Options income (`income`)

# UUUU — Planned Research Report

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
- Company: Energy Fuels Inc
- Sector / industry: Energy / Uranium
- Price: 12.35
- 52-week range: $8.16 – $27.90
- Market cap: $3.09B
- Enterprise value: $2.70B
- Shares outstanding: 249.92M
- Beta: 1.583
- Book equity: $678.40M
- Revenue (latest): $65.92M
- EBITDA (latest): -$95.72M
- Free cash flow (latest): -$141.27M
- Operating income: -$101.16M
- Operating margin: -153.4%
- EV / EBITDA: -28.3x
- ROIC: -7.8%
- FCF yield: -4.6%
- Debt / Equity: 0.9959950177254
- FCF / share: -$0.57
- Revenue / share: $0.26

### Capital structure
- Cash: $64.74M
- Short-term debt: —
- Long-term debt: $675.69M
- Total debt: $675.69M
- Net debt: $610.95M
- Net debt / EBITDA: -6.4x

### Growth
- Revenue CAGR: 74.0%
- FCF CAGR: —
- Latest revenue YoY: -15.6%
- Latest FCF YoY: -88.4%

### Market expectations (yfinance, sparse)
- Mean target: $26.12
- Target range: $16.00 – $32.50
- Recommendation: strong_buy

_Consensus revenue/EBITDA forecasts are often unavailable via free feeds; treat targets as point-in-time only._

### Historical KPIs (multi-year)

| Year | Revenue | OCF | Capex | FCF | EBITDA | LT debt | Cash | Net debt | Net income |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2025 | $65.92M | -$89.48M | $51.79M | -$141.27M | -$95.72M | $675.69M | $64.74M | $610.95M | -$85.63M |
| 2024 | $78.11M | -$43.97M | $31.02M | -$75.00M | -$34.05M | — | $38.60M | -$38.60M | -$47.77M |
| 2023 | $37.93M | -$15.41M | $44.71M | -$60.12M | -$29.62M | — | $57.45M | -$57.45M | $99.86M |
| 2022 | $12.52M | -$49.70M | $2.00M | -$51.70M | -$56.51M | — | $62.82M | -$62.82M | -$59.85M |

## Charts

### Revenue & FCF history
![Revenue & FCF history](/charts/UUUU_income_revenue_fcf.png)

## Web research — web_research

- Queries: UUUU news, Energy Fuels Inc earnings OR catalyst
- Unique hits: 11
- Pages fetched: 2/3

### Web synthesis — web_research (rule-based fallback — Ollama unavailable)
**Keyword hits:** risk, revenue, customer, segment, market

- It is owned by Saudi Research and Marketing Group that also operate Independent Urdu and Arab News, Pakistan edition, in Pakistan.
- Yahoo Finance Singapore · · · 21 hours ago · Energy Fuels (UUUU) Increases Despite Market Slip: Here's What You Need to Know ·  [HIT] Is Energy Fuels Inc.
- | Zacks Investment Research on MSN | https://www.msn.com/en-us/money/markets/energy-fuels-slides-18-in-past-3-months-exit-now-or-stay-put/ar-AA26ZJwX?ocid=BingNewsVerp Shares of Energy Fuels UUUU have been under pressure lately, falling roughly 18.3% over the three months.
- | Zacks Investment Research on MSN | https://www.msn.com/en-us/money/markets/can-energy-fuels-liquidity-position-support-its-expansion-plans/ar-AA27EPRF?ocid=BingNewsVerp Energy Fuels Inc.
- The market data on this page is currently delayed.
- Learn more Chart Range Bar 1D 5D -6.65% 1M -25.42% 6M -47.49% YTD -13.09% 1Y 34.09% 5Y 133.02% All -93.18% Mountain Advanced Chart AlphaSpace Chart Loading chart for UUUU News headlines Energy Fuels (UUUU) has shown resilience, gaining 2.18% despite broader market declines.
- However, the stock is down 30.62% over the past month, with analysts projecting significant revenue growth and improving EPS estimates for the upcoming quarters.
- Energy Fuels (UUUU) has shown resilience, gaining 2.18% despite broader market declines.

### Sources found
- [Urdu News](https://en.wikipedia.org/wiki/Urdu_News)
  - Urdu News is a Saudi Arabian Urdu language-news website with the focus on Pakistan, Saudi Arabia and other parts of the globe. It was the first daily Urdu ne…
- [Energy Fuels Inc. (UUUU) Stock Price, News, Quote & History - Yahoo Finance](https://finance.yahoo.com/quote/UUUU/)
  - 1 day ago - Energy Fuels (UUUU) is experiencing notable volatility, with a 2.18% increase on July 20 despite a 30.62% decline over the past month.
- [Energy Fuels: UUUU Stock Price Quote & News | Robinhood](https://robinhood.com/us/en/stocks/UUUU/)
  - On 2026-07-21, Energy Fuels(UUUU) stock moved within a range of $11.89 to $12.40.
- [Energy Fuels Inc (UUUU) Stock Price & News - Google Finance](https://www.google.com/finance/beta/quote/UUUU:NYSEAMERICAN)
  - May 25, 2026 - News stories · From sources across the web · Wealth Awesome · · · 7 hours ago · What's Going On With Energy Fuels Inc Stock Tuesday? Yahoo Fin…
- [Is Energy Fuels Inc. (UUUU) Stock Still a Long-Term Opportunity After Analyst Price Target Cut?](https://finance.yahoo.com/energy/articles/energy-fuels-inc-uuuu-stock-200741850.html)
  - We recently compiled a list of the 8 Best Rare Earth Stocks to Buy in 2026. Energy Fuels Inc. (NYSEAMERICAN:UUUU) is among the best rare earth stocks on this…
- [UUUU Falls 28% in a Year: Should You Buy, Hold or Sell the Stock?](https://www.nasdaq.com/articles/uuuu-falls-28-year-should-you-buy-hold-or-sell-stock)
  - Energy Fuels UUUU has declined 27.7% in the past 12 months against the non-ferrous mining industry’s 16.2% growth. The Zacks Basic Materials sector has slipp…
- [Energy Fuels slides 18% in past 3 months: Exit now or stay put?](https://www.msn.com/en-us/money/markets/energy-fuels-slides-18-in-past-3-months-exit-now-or-stay-put/ar-AA26ZJwX?ocid=BingNewsVerp)
  - Shares of Energy Fuels UUUU have been under pressure lately, falling roughly 18.3% over the three months. The stock has underperformed the non-ferrous mining…
- [Can Energy Fuels' liquidity position support its expansion plans?](https://www.msn.com/en-us/money/markets/can-energy-fuels-liquidity-position-support-its-expansion-plans/ar-AA27EPRF?ocid=BingNewsVerp)
  - Energy Fuels Inc. UUUU has continued to reinforce its financial position, providing it the flexibility to pursue its ...
- [Energy Fuels Inc: Investors | Uranium Stocks and Press Releases](https://investors.energyfuels.com/)
  - Investors · Jun 25, 2026. Energy Fuels Announces Election of Directors · Jun 23, 2026. Energy Fuels Announces Definitive Agreement to Acquire VAC for $1.9 Bi…
- [Energy Fuels (UUUU) Earnings: Latest Report, Earnings Call ...](https://public.com/stocks/uuuu/earnings)
  - The company is expected to announce its next earnings report on 08/05/2026 , with analysts projecting an EPS of -$0.04. Energy Fuels (UUUU) Earnings History ...
- [Uranium Mining & Energy - Presentation](https://www.energyfuels.com/presentation/)
  - ... Careers Privacy Policy Legal Site Map | Presentation. © 2026 ENERGY FUELS INC., ALL RIGHTS RESERVED 225 Union Blvd., Suite 600, Lakewood, Colorado 80228.

### Search warnings
- news:Energy Fuels Inc earnings OR catalyst: No results found.

## Put opportunities (heuristic) [S2]
- Expiration: 2026-08-21 (DTE 31)
- Candidates: 0
- ATM IV (est.): 79.5%
- IV rank: — (1 local samples)
- HV rank (20d realized): 6.1%


_Note: Delta band approximated via % OTM when greeks are unavailable; IV rank needs ~20+ local daily IV samples (have 1); run the options screen over time to build history.; HV rank is realized-vol rank (20d HV vs ~1y); useful when IV history is thin._

## Research loop (think → act)

1. _heuristic_ — Coverage looks adequate for this pass; stopping iterative loop.

## Sources

- **[S1]** UUUU fundamentals (yfinance)
  - Energy Fuels Inc: price=12.35, rev=65922000.0, fcf=-141273000.0, shares=249919146.0, rev_cagr=0.7399355982144395, ROIC=-0.07845383396530209, FCF yield=-0.045771237745452775
- **[S2]** UUUU put screen (yfinance_options)
  - Expiration 2026-08-21 (DTE 31): 0 candidates; IV=0.7949239257812499, IV rank=None, HV rank=0.060543710579782355. Delta band approximated via % OTM when greeks are unavailable; I…
- **[S3]** Urdu News (web) — https://en.wikipedia.org/wiki/Urdu_News
  - Urdu News is a Saudi Arabian Urdu language-news website with the focus on Pakistan, Saudi Arabia and other parts of the globe. It was the first daily Urdu newspaper published in…
- **[S4]** Energy Fuels Inc. (UUUU) Stock Price, News, Quote & History - Yahoo Finance (web) — https://finance.yahoo.com/quote/UUUU/
  - 1 day ago - Energy Fuels (UUUU) is experiencing notable volatility, with a 2.18% increase on July 20 despite a 30.62% decline over the past month.
- **[S5]** Energy Fuels: UUUU Stock Price Quote & News | Robinhood (web) — https://robinhood.com/us/en/stocks/UUUU/
  - On 2026-07-21, Energy Fuels(UUUU) stock moved within a range of $11.89 to $12.40.
- **[S6]** Energy Fuels Inc (UUUU) Stock Price & News - Google Finance (web) — https://www.google.com/finance/beta/quote/UUUU:NYSEAMERICAN
  - May 25, 2026 - News stories · From sources across the web · Wealth Awesome · · · 7 hours ago · What's Going On With Energy Fuels Inc Stock Tuesday? Yahoo Finance Singapore · · ·…
- **[S7]** Is Energy Fuels Inc. (UUUU) Stock Still a Long-Term Opportunity After Analyst Price Target Cut? (web) — https://finance.yahoo.com/energy/articles/energy-fuels-inc-uuuu-stock-200741850.html
  - We recently compiled a list of the 8 Best Rare Earth Stocks to Buy in 2026. Energy Fuels Inc. (NYSEAMERICAN:UUUU) is among the best rare earth stocks on this list. TheFly report…
- **[S8]** UUUU Falls 28% in a Year: Should You Buy, Hold or Sell the Stock? (web) — https://www.nasdaq.com/articles/uuuu-falls-28-year-should-you-buy-hold-or-sell-stock
  - Energy Fuels UUUU has declined 27.7% in the past 12 months against the non-ferrous mining industry’s 16.2% growth. The Zacks Basic Materials sector has slipped 1%, while the S&P…
- **[S9]** Energy Fuels slides 18% in past 3 months: Exit now or stay put? (web) — https://www.msn.com/en-us/money/markets/energy-fuels-slides-18-in-past-3-months-exit-now-or-stay-put/ar-AA26ZJwX?ocid=BingNewsVerp
  - Shares of Energy Fuels UUUU have been under pressure lately, falling roughly 18.3% over the three months. The stock has underperformed the non-ferrous mining industry’s 15.5% de…
- **[S10]** Can Energy Fuels' liquidity position support its expansion plans? (web) — https://www.msn.com/en-us/money/markets/can-energy-fuels-liquidity-position-support-its-expansion-plans/ar-AA27EPRF?ocid=BingNewsVerp
  - Energy Fuels Inc. UUUU has continued to reinforce its financial position, providing it the flexibility to pursue its ...
- **[S11]** Energy Fuels Inc. (UUUU) Stock Price, News, Quote & History - Yahoo Finance (web_page) — https://finance.yahoo.com/quote/UUUU/
  - Energy Fuels Inc. (UUUU) Stock Price, News, Quote & History - Yahoo Finance Oops, something went wrong Skip to navigation Skip to main content Skip to right column We are experi…
- **[S12]** Energy Fuels: UUUU Stock Price Quote & News | Robinhood (web_page) — https://robinhood.com/us/en/stocks/UUUU/
  - Energy Fuels: UUUU Stock Price Quote & News | Robinhood Energy Fuels ‌ 1D 1W 1M 3M YTD 1Y 5Y ALL Why Robinhood? Robinhood gives you the tools you need to put your money in motio…

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

# UUUU — Planned Research Report

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
- Company: Energy Fuels Inc
- Sector / industry: Energy / Uranium
- Price: 12.35
- 52-week range: $8.16 – $27.90
- Market cap: $3.09B
- Enterprise value: $2.70B
- Shares outstanding: 249.92M
- Beta: 1.583
- Book equity: $678.40M
- Revenue (latest): $65.92M
- EBITDA (latest): -$95.72M
- Free cash flow (latest): -$141.27M
- Operating income: -$101.16M
- Operating margin: -153.4%
- EV / EBITDA: -28.3x
- ROIC: -7.8%
- FCF yield: -4.6%
- Debt / Equity: 0.9959950177254
- FCF / share: -$0.57
- Revenue / share: $0.26

### Capital structure
- Cash: $64.74M
- Short-term debt: —
- Long-term debt: $675.69M
- Total debt: $675.69M
- Net debt: $610.95M
- Net debt / EBITDA: -6.4x

### Growth
- Revenue CAGR: 74.0%
- FCF CAGR: —
- Latest revenue YoY: -15.6%
- Latest FCF YoY: -88.4%

### Market expectations (yfinance, sparse)
- Mean target: $26.12
- Target range: $16.00 – $32.50
- Recommendation: strong_buy

_Consensus revenue/EBITDA forecasts are often unavailable via free feeds; treat targets as point-in-time only._

### Historical KPIs (multi-year)

| Year | Revenue | OCF | Capex | FCF | EBITDA | LT debt | Cash | Net debt | Net income |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2025 | $65.92M | -$89.48M | $51.79M | -$141.27M | -$95.72M | $675.69M | $64.74M | $610.95M | -$85.63M |
| 2024 | $78.11M | -$43.97M | $31.02M | -$75.00M | -$34.05M | — | $38.60M | -$38.60M | -$47.77M |
| 2023 | $37.93M | -$15.41M | $44.71M | -$60.12M | -$29.62M | — | $57.45M | -$57.45M | $99.86M |
| 2022 | $12.52M | -$49.70M | $2.00M | -$51.70M | -$56.51M | — | $62.82M | -$62.82M | -$59.85M |

## Charts

### Revenue & FCF history
![Revenue & FCF history](/charts/UUUU_fast_revenue_fcf.png)

### DCF scenario prices
![DCF scenario prices](/charts/UUUU_fast_dcf_scenarios.png)

### Base-case FCF path
![Base-case FCF path](/charts/UUUU_fast_base_fcf_path.png)

## DCF valuation (base / bull / bear) [S2]

> Simplified revenue->FCF DCF. Not investment advice; assumptions are editable heuristics.

- Spot price: $12.35
- Base revenue: $65.92M
- Shares: 249,919,146
- Net debt (Debt−Cash): $610.95M

| Scenario | Growth | FCF margin | WACC | Term. g | Equity value | Share price | Upside |
|----------|--------|------------|------|---------|--------------|-------------|--------|
| bear | -15.6% | 1.0% | 12.0% | 1.5% | -$607.88M | $-2.43 | -119.7% |
| base | 6.0% | 3.0% | 10.0% | 2.5% | -$579.63M | $-2.32 | -118.8% |
| bull | 15.0% | 8.0% | 9.0% | 3.0% | -$461.55M | $-1.85 | -115.0% |

### Assumption notes
- Base revenue growth seeded from historical rate (-15.6%).
- Recent revenue declined (-15.6% YoY); base/bull use normalized mid-cycle growth instead of extrapolating the decline.
- Latest FCF margin was -214.3%; scenarios use normalized positive margins for a going-concern DCF.

- _base: model equity value is negative after net debt (-579,633,059); showing $-2.32/sh._
- _bull: model equity value is negative after net debt (-461,547,058); showing $-1.85/sh._
- _bear: model equity value is negative after net debt (-607,878,518); showing $-2.43/sh._

### Base-case projected FCF

- Year 1: revenue $69.88M, FCF $2.10M (PV $1.91M)
- Year 2: revenue $74.07M, FCF $2.22M (PV $1.84M)
- Year 3: revenue $78.51M, FCF $2.36M (PV $1.77M)
- Year 4: revenue $83.23M, FCF $2.50M (PV $1.71M)
- Year 5: revenue $88.22M, FCF $2.65M (PV $1.64M)
- Terminal value $36.17M (PV $22.46M)

## Put opportunities (heuristic) [S3]
- Expiration: 2026-08-21 (DTE 31)
- Candidates: 0
- ATM IV (est.): 80.9%
- IV rank: — (1 local samples)
- HV rank (20d realized): 6.1%


_Note: Delta band approximated via % OTM when greeks are unavailable; IV rank needs ~20+ local daily IV samples (have 1); run the options screen over time to build history.; HV rank is realized-vol rank (20d HV vs ~1y); useful when IV history is thin._

## Research loop (think → act)

1. _heuristic_ — Coverage looks adequate for this pass; stopping iterative loop.

## Sources

- **[S1]** UUUU fundamentals (yfinance)
  - Energy Fuels Inc: price=12.35, rev=65922000.0, fcf=-141273000.0, shares=249919146.0, rev_cagr=0.7399355982144395, ROIC=-0.07845383396530209, FCF yield=-0.045771237745452775
- **[S2]** UUUU DCF valuation (dcf)
  - Base share price=-2.319282330772069, bull=-1.8467855109534992, bear=-2.4323007189325736
- **[S3]** UUUU put screen (yfinance_options)
  - Expiration 2026-08-21 (DTE 31): 0 candidates; IV=0.8085956640624999, IV rank=None, HV rank=0.060543710579782355. Delta band approximated via % OTM when greeks are unavailable; I…

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
