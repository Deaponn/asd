# dijkstra algorithm for a graph given in a neighbours list


from queue import PriorityQueue


def dijkstra(s, G):
    n = len(G)
    distance = [float("inf") for _ in range(n)]
    distance[s] = 0
    parent = [None] * n
    queue = PriorityQueue()
    queue.put((0, s))
    while not queue.empty():
        _, v = queue.get()
        for cost, w in G[v]:
            if distance[v] + cost < distance[w]:
                parent[w] = v
                distance[w] = distance[v] + cost
                queue.put((distance[w], w))
    return distance, parent
