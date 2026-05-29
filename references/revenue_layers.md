# Revenue Layering & Recognition Discipline

Re-group every revenue stream into three layers by **predictability** and **business nature**.
The total per year must reconcile with the underlying capacity model (rounding aside).

## Layer A — Recurring service revenue

- **Nature:** standard, high-predictability services billed repeatedly; this is the cash-flow ballast.
- **Examples (illustrative):** design packages, construct/assembly, screening, process optimization, analytics, purification, formulation, membership/subscription.
- **Recognition:** full, as earned. Quantity × utilization ramp × unit price.
- **Why it matters:** Layer A is usually the single largest base, so its gross margin is typically the **most sensitive** variable in the whole model. Make it large and solid first.

### Safety-floor test

Ask: can Layer A alone cover "cash opex + annual debt service"?

```
Cash rigid outflow (year t) = cash_opex[t] + annual_debt_payment
Layer-A cash gross profit   = layer_a_revenue[t] × gross_margin_a
```

If Layer-A cash gross profit < rigid outflow, the platform depends on B/C to close the gap
in early years. State the year at which Layer A finally covers the rigid outflow on its own.

## Layer B — Co-development revenue (milestone-driven)

- **Nature:** joint development / technology-transfer engagements with milestone payments.
- **Recognition discipline — risk-adjust, never over-front:**

```
recognized = deterministic_fee_share × nominal
           + milestone_share × nominal × milestone_probability
```

  A common prudent split is deterministic 60% + milestone 40% × ~55% probability.
- **Anti-pattern:** booking the entire signed contract value in the signing year. Over-fronting
  milestone or licensing revenue (e.g. a single mega-deal carrying the whole year, or a single
  pipeline being 95%+ of revenue) is exactly what makes a model fragile and non-credible.

## Layer C — IP / licensing revenue (high variance)

- **Nature:** lumpy, occasional big-ticket IP transfers or licenses. These appear only after the
  platform matures and are inherently unpredictable in timing and size.
- **Recognition is the ONLY thing that changes between scenarios:**
  - Conservative: `recognized = unit_price × projects × probability` (probability ~0.3–0.4).
  - Optimistic: `recognized = unit_price × projects` (full).
- **Concentration check:** even under full recognition, verify Layer C stays below a ~30%
  share of total revenue in any single year; if a base business is large enough, a lumpy deal
  should not dominate the mix.

## Reconciliation rule

Always show that A + B + C per year equals the capacity-model revenue line (within rounding).
Treat C as an **upside lever**, never as a guaranteed cash flow.
