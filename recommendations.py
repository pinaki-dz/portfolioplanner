from config import RISK_ALLOCATIONS, AGE_EQUITY_REDUCTIONS, MIN_EQUITY, MAX_EQUITY

def get_age_band(age):
    if age < 40:
        return "Under 40"
    if age < 50:
        return "40-49"
    if age < 60:
        return "50-59"
    return "60+"

def build_recommendation(age, risk_appetite, investible_portfolio):
    base = RISK_ALLOCATIONS[risk_appetite].copy()
    age_band = get_age_band(age)
    equity_reduction = AGE_EQUITY_REDUCTIONS[age_band]

    final_equity = max(MIN_EQUITY, min(MAX_EQUITY, base["Equity"] - equity_reduction))
    debt_increase = base["Equity"] - final_equity
    final = {
        "Equity": final_equity,
        "Debt": base["Debt"] + debt_increase,
        "Cash": base["Cash"],
    }
    amounts = {
        asset: investible_portfolio * allocation / 100
        for asset, allocation in final.items()
    }
    return {
        "risk_appetite": risk_appetite,
        "age_band": age_band,
        "base": base,
        "age_equity_reduction": equity_reduction,
        "final": final,
        "amounts": amounts,
        "investible_portfolio": investible_portfolio,
    }
