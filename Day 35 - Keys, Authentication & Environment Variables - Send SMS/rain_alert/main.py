import requests  # https://docs.python-requests.org/en/latest/
import config
MY_LAT = 52.545240  # Gotten from latlong.net
MY_LONG = -6.317470

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
        print("Bring an Umbrella")
