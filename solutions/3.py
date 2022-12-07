def score(letter):
    return ord(letter) - ord('a') + 1 if 'a' <= letter <= 'z' else ord(letter) - ord('A') + 27


def a(input):
    sum = 0
    for item in input:
        half = int(len(item) / 2)
        first, second = item[:half], item[half:]
        common = set(first) & set(second)
        sum += score(next(iter(common)))
    return sum


def b(input):
    sum = 0
    for a, b, c in [input[x:x+3] for x in range(0, len(input), 3)]:
        common = set(a) & set(b) & set(c)
        sum += score(next(iter(common)))
    return sum