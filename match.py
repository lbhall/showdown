from tournament import WINNER_SIDE, LOSER_SIDE
from player import Player


class Match:
    def __init__(
            self,
            loser_side: bool,
            tournament_round: int,
            match_in_round: int,
            player1: Player = None,
            player2: Player = None,
    ):
        self.loser_side = loser_side
        self.tournament_round = tournament_round
        self.match_in_round = match_in_round
        self.player1 = player1
        self.player2 = player2
        self.loser_match_ref = ''
        self.winner_match_ref = ''

    @property
    def player1(self):
        return self.player1

    @player1.setter
    def player1(self, player: Player):
        self.player1 = player

    @property
    def player2(self):
        return self.player2

    @player2.setter
    def player2(self, player: Player):
        self.player2 = player

    def player_str(self, player1=True):
        player_from = ''

        if player1:
            player_name = self.player1 if self.player1 is not None else 'None'
            if self.player1_from is not None:
                player_from = self.player1_from
        else:
            player_name = self.player2 if self.player2 is not None else 'None'
            if self.player2_from is not None:
                player_from = self.player2_from

        return f'{player_name}({player_from})'

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        match_reference = self.match_ref
        return f'{match_reference} {self.player_str(True)} vs {self.player_str(False)} {self.winner_match_ref} {self.loser_match}'

    @property
    def match_ref(self):
        winner_or_loser = WINNER_SIDE if not self.loser_side else LOSER_SIDE
        return f'{winner_or_loser}{self.tournament_round}:{self.match_in_round}'
