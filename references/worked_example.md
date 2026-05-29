# Worked Example — "MapleLeaf BioFoundry" (fully fictional)

This walkthrough uses the bundled `assets/sample_input.json`. Every number is **invented**
for teaching purposes and represents no real organization. Unit: kUSD (thousands).

## Inputs (fictional)

- Build-out CapEx (borrowed): **8,400**
- Annual rate: **3.2%**, equal-installment, **8-year** term
- Layer A (recurring), Y1–Y8: 620 / 1,480 / 2,510 / 3,360 / 3,980 / 4,420 / 4,710 / 4,880
- Layer B (co-dev), Y1–Y8: 0 / 60 / 180 / 340 / 520 / 640 / 760 / 880
- Layer C (IP): unit price **1,100**, projects Y3–Y8 = 1 / 2 / 2 / 3 / 3 / 3, probability **35%**
- Gross margins: A 48% · B 58% · C 82%
- Cash opex Y1–Y8: 760 / 1,080 / 1,480 / 1,780 / 1,940 / 2,040 / 2,110 / 2,150
- Depreciation Y1–Y8: 560 / 880 / 1,040 (×6)
- Working-capital change: 5% of YoY revenue change

## Run

```bash
python scripts/fin_model.py --input assets/sample_input.json --output result.json
```

## Headline results (from the engine)

- Monthly payment **99.29**, annual payment **1,191.52**, total interest over 8 yrs **1,132.16**.

| Metric | Conservative (35% weighted) | Optimistic (full) |
|--------|-----------------------------|--------------------|
| Accounting breakeven | **Y6** | **Y4** |
| FCF breakeven | **Y6** | **Y4** |
| Payback (cum. FCF > 0) | **not within 8 yrs** | **Y7** |
| Cumulative net income | **−3,311** | **+4,897** |
| Final cumulative FCF | **−4,377** | **+3,724** |
| Cash-flow trough | **Y5 (−5,309)** | **Y3 (−3,830)** |

## Sensitivity (effect on trough-year FCF, conservative caliber)

| Variable | Δ | Effect on trough FCF |
|----------|---|----------------------|
| Layer-A gross margin | −5pp | **−199** (largest) |
| IP recognition probability | −10pp | −180 |
| Financing rate | +100bp | −47 (smallest) |

## Reading

Same platform, same debt and cost structure — the only difference is whether the lumpy IP
deals are booked at 35% or 100%. That alone moves the platform from "never recovered in 8
years" to "paid back in Y7." Layer-A gross margin is the top sensitivity, confirming the
"make Layer A large and solid" conclusion; interest is the smallest rigid lever.
