import numpy as np


def part1():
    with open('Day11.txt') as file:
        energies = file.read().splitlines()
    energy_matrix = np.array([[int(i) for i in r] for r in energies])
    max_x, max_y = energy_matrix.shape
    visited_matrix = np.zeros(energy_matrix.shape, dtype=bool)
    flashes = 0
    for step in range(100):
        print("Step", step+1)
        for i in range(max_x):
            for j in range(max_y):
                position = (i, j)
                flashes += count_flashes(energy_matrix, visited_matrix, position, max_x, max_y)
        energy_matrix = np.where(energy_matrix > 9, 0, energy_matrix)
        visited_matrix = np.zeros(energy_matrix.shape, dtype=bool)
        print(energy_matrix)
    print(flashes)


def part2():
    with open('Day11.txt') as file:
        energies = file.read().splitlines()
    energy_matrix = np.array([[int(i) for i in r] for r in energies])
    max_x, max_y = energy_matrix.shape
    visited_matrix = np.zeros(energy_matrix.shape, dtype=bool)
    flashes = 0
    step = 0
    while not check_all_flashed(visited_matrix):
        visited_matrix = np.zeros(energy_matrix.shape, dtype=bool)
        print("Step", step+1)
        for i in range(max_x):
            for j in range(max_y):
                position = (i, j)
                flashes += count_flashes(energy_matrix, visited_matrix, position, max_x, max_y)
        energy_matrix = np.where(energy_matrix > 9, 0, energy_matrix)
        print(energy_matrix)
        step += 1
    print(step)


def count_flashes(energy_matrix, flashed_matrix, position, max_x, max_y):
    flashes = 0
    energy_matrix[position] += 1
    if energy_matrix[position] > 9:
        if not flashed_matrix[position]:
            print("Flash at", position)
            flashed_matrix[position] = True
            flashes += 1
            adjacents = get_adjacents(max_x, max_y, position)
            for adj in adjacents:
                flashes += count_flashes(energy_matrix, flashed_matrix, adj, max_x, max_y)
    return flashes


def check_all_flashed(flashed_matrix):
    rows, cols = flashed_matrix.shape
    for i in range(rows):
        for j in range(cols):
            if not flashed_matrix[(i, j)]:
                return False
    return True


def get_adjacents(max_x, max_y, current_position):
    adjacents = []
    x_position, y_position = current_position
    if x_position > 0:
        adjacents.append((x_position-1, y_position))
    if x_position < max_x-1:
        adjacents.append((x_position+1, y_position))
    if y_position > 0:
        adjacents.append((x_position, y_position-1))
    if y_position < max_y-1:
        adjacents.append((x_position, y_position+1))

    diag_1 = (x_position-1, y_position-1)
    diag_2 = (x_position-1, y_position+1)
    diag_3 = (x_position+1, y_position-1)
    diag_4 = (x_position+1, y_position+1)

    if in_bounds(max_x, max_y, diag_1):
        adjacents.append(diag_1)
    if in_bounds(max_x, max_y, diag_2):
        adjacents.append(diag_2)
    if in_bounds(max_x, max_y, diag_3):
        adjacents.append(diag_3)
    if in_bounds(max_x, max_y, diag_4):
        adjacents.append(diag_4)

    return adjacents


def in_bounds(max_x, max_y, pos):
    x, y = pos
    if max_x > x >= 0 and max_y > y >= 0:
        return True


if __name__ == "__main__":
    part2()
