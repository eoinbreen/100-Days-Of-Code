from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

data_manager = DataManager()
flight_searcher = FlightSearch()
sheet_data = data_manager.get_destination_data()
if sheet_data[0]["iataCode"] == "":
    for data in sheet_data:
        data["iataCode"] = flight_searcher.get_iata_code(data["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

# pprint(sheet_data)


