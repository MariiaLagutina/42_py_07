import random

from ex0.Card import CardRarity
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    _CREATURES = [
        ("Fire Dragon", 5, CardRarity.LEGENDARY, 7, 5),
        ("Goblin Warrior", 2, CardRarity.COMMON, 2, 1),
        ("Ice Wizard", 4, CardRarity.RARE, 3, 4),
    ]

    _SPELLS = [
        ("Lightning Bolt", 3, CardRarity.COMMON, "damage"),
        ("Fireball", 4, CardRarity.RARE, "damage"),
        ("Healing Potion", 2, CardRarity.COMMON, "heal"),
    ]

    _ARTIFACTS = [
        ("Mana Crystal", 2, CardRarity.COMMON, 5, "+1 mana per turn"),
        ("Sword of Power", 3, CardRarity.RARE, 3, "+2 attack"),
    ]

    def create_creature(self, name_or_power=None) -> CreatureCard:
        name, cost, rarity, attack, health = random.choice(self._CREATURES)

        if isinstance(name_or_power, str):
            name = name_or_power
        elif isinstance(name_or_power, int):
            attack = name_or_power

        return CreatureCard(
            name=name,
            cost=cost,
            rarity=rarity,
            attack=attack,
            health=health,
        )

    def create_spell(self, name_or_power=None) -> SpellCard:
        name, cost, rarity, effect = random.choice(self._SPELLS)

        if isinstance(name_or_power, str):
            effect = name_or_power

        return SpellCard(
            name=name,
            cost=cost,
            rarity=rarity,
            effect_type=effect,
        )

    def create_artifact(self, name_or_power=None) -> ArtifactCard:
        name, cost, rarity, durability, effect = random.choice(self._ARTIFACTS)

        if isinstance(name_or_power, int):
            durability = name_or_power

        return ArtifactCard(
            name=name,
            cost=cost,
            rarity=rarity,
            durability=durability,
            effect=effect,
        )

    def create_themed_deck(self, size: int) -> dict:
        cards = []

        for i in range(size):
            if i % 3 == 0:
                cards.append(self.create_creature())
            elif i % 3 == 1:
                cards.append(self.create_spell())
            else:
                cards.append(self.create_artifact())

        return {
            "theme": "Fantasy",
            "size": size,
            "cards": cards,
        }

    def get_supported_types(self) -> dict:
        return {
            "creatures": [c[0] for c in self._CREATURES],
            "spells": [s[0] for s in self._SPELLS],
            "artifacts": [a[0] for a in self._ARTIFACTS],
        }
