"""
Game: Sevens

Game Description:
All cards in the deck are dealt out to the player, in order to start the game the player with a Seven of a Suit
must put down their card. Cards played after must be between a tolerance of one. (e.g If the deck has S7 in it.
Only S6 and S5 can be played) The game ends when a player has played all their cards successfully.

Game Features:
1) Player can skip at any time
2) If player chooses to play a card. It must be within the games.txt rules
3) Game needs a minimum of 3 players

Task Rules:
1) Allow the user to select the number of players - a minimum of three or more
2) All cards are dealt out between the players
3) The player with the seven of spades starts
4) A seven of a suit must be played before the rest of that suit
5) A player must play a card if they can
6) You can always play a seven
7) The player can add in the same suite above or below the cards played e.g if 6,7,8 of spades have been played the next player can play the 5 or 9 of spades
8) A player must play the cards in order
9) Ace is low i.e. placed after a 2 and King is high

"""

import playingCard


def get_num_players():
    """Get the number of players playing the game"""

    valid_number = False

    # Make sure that the number of players is above 3
    number_of_players = input("Please Enter The Number of Players! The Minimum is 3\n")
    while not valid_number:
        if number_of_players.isdigit():
            if int(number_of_players) >= 3:
                valid_number = True
                continue
        number_of_players = input("Number of Players Entered Not Valid! Try Again!\n")

    return int(number_of_players)


def initiate_players(hands):
    """Map each player to a hand in the deck"""

    players = {}
    for length, item in enumerate(hands):
        players[length] = item
    return players


def initiate_table_hand():
    """Initialise the hand for the 'table'"""

    table_hands = {}
    for suit in playingCard.suits.keys():
        table_hands[suit] = []
    return table_hands


def play_card(current_hand, user_card, suit, bigger):
    """
    Let the user play the card

    - Remove the card from the hand
    - Insert card at the end when bigger
    - Insert card at the start when smaller
    """

    current_hand.remove(user_card)
    suit.append(user_card) if bigger else suit.insert(0, user_card)


def validate_card(current_hand, user_card, table_hands):
    """Make sure that card can be played within the game"""

    suit = table_hands[user_card[:1]]
    card = playingCard.convertFaceToNumber(user_card)
    not_valid = False

    # When suit is empty, check if card starts with 7 in the suit
    # Ask the player again if the player doesn't enter a card with 7
    if not suit:
        if int(card[1:len(card)]) == 7:
            play_card(current_hand, user_card, suit, bigger=True)
        else:
            print("Card Was Not 7 In Empty Suit! Please Try Again!")
            not_valid = True

    # Check if card can be inserted above or below the current deck
    # Ask the player again when the user tries to play a card that is not above or below the cards on the deck
    else:
        min_suit_card = playingCard.convertFaceToNumber(suit[0].upper())
        max_suit_card = playingCard.convertFaceToNumber(suit[-1].upper())
        if int(card[1:len(card)]) == (int(min_suit_card[1:len(min_suit_card)]) - 1):
            play_card(current_hand, user_card, suit, bigger=False)
        elif int(card[1:len(card)]) == (int(max_suit_card[1:len(max_suit_card)]) + 1):
            play_card(current_hand, user_card, suit, bigger=True)
        else:
            print("Card Was Not +1 or -1 of Any Cards In The Deck! Please Try Again!")
            not_valid = True

    return not_valid


def check_in_hand(user_card, hand, table_hands):
    """Check if the card chosen by the user exists in the hand"""

    # Do nothing if the user wishes to skip
    # Returning "False, False" as I'm returning 2 variables when check_in_hand() is called
    if user_card == "S":
        print("Player Has Skipped Their Turn!")
        return

    # Iterate through all the cards within the hand checking if the card exists in the hand
    valid = False
    for card in hand:
        if user_card == card:
            # Do nothing if card was invalid even after being in the hand
            # If it's not valid at all in the hand, break out of the loop and display error message after
            not_valid = validate_card(hand, user_card, table_hands)
            if not_valid: return
            valid = True
            break

    # When card is not in the hand, ask the player to enter a valid card
    if not valid: print("Card Was Not Found In Hand! Please Try Again!")
    return valid


def print_deck(table_hands, title):
    """Print the deck at the current time of function call"""

    print(title)
    for suit, cards in table_hands.items():
        print(f"{suit}: {cards}")


def sevens(players, table_hands):
    """Play Sevens"""

    counter = 0
    winner = False

    # Play until a player has no cards left in their hand
    while not winner:
        current_hand = players[counter]
        print_deck(table_hands, title="\nCurrent Deck:")

        # Let the user play a card and check if it's valid
        # When the player inputs a wrong card, prompt them to enter the card again
        # Don't trigger the prompt if the player wants to skip
        user_card = input(f"\nPlayer {counter + 1}'s Deck: {current_hand}\n"
                          f"Would You Like To Play A Card? Press 'S' To Skip\n").upper()
        while not check_in_hand(user_card, current_hand, table_hands) and not user_card == "S":
            print_deck(table_hands, title="\nCurrent Deck:")
            user_card = input(f"\nPlayer {counter + 1}'s Deck: {current_hand}\n"
                              f"Would You Like To Play A Card? Press 'S' To Skip\n").upper()

        # End the while loop once a player's hand is empty
        # Increment counter to allow for turn based system, going through each player
        if len(players[counter]) == 0: winner = True
        counter = (counter + 1) % len(players)

    # Since while loop has been exited. We can announce the winner
    print(f"\nPlayer {counter} Is The Winner!")
    print_deck(table_hands, title="Winning Deck:")


def main():
    """
    Get the number of players, generate the deck and play Sevens

    I think some of the logic in this is over-complicated but I'm glad to get it working with it's features
    """

    num_of_players = get_num_players()
    deck = playingCard.generateDeck()
    deck = playingCard.shuffleCards(deck)
    hands = playingCard.dealCards(deck, 0, num_of_players, [])

    players = initiate_players(hands)
    table_hands = initiate_table_hand()
    sevens(players, table_hands)


# Execute main method
main()
