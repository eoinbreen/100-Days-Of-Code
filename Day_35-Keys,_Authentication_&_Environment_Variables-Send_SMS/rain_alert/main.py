import requests  # https://docs.python-requests.org/en/latest/
import config
import os
from twilio.rest import Client

MY_LAT = 52.545240  # Gotten from latlong.net
MY_LONG = -6.317470
API_KEY = os.environ.get("API_KEY")

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": config.API_KEY,
    "cnt": 4
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast?", params=parameters)
response.raise_for_status()
data = response.json()
weather_data = []

for n in range(len(data["list"])):
    weather = data["list"][n]["weather"]
    weather_data.append(weather)
    
for weather in weather_data:
    id_code = weather[0]["id"]
    if id_code < 700:
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
            body="Bring an Umbrella.",
            from_='+15673131224',
            to='+3530876544958'
        )
