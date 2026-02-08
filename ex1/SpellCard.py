from typing import Dict, List
from ex0.Card import Card, CardType
from enum import Enum


class SpellEffect(Enum):
    DAMAGE = "damage"
    HEAL = "heal"
    BUFF = "buff"
    DEBUFF = "debuff"


class SpellCard(Card):
    @property
    def card_type(self) -> CardType:
        return CardType.SPELL

    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        super().__init__(name=name, cost=cost, rarity=rarity)
        self.effect_type = effect_type

    def play(self, game_state: Dict) -> Dict:
        game_state["total_mana"] -= self.cost
        return {'card_played': self.name, 'mana_used': self.cost,
                'effect': 'Deal 3 damage to target'}

    def resolve_effect(self, targets: List) -> Dict:
        pass
