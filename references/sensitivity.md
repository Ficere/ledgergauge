# Sensitivity Analysis on the Cash-Flow Trough

Because fixed outflows (depreciation + debt service) are huge relative to early-year cash
generation, the platform is highly sensitive to a few variables. Run **one-at-a-time**
perturbations and measure the effect on the **trough-year FCF** (the most binding moment).

## Standard perturbations

| Variable | Perturbation | Why it matters |
|----------|--------------|----------------|
| **Layer-A gross margin** | −5pp | Layer A has the largest revenue base, so margin moves dominate cash |
| **IP recognition probability** | −10pp | Tests how much the upside depends on lumpy deals (conservative caliber) |
| **Financing rate** | +100bp | Tests interest exposure (usually modest when the rate is low) |
| **Milestone confirmation ratio** | down a step | Tests Layer-B fragility |

## How to run

Use the engine's sensitivity block (`scripts/fin_model.py` returns it automatically), or
perturb a copied config and re-run. Report a table:

| Variable | Δ | Trough-year FCF | vs. baseline |
|----------|---|-----------------|--------------|
| baseline | — | … | 0 |
| Layer-A gross margin | −5pp | … | … |
| IP recognition probability | −10pp | … | … |
| Financing rate | +100bp | … | … |

## Interpretation rules

- Rank variables by absolute impact; the **largest** is the one to manage first.
- In most capacity-driven platforms, **Layer-A gross margin** ranks first (largest base),
  IP probability second, financing rate a distant third.
- Tie the ranking back to the conclusions: "make Layer A large and solid" is usually the
  primary lever, with Layer C as the upside engine.

## Interest-rate note

When the financing rate is already low, total interest over the horizon is a small slice of
the rigid outflows. State plainly that the binding constraints are **principal repayment and
depreciation**, not interest — so a rate shock, while unwelcome, is not the dominant risk.
