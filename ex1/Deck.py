from ex0.Card import Card, CardType
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard, SpellEffect
from ex1.ArtifactCard import ArtifactCard
from typing import Dict, List


class Deck:
    def __init__(self):
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
    
    def shuffle(self) -> None:
        pass
    
    def draw_card(self) -> Card:
        pass
    
    def get_deck_stats(self) -> Dict:
        deck_stats: Dict = {}
        total_cards_count = len(self.cards)
        creaters = 0
        spells = 0
        artifacts = 0
        cost_sum = 0.0
        avg_cost = 0.0
        for card in self.cards:
            if card.card_type == CardType.CREATURE:
                creaters += 1
            elif card.card_type == CardType.SPEL:
                spells += 1
            elif card.card_type == CardType.ARTIFACT:
                artifacts += 1
            cost_sum += card.cost
        if total_cards_count != 0:
            avg_cost = cost_sum / total_cards_count
        deck_stats["total_cards"] = total_cards_count
        deck_stats["creaters"] = creaters
        deck_stats["spells"] = spells
        deck_stats["artifacts"] = artifacts
        deck_stats["avg_cost"] = avg_cost
        return deck_stats
