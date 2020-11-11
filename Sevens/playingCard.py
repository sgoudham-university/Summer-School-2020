import random  # , playingCardTests

suits = {"H": "Hearts", "D": "Diamonds", "S": "Spades", "C": "Clubs"}
faces = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

userHand = 0


# Function: generateDeck
# Description: This function generates a 52 pack of cards, with four suites and 13 playing cards Ace to King.
# The cards are returned in an ordered deck
def generateDeck():
    deck = []
    for suit in suits.keys():
        for face in faces:
            deck.append(suit + face)
    return deck


# Function: shuffleDeck
# Description: A set of cards is supplied and shuffled, randomly ordered.
def shuffleCards(cards):
    random.shuffle(cards)
    return cards


# Method: trentineSmall
# Description: An Italian set of cards Tertine can be only 40 cards or 52. The small set has no "8","9" or "10". It
# still has ace to seven and jack, queen and king.
def trentineSmall():
    faces.remove("8")
    faces.remove("9")
    faces.remove("10")


# Function: dealACard
# Description: Remove a card from a deck or hand of cards and return the card.
def dealACard(cards):
    return cards.pop()


# Function: dealCards
# Description: Deal a number of cards from a deck to a number of players (no of hands). Optionally an existing set of
# hands of cards can be passed. The default is for no existing hands of cards to be passed.
def dealCards(deck, noOfCards, noOfHands, hands=[]):
    if noOfCards == 0:
        noOfCards = int(len(deck) / noOfHands) + 1
    # Setup hand
    if hands:  # I.E. a hand has already been provided
        missingHands = noOfHands - len(hands)
        for index in range(0, missingHands):
            hands += [[]]
    else:
        for index in range(0, noOfHands):
            hands += [[]]

    for handIndex in range(0, noOfHands):
        while len(hands[handIndex]) < noOfCards and len(deck) > 0:
            dealtCard = dealACard(deck)
            hands[handIndex].append(dealtCard)

    return hands


# Method: playACard
# Description: A hand of cards is input and an individual playing card. If the individual playing card is found in the hand it is removed from
# the hand.
def playACard(hand, cardToPlay):
    if cardToPlay in hand:
        hand.remove(cardToPlay)


# Function: isPlayingACard
# Description: For a given hand of cards if an individual hand of card is found it is removed from the hand and returns
# True if no card if found this function returns False.
def isPlayingACard(hand, cardToPlay):
    played = False
    currentSize = len(hand)
    playACard(hand, cardToPlay)
    if currentSize > len(hand):
        played = True
    return played


# Function: convertFaceToName
# Description: An individual playing card is input and it is a face card e.g. A,K,Q,J we convert to hexadecimal. We
# include converting a 10 to A, since it will order 1,2,...9,A,B,C,D. The converted individual playing card is returned.
# HA -> H1
# H10 -> H10 -- No change
# HJ -> H11
# HQ -> H12
# CK -> C13
def convertFaceToNumber(card):
    face = card[1:len(card)]
    if face == "K":
        newFace = "13"
    elif face == "Q":
        newFace = "12"
    elif face == "J":
        newFace = "11"
    elif face == "10":
        newFace = "10"
    elif face == "A":
        newFace = "01"
    else:
        newFace = str(0) + face

    return card[0] + newFace


# Method: convertFacesToNumbers
# Description: For a hand of cards, each playing card in the hand is converted from faces to hexadecimal numbers
def convertFacesToNumbers(hand):
    for counter in range(0, len(hand)):
        hand[counter] = convertFaceToNumber(hand[counter])


# Function: convertNumberToFace
# Description: For an individual playing card this reverse the conversion from Face to hexadecimal number.
def convertNumberToFace(card):
    face = card[1:len(card)]
    if face == "13":
        newFace = "K"
    elif face == "12":
        newFace = "Q"
    elif face == "11":
        newFace = "J"
    elif face == "10":
        newFace = "10"
    elif face == "01":
        newFace = "A"
    else:
        newFace = str(int(face))
    return card[0] + newFace


# Method: convertNumbersToFaces
# Description: For a hand of cards, each playing card in the hand is converted from a hexadecimal number to a face card
def convertNumbersToFaces(hand):
    for counter in range(0, len(hand)):
        hand[counter] = convertNumberToFace(hand[counter])


# Method: sortHand
# Description: For a hand of playing cards it is sorted. It is converted to hexadecimal numbers, sorted and converted
# back to face cards
def sortHand(hand):
    convertFacesToNumbers(hand)
    hand.sort()
    convertNumbersToFaces(hand)


# Method: sortHands
# Description: For a set of hands of cards for a number of players, each hand is sorted
def sortHands(hands):
    for hand in hands:
        sortHand(hand)

# if __name__ == '__main__':
#    playingCardTests.main()
