# implementation of Bellman-Ford algorithm
# for graph in adjacency list format


def relax(v, w, cost, distances, parents):
    if distances[w] > distances[v] + cost:
        parents[w] = v
        distances[w] = distances[v] + cost


def bellman_ford(s, G):
    n = len(G)
    distances = [float("inf")] * n
    parents = [-1] * n
    distances[s] = 0
    for _ in range(n - 1):
        for v in range(n):
            for w, cost in G[v]:
                relax(v, w, cost, distances, parents)
    for v in range(n):
        for w, cost in G[v]:
            if distances[w] > distances[v] + cost:
                return False    # means that there is a negative-sum cycle in the graph
    return distances, parents


graph = [
    [(1, 3)],
    [(2, 2)],
    [(3, -3)],
    [(4, 4)],
    [(1, -1), (5, 2)],
    []
]

graph_with_negative_cycle = [
    [(1, 3)],
    [(2, -2)],      # changing this to -2 makes the cycle overall sum negative
    [(3, -3)],
    [(4, 4)],
    [(1, -1), (5, 2)],
    []
]

print(bellman_ford(0, graph))
print(bellman_ford(0, graph_with_negative_cycle))