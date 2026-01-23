from typing import Any
from ex0.Card import Card, CardRarity
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: CardRarity,
        attack_power: int,
        health: int,
        mana: int,
    ) -> None:
        super().__init__(name, cost, rarity)

        if attack_power <= 0 or health <= 0 or mana < 0:
            raise ValueError("Invalid EliteCard stats")

        self.attack_power = attack_power
        self.health = health
        self.mana = mana

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "status": "Elite card enters the battlefield",
        }

    def attack(self, target: Any) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power,
            "combat_type": "melee",
        }

    def defend(self, incoming_damage: int) -> dict:
        damage_taken = min(incoming_damage, self.health)
        self.health -= damage_taken

        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "remaining_health": self.health,
            "still_alive": self.health > 0,
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack_power": self.attack_power,
            "health": self.health,
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        cost_per_target = 2
        total_cost = cost_per_target * len(targets)

        if self.mana < total_cost:
            return {
                "caster": self.name,
                "spell": spell_name,
                "status": "Not enough mana",
            }

        self.mana -= total_cost

        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": total_cost,
        }

    def channel_mana(self, amount: int) -> dict:
        self.mana += amount

        return {
            "channeled": amount,
            "total_mana": self.mana,
        }

    def get_magic_stats(self) -> dict:
        return {
            "mana": self.mana,
        }
