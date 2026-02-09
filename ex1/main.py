from ex1.Deck import Deck
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard, SpellEffect


if __name__ == "__main__":
   print(" === DataDeck Deck Builder ===")
   print()

   print("Building deck with different card types...\n")
   deck: Deck = Deck()
   creature_card: Card = CreatureCard(name="Fire Dragon", cost=5,
                                         rarity="Legendary",
                                         attack=7, health=5)
   spell_card: Card = SpellCard(name="Lightning Bolt", cost=3, rarity="Common",
                                effect_type=SpellEffect.DAMAGE)
   artifact_card: Card = ArtifactCard(name="Mana Crystal", cost=2,
                                      rarity="Common",
                                      effect="Permanent: +1 mana per turn")
   deck.add_card(creature_card)
   deck.add_card(spell_card)
   deck.add_card(artifact_card)

   print(f"Deck stats: {deck.get_deck_stats()}")