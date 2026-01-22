from abc import ABC, abstractmethod
from ex0.Card import Card


class CardFactory(ABC):
    @abstractmethod
    def create_creature(
        self,
        name_or_power: str | int | None = None
    ) -> Card:
        """
        Creates and returns a creature card according to the factory theme.
        """
        pass

    @abstractmethod
    def create_spell(
        self,
        name_or_power: str | int | None = None
    ) -> Card:
        """
        Creates and returns a spell card according to the factory theme.
        """
        pass

    @abstractmethod
    def create_artifact(
        self,
        name_or_power: str | int | None = None
    ) -> Card:
        """
        Creates and returns an artifact card according to the factory theme.
        """
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict:
        """
        Creates a themed deck of the given size.
        """
        pass

    @abstractmethod
    def get_supported_types(self) -> dict:
        """
        Returns information about supported card types and themes.
        """
        pass
