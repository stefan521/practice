from enum import Enum


# Problem 7.1 Deck of cards
class CardSuit(Enum):
    HEARTS = "HEARTS"
    CLUBS = "CLUBS"
    DIAMOND = "DIAMOND"
    SPADES = "SPADES"


class CardNumber(Enum):
    ACE = "ACE"
    TWO = "TWO"
    THREE = "THREE"
    FOUR = "FOUR"
    FIVE = "FIVE"
    SIX = "SIX"
    SEVEN = "SEVEN"
    EIGHT = "EIGHT"
    NINE = "NINE"
    TEN = "TEN"
    JACK = "JACK"
    QUEEN = "QUEEN"
    KING = "KING"


class Card:
    suit: CardSuit
    number: CardNumber

    def __init__(self, suit: CardSuit, number: CardNumber):
        self.suit = suit
        self.number = number

    def __repr__(self) -> str:
        return f"Card(suit='{self.suit}', number='{self.number}')"


class Deck:
    cards: list[Card]

    def __init__(self):
        self.cards = [Card(suit, num) for suit in CardSuit for num in CardNumber]
