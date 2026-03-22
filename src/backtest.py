import numpy as np
import pandas as pd


def generate_signal(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create trading signal based on macro conditions.
    """

    df = df.copy()
    df["signal"] = 0

    # Risk-on regime
    df.loc[
        (df["vix_z"] < -0.5) &
        (df["momentum_3m"] > 0),
        "signal"
    ] = 1

    # Risk-off regime
    df.loc[
        (df["vix_z"] > 1.5),
        "signal"
    ] = -1

    return df


def backtest(df: pd.DataFrame) -> pd.DataFrame:
    """
    Run simple backtest with lagged signal.
    """

    df = df.copy()

    # Use lagged signal to avoid look-ahead bias
    df["strategy_returns"] = df["signal"].shift(1) * df["returns"]

    df = df.dropna()

    # Cumulative performance
    df["cum_market"] = (1 + df["returns"]).cumprod()
    df["cum_strategy"] = (1 + df["strategy_returns"]).cumprod()

    # Drawdown
    df["roll_max"] = df["cum_strategy"].cummax()
    df["drawdown"] = df["cum_strategy"] / df["roll_max"] - 1

    return df


def performance_metrics(df: pd.DataFrame) -> dict:
    """
    Compute strategy performance statistics.
    """

    ann_return = df["strategy_returns"].mean() * 12
    ann_vol = df["strategy_returns"].std() * np.sqrt(12)
    sharpe = ann_return / ann_vol if ann_vol != 0 else np.nan

    max_dd = df["drawdown"].min()

    hit_ratio = (df["strategy_returns"] > 0).mean()

    return {
        "return": ann_return,
        "vol": ann_vol,
        "sharpe": sharpe,
        "max_dd": max_dd,
        "hit_ratio": hit_ratio,
    }
