import sys
import importlib.util

from aocd import get_data
from aocd import submit

import test_data_fetcher
from exceptions import AOCDException


def get_solve_part_function(module_name, function_name):
    try:
        spec = importlib.util.spec_from_file_location(f"solutions.{module_name}", f"solutions/{module_name}.py")
        foo = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = foo
        spec.loader.exec_module(foo)
        return getattr(foo, function_name)
    except Exception as err:
        raise AOCDException(f"Error has occurred = {str(err)}")

# export AOC_SESSION=53616c7465645f5fc3ecf4c6b03a5a3e97e6c6017c64c47f0aed7a0db5074830d3ef907a0307afea8c093acf21ddd66dcf8279e6158a46c91bee3c4ce39daeef


day = test_data_fetcher.get_current_day_of_month_in_aocd_timezone()
official_input = get_data(day=day, year=2022)
test_input, test_answer = test_data_fetcher.get_test_data_from_part_a(day, parse_to_list=False)
try:
    test_answer = int(test_answer)
except ValueError:
    pass

part = 'b'
solve_func = get_solve_part_function(day, part)
answer = solve_func(test_input)

if test_answer == answer:
    print("Gicior")
    a_answer = solve_func(official_input)
    submit(a_answer, part=part, day=day, year=2022)
else:
    print(f"Should be {test_answer}, but currently it is {answer}, improve solution!")