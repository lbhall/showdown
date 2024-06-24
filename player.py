import logging


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

    @property
    def player1_name(self):
        return self.player1_name

    @player1_name.setter
    def player1_name(self, player1_name:str):
        self.player1_name = player1_name

    @property
    def player2_name(self):
        return self.player1_name

    @player2_name.setter
    def player2_name(self, player2_name: str):
        self.player2_name = player2_name

    @@property
    def winner(self):
        return self.winner

    @winner.setter
    def winner(self, winner: str):
        self.winner = winner


class Player:
    def __init_(self, name:str):
        self.name = name
        self.matches_history = []

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name:str):
        self.name = name

    def add_history(self, history: MatchHistory):
        self.matches_history.append(history)

    @property
    def matches_history(self):
        return self.matches_history

    @matches_history.setter
    def matches_history(self, history:MatchHistory):
        self.matches_history = history