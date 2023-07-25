# implementation of prim's algorithm
# for a graph given as an adjacency list


from queue import PriorityQueue


# this assumes that the item exists
# def bin_search(iterable, item, compare):
#     start = 0
#     end = len(iterable)
#     middle = (start + end) // 2
#     comparison = compare(iterable[middle], item)
#     while not comparison == 0:
#         if comparison < 0:
#             end = middle - 1
#         else:
#             start = middle + 1
#         middle = (start + end) // 2
#         comparison = compare(iterable[middle], item)
#     return iterable[middle]


def prim1(s, G):
    n = len(G)
    parent = [None] * n
    distance = [float("inf")] * n
    vertex_queue = PriorityQueue()
    vertex_queue.put((0, s, -1))
    while not vertex_queue.empty():
        dist, v, p = vertex_queue.get()
        distance[v] = dist
        parent[v] = p
        for w, cost in G[v]:
            if cost < distance[w]:
                vertex_queue.put((cost, w, v))
    return parent


def prim(s, G):
    n = len(G)
    distance = [float("inf") for _ in range(n)]
    distance[s] = 0
    parent = [None] * n
    nonvisited = [True] * n
    queue = PriorityQueue()
    queue.put((0, s))
    while not queue.empty():
        _, v = queue.get()
        for w, cost in G[v]:
            if nonvisited[w] and cost < distance[w]:
                print(v, w, cost, distance[w])
                parent[w] = v
                distance[w] = cost
                queue.put((distance[w], w))
        nonvisited[v] = False
    return parent


graph = [
    [(2, 1), (8, 3)],
    [(2, 1), (4, 3), (6, 3), (7, 3)],
    [(0, 1), (1, 1), (3, 1), (4, 1), (5, 3)],
    [(2, 1), (5, 3)],
    [(2, 1), (6, 1), (1, 3)],
    [(4, 1), (2, 3), (3, 3)],
    [(4, 1), (7, 1), (1, 3)],
    [(6, 1), (8, 1), (1, 3)],
    [(7, 1), (0, 3)],
]

graph2 = [
    [(1, 1), (5, 8), (4, 5)],  # 0
    [(0, 1), (2, 3)],  # 1
    [(1, 3), (3, 6), (4, 4)],  # 2
    [(2, 6), (4, 2)],  # 3
    [(3, 2), (5, 7), (0, 5), (2, 4)],  # 4
    [(4, 7), (0, 8)],  # 5
]

parents = prim(0, graph2)

for vertex, parent in enumerate(parents[::-1]):
    print(len(graph2) - vertex - 1, " -> ", parent)
