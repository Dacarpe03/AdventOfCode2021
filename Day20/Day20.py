import numpy as np


def part1():
    with open("Day20.txt", "r") as file:
        algorithm = file.readline().rstrip("\n")
        file.readline()
        matrix = []
        for line in file.readlines():
            line = line.strip("\n")
            row = []
            for character in line:
                if character == "#":
                    row.append(1)
                else:
                    row.append(0)
            matrix.append(row)

    image = np.array(matrix)
    print(image)
    print_image(image)

    first_border = algorithm[0]
    if first_border == "#":
        first_border = 1
    else:
        first_border = 0
    second_border = algorithm[511]
    if second_border == "#":
        second_border = 1
    else:
        second_border = 0

    image = expand_image(image, 3, 0)
    for i in range(1, 51):
        image = update_image(image, algorithm)
        if i % 2 == 0:
            image = expand_image(image, 3, 0)
        else:
            image = expand_image(image, 3, 1)
        print_image(image)

        count = 0
        for row in range(0, len(image)):
            for column in range(0, len(image)):
                count += image[row][column]
        print(count)


def expand_image(image, n_borders, value):
    rows, columns = image.shape
    for i in range(n_borders):
        if value == 0:
            image = np.c_[image, np.zeros(rows, dtype=int)]
            image = np.c_[np.zeros(rows, dtype=int), image]
        else:
            image = np.c_[image, np.ones(rows, dtype=int)]
            image = np.c_[np.ones(rows, dtype=int), image]

    rows, columns = image.shape
    for i in range(n_borders):
        if value == 0:
            image = np.r_[image, [np.zeros(columns, dtype=int)]]
            image = np.r_[[np.zeros(columns, dtype=int)], image]
        else:
            image = np.r_[image, [np.ones(columns, dtype=int)]]
            image = np.r_[[np.ones(columns, dtype=int)], image]
    return image


def update_image(image, algorithm):
    updated = []
    for i in range(2, len(image)-2):
        row = []
        for j in range(2, len(image)-2):
            row.append(enhance_pixel(image, i, j, algorithm))
        updated.append(row)
    updated = np.array(updated)
    return updated


def enhance_pixel(image, row, column, algorithm):
    binary = ""
    binary += str(image[row-1][column-1])
    binary += str(image[row-1][column])
    binary += str(image[row-1][column+1])
    binary += str(image[row][column-1])
    binary += str(image[row][column])
    binary += str(image[row][column+1])
    binary += str(image[row+1][column-1])
    binary += str(image[row+1][column])
    binary += str(image[row+1][column+1])
    number = int(binary, 2)
    if algorithm[number] == "#":
        return 1
    return 0


def print_image(image):
    for i in range(0, len(image)):
        row = ""
        for j in range(0, len(image)):
            if image[i][j] == 0:
                row += "."
            else:
                row += "#"
        print(row)


if __name__ == "__main__":
    A = [[1, 2, 3], [4, 5, 6]]
    A = np.array(A)
    r,c = A.shape
    A = np.c_[A,np.zeros(r, dtype=int)]
    print(A)
    part1()
