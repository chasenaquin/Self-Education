import random


class Card:

    def __init__(self):
        self.face = ""
        self.suit = ""
        self.value = 0
        self.is_ace = False
        self.display = ""

    def generate_card(self, deck):
        if deck.is_empty:
            return "There are no more cards in the deck."

        # Generate Card and set instance attributes.
        self.face = random.choice(list(deck.deck.keys()))
        self.suit = random.choice(list(deck.suits.keys()))
        self.value = deck.deck[self.face]["value"]
        self.is_ace = self.face == "A"
        self.display = ""

        # Check card generation for availability and remove from deck.
        total_cards = deck.deck[self.face]["total"]
        total_suit_count = deck.deck[self.face]["suit_count"][self.suit]
        if total_cards != 0 and total_suit_count != 0:
            deck.deck_card_total -= 1
            deck.deck[self.face]["total"] -= 1
            deck.deck[self.face]["suit_count"][self.suit] -= 1
            self.display = str(self.face) + str(deck.suits[self.suit])
        else:
            self.generate_card(deck)

    def add_card_to_hand(self, hand):
        hand.hand.append(self)
        hand.display_hand.append(self.display)
