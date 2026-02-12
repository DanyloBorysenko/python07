from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform
from ex0.Card import Rarities


def print_leaderboard(platform: TournamentPlatform) -> None:
    print("\nCurrent leaderboard:")
    leaderboard = platform.get_leaderboard()
    for i in range(0, len(leaderboard)):
        print(f"{i + 1}. {leaderboard[i].name} "
              f"rating: {leaderboard[i].rating}")


if __name__ == "__main__":
    print("=== DataDeck Tournament Platform ===")
    print("\nRegistering Tournament Cards...")

    platform = TournamentPlatform()

    fire_dragon = TournamentCard(name="Fire Dragon",
                                 cost=4, rarity=Rarities.COMMON.value,
                                 attack=2, rating=1200)

    platform.register_card(fire_dragon)
    ice_wizard = TournamentCard(name="Ice Wizard", cost=5,
                                rarity=Rarities.COMMON.value,
                                attack=5, rating=1200)

    platform.register_card(ice_wizard)
    print_leaderboard(platform)

    print("\nCreating tournament match...\nResult:")
    match_info = platform.create_match("1", "2")
    print(match_info)
    print_leaderboard(platform)
    print(f"\nPlatform Report:\n{platform.generate_tournament_report()}")
