import random
from os import system
from hangman_word_list import word_list
from hangman_art import logo
from hangman_art import stages


system('clear')
print(logo)

computer_chosen_word = random.choice(word_list)

chosen_word_list = []
for letter in computer_chosen_word:
    chosen_word_list += letter

display_text_list = []
for letter in computer_chosen_word:
    display_text_list += "_"

print(f"The word is: {len(computer_chosen_word)} letters.\n")
print(' '.join(display_text_list))
print("\n")
print(stages[6])

lives = 6
is_over = False

while not is_over:
    chosen_letter = input("What letter do you want to try: ").lower()
    print("\n")

    for position in range(0, len(chosen_word_list)):
        if chosen_letter == chosen_word_list[position]:
            display_text_list[position] = chosen_letter

    if chosen_letter in display_text_list:
        print("You have already guessed this letter.")

    if chosen_letter not in chosen_word_list:
        lives -= 1

    print(' '.join(display_text_list))
    print(stages[lives])
    print(f"Lives Remaining: {lives}")
    if lives == 0:
        is_over = True
        print(f"The word was: {computer_chosen_word}")
        print("You lose. You Loser!")

    if display_text_list == chosen_word_list:
        is_over = True
        print("You win!")



# #Angelas Code
#
# import random
#
# #TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
# #Delete this line: word_list = ["ardvark", "baboon", "camel"]
# from hangman_words import word_list
#
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)
#
# end_of_game = False
# lives = 6
#
# #TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
# from hangman_art import logo
# print(logo)
#
# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')
#
# #Create blanks
# display = []
# for _ in range(word_length):
#     display += "_"
#
# while not end_of_game:
#     guess = input("Guess a letter: ").lower()
#
#     #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
#     if guess in display:
#         print(f"You've already guessed {guess}")
#
#     #Check guessed letter
#     for position in range(word_length):
#         letter = chosen_word[position]
#         #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#         if letter == guess:
#             display[position] = letter
#
#     #Check if user is wrong.
#     if guess not in chosen_word:
#         #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
#         print(f"You guessed {guess}, that's not in the word. You lose a life.")
#
#         lives -= 1
#         if lives == 0:
#             end_of_game = True
#             print("You lose.")
#
#     #Join all the elements in the list and turn it into a String.
#     print(f"{' '.join(display)}")
#
#     #Check if user has got all letters.
#     if "_" not in display:
#         end_of_game = True
#         print("You win.")
#
#     #TODO-2: - Import the stages from hangman_art.py and make this error go away.
#     from hangman_art import stages
#     print(stages[lives])
