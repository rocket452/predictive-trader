"""Minimal backtesting utilities"""

import pandas as pd

def simple_backtest(prices: pd.Series, signals: pd.Series, initial_capital: float = 10000.0):
    """
    Very simple backtest:
    - signals: 1 = long, 0 = flat
    - assumes all-in positions, no leverage, no fees
    Returns a dict with portfolio value series and simple metrics.
    """
    positions = signals.shift(1).fillna(0)  # act on previous signal
    returns = prices.pct_change().fillna(0)
    strategy_returns = positions * returns
    portfolio = (1 + strategy_returns).cumprod() * initial_capital
    total_return = portfolio.iloc[-1] / initial_capital - 1
    return {
        "portfolio": portfolio,
        "total_return": total_return,
        "max_drawdown": (portfolio.cummax() - portfolio).max()
    }