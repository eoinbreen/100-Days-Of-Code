import csv

with open("weather_data.csv", mode="r") as file:
    weather_data = csv.reader(file)
    temperatures = []
    for row in weather_data:
        if row[1] != "temp":
            rows_temperature = int(row[1])
            temperatures.append(rows_temperature)
    print(temperatures)
