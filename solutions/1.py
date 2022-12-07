def a(input):
    most = 0
    iterator = iter(input)
    while True:
        current = 0
        try:
            line = next(iterator)
            while line:
                current += int(line)
                line = next(iterator)
            most = current if current > most else most
        except StopIteration:
            break
    return most



def b(input):
    a = [sum(int(i) for i in x.split()) for x in input.split("\n\n")]
    ans = max(a)
    a.remove(max(a))
    ans += max(a)
    a.remove(max(a))
    ans += max(a)
    return ans