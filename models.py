class Tournament:
    name = "My Tournament"
    double_elimination = True
    players = None

    def __init__(self, name:str, double_elimination:bool=True, players=None):
        if players is None:
            players = []
        self.name = name
        self.double_elimination = double_elimination
        self.players = players

    def regen(self):
        if self.players is not None and len(self.players) > 3:
            self.generate_bracket()

    def generate_bracket(self):
        pass

    def clear_players(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)
        self.regen()

    def get_players(self):
        return self.players

    def set_double_elimination(self, double_elimination:bool):
        self.double_elimination = double_elimination
        self.regen()

    def set_name(self, name:str):
        self.name = name