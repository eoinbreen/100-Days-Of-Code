import os
import requests
from requests.auth import HTTPBasicAuth  #https://requests.readthedocs.io/en/latest/user/authentication/#basic-authentication
from datetime import datetime

# Nutritionix Documentation :
# https://docs.google.com/document/d/1_q-K-ObMTZvO0qUEAxROrN3bwMujwAN25sLHwJzliK0/edit#heading=h.73n49tgew66c
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

NUTRITIONIX_APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
NUTRITIONIX_API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
SHEETY_USERNAME = os.environ.get("SHEETY_USERNAME")
SHEETY_PASSWORD = os.environ.get("SHEETY_PASSWORD")
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")

query = input("What Exercise did you do today?")

headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}

params = {
    "query": query
}

response = requests.post(url=NUTRITIONIX_ENDPOINT, json=params, headers=headers)

data = response.json()["exercises"]
workouts = []
for exercise in data:
    workout = {
        "exercise": exercise["user_input"],
        "duration": float(exercise["duration_min"]),
        "calories": exercise["nf_calories"]
    }
    workouts.append(workout)


now = datetime.now()
date = now.strftime("%m/%d/%Y")
time = now.strftime("%H:%M:%S")

basic_authentication = HTTPBasicAuth(SHEETY_USERNAME, SHEETY_PASSWORD)
for workout in workouts:
    params = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": workout["exercise"].title(),
            "duration": workout["duration"],
            "calories": workout["calories"],
        }
    }
    response = requests.post(url=SHEETY_ENDPOINT, json=params, auth=basic_authentication)
    print("response.status_code =", response.status_code)
    print("response.text =", response.text)


#  URL for database - https://docs.google.com/spreadsheets/d/1mdEyngl2I4NS69inHW_lghe4pIMKCREDM06pIavox5s/edit#gid=0

