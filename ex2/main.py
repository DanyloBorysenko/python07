from ex2.EliteCard import EliteCard
from ex0.Card import Card, Rarities
from ex0.CreatureCard import CreatureCard


if __name__ == "__main__":
    print("=== DataDeck Ability System ===")
    print()

    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    arcane_warrior: Card = EliteCard(name="Arcane warrior", cost=5,
                                     rarity=Rarities.EPIC)
    print(f"\nPlaying Arcane Warrior ({arcane_warrior.card_type.value})")

    print("\nCombat phase:")
    target = CreatureCard(name="Enemy", cost=5, rarity=Rarities.COMMON.value,
                          attack=5, health=10)
    attack_res = arcane_warrior.attack(target)
    print(f"Attack result: {attack_res}")

    def_res = arcane_warrior.defend(1)
    print(f"Defense result: {def_res}")

    print("\nMagic phase:")

    print(f"Spell cast: {arcane_warrior.cast_spell("Fireball", [target])}")
    print(f"Mana channel: {arcane_warrior.channel_mana(3)}")

    print("\nMultiple interface implementation successful!")
