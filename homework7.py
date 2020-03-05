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
    visited = {u: False for u in graph}
    for u in graph:
        if visited[u] is False:
            if DFS(graph, u, u, visited):
                return True
    return False


def DFS(graph, u, previous_node, visited):
    visited[u] = True
    for v in graph[u]:
        if v not in graph:
            continue
        elif visited[v] and graph[v] != previous_node:
            return True
        elif visited[v] is False:
            if DFS(graph, v, u, visited):
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
    +) Thuật toán có độ phức tạp thời gian là O(u+v) do phải thực
    hiện if với n lần (u là len của dict , v la len cua graph[u])
    +) Space memory là O(1)
"""