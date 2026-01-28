import MetaTrader5 as mt5
import pandas as pd

mt5.initialize()

def get_data(symbol="XAUUSD", timeframe=mt5.TIMEFRAME_M5, bars=500):
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, bars)
    df = pd.DataFrame(rates)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    return df
