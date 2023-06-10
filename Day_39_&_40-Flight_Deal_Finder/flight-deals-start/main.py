# Document - https://docs.google.com/spreadsheets/d/1UEFU-HJS_Uz-TRXC4q7pnMqTj4kOssJ1sZzkIT9-MeM/edit#gid=0
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from flight_data import FlightData

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
ORIGIN_CITY_IATA = "DUB"
data_manager = DataManager()
flight_searcher = FlightSearch()
sheet_data = data_manager.get_destination_data()

if sheet_data[0]["iataCode"] == "":
    for data in sheet_data:
        data["iataCode"] = flight_searcher.get_iata_code(data["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()




for data in sheet_data:
    flight = flight_searcher.get_lowest_price(origin_city_code=ORIGIN_CITY_IATA, destination_city_code=data["iataCode"])
    if flight is not None:
        if flight.price < data["lowestPrice"]:
            notification_manager = NotificationManager(flight)
            notification_manager.send_notification()

