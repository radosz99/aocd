def calculate_dirs_size(tree, sizes):
    directory_size = 0
    for key, value in tree.items():
        if isinstance(value, int):
            file_size = value
            directory_size += file_size
        else:
            subdirectory_size, _ = calculate_dirs_size(tree[key], sizes)
            directory_size += subdirectory_size
    sizes.append(directory_size)
    return directory_size, sizes


def get_tree_for_path(tree, path):
    return tree if not path else get_tree_for_path(tree[path[0]], path[1:])


def create_tree(input):
    path, tree = [], {}
    for line in input.split('\n'):
        split = line.split()
        current_tree = get_tree_for_path(tree, path)
        if split[0].isdigit():
            current_tree[split[1]] = int(split[0])
        elif split[1] == "cd":
            if (directory := split[2]) == "..":
                path.pop()
            else:
                current_tree[directory] = {}
                path.append(directory)
    return tree


def a(input):
    tree = create_tree(input)
    _, sizes = calculate_dirs_size(tree, [])
    return sum([size for size in sizes if size < 100000])


def b(input):
    tree = create_tree(input)
    _, sizes = calculate_dirs_size(tree, [])
    return min([size for size in sizes if size > 30000000 - (70000000 - max(sizes))])


