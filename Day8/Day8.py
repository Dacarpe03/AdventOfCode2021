ZERO = {'a', 'b', 'c', 'e', 'f', 'g'}
ONE = {'c', 'f'}
TWO = {'a', 'c', 'd', 'e', 'g'}
THREE = {'a', 'c', 'd', 'f', 'g'}
FOUR = {'b', 'c', 'd', 'f'}
FIVE = {'a', 'b', 'd', 'f', 'g'}
SIX = {'a', 'b', 'd', 'e', 'f', 'g'}
SEVEN = {'a', 'c', 'f'}
EIGHT = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
NINE = {'a', 'b', 'c', 'd', 'f', 'g'}

SEGMENTS_NUMBER_DICT = {
    2: [ONE],
    3: [SEVEN],
    4: [FOUR],
    5: [TWO, THREE, FIVE],
    6: [ZERO, SIX, NINE],
    7: [EIGHT]
}


def get_decode_dict():
    return {'a': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
            'b': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
            'c': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
            'd': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
            'e': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
            'f': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
            'g': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
            }


def get_number_dict():
    return {'a': {},
            'b': {},
            'c': {},
            'd': {},
            'e': {},
            'f': {},
            'g': {},
            }


def update_decode_dict(signal, decode_dict):
    n_segments = len(signal)
    for segment in signal:
        possible_numbers = SEGMENTS_NUMBER_DICT[n_segments]
        possible_decode = decode_dict[segment]
        for possible_number in possible_numbers:
            if len(possible_decode) > 1:
                decode_dict[segment] = possible_decode.intersection(possible_number)


def update_possible_number_dict(signal, pn_dict):
    n_segments = len(signal)
    for segment in signal:
        pn_dict[segment].add(n_segments)


def part1():
    count = 0
    onefourseveneight = [2, 3, 4, 7]
    with open('Day8.txt') as file:
        for line in file.readlines():
            line = line[:-1].split(" | ")
            output = line[1].split(" ")
            print(output)
            for number in output:
                length = len(number)
                if length in onefourseveneight:
                    count += 1
    print("Solution:", count)


def decode_signals(signals):
    dict_lenghts = {
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: []
    }

    dict_decoding = {
    }

    for signal in signals:
        l = len(signal)
        dict_lenghts[l].append(set(signal))

    dict_decoding[1] = dict_lenghts[2][0]
    dict_decoding[4] = dict_lenghts[4][0]
    dict_decoding[7] = dict_lenghts[3][0]
    dict_decoding[8] = dict_lenghts[7][0]

    for signal in dict_lenghts[6]:
        if len(signal.intersection(dict_decoding[4])) == 4:
            dict_decoding[9] = signal
        elif len(signal.intersection(dict_decoding[1])) == 2:
            dict_decoding[0] = signal
        else:
            dict_decoding[6] = signal

    for signal in dict_lenghts[5]:
        if len(signal.intersection(dict_decoding[7])) == 3:
            dict_decoding[3] = signal
        elif len(signal.intersection(dict_decoding[6])) == 5:
            dict_decoding[5] = signal
        else:
            dict_decoding[2] = signal
    return dict_decoding


def use_decoder(dict_decode, output):
    number = ""
    print(output)
    print(dict_decode)
    for out in output:
        print(out)
        for i in range(0, 10):
            if set(out) == dict_decode[i]:
                number += str(i)
                break
    print(number)
    return int(number)


def part2():
    count = 0
    with open('Day8.txt') as file:
        for line in file.readlines():
            print(line)
            line = line.split(" | ")
            signals = line[0].split(" ")
            output = line[1][:-1].split(" ")
            dict_decode = decode_signals(signals)
            count += use_decoder(dict_decode, output)
    print("Solution:", count)


if __name__ == "__main__":
    # part1()
    part2()
