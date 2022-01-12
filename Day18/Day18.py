LEFT = 'Left'
RIGHT = 'Right'
UPPER = 'Upper'
import math

import sys


def part1():
    with open("Day18.txt") as file:
        first = file.readline().strip("\n")
        print("First", first)
        second = file.readline().strip("\n")
        snail_str = "["+first+","+second+"]"
        print("Second", second)
        snailfish_number, id = process_line(list(snail_str), 0, None, 0)
        print(print_node(snailfish_number))
        reduce_number(snailfish_number, id+1)
        print(print_node(snailfish_number))
        for line in file.readlines():
            print("\nProcessing new line")
            line = line.rstrip('\n')
            snailfish_str = "["+print_node(snailfish_number)+","+line+"]"
            snailfish_number, id = process_line(list(snailfish_str), 0, None, 0)
            print(snailfish_number)
            print(print_node(snailfish_number))
            reduce_number(snailfish_number, id+1)
        print(print_node(snailfish_number))
        print(get_magnitude(snailfish_number))


def part2():
    with open("Day18.txt", "r") as file:
        numbers_strs = []
        for line in file.readlines():
            numbers_strs.append(line.rstrip("\n"))
        max = 0
        for i in range(0, len(numbers_strs)):
            for j in range(0, len(numbers_strs)):
                if i != j:
                    first = numbers_strs[i]
                    print("First", first)
                    second = numbers_strs[j]
                    snail_str = "[" + first + "," + second + "]"
                    print("Second", second)
                    snailfish_number, id = process_line(list(snail_str), 0, None, 0)
                    print(snailfish_number)
                    print(print_node(snailfish_number))
                    reduce_number(snailfish_number, id + 1)
                    print(print_node(snailfish_number))
                    magnitude = get_magnitude(snailfish_number)
                    if magnitude > max:
                        max = magnitude
        print(max)


def get_magnitude(node):
    if isinstance(node, int):
        return node
    else:
        return 3*get_magnitude(node[LEFT]) + 2*get_magnitude(node[RIGHT])


def process_line(line, depth, upper_node, id):
    node = {
        'Id': id,
        'Depth': depth,
        'Upper': upper_node,
        'Left': None,
        'Right': None,
    }
    character = line.pop(0)
    if character != '[' and character != ']':
        return int(character), id
    if character == '[':
        node['Left'], id = process_line(line, depth+1, node, id + 1)
        comma = line.pop(0)
        node['Right'], id = process_line(line, depth+1, node, id + 1)
        corchete = line.pop(0)
        return node, id


def reduce_number(snailfish_number, next_id):
    clear_number(snailfish_number, None)
    print(print_node(snailfish_number))
    again, next_id = process_node_explode(snailfish_number, 0, next_id)
    if again:
        reduce_number(snailfish_number, next_id)
    else:
        again, next_id = process_node_split(snailfish_number, 0, next_id)
        if again:
            reduce_number(snailfish_number, next_id)


def process_node_explode(node, depth, next_id):
    if not isinstance(node, int):
        if node['Depth'] == 4:
            print("Exploding", print_node(node))
            explode(node)
            return True, next_id

        changed, next_id = process_node_explode(node[LEFT], depth + 1, next_id)
        if changed:
            return True, next_id

        changed, next_id = process_node_explode(node[RIGHT], depth + 1, next_id)
        if changed:
            return True, next_id

    return False, next_id


def process_node_split(node, depth, next_id):
    if not isinstance(node, int):
        if not isinstance(node[LEFT], int):
            changed, next_id = process_node_split(node[LEFT], depth + 1, next_id)
            if changed:
                return True, next_id
        elif isinstance(node[LEFT], int) and node[LEFT] > 9:
            print("Spliting", print_node(node))
            split(node, LEFT, next_id)
            return True, next_id + 1

        if not isinstance(node[RIGHT], int):
            changed, next_id = process_node_split(node[RIGHT], depth + 1, next_id)
            if changed:
                return True, next_id
        elif isinstance(node[RIGHT], int) and node[RIGHT] > 9:
            print("Spliting", print_node(node))
            split(node, RIGHT, next_id)
            return True, next_id + 1



    return False, next_id


