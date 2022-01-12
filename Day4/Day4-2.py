def get_info():
    random_numbers_list = []
    bingos_list = []
    numbers_info = {
    }

    with open("Day4-1.txt", "r") as file:
        rand_input = file.readline()[:-1]
        random_numbers_list = rand_input.split(",")
        bingo_id = 0
        while file.readline():
            # New bingo
            bingo_dict = {
                "content": [],
                "boolean_matrix": [[False, False, False, False, False],
                                   [False, False, False, False, False],
                                   [False, False, False, False, False],
                                   [False, False, False, False, False],
                                   [False, False, False, False, False]],
                "rows": {
                    0: 0,
                    1: 0,
                    2: 0,
                    3: 0,
                    4: 0
                },
                "columns": {
                    0: 0,
                    1: 0,
                    2: 0,
                    3: 0,
                    4: 0
                },
                "won": False
            }

            for i in range(0, 5):
                line = file.readline()
                line_numbers = line.split()
                for j in range(0, 5):
                    number = line_numbers[j]
                    if number in numbers_info.keys():
                        numbers_info[number]["bingos_attached"].append(bingo_id)
                        numbers_info[number]["positions"].append([i, j])
                    else:
                        numbers_info[number] = {
                            "bingos_attached": [bingo_id],
                            "positions": [[i, j]]
                        }
                bingo_dict["content"].append(line_numbers)
            bingos_list.append(bingo_dict)
            bingo_id += 1

    return numbers_info, random_numbers_list, bingos_list


def check_bingo(bingo):
    if bingo["won"]:
        return False

    if 5 in bingo["rows"].values() or 5 in bingo["columns"].values():
        return True
    else:
        return False


def mark_bingos(n_info, bingos_list):
    win_count = 0
    last_id = -1
    for i in range(len(n_info["bingos_attached"])):
        bingo_id = n_info["bingos_attached"][i]
        position = n_info["positions"][i]
        row = position[0]
        column = position[1]

        bingos_list[bingo_id]["rows"][row] += 1
        bingos_list[bingo_id]["columns"][column] += 1

        bingos_list[bingo_id]["boolean_matrix"][row][column] = True

        if check_bingo(bingos_list[bingo_id]):
            print("Bingo!!!:", bingo_id)
            bingos_list[bingo_id]["won"] = True
            win_count += 1
            last_id = bingo_id
    return win_count, last_id


def calculate_bingo_sum(bingo):
    bool_matrix = bingo["boolean_matrix"]
    content = bingo["content"]
    sum = 0

    for i in range(0, 5):
        for j in range(0, 5):
            if not bool_matrix[i][j]:
                sum += int(content[i][j])
    return sum


if __name__ == '__main__':
    numbers_info, random_numbers_list, bingos_list = get_info()
    win_count = 0
    for n in random_numbers_list:
        n_info = numbers_info[n]
        n_wins, last_id = mark_bingos(n_info, bingos_list)
        win_count += n_wins
        if win_count == len(bingos_list):
            bingo = bingos_list[last_id]
            print("Last Winning number:", n)
            print("Last Winning bingo:")
            print(bingo)
            bingo_sum = calculate_bingo_sum(bingo)
            print("Bingo sum:", bingo_sum)
            print("Solution:", bingo_sum * int(n))
            break

