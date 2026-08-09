import streamlit as st
from inputs import get_user_inputs, validate_inputs
from calculations import build_projection
from recommendations import build_recommendation
from display import display_results

st.set_page_config(page_title="Portfolio Planner", page_icon="📊", layout="wide")
st.title("📊 Portfolio Planner")
st.caption("Version 1.0.1 • Educational planning tool")

inputs = get_user_inputs()

if st.button("Create Portfolio Plan", type="primary", use_container_width=True):
    errors = validate_inputs(inputs)
    if errors:
        for error in errors:
            st.error(error)
    else:
        investible_portfolio = inputs["portfolio_value"] - inputs["emergency_fund"]
        recommendation = build_recommendation(
            inputs["age"], inputs["risk_appetite"], investible_portfolio
        )
        projection = build_projection(
            investible_portfolio,
            inputs["annual_contribution"],
            inputs["expected_return"],
            inputs["inflation"],
            inputs["age"],
            inputs["retirement_age"],
        )
        display_results(inputs, recommendation, projection)
