"""LP3 ML Practical 11: K-Means clustering and elbow method for sales dataset."""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

DATA_DIR = Path(__file__).resolve().parent
CSV_FILE = DATA_DIR / "sales_data_sample (1).csv"
FEATURES = ["QUANTITYORDERED", "PRICEEACH", "SALES", "MSRP", "QTR_ID", "MONTH_ID", "YEAR_ID"]


def main():
    if not CSV_FILE.exists():
        raise FileNotFoundError(f"Dataset not found: {CSV_FILE}")
    df = pd.read_csv(CSV_FILE, encoding="latin-1")
    use = [c for c in FEATURES if c in df.columns]
    if len(use) < 2:
        numeric = df.select_dtypes(include="number").columns.tolist()
        use = numeric[:]
    if len(use) < 2:
        raise ValueError("Need at least two numeric features to cluster.")
    X = df[use].replace([np.inf, -np.inf], np.nan)
    X = X.loc[:, X.nunique(dropna=True) > 1]
    if X.shape[1] < 2:
        raise ValueError("Need at least two non-constant numeric features.")
    prep = make_pipeline(SimpleImputer(strategy="median"), StandardScaler())
    X_scaled = prep.fit_transform(X)
    max_k = min(10, len(X_scaled))
    ks, inertias = list(range(1, max_k + 1)), []
    for k in ks:
        km = KMeans(n_clusters=k, random_state=42, n_init=10)
        km.fit(X_scaled)
        inertias.append(km.inertia_)
    plt.plot(ks, inertias, marker="o")
    plt.xlabel("Number of clusters (K)")
    plt.ylabel("Inertia")
    plt.title("Elbow Method for K-Means")
    plt.xticks(ks)
    plt.tight_layout()
    output_plot = DATA_DIR / "elbow_method.png"
    plt.savefig(output_plot, dpi=150)
    print("Elbow plot saved to:", output_plot)
    plt.show()
    k = 3  # Change this after inspecting the elbow plot.
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = model.fit_predict(X_scaled)
    df["Cluster"] = labels
    print("Features used:", use)
    print("Cluster counts:\n", df["Cluster"].value_counts().sort_index())
    print("First 10 assigned clusters:\n", df[["Cluster"]].head(10))

if __name__ == "__main__":
    main()
