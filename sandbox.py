import traceback

class Coordinates:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_with_direction(self, direction):
        x_shift, y_shift = {'D': (0, -1), 'U': (0, 1), 'R': (1, 0), 'L': (-1, 0)}[direction]
        self.x += x_shift
        self.y += y_shift

    def move_to_be_adjacent(self, other):
        import math

        if abs(self.x - other.x) == 2:
            self.x = self.x + 1 if other.x > self.x else self.x - 1
            self.y = self.y + math.ceil((self.y + other.y) / 2)
        if abs(self.y - other.y) == 2:
            self.x = self.x + math.ceil((self.x + other.x) / 2)
            self.y = self.y + 1 if other.y > self.y else self.y - 1

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"({self.x}, {self.y})"


try:
    head = Coordinates(2,2)
    tail = Coordinates(0,0)

    tail.move_to_be_adjacent(head)
    assert tail.x == 1 and tail.y == 1

    head = Coordinates(2,1)
    tail = Coordinates(0,0)

    tail.move_to_be_adjacent(head)
    assert tail.x == 1 and tail.y == 1


    head = Coordinates(0,2)
    tail = Coordinates(0,0)

    tail.move_to_be_adjacent(head)
    assert tail.x == 0 and tail.y == 1


    head = Coordinates(2,0)
    tail = Coordinates(0,0)

    tail.move_to_be_adjacent(head)
    assert tail.x == 1 and tail.y == 0
except AssertionError:
    traceback.print_exc()
    print(tail)