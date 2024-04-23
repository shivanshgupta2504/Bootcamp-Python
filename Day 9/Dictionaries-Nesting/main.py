# Creating a dictionary
programming_dict = {
    "Bug": "An error in a program",
    "Function": "A piece of code that does something",
    "Loop": "The a piece of code that does something over and over again",
}
# Accessing any value
print(programming_dict["Bug"])

# Adding new items to the dictionary
programming_dict["Variable"] = "An area to store values and objects"
print(programming_dict)

# Creating an empty dictionary or wipe an existing dictionary
empty_dictionary = {}
# programming_dict = {}

# Edit an item in the dictionary
# Values are editable, keys are not
programming_dict["Bug"] = "A moth in your computer"
print(programming_dict["Bug"])

# Loop through the dictionary
for key in programming_dict:  # it loops via keys of the dictionary
    print(key)
    print(programming_dict[key])
