from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self, factory: CardFactory, strategy: GameStrategy):
        self.factory = factory
        self.strategy = strategy
        self.hand = []
        self.battlefield = []

    def setup_game(self, deck_size: int = 6, hand_size: int = 3) -> dict:
        deck_info = self.factory.create_themed_deck(deck_size)
        deck = deck_info["cards"]

        self.hand = deck[:hand_size]
        self.battlefield = []

        return {
            "engine": "initialized",
            "strategy": self.strategy.get_strategy_name(),
            "factory": deck_info["theme"],
            "hand_size": len(self.hand),
        }

    def play_turn(self) -> dict:
        decision = self.strategy.execute_turn(
            self.hand,
            self.battlefield,
        )

        for card_name in decision.get("cards_played", []):
            for card in list(self.hand):
                if card.name == card_name:
                    self.hand.remove(card)
                    self.battlefield.append(card)
                    break

        return {
            "turn_result": decision,
            "hand_remaining": len(self.hand),
            "battlefield_size": len(self.battlefield),
        }

    def get_game_state(self) -> dict:
        return {
            "hand": [card.name for card in self.hand],
            "battlefield": [card.name for card in self.battlefield],
        }
