# Bartosz Sajecki

# algorytm opiera sie na dwoch etapach podrozy Zlycerza:
# pierwszy etap to podroz do zamku ktory moze obrabowac (lub nie)
# drugi etap to podroz z juz obrabowanego zamku do zamku docelowego (zakladajac ze obrabowal nowy "startowy" zamek)
# poniewaz obrabowac moze tylko jeden zamek w czasie jednej podrozy, te dwa przeszukiwania grafu sa wystarczajace
# szukamy minimalnego kosztu przejazdu, czyli zakladajac dwie tablice dwuwymiarowe:
# P[i][j] - koszt dojechania do zamku j z zamku i
# R[i][j] - koszt dojechania do zamku j z zamku i po obrabowaniu zamku (zwiekszone wagi krawedzi)
# szukamy min(P[s][t], P[s][i] + R[i][t] - V[i]) dla kazdego i nalezacego do zbioru wierzcholkow

# zlozonosc tego rozwiazania to O(V^3)


from egz1Atesty import runtests


def list_to_matrix(G): # O(V^2)
    n = len(G)
    matrix = [[float("inf")] * n for _ in range(n)]
    for v in range(n):
        for w, cost in G[v]:
            matrix[v][w] = cost
    return matrix


def floyd_warshall(G): # O(V^3)
    n = len(G)
    output = [[float("inf") for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if x != y and G[x][y] != float("inf"):
                output[x][y] = G[x][y]
    for t in range(n):
        for x in range(n):
            for y in range(n):
                output[x][y] = min(output[x][y], output[x][t] + output[t][y])
    return output


def increase_costs(G, r): # O(V^2)
    n = len(G)
    for x in range(n):
        for y in range(n):
            G[x][y] = 2 * G[x][y] + r


def gold(G,V,s,t,r):
    n = len(G)
    G = list_to_matrix(G)
    peaceful_paths = floyd_warshall(G)
    increase_costs(G, r)
    violent_paths = floyd_warshall(G)
    for x in range(n):
        peaceful_paths[x][x] = 0
        violent_paths[x][x] = 0
    return min(peaceful_paths[s][t], min(peaceful_paths[s][i] + violent_paths[i][t] - V[i] for i in range(n)))

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )
