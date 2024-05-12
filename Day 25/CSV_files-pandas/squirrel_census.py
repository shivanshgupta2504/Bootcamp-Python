import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

count_cinnamon = data[data["Primary Fur Color"] == "Cinnamon"]
count_black = data[data["Primary Fur Color"] == "Black"]
count_gray = data[data["Primary Fur Color"] == "Gray"]
print(len(count_cinnamon))
print(len(count_black))
print(len(count_gray))

my_dict = {
    "Fur Color": ['Gray', 'Cinnamon', 'Black'],
    "Count": [len(count_gray), len(count_cinnamon), len(count_black)],
}

my_df = pd.DataFrame(my_dict)
# print(my_df)
my_df.to_csv("squirrel_count.csv")

