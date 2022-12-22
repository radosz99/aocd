def compare(left, right):
    # <0 if left > right, >0 if right>left, 0 if right=left
    if not isinstance(left, list) and not isinstance(right, list):
        return left - right
    else:
        left = [left] if not isinstance(left, list) else left
        right = [right] if not isinstance(right, list) else right
        for l, r in zip(left, right):
            if (result := compare(l, r)) != 0:
                return result
        return len(left) - len(right)  # one of lists has been exhausted


def bubble_sort(array):
    n = len(array)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if compare(array[j+1], array[j]) < 0:
                swapped = True
                array[j], array[j+1] = array[j+1], array[j]
        if not swapped:
            return


def a(input):
    score = 0
    for index, pair in enumerate(input.split('\n\n'), start=1):
        score += index if compare(*[eval(item) for item in pair.splitlines()]) < 0 else 0
    return score


def b(input):
    dividers = [[[2]], [[6]]]
    packets = [eval(packet) for packet in input.splitlines() if packet] + dividers
    bubble_sort(packets)
    return (packets.index(dividers[0]) + 1) * (packets.index(dividers[1]) + 1)