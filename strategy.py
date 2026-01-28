import joblib
from model import FEATURES

model = joblib.load("xau_model.pkl")

def generate_signal(df):
    last = df.iloc[-1]

    # Market context (human logic)
    if not (last.ema50 > last.ema200):
        return "NO_TRADE"

    if last.rsi < 40 or last.rsi > 60:
        return "NO_TRADE"

    X = df[FEATURES].iloc[-1:].values
    prediction = model.predict(X)[0]

    if prediction == 1:
        return "BUY"
    elif prediction == -1:
        return "SELL"
    else:
        return "NO_TRADE"
