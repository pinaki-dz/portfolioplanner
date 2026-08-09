APP_VERSION = "1.0.1"

RISK_ALLOCATIONS = {
    "Conservative": {"Equity": 40, "Debt": 50, "Cash": 10},
    "Moderate": {"Equity": 60, "Debt": 35, "Cash": 5},
    "Aggressive": {"Equity": 80, "Debt": 15, "Cash": 5},
}

AGE_EQUITY_REDUCTIONS = {
    "Under 40": 0,
    "40-49": 5,
    "50-59": 10,
    "60+": 15,
}

MIN_EQUITY = 20
MAX_EQUITY = 90
