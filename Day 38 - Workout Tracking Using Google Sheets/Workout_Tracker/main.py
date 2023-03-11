import os
import requests

# Nutritionix Documentation :
# https://docs.google.com/document/d/1_q-K-ObMTZvO0qUEAxROrN3bwMujwAN25sLHwJzliK0/edit#heading=h.73n49tgew66c

NUTRITIONIX_APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
NUTRITIONIX_API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}

params = {
    "query": "Walked for 30 minutes"
}

response = requests.post(url=NUTRITIONIX_ENDPOINT, json=params, headers=headers)
print(response.text)

