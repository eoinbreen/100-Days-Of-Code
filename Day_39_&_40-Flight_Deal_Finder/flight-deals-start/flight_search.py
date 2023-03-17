import requests
import os
TEQUELA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUELA_KEY = os.environ.get("TEQUELA_KEY")
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def get_iata_code(self, city):
        query_endpoint = f"{TEQUELA_ENDPOINT}/locations/query"  #  https://tequila.kiwi.com/portal/docs/tequila_api/locations_api
        headers = {
            "apikey": TEQUELA_KEY
        }
        params = {
            "term": city,
            "location_types": "city"
        }

        response = requests.get(url=query_endpoint, params=params, headers=headers)
        results = response.json()["locations"]
        iata_code = results[0]["code"]
        return iata_code

