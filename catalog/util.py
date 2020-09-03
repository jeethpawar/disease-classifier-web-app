from joblib import load
import pandas as pd

# 3. Transform form data into row proportions
def row_prop(data):
    # assuming data is a list of booleans
    s = sum(data)
    for i, val in enumerate(data):
        data[i] = (val * 1.0) / s
    return data


# 4. Feed model form proportions
def model_predict(clf, X_test):
    return clf.predict(X_test)

