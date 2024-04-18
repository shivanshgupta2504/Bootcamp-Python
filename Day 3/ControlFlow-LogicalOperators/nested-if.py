height = int(input("What is your height? "))

if height > 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5.")
    else:
        print("Please pay $12.")
else:
    print("You cannot ride the rollercoaster")

