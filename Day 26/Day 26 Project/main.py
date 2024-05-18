import pandas as pd

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

df = pd.read_csv("nato_phonetic_alphabet.csv")


phonetic_code = {row.letter: row.code for (index, row) in df.iterrows()}


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        word_list = [phonetic_code[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in alphabet please")
        generate_phonetic()
    else:
        print(word_list)


generate_phonetic()
