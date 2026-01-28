from data import get_data
from features import add_features
from strategy import generate_signal
from risk import calculate_sl_tp
from trade import place_trade

SYMBOL = "XAUUSD"
LOT = 0.01

df = get_data(SYMBOL)
df = add_features(df)

signal = generate_signal(df)

if signal != "NO_TRADE":
    price = df.iloc[-1].close
    atr = df.iloc[-1].atr

    sl, tp = calculate_sl_tp(price, atr, signal)
    place_trade(SYMBOL, signal, LOT, sl, tp)
