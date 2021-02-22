class Hand:

    def __init__(self):
        self.hand = []
        self.display_hand = []
        self.total = 0
        self.split_possibility = False
        self.is_blackjack = False
        self.bust = False

    def add_hand_to_player(self, player):
        player.hands.append(self.hand)

    def detect_split_possibility(self):
        card1 = self.hand[0].face
        card2 = self.hand[1].face
        if card1 == card2:
            self.split_possibility = True

    def detect_blackjack(self):
        if self.hand[0].value + self.hand[1].value == 21:
            self.is_blackjack = True

    def detect_bust(self):
        if self.total > 21:
            self.bust = True

    def calculate_hand_total(self):
        card_total = 0
        for card in self.hand:
            card_total += card.value
            self.total = card_total

        if self.split_possibility and self.hand[0] == "A":
            self.hand[1].value = 1
        elif card_total > 21:
            for card in self.hand:
                if card.face == "A":
                    card.value = 1

    def reset_hand(self):
        self.hand = []
        self.display_hand = []
