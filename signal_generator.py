import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from data_collector import get_data

def compute_zscore(series):
    return (series - series.mean()) / series.std()

def generate_signals(ticker1, ticker2, lookback=20):
    df1 = get_data(ticker1)
    df2 = get_data(ticker2)

    # Align data on dates
    df = pd.merge(df1, df2, left_index=True, right_index=True, suffixes=(f'_{ticker1}', f'_{ticker2}'))

    # Calculate spread
    df['spread'] = df[f'close_{ticker1}'] - df[f'close_{ticker2}']

    # Rolling mean and std
    df['mean'] = df['spread'].rolling(window=lookback).mean()
    df['std'] = df['spread'].rolling(window=lookback).std()

    # Z-score
    df['zscore'] = (df['spread'] - df['mean']) / df['std']

    return df

if __name__ == "__main__":
    
    # Test Signal Generator With Coke and Pepsi
    
    df_signals = generate_signals('KO', 'PEP', lookback=20)
    print(df_signals.tail())

    # Plot Z-score
    df_signals['zscore'].plot(title="Spread Z-score (KO - PEP)")
    plt.axhline(1, color='red', linestyle='--', label='Upper Threshold')
    plt.axhline(-1, color='green', linestyle='--', label='Lower Threshold')
    plt.axhline(0, color='black', linestyle='-', label='Mean')
    plt.legend()
    plt.show()