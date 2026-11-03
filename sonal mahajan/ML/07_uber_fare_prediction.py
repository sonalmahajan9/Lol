
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

DATA_DIR = Path(__file__).resolve().parent
CSV_FILE = DATA_DIR / "uber.csv"


def main():
    if not CSV_FILE.exists():
        raise FileNotFoundError(f"Dataset not found: {CSV_FILE}")
    df = pd.read_csv(CSV_FILE)
    required = ["fare_amount", "pickup_longitude", "pickup_latitude", "dropoff_longitude", "dropoff_latitude", "passenger_count"]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Missing expected columns: {missing}")
    df = df[required].replace([np.inf, -np.inf], np.nan).dropna()
    df = df[(df.fare_amount > 0) & (df.fare_amount < 500)]
    df = df[df.passenger_count.between(1, 6)]
    df = df[df.pickup_longitude.between(-180, 180) & df.dropoff_longitude.between(-180, 180)]
    df = df[df.pickup_latitude.between(-90, 90) & df.dropoff_latitude.between(-90, 90)]
    if len(df) > 15000:
        df = df.sample(n=15000, random_state=42)
    if len(df) < 10:
        raise ValueError("Not enough valid rows after cleaning the dataset.")
    X = df.drop(columns="fare_amount")
    y = df["fare_amount"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    models = {
        "Linear Regression": LinearRegression(),
        "Random Forest Regression": RandomForestRegressor(n_estimators=25, random_state=42, n_jobs=-1, min_samples_leaf=2),
    }
    print(f"Rows used: {len(df)} (maximum 15,000 for quicker execution)")
    for name, model in models.items():
        model.fit(X_train, y_train)
        pred = model.predict(X_test)
        print(f"\n{name}")
        print(f"MAE: {mean_absolute_error(y_test, pred):.4f}")
        print(f"R2:  {r2_score(y_test, pred):.4f}")
        print(f"Predicted fare for one test trip: {model.predict(X_test.iloc[[0]])[0]:.2f}")

if __name__ == "__main__":
    main()
