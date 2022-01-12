import numpy as np


def part1():
    with open('Day9.txt') as file:
        heights = file.read().splitlines()
    heights_matrix = np.array([[int(i) for i in r] for r in heights])
    print(heights_matrix)
    max_x, max_y = heights_matrix.shape
    visited_matrix = np.zeros(heights_matrix.shape, dtype=bool)
    print(visited_matrix)

    low_points = []
    low_points_positions = []

    for i in range(0, max_x):
        for j in range(0, max_y):
            adjacentes = get_adjacents(max_x, max_y, (i, j))
            low = True
            print("new:", heights_matrix[(i, j)])

            for adj in adjacentes:
                print(heights_matrix[adj])
                if heights_matrix[(i, j)] >= heights_matrix[adj]:
                    low = False
                    break
            if low:
                print("Its low")
                low_points.append(heights_matrix[(i, j)])
                low_points_positions.append((i, j))
                print(low_points)
            # if not visited_matrix[(i, j)]:
            #     adjacentes = get_adjacents(max_x, max_y, (i, j))
            #     for adj in adjacentes:
            #         if heights_matrix[(i, j)] > heights_matrix[adj]:
            #             visited_matrix[(i, j)] = True
            #         else:
            #             heights_matrix[adj] = True
            #
            #     if not visited_matrix[(i, j)]:
            #         low_points.append(heights_matrix[(i, j)])

    print(low_points)
    total = sum(low_points) + len(low_points)
    print("Solution", total)

    basins_sizes = []
    for position in low_points_positions:
        basins_sizes.append(calculate_basin_size(position, heights_matrix, visited_matrix, max_x, max_y))

    basins_sizes.sort(reverse=True)
    print(basins_sizes)
    print(basins_sizes[0])
    print(basins_sizes[1])
    print(basins_sizes[2])
    print("Solution:", basins_sizes[0] * basins_sizes[1] * basins_sizes[2] )


def calculate_basin_size(position, heights_matrix, visited_matrix, max_x, max_y):
    if visited_matrix[position]:
        return 0
    else:
        visited_matrix[position] = True
        size = 1
        adjacets = get_adjacents_not_visited(max_x, max_y, position, visited_matrix)
        size += count_adjacents(adjacets, visited_matrix, heights_matrix, max_x, max_y)
    return size


def count_adjacents(adjacents, visited_matrix, height_matrix, max_x, max_y):
    size = 0
    for adj in adjacents:
        if not visited_matrix[adj]:
            visited_matrix[adj] = True
            if height_matrix[adj] != 9:
                size += 1
                adj_adj = get_adjacents_not_visited(max_x, max_y, adj, visited_matrix)
                if len(adj_adj) > 0:
                    size += count_adjacents(adj_adj, visited_matrix, height_matrix, max_x, max_y)
    return size


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

    return adjacents


def get_adjacents_not_visited(max_x, max_y, current_position, visited_matrix):
    adjacents = []
    x_position, y_position = current_position
    if x_position > 0 and not visited_matrix[(x_position-1, y_position)]:
        adjacents.append((x_position-1, y_position))
    if x_position < max_x-1 and not visited_matrix[(x_position+1, y_position)]:
        adjacents.append((x_position+1, y_position))
    if y_position > 0 and not visited_matrix[(x_position, y_position-1)]:
        adjacents.append((x_position, y_position-1))
    if y_position < max_y-1 and not visited_matrix[(x_position, y_position+1)]:
        adjacents.append((x_position, y_position+1))

    return adjacents


if __name__ == "__main__":
    part1()
