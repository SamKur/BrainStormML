# common functionality - like eval functions
import os
import sys

import numpy as np
import pandas as pd
import dill #to handle pickle file
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import SusamayException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise SusamayException(e, sys)
    
def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    try:
        report = {}

        # Iterate over models and corresponding parameters using zip
        for model_name, model in models.items():
            # Get the hyperparameters for the current model
            para = param[model_name]

            # Perform grid search to find the best parameters
            gs = GridSearchCV(model, para, cv=3)
            gs.fit(X_train, y_train)

            # Use the best found parameters
            best_model = gs.best_estimator_

            # Predict on train and test sets
            y_train_pred = best_model.predict(X_train)
            y_test_pred = best_model.predict(X_test)

            # Calculate R2 score for both train and test sets
            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            # Store the test score in the report
            report[model_name] = test_model_score
        
        return report

    except Exception as e:
        raise SusamayException(e, sys)
