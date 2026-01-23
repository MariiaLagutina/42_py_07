from ex0.Card import CardRarity
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main():
    print("\n=== DataDeck Deck Builder ===")

    creature = CreatureCard(
        name="Fire Dragon",
        cost=5,
        rarity=CardRarity.LEGENDARY,
        attack=7,
        health=5,
    )

    spell = SpellCard(
        name="Lightning Bolt",
        cost=3,
        rarity=CardRarity.RARE,
        effect_type="3 damage to target",
    )

    artifact = ArtifactCard(
        name="Mana Crystal",
        cost=2,
        rarity=CardRarity.RARE,
        durability=3,
        effect="+1 mana per turn",
    )

    deck = Deck()

    print("\nBuilding deck with different card types...")
    deck.add_card(creature)
    deck.add_card(spell)
    deck.add_card(artifact)

    print("Deck stats:", deck.get_deck_stats())

    print("\nDrawing and playing cards:\n")
    deck.shuffle()

    while True:
        try:
            card = deck.draw_card()
            card_type = card.__class__.__name__.replace("Card", "")
            print(f"\nDrew: {card.name} ({card_type})")
            print("Play result:", card.play({}))
        except IndexError:
            break

    print(
        "\nPolymorphism in action: "
        "Same interface, different card behaviors!"
    )


if __name__ == "__main__":
    main()
