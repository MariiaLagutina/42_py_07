from abc import ABC, abstractmethod


class Rankable(ABC):
    @abstractmethod
    def calculate_rating(self) -> int:
        """
        Calculate and return the current rating.
        """
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """
        Update the number of recorded wins.
        """
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """
        Update the number of recorded losses.
        """
        pass

    @abstractmethod
    def get_rank_info(self) -> dict:
        """
        Return a structured summary of ranking information.
        """
        pass
