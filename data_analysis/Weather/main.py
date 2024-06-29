# with open("weather_data.csv") as data_file:
#     data = []
#     data = data_file.readlines()
#     print(data)
#     data1 = []
#
# for i in data:
#     x = i.strip()
#     # print(x)
#     data1.append(x)
#
# print(data1)
#

# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     print(data)
# #
# #     data1 = []
# #     temp = []
# #
# #     for i in data:
# #         data1.append(i)
# #     print(data1)
# #
# #
# #     for i in data1[1:]:
# #         x = i[1]
# #         x = int(x)
# #         temp.append(x)
#     print(temp)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

max = data["temp"].max()

print(max)

print(data[data.temp == max])

monday = data[data.day == "Monday"]

tempc = monday.temp

tempf = (tempc * 9/5) + 32

print(tempf)





