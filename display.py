import pandas as pd
import plotly.express as px
import streamlit as st

def inr(value):
    return f"₹{value:,.0f}"

def display_results(inputs, recommendation, projection):
    investible_portfolio = recommendation["investible_portfolio"]

    st.divider()
    st.subheader("Portfolio Plan — At a Glance")
    summary_cols = st.columns(5)
    summary_cols[0].metric("Total Portfolio", inr(inputs["portfolio_value"]))
    summary_cols[1].metric("Emergency Fund", inr(inputs["emergency_fund"]))
    summary_cols[2].metric("Investible Portfolio", inr(investible_portfolio))
    summary_cols[3].metric("Projected Corpus", inr(projection["projected_value"]))
    summary_cols[4].metric("Years to Retirement", projection["years"])

    st.subheader("1. Profile")
    profile_cols = st.columns(5)
    profile_cols[0].metric("Name", inputs["name"] or "Not provided")
    profile_cols[1].metric("Current Age", inputs["age"])
    profile_cols[2].metric("Retirement Age", inputs["retirement_age"])
    profile_cols[3].metric("Risk Appetite", inputs["risk_appetite"])
    profile_cols[4].metric("Today's-Value Equivalent", inr(projection["inflation_adjusted_value"]))

    st.subheader("2. Recommended Allocation")
    allocation_df = pd.DataFrame([
        {
            "Asset Class": asset,
            "Allocation": f"{allocation}%",
            "Amount": inr(recommendation["amounts"][asset]),
        }
        for asset, allocation in recommendation["final"].items()
    ])
    st.dataframe(allocation_df, use_container_width=True, hide_index=True)

    chart_cols = st.columns(2)
    with chart_cols[0]:
        fig = px.pie(
            values=list(recommendation["final"].values()),
            names=list(recommendation["final"].keys()),
            hole=0.55,
            title="Recommended Asset Allocation",
        )
        st.plotly_chart(fig, use_container_width=True)

    with chart_cols[1]:
        st.markdown("**How the allocation was derived**")
        st.write(f"Base allocation for **{recommendation['risk_appetite']}** risk appetite:")
        st.write(
            f"Equity {recommendation['base']['Equity']}% • "
            f"Debt {recommendation['base']['Debt']}% • "
            f"Cash {recommendation['base']['Cash']}%"
        )
        st.write(
            f"Age band: **{recommendation['age_band']}**. "
            f"Equity reduction: **{recommendation['age_equity_reduction']} percentage points**."
        )
        st.write(
            f"Final allocation: **{recommendation['final']['Equity']}% Equity / "
            f"{recommendation['final']['Debt']}% Debt / "
            f"{recommendation['final']['Cash']}% Cash**."
        )
        st.caption(
            "The allocation applies to the investible portfolio only. "
            "The emergency fund is kept outside this allocation."
        )

    st.subheader("3. Portfolio Projection")
    metric_cols = st.columns(4)
    metric_cols[0].metric("Investible Portfolio", inr(investible_portfolio))
    metric_cols[1].metric("Annual Contribution", inr(inputs["annual_contribution"]))
    metric_cols[2].metric("Projected Portfolio", inr(projection["projected_value"]))
    metric_cols[3].metric("Today's-Value Equivalent", inr(projection["inflation_adjusted_value"]))

    projection_df = pd.DataFrame(projection["annual_projection"])
    fig = px.line(
        projection_df,
        x="Age",
        y="Portfolio",
        markers=True,
        title="Projected Portfolio Growth",
    )
    fig.update_yaxes(tickprefix="₹", separatethousands=True)
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("4. Interpretation")
    st.info(
        f"Based on the inputs provided, the selected risk appetite is **{inputs['risk_appetite']}**. "
        f"After applying the simple age adjustment, the suggested allocation is "
        f"**{recommendation['final']['Equity']}% Equity, "
        f"{recommendation['final']['Debt']}% Debt and "
        f"{recommendation['final']['Cash']}% Cash**."
    )

    with st.expander("Assumptions & Disclaimer"):
        st.write(
            "The emergency fund is treated as a reserve outside the investible portfolio "
            "and is not included in the allocation or growth projection."
        )
        st.write(
            "The projection assumes a constant annual return, constant annual contribution "
            "and annual compounding. Actual investment returns will vary and may be substantially higher or lower."
        )
        st.write(
            "This application is an educational planning tool and is not personalized investment, "
            "tax or financial advice."
        )
