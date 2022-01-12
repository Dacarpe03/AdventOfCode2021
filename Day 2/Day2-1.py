if __name__ == "__main__":
    x = 0
    y = 0
    with open('Day2-1.txt', 'r') as f:
        for line in f.readlines():
            order = line.split(' ')[0]
            units = int(line.split(' ')[1])

            if order == 'forward':
                x += units
            elif order == 'down':
                y += units
            else:
                y -= units
    print("Horizontal =", x)
    print("Depth =", y)
    print("Solution = ", x*y)
