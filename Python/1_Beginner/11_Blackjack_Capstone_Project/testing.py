from prettytable import PrettyTable


def check_ace_value(game_engine):
    for player in game_engine.player_list:
        for card in player.hands[0].hand:
            if card.face == "A":
                print(f"Player {player.id} - Ace Value: {card.value}")


def display_player_details(player):
    print("\n=====[ PLAYER DETAILS ]=====")
    print(f"Player ID: {player.id}")
    print(f"Player is_house: {player.is_house}")
    print(f"Player Name: {player.name}")
    print(f"Player Hand: {player.hands}")


def display_hand_attributes(hand):
    print("\n=====[ HAND DETAILS ]=====")
    print(f"Hand List: {hand.hand}")
    print(f"Display Hand: {hand.display_hand}")
    print(f"Hand Total: {hand.total}")
    print(f"Split Possibility: {hand.split_possibility}")
    print(f"Blackjack?: {hand.is_blackjack}")


def display_card_attributes(card):
    print("\n=====[ CARD DETAILS ]=====")
    print(f"Face: {card.face}")
    print(f"Suit: {card.suit}")
    print(f"Value: {card.value}")
    print(f"Ace?: {card.is_ace}")
    print(f"Display: {card.display}")


def run_deck_report(deck, *arg):
    """Prints a report of totals or suit totals per card. No return value."""
    print(f"\n=====[ DECK DETAILS {arg} ]=====")
    print(f"Deck Total: {deck.deck_card_total}")
    print(f"Empty?: {deck.is_empty}\n")

    table = PrettyTable()
    table.field_names = ["Identifier", "Total"]
    table.align = "l"

    if arg:
        table.field_names = ["Suit", "Total"]
        print(f"\nCard: {arg[0]}")
        for suit in deck.deck[arg[0]]['suit_count']:
            table.add_row([suit, deck.deck[arg[0]]['suit_count'][suit]])
    else:
        table.field_names = ["Card", "Total"]
        print("Card Totals:")
        for card in deck.deck:
            table.add_row([card, deck.deck[card]['total']])
    print(table)


def split_hand_testing(game_engine):
    for player in range(2, len(game_engine.player_list)):
        for hand in game_engine.player_list[player].hands:
            if hand.split_possibility:
                print(f"{game_engine.player_list[player].name}: hand {hand}")
                display_hand_attributes(hand)
