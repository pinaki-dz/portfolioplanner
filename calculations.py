def calculate_future_value(current_value, annual_contribution, annual_return, years):
    rate = annual_return / 100
    if years <= 0:
        return current_value
    future_current = current_value * ((1 + rate) ** years)
    if rate == 0:
        future_contributions = annual_contribution * years
    else:
        future_contributions = annual_contribution * (((1 + rate) ** years - 1) / rate)
    return future_current + future_contributions

def calculate_inflation_adjusted_value(future_value, inflation, years):
    inflation_rate = inflation / 100
    return future_value / ((1 + inflation_rate) ** years)

def calculate_years_to_retirement(age, retirement_age):
    return max(0, retirement_age - age)

def build_projection(current_value, annual_contribution, expected_return, inflation, age, retirement_age):
    years = calculate_years_to_retirement(age, retirement_age)
    annual_projection = []
    value = current_value
    rate = expected_return / 100

    for year in range(years + 1):
        annual_projection.append({"Year": year, "Age": age + year, "Portfolio": value})
        if year < years:
            value = value * (1 + rate) + annual_contribution

    projected_value = value
    inflation_adjusted_value = calculate_inflation_adjusted_value(
        projected_value, inflation, years
    )
    return {
        "years": years,
        "projected_value": projected_value,
        "inflation_adjusted_value": inflation_adjusted_value,
        "annual_projection": annual_projection,
    }
