from ex0.Card import Card, Rarities
from ex0.CreatureCard import CreatureCard
# from ex0.Card import MyCard


if __name__ == "__main__":
    print("=== DataDeck Card Foundation ===")
    print("\nTesting Abstract Base Class Design:")
    try:
        dragon_card: Card = CreatureCard(name="Fire Dragon", cost=5,
                                         rarity=Rarities.LEGENDARY.value,
                                         attack=7, health=5)
        goblin_warrior: Card = CreatureCard(name="Goblin Warrior", cost=1,
                                            rarity=Rarities.LEGENDARY.value,
                                            attack=4, health=10)
    except ValueError as e:
        print(e)
        exit()

    total_mana = 6
    game_stats = {"cards_available": [dragon_card, goblin_warrior],
                  "total_mana": total_mana}

    print("CreatureCard Info:")
    print(dragon_card.get_card_info())

    print(f"\nPlaying Fire Dragon with {total_mana} mana available:")
    print(f"Playable: {dragon_card.is_playable(game_stats['total_mana'])}")
    print(f"Play result: {dragon_card.play(game_stats)}")

    print("\nFire Dragon attacks Goblin Warrior:")
    print(f"Attack result: {dragon_card.attack_target(goblin_warrior)}")

    total_mana = 3
    print(f"\nTesting insufficient mana ({total_mana} available):")
    print(f"Playable: {dragon_card.is_playable(total_mana)}")
    print("Abstract pattern successfully demonstrated!")

    # MyCard("dfdsf", 5, "rare")
