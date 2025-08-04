import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from signal_generator import generate_signals

def backtest_pairs_trading(
    ticker1,
    ticker2,
    lookback=20,
    initial_capital=100000,
    leverage=3,
    entry_threshold=0.8,
    exit_threshold=0.1
):
    df = generate_signals(ticker1, ticker2, lookback)
    df = df.dropna().copy()

    position = 0  # 0 = no position, 1 = long spread, -1 = short spread
    capital = initial_capital
    capital_history = []
    returns = []
    trade_count = 0

    shares_1 = 0
    shares_2 = 0

    for i in range(1, len(df)):
        z = df['zscore'].iloc[i]
        price1 = df[f'close_{ticker1}'].iloc[i]
        price2 = df[f'close_{ticker2}'].iloc[i]
        price1_prev = df[f'close_{ticker1}'].iloc[i - 1]
        price2_prev = df[f'close_{ticker2}'].iloc[i - 1]

        daily_pnl = 0

        if position == 0:
            if z < -entry_threshold:
                position = 1  # Long spread: Long ticker1, Short ticker2
                trade_count += 1
                allocation = capital * leverage / 2
                shares_1 = allocation / price1
                shares_2 = allocation / price2
            elif z > entry_threshold:
                position = -1  # Short spread: Short ticker1, Long ticker2
                trade_count += 1
                allocation = capital * leverage / 2
                shares_1 = allocation / price1
                shares_2 = allocation / price2

        elif position == 1:  # Long spread
            if abs(z) < exit_threshold:
                position = 0  # Close position
                shares_1 = 0
                shares_2 = 0

        elif position == -1:  # Short spread
            if abs(z) < exit_threshold:
                position = 0  # Close position
                shares_1 = 0
                shares_2 = 0

        # Calculate PnL based on position
        if position == 1:
            daily_pnl = (price1 - price1_prev) * shares_1 - (price2 - price2_prev) * shares_2
        elif position == -1:
            daily_pnl = (price2 - price2_prev) * shares_2 - (price1 - price1_prev) * shares_1

        capital += daily_pnl
        capital_history.append(capital)
        returns.append(daily_pnl / initial_capital)

    # Create series for analysis
    capital_series = pd.Series(capital_history, index=df.index[-len(capital_history):])
    returns_series = pd.Series(returns, index=df.index[-len(returns):])
    cumulative_returns = capital_series / initial_capital - 1

    sharpe_ratio = np.sqrt(252) * returns_series.mean() / returns_series.std()
    max_drawdown = (cumulative_returns.cummax() - cumulative_returns).max()

    print(f"Final Portfolio Value: ${capital:.2f}")
    print(f"Total Return: {cumulative_returns.iloc[-1] * 100:.2f}%")
    print(f"Sharpe Ratio: {sharpe_ratio:.2f}")
    print(f"Max Drawdown: {max_drawdown * 100:.2f}%")
    print(f"Total Trades Executed: {trade_count}")

    # Plot cumulative returns
    plt.figure(figsize=(10, 6))
    cumulative_returns.plot(title=f"{ticker1}-{ticker2} Pairs Trading Backtest - Cumulative Returns")
    plt.xlabel("Date")
    plt.ylabel("Cumulative Return")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    backtest_pairs_trading(
        ticker1='AAPL',
        ticker2='MSFT',
        lookback=20,
        initial_capital=100000,
        leverage=1,
        entry_threshold=0.8,
        exit_threshold=0.1
    )
