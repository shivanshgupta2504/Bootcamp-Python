import random
import os
from art import logo

difficulty_map = {
    "easy": 10,
    "hard": 5,
}


def guess_the_number(difficulty):
    answer = random.randint(1, 100)
    numer_of_guesses = difficulty_map[difficulty]
    print(f"You have total {numer_of_guesses} number of guesses.")
    print("Now start guessing!!")
    is_play_complete = False

    while not is_play_complete:
        user_guess = int(input("Guess a number between 1 and 100: "))
        if user_guess == answer:
            print(f"Congrats you guessed the correct number {answer} 😎")
            is_play_complete = True
        elif user_guess < answer:
            print("Too Low...")
            print("Guess Again.")
            numer_of_guesses -= 1
            print(f"You have {numer_of_guesses} attempts left to guess the number")
        elif user_guess > answer:
            print("Too High...")
            print("Guess Again.")
            numer_of_guesses -= 1
            print(f"You have {numer_of_guesses} attempts left to guess the number")
        if numer_of_guesses == 0:
            print(f"Sorry You ran out of guesses. The correct number was {answer}")
            is_play_complete = True


def play_game():
    if input("Do you want to play the guessing game? (y/n): ") == 'y':
        os.system('clear')
        print(logo)
        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100")
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
        guess_the_number(difficulty)
        play_game()
    else:
        print("Thanks for playing!")


play_game()


