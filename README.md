# Pairs Trading Backtester

This project collects historical stock data from Alpaca and is designed to backtest pairs trading strategies

## Features

- Fetches daily historical stock prices using Alpaca API
- Easily extendable for backtesting and live trading

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Rlin2024/pairs-trading-backtester.git
cd pairs-trading-backtester
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
pip install python-dotenv
```

### 3. Configure API keys

Copy the example environment file and fill in your Alpaca API credentials:

```bash
cp .env.example .env
```

Then edit the `.env` file to add your API key, secret, and base URL.

### 4. Run the backtester

```bash
python backtester.py
```

## File Descriptions

### `data_collector.py`
Fetches historical daily close prices for a given stock symbol using Alpaca’s REST API. It returns a DataFrame indexed by date. 
 ➤ You can change the data collection range by modifying `start_date="2022-06-01"` and `end_date="2025-08-01"`

### `signal_generator.py`
Takes two stock tickers, aligns their close prices, and computes the spread, rolling mean, standard deviation, and Z-score over a specified lookback window.

### `backtest.py`
Uses the Z-score signals to simulate a simple mean-reversion pairs trading strategy. It tracks capital over time and computes performance metrics like:
- Total return
- Sharpe ratio
- Max drawdown
- Trade count

Also includes plotting functionality for Z-scores and cumulative returns.


You can modify the following variables to customize your backtest:

```python
ticker1 = 'AAPL'
ticker2 = 'MSFT'
lookback = 20
initial_capital = 100000
leverage = 1
entry_threshold = 0.8
exit_threshold = 0.1
```

## Notes
* This bot currently uses Alpaca’s paper trading API.

