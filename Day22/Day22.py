import numpy
import numpy as np


def part1():
    x = np.zeros(100, dtype=bool)
    y = np.zeros(100, dtype=bool)
    z = np.zeros(100, dtype=bool)
    with open("Day22.txt", "r") as file:
        for line in file.readlines():
            line = line.rstrip("\n")
            switch = line.split(" ")[0]
            if switch == "on":
                value = True
            else:
                value = False

            cubes = line.split(" ")[1]

            x_str = cubes.split(',')[0]
            x = update_array(x, x_str, value)
            y_str = cubes.split(',')[1]
            y = update_array(y, y_str, value)
            z_str = cubes.split(',')[2]
            z = update_array(z, z_str, value)

    x_count = 0
    y_count = 0
    z_count = 0
    for i in range(0, 100):
        if x[i]:
            x_count += 1
        if y[i]:
            y_count += 1
        if z[i]:
            z_count += 1
    print(x)
    print(y)
    print(z)
    print(x_count * y_count * z_count)


def update_array(array, info, value):
    ini = int(info.split("=")[1].split("..")[0]) + 50
    if ini < 0:
        ini = 0
    end = int(info.split("=")[1].split("..")[1]) + 50
    if end > 100:
        end = 100
    print(ini, end)
    for i in range(ini, end+1):
        array[i] = value
    return array


if __name__ == "__main__":
    part1()
