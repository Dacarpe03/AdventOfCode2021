FIRST_CYCLE_TIMER = 8
CYCLE_TIMER = 6
CYCLES_1 = 80
CYCLES_2 = 256


class Fish:
    def __init__(self, timer):
        self.timer = timer

    def next_cycle(self):
        self.timer -= 1
        if self.timer < 0:
            self.timer = 6
            return True
        return False


def next_cycle(lanternfishes_days):
    new_day = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(1, 9):
        new_day[i-1] += lanternfishes_days[i]
    new_day[8] += lanternfishes_days[0]
    new_day[6] += lanternfishes_days[0]
    return new_day


def main(cycles):
    with open('Day6.txt') as file:
        lanternfishes_days = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        initial_timers = file.readline().split(',')
        for t in initial_timers:
            lanternfishes_days[int(t)] += 1

        for i in range(0, cycles):
            lanternfishes_days = next_cycle(lanternfishes_days)

        total_fish = 0
        for i in range(0, 9):
            total_fish += lanternfishes_days[i]

        print("Solution:", total_fish)


if __name__ == "__main__":
    main(CYCLES_1)
    main(CYCLES_2)
