from abc import ABC, abstractmethod
from enum import Enum


class CardRarity(Enum):
    COMMON = "Common"
    RARE = "Rare"
    LEGENDARY = "Legendary"


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: CardRarity) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """Play the card and return the resulting game state changes."""
        pass

    def get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity.value,
            "type": self.__class__.__name__.replace("Card", ""),
        }

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost
