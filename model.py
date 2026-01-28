from sklearn.ensemble import RandomForestClassifier
import joblib

FEATURES = [
    'ema20','ema50','ema200','rsi','atr','candle_body','range'
]

def train_model(df):
    df['label'] = 0

    # simple future move logic (can be improved)
    df.loc[df['close'].shift(-3) > df['close'], 'label'] = 1
    df.loc[df['close'].shift(-3) < df['close'], 'label'] = -1

    X = df[FEATURES]
    y = df['label']

    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=6,
        random_state=42
    )
    model.fit(X, y)

    joblib.dump(model, "xau_model.pkl")
    return model
