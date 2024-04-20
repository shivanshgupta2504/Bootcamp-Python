import random
from hangman_words import word_list
from hangman_art import logo
from hangman_art import stages

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}.")

    # Check guessed letter and updating the display if letter found
    for position in range(word_length):
        if chosen_word[position] == guess:
            display[position] = chosen_word[position]

    # Check if user is wrong.
    if guess not in chosen_word:
        print(f"{guess} is not in the chosen word. You Lost a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"Word is {chosen_word}")
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])

