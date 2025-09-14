"""Defines the card abilities for each card color and kind in the game.

This module maps each CardColor to a list of (CardKind, Ability) tuples,
where Ability is an instance of a card action class.
"""

from cards.cards import (
    CardColor,
    CardKind,
    Cover,
    Donate,
    ExtraCard,
    RemoveColor,
    RemoveKind,
    SwitchCard,
)

CARD_DEFINITIONS = {
    CardColor.RED: [
        (CardKind.DUCK, RemoveKind(CardKind.DRAGON)),
        (CardKind.DRAGON, RemoveColor(CardColor.GRAY)),
        (CardKind.ZOMBIE, Cover()),
        (CardKind.FROG, Donate()),
        (CardKind.UNICORN, SwitchCard()),
        (CardKind.CAT, ExtraCard()),
    ],
    CardColor.BLUE: [
        (CardKind.DUCK, Donate()),
        (CardKind.DRAGON, SwitchCard()),
        (CardKind.ZOMBIE, ExtraCard()),
        (CardKind.FROG, RemoveKind(CardKind.UNICORN)),
        (CardKind.UNICORN, RemoveColor(CardColor.YELLOW)),
        (CardKind.CAT, Cover()),
    ],
    CardColor.GREEN: [
        (CardKind.DUCK, ExtraCard()),
        (CardKind.DRAGON, RemoveKind(CardKind.ZOMBIE)),
        (CardKind.ZOMBIE, RemoveColor(CardColor.RED)),
        (CardKind.FROG, Cover()),
        (CardKind.UNICORN, Donate()),
        (CardKind.CAT, SwitchCard()),
    ],
    CardColor.YELLOW: [
        (CardKind.DUCK, SwitchCard()),
        (CardKind.DRAGON, ExtraCard()),
        (CardKind.ZOMBIE, RemoveKind(CardKind.FROG)),
        (CardKind.FROG, RemoveColor(CardColor.GREEN)),
        (CardKind.UNICORN, Cover()),
        (CardKind.CAT, Donate()),
    ],
    CardColor.PURPLE: [
        (CardKind.DUCK, Cover()),
        (CardKind.DRAGON, Donate()),
        (CardKind.ZOMBIE, SwitchCard()),
        (CardKind.FROG, ExtraCard()),
        (CardKind.UNICORN, RemoveKind(CardKind.CAT)),
        (CardKind.CAT, RemoveColor(CardColor.BLUE)),
    ],
    CardColor.GRAY: [
        (CardKind.DUCK, RemoveColor(CardColor.PURPLE)),
        (CardKind.DRAGON, Cover()),
        (CardKind.ZOMBIE, Donate()),
        (CardKind.FROG, SwitchCard()),
        (CardKind.UNICORN, ExtraCard()),
        (CardKind.CAT, RemoveKind(CardKind.DUCK)),
    ],
}
