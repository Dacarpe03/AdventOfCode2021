HEXA_DICT = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    'C': "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
}

PACKET_VERSION_LENGTH = 3
PACKET_TYPE_ID_LENGTH = 3
PACKET_LENGTH_ID_LENGTH = 1

LENGHTS_ID_DICT = {
    "0": 15,
    "1": 11
}

LITERAL_VALUE = 4
N_BITS = 4
MULTIPLE_OF = 4


def part1():
    with open('Day16.txt') as file:
        line = file.readline()
        binary_string = ""
        for hexa in line:
            binary_string += HEXA_DICT[hexa]
        print(binary_string)

    print(len(binary_string))
    packets, index = parse_string(binary_string, 0, 0, len(binary_string))
    print(packets)

    version_sum = 0
    version_sum += recursive_version_sum(packets)
    print(version_sum)

    operation_solution = recursive_values_operation(packets)
    print(operation_solution)


def parse_string(binary_string, start, index, limit):
    print("String left", binary_string[index:])
    packets = {
        "Version": 0,
        "Type": -1,
        "Literals": None,
        "Subpackets": []
    }

    print("We are at index", index)
    print("The limit is", limit - 1)
    # Get packet version and update index
    packet_version = get_packet_version(binary_string, index)
    index += PACKET_VERSION_LENGTH
    print("Packet version:", packet_version)

    # Get packet type and update index
    packet_type_id = get_packet_type_id(binary_string, index)
    index += PACKET_TYPE_ID_LENGTH
    print("Packet type id:", packet_type_id)
    # If literal value
    if packet_type_id == LITERAL_VALUE:
        print("We have literal value from type ID")
        # Get literal values
        literal_value, literal_length = get_literal_value(binary_string, index)
        index += literal_length

        # Create new packet
        new_packet = {
            "Version": packet_version,
            "Type": packet_type_id,
            "Literals": literal_value,
            "Subpackets": []
        }
        print(new_packet)
        return new_packet, index

    else:
        # Get I bit
        length_id = get_length_id(binary_string, index)
        index += PACKET_LENGTH_ID_LENGTH
        next_str_len = LENGHTS_ID_DICT[length_id]

        # Parse L bits
        if length_id == "0":
            subpackets_length = get_n_subpackets(binary_string, index, next_str_len)
            index += next_str_len
            subpackets_ending = index + subpackets_length
            subpackets = []

            while index < subpackets_ending - 1:
                print("\nNew zero subpacket")
                new_subpacket, index = parse_string(binary_string, index, index, subpackets_ending)
                print(index)
                print("Exiting recursion")
                subpackets.append(new_subpacket)

            new_packet = {
                "Version": packet_version,
                "Type": packet_type_id,
                "Literals": None,
                "Subpackets": subpackets
            }
            packets['Subpackets'].append(new_packet)
        else:
            print("\nNew one subpacket")
            n_subpackets = get_n_subpackets(binary_string, index, next_str_len)
            index += next_str_len
            subpackets = []
            while len(subpackets) < n_subpackets:
                new_subpacket, index = parse_string(binary_string, index, index, len(binary_string))
                subpackets.append(new_subpacket)
            new_packet = {
                "Version": packet_version,
                "Type": packet_type_id,
                "Literals": None,
                "Subpackets": subpackets
            }
            packets['Subpackets'].append(new_packet)
            # Skip leading zeroes
    return new_packet, index


def get_packet_version(binary_string, index):
    binary_string = get_substring(binary_string, index, PACKET_VERSION_LENGTH)
    version = int(binary_string, 2)
    return version


def get_packet_type_id(binary_string, index):
    binary_string = get_substring(binary_string, index, PACKET_TYPE_ID_LENGTH)
    type_id = int(binary_string, 2)
    return type_id


def get_literal_value(binary_string, index):
    initial_index = index
    last = False
    binary_number = ""
    while not last:
        last = binary_string[index] == "0"
        index += 1
        binary_number += get_substring(binary_string, index, N_BITS)
        index += N_BITS
    length = index - initial_index
    number = int(binary_number, 2)
    return number, length


def get_length_id(binary_string, index):
    l_id = get_substring(binary_string, index, PACKET_LENGTH_ID_LENGTH)
    return l_id


def get_n_subpackets(binary_string, index, str_len):
    subpackets_string = get_substring(binary_string, index, str_len)
    return int(subpackets_string, 2)


def get_substring(binary_string, index, lenght):
    return binary_string[index: index + lenght]


def recursive_version_sum(packet):
    if len(packet['Subpackets']) == 0:
        return packet['Version']
    else:
        version_sum = packet['Version']
        for subpacket in packet['Subpackets']:
            version_sum += recursive_version_sum(subpacket)
        return version_sum


def recursive_values_operation(packet):
    ptype = packet['Type']
    if ptype == 4:
        value = packet['Literals']
    else:
        print("Operation", ptype)
        value = operate_subpackets(packet['Subpackets'], ptype)
    print("Value", value, "of", packet, )
    return value


def check_values(packet):
    if len(packet['Subpackets']) == 0 and packet['Literals'] is None:
        return False
    for s in packet['Subpackets']:
        if not check_values(s):
            return False


def operate_subpackets(subpackets, ptype):
    switch_ptype = {
        0: add_packets,
        1: product_packets,
        2: min_packets,
        3: max_packets,
        5: greater_packet,
        6: less_packet,
        7: equal_packet,
    }

    return switch_ptype[ptype](subpackets)


def add_packets(packets):
    total = 0
    for subpacket in packets:
        total += recursive_values_operation(subpacket)
    return total


def product_packets(packets):
    total = 1
    for subpacket in packets:
        total *= recursive_values_operation(subpacket)
    return total


def min_packets(packets):
    values = []
    for subpacket in packets:
        val = recursive_values_operation(subpacket)
        values.append(val)
    return min(values)


def max_packets(packets):
    values = []
    for subpacket in packets:
        val = recursive_values_operation(subpacket)
        values.append(val)
    return max(values)


def greater_packet(packets):
    if recursive_values_operation(packets[0]) > recursive_values_operation(packets[1]):
        return 1
    else:
        return 0


def less_packet(packets):
    if recursive_values_operation(packets[0]) < recursive_values_operation(packets[1]):
        return 1
    else:
        return 0


def equal_packet(packets):
    if recursive_values_operation(packets[0]) == recursive_values_operation(packets[1]):
        return 1
    else:
        return 0


if __name__ == "__main__":
    part1()
