import dill
import os
import sys

import numpy as np
import pandas as pd

from src.exception import CustomException
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score

def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)
        
        os.makedirs(dir_path,exist_ok=True)
        
        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)
    
    except Exception as e:
        raise CustomException(e,sys)

from sklearn.metrics import r2_score

def evaluate_models(x_train, y_train, x_test, y_test, models, param):
    try:
        report = {}

        for model_name, model in models.items():

            # Train model
            model.fit(x_train, y_train)

            # Predictions
            y_train_pred = model.predict(x_train)
            y_test_pred = model.predict(x_test)

            # Scores
            train_score = r2_score(y_train, y_train_pred)
            test_score = r2_score(y_test, y_test_pred)

            # Store only test score
            report[model_name] = test_score

        return report

    except Exception as e:
        raise CustomException(e, sys)
    
def load_object(file_path):
    try:
        with open(file_path,"rb")as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise CustomException(e,sys)