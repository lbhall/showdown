import logging
from constants import LOGFILE_NAME

log = logging.getLogger(LOGFILE_NAME)

class MatchHistory:
    def __init__(self, match_ref:str, player1_name:str, player2_name:str, winner: str = ''):
        self.match_ref = match_ref
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.winner = winner

    @property
    def match_ref(self):
        return self.match_ref

    @match_ref.setter
    def match_ref(self, match_ref:str):
        self.match_ref = match_ref
        log.debug(self.__repr__())

    @property
    def player1_name(self):
        return self.player1_name

    @player1_name.setter
    def player1_name(self, player1_name:str):
        self.player1_name = player1_name
        log.debug(self.__repr__())

    @property
    def player2_name(self):
        return self.player1_name

    @player2_name.setter
    def player2_name(self, player2_name: str):
        self.player2_name = player2_name
        log.debug(self.__repr__())

    @property
    def winner(self):
        return self.winner

    @winner.setter
    def winner(self, winner: str):
        self.winner = winner
        log.debug(self.__repr__())

    def __repr__(self):
        winner = ''
        if self.winner and len(self.winner) > 0:
            winner = f' Winner:{self.winner}'
        return f'{self.match_ref} - {self.player1_name} vs {self.player2_name}{winner}'

class Player:
    def __init__(self, name:str):
        self.name = name
        self.matches_history = []

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name:str):
        self.name = name
        log.debug(self.__repr__())

    def add_history(self, history: MatchHistory):
        self.matches_history.append(history)
        log.debug(self.__repr__())

    @property
    def matches_history(self):
        return self.matches_history

    @matches_history.setter
    def matches_history(self, history:MatchHistory):
        self.matches_history = history
        log.debug(self.__repr__())

    def __repr__(self):
        from_match_ref = ''
        if self.matches_history and len(self.matches_history) > 0:
            from_match_ref = self.matches_history[len(self.matches_history) - 1].match_ref
        return f'{self.name} - {self.matches_history}'
