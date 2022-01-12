import statistics


def part1():
    with open('Day7.txt') as file:
        crabs = [int(x) for x in file.readline().split(',')]
        median = int(statistics.median(crabs))

        fuel = 0
        for crab in crabs:
            fuel += abs(median - crab)
        print(fuel)


def part2():
    with open('Day7.txt') as file:
        crabs = [int(x) for x in file.readline().split(',')]
        mean = int(statistics.mean(crabs))

        fuel = 0
        for crab in crabs:
            distance = abs(mean - crab)
            fuel += distance*(distance+1)/2
        print(fuel)


if __name__ == "__main__":
    part1()
    part2()
