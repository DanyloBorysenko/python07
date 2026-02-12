from ex4.TournamentCard import TournamentCard
from typing import Dict, List


class TournamentPlatform:
    def __init__(self) -> None:
        self.tournament_cards: Dict[int, TournamentCard] = {}
        self.matches_played: int = 0
        self.total_cards = 0
        self.counter = 1

    def register_card(self, card: TournamentCard) -> str:
        self.tournament_cards.update({self.counter: card})
        self.total_cards += 1
        self.counter += 1
        return f"Card {card.name} id {self.counter - 1} was registered"

    def create_match(self, card1_id: str, card2_id: str) -> Dict:
        self.matches_played += 1
        card_1: TournamentCard = None
        card_2: TournamentCard = None
        winer = None
        loser = None
        winer_id = None
        loser_id = None
        try:
            card_1 = self.tournament_cards.get(int(card1_id))
            card_2 = self.tournament_cards.get(int(card2_id))
            if card_1.attack >= card_2.attack:
                winer = card_1
                winer_id = card1_id
                loser = card_2
                loser_id = card2_id
            else:
                winer = card_2
                winer_id = card2_id
                loser = card_1
                loser_id = card1_id
            winer.update_wins(1)
            loser.update_losses(1)
            return {'winner': f"{winer.name}_{winer_id}",
                    'loser': f"{loser.name}_{loser_id}",
                    'winner_rating': winer.rating,
                    'loser_rating': loser.rating}
        except Exception as e:
            print(e)
            return {}

    def get_leaderboard(self) -> List:
        if len(self.tournament_cards) == 0:
            return []
        else:
            cards = list(self.tournament_cards.values())
            cards.sort(key=lambda card: card.rating,
                       reverse=True)
            return cards

    def generate_tournament_report(self) -> Dict:
        if self.total_cards == 0:
            avg_rating = 0
        else:
            ratings_sum = sum([card.rating
                               for card in self.tournament_cards.values()])
            avg_rating = round(ratings_sum / self.total_cards)
        return {'total_cards': len(self.tournament_cards),
                'matches_played': self.matches_played,
                'avg_rating': avg_rating, 'platform_status': 'active'}
