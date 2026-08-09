import streamlit as st

def get_user_inputs():
    st.sidebar.header("Your Information")
    name = st.sidebar.text_input("Name", value="")
    age = st.sidebar.number_input("Current Age", min_value=18, max_value=80, value=50, step=1, format="%d")
    retirement_age = st.sidebar.number_input("Target Retirement Age", min_value=19, max_value=85, value=60, step=1, format="%d")

    st.sidebar.header("Financial Information")
    portfolio_value = st.sidebar.number_input(
        "Current Portfolio Value (₹)", min_value=0.0, value=1000000.0,
        step=100000.0, format="%.0f",
        help="Total financial assets you want the planner to consider."
    )
    annual_contribution = st.sidebar.number_input(
        "Annual Investment / Contribution (₹)", min_value=0.0, value=300000.0,
        step=10000.0, format="%.0f"
    )
    expected_return = st.sidebar.number_input(
        "Expected Annual Return (%)", min_value=0.0, max_value=30.0,
        value=9.0, step=0.5, format="%.1f"
    )
    inflation = st.sidebar.number_input(
        "Expected Inflation (%)", min_value=0.0, max_value=20.0,
        value=6.0, step=0.5, format="%.1f"
    )

    st.sidebar.header("Risk Information")
    risk_appetite = st.sidebar.selectbox(
        "Risk Appetite", ["Conservative", "Moderate", "Aggressive"], index=1
    )
    emergency_fund = st.sidebar.number_input(
        "Emergency Fund / Cash Reserve (₹)", min_value=0.0, value=0.0,
        step=10000.0, format="%.0f",
        help="Kept outside the investible portfolio and excluded from allocation and growth projection."
    )

    return {
        "name": name.strip(),
        "age": int(age),
        "retirement_age": int(retirement_age),
        "portfolio_value": float(portfolio_value),
        "annual_contribution": float(annual_contribution),
        "expected_return": float(expected_return),
        "inflation": float(inflation),
        "risk_appetite": risk_appetite,
        "emergency_fund": float(emergency_fund),
    }

def validate_inputs(inputs):
    errors = []
    if inputs["retirement_age"] <= inputs["age"]:
        errors.append("Target retirement age must be greater than current age.")
    if inputs["portfolio_value"] < 0:
        errors.append("Portfolio value cannot be negative.")
    if inputs["annual_contribution"] < 0:
        errors.append("Annual contribution cannot be negative.")
    if inputs["emergency_fund"] > inputs["portfolio_value"]:
        errors.append("Emergency fund cannot be greater than the current portfolio value.")
    if not 0 <= inputs["expected_return"] <= 30:
        errors.append("Expected return must be between 0% and 30%.")
    if not 0 <= inputs["inflation"] <= 20:
        errors.append("Inflation must be between 0% and 20%.")
    return errors
