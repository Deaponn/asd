# implementation of prim's algorithm
# for a graph given as a, adjacency list


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


def prim(s, G):
    n = len(G)
    parent = [None] * n
    distance = [float("inf")] * n
    vertex_queue = PriorityQueue()
    vertex_queue.put((0, s))
    while not vertex_queue.empty():
        dist, v = vertex_queue.get()
        distance[v] = dist
        for w, cost in G[v]:
            if cost < distance[w]:
                vertex_queue.put((cost, w))
                parent[w] = v
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
    [(7, 1), (0, 3)]
]


parents = prim(0, graph)

for vertex, parent in enumerate(parents[::-1]):
    print(len(graph) - vertex - 1, " -> ", parent)
