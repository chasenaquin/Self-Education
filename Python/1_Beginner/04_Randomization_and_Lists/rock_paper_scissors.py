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


import random
from os import system

choices = ["rock", "paper", "scissors"]

print("1 : Rock")
print("2 : Paper")
print("3 : Scissors")
input_choice = input("What do you choose? ").lower()
system('clear')

user_choice = choices[int(input_choice) - 1]
print(f"You have chosen: {user_choice}")
if user_choice == "rock":
    print(rock)
elif user_choice == "paper":
    print(paper)
elif user_choice == "scissors":
    print(scissors)
else:
    print("Something went wrong with user choice.")

computer_choice = random.choice(choices)
print(f"Computer Chooses: {computer_choice}")
if computer_choice == "rock":
    print(rock)
elif computer_choice == "paper":
    print(paper)
elif computer_choice == "scissors":
    print(scissors)
else:
    print("Something went wrong with computer choice.")

#Maybe i can tunr this into a function.

if user_choice == "rock" and computer_choice == "paper":
    print ("Paper beats rock. Computer Wins.")
elif user_choice =="rock" and computer_choice == 'scissors':
    print("Rock beats Scissors. You win")

if user_choice == "paper" and computer_choice =="rock":
    print ("Paper beats rock. You Win.")
elif user_choice == "paper" and computer_choice == "scissors":
    print("Scissors beats Paper. Computer Wins.")

if user_choice == "scissors" and computer_choice =="rock":
    print ("Rock beats Scissors. Computer Wins.")
elif user_choice == "scissors" and computer_choice == "paper":
    print("Scissors beats Paper. You Win.")

if user_choice == computer_choice:
    print(f"Both choose: {user_choice}. It is a tie")


# #Angelas Code
#
# import random
#
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
#
# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''
#
# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
# game_images = [rock, paper, scissors]
#
# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# print(game_images[user_choice])
#
# computer_choice = random.randint(0, 2)
# print("Computer chose:")
# print(game_images[computer_choice])
#
# if user_choice >= 3 or user_choice < 0:
#   print("You typed an invalid number, you lose!")
# elif user_choice == 0 and computer_choice == 2:
#   print("You win!")
# elif computer_choice == 0 and user_choice == 2:
#   print("You lose")
# elif computer_choice > user_choice:
#   print("You lose")
# elif user_choice > computer_choice:
#   print("You win!")
# elif computer_choice == user_choice:
#   print("It's a draw")
#
# ####### Debugging challenge: #########
# #Try running this code and type 5.
# #It will give you an IndexError and point to line 32 as the issue.
# #But on line 38 we are trying to prevent a crash by detecting
# #any numbers great than or equal to 3 or less than 0.
# #So what's going on?
# #Can you debug the code and fix it?
# #Solution: https://repl.it/@appbrewery/rock-paper-scissors-debugged-end
