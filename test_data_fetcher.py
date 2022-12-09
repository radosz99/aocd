from datetime import datetime, timedelta
import os

import requests
from bs4 import BeautifulSoup

from exceptions import AOCDException


def get_time_in_aocd_timezone():
    return datetime.now() - timedelta(hours=6)


def get_current_day_of_month_in_aocd_timezone():
    now = get_time_in_aocd_timezone()
    return int(now.day)


def fetch_test_data(day, year=2022):
    if day > get_current_day_of_month_in_aocd_timezone():
        raise AOCDException(f"Day {day} is in the future in timezone UTC-5! = {get_time_in_aocd_timezone()}")

    page = requests.get(f"https://adventofcode.com/{year}/day/{day}")
    soup = BeautifulSoup(page.content, "html.parser")

    test_answer, test_input = None, None
    for item in soup.find_all("code"):
        if '\n' in item.text:
            test_input = item.text.split('\n')
        try:
            test_answer = int(item.text)
        except ValueError:
            pass

    if not test_answer or not test_input:
        raise AOCDException("Tests have to be skipped, unknown error has occurred")
    return test_input, test_answer


def save_test_data(day=None):
    day = get_current_day_of_month_in_aocd_timezone() if not day else day
    test_dir = f"test_inputs/{day}"
    input, answer = fetch_test_data(day)
    try:
        os.mkdir(test_dir)
    except FileExistsError:
        pass
    with open(f"{test_dir}/input.txt", "w") as f:
        f.write('\n'.join(input))
    with open(f"{test_dir}/answer.txt", "w") as f:
        f.writelines(str(answer))


def get_test_data_from_part_a(day=None, parse_to_list=True):
    day = get_current_day_of_month_in_aocd_timezone() if not day else day
    test_dir = f"test_inputs/{day}"

    if not os.path.exists(f"{test_dir}/input.txt"):
        save_test_data(day)

    with open(f"{test_dir}/input.txt") as f:
        if not parse_to_list:
            input = f.read()
        else:
            input = [line.rstrip() for line in f.readlines()]
    with open(f"{test_dir}/answer.txt") as f:
        answer = f.readline()
    return input, answer