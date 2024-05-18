# try:
#     file = open("data.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["key"])
# except FileNotFoundError:
#     file = open("data.txt", "w")
#     file.write("Something")
# except KeyError as error_msg:
#     print(f"The key {error_msg} doesn't exists")
# else:  # works only when no error is generated
#     content = file.read()
#     print(content)
# finally:  # Executes no matter what error occurs
#     raise TypeError("This is error message I made up.")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:  # raising our own exceptions
    raise ValueError("Human height should not be more than 3m")

bmi = weight / height ** 2
print(bmi)


