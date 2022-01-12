CHARACTER_DICT = {
    "[": "]",
    "{": "}",
    "<": ">",
    "(": ")"
}

ERRORS_DICT = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

SCORES_DICT = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}


def part1():
    with open("Day10.txt", "r") as file:
        lines = []
        for line in file.readlines():
            lines.append(list(line[:-1]))

    total_error = 0
    incomplete_lines = []
    missing_characters = []
    for line in lines:
        first_error, expected_characters = get_first_error(line)
        if first_error != "OK":
            print(line)
            print("Error:", first_error)
            total_error += ERRORS_DICT[first_error]
        else:
            incomplete_lines.append(lines)
            missing_characters.append(expected_characters)

    print("Solution", total_error)
    calculate_score(missing_characters)


def calculate_score(missing_characters):
    scores = []
    for missing in missing_characters:
        score = 0
        while not len(missing) == 0:
            score *= 5
            character = missing.pop()
            score += SCORES_DICT[character]
        scores.append(score)
    scores.sort()
    print("Solution", scores[len(scores)//2])


def get_first_error(line):
    error = False
    index = 0
    character = line[index]
    expected_characters = [CHARACTER_DICT[character]]
    index = 1
    while not error and index < len(line):
        current_character = line[index]
        # print("Current character", current_character)
        if current_character in CHARACTER_DICT.keys():
            expected_characters.append(CHARACTER_DICT[current_character])
            # print("Expected characters", expected_characters)
        else:
            expected_character = expected_characters.pop()
            # print("Expected character", expected_character)
            # print("Expected characters", expected_characters)

            if current_character != expected_character:
                return current_character, expected_characters
        index += 1
    return "OK", expected_characters


if __name__ == "__main__":
    part1()