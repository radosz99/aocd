class Coordinates:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_with_direction(self, direction):
        x_shift, y_shift = {'D': (0, -1), 'U': (0, 1), 'R': (1, 0), 'L': (-1, 0)}[direction]
        self.x += x_shift
        self.y += y_shift

    def move_to_become_neighbor(self, other):
        if abs(self.x - other.x) == 2 and abs(self.y - other.y) == 2:
            self.x = self.x + int((other.x - self.x) / 2)
            self.y = self.y + int((other.y - self.y) / 2)
        elif abs(self.x - other.x) == 2:
            self.x = self.x + int((other.x - self.x) / 2)
            self.y = other.y
        elif abs(self.y - other.y) == 2:
            self.x = other.x
            self.y = self.y + int((other.y - self.y) / 2)


def solve(size, input):
    knots = [Coordinates() for _ in range(size)]
    tail_coordinates_set = set()
    for direction, number in [row.split() for row in input.splitlines()]:
        for _ in range(int(number)):
            knots[0].move_with_direction(direction)
            for index, knot in enumerate(knots[1:size], start=1):
                knot.move_to_become_neighbor(knots[index - 1])
            tail_coordinates_set.add((knots[size - 1].x, knots[size - 1].y))
    return len(tail_coordinates_set)


def a(input):
    return solve(2, input)

def b(input):
    return solve(10, input)

