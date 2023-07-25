from queue import PriorityQueue

# dijkstra
# CHUJOWE

# graf reprezentowany w postaci list sasiadow
def dijkstra(G, s):
    n = len(n)
    distances = [float("inf") for _ in range(n)]
    parents = [None for _ in range(n)]
    distances[s] = 0
    Q = PriorityQueue()
    Q.put((distances[s], s))
    while not Q.empty():
        w, u = Q.get()
        for v, a in G[u]:
            if distances[u] + a < distances[v]:
                distances[v] = distances[u] + a
                parents[v] = u

            if distances[v] == float("inf"):
                Q.put((distances[v], v))
