"""Definitions for card colors, kinds, and effects used in the game."""

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


class CardEffect:
    """Base class for all card effects in the game."""

    pass


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
