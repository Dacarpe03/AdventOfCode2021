def part1():
    with open("Day18.txt") as file:
        first = file.readline().strip("\n")
        print("First", first)
        second = file.readline().strip("\n")
        snailfish_str = "["+first+","+second+"]"
        print("Second", second)
        snailfish_number = proccess_line(first)
        print(snailfish_number)
        print(first)
        print(snailfish_number_to_str(snailfish_number))
        for line in file.readlines():
            print("\nProcessing new line")
            line = line.rstrip('\n')
            snailfish_str = "["+snailfish_str+","+line+"]"
            snailfish_str = reduce_number(snailfish_str)


def reduce_number(snailfish_number):
    again = True
    while again:
        lower = 100
        for index in range(0, len(snailfish_number)):
            reg = snailfish_number[index]
            depth = reg['Value']


def proccess_line(snailfish_str):
    index = 0
    depth = -1
    snailfish_number = []
    while index < len(snailfish_str) - 1:
        actual_character = snailfish_str[index]
        if actual_character == '[':
            depth += 1
        elif actual_character == ']':
            depth -= 1
        elif actual_character != ',':
            number = ""
            while actual_character not in ['[', ']', ',']:
                number += actual_character
                index += 1
                actual_character = snailfish_str[index]
            index -= 1
            number = int(number)
            snailfish_number.append({'Depth': depth,
                                     'Value': number})
        index += 1

    return snailfish_number


def snailfish_number_to_str(snailfish_number):
    str_number = "["
    last_depth = 0
    for reg in snailfish_number:
        depth = reg['Depth']
        value = reg['Value']
        if depth > last_depth:
            for i in range(last_depth, depth):
                str_number += "["
            str_number += str(value) + ","
        elif depth == last_depth:
            str_number += str(value) + "]"
        elif last_depth > depth:
            for i in range(depth, last_depth):
                str_number += "]"
            str_number += "," + "[" + str(value) + ","
        last_depth = depth
    for i in range(0, last_depth):
        str_number += "]"

    return str_number


if __name__ == "__main__":
    part1()

