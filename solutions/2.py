second = ".XYZ"

points = {
    'XA': 3,
    'YB': 3,
    'ZC': 3,
    'XC': 6,
    'XB': 0,
    'YA': 6,
    'YC': 0,
    'ZA': 0,
    'ZB': 6
}


def get_points_from_expect_move(expectation, someone):
    if expectation == 'X':
        expected_value = 0
    elif expectation == 'Y':
        expected_value = 3
    else:
        expected_value = 6

    for key, value in points.items():
        if key[1] == someone and value == expected_value:
            return value + second.index(key[0])


def get_score(me, someone):
    return points[f"{me}{someone}"] + second.index(me)


def a(input):
    score = 0
    for game_round in input:
        someone_move, my_move = game_round.split()
        score += get_score(my_move, someone_move)
    return score


def b(input):
    score = 0
    for game_round in input:
        someone_move, my_move = game_round.split()
        score += get_points_from_expect_move(my_move, someone_move)
    return score