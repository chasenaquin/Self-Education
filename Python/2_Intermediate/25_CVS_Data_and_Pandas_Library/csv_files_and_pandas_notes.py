# Reading CSV Files

# with open("weather_data.csv") as weather_data_file:
#     weather_data_list = weather_data_file.readlines()
#
# print(weather_data_list)

# import csv
#
# with open("weather_data.csv") as weather_data_file:
#     temp_list = []
#     # Creates an object. Can be looped through
#     data = csv.reader(weather_data_file)
#     for row in data:
#         temp = row[1]
#         # Dropped the column title.
#         if row[1] != "Temperature":
#             temp_list.append(int(temp))
#
# print(temp_list)

# Pandas

import pandas
data = pandas.read_csv("weather_data.csv")
print(data)

#Pandas core frame DataFrame (whole table)
print(type(data))

# Automatically takes the top row as column titles
# print(data["Temperature"])

# Pandas Series = columns
print(type(data["Temperature"]))

# Make a dictionary out of the dataframe
data_dict = data.to_dict()
print(data_dict)

# Make a series into a list
temp_list = data["Temperature"].to_list()
print(temp_list)

# temp_mean = sum(temp_list) / len(temp_list)
# print(temp_mean)

print(data["Temperature"].mean())
print(data["Temperature"].max())

# Another method to work with columns
print(data.Condition)

# Get data from rows
print(data[data.Day == "Monday"])

# Data Frame [ conditional filtering ] = Display the row
print(data[data.Temperature == data.Temperature.max()])

monday = data[data.Day == "Monday"]
print(monday.Condition)


# Create a DataFrame from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
score_data = pandas.DataFrame(data_dict)
score_data.to_csv("Score_Data.csv")