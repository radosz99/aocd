def a(input):
    val = {"2": "2", "1": "1", "0": "0", "-": "-1", "=": "-2", "3": "=", "4": "-", "5": "0"}
    s = sum([pow(5, index) * int(val[ch]) for line in input.splitlines() for index, ch in enumerate(line[::-1])])
    output = ""
    rest = 0
    while s != 0 or rest:
        remainder = s % 5 + rest
        rest = 0 if remainder <= 2 else 1
        output = val[str(remainder)] + output
        s //= 5
    return output

