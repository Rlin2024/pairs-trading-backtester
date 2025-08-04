# Pairs Trading Bot

This project collects historical stock data from Alpaca and is designed to support pairs trading strategies.

## Features

- Fetches daily historical stock prices using Alpaca API
- Easily extendable for backtesting and live trading
- Uses environment variables for secure API key management

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Rlin2024/pairs-trading-backtester.git
cd pairs-trading-backtester


2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
pip install python-dotenv
3. Configure API keys
Copy the example environment file and fill in your Alpaca API credentials:

bash
Copy
Edit
cp .env.example .env
Edit .env with your API key, secret, and base URL.

4. Run the data collector
bash
Copy
Edit
python data_collector.py
Notes
Make sure .env is included in .gitignore to keep your API keys secure.

This bot currently uses Alpaca’s paper trading API.