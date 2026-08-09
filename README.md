# Portfolio Planner — V1.0.1

A simple educational portfolio planning application built with Python and Streamlit.

## V1.0.1 improvements

- Emergency fund is kept outside the investible portfolio.
- Allocation amounts and projection use the investible portfolio.
- Added a top-level portfolio summary.
- Improved monetary input display.
- Added validation preventing emergency fund from exceeding portfolio value.
- Clarified assumptions and emergency-fund treatment.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Project structure

- `app.py` — Streamlit entry point
- `inputs.py` — Input collection and validation
- `calculations.py` — Projection calculations
- `recommendations.py` — Allocation logic
- `display.py` — Dashboard and charts
- `config.py` — Assumptions and constants
- `requirements.txt` — Python dependencies

## Disclaimer

This is an educational planning tool. It does not constitute personalized investment, tax or financial advice. Actual investment returns are uncertain.
