from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main():
    print("=== DataDeck Game Engine Demo ===")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine(factory, strategy)

    print("\nSetting up game...")
    setup_info = engine.setup_game(deck_size=6, hand_size=3)
    print(setup_info)

    print("\nInitial game state:")
    print(engine.get_game_state())

    print("\nPlaying one turn...")
    turn_result = engine.play_turn()
    print(turn_result)

    print("\nGame state after turn:")
    print(engine.get_game_state())

    print("\nex3 demonstration completed successfully!")


if __name__ == "__main__":
    main()
