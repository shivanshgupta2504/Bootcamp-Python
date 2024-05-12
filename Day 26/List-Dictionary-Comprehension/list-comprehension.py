# List Comprehension - new_list = [new_item for item in list <conditions>]
org_list = [1, 2, 3]
new_list = [n + 1 for n in org_list]
print(new_list)

# On strings
name = "Shivansh"
letters = [letter for letter in name]
print(letters)

# On ranges
double_list = [2 * n for n in range(1, 5)]
print(double_list)

# Conditional list comprehension
even_list = [n for n in range(1, 11) if n % 2 == 0]
print(even_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
long_names = [name.upper() for name in names if len(name) >= 5]
print(long_names)
