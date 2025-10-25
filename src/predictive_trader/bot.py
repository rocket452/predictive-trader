"""Simple trading bot scaffold.

This file contains a minimal TradingBot class that:
- fetches data
- generates signals (SMA crossover by default)
- backtests signals
- has placeholders for executing trades and plugging in ML models
"""

from typing import Optional
import pandas as pd

from .data import fetch_yahoo
from .backtest import simple_backtest

class TradingBot:
    def __init__(self, ticker: str, short_window: int = 10, long_window: int = 30):
        self.ticker = ticker
        self.short_window = short_window
        self.long_window = long_window
        self.prices: Optional[pd.DataFrame] = None
        self.signals: Optional[pd.Series] = None

    def fetch_data(self, period: str = "1y", interval: str = "1d"):
        self.prices = fetch_yahoo(self.ticker, period=period, interval=interval)
        return self.prices

    def generate_signals(self):
        """
        Default deterministic signal: SMA crossover
        Replace this method with an ML-based predictor later.
        """
        if self.prices is None:
            raise RuntimeError("No price data. Call fetch_data first.")
        close = self.prices['Adj Close'] if 'Adj Close' in self.prices else self.prices['Close']
        sma_short = close.rolling(self.short_window).mean()
        sma_long = close.rolling(self.long_window).mean()
        signal = (sma_short > sma_long).astype(int)
        self.signals = signal
        return self.signals

    def backtest(self):
        if self.signals is None or self.prices is None:
            raise RuntimeError("Signals or prices missing")
        result = simple_backtest(self.prices['Adj Close'] if 'Adj Close' in self.prices else self.prices['Close'], self.signals)
        return result

    def execute_trade(self, signal: int):
        """
        Placeholder: send trade to broker / paper trading system.
        Implement API calls here (e.g., Alpaca, IB, CCXT, broker SDK).
        """
        # Example: log or print, replace with real execution logic
        print(f"Executing trade signal={{signal}} for {{self.ticker}}")

    def run(self):
        """End-to-end run: fetch, signal, backtest"""
        self.fetch_data()
        self.generate_signals()
        results = self.backtest()
        return results
