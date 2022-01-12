STEPSONE = 10
STEPSTWO = 40


def part1():
    rule_dict = {}
    count_dict = {}
    element_dict = {}

    with open('Day14.txt') as file:
        for line in file.readlines():
            line = line.split(" -> ")
            rule = line[0]
            element = line[1][:-1]
            rule_dict[rule] = element
            count_dict[rule] = 0
            element_dict[element] = 0
    initial_state = "KFVHFSSVNCSNHCPCNPVO"
    a = initial_state[0]
    for e in initial_state[1:]:
        element_dict[a] += 1
        b = e
        rule = a + b
        count_dict[rule] += 1
        a = b

    element_dict[a] += 1

    for i in range(0, STEPSTWO):
        print("Step", i)
        update_dicts(count_dict, rule_dict, element_dict)
        print(element_dict)

    minimum = min(element_dict.values())
    maximum = max(element_dict.values())

    print(maximum - minimum)


def update_dicts(count_dict, rule_dict, element_dict):
    new_count = {}
    for key in count_dict:
        if count_dict[key] > 0:
            a = key[0]
            b = key[1]
            e = rule_dict[key]
            first_combination = a+e
            second_combination = e+b

            actual_count = count_dict[key]

            count_dict[key] -= actual_count

            element_dict[e] += actual_count

            if first_combination in new_count.keys():
                new_count[first_combination] += actual_count
            elif actual_count > 0:
                new_count[first_combination] = actual_count

            if second_combination in new_count.keys():
                new_count[second_combination] += actual_count
            elif actual_count > 0:
                new_count[second_combination] = actual_count
    for key in new_count:
        count_dict[key] += new_count[key]


if __name__ == "__main__":
    part1()
