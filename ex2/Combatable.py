from abc import ABC, abstractmethod
from typing import Any


class Combatable(ABC):
    @abstractmethod
    def attack(self, target: Any) -> dict:
        """Perform an attack on the target and return the combat result."""
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        """Defend against incoming damage and return the defense result."""
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict:
        """Return the combat-related statistics of the entity."""
        pass
