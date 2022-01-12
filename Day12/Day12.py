START = "start"
END = "end"

def part1():
    graph = {}
    with open("Day12.txt", "r") as file:
        lines = []
        for line in file.readlines():
            lines.append(line[:-1])

    for line in lines:
        ini = line.split('-')[0]
        end = line.split('-')[1]
        if ini in graph.keys():
            graph[ini]['Adjacents'].append(end)
        else:
            small = True
            if ini.isupper():
                small = False
            graph[ini] = {'Small': small,
                          'Adjacents': [end]}

        if end in graph.keys():
            graph[end]['Adjacents'].append(ini)
        else:
            small = True
            if end.isupper():
                small = False
            graph[end] = {'Small': small,
                          'Adjacents': [ini]}

    smalls_visited = set()
    n_paths = get_n_paths_repeated(graph, START, smalls_visited, False, None, [START])
    print(n_paths)


def get_n_paths(graph, ini, smalls_visited):
    n_paths = 0
    if ini == END:
        return 1
    else:
        if graph[ini]['Small']:
            smalls_visited.add(ini)
        adjacents = graph[ini]['Adjacents']
        for adj in adjacents:
            if adj not in smalls_visited:
                n_paths += get_n_paths(graph, adj, smalls_visited)
        if graph[ini]['Small']:
            smalls_visited.remove(ini)
    return n_paths


def get_n_paths_repeated(graph, ini, smalls_visited, repeated, repeated_node, lista):
    n_paths = 0
    if ini == END:
        print(lista)
        return 1
    else:
        if graph[ini]['Small']:
            smalls_visited.add(ini)
        adjacents = graph[ini]['Adjacents']
        for adj in adjacents:
            if adj in smalls_visited and not repeated and adj != START:
                lista.append(adj)
                n_paths += get_n_paths_repeated(graph, adj, smalls_visited, True, adj, lista)
                lista.pop()
            elif adj not in smalls_visited:
                lista.append(adj)
                n_paths += get_n_paths_repeated(graph, adj, smalls_visited, repeated, None, lista)
                lista.pop()

        if not repeated:
            if graph[ini]['Small']:
                smalls_visited.remove(ini)
        else:
            if graph[ini]['Small'] and ini != repeated_node:
                smalls_visited.remove(ini)

    return n_paths


if __name__ == "__main__":
    part1()
