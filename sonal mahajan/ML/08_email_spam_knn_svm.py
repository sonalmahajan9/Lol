"""LP3 ML Practical 8: email spam classification with KNN and SVM.

IMPORTANT: Add your email-spam dataset CSV to this folder. By default, this script
looks for emails.csv. Set CSV_FILE and TARGET_COLUMN below if needed.
"""
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

DATA_DIR = Path(__file__).resolve().parent
CSV_FILE = DATA_DIR / "emails.csv"  # Change to the actual dataset filename.
TARGET_COLUMN = None                # e.g. "Prediction", "spam", "label"; None = auto-detect.
COMMON_TARGETS = ["Prediction", "prediction", "spam", "Spam", "label", "Label", "class", "Class", "Category", "target", "Target"]
ID_COLUMNS = ["Email No.", "Email No", "email", "Email", "email_id", "EmailID", "Unnamed: 0"]


def main():
    if not CSV_FILE.exists():
        print(f"EMAIL SPAM DATASET NOT FOUND: {CSV_FILE.name}")
        print("The uploaded files contained Uber, sales, diabetes, and bank churn datasets, but no email spam CSV.")
        print("Copy your email-spam CSV into this ML folder, then update CSV_FILE at the top of this script.")
        return
    df = pd.read_csv(CSV_FILE, encoding="latin-1")
    target = TARGET_COLUMN
    if target is None:
        target = next((c for c in COMMON_TARGETS if c in df.columns), None)
    if target is None or target not in df.columns:
        print("Could not find the target/label column.")
        print("Available columns:", list(df.columns))
        print("Set TARGET_COLUMN near the top of this file to the actual spam/not-spam label column.")
        return
    y = df[target]
    X = df.drop(columns=[target] + [c for c in ID_COLUMNS if c in df.columns], errors="ignore")
    X = X.select_dtypes(include="number")
    if X.shape[1] == 0:
        print("No numeric word-frequency/features columns found. Convert text features or check your dataset format.")
        return
    valid = y.notna()
    X, y = X.loc[valid], y.loc[valid]
    if y.nunique() < 2:
        print("Target must contain at least two classes (spam and not-spam).")
        return
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    models = {
        "KNN": make_pipeline(SimpleImputer(strategy="median"), StandardScaler(), KNeighborsClassifier(n_neighbors=5)),
        "SVM": make_pipeline(SimpleImputer(strategy="median"), StandardScaler(), SVC(kernel="linear")),
    }
    for name, model in models.items():
        model.fit(X_train, y_train)
        pred = model.predict(X_test)
        print(f"\n{name}")
        print(f"Accuracy: {accuracy_score(y_test, pred):.4f}")
        print("Confusion matrix:\n", confusion_matrix(y_test, pred))
        print(classification_report(y_test, pred, zero_division=0))

if __name__ == "__main__":
    main()
