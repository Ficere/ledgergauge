# MapleLeaf BioFoundry Financial Model & Revenue Accounting (Debt-Financed)

**Date:** 2026-05-29
**Unit:** kUSD (thousands of USD)
**This is an internal feasibility projection, not investment advice. Inputs are editable assumptions (marked clearly); computed results follow from the formulas in `scripts/fin_model.py`.**

> **Worked example notice:** Every name and number in this report is fictional and generated
> from `assets/sample_input.json`. MapleLeaf BioFoundry does not exist. The report is shipped
> only to show what an end-to-end LedgerGauge deliverable looks like.

> **Caliber note:** This report uses a full debt-financing caliber — the build-out CapEx is
> modeled as a single 8400 kUSD loan repaid by equal monthly installments over 8 years — to
> stress-test short-term repayment capacity. Layers A (recurring) and B (co-development) are
> identical across both scenarios; the **only** divergence is how the high-variance Layer C
> (IP/licensing) is recognized: **conservative = probability-weighted (35%)**, **optimistic =
> full recognition**.

---

## 1. Financing & Repayment Plan (shared)

| Item | Value |
|------|------:|
| Principal | 8,400 kUSD |
| Annual rate | 3.20% |
| Term | 8 years (96 months) |
| Repayment style | Equal monthly installment (本息等额) |
| Monthly payment | 99.29 kUSD |
| Annual payment | 1,191.52 kUSD |
| Total payment over term | 9,532.16 kUSD |
| Total interest | 1,132.16 kUSD |

Year-by-year schedule:

| Year | Opening balance | Payment | Principal | Interest | Closing balance |
|---:|---:|---:|---:|---:|---:|
| 1 | 8,400.00 | 1,191.52 | 936.37 | 255.15 | 7,463.63 |
| 2 | 7,463.63 | 1,191.52 | 966.78 | 224.74 | 6,496.84 |
| 3 | 6,496.84 | 1,191.52 | 998.18 | 193.34 | 5,498.67 |
| 4 | 5,498.67 | 1,191.52 | 1,030.59 | 160.93 | 4,468.08 |
| 5 | 4,468.08 | 1,191.52 | 1,064.06 | 127.46 | 3,404.02 |
| 6 | 3,404.02 | 1,191.52 | 1,098.61 | 92.91 | 2,305.41 |
| 7 | 2,305.41 | 1,191.52 | 1,134.29 | 57.23 | 1,171.12 |
| 8 | 1,171.12 | 1,191.52 | 1,171.12 | 20.40 | 0.00 |

The annual payment is a hard cash outflow of ~1,191.52 kUSD every year regardless of profit.
Note that interest is small and shrinking (255 → 20 kUSD); the heavy rigid outflow is the
**principal**, which grows from 936 to 1,171 kUSD as interest gives way to amortization.

## 2. Revenue Layering & Recognition Cadence

| Layer | Definition | Recognition |
|------|------|------|
| **A — Recurring** | Standard foundry/assay services, predictable utilization | Booked in full as forecast |
| **B — Co-development** | Milestone-based shared programs, medium risk | Risk-adjusted; not over-fronted |
| **C — IP / licensing** | High unit price (1,100 kUSD), low frequency, high variance | **The only divergence:** conservative = prob-weighted (35%), optimistic = full |

Recognized revenue lines (kUSD):

| Year | Layer A | Layer B | Layer C (conservative) | Layer C (optimistic) |
|---:|---:|---:|---:|---:|
| 1 | 620 | 0 | 0 | 0 |
| 2 | 1,480 | 60 | 0 | 0 |
| 3 | 2,510 | 180 | 385 | 1,100 |
| 4 | 3,360 | 340 | 770 | 2,200 |
| 5 | 3,980 | 520 | 770 | 2,200 |
| 6 | 4,420 | 640 | 1,155 | 3,300 |
| 7 | 4,710 | 760 | 1,155 | 3,300 |
| 8 | 4,880 | 880 | 1,155 | 3,300 |

**Layer-A safety-floor test:** by Year 4, Layer A alone (3,360 kUSD) already exceeds the annual
debt payment (1,191.52 kUSD), i.e. the recurring base covers repayment ~2.8× before any
co-development or licensing income. This is the single most important survival property.

**Concentration check:** in the peak optimistic year (Year 8), Layer C contributes 3,300 of
9,060 kUSD ≈ 36% of revenue — a meaningful concentration that justifies modeling it as the
swing variable rather than a stable base.

## 3. Layered Gross-Margin Calibration

