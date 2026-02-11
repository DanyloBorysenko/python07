from ex0.Card import Card, CardType
from typing import Dict, List
import random


class Deck:
    def __init__(self):
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        card = random.choice(self.cards)
        self.remove_card(card_name=card.name)
        return card

    def get_deck_stats(self) -> Dict:
        deck_stats: Dict = {}
        total_cards_count = len(self.cards)
        creatures = 0
        spells = 0
        artifacts = 0
        cost_sum = 0.0
        avg_cost = 0.0
        for card in self.cards:
            if card.card_type == CardType.CREATURE:
                creatures += 1
            elif card.card_type == CardType.SPELL:
                spells += 1
            elif card.card_type == CardType.ARTIFACT:
                artifacts += 1
            cost_sum += card.cost
        if total_cards_count != 0:
            avg_cost = cost_sum / total_cards_count
        deck_stats["total_cards"] = total_cards_count
        deck_stats["creatures"] = creatures
        deck_stats["spells"] = spells
        deck_stats["artifacts"] = artifacts
        deck_stats["avg_cost"] = round(avg_cost, 1)
        return deck_stats
