#!/usr/bin/env python3
"""
LedgerGauge — debt-financed platform financial model engine.

Pure-Python (no third-party deps). Computes, for a capital-intensive
service/R&D platform funded entirely by debt:

  1. Equal-installment amortization schedule
  2. Three-layer revenue recognition (recurring / co-development / IP licensing)
  3. Dual-caliber projection: accounting P&L and free cash flow (FCF)
  4. Multiple scenarios that differ ONLY in how the high-variance IP layer
     is recognized (e.g. probability-weighted vs. full recognition)
  5. One-at-a-time sensitivity on the cash-flow trough

Run:
    python fin_model.py --input assets/sample_input.json --output result.json

All numbers in the sample input are FICTIONAL and for illustration only.
"""

import argparse
import json
import sys


# --------------------------------------------------------------------------
# 1. Debt amortization (equal installments)
# --------------------------------------------------------------------------
def amortization_schedule(principal, annual_rate, years):
    """Equal-installment (equal payment) monthly amortization, aggregated to years."""
    n_months = years * 12
    r = annual_rate / 12.0
    if r == 0:
        monthly = principal / n_months
    else:
        monthly = principal * (r * (1 + r) ** n_months) / ((1 + r) ** n_months - 1)

    rows = []
    bal = principal
    annual = monthly * 12.0
    for y in range(1, years + 1):
        open_bal = bal
        year_interest = 0.0
        year_principal = 0.0
        for _ in range(12):
            interest = bal * r
            princ = monthly - interest
            bal -= princ
            year_interest += interest
            year_principal += princ
        rows.append({
            "year": y,
            "open_balance": round(open_bal, 2),
            "annual_payment": round(annual, 2),
            "principal_paid": round(year_principal, 2),
            "interest_paid": round(year_interest, 2),
            "close_balance": round(max(bal, 0.0), 2),
        })
    return {
        "monthly_payment": round(monthly, 2),
        "annual_payment": round(annual, 2),
        "total_payment": round(annual * years, 2),
        "total_interest": round(annual * years - principal, 2),
        "schedule": rows,
    }


# --------------------------------------------------------------------------
# 2. Revenue layers
# --------------------------------------------------------------------------
def recognized_ip_revenue(ip_cfg, mode):
    """
    Recognize the high-variance IP/licensing layer under a given mode.
      mode == "weighted": multiply nominal by probability
      mode == "full":     recognize 100%
    ip_cfg: {"unit_price": float, "projects": [per-year counts], "probability": float}
    Returns a per-year list (length = len(projects)).
    """
    unit = ip_cfg["unit_price"]
    projects = ip_cfg["projects"]
    if mode == "full":
        factor = 1.0
    else:
        factor = ip_cfg.get("probability", 0.3)
    return [round(unit * p * factor, 2) for p in projects]


# --------------------------------------------------------------------------
# 3. Dual-caliber projection for one scenario
# --------------------------------------------------------------------------
def project_scenario(cfg, amort, ip_mode):
    years = cfg["years"]
    A = cfg["layer_a_recurring"]            # per-year recurring revenue
    B = cfg["layer_b_codev"]               # per-year co-development revenue
    ip = recognized_ip_revenue(cfg["layer_c_ip"], ip_mode)

    gmA = cfg["gross_margin"]["a"]
    gmB = cfg["gross_margin"]["b"]
    gmC = cfg["gross_margin"]["c"]

    opex = cfg["cash_opex"]                 # per-year cash operating expense
    depr = cfg["depreciation"]             # per-year depreciation/amortization (non-cash)
    wc_ratio = cfg.get("working_capital_ratio", 0.05)
    sched = amort["schedule"]

    out = []
    cum_fcf = 0.0
    prev_rev = 0.0
    for i in range(years):
        rev = A[i] + B[i] + ip[i]
        gp = A[i] * gmA + B[i] * gmB + ip[i] * gmC
        cogs = rev - gp
        gm_pct = gp / rev if rev else 0.0
        interest = sched[i]["interest_paid"]
        principal = sched[i]["principal_paid"]

        net_income = gp - opex[i] - depr[i] - interest          # accounting caliber
        wc_change = (rev - prev_rev) * wc_ratio
        fcf = net_income + depr[i] - principal - wc_change       # cash caliber
        cum_fcf += fcf
        prev_rev = rev

        out.append({
            "year": i + 1,
            "revenue": round(rev, 2),
            "cogs": round(cogs, 2),
            "gross_profit": round(gp, 2),
            "gross_margin": round(gm_pct, 4),
            "cash_opex": round(opex[i], 2),
            "depreciation": round(depr[i], 2),
            "interest": round(interest, 2),
            "net_income": round(net_income, 2),
            "principal_repaid": round(principal, 2),
            "wc_change": round(wc_change, 2),
            "fcf": round(fcf, 2),
            "cum_fcf": round(cum_fcf, 2),
        })

    def first_positive(key):
        for row in out:
            if row[key] > 0:
                return row["year"]
        return None

    return {
        "rows": out,
        "net_income_breakeven_year": first_positive("net_income"),
        "fcf_breakeven_year": first_positive("fcf"),
        "payback_year": first_positive("cum_fcf"),
        "cumulative_net_income": round(sum(r["net_income"] for r in out), 2),
        "final_cum_fcf": round(out[-1]["cum_fcf"], 2),
        "cash_trough_year": min(out, key=lambda r: r["cum_fcf"])["year"],
        "cash_trough_value": round(min(r["cum_fcf"] for r in out), 2),
    }


