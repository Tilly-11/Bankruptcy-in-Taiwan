# Import libraries
import gzip
import json
import pickle

import pandas as pd
#wrangle function
def wrangle(filepath):
    #openng json file
    with gzip.open(filepath, "r") as f:
        data = json.load(f)
        
    #reading data into a dataframe
    df = pd.DataFrame().from_dict(data["observations"]).set_index("id")
    
    return df

#prediction function
def make_predictions(data_filepath, model_filepath):
    #wrangle data
    df = wrangle(data_filepath)
    
    #open model
    with open(model_filepath, "rb") as f:
        model=pickle.load(f)
        
    #make predictions using X_tets
    y_test_pred = model.predict(X_test)
    
    #putting predictions into a series
    y_test_pred = pd.Series(y_test_pred, index = y_test.index, name= "bankrupt")
    
    return y_test_pred
