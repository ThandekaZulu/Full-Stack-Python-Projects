import pandas
# Squerrel Data
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20251201.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(black_squirrels_count)
print(red_squirrels_count)
print(grey_squirrels_count)

data_dict = {
  "Fur Color": ["Gray", "Cinnamon", "Black"],
  "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}
df = pandas.DataFrame(data_dict)
print(df)
# print(data_dict)

# ........
# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])
# print(data)

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(len(temp_list))
# temp_average = sum(data["temp"]) / len(data["temp"])
# another_way_cal_average = sum(temp_list) / len(temp_list)
# # Create dataframe from scratch
# data_dict = {
#   "students": ["Amy","James","Angela"],
#   "scores": [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")
# Get data in rows
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)
# 
# monday = data[data.day == "Monday"]
# print(monday)
# print(data[data.temp == data.temp.max()])
# print(data[data.day == "Monday"])
# max_row = data.loc[data["temp"].idxmax()]
# print(max_row)
# print(data(max([data.day == "Monday"])))
# print(data[data.condition == "Sunny"])

# ....get data in columns....
# print(data["temp"].max())
# print(data.condition)
# print(data["condition"])
# print(another_way_cal_average)
# print(temp_average)
# print(data["temp"].mean())



# ...................
# with open("weather_data.csv") as file:
#   data = file.readlines()
#   print(data)
# ------------------
# import csv

# with open("weather_data.csv") as data_file:
#   data = csv.reader(data_file)
#   temperature = []
#   # next(data)
#   # print(data)
#   for row in data:
#     if row[1] != "temp":
#       temperature.append(int(row[1]))
#   print(temperature)
