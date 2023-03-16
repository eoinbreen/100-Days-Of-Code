from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

data_manager = DataManager()
flight_searcher = FlightSearch()
sheet_data = data_manager.get_data()
for data in sheet_data["prices"]:
    if data["iataCode"] == "":
        data["iataCode"] = flight_searcher.get_iata_code(data["city"])
        data_manager.set_data(row=data["id"], key="iataCode", value=data["iataCode"])

# pprint(sheet_data)


