import requests
import json

global_url = "https://api.coinmarketcap.com/v2/global/"

request = requests.get(global_url)
results = request.json()
print(results)