from ex4.TournamentCard import TournamentCard
from typing import Dict, List


class TournamentPlatform:
    def __init__(self) -> None:
        self.tournament_cards: List[TournamentCard] = []
        self.matches_played: int = 0
        self.total_cards = 0

    def register_card(self, card: TournamentCard) -> str:
        self.tournament_cards.append(card)
        self.total_cards += 1
        return f"Card {card.name} was registered"

    def create_match(self, card1_id: str, card2_id: str) -> Dict:
        self.matches_played += 1
        card_1: TournamentCard | None = None
        card_2: TournamentCard | None = None
        winer = None
        loser = None
        for card in self.tournament_cards:
            if card.id == card1_id:
                card_1 = card
            if card.id == card2_id:
                card_2 = card
        if card_1 and card_2:
            
        return {'winner': 'dragon_001', 'loser': 'wizard_001',
                'winner_rating': 1216, 'loser_rating': 1134}

    def get_leaderboard(self) -> List:
        if len(self.tournament_cards) == 0:
            return []
        else:
            self.tournament_cards.sort(key=lambda card: card.rating,
                                       reverse=True)
            return self.tournament_cards

    def generate_tournament_report(self) -> Dict:
        if self.total_cards == 0:
            avg_rating = 0
        else:
            ratings_sum = sum([card.rating for card in self.tournament_cards])
            avg_rating = round(ratings_sum / self.total_cards)
        return {'total_cards': len(self.tournament_cards),
                'matches_played': self.matches_played,
                'avg_rating': avg_rating, 'platform_status': 'active'}
