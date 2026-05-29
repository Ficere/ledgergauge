# Dual-Caliber Projection: Accounting P&L vs. Free Cash Flow

A debt-financed build-out must be judged on **both** calibers, because each hides what the
other reveals.

## Definitions

| Item | Accounting caliber | Cash caliber (FCF) |
|------|--------------------|--------------------|
| Depreciation / amortization | **Subtracted** (non-cash expense) | **Added back** (not a cash outflow) |
| Interest | Subtracted (finance cost) | Subtracted (real cash) |
| Principal repayment | **Not** subtracted (balance-sheet movement) | **Subtracted** (real cash outflow) |
| Working-capital change | Not modeled here | Subtracted (≈ 5% of YoY revenue change) |

## Formulas

```
gross_profit          = Σ ( layer_revenue × layer_gross_margin )
accounting_net_income = gross_profit − cash_opex − depreciation − interest
free_cash_flow (FCF)  = accounting_net_income + depreciation − principal_repaid − wc_change
cumulative_FCF[t]     = Σ FCF[1..t]
```

## The "two boulders"

In a capital-intensive, debt-financed platform the two largest fixed outflows are usually:

1. **Depreciation** — large because of the heavy up-front CapEx; it crushes *accounting* profit
   for years even though it is non-cash.
2. **Principal repayment** — drains *cash* every year regardless of profit.

Interest is often the *smallest* of the rigid outflows when the rate is favorable — so do not
over-focus on interest. The binding constraints are principal and depreciation.

## Markers to report

For each scenario, extract and state:

- **Accounting breakeven year** — first year net income > 0
- **FCF breakeven year** — first year single-year FCF > 0
- **Payback year** — first year cumulative FCF > 0 (may be "not within horizon")
- **Cumulative net income** over the horizon
- **Cash-flow trough** — the most-negative cumulative-FCF year and its value

A platform can be accounting-profitable years before it is cash-recovered; always show both.
