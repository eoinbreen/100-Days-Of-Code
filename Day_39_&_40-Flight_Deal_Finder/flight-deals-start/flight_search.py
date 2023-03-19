import requests
import os
from flight_data import FlightData
TEQUELA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUELA_KEY = os.environ.get("TEQUELA_KEY")


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

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

    def get_lowest_price(self, origin_city_code, destination_city_code, from_time, to_time):
        search_endpoint = f"{TEQUELA_ENDPOINT}/v2/search"  # https://tequila.kiwi.com/portal/docs/tequila_api/search_api

        headers = {
            "apikey": TEQUELA_KEY
        }
        params = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "dateFrom": from_time.strftime("%d/%m/%Y"),
            "dateTo": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "EUR",
        }
        response = requests.get(url=search_endpoint, params=params, headers=headers)
        response.raise_for_status()
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: €{flight_data.price}")
        return flight_data
