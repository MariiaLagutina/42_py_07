from typing import Any
from ex0.Card import Card, CardRarity


class SpellCard(Card):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: CardRarity,
        effect_type: str
    ) -> None:
        super().__init__(name, cost, rarity)

        if not isinstance(effect_type, str) or not effect_type:
            raise ValueError("effect_type must be a non-empty string")

        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Deal {self.effect_type}",
        }

    def resolve_effect(self, targets: list[Any]) -> dict:
        return {
            "spell": self.name,
            "rarity": self.rarity.value,
            "effect_type": self.effect_type,
            "targets": targets,
            "resolved": True,
        }
