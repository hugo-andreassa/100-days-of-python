# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# ------------------------------
data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

# ------------------------------
data_dict = data.to_dict()
# print(data_dict)

# Average ------------------------------
temp_list = data["temp"].to_list()
# print(temp_list)
# print(sum(temp_list) / len(temp_list))

# Average with panda ------------------------------
# print(data["temp"].mean())

# Higher temp ------------------------------
# print(data["temp"].max())

# Get data in a row ------------------------------
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
# print(data[data.temp == data.temp.min()])

monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# Create a dataframe from scratch ------------------------------
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 89, 57]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")

