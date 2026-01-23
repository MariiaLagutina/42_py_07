from abc import ABC, abstractmethod


class Magical(ABC):
    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """Cast a spell on the given targets and return the casting result."""
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        """
        Channel a certain amount of mana and return the channeling result.
        """
        pass

    @abstractmethod
    def get_magic_stats(self) -> dict:
        """Return the magic-related statistics of the entity."""
        pass
