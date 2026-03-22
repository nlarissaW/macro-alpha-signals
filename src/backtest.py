import numpy as np
import pandas as pd


def generate_signal(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create trading signal based on macro conditions
    """

    df = df.copy()
    df["signal"] = 0

    # Risk-on
    df.loc[
        (df["vix_z"] < -0.5) &
        (df["momentum_3m"] > 0),
        "signal"
    ] = 1

    # Risk-off
    df.loc[
        (df["vix_z"] > 1.5),
        "signal"
    ] = -1

    return df


def backtest(df: pd.DataFrame) -> pd.DataFrame:
    """
    Run simple backtest
    """

    df = df.copy()

    # Apply signal with lag
    df["strategy_returns"] = df["signal"].shift(1) * df["returns"]

    df = df.dropna()

    # Cumulative returns
    df["cum_market"] = (1 + df["returns"]).cumprod()
    df["cum_strategy"] = (1 + df["strategy_returns"]).cumprod()

    return df


def performance_metrics(df: pd.DataFrame) -> dict:
    """
    Compute performance statistics
    """

    ann_return = df["strategy_returns"].mean() * 12
    ann_vol = df["strategy_returns"].std() * np.sqrt(12)
    sharpe = ann_return / ann_vol

    cum = df["cum_strategy"]
    roll_max = cum.cummax()
    drawdown = cum / roll_max - 1
    max_dd = drawdown.min()

    return {
        "return": ann_return,
        "vol": ann_vol,
        "sharpe": sharpe,
        "max_dd": max_dd
    }
