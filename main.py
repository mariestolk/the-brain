"""Define the core classes and enumerations for the card game.

Include CardColor, CardKind, CardEffect, Card, Player, and Game.
"""

from enum import Enum


class CardColor(Enum):
    """Enumeration of possible card colors in the game."""

    BLUE = 1
    GRAY = 2
    ORANGE = 3
    PURPLE = 4
    RED = 5
    GREEN = 6

class CardKind(Enum):
    """Enumeration of possible card kinds in the game."""

    DUCK = 1
    DRAGON = 2
    ZOMBIE = 3
    FROG = 4
    UNICORN = 5
    CAT = 6

class CardEffect(Enum):
    """Enumeration of possible card effects in the game."""

    COVER = 1
    DONATE = 2
    EXTRA_CARD = 3
    TAKE_BACK = 4
    REMOVE_KIND = 5
    REMOVE_COLOR = 6

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

start()
