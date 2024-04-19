import random

# Generates a random whole number between 1 and 10
# (both inclusive)
random_int = random.randint(1, 10)
print(random_int)

# Generate a random floating point number
# [0, 1)
random_float = random.random()
print(random_float)

# To Generate a random floating point number
# in higher range like [0, 10)
random_float = random.random() * 10
print(random_float)
