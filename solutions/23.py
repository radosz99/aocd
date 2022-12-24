class Elf:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def check_if_no_elf_in_coordinates(coordinates_to_check, elves):
    return all((elf.x, elf.y) not in coordinates_to_check for elf in elves)

def get_destination_proposition(round_number, elves, elf):
    directions = ['N', 'S', 'W', 'E'] * 2
    x, y = elf.x, elf.y

    coordinates_to_check = [(x, y+1), (x, y-1), (x-1, y), (x+1,y), (x-1,y-1), (x-1,y+1), (x+1,y+1),(x+1,y-1)]
    if check_if_no_elf_in_coordinates(coordinates_to_check, elves):
        return None, None

    for direction in directions[round_number % 4: round_number % 4 + 4]:
        if direction == 'N' and check_if_no_elf_in_coordinates([(x-1, y-1), (x-1, y), (x-1, y+1)], elves):
            return x - 1, y
        elif direction == 'S' and check_if_no_elf_in_coordinates([(x+1, y-1), (x+1, y), (x+1, y+1)], elves):
            return x + 1, y
        elif direction == 'W' and check_if_no_elf_in_coordinates([(x+1, y-1), (x, y-1), (x-1, y-1)], elves):
            return x, y - 1
        elif direction == 'E' and check_if_no_elf_in_coordinates([(x+1, y+1), (x, y+1), (x-1, y+1)], elves):
            return x, y + 1
    return x, y

def run(input, b=False, rounds=10):
    rounds = rounds
    elves = [Elf(row_index, col_index) for row_index, row in enumerate([[*line] for line in input.splitlines()]) for col_index, item in enumerate(row) if item == '#']
    for i in range(rounds):
        proposition_list = [get_destination_proposition(i, elves, elf) for elf in elves]
        if b and all([proposition == (None, None) for proposition in proposition_list]):
            return i + 1
        for index, elf in enumerate(elves):
            prop_x, prop_y = proposition_list[index]
            if prop_x is not None and prop_y is not None and proposition_list.count((prop_x, prop_y)) == 1:
                elf.x, elf.y = prop_x, prop_y
    xs, ys = [elf.x for elf in elves], [elf.y for elf in elves]
    return (max(xs) - min(xs)+1) * (max(ys)-min(ys)+1) - len(elves)

def a(input):
    return run(input)

def b(input):
    return run(input, b=True, rounds=10000)