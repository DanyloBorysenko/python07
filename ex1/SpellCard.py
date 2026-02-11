from typing import Dict, List
from ex0.Card import Card, CardType
from ex0.CreatureCard import CreatureCard
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
        self.is_used = False

    def play(self, game_state: Dict) -> Dict:
        if game_state["total_mana"] >= self.cost:
            game_state["total_mana"] -= self.cost
            return {'card_played': self.name, 'mana_used': self.cost,
                    'effect': 'Deal 3 damage to target'}
        else:
            print("Not enough mana")
            return {}

    def resolve_effect(self, targets: List[CreatureCard]) -> Dict:
        effect_value = 1
        effect = self.effect_type
        res = {}
        if targets:
            for target in targets:
                if effect == SpellEffect.DAMAGE.value:
                    target.health -= effect_value
                elif effect == SpellEffect.HEAL.value:
                    target.health += effect_value
                elif effect == SpellEffect.BUFF.value:
                    target.attack += effect_value
                elif effect == SpellEffect.DEBUFF.value:
                    target.attack -= effect_value
                res[target.name] = effect_value
            self.is_used = True
        return res

    def get_card_info(self) -> Dict:
        card_info: Dict = super().get_card_info()
        card_info["effect_type"] = self.effect_type
        return card_info

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost and self.is_used is False
