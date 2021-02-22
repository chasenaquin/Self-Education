from game_engine import GameEngine
from images import logo
import testing
from os import system

# TODO - Add in betting
# TODO - 3x payout for blackjack - pay out immediately if house doesnt have a blackjack
# TODO - Add push
# TODO - Add Double Down
# TODO - Split hand (Additional Wager) - can split any hand with same card values
# TODO - surrender - lose, but get half your wager back
# TODO - Need to test that when deck is empty, the game quits.


system('clear')
game_engine = GameEngine()
print(logo)
game_engine.create_house_player_instance()
game_engine.create_user_instance()
print("\nAs of now, it is just you and I sir. ")
game_engine.create_player_instances()
game_engine.initialize_deck()


def action_choice():
    user = game_engine.player_list[1]
    user_hand = game_engine.player_list[1].hands[0]
    hand_over = False
    while not hand_over:
        if user_hand.bust:
            user.action = "Bust"
            hand_over = True
        else:
            if user_hand.split_possibility:
                choice = input("(Surrender | Hit | Double |Stand | Split?): ").lower()
            else:
                choice = input("(Surrender | Hit | Double | Stand): ").lower()

            if choice == "split":
                print("Split Hand.")
                # game_engine.split_hand(user)
            elif choice == "hit":
                game_engine.draw_card(user, user_hand)
                user_hand.calculate_hand_total()
                user_hand.detect_bust()
            elif choice == "stand":
                user.action = "Stands"
                hand_over = True
        game_engine.game_display(mask_state="on")


def play_a_round():
    game_engine.total_hands += 1
    game_engine.create_player_hands()
    game_engine.deal()
    game_engine.game_display(mask_state="on")
    game_engine.detect_house_blackjack_victory()
    action_choice()
    game_engine.auto_draw_house()
    for player in range(2, len(game_engine.player_list)):
        # game_engine.auto_split_hand()
        game_engine.auto_draw_player(game_engine.player_list[player])
    game_engine.detect_winner()
    game_engine.output_final_display()
    game_engine.reset_game()


game_over = False
while not game_over:
    user_continue = input("Ready to play? (y/n): ").lower()  # Replace with make bet.
    if user_continue == "y":
        play_a_round()
    elif user_continue == "n":
        game_over = True
    else:
        print("Please make a valid choice.")
