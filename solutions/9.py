class Coordinates:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_to_become_neighbor(self, other):
        if abs(self.x - other.x) == 2 or abs(self.y - other.y) == 2:
            self.x += (0 if self.x == other.x else (other.x - self.x) // abs(other.x - self.x))
            self.y += (0 if self.y == other.y else (other.y - self.y) // abs(other.y - self.y))


def solve(size, input):
    knots = [Coordinates() for _ in range(size)]
    tail_coordinates_set = set()
    for direction, number in [row.split() for row in input.splitlines()]:
        for _ in range(int(number)):
            x_shift, y_shift = {'D': (0, -1), 'U': (0, 1), 'R': (1, 0), 'L': (-1, 0)}[direction]
            knots[0].x += x_shift
            knots[0].y += y_shift
            for index, knot in enumerate(knots[1:size], start=1):
                knot.move_to_become_neighbor(knots[index - 1])
            tail_coordinates_set.add((knots[size - 1].x, knots[size - 1].y))
    return len(tail_coordinates_set)


def a(input):
    return solve(2, input)

def b(input):
    return solve(10, input)