# --------------------------------------------------------------------------
# 4. Sensitivity on the cash-flow trough (one-at-a-time)
# --------------------------------------------------------------------------
def sensitivity(cfg, amort, base_scenario_mode, trough_year):
    """Perturb single variables, report effect on the trough-year FCF."""
    base = project_scenario(cfg, amort, base_scenario_mode)
    base_fcf = next(r["fcf"] for r in base["rows"] if r["year"] == trough_year)
    results = [{"variable": "baseline", "delta": "—",
                "trough_fcf": base_fcf, "vs_base": 0.0}]

    # a) Layer-A gross margin -5pp
    c = json.loads(json.dumps(cfg))
    c["gross_margin"]["a"] = max(0.0, c["gross_margin"]["a"] - 0.05)
    s = project_scenario(c, amort, base_scenario_mode)
    f = next(r["fcf"] for r in s["rows"] if r["year"] == trough_year)
    results.append({"variable": "Layer-A gross margin", "delta": "-5pp",
                    "trough_fcf": round(f, 2), "vs_base": round(f - base_fcf, 2)})

    # b) IP probability -10pp (only meaningful for weighted mode)
    c = json.loads(json.dumps(cfg))
    c["layer_c_ip"]["probability"] = max(0.0, c["layer_c_ip"].get("probability", 0.3) - 0.10)
    s = project_scenario(c, amort, "weighted")
    f = next(r["fcf"] for r in s["rows"] if r["year"] == trough_year)
    results.append({"variable": "IP recognition probability", "delta": "-10pp",
                    "trough_fcf": round(f, 2), "vs_base": round(f - base_fcf, 2)})

    # c) Interest rate +100bp
    c = json.loads(json.dumps(cfg))
    amort2 = amortization_schedule(cfg["principal"], cfg["annual_rate"] + 0.01, cfg["years"])
    s = project_scenario(c, amort2, base_scenario_mode)
    f = next(r["fcf"] for r in s["rows"] if r["year"] == trough_year)
    results.append({"variable": "Financing rate", "delta": "+100bp",
                    "trough_fcf": round(f, 2), "vs_base": round(f - base_fcf, 2)})

    return results


# --------------------------------------------------------------------------
# Driver
# --------------------------------------------------------------------------
def run(cfg):
    amort = amortization_schedule(cfg["principal"], cfg["annual_rate"], cfg["years"])
    scenarios = {}
    for name, mode in cfg.get("scenarios", {"conservative": "weighted",
                                            "optimistic": "full"}).items():
        scenarios[name] = project_scenario(cfg, amort, mode)

    base_mode = cfg.get("sensitivity_base", "weighted")
    base_scn = next(s for n, s in scenarios.items()
                    if cfg.get("scenarios", {}).get(n) == base_mode)
    sens = sensitivity(cfg, amort, base_mode, base_scn["cash_trough_year"])

    return {"amortization": amort, "scenarios": scenarios, "sensitivity": sens}


def main():
    ap = argparse.ArgumentParser(description="LedgerGauge financial model engine")
    ap.add_argument("--input", required=True, help="Path to config JSON")
    ap.add_argument("--output", default=None, help="Path to write result JSON")
    args = ap.parse_args()

    with open(args.input, "r", encoding="utf-8") as fh:
        cfg = json.load(fh)

    result = run(cfg)
    text = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as fh:
            fh.write(text)
        print(f"Wrote {args.output}")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
