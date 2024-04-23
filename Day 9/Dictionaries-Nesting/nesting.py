# Nesting a list in a dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}
print(travel_log)

# Nesting a dictionary in a dictionary
# it shows how many times I've traveled to each place in a country
travel_log = {
    "France": {"Paris": 3, "Lille": 1, "Dijon": 2},
    "Germany": {"Berlin": 4, "Hamburg": 1, "Stuttgart": 0},
}
print(travel_log["Germany"])

