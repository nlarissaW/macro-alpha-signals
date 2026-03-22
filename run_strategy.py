# Main script to run the macro alpha strategy pipeline

from src.data_loader import build_base_dataset
from src.features import compute_features
from src.backtest import generate_signal, backtest, performance_metrics


def main():
    # 1) Load data
    df = build_base_dataset()

    # 2) Compute features
    df = compute_features(df)

    # 3) Generate signal
    df = generate_signal(df)

    # 4) Backtest
    df = backtest(df)

    # 5) Metrics
    metrics = performance_metrics(df)

    print("\n===== Macro Alpha Strategy Performance =====")
    print(f"Annual Return   : {metrics['return']:.4f}")
    print(f"Annual Vol      : {metrics['vol']:.4f}")
    print(f"Sharpe Ratio    : {metrics['sharpe']:.4f}")
    print(f"Max Drawdown    : {metrics['max_dd']:.4f}")
    print(f"Hit Ratio       : {metrics['hit_ratio']:.4f}")


if __name__ == "__main__":
    main()
