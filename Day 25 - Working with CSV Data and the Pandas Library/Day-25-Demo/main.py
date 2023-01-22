# CSV CODE - A LOT OF WORK FOR ONE ARRAY
# import csv
#
# with open("weather_data.csv", mode="r") as file:
#     weather_data = csv.reader(file)
#     temperatures = []
#     for row in weather_data:
#         if row[1] != "temp":
#             rows_temperature = int(row[1])
#             temperatures.append(rows_temperature)
#     print(temperatures)

import pandas  # https://pandas.pydata.org/docs/

# data = pandas.read_csv("weather_data.csv")
# data_dictionary = data.to_dict()
#
# temp_list = data["temp"].to_list()
# average_temp = data["temp"].mean()
# max_temp = data["temp"].max()
#
# print(max_temp)
#
# # Get data in row
# print(data.temp)  # Panda turns labels into variables
#
# # Get data in Column
#
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# mon = data[data.day == "Monday"]
# mon_celsius = int(mon.temp)
# mon_fahrenheit = (mon_celsius * 1.8) + 32
#
# print(f"Monday's Temperature is {mon_celsius} degrees Celsius or {mon_fahrenheit} degrees Fahrenheit")

# # Creating a Data Frame and a CSV File
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

# data = pandas.read_csv("Squirrel_Data.csv")
# fur_color_list = data["Primary Fur Color"].to_list()
# red_count = fur_color_list.count("Cinnamon")
# gray_count = fur_color_list.count("Gray")
# black_count = fur_color_list.count("Black")
#
# fur_color_dict = {
#     "Fur Color":["Red", "Gray", "Black"],
#     "Count": [red_count, gray_count, black_count]
# }
#
# fur_color_data = pandas.DataFrame(fur_color_dict)
# fur_color_data.to_csv("Fur_Color.csv")

# Iterating Through Pandas Library
student_dict = {
    "student": ["Eoin", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)

for (index, row) in student_data_frame.iterrows():
    print(row.student)