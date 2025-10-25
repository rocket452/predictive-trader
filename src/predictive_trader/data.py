"""Simple data fetching utilities using yfinance"""
import pandas as pd
import yfinance as yf
from typing import Optional

def fetch_yahoo(ticker: str, period: str = "1y", interval: str = "1d") -> pd.DataFrame:
    """
    Fetch OHLCV data for ticker from Yahoo Finance.
    Returns a DataFrame with columns: ['Open','High','Low','Close','Adj Close','Volume']
    """
    data = yf.download(ticker, period=period, interval=interval, progress=False)
    data = data.dropna()
    return data
