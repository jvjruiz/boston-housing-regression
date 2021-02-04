from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from utils import pre_processing_pipeline
from typing import Optional
from joblib import load

import pandas as pd

app = FastAPI()


@app.post('/predict/{model}')
async def create_item(stats: Request, model):
    predictions = []
    # convert body to json
    data = await stats.json()
    # convert to dataframe
    df = pd.read_json(data, orient='records')
    total_records_sent = df.shape[0]

    # pre-process records
    df = pre_processing_pipeline(df)
    # grab remaining indices for return
    indices = df.index.tolist()

    # load model depicted by query string
    if model.lower() != 'linear' and model.lower() != 'rf':
        # return message if no model is selected
        message = 'Please provide model type in URL'
        return jsonable_encoder({'message': message, 'predictions':[]})
    elif model.lower() == 'linear':
        model = load('./models/linear_model.joblib')
    elif model.lower() == 'rf':
        model = load('./models/random_forest.joblib')

    # make predictions
    try:
        preds = model.predict(df).tolist()
    except:
        message = 'Something went wrong, please ensure data is in correct format.'
        return jsonable_encoder({'message': message, 'predictions': []})


    for i in range(0, len(preds)):
        predictions.append([indices[i],preds[i]])
    message = 'Predictions successfully completed, {} rows were filtered out for having null values'.format(total_records_sent - len(predictions))
    return jsonable_encoder({'message': message, 'predictions': predictions})
    
