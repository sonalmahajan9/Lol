ML PRACTICALS — RUN GUIDE
========================

1) Install packages (Python 3.10+ recommended):
   python -m pip install pandas numpy scikit-learn matplotlib

2) Open a terminal in this ML folder and run any file, for example:
   python 10_diabetes_knn.py
   python 07_uber_fare_prediction.py

The scripts use file paths relative to this ML folder. The datasets supplied in this pack are included here.

PRACTICAL-TO-FILE MAP
---------------------
07_uber_fare_prediction.py : Linear Regression and Random Forest Regression using uber.csv
08_email_spam_knn_svm.py  : KNN and SVM template. The email spam dataset was NOT uploaded; add its CSV to this folder and check/set the label column at the top of the script.
09_bank_churn_mlp.py      : neural-network-style MLP classifier for Churn_Modelling.csv (target Exited)
10_diabetes_knn.py        : KNN with accuracy, error rate, precision and confusion matrix
11_sales_kmeans_elbow.py  : K-Means and elbow plot using sales_data_sample (1).csv

NOTES
-----
- Use practical data files and column names as supplied. If a CSV is named differently on your computer, adjust the CSV_FILE constant at the top of the matching script.
- Uber is a relatively large file, so the script samples at most 15,000 usable rows to finish faster on a lab computer.
- The models split data into train/test sets. Your numerical output can vary slightly across datasets/library versions.
- For email spam, the script tries common target column names including Prediction, spam, label, class, and Category. If none exists, edit TARGET_COLUMN to the correct label column.
