"""LP3 ML Practical 9: Predict bank customer churn with an MLP neural network."""
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

DATA_DIR = Path(__file__).resolve().parent
CSV_FILE = DATA_DIR / "Churn_Modelling.csv"


def main():
    if not CSV_FILE.exists():
        raise FileNotFoundError(f"Dataset not found: {CSV_FILE}")
    df = pd.read_csv(CSV_FILE)
    if "Exited" not in df.columns:
        raise ValueError("Expected target column 'Exited' was not found.")
    X = df.drop(columns=["Exited", "RowNumber", "CustomerId", "Surname"], errors="ignore")
    y = df["Exited"]
    numeric = X.select_dtypes(include="number").columns.tolist()
    categorical = X.select_dtypes(exclude="number").columns.tolist()
    transformers = []
    if numeric:
        transformers.append(("numeric", Pipeline([("imputer", SimpleImputer(strategy="median")), ("scale", StandardScaler())]), numeric))
    if categorical:
        transformers.append(("categorical", Pipeline([("imputer", SimpleImputer(strategy="most_frequent")), ("encode", OneHotEncoder(handle_unknown="ignore"))]), categorical))
    preprocess = ColumnTransformer(transformers)
    model = Pipeline([("preprocess", preprocess), ("neural_network", MLPClassifier(hidden_layer_sizes=(16, 8), max_iter=300, random_state=42, early_stopping=True))])
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print("Target: Exited (1 = customer left, 0 = customer stayed)")
    print(f"Accuracy: {accuracy_score(y_test, pred):.4f}")
    print("Confusion matrix:\n", confusion_matrix(y_test, pred))
    print(classification_report(y_test, pred, zero_division=0))
    print("Example prediction:", int(model.predict(X_test.iloc[[0]])[0]))

if __name__ == "__main__":
    main()
