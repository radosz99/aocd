from collections import deque
import re

def run(start, end, grid, minimum=99999):
    w, h = len(grid[0]), len(grid)
    grid[start[0]][start[1]], grid[end[0]][end[1]] = 'a', 'z'
    visited = []
    q = deque()

    q.append((start[0], start[1], 1, ""))
    while q:
        x, y, t, path = q.popleft()
        if t > minimum:
            return None
        if (x, y) in visited:
            continue
        visited.append((x, y))
        for new_x, new_y in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            if 0 <= new_x < h and 0 <= new_y < w and ord(grid[new_x][new_y])-ord(grid[x][y]) <= 1:
                if end == (new_x, new_y):
                    print(path)
                    return t
                q.append((new_x, new_y, t+1, path+grid[new_x][new_y]))
    return None

def a(input):
    grid = []
    end = None
    start = None
    for index, line in enumerate(input.splitlines()):
        if 'E' in line:
            end = index, line.index('E')
        if 'S' in line:
            start = index, line.index('S')
        grid.append([*line])
    return run(start, end, grid)

def b(input):
    grid = []
    a_list = []
    end = None
    for index, line in enumerate(input.splitlines()):
        for a_index in [m.start() for m in re.finditer('a', line)]:
            a_list.append((index, a_index))
        if 'E' in line:
            end = index, line.index('E')
        if 'S' in line:
            a_list.append((index, line.index('S')))
            line.replace('S', 'a')
        grid.append([*line])
    minimum = 999999
    for start in a_list:
        if path_len := run(start, end, grid, minimum):
            minimum = path_len if path_len < minimum else minimum
    return minimum
