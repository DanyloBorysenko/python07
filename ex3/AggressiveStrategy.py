from ex3.GameStrategy import GameStrategy
from typing import List, Dict, Union
from ex0.CreatureCard import CreatureCard
from ex2.EliteCard import EliteCard
from ex0.Card import Card


# def sort_by_health(card: Union[CreatureCard, EliteCard]) -> int:
#     return card.health


class AggressiveStrategy(GameStrategy):
    def __init__(self):
        super().__init__()

    def execute_turn(self, hand: List[Card], battlefield: List) -> Dict:
        mana_used = 0
        damage = 0
        hand.sort(key=lambda card: card.cost)
        for card in hand:
            if isinstance(card, CreatureCard) or isinstance(card, EliteCard):
                damage += card.attack
            mana_used += card.cost
        return {'cards_played': [f"{card.name} ({card.cost})"
                                 for card in hand],
                'mana_used': mana_used, 'targets_attacked': ['Enemy Player'],
                'damage_dealt': damage}

    def get_strategy_name(self) -> str:
        return self.__class__.__name__

    def prioritize_targets(self,
                           available_targets: List[
                               Union[CreatureCard, EliteCard]]) -> List[
                                   Union[CreatureCard, EliteCard]]:
        # available_targets.sort(key=sort_by_health)
        available_targets.sort(key=lambda card: card.health)
        return available_targets
