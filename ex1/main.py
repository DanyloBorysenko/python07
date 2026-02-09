from ex1.Deck import Deck
from ex0.Card import Card, Rarities
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard, SpellEffect


if __name__ == "__main__":
   print(" === DataDeck Deck Builder ===")
   print()

   print("Building deck with different card types...")
   deck: Deck = Deck()
   creature_card: Card = CreatureCard(name="Fire Dragon", cost=2,
                                         rarity=Rarities.LEGENDARY,
                                         attack=7, health=5)
   spell_card: Card = SpellCard(name="Lightning Bolt", cost=3,
                                rarity=Rarities.COMMON.value,
                                effect_type=SpellEffect.DAMAGE)
   artifact_card: Card = ArtifactCard(name="Mana Crystal", cost=5,
                                      rarity=Rarities.COMMON.value,
                                      effect="Permanent: +1 mana per turn",
                                      durability=3)
   deck.add_card(creature_card)
   deck.add_card(spell_card)
   deck.add_card(artifact_card)

   total_mana = 20
   game_stats = {"cards_available": deck.cards,
                  "total_mana": total_mana}

   print(f"Deck stats: {deck.get_deck_stats()}")

   print("\nDrawing and playing cards:\n")
   try:
        drew_card = deck.draw_card()
        print(f"Drew: {drew_card.name} ({drew_card.card_type.value})")
        print(f"Play result: {drew_card.play(game_stats)}")
   except Exception:
        print("Deck is empty")
   print()

   try:
        drew_card = deck.draw_card()
        print(f"Drew: {drew_card.name} ({drew_card.card_type.value})")
        print(f"Play result: {drew_card.play(game_stats)}")
   except Exception:
        print("Deck is empty")
   print()

   try:
        drew_card = deck.draw_card()
        print(f"Drew: {drew_card.name} ({drew_card.card_type.value})")
        print(f"Play result: {drew_card.play(game_stats)}")
   except Exception:
        print("Deck is empty")
   print()

   try:
        drew_card = deck.draw_card()
        print(f"Drew: {drew_card.name} ({drew_card.card_type.value})")
        print(f"Play result: {drew_card.play(game_stats)}")
   except Exception:
        print("Deck is empty")
   print()