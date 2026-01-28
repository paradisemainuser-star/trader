def calculate_sl_tp(price, atr, direction):
    if direction == "BUY":
        sl = price - (1.5 * atr)
        tp = price + (3 * atr)
    else:
        sl = price + (1.5 * atr)
        tp = price - (3 * atr)

    return sl, tp
