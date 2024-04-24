import random
from art import logo
import os


def deal_card():
    """It returns a random card from the Deck(list) of Cards"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    """Calculates the sum(score) of in the given list of cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    """It compares user score with computer score and returns the final result"""
    if computer_score == user_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has BlackJack 😱"
    elif user_score == 0:
        return "Win with a BlackJack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You Win 😃"
    else:
        return "You Lose 😤"


def play_game():
    """Initializes a New Game"""
    print(logo)
    print("Welcome to the Black-Jack Game!!")
    # Give 2 cards to each user and computer
    user_cards = []
    computer_cards = []
    user_score = 0
    computer_score = 0
    is_game_over = False
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your Cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first Card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n':") == 'y':
    os.system('clear')
    play_game()






