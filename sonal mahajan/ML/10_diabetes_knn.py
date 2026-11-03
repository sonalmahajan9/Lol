"""LP3 ML Practical 10: KNN on diabetes.csv with evaluation metrics."""
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, classification_report

DATA_DIR = Path(__file__).resolve().parent
CSV_FILE = DATA_DIR / "diabetes (1).csv"


def main():
    if not CSV_FILE.exists():
        raise FileNotFoundError(f"Dataset not found: {CSV_FILE}")
    df = pd.read_csv(CSV_FILE)
    if "Outcome" not in df.columns:
        raise ValueError("Expected target column 'Outcome' was not found.")
    X, y = df.drop(columns=["Outcome"]), df["Outcome"]
    # In this common diabetes dataset, zero can represent missing readings for these columns.
    for col in ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]:
        if col in X.columns:
            X[col] = X[col].replace(0, float("nan"))
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    model = make_pipeline(SimpleImputer(strategy="median"), StandardScaler(), KNeighborsClassifier(n_neighbors=5))
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, pred)
    print("Confusion matrix:\n", confusion_matrix(y_test, pred))
    print(f"Accuracy: {accuracy:.4f} ({accuracy * 100:.2f}%)")
    print(f"Error rate: {1 - accuracy:.4f}")
    print(f"Precision: {precision_score(y_test, pred, zero_division=0):.4f}")
    print("Classification report:\n", classification_report(y_test, pred, zero_division=0))

if __name__ == "__main__":
    main()
