# SUITs
# ________________
# Spades   -->  3
# Hearts   -->  2
# Diamonds -->  1
# Clubs    -->  0

# RANKS
# _______________
# Jack   -->  11
# Queen  -->  12
# King   -->  13

import random


class Cards:
    # Class objects
    # Same for any instance of a class
    suits = ("Clubs", "Diamonds", "Hearts", "Spades")
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

    # Dictionary that holds the numerical values of each card
    values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
              'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
    playing = True

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    # Overrides print method
    def __str__(self):
        return self.rank + " of " + self.suit


if __name__ == "__main__":
    c1 = Cards("Clubs", "Two")
    print(c1)
