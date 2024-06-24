from constants import (
    WINNER_SIDE,
    LOSER_SIDE,
    LOSER_CONFIGURATION,
)

class Tournament:
    name = 'My Tournament'
    double_elimination = False
    bracket_size = None
    tournament_bracket = {
        WINNER_SIDE: {},
        LOSER_SIDE: {}
    }
    number_of_players = 0
    max_winner_round = 0
    max_loser_round = 0

    def __init__(self, num_players, double_elimination=False):
        self.number_of_players = num_players
        self.double_elimination = False if num_players <= 2 else double_elimination
        self.set_bracket_size()
        logging.info(f'Init Tournament-> Num Players: {self.number_of_players}, Bracket Size: {self.bracket_size}, Double Elimination: {self.double_elimination}')

    def get_max_round(self, bracket_side='W'):
        return list(self.tournament_bracket[bracket_side].keys())[-1]

    def find_last_winner_match_ref(self):
        try:
            return self.tournament_bracket[WINNER_SIDE][self.get_max_round()][0]
        except Exception as err:
            logging.exception(f'Exception: {err}')

        return ''

    def find_match(self, match_ref) -> Optional["Match"]:
        try:
            if match_ref == 'FINALS':
                return self.find_last_winner_match_ref()

            parts = match_ref.split(':')
            tournament_round = parts[0][1]
            match_in_round = parts[1]
            winner_or_loser = match_ref[0]

            return self.tournament_bracket[winner_or_loser][int(tournament_round)][int(match_in_round) - 1]
        except Exception as err:
            logging.exception(f'Exception: {err}, match not found for match: {match_ref}')

        return None

    @staticmethod
    def get_loser_round(tournament_round):
        match tournament_round:
            case 1:
                return 1
            case 2:
                return 2
            case 3:
                return 4
            case 4:
                return 6
            case 5:
                return 8

    def set_bracket_size(self):
        self.bracket_size = 0
        power_of_2 = 0
        while self.bracket_size < self.number_of_players:
            power_of_2 += 1
            self.bracket_size = pow(2, power_of_2)

    def map_from(self, from_ref, to_ref):
        match = self.find_match(to_ref)
        if match is not None:
            if match.player1_from is None:
                match.player1_from = from_ref
            else:
                match.player2_from = from_ref

    def process_mapping(self, bracket_side):
        for i in range(1, self.get_max_round(bracket_side)):
            current_round_matches = self.tournament_bracket[bracket_side][i]
            for match in current_round_matches:
                self.map_from(match.match_reference(), match.winner_match)
                if match.loser_match is not None:
                    self.map_from(match.match_reference(), match.loser_match)

    def create_from_mappings(self):
        self.process_mapping(WINNER_SIDE)
        self.process_mapping(LOSER_SIDE)

    def generate_bracket(self):
        tournament_round = 1
        num_matches_in_round = self.bracket_size / 2
        not_done = True
        backwards=False
        populate_loser_match_fully = True

        # generate winner side draw
        while not_done:
            if num_matches_in_round == 1:
                not_done = False

            self.tournament_bracket[WINNER_SIDE][tournament_round] = (
                self.generate_winner_round(
                    tournament_round, num_matches_in_round, backwards, populate_loser_match_fully))
            tournament_round += 1
            num_matches_in_round = num_matches_in_round / 2
            backwards = not backwards
            populate_loser_match_fully = False

        self.max_winner_round = tournament_round

        if self.double_elimination:
            new_match = Match(False, tournament_round, 1)
            self.tournament_bracket[WINNER_SIDE][tournament_round] = [new_match]

            # generate the loser side draw
            for loser_round in range(loser_configuration[str(self.bracket_size)]['number_of_rounds']):
                tournament_round = loser_round + 1
                self.tournament_bracket[LOSER_SIDE][tournament_round] = self.generate_loser_round(tournament_round)
                self.max_loser_round = tournament_round
        self.create_from_mappings()

    def generate_winner_round(
            self, tournament_round, num_matches_in_round, backwards=False, populate_loser_match_fully=True):
        round_matches = []

        for match_in_round in range(int(num_matches_in_round)):
            new_match = Match(False, tournament_round, match_in_round + 1)
            if num_matches_in_round > 1 or num_matches_in_round == 1 and self.double_elimination:
                winner_match_in_round = int(math.ceil(new_match.match_in_round / 2))
                winner_reference = WINNER_SIDE + str(tournament_round + 1) + ':' + str(winner_match_in_round)
                new_match.winner_match = winner_reference
                if self.double_elimination:
                    loser_round = Tournament.get_loser_round(tournament_round)
                    if not backwards:
                        if populate_loser_match_fully:
                            loser_match_in_round = winner_match_in_round
                        else:
                            loser_match_in_round = match_in_round + 1
                    else:
                        loser_match_in_round = int(num_matches_in_round - match_in_round)
                    loser_reference = LOSER_SIDE + str(loser_round) + ':' + str(loser_match_in_round)
                    new_match.loser_match = loser_reference
            round_matches.append(new_match)
        return round_matches

    def generate_loser_round(self, loser_bracket_round):
        matches_in_round = loser_configuration[str(self.bracket_size)]['matches_per_round'][str(loser_bracket_round)]
        round_matches = []
        even = False
        if loser_bracket_round // 2 * 2 == loser_bracket_round:
            even = True

        last_match = None
        for match_in_round in range(matches_in_round):
            new_match = Match(True, loser_bracket_round, match_in_round + 1)
            last_match = new_match
            if loser_bracket_round < loser_configuration[str(self.bracket_size)]['number_of_rounds']:
                target_match_in_next_round = match_in_round
                if even:
                    target_match_in_next_round = math.ceil(match_in_round/2)
                target_match_in_next_round += 1
                new_match.winner_match = f'L{loser_bracket_round + 1}:{target_match_in_next_round}'
            round_matches.append(new_match)

        if last_match is not None:
            finals_ref = self.find_last_winner_match_ref()
            last_match.winner_match = finals_ref

        return round_matches

    def tourney_type(self):
        return 'Double' if self.double_elimination else 'Single'
