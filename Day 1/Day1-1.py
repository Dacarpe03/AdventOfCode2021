if __name__ == "__main__":
    first = True
    prev = 0
    actual = 0
    count = 0
    with open('Day1-1.txt', 'r') as f:
        for x in f.readlines():
            prev = actual
            actual = int(x)
            if not first:
                if actual > prev:
                    count += 1
            first = False
    print(count)
