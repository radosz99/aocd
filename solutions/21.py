from sympy import sympify, solve
import contextlib


class Monkey:
    def __init__(self, function, name=""):
        self.name = name
        self.function = function
        self.monkey_1, self.monkey_2 = (function[0:4], function[7:11]) if not function.isdigit() else (None, None)
        self.number = int(function) if function.isdigit() else None
        self.first_value, self.second_value = None, None

    def get_number(self, monkeys):
        if self.name == 'humn':
            return None
        return self.evaluate(monkeys) if not self.number else self.number

    def get_monkey_without_calculated_number(self):
        return self.monkey_1 if not self.first_value else self.monkey_2

    def evaluate(self, monkeys):
        self.first_value = monkeys[self.monkey_1].get_number(monkeys)
        self.second_value = monkeys[self.monkey_2].get_number(monkeys)
        return int(eval(self.function, {self.monkey_1: self.first_value, self.monkey_2: self.second_value})) if (self.first_value and self.second_value) else None

    def solve_equation(self, score):
        eq = self.function.replace(str(self.monkey_1), str(self.first_value).lower())
        eq = eq.replace(str(self.monkey_2), str(self.second_value).lower())
        return solve(sympify(f"Eq({eq.replace(' ', '')},{score})"))[0]


def a(input):
    monkeys = {name: Monkey(function) for name, function in [line.split(': ') for line in input.splitlines()]}
    return monkeys['root'].get_number(monkeys)


def b(input):
    monkeys = {name: Monkey(function, name) for name, function in [line.split(': ') for line in input.splitlines()]}
    monkeys['root'].get_number(monkeys)

    current_monkey = 'root'
    expected_number = monkeys[current_monkey].first_value or monkeys[current_monkey].second_value
    try:
        while True:
            current_monkey = monkeys[current_monkey].get_monkey_without_calculated_number()
            expected_number = monkeys[current_monkey].solve_equation(expected_number)
    except IndexError:
        return expected_number

