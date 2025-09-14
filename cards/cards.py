"""Definitions for card colors, kinds, and effects used in the game."""

from enum import Enum


class CardColor(Enum):
    """Enumeration of possible card colors in the game."""

    BLUE = 1
    GRAY = 2
    YELLOW = 3
    PURPLE = 4
    RED = 5
    GREEN = 6

    def ansi_code(self) -> str:
        """Return the ANSI color code for pretty-printing the color."""
        mapping = {
            CardColor.BLUE: "\033[94m",
            CardColor.GRAY: "\033[90m",
            CardColor.YELLOW: "\033[33m",
            CardColor.PURPLE: "\033[95m",
            CardColor.RED: "\033[91m",
            CardColor.GREEN: "\033[92m",
        }
        return mapping[self]

    def __str__(self) -> str:
        """Pretty-print the color with ANSI code."""
        return f"{self.ansi_code()}{self.name.title()}\033[0m"


class CardKind(Enum):
    """Enumeration of possible card kinds in the game."""

    DUCK = 1
    DRAGON = 2
    ZOMBIE = 3
    FROG = 4
    UNICORN = 5
    CAT = 6


class CardEffect:
    """Base class for all card effects in the game."""

    def __str__(self) -> str:
        """Return the name of the effect class."""
        return self.__class__.__name__


class Cover(CardEffect):
    """Effect that allows a card to cover another card in CenterZone."""

    pass


class Donate(CardEffect):
    """Effect that allows a player to donate a card to another player."""

    pass


class ExtraCard(CardEffect):
    """Effect that allows a player to pass an extra card to CenterZone."""

    pass


class SwitchCard(CardEffect):
    """Effect that allows a player to switch handcard for card from CenterZone."""

    pass


class RemoveKind(CardEffect):
    """Effect that allows a player to remove cards of target kind from CenterZone."""

    def __init__(self, target_kind: CardKind) -> None:
        """Initialize RemoveKind effect with the specified target kind.

        Args:
            target_kind (CardKind): The kind of card to be removed from CenterZone.

        """
        self.target_kind = target_kind


class RemoveColor(CardEffect):
    """Effect that allows a player to remove cards of target color from CenterZone."""

    def __init__(self, target_color: CardColor) -> None:
        """Initialize RemoveColor effect with the specified target color.

        Args:
            target_color (CardColor): The color of card to be removed from CenterZone.

        """
        self.target_color = target_color


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

    def __str__(self) -> str:
        """Return a string representation of the card."""
        if isinstance(self.effect, RemoveKind):
            effect_str = f"RemoveKind({self.effect.target_kind.name})"
        elif isinstance(self.effect, RemoveColor):
            effect_str = f"RemoveColor({self.effect.target_color.name})"
        else:
            effect_str = str(self.effect)
        return f"{self.color} {self.kind.name.title()} [{effect_str}]"
