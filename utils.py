def get_bracket_size(num_players) -> int:
    bracket_size = 0
    power_of_2 = 0
    while bracket_size < num_players:
        power_of_2 += 1
        bracket_size = pow(2, power_of_2)

    return bracket_size


def loser_configuration(num_players):
    if num_players < 4:
        raise ValueError("Number of players must be greater than or equal to 4.")

    bracket_size = get_bracket_size(num_players)
    match bracket_size:
        case 4:
            number_of_rounds = 2
        case 8:
            number_of_rounds = 4
        case 16:
            number_of_rounds = 6
        case 32:
            number_of_rounds = 8
        case 64:
            number_of_rounds = 10
        case _:
            number_of_rounds = 0

    config = {
        'rounds': number_of_rounds
    }

    matches_per_round = {}
    matches_in_round = bracket_size / 4
    for loser_round in range(1, config['rounds']):
        if loser_round == 1:
            matches_in_round = bracket_size / 4
        else:
            if loser_round % 2 != 0:
                matches_in_round = matches_in_round / 2
        matches_per_round[loser_round] = matches_in_round

    config['matches_per_round'] = matches_per_round
    return config