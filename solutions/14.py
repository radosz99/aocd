import re
import numpy

get_numbers = lambda a: list(map(int, re.findall('\d+', a)))


def generate_deltas(diff):
    start, end = sorted(diff)
    return [(0, i) if diff[0] == 0 else (i, 0) for i in range(start, end + 1)]


def draw_rocks(grid, coords, deltas):
    for delta in deltas:
        x, y = tuple(numpy.subtract(coords, delta))
        grid[x][y] = '#'


def draw_path(grid, list_of_coords):
    for counter in range(len(list_of_coords)-1):
        diff = tuple(numpy.subtract(list_of_coords[counter], list_of_coords[counter + 1]))
        draw_rocks(grid, list_of_coords[counter], generate_deltas(diff))


def a(input):
    grid = {}
    lists_of_coords = []
    for line in input.split('\n'):
        numbers = get_numbers(line)
        lists_of_coords.append([(numbers[x], numbers[x+1]) for x in range(0, len(numbers), 2)])
    maxim = max([coords[1] for list_of_coords in lists_of_coords for coords in list_of_coords])
    for coord in range(
            min([coords[0] for list_of_coords in lists_of_coords for coords in list_of_coords]),
            max([coords[0] for list_of_coords in lists_of_coords for coords in list_of_coords])+1):
        grid[coord] = ['.' for _ in range(maxim+1)]

    for list_of_coords in lists_of_coords:
        draw_path(grid, list_of_coords)
    counter = 0

    while True:
        coords = (500, 0)
        while True:
            if coords[0] == list(grid.keys())[0] or coords[1] == len(grid[500])-1:
                return counter
            if grid[coords[0]][coords[1]+1] == '.':
                coords = (coords[0], coords[1]+1)
                continue
            elif grid[coords[0]-1][coords[1]+1] == '.':
                coords = (coords[0]-1, coords[1]+1)
                continue
            elif grid[coords[0]+1][coords[1]+1] == '.':
                coords = (coords[0]+1, coords[1]+1)
                continue
            break
        grid[coords[0]][coords[1]] = 'o'
        counter += 1


def b(input):
    grid = {}
    lists_of_coords = []
    for line in input.split('\n'):
        numbers = get_numbers(line)
        lists_of_coords.append([(numbers[x], numbers[x+1]) for x in range(0, len(numbers), 2)])
    maxim = max([coords[1] for list_of_coords in lists_of_coords for coords in list_of_coords])
    for coord in range(0, 1000):
        grid[coord] = ['.' if counter != maxim + 2 else '#' for counter in range(maxim+3)]

    for list_of_coords in lists_of_coords:
        draw_path(grid, list_of_coords)
    counter = 0
    while True:
        coords = (500, 0)
        while True:
            if grid[coords[0]][coords[1]+1] == '.':
                coords = (coords[0], coords[1]+1)
                continue
            elif grid[coords[0]-1][coords[1]+1] == '.':
                coords = (coords[0]-1, coords[1]+1)
                continue
            elif grid[coords[0]+1][coords[1]+1] == '.':
                coords = (coords[0]+1, coords[1]+1)
                continue
            break
        grid[coords[0]][coords[1]] = 'o'
        counter += 1
        if coords == (500, 0):
            return counter






