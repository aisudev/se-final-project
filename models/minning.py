import requests
import json

page = 1
size = 100000
coins = 1

#url = f"https://api.coinmarketcap.com/content/v3/news?size={size}&page={page}&coins={coins}"
url = f"https://api.coinmarketcap.com/content/v3/news?size={size}&page={page}"
response = requests.get(url)
with open(f"raw_data.json", 'w') as f:
    f.write(response.text)
