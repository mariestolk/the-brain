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
    pass


class Donate(CardEffect):
    pass


class ExtraCard(CardEffect):
    pass


class TakeBack(CardEffect):
    pass


class RemoveKind(CardEffect):
    def __init__(self, target_kind):
        self.target_kind = target_kind


class RemoveColor(CardEffect):
    def __init__(self, target_color):
        self.target_color = target_color


CARD_DEFINITIONS = {
    CardColor.RED: [
        (CardKind.DUCK, RemoveKind(CardKind.DRAGON)),
        (CardKind.DRAGON, RemoveColor(CardColor.GRAY)),
        (CardKind.ZOMBIE, Cover()),
        (CardKind.FROG, Donate()),
        (CardKind.UNICORN, TakeBack()),
        (CardKind.CAT, ExtraCard()),
    ],
    CardColor.BLUE: [
        (CardKind.DUCK, Donate()),
        (CardKind.DRAGON, TakeBack()),
        (CardKind.ZOMBIE, ExtraCard()),
        (CardKind.FROG, RemoveKind(CardKind.UNICORN)),
        (CardKind.UNICORN, RemoveColor(CardColor.ORANGE)),
        (CardKind.CAT, Cover()),
    ],
    CardColor.GREEN: [
        (CardKind.DUCK, ExtraCard()),
        (CardKind.DRAGON, RemoveKind(CardKind.ZOMBIE)),
        (CardKind.ZOMBIE, RemoveColor(CardColor.RED)),
        (CardKind.FROG, Cover()),
        (CardKind.UNICORN, Donate()),
        (CardKind.CAT, TakeBack()),
    ],
    CardColor.ORANGE: [
        (CardKind.DUCK, TakeBack()),
        (CardKind.DRAGON, ExtraCard()),
        (CardKind.ZOMBIE, RemoveKind(CardKind.FROG)),
        (CardKind.FROG, RemoveColor(CardColor.GREEN)),
        (CardKind.UNICORN, Cover()),
        (CardKind.CAT, Donate()),
    ],
    CardColor.PURPLE: [
        (CardKind.DUCK, Cover()),
        (CardKind.DRAGON, Donate()),
        (CardKind.ZOMBIE, TakeBack()),
        (CardKind.FROG, ExtraCard()),
        (CardKind.UNICORN, RemoveKind(CardKind.CAT)),
        (CardKind.CAT, RemoveColor(CardColor.BLUE)),
    ],
    CardColor.GRAY: [
        (CardKind.DUCK, RemoveColor(CardColor.PURPLE)),
        (CardKind.DRAGON, Cover()),
        (CardKind.ZOMBIE, Donate()),
        (CardKind.FROG, TakeBack()),
        (CardKind.UNICORN, ExtraCard()),
        (CardKind.CAT, RemoveKind(CardKind.DUCK)),
    ],
}
