def process_line(line):
    print("Processing:", line)
    fields = line.split(" -> ")

    initial_position = fields[0].split(',')
    ending_position = fields[1].split(',')

    initial_x_position = int(initial_position[0])
    initial_y_position = int(initial_position[1])
    ending_x_position = int(ending_position[0])
    ending_y_position = int(ending_position[1])

    return initial_x_position, initial_y_position, ending_x_position, ending_y_position


def get_vent_positions(initial_x_position, initial_y_position, ending_x_position, ending_y_position, diagonal):
    print("...Getting positions")
    positions_list = []
    if initial_x_position != ending_x_position and initial_y_position != ending_y_position and not diagonal:
        print("...Doesn't count")
        return positions_list

    x_positions = get_range(initial_x_position, ending_x_position)
    y_positions = get_range(initial_y_position, ending_y_position)

    if initial_x_position != ending_x_position and initial_y_position != ending_y_position:
        for i in range(len(x_positions)):
            positions_list.append(x_positions[i], y_positions[i])
    else:
        for x_pos in x_positions:
            for y_pos in y_positions:
                positions_list.append([x_pos, y_pos])
    return positions_list


def get_range(initial_position, ending_position):
    if initial_position < ending_position:
        greater_position = ending_position+1
        lower_position = initial_position
    else:
        greater_position = initial_position+1
        lower_position = ending_position

    pos_list = []
    for pos in range(lower_position, greater_position):
        pos_list.append(pos)
    return pos_list


def process_vent_position(positions_dictionary, position_lists):
    print("...Adding to dictionary")
    count = 0
    for position in position_lists:
        pos_key = get_pos_key(position)
        if pos_key in positions_dictionary.keys():
            positions_dictionary[pos_key] += 1
            if positions_dictionary[pos_key] == 2:
                count += 1
        else:
            positions_dictionary[pos_key] = 1

    return count


def get_pos_key(position):
    pos_key = f"{position[0]},{position[1]}"
    return pos_key


def count_crossings(positions_dictionary, needed_count):
    print("...Counting crossings")
    crossings = 0
    for val in positions_dictionary.values():
        if val >= needed_count:
            crossings += 1
    return crossings


def main(diagonals):
    positions_dictionary = {}
    with open('Day5.txt', 'r') as f:
        crossings = 0
        for line in f.readlines():
            ini_pos_x, ini_pos_y, end_pos_x, end_pos_y = process_line(line)
            vent_positions = get_vent_positions(ini_pos_x, ini_pos_y, end_pos_x, end_pos_y, diagonal=diagonals)
            crossings += process_vent_position(positions_dictionary, vent_positions)

    print(crossings)
    crossings = count_crossings(positions_dictionary, 2)
    print("Solution:", crossings)


if __name__ == "__main__":
    # main(False)
    main(True)