| Layer | Gross margin | Rationale / benchmark |
|------|---:|------|
| **A — Recurring services** | 48% | In line with contract-research / lab-services gross margins disclosed by listed CROs such as [Charles River Laboratories](https://ir.criver.com/) and [Medpace](https://investor.medpace.com/) (services GM typically ~30–50%). |
| **B — Co-development** | 58% | Shared-program economics carry higher margin than pure services but below pure IP. |
| **C — IP / licensing** | 82% | Licensing income is near-pure margin; comparable to royalty/licensing lines reported by IP-heavy biotechs (e.g. disclosures in [Royalty Pharma filings](https://www.royaltypharma.com/investors/)). |

Blended gross margin lands around 53–55% (conservative) and 60–62% (optimistic), with the
spread driven entirely by the higher weight of the 82%-margin Layer C in the optimistic case.

## 4. Dual-Caliber Projection

### 4.1 Conservative (Layer-C probability-weighted)

| Year | Revenue | Gross profit | Cash opex | Depr. | Interest | Net income | FCF | Cum. FCF |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 620 | 298 | 760 | 560 | 255 | −1,278 | −1,685 | −1,685 |
| 2 | 1,540 | 745 | 1,080 | 880 | 225 | −1,440 | −1,572 | −3,257 |
| 3 | 3,075 | 1,625 | 1,480 | 1,040 | 193 | −1,088 | −1,123 | −4,381 |
| 4 | 4,470 | 2,441 | 1,780 | 1,040 | 161 | −540 | −600 | −4,980 |
| 5 | 5,270 | 2,843 | 1,940 | 1,040 | 127 | −264 | −328 | **−5,309** |
| 6 | 6,215 | 3,440 | 2,040 | 1,040 | 93 | +267 | +161 | −5,147 |
| 7 | 6,625 | 3,649 | 2,110 | 1,040 | 57 | +441 | +327 | −4,821 |
| 8 | 6,915 | 3,800 | 2,150 | 1,040 | 20 | +590 | +444 | −4,377 |

### 4.2 Optimistic (Layer-C full recognition)

| Year | Revenue | Gross profit | Cash opex | Depr. | Interest | Net income | FCF | Cum. FCF |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 620 | 298 | 760 | 560 | 255 | −1,278 | −1,685 | −1,685 |
| 2 | 1,540 | 745 | 1,080 | 880 | 225 | −1,440 | −1,572 | −3,257 |
| 3 | 3,790 | 2,211 | 1,480 | 1,040 | 193 | −502 | −573 | **−3,830** |
| 4 | 5,900 | 3,614 | 1,780 | 1,040 | 161 | +633 | +537 | −3,293 |
| 5 | 6,700 | 4,016 | 1,940 | 1,040 | 127 | +909 | +844 | −2,449 |
| 6 | 8,360 | 5,199 | 2,040 | 1,040 | 93 | +2,026 | +1,884 | −564 |
| 7 | 8,770 | 5,408 | 2,110 | 1,040 | 57 | +2,200 | +2,086 | +1,521 |
| 8 | 9,060 | 5,559 | 2,150 | 1,040 | 20 | +2,348 | +2,203 | +3,724 |

### 4.3 Side-by-side key metrics

| Metric | Conservative | Optimistic |
|--------|---:|---:|
| Year-8 revenue | 6,915 | 9,060 |
| Accounting breakeven (net income > 0) | Year 6 | Year 4 |
| FCF breakeven (annual FCF > 0) | Year 6 | Year 4 |
| Payback (cumulative FCF > 0) | Not within 8 yrs | Year 7 |
| Cumulative net income (8 yrs) | −3,311 | +4,897 |
| Cash-flow trough | Year 5: −5,309 | Year 3: −3,830 |

> One-line interpretation: the entire spread between these two outcomes is driven by Layer-C
> execution (how much licensing income actually closes and gets recognized). Reality will sit
> somewhere between the two columns — neither is a forecast on its own.

## 5. Sensitivity Analysis

Interest is the smallest rigid outflow and it shrinks every year, so a rate shock barely moves
the picture. The dangerous levers are operating margin and licensing execution. One-at-a-time
perturbation on the conservative trough-year FCF (Year 5 baseline = −328 kUSD):

| Variable | Shock | Trough-year FCF | Δ vs baseline | Rank |
|------|------|---:|---:|:--:|
| Layer-A gross margin | −5 pp | −527 | **−199** | 1 (most severe) |
| IP recognition probability | −10 pp | −509 | −180 | 2 |
| Financing rate | +100 bp | −375 | −47 | 3 (least severe) |

The ranking confirms the intuition: a 5-point erosion in the recurring-services margin hurts
the cash trough four times more than a full 100 bp rate hike. Protect Layer-A margin first.

## 6. Conclusions & Pitfall Warnings

1. **Realistic range is bounded by the two scenarios.** The platform turns cash-positive on an
   annual basis between Year 4 (optimistic) and Year 6 (conservative); cumulative payback lands
   at Year 7 in the optimistic case and beyond the 8-year window in the conservative case.
2. **The two boulders are depreciation + principal repayment.** Interest is minor; the real
   weight on cash is the ~1,000–1,170 kUSD annual principal plus ~1,040 kUSD depreciation. Both
   are rigid and independent of profit.
3. **Layer A is the lifeline.** It must be large and solid: by Year 4 it alone covers the annual
   debt payment several times over. Sensitivity shows its margin is the most fragile lever.
4. **Levers to de-risk:** down-size or phase the build-out CapEx; **optimize the capital
   structure** to secure favorable terms; and convert Layers B and C from lumpy, high-variance
   income into predictable recurring revenue wherever contractually possible.

---

> **Sources & caliber:** revenue / utilization / cost / depreciation come from the fictional
> capacity model in `assets/sample_input.json`; repayment is computed by the equal-installment
> formula in `scripts/fin_model.py`; layered gross margins are benchmarked to public CRO and
> royalty-company disclosures cited above. All inputs are editable assumptions, not market
> promises. This is an internal feasibility projection generated for demonstration only — **not
> investment advice**, and MapleLeaf BioFoundry is entirely fictional.
