# Macro Alpha Signals

A research-oriented GitHub project exploring macro-driven systematic trading signals using open financial and macroeconomic data.

## Overview

This repository develops a simple but structured macro strategy based on:

- S&P 500 returns
- VIX volatility regimes
- US unemployment data from FRED

The objective is to test whether macro and volatility conditions can improve risk-adjusted market timing.

## Data sources

- Yahoo Finance (`^GSPC`, `^VIX`)
- FRED (`UNRATE`)

## Methodology

The current prototype includes:

1. Data download and cleaning
2. Feature engineering
   - VIX z-score
   - 3-month momentum
   - Unemployment change
3. Signal construction
   - Risk-on regime
   - Risk-off regime
4. Backtesting
5. Performance evaluation

## Current results

| Metric | Value |
|---|---:|
| Annual Return | 1.16% |
| Sharpe Ratio | 0.59 |
| Max Drawdown | -4.9% |

## Key insight

Tighter signal filtering improved the Sharpe ratio materially relative to the initial version, suggesting that simple macro regime definitions may already contain useful information for systematic allocation.

## Repository structure

```text
data/         Placeholder for datasets
notebooks/    Research notebooks
src/          Reusable Python code
