import pandas

data = pandas.read_csv("sqrl.csv")

# print(data.nunique(data["Primary Fur Color"]))

colors = data["Primary Fur Color"]

print(colors.value_counts())

df = colors.value_counts()

df.to_csv("squirrel_count.csv")