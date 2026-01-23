from ex0.Card import Card, CardRarity


class ArtifactCard(Card):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: CardRarity,
        durability: int,
        effect: str
    ) -> None:
        super().__init__(name, cost, rarity)

        if not isinstance(durability, int) or durability <= 0:
            raise ValueError("durability must be a positive integer")
        if not isinstance(effect, str) or not effect:
            raise ValueError("effect must be a non-empty string")

        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Permanent: {self.effect}",
        }

    def activate_ability(self) -> dict:
        if self.durability <= 0:
            return {
                "artifact": self.name,
                "status": "destroyed",
            }

        self.durability -= 1

        return {
            "artifact": self.name,
            "effect": self.effect,
            "remaining_durability": self.durability,
        }
