from GameChips import Chips
from Hands import Hands
from Decks import Deck
from Cards import Cards


def make_bet(chips):
    while True:
        try:
            chips.bet = int(input("Place your bet: "))
        except ValueError:
            print("Please enter an integer!")
        else:
            if chips.bet > chips.total:
                print("Not enough chips try a lower bet. You have {}".format(chips.total))
            else:
                break


def hit(deck, hand):
    single_card = deck.deal()
    hand.add_card(single_card)


def hit_or_stay(deck, hand):
    global playing
    while True:
        x = input("Hit ir Stay? Use h or s: ")

        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("Player stays, Dealers turn")
            playing = False
        else:
            print("Please enter h or s only.")
            continue
        break


def player_losses(player, dealer, chips):
    print("Player lost!")
    chips.lost_game()


def player_wins(player, dealer, chips):
    print("Player won!")
    chips.won_game()


def dealer_losses(player, dealer, chips):
    print("Player wins Dealer lost!")
    chips.won_game()


def dealer_wins(player, dealer, chips):
    print("Player lost Dealer won!")
    chips.lost_game()


def tie(player, dealer):
    print("There is a tie")


def show_some_cards(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print(" ", dealer.hand_cards[1])
    print("\nPlayer's hand: ", *player.hand_cards, sep="\n ")


def show_cards(player, dealer):
    print("\nDealer's Hand:", *dealer.hand_cards, sep="\n ")
    print("Dealer's Hand = ", dealer.value)
    print("\nPlayer's hand: ", *player.hand_cards, sep="\n ")
    print("Player's Hand = ", player.value)


if __name__ == "__main__":
    while True:
        print("Hello! Lets play BlackJack")

        # Create and shuffle the deck and deal two cards to each player and dealer
        game_deck = Deck()
        game_deck.shuffle()

        player1_hand = Hands()
        player1_hand.add_card(game_deck.deal())
        player1_hand.add_card(game_deck.deal())

        dealer_hand = Hands()
        dealer_hand.add_card(game_deck.deal())
        dealer_hand.add_card(game_deck.deal())

        # Player chips for game play
        player1_chips = Chips()  # default value is set at 200

        # Ask the player to make a bet
        make_bet(player1_chips)

        # Show the players' cards
        show_some_cards(player1_hand, dealer_hand)
        playing = True
        while playing:  # global variable from the cards class

            # Ask the player of they want to hit or stay
            hit_or_stay(game_deck, player1_hand)

            # show some of the cards but keep the dealers hidden
            show_some_cards(player1_hand, dealer_hand)

            # If players hand is greater than 21, tun player_losses and break out of loop
            if player1_hand.value > 21:
                player_losses(player1_hand, dealer_hand, player1_chips)
                break

        # If the player has not lost, play dealers hand until dealer reaches 17
        if player1_hand.value <= 21:
            while dealer_hand.value < player1_hand.value:
                hit(game_deck, dealer_hand)

            # Show all of the cards
            show_cards(player1_hand, dealer_hand)

            # Check for winners
            if dealer_hand.value > 21:
                dealer_losses(player1_hand, dealer_hand, player1_chips)
            elif dealer_hand.value > player1_hand.value:
                dealer_wins(player1_hand, dealer_hand, player1_chips)
            else:
                tie(player1_hand, dealer_hand)

        # Show chip total
        print("\n Player1's available chips: {}".format(player1_chips.total))

        # Play again?

        new_game = input("Do you want to play again Yes or No: ")

        if new_game[0].lower() == "y":
            player = True
            continue
        else:
            print("Thank you for playing")
            break

