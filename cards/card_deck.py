"""Module for managing a deck of cards in the game."""

from cards.card_definitions import CARD_DEFINITIONS, Card


class CardDeck:
    """Represents a deck of cards in the game.

    Attributes:
        cards (list): The list of cards in the deck.

    """

    def __init__(self):
        """Initialize an empty card deck."""
        self.cards = []

        for (color, kind), data in CARD_DEFINITIONS.items():
            self.cards.append(Card(color, kind, data["effect"]))

        self.shuffle()

    def shuffle(self):
        """Shuffle the deck of cards."""
        import random

        random.shuffle(self.cards)

    def print_deck(self):
        """Print the details of each card in the deck."""
        for card in self.cards:
            print(f"Color: {card.color}, Kind: {card.kind}, Effect: {card.effect}")
