from abc import ABC, abstractmethod
from typing import Dict
from enum import Enum


class CardType(Enum):
    CREATURE = "Creature"
    SPELL = "Spell"


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        super().__init__()
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @property
    @abstractmethod
    def card_type(self) -> CardType:
        """returns specific card type"""
        pass

    @abstractmethod
    def play(self, game_state: Dict) -> Dict:
        pass

    def get_card_info(self) -> Dict:
        return {"name": self.name,
                "cost": self.cost,
                "rarity": self.rarity,
                "type": self.card_type.value}

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost


# class MyCard(Card):
#     pass
