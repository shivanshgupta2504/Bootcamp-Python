import pandas as pd

data = pd.read_csv("weather_data.csv")
# data - DataFrame i.e. full table with rows and columns
print(data, "\n")
# data[column name] - Series i.e. a column in that table
print(data["temp"], "\n")

data_dict = data.to_dict()
print(data_dict, "\n")

temp_list = data["temp"].to_list()
print(temp_list, "\n")
print(f"Avg. temperature: {sum(temp_list) / len(temp_list)}\n")
print(f"Avg. temperature: {data["temp"].mean()}\n")
print(f"Max. temperature: {data["temp"].max()}\n")

# Get data from columns
print(data["day"])
# or
print(data.day)

# Gey data from rows
print(data[data.day == 'Monday'])
print(data[data.temp == data.temp.max()])

# Get info from a particular row
monday = data[data.day == 'Monday']
print(9/5 * monday.temp + 32)

# Create a DataFrame from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pd.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")
