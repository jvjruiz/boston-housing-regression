import requests
import pandas as pd
import json

# load csv and convert to list of json objects
data = pd.read_csv('./housingdata_test.csv').to_json(orient='records')

# setup url
url = 'http://127.0.0.1:8000/predict/linear'

# make request and print response
r = requests.post(url, json=data)
content = json.loads(r.content) 
print(content)