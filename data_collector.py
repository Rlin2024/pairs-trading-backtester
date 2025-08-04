from alpaca_trade_api.rest import REST
import pandas as pd
from datetime import datetime
import alpaca_config as config

api = REST(config.API_KEY, config.SECRET_KEY, config.BASE_URL, api_version='v2')

def get_data(symbol, start_date="2022-06-01", end_date="2025-08-01"):
    """
    Fetch daily historical close price data for a given symbol from Alpaca.
    Returns a DataFrame indexed by date with a 'close' column.
    """
    try:
        bars = api.get_bars(
            symbol,
            timeframe="1Day",
            start=start_date,
            end=end_date,
        ).df
        
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return pd.DataFrame()

    if bars.empty:
        print(f"No data returned for {symbol}.")
        return pd.DataFrame()

    if isinstance(bars.index, pd.MultiIndex):
        bars = bars.loc[symbol]

    df = bars[['close']].copy()
    df.index.name = 'date'
    df.sort_index(inplace=True)

    return df

if __name__ == "__main__":
    # Test with AAPL
    df_aapl = get_data("AAPL")
    print(df_aapl.tail())