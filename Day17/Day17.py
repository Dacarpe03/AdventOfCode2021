
def part2():
    x_min = 20
    x_max = 30
    y_max = -5
    y_min = -10

    targeted_points = set()
    for i in range(x_min, x_max+1):
        for j in range(y_min, y_max+1):
            x_speeds, found_x = get_initial_speeds(i)
            print(i, j)
            print(x_speeds)
            # y_speeds, found_y = get_initial_speeds(j)

    print(targeted_points)
    print(len(targeted_points))


def get_initial_speeds(final_position):
    found = False
    # print("Final position", final_position)
    initial_speeds = []
    n = 1
    while n < final_position:
        initial_speed = final_position/n + n*(n-1)/2
        if initial_speed.is_integer():
            initial_speeds.append([int(initial_speed), n])
            found = True
        n += 1
    return initial_speeds, found


def match(x_step, y_step):
    if x_step > y_step:
        return False
    else:
        return True


if __name__ == "__main__":
    part2()