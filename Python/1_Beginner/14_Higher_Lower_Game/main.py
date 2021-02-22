# High Level Processes
# 1. Display title
# 2. Display 2 options vs each other.
# 3. Choose an options
# 4. check the followers for each and determine if choice was correct or not.
# 5. If choice correct, keep the correct choice and generate 1 additional option. Score += 1
# 6. Continue this until the user answers incorrectly.

import random
from os import system
from higher_lower_art import logo, vs
from higher_lower_game_data import data


def generate_option():
    """returns an option out of the data list"""
    return random.choice(data)


def display_option(option_choice, option):
    """Formats and prints the option. Needs input of option_choice and option."""
    print(f"{option_choice}: {option['name']}, {option['description']}, from {option['country']}.")


def get_choice(first_option, second_option):
    """returns choice option"""
    choice = input("Who has more instagram followers: A or B: ").lower()
    if choice == "a":
        return first_option
    elif choice == "b":
        return second_option
    else:
        return "Please select a valid option."


def check_followers(choice, first_option, second_option, score):
    """Checks if the user choice is correct or not. Returns score if correct"""
    more_followers = max(first_option['follower_count'], second_option['follower_count'])
    if choice['follower_count'] >= more_followers:
        score += 1
        return score
    else:
        return None


def higher_lower_game():
    score = 0
    first_option = generate_option()

    game_over = False
    while not game_over:
        system('clear')
        print(logo)
        print(f"Your current score is: {score}")
        display_option(option_choice="Option A", option=first_option)
        print(vs)
        second_option = generate_option()
        if first_option == second_option:
            second_option = generate_option()
        display_option(option_choice="Option B", option=second_option)
        print("\n")

        choice = get_choice(first_option=first_option, second_option=second_option)
        score = check_followers(choice=choice, first_option=first_option, second_option=second_option, score=score)

        # This doesnt display score at end.
        # I may come back and fix this, but not necessary.
        # I will have to rewrite check_followers() and this if statement.
        if score is None:
            print("You lose. Try again.")
            print(score)
            game_over = True
        else:
            first_option = choice

        print(score)


higher_lower_game()

# # Angelas Code
# from game_data import data
# import random
# from art import logo, vs
# from replit import clear
#
# def get_random_account():
#   """Get data from random account"""
#   return random.choice(data)
#
# def format_data(account):
#   """Format account into printable format: name, description and country"""
#   name = account["name"]
#   description = account["description"]
#   country = account["country"]
#   # print(f'{name}: {account["follower_count"]}')
#   return f"{name}, a {description}, from {country}"
#
# def check_answer(guess, a_followers, b_followers):
#   """Checks followers against user's guess
#   and returns True if they got it right.
#   Or False if they got it wrong."""
#   if a_followers > b_followers:
#     return guess == "a"
#   else:
#     return guess == "b"
#
#
# def game():
#   print(logo)
#   score = 0
#   game_should_continue = True
#   account_a = get_random_account()
#   account_b = get_random_account()
#
#   while game_should_continue:
#     account_a = account_b
#     account_b = get_random_account()
#
#     while account_a == account_b:
#       account_b = get_random_account()
#
#     print(f"Compare A: {format_data(account_a)}.")
#     print(vs)
#     print(f"Against B: {format_data(account_b)}.")
#
#     guess = input("Who has more followers? Type 'A' or 'B': ").lower()
#     a_follower_count = account_a["follower_count"]
#     b_follower_count = account_b["follower_count"]
#     is_correct = check_answer(guess, a_follower_count, b_follower_count)
#
#     clear()
#     print(logo)
#     if is_correct:
#       score += 1
#       print(f"You're right! Current score: {score}.")
#     else:
#       game_should_continue = False
#       print(f"Sorry, that's wrong. Final score: {score}")
#
# game()
#
#
# # Generate a random account from the game data.
#
# # Format account data into printable format.
#
# # Ask user for a guess.
#
# # Check if user is correct.
# ## Get follower count.
# ## If Statement
#
# # Feedback.
#
# # Score Keeping.
#
# # Make game repeatable.
#
# # Make B become the next A.
#
# # Add art.
#
# # Clear screen between rounds.
