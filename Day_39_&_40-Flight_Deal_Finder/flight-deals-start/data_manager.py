# Document - https://docs.google.com/spreadsheets/d/1UEFU-HJS_Uz-TRXC4q7pnMqTj4kOssJ1sZzkIT9-MeM/edit#gid=0
import requests
import os

SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def get_data(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        return response.json()["prices"]

    def set_data(self, row, key, value):
        put_endpoint = f"{SHEETY_ENDPOINT}/{row}"
        params = {
            "price": {
                key: value
            }
        }
        response = requests.put(url=put_endpoint, json=params)
        # print(response.text)


