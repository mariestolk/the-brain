"""Define the core classes and enumerations for the card game.

Include CardColor, CardKind, CardEffect, Card, Player, and Game.
"""

from itertools import product

from card_definitions import CardColor, CardKind, CardEffect


class CardDeck:
    """Represents a deck of cards in the game.

    Attributes:
        cards (list): The list of cards in the deck.

    """

    def __init__(self):
        """Initialize an empty card deck."""
        self.cards = []

        for color, kind, effect in product(CardColor, CardKind, CardEffect):
            self.cards.append(Card(color, kind, effect))

    def print_deck(self):
        """Print the details of each card in the deck."""
        for card in self.cards:
            print(f"Color: {card.color}, Kind: {card.kind}, Effect: {card.effect}")


class Card:
    """Represents a card in the game with a color, kind, and effect."""

    def __init__(self, color: CardColor, kind: CardKind, effect: CardEffect) -> None:
        """Initialize a card with a color, kind, and effect.

        Args:
            color (CardColor): The color of the card.
            kind (CardKind): The kind of the card.
            effect (CardEffect): The effect of the card.

        """
        self.color = color
        self.kind = kind
        self.effect = effect

class player:
    """Represents a player in the game.

    Attributes:
        name (str): The name of the player.
        hand (list): The cards currently held by the player.

    """

    def __init__(self, name):
        """Initialize a player with a name and an empty hand."""
        self.name = name
        self.hand = []

class game:
    """Represents the game logic and manages the players."""

    def __init__(self, players):
        """Initialize the game with a list of players.

        Args:
            players (list): The players participating in the game.

        """
        self.players = players

def start():
    """Start the game and print a message indicating the game has started."""
    print("Game started")

card_deck = CardDeck()
card_deck.print_deck()
