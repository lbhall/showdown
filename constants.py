LOGFILE_NAME = 'showdown.log'
MAX_PLAYERS = 32
WINNER_SIDE = 'W'
LOSER_SIDE = 'L'

LOSER_CONFIGURATION = {
    '2': {
        'number_of_rounds': 0,
    },
    '4': {
        'number_of_rounds': 2,
        'matches_per_round': {
            '1': 1,
            '2': 1,
        }
    },
    '8': {
        'number_of_rounds': 4,
        'matches_per_round': {
            '1': 2,
            '2': 2,
            '3': 1,
            '4': 1,
        }
    },
    '16': {
        'number_of_rounds': 6,
        'matches_per_round': {
            '1': 4,
            '2': 4,
            '3': 2,
            '4': 2,
            '5': 1,
            '6': 1,
        }
    },
    '32': {
        'number_of_rounds': 8,
        'matches_per_round': {
            '1': 8,
            '2': 8,
            '3': 4,
            '4': 4,
            '5': 2,
            '6': 2,
            '7': 1,
            '8': 1,
        }
    },
    '64': {
        'number_of_rounds': 10,
        'matches_per_round': {
            '1': 16,
            '2': 16,
            '3': 8,
            '4': 8,
            '5': 4,
            '6': 4,
            '7': 2,
            '8': 2,
            '9': 1,
            '10': 1,
        }
    },
}
