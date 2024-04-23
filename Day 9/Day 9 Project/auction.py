from art import logo
import os

print(logo)

print("Welcome to the Secret Auction Program")
end = False
auction = {}

while not end:
    name = input("What is your name: ")
    bid = int(input("What's your bid: $"))
    auction[name] = bid
    ask = input("Are there any other bidders? Type 'yes' or 'no': ")
    if ask == 'yes':
        os.system('clear')
        continue
    else:
        os.system('clear')
        highest_bid = 0
        winner = ''
        for name in auction:
            if auction[name] > highest_bid:
                highest_bid = auction[name]
                winner = name

        print(f"The winner is {winner} with a bid of {highest_bid}")
        print("Participants of the Auction are :-")
        for name in auction:
            print(f"{name} : {auction[name]}")
        end = True

