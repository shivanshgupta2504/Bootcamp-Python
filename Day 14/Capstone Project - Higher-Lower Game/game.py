from game_data import data
from art import logo, vs
import os
import random


def generate_random_account():
    """Generates a random choice from the given data"""
    return random.choice(data)


def format_data(account):
    """Formats the account into printable form"""
    return f"{account['name']}, {account['description']}, from {account['country']}"


def check_answer(choice, follower_count_a, follower_count_b):
    """Based on the counts from both accounts it compares user's choice and
    return whether it is right choice or not"""
    if follower_count_a > follower_count_b:
        return choice == 'A'
    else:
        return choice == 'B'


def game():
    is_game_finish = False
    score = 0
    account_a = generate_random_account()
    account_b = generate_random_account()

    while not is_game_finish:
        account_a = account_b
        account_b = random.choice(data)
        os.system('clear')
        print(logo)

        if score != 0:
            print(f"\nYou're right! Current score: {score}.\n")

        while account_a == account_b:
            account_b = generate_random_account()

        print(f"\nCompare A: {format_data(account_a)}\n")
        print(vs)
        print(f"\nAgainst B: {format_data(account_b)}\n")

        follower_count_a = account_a['follower_count']
        print(follower_count_a)
        follower_count_b = account_b['follower_count']
        print(follower_count_b)

        choice = input("Who has more followers? Type 'A' or 'B': ").upper()

        is_right = check_answer(choice, follower_count_a, follower_count_b)

        if is_right:
            score += 1
            continue
        else:
            os.system('clear')
            print(logo)
            print(f"Sorry that's wrong. Final Score: {score}")
            is_game_finish = True


game()

print(f"\nThanks for playing!")

