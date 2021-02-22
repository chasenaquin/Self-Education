import random


def select_difficulty():
    difficulty_level = ""
    difficulty_level = input("What difficulty would you like: Easy or Hard? ").lower()
    if difficulty_level == "easy":
        return 10
    elif difficulty_level == "hard":
        return 5
    else:
        return "Please select a valid difficulty level."


def get_number():
    return random.randint(1, 100)


selected_number = get_number()

remaining_lives = select_difficulty()

is_over = False
while not is_over:
    guess = int(input("Guess a number: "))
    if guess == selected_number:
        print(f"The number was {selected_number}! You Win!")
        is_over = True
    elif guess > selected_number:
        print(f"{guess} is too high. Try again.")
        print(f"{remaining_lives} guesses remaining.")
        remaining_lives -= 1
    elif guess < selected_number:
        print(f"{guess} is too low. Try again.")
        remaining_lives -= 1
        print(f"{remaining_lives} guesses remaining.")

    if remaining_lives == 0:
        print("You have run out of guesses. You Lose!")
        exit()

# # Angelas Code
# from random import randint
# from art import logo
#
# EASY_LEVEL_TURNS = 10
# HARD_LEVEL_TURNS = 5
#
# #Function to check user's guess against actual answer.
# def check_answer(guess, answer, turns):
#   """checks answer against guess. Returns the number of turns remaining."""
#   if guess > answer:
#     print("Too high.")
#     return turns - 1
#   elif guess < answer:
#     print("Too low.")
#     return turns - 1
#   else:
#     print(f"You got it! The answer was {answer}.")
#
# #Make function to set difficulty.
# def set_difficulty():
#   level = input("Choose a difficulty. Type 'easy' or 'hard': ")
#   if level == "easy":
#     return EASY_LEVEL_TURNS
#   else:
#     return HARD_LEVEL_TURNS
#
# def game():
#   print(logo)
#   #Choosing a random number between 1 and 100.
#   print("Welcome to the Number Guessing Game!")
#   print("I'm thinking of a number between 1 and 100.")
#   answer = randint(1, 100)
#   print(f"Pssst, the correct answer is {answer}")
#
#   turns = set_difficulty()
#   #Repeat the guessing functionality if they get it wrong.
#   guess = 0
#   while guess != answer:
#     print(f"You have {turns} attempts remaining to guess the number.")
#
#     #Let the user guess a number.
#     guess = int(input("Make a guess: "))
#
#     #Track the number of turns and reduce by 1 if they get it wrong.
#     turns = check_answer(guess, answer, turns)
#     if turns == 0:
#       print("You've run out of guesses, you lose.")
#       return
#     elif guess != answer:
#       print("Guess again.")
#
#
# game()
