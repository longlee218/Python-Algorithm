def find_cycle(graph):
    for i in graph:
        if graph[i] != graph:
            continue
        return True
    return False


if __name__ == '__main__':
    graph = {
        'a': {'a2': {}, 'a3': {}},
        'b': {'b2': {}},
        'c': {}
    }
    print(find_cycle(graph))
    graph['c'] = graph
    print(find_cycle(graph))
