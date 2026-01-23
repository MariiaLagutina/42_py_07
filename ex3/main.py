from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main():
    print("\n=== DataDeck Game Engine ===")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine(factory, strategy)

    print("\nConfiguring Fantasy Card Game...")
    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")

    engine.configure_engine(factory, strategy)

    print("\nSimulating aggressive turn...")

    report = engine.simulate_turn()

    print("\n[Current Hand]:")
    for card in engine.hand:
        dmg = getattr(card, "attack", getattr(card, "attack_power", 0))
        print(f" - {card.name} (Cost: {card.cost}, Dmg: {dmg})")

    actions = report["actions"]
    print("\n[Turn Execution Log]:")
    print(f"Strategy Used: {report['strategy_used']}")

    print(f"Cards Played: {', '.join(actions['cards_played'])}")
    print(f"Mana Used: {actions['mana_used']}/10")

    print(f"Target Priority: {actions['targets_attacked']}")

    if actions.get("special_effects"):
        print("\n*** COMBO TRIGGERED ***")
        for effect in actions["special_effects"]:
            print(f"🔥 {effect} 🔥")
        print("***********************")

    print("\n[Game Report]:")
    print(f"Total Damage Dealt: {report['total_damage']}")
    print(f"Cards Created: {report['cards_created']}")

    print("\nAbstract Factory + Strategy Pattern: "
          "Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
