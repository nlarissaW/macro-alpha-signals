import pandas as pd
import yfinance as yf
from pandas_datareader import data as web


def load_sp500(start="2010-01-01"):
    sp500 = yf.download("^GSPC", start=start, auto_adjust=False, progress=False)
    sp500["returns"] = sp500["Adj Close"].pct_change()
    return sp500


def load_vix(start="2010-01-01"):
    vix = yf.download("^VIX", start=start, auto_adjust=False, progress=False)
    return vix[["Adj Close"]].rename(columns={"Adj Close": "vix"})


def load_fred_series(series_id, start="2010-01-01"):
    df = web.DataReader(series_id, "fred", start)
    return df
