def a(input):
    s = 0
    for line in input.splitlines():
        for index, ch in enumerate(line[::-1]):
            s += pow(5, index) * {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}[ch]

    output = ""
    rest = 0
    while s != 0 or rest:
        remainder = s % 5 + rest
        rest = 0
        if remainder > 2:
            rest = 1
        output = {0: "0", 1: "1", 2: "2", 3: "=", 4: "-", 5: "0"}[remainder] + output
        s //= 5
    return output

