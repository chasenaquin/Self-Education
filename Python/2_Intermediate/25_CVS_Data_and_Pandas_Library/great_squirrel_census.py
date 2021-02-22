import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])
print(f"Gray Squirrels: {gray}")
print(f"Gray Squirrels: {cinnamon}")
print(f"Gray Squirrels: {black}")

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, cinnamon, black]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel_Count.csv")