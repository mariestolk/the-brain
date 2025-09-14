"""Define the Zone class for managing collections of cards in different zones."""

from cards.cards import Card


class Zone:
    """Represents a collection of cards in a specific zone.

    Attributes
    ----------
    name : str
        The name of the zone.
    cards : list[Card]
        The list of cards in the zone.

    """

    def __init__(self, name: str) -> None:
        """Initialize a Zone with a name and an empty list of cards.

        Parameters
        ----------
        name : str
            The name of the zone.

        """
        self.name = name
        self.cards = []

    def add(self, card: Card) -> None:
        """Add a card to the zone.

        Parameters
        ----------
        card : Card
            The card to add to the zone.

        """
        self.cards.append(card)

    def remove(self, card: Card) -> None:
        """Remove a card from the zone.

        Parameters
        ----------
        card : Card
            The card to remove from the zone.

        Raises
        ------
        ValueError
            If the card is not found in the zone.

        """
        self.cards.remove(card)

    def __len__(self) -> int:
        """Return the number of cards in the zone."""
        return len(self.cards)


class DrawPile(Zone):
    """Represents the draw pile zone."""

    def __init__(self):
        """Initialize the Draw Pile with a specific name."""
        super().__init__("Draw Pile")


class DiscardPile(Zone):
    """Represents the discard pile zone."""

    def __init__(self):
        """Initialize the Discard Pile with a specific name."""
        super().__init__("Discard Pile")


class CenterArea(Zone):
    """Represents the center area zone."""

    def __init__(self):
        """Initialize the Center Area with a specific name."""
        super().__init__("Center Area")


class PlayerHand(Zone):
    """Represents a player's hand zone."""

    def __init__(self, player_name: str):
        """Initialize the Player Hand with a specific name.

        Parameters
        ----------
        player_name : str
            The name of the player whose hand this is.

        """
        super().__init__(f"{player_name}'s Hand")
