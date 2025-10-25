"""Example usage of the minimal scaffold."""
from predictive_trader.bot import TradingBot

def main():
    bot = TradingBot("AAPL", short_window=10, long_window=30)
    results = bot.run()
    print("Total return:", results["total_return"])
    print("Max drawdown:", results["max_drawdown"])
    # Optionally plot the portfolio
    try:
        import matplotlib.pyplot as plt
        results["portfolio"].plot(title="Portfolio Value")
        plt.show()
    except Exception:
        pass

if __name__ == "__main__":
    main()