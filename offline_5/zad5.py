# Bartosz Sajecki

# wykonuje algorytm Dijkstry z wierzcholka a oraz b
# nastepnie znajduje najblizsza osobliwosc od a oraz od b
# jesli suma odleglosci jest mniejsza niz dlugosc sciezki bezposredniej
# to korzystam z przejscia osobliwoscia i zwracam sume tych odleglosci
# rozwiazanie to dziala poniewaz algorytm Dijkstry zawsze znajduje najkrotsza sciezke
# zlozonosc tego algorytmu to O(E + ElogV + S)


from zad5testy import runtests
from queue import PriorityQueue


# def construct_matrix_representation(E, S, n):
#     s = len(S)
#     G = [[-1 for _ in range(n)] for _ in range(n)]
#     for (v, w, c) in E:
#         G[v][w] = c
#         G[w][v] = c
#     for x in range(s):
#         for y in range(x + 1, s):
#             G[S[x]][S[y]] = 0
#             G[S[y]][S[x]] = 0
#     return G


def construct_list_representation(E, n):
    G = [[] for _ in range(n)]
    for (v, w, c) in E:
        G[v].append((c, w))
        G[w].append((c, v))
    return G


# def dijkstra_matrix(G, s, n):
#     distances = [float("inf") for _ in range(n)]
#     distances[s] = 0
#     queue = PriorityQueue()
#     for x in range(n):
#         if x == s:
#             queue.put((0, x))
#         else:
#             queue.put((float("inf"), x))
#     while not queue.empty():
#         (_, u) = queue.get()
#         for w in range(n):
#             if G[u][w] != -1:
#                 if distances[w] > distances[u] + G[u][w]:
#                     distances[w] = distances[u] + G[u][w]
#                     queue.put((distances[w], w))
#     return distances


def dijkstra_list(G, s, n):
    distances = [float("inf") for _ in range(n)]
    distances[s] = 0
    queue = PriorityQueue()
    for x in range(n):
        if x == s:
            queue.put((0, x))
        else:
            queue.put((float("inf"), x))
    while not queue.empty():
        (_, u) = queue.get()
        for (distance, w) in G[u]:
            if distances[w] > distances[u] + distance:
                distances[w] = distances[u] + distance
                queue.put((distances[w], w))
    return distances


def spacetravel( n, E, S, a, b ):
    G = construct_list_representation(E, n)
    distances_a = dijkstra_list(G, a, n)
    distances_b = dijkstra_list(G, b, n)
    closest_a_singularity = distances_a[S[0]]
    closest_b_singularity = distances_b[S[0]]
    for v in S:
        if distances_a[v] < closest_a_singularity:
            closest_a_singularity = distances_a[v]
        if distances_b[v] < closest_b_singularity:
            closest_b_singularity = distances_b[v]
    if distances_a[b] == float("inf") and (closest_a_singularity == float("inf") or closest_b_singularity == float("inf")):
        return None
    return min(distances_a[b], closest_a_singularity + closest_b_singularity)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )