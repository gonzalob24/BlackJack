class Chips:

    def __init__(self, total=200):
        """
        Start the game with 200 chips
        and bet set to 0
        """
        self.total = total
        self.bet = 0

    def won_game(self):
        """
        update total if you win the current game
        """
        self.total += self.bet

    def lost_game(self):
        """
        update the total if you win the current game
        """
        self.total -= self.bet


