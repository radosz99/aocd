class Elf:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def get_destination_proposition(round_number, grid, elf):
    directions = ['N', 'S', 'W', 'E'] * 2
    x, y = elf.x, elf.y

    if '#' not in [grid[x][y + 1], grid[x - 1][y], grid[x + 1][y], grid[x - 1][y - 1], grid[x - 1][y + 1],
                   grid[x][y - 1], grid[x + 1][y - 1], grid[x + 1][y + 1]]:
        return -1, -1

    for direction in directions[round_number % 4: round_number % 4 + 4]:
        if direction == 'N' and '#'not in [grid[x-1][y-1], grid[x-1][y], grid[x-1][y+1]]:
            return x - 1, y
        elif direction == 'S' and '#'not in [grid[x+1][y-1], grid[x+1][y], grid[x+1][y+1]]:
            return x + 1, y
        elif direction == 'W' and '#'not in [grid[x+1][y-1], grid[x][y-1], grid[x-1][y-1]]:
            return x, y - 1
        elif direction == 'E' and '#'not in [grid[x+1][y+1], grid[x][y+1], grid[x-1][y+1]]:
            return x, y + 1
    return x, y

def a(input):
    n = 1000
    rounds = 10
    grid = [(['.'] * n) + [*line] + (['.'] * n) for line in input.splitlines()]
    grid = [['.'] * len(grid[0]) for _ in range(n)] + grid + [['.'] * len(grid[0]) for _ in range(n)]

    elves = []
    for i, row in enumerate(grid):
        elves.extend([Elf(i, index) for index, elem in enumerate(row) if elem == '#'])

    for i in range(rounds):
        proposition_list = [get_destination_proposition(i, grid, elf) for elf in elves]
        # if all([proposition == (-1, -1) for proposition in proposition_list]):
        #     return i + 1
        for index, elf in enumerate(elves):
            prop_x, prop_y = proposition_list[index]
            if prop_x >= 0 and prop_y >= 0 and proposition_list.count((prop_x, prop_y)) == 1:
                grid[elf.x][elf.y] = '.'
                elf.x, elf.y = prop_x, prop_y
                grid[elf.x][elf.y] = '#'
    xs, ys = [elf.x for elf in elves], [elf.y for elf in elves]
    new_grid = [row[min(ys):max(ys)+1] for row in grid[min(xs):max(xs)+1]]
    return [item for sublist in new_grid for item in sublist].count('.')


