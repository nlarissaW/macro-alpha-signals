# Main script to run the macro alpha strategy pipeline

from src.data_loader import build_base_dataset
from src.features import compute_features
from src.backtest import generate_signal, backtest, performance_metrics


def main():
    # 1) Load data
    df = build_base_dataset()

    # 2) Compute features
    df = compute_features(df)

    # 3) Generate trading signal
    df = generate_signal(df)

    # 4) Run backtest
    df = backtest(df)

    # 5) Compute performance metrics
    metrics = performance_metrics(df)

    print("\n===== Strategy Performance =====")
    for k, v in metrics.items():
        print(f"{k}: {v:.4f}")


if __name__ == "__main__":
    main()
