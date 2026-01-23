# from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex0.Card import CardRarity


def main():
    print("\n=== DataDeck Card Foundation ===")
    print("\nTesting Abstract Base Class Design:\n")

    # try:
    #     Card("Test", 1, "Common")
    # except TypeError as e:
    #     print("Cannot instantiate Card directly:", e)

    creature = CreatureCard(
        name="Fire Dragon",
        cost=5,
        rarity=CardRarity.LEGENDARY,
        attack=7,
        health=5
    )

    print("CreatureCard Info:")
    print(creature.get_card_info())

    mana = 6
    print(f"\nPlaying {creature.name} with {mana} mana available:")
    print("Playable:", creature.is_playable(mana))
    print("Play result:", creature.play({}))

    print(f"\n{creature.name} attacks Goblin Warrior:")
    print("Attack result:", creature.attack_target("Goblin Warrior"))

    mana = 3
    print(f"\nTesting insufficient mana ({mana} available):")
    print("Playable:", creature.is_playable(mana))

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
