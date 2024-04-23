from art import logo


# Add
def add(a, b):
    return a + b


# Subtract
def subtract(a, b):
    return a - b


# Multiply
def multiply(a, b):
    return a * b


# Divide
def divide(a, b):
    return a / b


# Exponent
def exponent(a, b):
    return a ** b


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '^': exponent,
}


def calculator():
    print(logo)
    num1 = float(input("What's the first number: "))
    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation from line above: ")
        num2 = float(input("What's the next number: "))
        if num2 == 0 and operation_symbol == '/':
            print("Division by Zero is not Allowed!!")
            calculator()
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        new = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation or 'e' to exit: ")

        if new == "y":
            num1 = answer
        elif new == 'e':
            print("Ending the Calculation")
            print(f"Your Final Result is: {answer}")
            should_continue = False
        else:
            should_continue = False
            calculator()  # recursion


calculator()


