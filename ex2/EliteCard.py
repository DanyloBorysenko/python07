from ex0.Card import Card, CardType
from ex0.CreatureCard import CreatureCard
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from typing import Dict, List, Union
# from enum import Enum


# class CombatType(Enum):
#     MELEE = "melee"


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str):
        super().__init__(name, cost, rarity)
        self.own_mana = 10
        self.health = 10
        self.atack = 5
        self.shield = 3
        self.still_alive = True

    # @property
    # def combat_type(self) -> CombatType:
    #     return CombatType.MELEE

    def cast_spell(self, spell_name: str,
                   targets: List[Union[CreatureCard, "EliteCard"]]) -> Dict:
        mana_used = 4
        return {'caster': self.name, 'spell': spell_name,
                'targets': [target.name for target in targets],
                'mana_used': mana_used}

    def channel_mana(self, amount: int) -> Dict:
        """Connect channels of mana(amount) to encrease own mana"""
        channel_value = 1
        self.own_mana += amount * channel_value
        return {'channeled': amount, 'total_mana': self.own_mana}

    def get_magic_stats(self) -> Dict:
        return {"name": self.name, "own_mana": self.own_mana}

    def attack(self, target: Union[CreatureCard, "EliteCard"]) -> Dict:
        target.health -= self.atack
        return {'attacker': self.name, 'target': target.name,
                'damage': self.atack, 'combat_type': "melee"}

    def defend(self, incoming_damage: int) -> Dict:
        damage_taken = incoming_damage - self.shield
        if damage_taken <= 0:
            damage_taken = 0
        self.health -= damage_taken
        if self.health <= 0:
            self.still_alive = False
        return {'defender': self.name, 'damage_taken': damage_taken,
                'damage_blocked': self.shield, 'still_alive': self.still_alive}

    def get_combat_stats(self) -> Dict:
        return {"name": self.name, "health": self.health,
                "damage_power": self.atack, "defend_power": self.shield,
                "is_still_alive": self.still_alive}

    @property
    def card_type(self) -> CardType:
        return CardType.ELITE_CARD

    def play(self, game_state: Dict) -> Dict:
        if self.is_playable(game_state["total_mana"]):
            game_state["total_mana"] -= self.cost
            return {'card_played': self.name,
                    'mana_used': self.cost}
        else:
            print("Not enough mana")
            return {}
