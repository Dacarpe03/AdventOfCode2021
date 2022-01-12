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


def main(cycles):
    with open('Day6.txt') as file:
        lanternfishes = []
        initial_timers = file.readline().split(',')
        for t in initial_timers:
            lanternfishes.append(Fish(int(t)))

    for i in range(0, cycles):
        new_fish_count = 0

        for fish in lanternfishes:
            if fish.next_cycle():
                new_fish_count += 1

        for count in range(0, new_fish_count):
            lanternfishes.append(Fish(FIRST_CYCLE_TIMER))
    print("Solution:", len(lanternfishes))


if __name__ == "__main__":
    main(CYCLES_1)
    # main(CYCLES_2)
