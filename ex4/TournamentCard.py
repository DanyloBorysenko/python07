from ex0.Card import Card, CardType
from ex4.Rankable import Rankable
from ex2.Combatable import Combatable
from typing import Dict


class TournamentCard(Card, Rankable, Combatable):
    def __init__(self, name: str, cost: int,
                 rarity: str, id: str, attack: int,
                 shield: int):
        super().__init__(name, cost, rarity)
        self.rating = 0
        self.wins = 0
        self.losses = 0
        self.attack = attack
        self.id = id

    @property
    def card_type(self) -> CardType:
        """returns specific card type"""
        CardType.TOURNAMENT_CARD

    def play(self, game_state: Dict) -> Dict:
        return {"card played": self.name, "rating": self.rating}

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.rating += wins * 16

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.rating -= losses * 16

    def get_rank_info(self) -> Dict:
        return {"name": self.name, "rating": self.rating,
                "wins": self.wins, "losses": self.losses}

    def attack(self, target) -> Dict:
        if isinstance(target, TournamentCard):
            return {"target": target.name, "damage": self.attack}
        else:
            return {}

    def defend(self, incoming_damage: int) -> Dict:
        # max()
        return {"name": self.name, "damage_received": incoming_damage}

    def get_combat_stats(self) -> Dict:
        return {"name": self.name, "power": self.attack}
