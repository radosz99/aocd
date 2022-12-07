def a(input):
    lines = input.split('\n')
    counter = 0
    for line in lines:
        first, second = line.split(',')
        a, b = map(int, first.split("-"))
        c, d = map(int, second.split("-"))
        if a <= c and d <= b or c <= a and b <= d:
            counter += 1
    return counter


def b(input):
    lines = input.split('\n')
    counter = 0
    for line in lines:
        # a, b, c, d = map(int, re.findall('\d+', line))
        first, second = line.split(',')
        a, b = map(int, first.split("-"))
        c, d = map(int, second.split("-"))
        if c <= a <= d or c <= b <= d or a <= c <= b or a <= d <= b:
            counter += 1
    return counter