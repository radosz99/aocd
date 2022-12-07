import re

def a(input):
    containers = []
    content, moves = input.split('\n\n')
    content = content.split('\n')[:-1]
    content.reverse()
    for line in content:
        for index, column in enumerate(line[1::4]):
            if len(containers) == index:
                containers.append([])
            if column != " ":
                containers[index].append(column)

    for move in moves.split('\n'):
        which, source, destination = map(int, re.findall('\d+', move))
        for _ in range(which):
            containers[destination-1].append(containers[source - 1].pop())
    result = "".join([container[0] for container in containers])
    print(result)
    return "".join([container[0] for container in containers])


def b(input):
    containers = []
    data, moves = input.split('\n\n')
    extra_data = []
    for line in data.split('\n'):
        numbers = list(map(int, re.findall('\d+', line)))
        if numbers:
            for _ in numbers:
                containers.append([])
        else:
            extra_data.append(line)

    for index, line in enumerate(extra_data):
        data = line[1::4]
        for index, column in enumerate(data):
            if column != " ":
                containers[index].append(column)

    for move in moves.split('\n'):
        which, source, destination = map(int, re.findall('\d+', move))
        letters = containers[source-1][0:which]
        for index, letter in enumerate(letters):
            del containers[source-1][0]
            containers[destination-1].insert(index, letter)
    result = ""
    for container in containers:
        result+=container[0]
    return result

