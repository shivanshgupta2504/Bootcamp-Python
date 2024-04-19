print("The Love Calculator is calculating your score...")
name1 = input()  # What is your name?
name2 = input()  # What is their name?
name1 = name1.lower()
name2 = name2.lower()

combine_name = name1 + name2

count_true = 0
count_love = 0

count_true += combine_name.count('t')+combine_name.count('r')+combine_name.count('u')+combine_name.count('e')
count_love += combine_name.count('l')+combine_name.count('o')+combine_name.count('v')+combine_name.count('e')

love_score = count_true * 10 + count_love

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")

