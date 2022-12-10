def a(input):
    cycle_counter = 1
    signal_value = 1
    total_sum = 0
    for line in input.splitlines():
        cycle_counter += 1
        if "addx" in line:
            if cycle_counter in [20, 60, 100, 140, 180, 220]:
                total_sum += cycle_counter * signal_value
            cycle_counter += 1
            signal_value += int(line.split()[1])
        total_sum += (cycle_counter * signal_value if cycle_counter in [20, 60, 100, 140, 180, 220] else 0)
    return total_sum


def b(input):
    output = []
    cycle_counter = 0
    sprite_positions = [0, 1, 2]
    for line in input.splitlines():
        for x in range(2 if "addx" in line else 1):
            output.append('█' if cycle_counter in sprite_positions else '.')
            cycle_counter = (cycle_counter + 1) % 40
            sprite_positions = [x + int(line.split()[1]) for x in sprite_positions] if x == 1 else sprite_positions
    for row in range(6):
        print(''.join(output[row*40:(row+1)*40]))
    return "ELPLZGZL"