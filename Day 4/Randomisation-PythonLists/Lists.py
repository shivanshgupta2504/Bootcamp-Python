# Data Structure of items of any data type
# [] - type of brackets used
# Ordered Items meaning items have indices associated
# Mutable

# Simple List
num_list = [1, 2, 3, 4, 5]
print(num_list)
# Indexing
print(num_list[3])  # Positive index
print(num_list[-2])  # Negative index
# Mutable
num_list[0] = 10
print(num_list)
# Add something in last
num_list.append(6)
print(num_list)
# Extend the list with another list
num_list.extend([7, 8, 9])
print(num_list)
# Nested List
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
main_list = [list1, list2]
print(main_list)  # Whole nested list
print(main_list[0])  # first list of nested list
print(main_list[1][3])  # fourth item of second list of nested list

