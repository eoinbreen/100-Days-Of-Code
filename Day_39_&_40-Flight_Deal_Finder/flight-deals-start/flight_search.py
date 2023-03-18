import requests
import os
TEQUELA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUELA_KEY = os.environ.get("TEQUELA_KEY")
DUBLIN = "DUB"
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


    def get_prices(self):
        search_endpoint = f"{TEQUELA_ENDPOINT}/v2/search"
        headers = {
            "apikey": TEQUELA_KEY
        }
        params = {
            "fly_from": DUBLIN,
            "fly_to": "PAR",
            "dateFrom": "18/03/2023",
            "dateTo": "18/09/2023",
            "sort": "price",
        }
        response = requests.get(url=search_endpoint, params=params, headers=headers)
        response.raise_for_status()
        lowest_price = response.json()["data"][0]["price"]
        city = response.json()["data"][0]["cityTo"]
        return f"{city} : €{lowest_price}"

flight_searcher = FlightSearch()
print(flight_searcher.get_prices())
