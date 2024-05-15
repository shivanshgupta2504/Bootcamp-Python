def add(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum


print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=2, multiply=5)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.year = kwargs.get("year")


my_car = Car(make="Nissan")
print(my_car.model)
