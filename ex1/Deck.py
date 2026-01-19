import random
import math
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard


class Deck:
    def __init__(self):
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        if not isinstance(card, Card):
            raise TypeError("Only Card instances can be added to the deck")
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if not self.cards:
            raise IndexError("Cannot draw from an empty deck")
        return self.cards.pop(0)

    def get_deck_stats(self) -> dict:
        total = len(self.cards)
        if total == 0:
            return {
                "total_cards": 0,
                "creatures": 0,
                "spells": 0,
                "artifacts": 0,
                "avg_cost": 0.0
                }

        creatures = sum(1 for c in self.cards if isinstance(c, CreatureCard))
        spells = sum(1 for c in self.cards if isinstance(c, SpellCard))
        artifacts = sum(1 for c in self.cards if isinstance(c, ArtifactCard))

        avg_cost = (
            sum(c.cost for c in self.cards) / total
            if total > 0 else 0
        )

        return {
            "total_cards": total,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": float(math.ceil(avg_cost)),
        }
