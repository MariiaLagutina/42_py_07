from abc import ABC, abstractmethod


class GameStrategy(ABC):
    @abstractmethod
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """
        Defines how a single turn is executed.
        """
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        """
        Returns the name of the strategy.
        """
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: list) -> list:
        """
        Defines target prioritization logic.
        """
        pass
