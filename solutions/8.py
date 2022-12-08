def find_horizontal(items, columns=False):
    lst = []
    for row_index, row in enumerate(items[1:-1], start=1):
        for col_index, tree in enumerate(row[1:-1], start=1):
            tree_coordinates = (col_index, row_index) if columns else (row_index, col_index)
            if all([int(character) < int(tree) for character in row[:col_index]]) or all([int(character) < int(tree) for character in row[col_index+1:]]):
                lst.append(tree_coordinates)
    return lst


def a(input):
    rows = input.splitlines()
    size = len(rows)
    columns = [([rows[y][x] for y in range(size)]) for x in range(size)]
    return len(set(find_horizontal(rows) + find_horizontal(columns, columns=True))) + (size-1) * 4


def get_number_of_visible(trees_list, tree):
    counter = 0
    for index, item in enumerate(trees_list):
        if all([int(character) < int(tree) for character in trees_list[:index]]):
            counter = index + 1
        else:
            break
    return counter


def get_visible_horizontally_multiplied(items, columns=False):
    dct = {}
    for row_index, row in enumerate(items):
        for col_index, tree in enumerate(row):
            dct[(col_index, row_index) if columns else (row_index, col_index)] = get_number_of_visible(row[:col_index][::-1], tree) * get_number_of_visible(row[col_index+1:], tree)
    return dct


def b(input):
    rows = [x for x in input.splitlines()]
    size = len(rows)
    columns = [([rows[y][x] for y in range(size)]) for x in range(size)]
    visible_in_row = get_visible_horizontally_multiplied(rows)
    visible_in_column = get_visible_horizontally_multiplied(columns, columns=True)
    return max(visible_in_row[key] * visible_in_column[key] for key, value in visible_in_row.items())