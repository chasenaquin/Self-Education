class Player:
    id = 0

    def __init__(self):
        self.id = Player.id
        self.is_house = False
        self.name = ""
        self.hands = []
        self.action = ""
        self.is_winner = False
        self.wins = 0
        self.money = 500
        Player.id += 1

    def initialize_house(self, player_list):
        """Creates the House/Dealer object. Appends to player_list"""
        self.id = 0
        self.name = "House"
        self.is_house = True
        player_list.append(self)

    def initialize_user(self, player_list):
        """Creates user player instance. Appends to player_list"""
        self.id = 1
        self.name = input("Hello sir. Welcome to the table. May i ask your name? ")
        player_list.append(self)

    def initialize_player(self, player_list):
        """Create player instance. Appends to player_list"""
        self.name = input(f"Player {self.id} name: ")
        player_list.append(self)

    def reset_player_hand(self):
        self.hands = []
