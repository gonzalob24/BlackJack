from Decks import Deck


class Hands(Deck):

    def __init__(self):
        """
        Inherit functions from deck
        """
        Deck.__init__(self)
        self.hand_cards = []  # Creates an empty hand
        self.value = 0  # 0 value
        self.ace = 0  # Will keep track of aces

    def add_card(self, card):
        """
        Deals one card at a time to the players
        :return:
        """
        # Deal a card from the deck I created
        # card will come from deck.deal()
        self.hand_cards.append(card)
        self.value += self.values[card.rank]  # card.rank gets the value of the dealt card

        # Tracking the aces
        if card.rank == "Ace":
            self.ace += 1

    def handle_ace(self):
        # If player value is over 21 and has an ace
        # Change the value of ace to 1 instead of 11
        while self.value > 21 and self.ace > 0:
            self.values -= 10  # subtract 10 b/c initially ace = 11. In game its can be 11 or 1
            self.ace -= 1


if __name__ == "__main__":
    deck1 = Deck()
    deck1.shuffle()
    player1 = Hands()
    player1.add_card(deck1.deal())
    player1.add_card(deck1.deal())
    for card in player1.hand_cards:
        print(card)
    print(player1.value)