def explode(node):
    if not isinstance(node[LEFT], int):
        explode(node[LEFT])
    elif not isinstance(node[RIGHT], int):
        explode(node[RIGHT])
    else:
        node_id = node['Id']
        left_number = node[LEFT]
        right_number = node[RIGHT]
        leftmost_node = get_dirmost_node_recursion(node_id, node_id, node, LEFT, False, left_number)
        # print("Leftmo1st", print_node(leftmost_node))
        rightmost_node = get_dirmost_node_recursion(node_id, node_id, node, RIGHT, False, right_number)
        # print("Rightmost", print_node(rightmost_node))
        node[LEFT] = -1
        node[RIGHT] = -1


def split(node, side, id):
    number = node[side]
    upper = math.ceil(number/2)
    lower = math.floor(number/2)
    depth = node['Depth'] + 1
    node[side] = {
        'Id': id,
        'Depth': depth,
        'Upper': node,
        'Left': lower,
        'Right': upper
    }


def get_dirmost_node_recursion(initial_node_id, previous_id, node, direction, turned, adding):
    if not turned:
        if node[UPPER] is None:
            if isinstance(node[direction], int):
                node[direction] += adding
                return node
            elif node[direction]['Id'] == previous_id:
                return None
            else:
                return get_dirmost_node_recursion(initial_node_id, node['Id'], node[direction], direction, True, adding)
        elif not isinstance(node[UPPER][direction], int):
            if node[UPPER][direction]['Id'] == node['Id']:
                return get_dirmost_node_recursion(initial_node_id, node['Id'], node[UPPER], direction, turned, adding)
            else:
                return get_dirmost_node_recursion(initial_node_id, node['Id'], node[UPPER][direction], direction, True, adding)
        elif isinstance(node[UPPER][direction], int):
            node[UPPER][direction] += adding
            return node[UPPER]
    else:
        # print("turned")
        opposite = LEFT if direction == RIGHT else RIGHT
        if isinstance(node[opposite], int):
            node[opposite] += adding
            return node
        elif node[opposite]['Id'] == initial_node_id:
            return None
        else:
            return get_dirmost_node_recursion(initial_node_id, node['Id'], node[opposite], direction, True, adding)


def get_dirmost_node(node, direction, turned, adding):
    found = False
    current_node = node.copy()
    while not found:
        if not turned:
            if current_node[UPPER] is None:
                return None
            elif current_node[UPPER]['Id'] == current_node['Id']:
                current_node = current_node[UPPER].copy()
            else:
                if isinstance(current_node[UPPER][direction], int):
                    current_node[UPPER][direction] += adding
                    found = True
                    return current_node[UPPER]
                else:
                    turned = True
                    current_node = current_node[UPPER][direction].copy()
        else:
            print("turned")
            opposite = LEFT if direction == RIGHT else RIGHT
            if isinstance(current_node[opposite], int):
                current_node[opposite] += adding
                found = True
                return current_node
            else:
                current_node = current_node[opposite].copy()


def clear_number(node, side):
    if isinstance(node[LEFT], int) and isinstance(node[RIGHT], int):
        if node[LEFT] == -1 and node[RIGHT] == -1:
            node[UPPER][side] = 0
        return
    else:
        if not isinstance(node[LEFT], int):
            clear_number(node[LEFT], LEFT)
        if not isinstance(node[RIGHT], int):
            clear_number(node[RIGHT], RIGHT)


def print_node(node):
    if node is None:
        return "None"
    # node_str = "D"+str(node['Depth'])
    node_str = "["
    if isinstance(node['Left'], int):
        node_str += str(node['Left'])
    else:
        node_str += print_node(node['Left'])
    node_str += ","
    if isinstance(node['Right'], int):
        node_str += str(node['Right'])
    else:
        node_str += print_node(node['Right'])
    node_str += "]"
    return node_str


if __name__ == "__main__":
    part2()

