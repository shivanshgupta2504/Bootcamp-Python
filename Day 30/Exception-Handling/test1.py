try:
    file = open("data.txt")
    a_dict = {"key": "value"}
    print(a_dict["key"])
except FileNotFoundError:
    file = open("data.txt", "w")
    file.write("Something")
except KeyError as error_msg:
    print(f"The key {error_msg} doesn't exists")
else:  # works only when no error is generated
    content = file.read()
    print(content)
finally:  # Executes no matter what error occurs
    file.close()
    print("File is closed")


