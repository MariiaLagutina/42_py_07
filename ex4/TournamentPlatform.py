from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self) -> None:
        self._cards: dict[str, TournamentCard] = {}
        self._matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        if card.card_id in self._cards:
            raise ValueError(
                f"Card with ID '{card.card_id}' is already registered"
            )

        self._cards[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        if card1_id == card2_id:
            raise ValueError("A card cannot play against itself")

        card1 = self._cards.get(card1_id)
        card2 = self._cards.get(card2_id)

        if not card1 or not card2:
            raise ValueError("Both cards must be registered")

        if card1.attack_power >= card2.attack_power:
            winner, loser = card1, card2
        else:
            winner, loser = card2, card1

        winner.process_match_result(True)
        loser.process_match_result(False)
        self._matches_played += 1

        return {
            "winner": winner.card_id,
            "loser": loser.card_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating(),
        }

    def get_leaderboard(self) -> list:
        return sorted(
            self._cards.values(),
            key=lambda card: card.calculate_rating(),
            reverse=True,
        )

    def generate_tournament_report(self) -> dict:
        total_cards = len(self._cards)
        avg_rating = (
            sum(card.calculate_rating() for card in self._cards.values())
            // total_cards
            if total_cards > 0
            else 0
        )

        return {
            "total_cards": total_cards,
            "matches_played": self._matches_played,
            "avg_rating": avg_rating,
            "platform_status": "active",
        }

    def get_all_ids(self) -> list:
        return list(self._cards.keys())
