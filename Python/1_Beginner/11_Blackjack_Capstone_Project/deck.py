# coding=utf-8
class Deck:

    def __init__(self):
        self.deck_count = 0
        self.deck_card_total = 0
        self.is_empty = False
        self.suits = {"spades": "♤", "hearts": "♡", "clubs": "♧", "diamonds": "♢"}
        self.deck = {"A":  # Deck: {card_name, card_totals, suit_count: {suit}, value(s)}
            {
                "total": 0,
                "suit_count":
                    {
                        "clubs": 0,
                        "diamonds": 0,
                        "hearts": 0,
                        "spades": 0,
                    },
                "value": 11,
            },
            2:
                {
                    "total": 0,
                    "suit_count":
                        {
                            "clubs": 0,
                            "diamonds": 0,
                            "hearts": 0,
                            "spades": 0,
                        },
                    "value": 2,
                },
            3:
                {
                    "total": 0,
                    "suit_count":
                        {
                            "clubs": 0,
                            "diamonds": 0,
                            "hearts": 0,
                            "spades": 0,
                        },
                    "value": 3,
                },
            4:
                {
                    "total": 0,
                    "suit_count":
                        {
                            "clubs": 0,
                            "diamonds": 0,
                            "hearts": 0,
                            "spades": 0,
                        },
                    "value": 4,
                },
            5:
                {
                    "total": 0,
                    "suit_count":
                        {
                            "clubs": 0,
                            "diamonds": 0,
                            "hearts": 0,
                            "spades": 0,
                        },
                    "value": 5,
                },
            6:
                {
                    "total": 0,
                    "suit_count":
                        {
                            "clubs": 0,
                            "diamonds": 0,
                            "hearts": 0,
                            "spades": 0,
                        },
                    "value": 6,
                },
            7:
                {
                    "total": 0,
                    "suit_count":
                        {
                            "clubs": 0,
                            "diamonds": 0,
                            "hearts": 0,
                            "spades": 0,
                        },
                    "value": 7,
                },
            8:
                {
                    "total": 0,
                    "suit_count":
                        {
                            "clubs": 0,
                            "diamonds": 0,
                            "hearts": 0,
                            "spades": 0,
                        },
                    "value": 8,
                },
            9:
                {
                    "total": 0,
                    "suit_count":
                        {
                            "clubs": 0,
                            "diamonds": 0,
                            "hearts": 0,
                            "spades": 0,
                        },
                    "value": 9,
                },
            10:
                {
                    "total": 0,
                    "suit_count":
                        {
                            "clubs": 0,
                            "diamonds": 0,
                            "hearts": 0,
                            "spades": 0,
                        },
                    "value": 10,
                },
            "J":
                {
                    "total": 0,
                    "suit_count":
                        {
                            "clubs": 0,
                            "diamonds": 0,
                            "hearts": 0,
                            "spades": 0,
                        },
                    "value": 10,
                },
            "Q":
                {
                    "total": 0,
                    "suit_count":
                        {
                            "clubs": 0,
                            "diamonds": 0,
                            "hearts": 0,
                            "spades": 0,
                        },
                    "value": 10,
                },
            "K":
                {
                    "total": 0,
                    "suit_count":
                        {
                            "clubs": 0,
                            "diamonds": 0,
                            "hearts": 0,
                            "spades": 0,
                        },
                    "value": 10,
                },
        }

    def set_deck_count(self):
        """Updated the deck to reflect appropriate amount of cards  per suit."""
        self.deck_count = int(input("How many decks would you like the house to use: "))
        for card in self.deck:
            self.deck[card]["total"] = (4 * self.deck_count)
            for suit in self.deck[card]["suit_count"]:
                self.deck[card]["suit_count"][suit] = (1 * self.deck_count)
            self.deck_card_total += self.deck[card]["total"]

    def is_deck_empty(self):
        """Checks to see if deck is empty by totalling all remaining cards."""
        if self.deck_card_total == 0:
            self.is_empty = True
