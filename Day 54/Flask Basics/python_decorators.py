import time

def delay_decorator(function):  # A decorator function which gives extra functionality to the function passed
    def wrapper_function():
        time.sleep(2)
        # Do something before function
        function()
        # Do something before function
    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")


@delay_decorator
def say_bye():
    print("Bye")


say_hello()  # after decorating yhe function we have to run it
say_bye()

# "@delay_decorator" can also be written as (syntactic sugar)
decorated_function = delay_decorator(say_hello)
decorated_function()  # executes say_hello function with time delay
