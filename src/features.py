import pandas as pd


def compute_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create macro features:
    - VIX z-score
    - unemployment change
    - momentum
    """

    df = df.copy()

    # VIX z-score (12-month rolling)
    df["vix_z"] = (
        (df["vix"] - df["vix"].rolling(12).mean()) /
        df["vix"].rolling(12).std()
    )

    # Unemployment monthly change
    df["unrate_change"] = df["UNRATE"].diff()

    # 3-month momentum
    df["momentum_3m"] = df["returns"].rolling(3).mean()

    return df.dropna()
