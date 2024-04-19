print("Welcome to the Rollercoaster")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        print("Child Tickets are $5.")
        bill += 5
    elif age <= 18:
        print("Youth Tickets are $7")
        bill += 7
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        print("Adult Tickets are $12.")
        bill += 12
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo.lower() == 'y':
        print("Pay extra $3.")
        bill += 3
    print(f"You have to pay ${bill}")
else:
    print("You cannot ride the rollercoaster")

