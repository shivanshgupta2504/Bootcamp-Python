import test2

print("Test1 says: " + __name__)

if __name__ == "test2":  # it does not work
    test2.welcome()

if __name__ == "__main__":  # it works -> it defines the start point of execution
    test2.welcome()