from contextlib import suppress
import re

get_numbers = lambda a: iter(map(int, (int(z[1:]) for z in re.findall(r'=-?\d+', a))))


def a(input):
    row = 2000000
    not_allowed_rows = set()
    beacons = set()
    for line in input.splitlines():
        numbers = get_numbers(line)

        sensor = (next(numbers), next(numbers))
        closest_beacon = (next(numbers), next(numbers))
        beacons.add(closest_beacon)

        manhattan_distance = abs(sensor[0] - closest_beacon[0]) + abs(sensor[1] - closest_beacon[1])
        occupied_in_row = manhattan_distance - abs(row - sensor[1])
        for x in range(sensor[0] - occupied_in_row,
                       sensor[0] + occupied_in_row + 1):
            not_allowed_rows.add((x, row))
    for beacon in beacons:
        with suppress(KeyError):
            not_allowed_rows.remove(beacon)
    return len(not_allowed_rows)


def get_overlapped_range(range1, range2):
    start1, end1 = range1
    start2, end2 = range2
    return (max(start1, start2), min(end1, end2)) if (start1 <= end2) and (start2 <= end1) else None


def rotate_coordinates_45(x, y):
    return -x + y, x + y


def undo_rotate_coordinates_45(x, y):
    return (x - y) / - 2, (x + y) / 2


class Sensor:
    def __init__(self, sensor, distance):
        self.converted_right_top = rotate_coordinates_45(sensor[0] - distance, sensor[1])
        self.converted_left_down = rotate_coordinates_45(sensor[0] + distance, sensor[1])
        self.converted_left_top = rotate_coordinates_45(sensor[0], sensor[1] - distance)
        self.converted_right_down = rotate_coordinates_45(sensor[0], sensor[1] + distance)
        self.sensor = sensor
        self.distance = distance

    def get_coordinates_candidates(self, other):
        # checking if distance between opposite edges in two Sensor instances = 2

        # self top to other bottom
        if self.converted_left_top[1] - 2 == other.converted_left_down[1]:
            if overlap := get_overlapped_range(
                    (self.converted_left_top[0], self.converted_right_top[0]),
                    (other.converted_left_down[0], other.converted_right_down[0])):
                return [(i, self.converted_left_top[1] - 1) for i in range(overlap[0], overlap[1])]

        # self down to other top
        elif self.converted_left_down[1] + 2 == other.converted_left_top[1]:
            if overlap := get_overlapped_range(
                    (self.converted_left_down[0], self.converted_right_down[0]),
                    (other.converted_left_top[0], other.converted_right_top[0])):
                return [(i, self.converted_left_down[1] + 1) for i in range(overlap[0], overlap[1])]

        # self left to other right
        elif self.converted_left_down[0] - 2 == other.converted_right_down[0]:
            if overlap := get_overlapped_range(
                    (self.converted_left_top[1], self.converted_left_down[1]),
                    (other.converted_right_top[1], other.converted_right_down[1])):
                return [(self.converted_left_down[1] - 1, i) for i in range(overlap[0], overlap[1])]

        # self right to other left
        elif self.converted_right_down[0] + 2 == other.converted_left_down[0]:
            if overlap := get_overlapped_range(
                    (self.converted_right_top[1], self.converted_right_down[1]),
                    (other.converted_left_top[1], other.converted_left_down[1])):
                return [(self.converted_right_down[1] + 1, i) for i in range(overlap[0], overlap[1])]
        return []

    def outside_sensor_range(self, x, y):
        if abs(self.sensor[0] - x) + abs(self.sensor[1] - y) > self.distance:
            return True


def b(input):
    sensors = []

    for line in input.splitlines():
        numbers = get_numbers(line)
        sensor = (next(numbers), next(numbers))
        closest_beacon = (next(numbers), next(numbers))
        manhattan_distance = abs(sensor[0] - closest_beacon[0]) + abs(sensor[1] - closest_beacon[1])
        sensors.append(Sensor(sensor, manhattan_distance))

    candidates = []
    for sensor in sensors:
        for sensor_2 in sensors:
            candidates.extend(sensor.get_coordinates_candidates(sensor_2))
    candidates = [undo_rotate_coordinates_45(x, y) for x, y in candidates]
    candidates = [(int(x), int(y)) for x, y in candidates if x.is_integer() and y.is_integer() and x >= 0 and y >= 0]
    candidates = list(set(candidates))
    for x, y in candidates:
        if all([sensor.outside_sensor_range(x, y) for sensor in sensors]):
            return x * 4000000 + y
