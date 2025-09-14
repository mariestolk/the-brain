"""Represents a player in the game."""

from cards.cards import Card


class player:
    """Represents a player in the game.

    Attributes:
        name (str): The name of the player.
        hand (list): The cards currently held by the player.

    """

    def __init__(self, name: str, hand: list[Card] = None):
        """Initialize a player with a name and an empty hand."""
        self.name = name
        self.hand = hand
