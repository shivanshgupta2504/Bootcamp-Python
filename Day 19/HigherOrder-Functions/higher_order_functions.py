def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def calculator(func, n1, n2):  # higher order function
    """
    This is a higher order function that takes a function as an argument
    and returns the result of that function.
    """
    return func(n1, n2)


print(calculator(func=divide, n1=2, n2=3))

