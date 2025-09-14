"""Represents a player in the game."""

from cards.cards import Card
from cards.card_zones import PlayerHand


class Player:
    """Represents a player in the game.

    Attributes:
        name (str): The name of the player.
        hand (list): The cards currently held by the player.

    """

    def __init__(self, name: str, hand: PlayerHand = None):
        """Initialize a player with a name and an empty hand."""
        self.name = name

        if hand is None:
            hand = PlayerHand(self.name)
        self.hand = hand

    def print_name(self):
        """Print the player's name."""
        print(f"Player Name: {self.name}")

    def print_hand(self):
        """Print the player's hand."""
        print(f"{self.name}'s Hand:")
        for card in self.hand:
            print(f"  - {card}")
