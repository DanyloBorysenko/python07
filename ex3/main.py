from ex3.CardFactory import CardFactory
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameStrategy import GameStrategy
from ex3.AggressiveStrategy import AggressiveStrategy
from ex1.Deck import Deck
from ex3.GameEngine import GameEngine


if __name__ == "__main__":
    print("=== DataDeck Game Engine ===")
    print()

    print("Configuring Fantasy Card Game...")
    factory: CardFactory = FantasyCardFactory()
    strategy: GameStrategy = AggressiveStrategy()
    print("Factory: FantasyCardFactory")
    print("Strategy: AggressiveStrategy")

    print(f"Available types: {factory.get_supported_types()}")
    print()

    print("Simulating aggressive turn...")
    engine = GameEngine()
    engine.configure_engine(factory=factory, strategy=strategy)
    print(f"Engine status: {engine.get_engine_status()}")
    deck: Deck = engine.factory.create_themed_deck(5)["deck"]
    print(f"hand - {[f"{card.name} ({card.cost})" for card in deck.cards]}")
    print()
    print("Turn execution:")
    print(f"{engine.strategy.execute_turn(deck.cards, [])}")
