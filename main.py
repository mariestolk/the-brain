"""Define the core classes and enumerations for the card game.

Include CardColor, CardKind, CardEffect, Card, Player, and Game.
"""

import random
from enum import Enum

from cards.cards import Card
from cards.card_definitions import CARD_DEFINITIONS
from player.player import Player

NUMBER_OF_HAND_CARDS = 5


class DifficultyLevel(Enum):
    """Enumeration for difficulty levels in the game."""

    EASY = 7
    MEDIUM = 6
    HARD = 5


class Game:
    """Represents the game logic and manages the players."""

    def __init__(self, players: list[str], difficulty_level: DifficultyLevel) -> None:
        """Initialize the game with a list of players.

        The draw pile is created based on CARD_DEFINITIONS and shuffled.
        Discard pile and center zone are initialized as empty.
        Each player is dealt 5 cards from the draw pile.

        Args:
            players (list[str]): The players participating in the game.
            difficulty_level (DifficultyLevel): The difficulty level of the game.

        Attributes:
            players (list[Player]): The list of Player objects.
            draw_pile (list[Card]): The draw pile containing the cards.

        """
        self.players = [Player(name) for name in players]
        self.max_center_cards = difficulty_level.value - 1

        self.draw_pile = []
        self.discard_pile = []
        self.center_zone = []

        for color, definitions in CARD_DEFINITIONS.items():
            for kind, effect in definitions:
                self.draw_pile.append(Card(color, kind, effect))

        random.shuffle(self.draw_pile)

        for player in self.players:
            for _ in range(NUMBER_OF_HAND_CARDS):
                if self.draw_pile:
                    player.hand.add(self.draw_pile.pop())
            player.print_hand()

    def start_game(self):
        """Start the game logic."""
        while not self.game_over():

            print("\n--- NEW ROUND ---")

            for player in self.players:
                player.print_hand()

                self.center_zone.append(player.hand.pop()) #TODO: currently players just pop the last card, should be random or chosen

            print("\nCenter Zone:")
            for card in self.center_zone:
                print(f"  - {card}")

    def game_over(self):
        """Finish the current player's turn and check lose condition."""
        if len(self.center_zone) > self.max_center_cards:
            print("💀 Too many cards in the center — you lose!")
            return True
        return False


game = Game(["Marie", "Vincent"], DifficultyLevel.MEDIUM)
print(f"Number of players in the game: {len(game.players)}")

game.start_game()
