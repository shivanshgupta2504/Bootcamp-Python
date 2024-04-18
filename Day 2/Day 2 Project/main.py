# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
print("Welcome to Tip Calculator!")
# Taking inputs
total_bill = input("What was the total bill? $")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
number_of_people = input("How many people to split the bill? ")
# Calculating each person bill
bill_split = (float(total_bill) / int(number_of_people)) * ((int(tip) + 100) / 100)
bill_split = "{:.2f}".format(round(bill_split, 2))  # changes to string
print(type(bill_split))
# Printing
print(f"Each person should pay: ${bill_split}")


