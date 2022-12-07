def a(input):
    # lines = input.split('\n')
    n = 14
    items = [None] * n
    for index, letter in enumerate(input):
        for index_l, item in enumerate(items):
            try:
                items[index_l] = items[index_l+1]
            except IndexError:
                items[index_l] = letter
        dist = list(set(items))
        if len(dist) == n and None not in dist:
            return index+1

