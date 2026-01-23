from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def get_strategy_name(self) -> str:
        return "AggressiveStrategy (Berserker Mode)"

    def prioritize_targets(self, available_targets: list) -> list:
        return sorted(
            available_targets,
            key=lambda t: "Player" not in str(t)
        )

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        actions = {
            "cards_played": [],
            "mana_used": 0,
            "targets_attacked": [],
            "damage_dealt": 0,
            "special_effects": []
        }

        playable_cards = list(hand)

        playable_cards.sort(key=lambda card: card.cost)

        current_mana = 10
        cards_played_count = 0

        for card in playable_cards:
            if actions["mana_used"] + card.cost > current_mana:
                continue

            actions["cards_played"].append(card.name)
            actions["mana_used"] += card.cost

            base_damage = getattr(
                card,
                "attack",
                getattr(card, "attack_power", 0)
            )
            actions["damage_dealt"] += base_damage

            battlefield.append(card)
            cards_played_count += 1

        if cards_played_count >= 3:
            bonus_damage = 5
            actions["damage_dealt"] += bonus_damage

            if "special_effects" not in actions:
                actions["special_effects"] = []

            actions["special_effects"].append(
                "BERSERKER RAGE! (+5 Damage Bonus)"
            )

        potential_targets = ["Enemy Minion", "Enemy Dragon", "Enemy Player"]
        priority_list = self.prioritize_targets(potential_targets)

        if priority_list:
            actions["targets_attacked"] = [priority_list[0]]

        return actions
