---
name: ledgergauge
description: "Build a debt-financed feasibility model and write the matching report for any capital-intensive service or R&D platform (shared labs, CRO/foundry platforms, pilot facilities, equipment-heavy ventures). Runs a debt-repayment stress test, layers revenue into recurring / co-development / high-variance licensing, projects dual-caliber accounting P&L and free cash flow, builds conservative-vs-optimistic scenarios that differ only in how the volatile licensing layer is recognized, and runs one-at-a-time sensitivity on the cash-flow trough. Use when the user asks for a platform/facility financial model, capacity-revenue-profit projection, payback/breakeven analysis, debt-financing pressure test, scenario or sensitivity analysis, or a feasibility report with a build-out CapEx funded by borrowing."
license: MIT
metadata:
  author: ledgergauge
  version: '1.0'
---

# LedgerGauge — Debt-Financed Platform Feasibility Model

A reproducible workflow for modeling a capital-intensive service/R&D platform whose
build-out is funded by debt, and for writing the feasibility report that goes with it.
It answers two distinct questions side by side:

- **Can it create value?** (accounting profit & loss)
- **Can it survive repayment?** (free cash flow under the debt schedule)

## When to Use This Skill

Use this skill when the user wants any of:

- A financial / feasibility model for a shared lab, foundry, CRO platform, pilot plant, or other equipment-heavy venture
- A capacity → revenue → profit projection over a multi-year horizon
- A **debt-financing pressure test** (one-time borrowing, equal-installment repayment)
- Breakeven / payback / cash-trough analysis
- **Scenario analysis** (conservative vs. optimistic) and **sensitivity analysis**
- A written report that pairs the numbers with structured commentary

Do **not** use it for: equity-only DCF valuation, personal budgeting, public-market security analysis, or accounting bookkeeping.

## Core Method (5 steps)

### Step 1 — Debt repayment stress test

Model the build-out CapEx as a **single up-front loan**, repaid by **equal installments**
(equal monthly payment) over the horizon. Produce the per-year schedule: opening balance,
payment, principal repaid (rising), interest paid (falling), closing balance.

> **Sensitive-data rule:** describe the financing only by its *financial parameters*
> (principal, rate, term, repayment style). Never attribute the favorable terms to any
> specific funding programme, government channel, or counterparty. If a rate is unusually
> low, express it only as "favorable rate" or "optimized capital structure" — never speculate
> about *why* in the deliverable.

### Step 2 — Layer the revenue

Re-group all revenue into three layers by predictability, then recognize each appropriately:

| Layer | Nature | Recognition |
|-------|--------|-------------|
| **A — Recurring service** | High-predictability standard services; the cash-flow ballast | Full, as earned |
| **B — Co-development** | Milestone-driven joint projects | Deterministic fee + **risk-adjusted** milestone — never book the full signed value up front |
| **C — IP / licensing** | High-variance, lumpy big-ticket deals | **This is the only layer that differs between scenarios** (see Step 4) |

Read `references/revenue_layers.md` for layer definitions, recognition discipline, and the
anti-pattern of over-fronting milestone/licensing revenue.

### Step 3 — Dual-caliber projection

For each year compute both calibers from the same inputs:

```
Accounting net income = gross_profit − cash_opex − depreciation − interest
Free cash flow (FCF)  = net_income + depreciation − principal_repaid − working_capital_change
```

- Accounting caliber **includes** depreciation, **excludes** principal.
- Cash caliber **excludes** depreciation (non-cash), **includes** principal repayment, and adds working-capital change.

The two heaviest fixed outflows in a debt-financed build-out are usually **depreciation**
(erodes accounting profit) and **principal repayment** (drains cash) — the "two boulders."
Read `references/dual_caliber.md`.

### Step 4 — Scenarios (differ ONLY in the licensing layer)

Build the report as **one platform under two recognition calibers**, not as two rival plans:

- **Conservative** — Layer C recognized **probability-weighted** (e.g. 30–40% of nominal).
- **Optimistic** — Layer C recognized **at full value** (deals land on time and in full).

Layers A and B, the debt schedule, the cost/depreciation structure, and the sensitivity
framework are **identical** across scenarios. The entire gap between the two ends is driven
by whether the lumpy licensing deals land. Read `references/scenarios.md`.

### Step 5 — Sensitivity on the cash trough

One-at-a-time perturbations on the trough-year FCF: Layer-A gross margin (−5pp), IP
recognition probability (−10pp), financing rate (+100bp), milestone confirmation ratio.
The variable with the largest impact is the one to manage first. Read `references/sensitivity.md`.

## Engine

`scripts/fin_model.py` is a **dependency-free Python 3** engine that performs all five steps.
Drive it from a single JSON config:

```bash
python scripts/fin_model.py --input assets/sample_input.json --output result.json
```

It returns the amortization schedule, every scenario's full year-by-year table (with breakeven,
payback, cumulative net income, and cash-trough markers), and the sensitivity table.
The bundled `assets/sample_input.json` is a **fully fictional** illustrative case
("MapleLeaf BioFoundry") — copy it, replace the figures with the user's real assumptions,
and re-run.

## Producing the Report

After running the engine, write the report following `references/report_template.md`. Standard sections:

1. Financing & repayment plan (shared by both scenarios)
2. Revenue layering & recognition cadence
3. Layered gross-margin calibration with industry benchmarks
4. Dual-caliber projection — one table per scenario + a side-by-side key-metrics summary
5. Sensitivity analysis
6. Conclusions & pitfall warnings (CapEx down-sizing, capital-structure optimization, making B/C recurring)

### Output discipline

- **Value pricing, not cost-plus** — price services by the value delivered and cross-check against real public benchmarks; do not invent client prices with no basis.
- **Milestone discipline** — never book a full signed contract in year one; risk-adjust.
- **No leaked financing specifics** — see the sensitive-data rule in Step 1.
- **Mark assumptions clearly** — flag every input as an editable assumption, not a market promise; end with a "not investment advice" note.
- **Cite benchmarks with real URLs** when comparing gross/net margins to comparable companies.

## Examples

```
Build me a debt-financed feasibility model for a shared bio-foundry: 8M build-out borrowed at 3.2%, repaid equal-installment over 8 years, with recurring + co-development + occasional licensing revenue. Give me conservative and optimistic scenarios.
```

```
Run a debt-repayment stress test on this platform and tell me the breakeven year, the payback year, and the cash-flow trough under both a probability-weighted and a full-recognition licensing case.
```

```
Take my capacity-revenue numbers, layer them into recurring / co-dev / IP, project accounting profit and free cash flow side by side, and write the feasibility report with a sensitivity analysis on the trough year.
```
