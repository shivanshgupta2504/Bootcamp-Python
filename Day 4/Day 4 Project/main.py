import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Welcome to Rock-Paper-Scissor Game!")
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.: "))
list_of_inputs = [rock, paper, scissors]
input_generate = random.randint(0, 2)
if (user_input == 0 and input_generate == 2) or (user_input == 1 and input_generate == 0) or (user_input == 2 and input_generate == 1):
    print(list_of_inputs[user_input])
    print("Computer Chose:")
    print(list_of_inputs[input_generate])
    print("You Win!")
elif (user_input == 2 and input_generate == 0) or (user_input == 0 and input_generate == 1) or (user_input == 1 and input_generate == 2):
    print(list_of_inputs[user_input])
    print("Computer Chose:")
    print(list_of_inputs[input_generate])
    print("You Lose!")
else:
    print(list_of_inputs[user_input])
    print("Computer Chose:")
    print(list_of_inputs[input_generate])
    print("It's a Draw!")

