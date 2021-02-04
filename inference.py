import requests
import pandas as pd
import json

data = pd.read_csv('./housingdata_test.csv').to_json(orient='records')
url = 'http://127.0.0.1:8000/predict/rf'

r = requests.post(url, json=data)
content = json.loads(r.content) 
print(content)