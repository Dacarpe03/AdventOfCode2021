# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np


def analyse_set(numbers_list, index):
    ones = []
    zeroes = []

    for n in numbers_list:
        if n[index] == "1":
            ones.append(n)
        else:
            zeroes.append(n)

    return ones, zeroes

if __name__ == '__main__':
    most_common = ""
    less_common = ""

    binary_list = []
    with open("Day3-1.txt", 'r') as f:
        for line in f.readlines():
            line = line[:-1]
            binary_list.append(line)

    most_common_list = binary_list
    less_common_list = binary_list
    index = 0

    while len(most_common_list) > 1:
        ones, zeroes = analyse_set(most_common_list, index)
        if len(ones) >= len(zeroes):
            most_common_list = ones
        else:
            most_common_list = zeroes
        index += 1

    index = 0
    while len(less_common_list) > 1:
        ones, zeroes = analyse_set(less_common_list, index)
        if len(zeroes) <= len(ones):
            less_common_list = zeroes
        else:
            less_common_list = ones
        index += 1

    print(less_common_list)
    print(most_common_list)
    oxigen_generation_rating = int(most_common_list[0], 2)
    print(oxigen_generation_rating)
    co2_scrubber_rating = int(less_common_list[0], 2)
    print("Oxigen generation rating:", oxigen_generation_rating)
    print("CO2 scrubber rating:", co2_scrubber_rating)
    print("Solution:", oxigen_generation_rating * co2_scrubber_rating)