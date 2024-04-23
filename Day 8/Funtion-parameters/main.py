def greet():
    print("Hello, How are you?")
    print("Everything Good?")
    print("What are you doing?")


greet()  # function without inputs


def greet_with_name(name):
    print(f"Hello, How are you {name}?")
    print(f"What are you doing {name}?")


greet_with_name("Shivansh")


def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it in {location}")


greet_with("Shivansh", "Bangalore")
greet_with(name="Diya", location="Dehradun")
