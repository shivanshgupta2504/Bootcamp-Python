from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_not_encrypt = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ':'
                      , ';', ',', '\'', '\"', '!', '@', '#', '$', '%', '&', '^'
                      , '*', '+', '-', '_', '`', '~', '/', '|', '(', ')', '{'
                      , '}', '[', ']', '<', '>', '=', '?', '\\']

encoded = False
cipher = False


def caesar(text, shift):
    if not encoded:
        text = text.lower()
        text_words = text.split(' ')
        encrypted_words = []
        # print(text_words)
        for word in text_words:
            word_letters = list(word)
            # print(word_letters)
            for i in range(len(word_letters)):
                if word_letters[i] in should_not_encrypt:
                    continue
                index_of_letter = alphabet.index(word_letters[i])
                new_letter = alphabet[(index_of_letter + shift) % 26]
                word_letters[i] = new_letter

            # print(word_letters)
            encrypted_words.append(''.join(word_letters))

        # print(encrypted_words)
        encrypted_message = ' '.join(encrypted_words)
        print(f"The encoded text is: {encrypted_message}")

    if encoded:
        text = text.lower()
        text_words = text.split(' ')
        decrypted_words = []
        #
        for word in text_words:
            word_letters = list(word)
            for i in range(len(word_letters)):
                if word_letters[i] in should_not_encrypt:
                    continue
                index_of_letter = alphabet.index(word_letters[i])
                new_letter = alphabet[(index_of_letter + 26 - shift) % 26]
                word_letters[i] = new_letter

            decrypted_words.append(''.join(word_letters))

        decrypted_message = ' '.join(decrypted_words)
        print(f"The decoded text is: {decrypted_message}")


print(logo)

while not cipher:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    if not encoded and direction == 'decode':
        print("Message is not encoded yet...")
        print("Please encode it first.")
        continue

    if direction == 'encode' and not encoded:
        plain_text = input("Type your message:\n").lower()
        shift_number = int(input("Type the shift number:\n"))
        print("Encrypting the message...")
        caesar(text=plain_text, shift=shift_number % 26)
        encoded = True
        cipher = True

while True:
    print("Do you want to restart the Cipher again? Enter 'y' to continue or any other letter ro exit")
    restart = input()
    if restart == 'y':
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

        if encoded and direction == 'encode':
            print("Message is already encoded...")
            print("Please decode it.")
            print("Cipher is running again to decode the message....\n")
            continue

        if direction == 'decode' and encoded:
            encrypted_text = input("Type your message:\n")
            shift_number = int(input("Type the shift number:\n"))
            print("Decrypting the message...")
            caesar(text=encrypted_text, shift=shift_number % 26)
            print("Caesar Cipher is done!")
            exit(0)

    else:
        print("Message is encoded only.")
        print("Kindly remember the encoded message and shift.")
        print("Cipher is running again to decode the message....\n")
        continue





