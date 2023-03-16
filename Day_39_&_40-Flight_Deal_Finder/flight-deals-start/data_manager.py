# Document - https://docs.google.com/spreadsheets/d/1UEFU-HJS_Uz-TRXC4q7pnMqTj4kOssJ1sZzkIT9-MeM/edit#gid=0
import requests

SHEETY_ENDPOINT = "https://api.sheety.co/7ce8f7a1b26d40fe98460d2fb88d0582/flightDeals/prices"

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def get_data(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        return response.json()

    def set_data(self, row, key, value):
        put_endpoint = f"{SHEETY_ENDPOINT}/{row}"
        params = {
            "price": {
                key: value
            }
        }
        response = requests.put(url=put_endpoint, json=params)
        # print(response.text)


