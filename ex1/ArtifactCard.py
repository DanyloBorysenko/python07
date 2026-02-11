from ex0.Card import Card, CardType
from typing import Dict


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    @property
    def card_type(self) -> CardType:
        return CardType.ARTIFACT

    def play(self, game_state: Dict) -> Dict:
        if game_state["total_mana"] >= self.cost:
            game_state["total_mana"] -= self.cost
            return {'card_played': self.name, 'mana_used': self.cost,
                    'effect': self.effect}
        else:
            print("Not enough mana")
            return {}

    def get_card_info(self) -> Dict:
        card_info: Dict = super().get_card_info()
        card_info["effect"] = self.effect
        card_info["durability"] = self.durability
        return card_info

    def activate_ability(self) -> Dict:
        res: Dict = {self.name: self.effect}
        print(f"Ability activated: {res}")
        return res
