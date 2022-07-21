# difficult to clean data and access csv data

# with open("./weather_data.csv") as weather_data_file:
#     weather_data_list = weather_data_file.readlines()
#     print(weather_data_list)
# this just returns each row as a string


# a lot of 'faff' - for just one column of data
# import csv

#code to print temperature column values
# with open("./weather_data.csv") as data_file:
#     weather_data = csv.reader(data_file) # returns each row as a list of elements
#     temperatures = []
#     for row in weather_data:
#         if row[1] != "temp":
#             temperatures.append((int(row[1])))
#     print(temperatures)

import pandas

data = pandas.read_csv("./weather_data.csv")
# print(data) # returns table / "Dataframe"
# print(type(data)) # dataframe
# print(type(data["temp"])) # series

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list() #get data in columns and convert to a list
# print(temp_list)

# print(data["temp"].max())

# get data in a columns
# print(data["condition"])
# print(data.condition)

# get data in a row
# print(data[data.day == "Monday"]) #obtained via primary key column value

# print(data[data["temp"] == data.temp.max()]) #obtained via max value of the column temp

# monday = data[data.day == "Monday"]
# monday_temp_c = monday.temp
# print(monday_temp_c * (9 / 5) + 32) #farenheit

# print(data[data["day"] == "Monday"].temp * (9/5) + 32)

#how to create a dataframe from scratch

# data_dict = {
#     "students": ["Ajay", "Vivek", "Pavan"], 
#     "scores": [76, 99, 120]
# }

# data = pandas.DataFrame(data_dict)

# data.to_csv("new_data.csv")

# print(data)

#latest
# squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# colors = ['Gray', 'Black', 'Cinnamon']
# count = []

# for color in colors:
#     color_rows = squirrel_data[squirrel_data['Primary Fur Color'] == color]
#     count.append(color_rows["Primary Fur Color"].size) #the length function also works
#     # count.append(color_rows.size) # This also works

# squirrel_count_dict = {}
# squirrel_count_dict["Fur Color"] = colors
# squirrel_count_dict["Count"] = count
# squirrel_count = pandas.DataFrame(squirrel_count_dict)
# # print(squirrel_count)

# squirrel_count.to_csv("squirrel_count.csv")

