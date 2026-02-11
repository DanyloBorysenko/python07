from typing import Dict
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self):
        self.factory = None
        self.strategy = None
        self.turns_simulated = 0
        self.cards_created = 0

    def configure_engine(self, factory: CardFactory, strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> Dict:
        cards_count = 3
        self.simulate_turn += 1
        deck = self.factory.create_themed_deck(cards_count)["deck"]
        self.strategy.execute_turn(deck.cards, [])

    def get_engine_status(self) -> Dict:
        return {"name": self.__class__.__name__,
                "factory": self.factory.__class__.__name__,
                "strategy": self.strategy.__class__.__name__}
