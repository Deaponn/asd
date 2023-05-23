# find euler cycle algorithm
# for graph represented as list of neighbours


def euler_cycle(G):
    output = []
    start = 0
    odd_neighbours = 0
    for x in range(len(G)):
        if len(G[x]) % 2 == 1:
            start = x
            odd_neighbours += 1
    if odd_neighbours != 0 and odd_neighbours != 2:
        return None

    # non-recursive version using stack:
    vertexes = [0]
    while len(vertexes) > 0:
        current_vertex = vertexes[-1]
        if len(G[current_vertex]) == 0:
            vertexes.pop()
            output.append(current_vertex)
        else:
            next_vertex = G[current_vertex][0]
            G[current_vertex].pop(0)
            G[next_vertex].remove(current_vertex)
            vertexes.append(next_vertex)

    # recursive version:
    # def DFSVisit(v):
    #     nonlocal G
    #     for w in G[v]:
    #         if w in G[v]:
    #             G[v].remove(w)
    #             G[w].remove(v)
    #             DFSVisit(w)
    #     output.append(v)
    # DFSVisit(start)
    return output[::-1]


graph_all_even = [
    [1, 2, 4, 5],
    [0, 3, 4, 6],
    [0, 3, 5, 6],
    [1, 2, 4, 5],
    [0, 1, 3, 5],
    [0, 2, 3, 4],
    [1, 2]
]

graph_two_odd = [
    [1, 2],
    [0, 3, 4, 6],
    [0, 3, 5, 6],
    [1, 2, 4, 5],
    [1, 3, 5],      # odd number of neigbours
    [2, 3, 4],      # odd number of neigbours
    [1, 2]
]

print(euler_cycle(graph_all_even))
print(euler_cycle(graph_two_odd))