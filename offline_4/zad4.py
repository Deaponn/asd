# Bartosz Sajecki

# algorytm dziala na podstawie BFS, ktory mapuje graf na tablice odleglosci od s do obecnego wierzcholka
# gdy dojdziemy do wierzcholka t, przerywamy dzialanie funkcji, bo na pewno przeszlismy juz po jednej z najkrotszych sciezek
# sprawdzamy wszystkich sasiadow t, wybieramy tylko tych z najmniejsza odlegloscia do s
# jesli jest tylko jeden taki sasiad to usuniecie dowolnej krawedzi na sciezce s->t skutkuje
# usunieciem tej sciezki badz jej wydluzeniem
# jesli kilku sasiadow ma ta sama odleglosc do s, to o ile nie posiadaja wspolnego przodka to nie da sie
# wydluzyc najkrotszej sciezki usuwajac tylko jedna krawedz
# natomiast jesli maja wspolnego przodka to usuwamy ten tzw "choke point" (rys. 1)

# zlozonosc tego rozwiazania to O(V + E + N + L), gdzie:
# V to liczba wierzcholkow,
# E to liczba krawedzi w grafie,
# N to liczba sasiadow wierzcholka t,
# L to dlugosc sciezek z s do t ktore sa najkrotsze (jesli jest takich kilka)

# rys. 1
#        o-----o
#       /       \
#   s--o1--o--o--t
#       \       /
#        o-----o
#
# krawedz s--o1 to jest "choke point" - miejsce gdzie zbiegaja sie wszystkie najkrotsze sciezki


from zad4testy import runtests


def BFS(G, start, end, distances, parents):
    queue = []
    distances[start] = 0
    queue.append(start)
    while len(queue) > 0:
        current = queue.pop(0)
        distance = distances[current] + 1
        for neighbour in G[current]:
            if distances[neighbour] == -1:
                distances[neighbour] = distance
                parents[neighbour] = current
                queue.append(neighbour)
        if current == end:
            return end
        

def get_common_ancestor(vertexes, parents):
    n = len(vertexes)
    identical = False
    while not identical:
        identical = True
        vertexes[0] = parents[vertexes[0]]
        for idx in range(1, n):
            vertexes[idx] = parents[vertexes[idx]]
            if vertexes[idx - 1] != vertexes[idx]:
                identical = False
    return (parents[vertexes[0]], vertexes[0])

def longer( G, s, t ):
    # warunki brzegowe
    if len(G[t]) == 0 or len(G[s]) == 0:
        return None
    if len(G[t]) == 1:
        return (G[t][0], t)
    if len(G[s]) == 1:
        return (s, G[s][0])
    n = len(G)

    distances = [-1 for _ in range(n)]
    parents = [-1 for _ in range(n)]
    BFS(G, s, t, distances, parents)

    min_distance_vertex = [G[t][0]]
    min_distance = distances[min_distance_vertex[0]]

    for idx in range(1, len(G[t])):
        current_vertex = G[t][idx]
        current_distance = distances[current_vertex]
        if min_distance == current_distance:
            min_distance_vertex.append(current_vertex)
        if min_distance > current_distance:
            min_distance_vertex = [current_vertex]
            min_distance = current_distance

    if len(min_distance_vertex) > 1:
        common_ancestor = get_common_ancestor(min_distance_vertex, parents)
        if common_ancestor[0] <= 0:
            return None
        return common_ancestor

    return (min_distance_vertex[0], t)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )