from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return available_targets

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        actions = {
            "strategy": self.get_strategy_name(),
            "cards_played": [],
            "mana_used": 0,
        }

        if hand:
            card = hand[0]
            actions["cards_played"].append(card.name)
            actions["mana_used"] += card.cost

        return actions
