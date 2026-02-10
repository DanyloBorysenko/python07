from typing import Dict, List
from ex3.CardFactory import CardFactory
from ex0.Card import Card, Rarities
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard, SpellEffect
from ex1.Deck import Deck
import random


class FantasyCardFactory(CardFactory):

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        sup_types: Dict[str, List[str]] = self.get_supported_types()
        name = random.choice(sup_types['creatures'])
        cost = random.randint(1, 5)
        rarity = Rarities.COMMON
        attack = random.randint(1, 5)
        health = random.randint(1, 5)
        if isinstance(name_or_power, str):
            if name_or_power not in sup_types["creatures"]:
                raise ValueError("not supported creature")
            name = name_or_power
        elif isinstance(name_or_power, int):
            if name_or_power <= 0:
                raise ValueError("power can not be negative")
            attack = name_or_power
        return CreatureCard(name, cost, rarity, attack, health)

        

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        sup_types: Dict[str, List[str]] = self.get_supported_types()
        name = random.choice(sup_types['spells'])
        cost = random.randint(1, 5)
        rarity = Rarities.COMMON
        effect = random.choice(list(SpellEffect))
        if isinstance(name_or_power, str):
            if name_or_power not in sup_types["spells"]:
                raise ValueError("not supported spell")
            name = name_or_power
        elif isinstance(name_or_power, int):
            if name_or_power < 3:
                effect = SpellEffect.BUFF
            elif name_or_power < 6:
                effect = SpellEffect.DEBUFF
            elif name_or_power < 8:
                effect = SpellEffect.HEAL
            else:
                effect = SpellEffect.DAMAGE
        return SpellCard(name, cost, rarity, effect.value)

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        sup_types: Dict[str, List[str]] = self.get_supported_types()
        name = random.choice(sup_types['artifacts'])
        cost = random.randint(1, 5)
        rarity = Rarities.EPIC
        durability = random.randint(1, 5)
        effect = random.choice(["Permanent: +1 mana per turn",
                                "Permanent: -1 mana per turn from all enemies"])
        if isinstance(name_or_power, str):
            if name_or_power not in sup_types["artifacts"]:
                raise ValueError("not supported artifact")
            name = name_or_power
        elif isinstance(name_or_power, int):
            if name_or_power <= 0:
                raise ValueError("power can not be negative")
            cost = name_or_power
            durability = name_or_power
        return ArtifactCard(name, cost, rarity, durability, effect)

    def create_themed_deck(self, size: int) -> Dict:
        deck = Deck()
        sup_types = self.get_supported_types()
        for _ in range(1, size + 1):
            card = random.choice(list(sup_types.keys()))
            if card == 'creatures':
                deck.add_card(self.create_creature())
            elif card == 'spells':
                deck.add_card(self.create_spell())
            elif card == 'artifacts':
                deck.add_card(self.create_artifact())
        return {"theme": "fantasy", "deck": deck, "size": size}

    def get_supported_types(self) -> Dict:
        return {'creatures': ['dragon', 'goblin'],
                'spells': ['fireball', 'iceball', 'lightning'],
                'artifacts': ['mana_ring']}