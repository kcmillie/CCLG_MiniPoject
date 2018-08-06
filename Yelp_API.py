import pandas as pd
import numpy as np
import json
import requests
from pprint import pprint
from config import api_key

API_KEY = api_key
API_HOST = 'https://api.yelp.com'
API_URL = 'https://api.yelp.com/v3/businesses/search?term='



url = API_URL + 'brewpubs' + '&location=kansascity'
headers = {'Authorization': f"Bearer {API_KEY}"}
results = requests.get(url, headers=headers)
results_json = results

print(results_json)

brewpub_df = pd.read_json(results_json)