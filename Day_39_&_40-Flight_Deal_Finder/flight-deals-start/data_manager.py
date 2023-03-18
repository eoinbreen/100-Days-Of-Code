# Document - https://docs.google.com/spreadsheets/d/1UEFU-HJS_Uz-TRXC4q7pnMqTj4kOssJ1sZzkIT9-MeM/edit#gid=0
import requests
import os

SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        self.destination_data = response.json()["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            put_endpoint = f"{SHEETY_ENDPOINT}/{city['id']}"
            params = {
                "price": {
                    'iataCode': city["iataCode"]
                }
            }
            response = requests.put(url=put_endpoint, json=params)
            print(response.text)


