import os
import requests
from datetime import datetime

# Nutritionix Documentation :
# https://docs.google.com/document/d/1_q-K-ObMTZvO0qUEAxROrN3bwMujwAN25sLHwJzliK0/edit#heading=h.73n49tgew66c

NUTRITIONIX_APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
NUTRITIONIX_API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/7ce8f7a1b26d40fe98460d2fb88d0582/workoutTracking/workouts"

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
    response = requests.post(url=SHEETY_ENDPOINT, json=params)
    print("response.status_code =", response.status_code)
    print("response.text =", response.text)
# print(response.text)

