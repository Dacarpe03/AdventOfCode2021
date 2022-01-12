if __name__ == "__main__":
    first = True
    a = 0
    b = 0
    c = 0
    prev_sum = -1
    actual_sum = -1
    count = 0
    numbers_read = 0
    with open('Day1-1.txt', 'r') as f:
        for x in f.readlines():
            a = b
            b = c
            c = int(x)

            numbers_read += 1

            prev_sum = actual_sum
            actual_sum = a + b + c

            if numbers_read > 3:
                if actual_sum > prev_sum:
                    count += 1

    print(count)
