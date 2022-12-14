class DestinationHasBeenFoundError(Exception):
    pass

def get_letter_from_grid(x, y, grid):
    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
        return '@', x, y
    else:
        return grid[x][y],x, y

def check_neighbourhood(grid, current, visited):
    x, y = current
    left = get_letter_from_grid(x, y-1, grid)
    right = get_letter_from_grid(x, y+1, grid)
    up = get_letter_from_grid(x - 1, y, grid)
    down = get_letter_from_grid(x + 1, y, grid)
    directions = sorted([left, right, up, down], key=lambda x: x[0], reverse=True)
    # print(directions)
    print(f"Left = {left}, right = {right}, up = {up}, down = {down}")


def a(input):
    grid = [[character for character in line] for line in input.split()]
    visited = [['..' for _ in line] for line in grid]

    current = (0, 0)
    grid[0][0] = 'a'
    visited[0][0] = "00"
    for i in range(100):
        current = check_neighbourhood(grid, current, visited)

