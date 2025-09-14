"""Define the Zone class for managing collections of cards in different zones."""

class Zone:
    """Represents a collection of cards in a specific zone.

    Attributes
    ----------
    name : str
        The name of the zone.
    cards : list
        The list of cards in the zone.

    """

    def __init__(self, name):
        """Initialize a Zone with a name and an empty list of cards.

        Parameters
        ----------
        name : str
            The name of the zone.

        """
        self.name = name
        self.cards = []

    def add(self, card):
        """Add a card to the zone.

        Parameters
        ----------
        card : object
            The card to add to the zone.

        """
        self.cards.append(card)

    def remove(self, card):
        """Remove a card from the zone.

        Parameters
        ----------
        card : object
            The card to remove from the zone.

        Raises
        ------
        ValueError
            If the card is not found in the zone.

        """
        self.cards.remove(card)

    def __len__(self):
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


