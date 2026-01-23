from ex0.Card import Card, CardRarity
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex2.EliteCard import EliteCard


def get_interface_methods(cls):
    return [func for func in dir(cls) if callable(getattr(cls, func))
            and not func.startswith("__")]


def main():
    print("\n=== DataDeck Ability System ===")

    elite = EliteCard(
        name="Arcane Warrior",
        cost=6,
        rarity=CardRarity.LEGENDARY,
        attack_power=5,
        health=10,
        mana=8
    )

    print("\nEliteCard capabilities:")
    print(f"Card: {get_interface_methods(Card)}")
    print(f"Combatable: {get_interface_methods(Combatable)}")
    print(f"Magical: {get_interface_methods(Magical)}")

    print(f"\nPlaying {elite.name} (Elite Card):")
    print(elite.play({}))

    print("\nCombat phase:")
    attack_res = elite.attack("Enemy Minion")
    print("Attack result:", attack_res)

    defense_res = elite.defend(3)
    print("Defense result:", defense_res)

    print("\nMagic phase:")
    spell_res = elite.cast_spell("Fireball", ["Enemy 1", "Enemy 2"])
    print("Spell cast:", spell_res)

    channel_res = elite.channel_mana(3)
    print("Mana channel:", channel_res)

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
