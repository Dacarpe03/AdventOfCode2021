if __name__ == "__main__":

    hztal = 0
    depth = 0
    aim = 0

    with open('Day2-2.txt', 'r') as f:
        for line in f.readlines():
            print(line)
            order = line.split(' ')[0]
            units = int(line.split(' ')[1])

            if order == 'forward':
                hztal += units
                depth += aim*units
            elif order == 'down':
                aim += units
            else:
                aim -= units

    print("Horizontal =", hztal)
    print("Depth =", depth)
    print("Solution = ", hztal*depth)
