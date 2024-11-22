import logging
from constants import (
    LOGFILE_NAME,
    WINNER_SIDE,
    LOSER_SIDE,
)
from typing import Optional
log = logging.getLogger(LOGFILE_NAME)


class MatchRef:
    """ Match References should be in the form of W:1:1 where the first letter indicates either a winner(W) or
    losser(L) side match.  The first 1 is for the round of the match and the last 1 is for the match within the
    round so this example is for the first match of the first round on the winner side. """

    def __init__(self, winner_side: bool, tournament_round: int, match_in_round: int):
        self.winner_side = winner_side
        self.round = tournament_round
        self.match_number = match_in_round

    @property
    def is_winner_side(self):
        return self.winner_side

    @property
    def tournament_round(self):
        return self.round

    @property
    def match_in_round(self):
        return self.match_number

    def __str__(self):
        bracket = WINNER_SIDE if self.winner_side else LOSER_SIDE
        return f'{bracket}{self.round}: {self.match_number}'


class Player:
    def __init__(self, name: str):
        self.name = name

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name: str):
        log.debug(f'Player SET name {self.name} to {name}')
        self.name = name
        log.debug(self.__repr__())

    def __repr__(self):
        return self.name


class Match:
    def __init__(
            self,
            winner_side: bool,
            tournament_round: int,
            match_in_round: int,
            player1: Optional[Player] = None,
            player2: Optional[Player] = None,
            winner_ref: Optional[MatchRef] = None,
            loser_ref: Optional[MatchRef] = None,
    ):
        self.ref = MatchRef(winner_side, tournament_round, match_in_round)
        self.player1 = player1
        self.player2 = player2
        self.winner_match_ref = winner_ref
        self.loser_match_ref = loser_ref

    @property
    def player1(self):
        return self.player1

    @player1.setter
    def player1(self, player: Player):
        log.debug(f'Match SET player1 to {player}')
        self.player1 = player
        log.debug(self.__repr__())

    @property
    def player2(self):
        return self.player2

    @player2.setter
    def player2(self, player: Player):
        log.debug(f'Match SET player2 to {player}')
        self.player2 = player
        log.debug(self.__repr__())

    @property
    def winner(self):
        return self.winner

    @winner.setter
    def winner(self, winner: str):
        if winner not in [self.player1.name, self.player2.name]:
            raise ValueError(f'MatchHistory Invalid winner {winner}, it must be {self.player1.name} or {self.player2.name}')
        log.debug(f'Match SET winner to {winner}')
        self.winner = winner
        log.debug(self.__repr__())

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        winner_match_ref = ''
        if self.winner_match_ref:
            winner_match_ref = self.winner_match_ref.__str__()
        loser_match_ref = ''
        if self.loser_match_ref:
            loser_match_ref = self.loser_match_ref.__str__()
        return f'{self.ref} {self.player1} vs {self.player2} {winner_match_ref} {loser_match_ref}'.strip()

    @property
    def match_ref(self):
        return self.ref

    @match_ref.setter
    def match_ref(self, match_ref: MatchRef):
        log.debug(f'Match SET match_ref to {match_ref}')
        self.ref = match_ref
        log.debug(self.__repr__())
