import numpy as np


def part1():
    with open('Day15.txt') as file:
        risk = file.read().splitlines()
    risk_matrix = np.array([[int(i) for i in r] for r in risk])
    max_x, max_y = risk_matrix.shape
    origin = (0, 0)
    goal = (max_x-1, max_y-1)
    distance_matrix = Dijkstra(risk_matrix, max_x, max_y, origin, goal)
    print(distance_matrix)


def part2():
    with open('Day15.txt') as file:
        risk = file.read().splitlines()
    risk_matrix = np.array([[int(i) for i in r] for r in risk])
    risk_matrix = expand_map(risk_matrix)
    max_x, max_y = risk_matrix.shape
    origin = (0, 0)
    goal = (max_x-1, max_y-1)
    distance_matrix = Dijkstra(risk_matrix, max_x, max_y, origin, goal)
    print(distance_matrix)


def Dijkstra(risk_matrix, max_x, max_y, origin, goal):
    visited_matrix = np.zeros(risk_matrix.shape, dtype=bool)
    lowest_risk_matrix = np.full(risk_matrix.shape, np.inf, dtype=float)
    lowest_risk_matrix[origin] = 0

    current_position = origin

    while not visited_matrix[goal]:
        if not visited_matrix[current_position]:
            possible_positions = get_possible_destinations(max_x, max_y, current_position)
            for pos in possible_positions:
                risk = risk_matrix[pos]
                if lowest_risk_matrix[current_position] + risk < lowest_risk_matrix[pos]:
                    lowest_risk_matrix[pos] = lowest_risk_matrix[current_position] + risk
            visited_matrix[current_position] = True
            print(visited_matrix)
        nodes_min_d = np.where(
            np.logical_and(lowest_risk_matrix == np.amin(lowest_risk_matrix[np.invert(visited_matrix)]),
                           np.invert(visited_matrix))
        )
        current_position = (nodes_min_d[0][0], nodes_min_d[1][0])

        if current_position == goal:
            return lowest_risk_matrix[goal]
    return lowest_risk_matrix[goal]


def get_possible_destinations(max_x, max_y, current_position):
    possible_destinations = []
    x_position, y_position = current_position
    if x_position > 0:
        possible_destinations.append((x_position-1, y_position))
    if x_position < max_x-1:
        possible_destinations.append((x_position+1, y_position))
    if y_position > 0:
        possible_destinations.append((x_position, y_position-1))
    if y_position < max_y-1:
        possible_destinations.append((x_position, y_position+1))

    return possible_destinations


def expand_map(og_map):
    old = np.copy(og_map)
    result = np.copy(og_map)
    for i in range(4):
        new_cols = old + np.ones(og_map.shape, dtype=int)
        new_cols = np.where(new_cols > 9, 1, new_cols)
        result = np.c_[result, new_cols]
        old = result[:, -og_map.shape[0]:]
    old = result
    for i in range(4):
        new_cols = old + np.ones((og_map.shape[0], og_map.shape[1] * 5), dtype=int)
        new_cols = np.where(new_cols > 9, 1, new_cols)
        result = np.r_[result, new_cols]
        old = result[-og_map.shape[0]:, :]
    return (result)


if __name__ == "__main__":
    part2()
