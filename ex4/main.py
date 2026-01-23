import random

from ex0.Card import CardRarity
from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("\n=== DataDeck Grand Tournament (6 Fighters) ===\n")

    platform = TournamentPlatform()

    roster = [
        TournamentCard(
            "dragon_01",
            "Red Dragon",
            6,
            CardRarity.LEGENDARY,
            8,
            8,
        ),
        TournamentCard(
            "wizard_01",
            "Ice Wizard",
            4,
            CardRarity.RARE,
            4,
            4,
        ),
        TournamentCard(
            "goblin_01",
            "Goblin King",
            3,
            CardRarity.RARE,
            3,
            5,
        ),
        TournamentCard(
            "knight_01",
            "Holy Knight",
            5,
            CardRarity.RARE,
            5,
            7,
        ),
        TournamentCard(
            "elf_01",
            "Forest Elf",
            2,
            CardRarity.COMMON,
            2,
            3,
        ),
        TournamentCard(
            "witch_01",
            "Dark Witch",
            4,
            CardRarity.LEGENDARY,
            6,
            4,
        ),
    ]

    print(f"Registering {len(roster)} fighters...")
    for card in roster:
        platform.register_card(card)
        print(f" -> {card.name} ({card.attack_power} ATK) ready!")

    all_ids = platform.get_all_ids()

    print("\n--- STARTING RANDOM MATCHES ---")

    for match_number in range(1, 6):
        fighter1_id, fighter2_id = random.sample(all_ids, 2)

        print(
            f"\nMatch #{match_number}: "
            f"{fighter1_id} VS {fighter2_id}"
        )

        match_result = platform.create_match(
            fighter1_id,
            fighter2_id,
        )

        print(
            f"Winner: {match_result['winner']} | "
            f"Loser: {match_result['loser']}"
        )

    print("\n--- FINAL LEADERBOARD ---")

    leaderboard = platform.get_leaderboard()

    for rank, card in enumerate(leaderboard, start=1):
        info = card.get_rank_info()
        streak_icon = "🔥" if info["streak"] > 1 else ""

        print(
            f"{rank}. {card.name.ljust(15)} | "
            f"Rating: {info['rating']} | "
            f"W-L: {info['wins']}-{info['losses']} {streak_icon}"
        )

    print("\n=== Tournament Completed Successfully! ===")


if __name__ == "__main__":
    main()
