from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

from datetime import datetime
from datetime import timedelta
from pprint import pprint
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
ORIGIN_CITY_IATA = "DUB"
data_manager = DataManager()
flight_searcher = FlightSearch()
sheet_data = data_manager.get_destination_data()

if sheet_data[0]["iataCode"] == "":
    for data in sheet_data:
        data["iataCode"] = flight_searcher.get_iata_code(data["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for data in sheet_data:
    flight = flight_searcher.get_lowest_price(origin_city_code=ORIGIN_CITY_IATA,destination_city_code=data["iataCode"],
                                              from_time=tomorrow, to_time=six_month_from_today)

# pprint(sheet_data)


