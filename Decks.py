import random
from Cards import Cards


class Deck(Cards):

    def __init__(self):
        # Constructor from inherited Card class
        Cards.__init__(self, suit=0, rank=0)
        self.deck = []  # items stored as example "A of Clubs"
        for suit in self.suits:
            for rank in self.ranks:  # Start at one b/c index 0 holds the dummy value
                self.deck.append(Cards(suit, rank))

    def shuffle(self):
        """
        Random generator to help shuffle cards
        """
        generator = random.Random()
        generator.shuffle(self.deck)

    def __str__(self):
        """
        Prints all 52 cards in the deck
        """
        # Start with an empty deck to add the cards to it to view with print()
        print_deck = ""
        for card in self.deck:
            print_deck += "\n" + card.__str__()
        return "The deck looks like: " + print_deck

    def deal(self):
        """
        deals one card at a time to the user
        :return: top_card
        """
        top_card = self.deck.pop()  # assign and remove the top card in the deck
        return top_card


if __name__ == "__main__":
    d1 = Deck()
    d1.shuffle()
    print(d1)
