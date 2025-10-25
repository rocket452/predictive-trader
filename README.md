# Predictive Trader

An AI-powered algorithmic trading platform that leverages machine learning to analyze market data, generate trading signals, and execute automated trades.

This repository provides a minimal scaffold to get started with:
- data collection (yfinance)
- a simple trading bot orchestration
- a placeholder for ML-based signal generation
- a simple backtester
- an example run script

Keep this scaffold simple: start with a deterministic strategy (SMA crossover) and later replace the signal generator with an ML model.

Getting started
1. Create a Python virtualenv and install requirements:
   pip install -r requirements.txt

2. Run the example (paper trading / backtest):
   python examples/simple_run.py

3. Replace predictive_trader/bot.generate_signals with your ML model or training pipeline.

Contributing
- Keep changes small.
- Add tests and CI for backtesting and sample data pipelines.