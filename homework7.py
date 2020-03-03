"""
    Hi, here's your problem today. This problem was recently asked by Facebook:
        Give an undirected graph, determine if a cycle exists in the graph

        Here is a function signature:

    def find_cycle(graph):
        #Fill this in.
    graph = {
            'a': {'a2': {}, 'a3': {}},
            'b': {'b2': {}},
            'c': {}
        }
    print(find_cycle(graph))
    # False
    graph['c'] = graph
    print(find_cycle(graph))
    #True

"""


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

"""
    +) Thuật toán có độ phức tạp về thời gian là O(n) do phải thực
    hiện if với n lần (n là len của dict)
    +) Độ phức tạp space memory là O(1) do ko khai báo thêm thành phần phụ
"""