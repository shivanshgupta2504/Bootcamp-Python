import random
from hangman_words import word_list
from hangman_art import *

chosen_word = random.choice(word_list)
lives = 6
end_of_game = False

# print(chosen_word)

# Create an empty list of '_' as many as in the chosen word
display = []
for i in range(len(chosen_word)):
    display.append('_')

print(logo)

while not end_of_game:
    guess = input("Guess a letter: ").lower()  # guess a letter

    if guess in display:
        print(f"You've already guessed {guess}.")
        continue

    # If letter found replace all it's occurrences in display
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = chosen_word[i]

    # if letter not found
    if guess not in chosen_word:
        print(f"'{guess}' is not in the chosen word")
        lives -= 1
        if lives == 0:
            print(f"'{chosen_word}' is the right answer")
            end_of_game = True
            print("You lose.")

    print(display)

    if "_" not in display:
        print(''.join(display))
        end_of_game = True
        print("You win!")

    print(stages[lives])



