def place_bet(player):
    bet_amount = int(input("Place wager [1, 5, 25, 50, 100, 500]: "))
    player.money -= bet_amount


class BetEngine:

    def __init__(self):
        self.chips = {'1': 1,
                      '5': 5,
                      '25': 25,
                      '50': 50,
                      '100': 100,
                      '500': 500, }

    def buy_in(self, player):
        pass

    def double_down_bet(self, player):
        pass

# TODO - 3x payout for blackjack - pay out immediately if house doesnt have a blackjack
# TODO - Add push
# TODO - Add Double Down
# TODO - Split hand (Additional Wager) - can split any hand with same card values
# TODO - surrender - lose, but get half your wager back
