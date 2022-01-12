def part1():
    min_y_position = -123
    # if min_y_position is -10 the maximum speed possible when getting to point height 0 is -9 then the initial speed must be 9
    # then the maximum height must be sum(9) as it decresases it speeds once per time unit
    max_y_speed = abs(min_y_position) - 1
    max_height = sumatory(max_y_speed)
    print(max_height)


def sumatory(n):
    return n*(n+1)/2


def part2():
    min = 124
    max = 174

    possible_speeds = []
    for speed in range(1, max+1):
        print("Speed:", speed)
        positions, steps = possible_x_positions(speed, min, max)
        print(positions)
        if len(positions) > 0:
            possible_speeds.append([speed, steps])
    print(possible_speeds)

    y_min = -123
    y_max = -86
    y_speeds = []
    for y_speed in range(y_min, abs(y_min)+1):
        y_speed -= 1
        print("Speed", y_speed)
        positions, steps = possible_positions(y_speed, y_min, y_max)
        print(positions)
        if len(positions) > 0:
            y_speeds.append([y_speed, steps])
    print(y_speeds)

    initial_speeds = set()
    count = 0
    for x in possible_speeds:
        x_speed = x[0]
        x_steps = x[1]
        for y in y_speeds:
            y_speed = y[0]
            y_steps = y[1]
            if match(x_speed, x_steps, y_speed, y_steps):
                count += 1
                initial_speeds.add((x_speed, y_speed))

    print(len(initial_speeds), initial_speeds)


def match(x_speed, x_steps, y_speed, y_steps):
    for x_step in x_steps:
        if x_step in y_steps:
            return True
    if x_steps[-1] == x_speed and y_steps[0] > x_steps[-1]:
        return True
    return False


def possible_x_positions(speed, min, max):
    positions = []
    possible_steps = []
    for steps in range(1, speed+1):
        final_pos = steps*speed - steps*(steps-1)/2
        if min <= final_pos <= max:
            positions.append(final_pos)
            possible_steps.append(steps)
    return positions, possible_steps


def possible_positions(speed, min, max):
    positions = []
    possible_steps = []
    for steps in range(1, 1000):
        final_pos = steps*speed - steps*(steps-1)/2
        if min <= final_pos <= max:
            positions.append([final_pos, steps])
            possible_steps.append(steps)
    return positions, possible_steps


def part_0():
    max_x_position = 30
    min_x_position = 20

    min_x_initial_speed = 1

    while not in_x_range(min_x_initial_speed, max_x_position, min_x_position):
        min_x_initial_speed += 1

    max_y_position = -5
    min_y_position = -10

    min_y_initial_speed = -86
    while not in_y_min_range(min_y_initial_speed, min_y_position, min_x_initial_speed):
        min_y_initial_speed += 1
    in_y_min_range(3, min_y_position, min_x_initial_speed)
    max_y_initial_speed = min_y_initial_speed
    while not in_y_max_range(max_y_initial_speed, max_y_position, min_y_position) and max_y_initial_speed < 10:
        max_y_initial_speed += 1

    print(max_y_initial_speed)


def in_x_range(initial_speed, max_x_position, min_x_position):
    steps_to_zero = initial_speed
    n = steps_to_zero - 1
    final_position = calculate_final_x_position(initial_speed, n)
    return max_x_position >= final_position >= min_x_position


def in_y_min_range(initial_speed, min_y_position, steps):
    final_position = calculate_final_y_position(initial_speed, steps)
    print(initial_speed, final_position)
    return final_position >= min_y_position


def in_y_max_range(initial_speed, max_y_position, min_y_position):
    position = 0
    last_position = 0
    speed = initial_speed
    print("Speed", initial_speed)
    while position > max_y_position:
        last_position = position
        position += speed
        print(position, last_position)
        speed -= 1
    print(last_position, min_y_position)
    if last_position >= min_y_position:
        print("Hola")
    else:
        print("pos no")
    return last_position >= min_y_position


def calculate_final_y_position(initial_speed, steps):
    steps_sum = (steps-1) * steps/2
    return steps*initial_speed - steps_sum


def calculate_final_x_position(initial_speed, n):
    n_sumatory = n*(n+1)/2
    return (n+1)*initial_speed - n_sumatory


if __name__ == "__main__":
    part2()
