# Python does not have blocks, as do some other languages (such as C/C++ or Java).
# Therefore, scoping unit in Python is a function.

# Global scope variable
global_var = "I'm global"


def example_function():
    # Local scope variable
    local_var = "I'm local"
    print(local_var + " inside the function\n")  # This will work

    if True:
        # Variables within conditional statements have no block scope
        # like other programming languages
        conditional_var = "I'm in a conditional"
        print(conditional_var + " inside the if statement\n")  # This will work

    print(conditional_var + " outside the if statement\n")
    # This will not raise an error


for _ in range(3):
    # Variables within loops have no block scope same as conditional statements
    loop_var = "I'm in a loop"
    print(loop_var + " inside for loop\n")  # This will work

print(loop_var + " outside for loop\n")
# This will raise a warning because loop_var is not defined outside the for loop
example_function()
print(global_var)  # This will work
# print(local_var)  # This will raise an error because local_var is defined inside the function
# print(conditional_var)  # This will raise an error because conditional_var is defined inside the function

# to access global scope variables inside function -> global var_name
# returning the modified global scope variable is also possible


