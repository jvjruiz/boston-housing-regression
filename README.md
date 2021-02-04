# Boston Housing Regression

## Pre-requisites
Please run `pip install -r requirements.txt` to install necessary packages

## Instructions for looking at model building

1. Run the command `jupyter notebook` in root folder and up 'housing-predictions.ipynb'
2. Inside notebook all cells should be loaded, if not hit restart and run cells

## Instructions for running api
1. Run the command `uvicorn main:app --reload` to run server
2. In another terminal you can run `python inference.py` to test inferences

The endpoint is expecting the data to be formatted as a list of JSON objects.

The endpoint is located at `http://127.0.0.1:8000:predict/{model}`
The two possible values for model are:
1. linear
2. rf

Each loads loads up a different model to be used for inference.