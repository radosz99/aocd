import re
from math import prod

get_numbers = lambda a: list(map(int, re.findall('\d+', a)))

class Monkey:
    def __init__(self, input, divider):
        self.items = get_numbers(input[1])
        self.operation = input[2].split('= ')[-1]
        self.test = get_numbers(input[3])[0]
        self.true_monkey = get_numbers(input[4])[0]
        self.false_monkey = get_numbers(input[5])[0]
        self.inspection_number = 0
        self.divider = divider

    def proceed_with_items(self, monkeys, modulo):
        for item in self.items:
            worry_level = eval(self.operation, {"old": item}) % modulo
            worry_level = worry_level // self.divider
            monkeys[self.true_monkey if worry_level % self.test == 0 else self.false_monkey].items.append(worry_level)
            self.inspection_number += 1
        self.items.clear()


def solve(input, rounds, divider):
    monkeys = [Monkey(monkey.split('\n'), divider=divider) for monkey in input.split("\n\n")]
    modulo = prod(monkey.test for monkey in monkeys)
    [[monkey.proceed_with_items(monkeys, modulo) for monkey in monkeys] for _ in range(rounds)]
    inspections = sorted([monkey.inspection_number for monkey in monkeys], reverse=True)
    return inspections[0] * inspections[1]


def a(input):
    return solve(input, 20, 3)


def b(input):
    return solve(input, 10000, 1)