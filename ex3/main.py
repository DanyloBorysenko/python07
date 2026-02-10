from ex3.CardFactory import CardFactory
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameStrategy import GameStrategy
from ex3.AggressiveStrategy import AggressiveStrategy


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

    deck_dict = factory.create_themed_deck(10)
    deck = deck_dict["deck"]
    for card in deck.cards:
        print(card.get_card_info())
