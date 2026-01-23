from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self, factory: CardFactory, strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy
        self.hand: list = []
        self.battlefield: list = []

    def configure_engine(
        self,
        factory: CardFactory,
        strategy: GameStrategy
    ) -> None:
        self.factory = factory
        self.strategy = strategy
        self.hand = []
        self.battlefield = []

    def simulate_turn(self) -> dict:
        if not self.hand:
            deck_info = self.factory.create_themed_deck(6)
            self.hand = deck_info["cards"]

        decision = self.strategy.execute_turn(self.hand, self.battlefield)

        return {
            "turns_simulated": 1,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": decision.get("damage_dealt", 0),
            "cards_created": len(self.hand),
            "actions": decision,
        }

    def get_engine_status(self) -> dict:
        return {
            "hand": [card.name for card in self.hand],
            "battlefield": [card.name for card in self.battlefield],
        }
