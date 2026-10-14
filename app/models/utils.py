import os
import pandas as pd
import joblib
from functools import lru_cache

APP_DIR_NAME='app'
MODEL_DIR_NAME='models'
MODEL_NAME='pipeline.joblib'

model_path=os.path.join(APP_DIR_NAME,MODEL_DIR_NAME,MODEL_NAME)


@lru_cache(maxsize=1)
def get_model():
    model = joblib.load(model_path)
    return model

def get_prediction(input:dict)->int:
    model=get_model()
    input_df = pd.DataFrame([input])
    return int(model.predict(input_df)[0])