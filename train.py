from data import get_data
from features import add_features
from model import train_model

df = get_data("XAUUSD", bars=2000)
df = add_features(df)

train_model(df)
print("✅ Model trained and saved")
