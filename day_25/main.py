# import csv
# import pandas
#
# # with open("weather-data.csv") as file:
# #     data = csv.reader(file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != 'temp':
# #             temperatures.append(int(row[1]))
# #     # print(temperatures)
#
# new_data = pandas.read_csv("weather-data.csv")
# # # print(type(new_data['temp']))
# # # print(type(new_data))
# #
# # temps = new_data['temp'].to_list()
# # print(temps)
# #
# # # length = len(temps)
# #
# # average = sum(temps) / len(temps)
# # print(average)
# #
# # print(new_data['temp'].mean())
# #
# # print(new_data['temp'].max())
#
# # max_day = new_data[new_data.temp == new_data.temp.max()]
# # print(max_day.condition)
#
#
# def new_temp(t):
#     return ((t * 9) / 5) + 32
#
#
# monday = new_data[new_data.day == "Monday"]
# print(monday)
# m_temp = monday.temp
#
# print(new_temp(m_temp))
#

import pandas
import csv

# with open("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv") as file:
#     data_object = csv.reader(file)
#     # print(data_object)

# Read the data with pandas and store it in all_data
all_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# fur_color = all_data["Primary Fur Color"].to_list()

# print(fur_color)

# Fetch data from the Primary Fur Color column or Series
# Fetch data from the series above with the specified parameters; Gray, Cinnamon or Black
# Use the len method to count the number of occurences.
gray = len(all_data[all_data["Primary Fur Color"] == "Gray"])
cinnamon = len(all_data[all_data["Primary Fur Color"] == "Cinnamon"])
black = len(all_data[all_data["Primary Fur Color"] == "Black"])

# Create a dictionary with the information and use the dictionary to create a data frame
color_count_dictionary = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [gray, cinnamon, black]
}
# Use the dictionary above to create a pandas Data Frame
df = pandas.DataFrame(color_count_dictionary)

# Convert the Data Frame to a csv format. 
df.to_csv("new_squirrel.csv")


# gray = 0
# cinnamon = 0
# black = 0
# for color in fur_color:
#     if color == "Gray":
#         gray += 1
#     elif color == "Cinnamon":
#         cinnamon += 1
#     elif color == "Black":
#         black += 1


# print(f"Gray = {gray}\nCinnamon = {cinnamon}\nBlack = {black}")

# color_dictionary = {"Fur Color": ["Gray", "Cinnamon", "Black"],
#                     "Count" : [gray, cinnamon, black]}
#
# print(color_dictionary)
# df = pandas.DataFrame(color_dictionary)
# df.to_csv("squirrel_count.csv")
# print(df)
