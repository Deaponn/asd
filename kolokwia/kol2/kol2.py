# Bartosz Sajecki

# piekne drzewo rozpinajace musi skladac sie ze spojnego podciagu wszystkich krawedzi grafu,
# ktore wczesniej posortowalismy w kolejnosci rosnacej wzgledem ich wagi

# poniewaz szukamy pieknego drzewa rozpinajacego o najmniejszej wadze,
# to zaczynamy od krawedzi o najmniejszej wadze, a gdy nie uda sie utworzyc
# pieknego MST zaczynajac od niej, to zaczynamy o krawedz dalej

# w szczegolnosci nalezy tez zwrocic uwage na to ze graf ten musi byc spojny

# zlozonosc tego rozwiazania to O(VE + E logE + V + E^2 + E^2 logV)) = O(VE + E^2 logV)


from kol2testy import runtests


class Node:
    def __init__(self, value):
        self.parent = self
        self.value = value
        self.rank = 0


def find_set(x):
    if x != x.parent:
        x.parent = find_set(x.parent)
    return x.parent


def union(x, y):
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def reset_find_unions(find_unions):
    for item in find_unions:
        item.parent = item


def convert_to_edge_list(G):
    n = len(G)
    output = []
    for v in range(n):
        for w, cost in G[v]:
            if v < w:
                output.append((v, w, cost))
    return output


def kruskall_from(start, G, vertexes, find_unions):
    n = len(G)
    edges_sum = 0
    vertexes_in_MST = 0
    for start_idx in range(start, n):
        if vertexes_in_MST == vertexes:
            return edges_sum
        v, u, cost = G[start_idx]
        v = find_set(find_unions[v])
        u = find_set(find_unions[u])
        if v == u:
            # znaleziono cykl a to oznacza, ze nie da sie wykorzystac
            # wszystkich krawedzi jedna za druga tak,
            # aby tworzyly one podciag spojny wsrod reszty krawedzi
            return None
        else:
            vertexes_in_MST += 1
            edges_sum += cost
            union(v, u)
    return edges_sum


def DFS(G):
    n = len(G)
    num_visited = 0
    visited = [False] * n
    stack = [0]
    while len(stack) > 0:
        v = stack.pop()
        for w, _ in G[v]:
            if not visited[w]:
                num_visited += 1
                visited[w] = True
                stack.append(w)
    second_num_visited = 0
    second_visited = [False] * n
    for v in range(n):
        if not visited[v]:
            stack = [v]
            while len(stack) > 0:
                v = stack.pop()
                for w, _ in G[v]:
                    if not second_visited[w]:
                        second_num_visited += 1
                        second_visited[w] = True
                        stack.append(w)
            break
    return (num_visited == second_num_visited and num_visited == n - 1) or second_num_visited == 0


def beautree(G):
    if not DFS(G):
        return None
    vertexes = len(G) - 1
    G = convert_to_edge_list(G) # O(VE)
    n = len(G)
    G.sort(key = lambda edge: edge[2]) # O(E logE)
    find_unions = [Node(x) for x in range(n)] # O(E)
    for start_idx in range(n): # O(E * (E + E logV)) = O(E^2 + E^2 logV)
        reset_find_unions(find_unions) # O(E)
        min_beautree = kruskall_from(start_idx, G, vertexes, find_unions) # O(E logV)
        if min_beautree is not None:
            return min_beautree
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( beautree, all_tests = True )
