
````markdown
# Pairs Trading Bot

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

## Notes
* This bot currently uses Alpaca’s paper trading API.

