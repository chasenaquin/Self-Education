from images import logo
from player import Player
from deck import Deck
from hand import Hand
from card import Card

from prettytable import PrettyTable
from os import system


def strike_out(text):
    result = ''
    for char in text:
        result = result + char + '\u0336'
    return result


class GameEngine:

    def __init__(self):
        self.player_list = []
        self.deck = Deck()
        self.total_hands = 0

    def create_house_player_instance(self):
        """Initializes the house player."""
        player = Player()
        player.initialize_house(self.player_list)

    def create_user_instance(self):
        """Initializes the user player."""
        player = Player()
        player.initialize_user(self.player_list)

    def create_player_instances(self):
        """Initializes all player instances."""
        player_count = int(input("How many other players would you like: "))
        for player in range(0, int(player_count)):
            new_player = Player()
            new_player.initialize_player(self.player_list)
        print("\n")

    def initialize_deck(self):
        """Initializes the deck instance."""
        self.deck.set_deck_count()

    def create_player_hands(self):
        """Creates an empty hand list instance for each player."""
        for player in self.player_list:
            new_hand = Hand()
            player.hands.append(new_hand)

    def draw_card(self, player, hand):
        """Generates a card and appends it to the selected hand."""
        new_card = Card()
        new_card.generate_card(self.deck)
        new_card.add_card_to_hand(hand)
        hand.calculate_hand_total()

    def detect_house_blackjack_victory(self):
        if self.player_list[0].hands[0].is_blackjack:
            self.player_list[0].wins += 1
            return "House has a Blackjack. House wins."

    def deal(self):
        """Deal 2 cards to every players hand."""
        for player in self.player_list:
            for card in range(0, 2):
                self.draw_card(player, player.hands[0])
            player.hands[0].calculate_hand_total()
            player.hands[0].detect_split_possibility()
            player.hands[0].detect_blackjack()
        self.detect_house_blackjack_victory()

    # def split_hand(self, player):
    #     """Creates an additional house hand. Moves a card to the new hand. Draws a card for each hand."""
    #     new_hand = Hand()
    #     new_hand.add_hand_to_player(player)
    #     self.draw_card(player, new_hand)
    #     self.draw_card(player, new_hand)
    #
    # def auto_split_hand(self):
    #     for player in self.player_list:
    #         for hand in player.hands:
    #             print(hand)
    #             # if hand.split_possibility:
    #             #     self.split_hand(player)

    def auto_draw_house(self):
        """House will continue to draw cards until hand total is above 17."""
        house = self.player_list[0]
        is_done = False
        while not is_done:
            for hand in house.hands:
                hand.calculate_hand_total()
                if hand.total <= 17:
                    self.draw_card(house, hand)
                    hand.detect_bust()
                elif hand.total > 21:
                    is_done = True
                    self.player_list[0].action = "Bust"
                else:
                    house.action = "Stands"
                    is_done = True
                hand.calculate_hand_total()

    def auto_draw_player(self, player):
        """Players will auto-draw if 15 or under."""
        is_done = False
        while not is_done:
            for hand in player.hands:
                hand.calculate_hand_total()
                if hand.total <= 15:
                    self.draw_card(player, hand)
                    hand.detect_bust()
                elif hand.total > 21:
                    is_done = True
                    player.action = strike_out("Bust")
                else:
                    player.action = "Stands"
                    is_done = True
                hand.calculate_hand_total()

    def detect_winner(self):
        hand_values = []
        for player in self.player_list:
            for hand in player.hands:
                if hand.total <= 21:
                    hand_values.append(hand.total)

        winning_hand = max(hand_values)
        for player in self.player_list:
            for hand in player.hands:
                if hand.total == winning_hand:
                    player.is_winner = True
                    player.wins += 1
                else:
                    player.is_winner = ""

    def reset_game(self):
        for player in self.player_list:
            for hand in player.hands:
                hand.reset_hand()
                player.reset_player_hand()

    def display_wins(self):
        table = PrettyTable()
        table.field_names = ["Player", "Wins", "Win Ratio", "Money"]
        table.align = "l"
        for player in self.player_list:
            if player.wins > 0:
                table.add_row([player.name, player.wins, "{:.0%}".format(player.wins / self.total_hands), "$" +
                               str(player.money)])
            else:
                table.add_row([player.name, player.wins, 0, "$" + str(player.money)])
        print(f"{table}")

    def game_display(self, mask_state):
        system('clear')
        self.display_wins()
        print(logo)
        for player in self.player_list:
            for hand in player.hands:
                hand.detect_split_possibility()
                hand.calculate_hand_total()
                hand.detect_blackjack()
                hand.detect_bust()

        table = PrettyTable()
        table.field_names = ["ID", "Player", "Hand"]
        table.align = "l"

        for player in self.player_list:
            for hand in player.hands:
                if player.id == 1:
                    table.add_row([player.id, player.name, hand.display_hand])
                else:
                    if mask_state == "on":
                        if player.id == 0:
                            hand.display_hand[0] = "▓"
                        table.add_row(
                            [player.id, player.name, hand.display_hand])
                    elif mask_state == "off":
                        hand.display_hand[0] = str(hand.hand[0].face) + str(self.deck.suits[hand.hand[0].suit])
                        table.add_row(
                            [player.id, player.name, hand.display_hand])
                    else:
                        print("something broke.")
        print(f"\n{table}\n")

        user = self.player_list[1]
        print(f"_____ {user.name} _____")
        for hand in user.hands:
            print(f"{hand.display_hand}\n")

    def output_final_display(self):
        self.display_wins()
        system('clear')
        print(logo)
        for player in self.player_list:
            for hand in player.hands:
                hand.detect_split_possibility()
                hand.calculate_hand_total()
                hand.detect_blackjack()
                hand.detect_bust()

        table = PrettyTable()
        table.field_names = ["ID", "Player", "Hand", "Total", "Action", "Winner"]
        table.align = "l"

        for player in self.player_list:
            for hand in player.hands:
                hand.display_hand[0] = str(hand.hand[0].face) + str(self.deck.suits[hand.hand[0].suit])
                if hand.total > 21:
                    table.add_row([strike_out(str(player.id)), strike_out(str(player.name)), hand.display_hand,
                                   strike_out(str(hand.total)), strike_out(str(player.action)),
                                   strike_out(str(player.is_winner))])
                else:
                    table.add_row(
                        [player.id, player.name, hand.display_hand, hand.total, player.action, player.is_winner])
        print(f"{table}\n")
