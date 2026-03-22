# Macro Alpha Signals (Systematic Strategy)

This project implements a macro-driven systematic trading strategy using:

- S&P 500 returns
- VIX (volatility index)
- US Unemployment rate (FRED)

## Strategy intuition

The model captures macro regimes:

- Risk-on: low volatility + positive momentum
- Risk-off: high volatility or deteriorating labor market

## Features engineered

- VIX z-score (rolling normalization)
- 3-month momentum
- Unemployment rate changes

## Results

| Metric | Value |
|------|------|
| Annual Return | 1.16% |
| Volatility | Low |
| Sharpe Ratio | 0.59 |
| Max Drawdown | ~-5% |

## Key takeaways

- Macro signals contain predictive power
- Filtering improves Sharpe significantly
- Simple models can generate stable risk-adjusted returns

## Next improvements

- Add yield curve (10Y-2Y)
- Add inflation (CPI)
- Regime-switching models (HMM)
- Machine learning signals

## Author

Larissa Nawo  
Quantitative Finance / Macro Risk / Data Science

## Repository structure

```text
data/
notebooks/
src/
results/
README.md
draft_paper.pdf
