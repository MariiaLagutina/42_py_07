from typing import Any

from ex0.Card import Card, CardRarity
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(
        self,
        card_id: str,
        name: str,
        cost: int,
        rarity: CardRarity,
        attack_power: int,
        health: int,
        base_rating: int = 1200,
    ) -> None:
        super().__init__(name, cost, rarity)

        self.card_id = card_id
        self.attack_power = attack_power
        self.health = health

        self.wins = 0
        self.losses = 0
        self.base_rating = base_rating
        self.current_streak = 0

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "status": "Tournament card played",
        }

    def attack(self, target: Any) -> dict:
        return {
            "attacker": self.name,
            "target": str(target),
            "damage": self.attack_power,
        }

    def defend(self, incoming_damage: int) -> dict:
        damage_taken = min(incoming_damage, self.health)
        self.health -= damage_taken

        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "remaining_health": self.health,
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack_power": self.attack_power,
            "health": self.health,
        }

    def calculate_rating(self) -> int:
        streak_bonus = self.current_streak * 10
        return (
            self.base_rating
            + (self.wins * 20)
            - (self.losses * 15)
            + streak_bonus
        )

    def update_wins(self, wins: int) -> None:
        if wins > 0:
            self.wins += wins
            self.current_streak += wins

    def update_losses(self, losses: int) -> None:
        if losses > 0:
            self.losses += losses
            self.current_streak = 0

    def get_rank_info(self) -> dict:
        return {
            "wins": self.wins,
            "losses": self.losses,
            "streak": self.current_streak,
            "rating": self.calculate_rating(),
        }

    def get_tournament_stats(self) -> dict:
        info = self.get_rank_info()
        info["name"] = self.name
        info["id"] = self.card_id
        return info

    def process_match_result(self, won: bool) -> dict:
        if won:
            self.update_wins(1)
            result = "win"
        else:
            self.update_losses(1)
            result = "loss"

        return {
            "card": self.name,
            "result": result,
            "rank_info": self.get_rank_info(),
        }
