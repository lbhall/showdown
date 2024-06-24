from tournament import WINNER_SIDE, LOSER_SIDE
from player import Player

class Match:
    player1 = None
    player2 = None
    player1_name = None       # The name of the first player in the match
    player1_from = None  # which match did player 1 come from
    player2 = None       # The name of the second player in the match
    player2_from = None  # which match did player 2 come from
    winner = None        # who won the match
    winner_match = None  # the reference for the match the winner will play next
    loser_side = False   # is this a lose side match
    loser_match = None   # the reference to the match the loser will play next
    tournament_round = 0 # which round this match is in
    match_in_round = 0   # the number if this match within the round

    def __init__(self, loser_side, tournament_round, match_in_round):
        self.loser_side = loser_side
        self.tournament_round = tournament_round
        self.match_in_round = match_in_round

    def set_player1(self, name: str, match_from: str, player1: bool=True):
        if player1:
            player1
            pass
        else:
            pass

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
        match_reference = self.match_reference()
        string_val = f'<Match {match_reference} {self.player_str(True)} vs {self.player_str(False)}'
        if self.winner_match is not None:
            string_val += f' W={self.winner_match}'
        if self.loser_match is not None:
            string_val += f' L={self.loser_match}'
        string_val += '>'
        return string_val

    def __str__(self):
        match_reference = self.match_reference()
        string_val = f'{match_reference} {self.player_str(True)} vs {self.player_str(False)}'
        if self.winner_match is not None:
            string_val += f' W={self.winner_match}'
        if self.loser_match is not None:
            string_val += f' L={self.loser_match}'
        return string_val

    def match_reference(self):
        winner_or_loser = WINNER_SIDE if not self.loser_side else LOSER_SIDE
        return f'{winner_or_loser}{self.tournament_round}:{self.match_in_round}'

