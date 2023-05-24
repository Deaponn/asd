# implementation of floyd-warshall algorithm
# for graph given in matrix form


def floyd_warshall(G):
    n = len(G)
    output = [[float("inf") for _ in range(n)] for _ in range(n)]
    parents = [[None for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if x != y and G[x][y] != 0:
                output[x][y] = G[x][y]
                parents[x][y] = x
    for t in range(n):
        for x in range(n):
            for y in range(n):
                new_distance = output[x][t] + output[t][y]
                if output[x][y] > new_distance:
                    output[x][y] = new_distance
                    parents[x][y] = parents[t][y]
    return output


graph = [
    [0, 1, 7, 0, 4, 5, 6],      # 0
    [0, 0, 0, 3, 0, 0, 1],      # 1
    [0, 0, 0, 0, 0, 0, 6],      # 2
    [0, 0, 8, 0, 4, 0, 0],      # 3
    [0, 1, 0, 0, 0, 0, 0],      # 4
    [0, 0, -3, 3, 4, 0, 0],     # 5
    [0, 0, 0, 0, 9, 0, 0]       # 6
]

second_graph = [
    [0, 1, 0, 0, 4, 5, 6],      # 0
    [0, 0, 0, 3, 0, 0, 0],      # 1
    [1, 0, 0, 0, 0, 0, 0],      # 2
    [0, 0, 0, 0, 0, 0, 1],      # 3
    [0, 0, 3, 0, 0, 0, 0],      # 4
    [0, 0, 0, 0, 0, 0, 0],      # 5
    [1, 2, 0, 4, 0, 0, 0]       # 6
]


output = floyd_warshall(graph)

for x in output:
    print(x)

print("-" * 16)

output = floyd_warshall(second_graph)

for x in output:
    print(x)